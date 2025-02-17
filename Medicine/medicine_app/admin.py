from django.contrib import admin
from .models import *


class MPiconsInlines(admin.TabularInline):
    model = MainPageIcons
    extra = 0


class QuestionMPInlines(admin.TabularInline):
    model = QuestionsMP
    extra = 0

class Personal(admin.TabularInline):
    model = MedlinkPersonal
    extra = 0

class AdminMP(admin.ModelAdmin):
    inlines = [MPiconsInlines,QuestionMPInlines,Personal]


admin.site.register(MainPage, AdminMP)
admin.site.register(ConsultZapis)

