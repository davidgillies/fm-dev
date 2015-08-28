from django.contrib import admin
from django.core.urlresolvers import reverse
from fenland_models.models import Surgery, Volunteer, Status, Appointment, AuditLog
import arrow
from django.contrib.admin.models import LogEntry, DELETION
from django.utils.html import escape
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class VolunteerResource(resources.ModelResource):

    class Meta:
        model = Volunteer

class AppointmentInline(admin.TabularInline):
    model = Appointment
    fields = ('appt_date', 'appt_time', 'test_site')
    extra = 0

class SurgeryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Surgery, SurgeryAdmin)


class VolunteerAdmin(ImportExportModelAdmin):
    ## change list view
    resource_class = VolunteerResource
    list_display = ('surname', 'forenames', 'town', 'postcode',)
    list_filter = ('town', 'surgeries__full_name')
    date_hierarchy = 'dob'
    search_fields = ('surname', 'forenames', 'town', 'postcode',
                     'surgeries__full_name')

    ## change form view
    inlines = [AppointmentInline, ]
    readonly_fields = ('modified', 'modified_by')
    fieldsets = (
        (None, {'fields': (('surname', 'forenames'),
                           ('initials', 'dob'),
                           ('title', 'sex'))}),
        ('Address', {'classes': ('collapse',),
                     'fields': (('addr1', 'home_tel'), ('addr2', 'work_tel'),
                                ('town', 'mobile'), ('county', 'email'),
                                'postcode')}),
        ('Details', {'classes': ('collapse', 'extrapretty'),
                     'description': 'Extra <b>details</b>',
                     'fields': (('nhs_no', 'surgeries'),
                                ('modified', 'modified_by'),
                                ('diabetes_diagnosed', 'moved_away'),)}),
    )

    def save_model(self, request, obj, form, change):
        obj.modified_by = request.user.get_username()
        obj.modified = str(arrow.now()).replace('+01:00', '')
        obj.save()

admin.site.register(Volunteer, VolunteerAdmin)


class AppointmentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Appointment, AppointmentAdmin)


class AuditLogAdmin(admin.ModelAdmin):
    pass

admin.site.register(AuditLog, AuditLogAdmin)


class StatusAdmin(admin.ModelAdmin):
    pass

admin.site.register(Status, StatusAdmin)


class LogEntryAdmin(admin.ModelAdmin):

    date_hierarchy = 'action_time'

    # readonly_fields = LogEntry._meta.get_all_field_names()

    list_filter = [
        'user',
        'content_type',
        'action_flag'
    ]

    search_fields = [
        'object_repr',
        'change_message'
    ]

    list_display = [
        'action_time',
        'user',
        'content_type',
        'object_link',
        'action_flag',
        'change_message',
    ]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser and request.method != 'POST'

    def has_delete_permission(self, request, obj=None):
        return False

    def object_link(self, obj):
        if obj.action_flag == DELETION:
            link = escape(obj.object_repr)
        else:
            ct = obj.content_type
            link = u'<a href="%s">%s</a>' % (
                reverse('admin:%s_%s_change' % (ct.app_label, ct.model), args=[obj.object_id]),
                escape(obj.object_repr),
            )
        return link
    object_link.allow_tags = True
    # object_link.admin_order_field = 'object_repr'
    object_link.short_description = u'object'

    def queryset(self, request):
        return super(LogEntryAdmin, self).queryset(request) \
            .prefetch_related('content_type')


admin.site.register(LogEntry, LogEntryAdmin)