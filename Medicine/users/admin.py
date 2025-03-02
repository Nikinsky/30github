from django.contrib import admin

from .models import *

admin.site.register(SpecialDoctor)

class EducationInline(admin.TabularInline):
    model = Education
    extra = 0

class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 0

class WorkTimeInlines(admin.TabularInline):
    model = WorkTime
    extra = 0


class DocktorAdmin(admin.ModelAdmin):
    inlines = [EducationInline,ExperienceInline, WorkTimeInlines]


admin.site.register(Doctor, DocktorAdmin)
admin.site.register(Patient)
admin.site.register(Feedback)

