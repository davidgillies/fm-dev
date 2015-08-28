from django.contrib import admin
from fenland_models.models import Surgery, Volunteer, Status, Appointment, AuditLog
import arrow


class AppointmentInline(admin.TabularInline):
    model = Appointment
    fields = ('appt_date', 'appt_time', 'test_site')
    extra = 0

class SurgeryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Surgery, SurgeryAdmin)


class VolunteerAdmin(admin.ModelAdmin):
    ## change list view
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