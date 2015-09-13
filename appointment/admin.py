from django.contrib import admin

from .models import *


class AppointmentInline(admin.TabularInline):
    model = Appointment
    readonly_fields = ['doctor', 'appointment_time', 'patient']

class DoctorAdmin(admin.ModelAdmin):
    list_display = ["name", "available", "specialization"]
    inlines = [
            AppointmentInline,
            ]

class SpecializationAdmin(admin.ModelAdmin):
    list_display = ["name"]

admin.site.register(Specialization, SpecializationAdmin)
admin.site.register(Doctor, DoctorAdmin)
