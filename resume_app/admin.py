from django.contrib import admin
from .models import Resume


class ResumeAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone_number', 'education', 'experience', 'skills', 'additional_information']
    actions = ['copy_resume']

    def copy_resume(self, request, queryset):
        for resume in queryset:
            resume.pk = None
            resume.save()

    copy_resume.short_description = "Copy selected resumes"


admin.site.register(Resume, ResumeAdmin)
