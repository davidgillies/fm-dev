from django.contrib import admin
from fenland_models.models import Surgery, Volunteer, Status, Appointment, AuditLog


class SurgeryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Surgery, SurgeryAdmin)


class VolunteerAdmin(admin.ModelAdmin):
    pass

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