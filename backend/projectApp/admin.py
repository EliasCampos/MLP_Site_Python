from django.contrib import admin
from projectApp.models import Project, Tag, Status


class ProjectAdmin(admin.ModelAdmin):
    pass


class TagAdmin(admin.ModelAdmin):
    pass


class StatusAdmin(admin.ModelAdmin):
    pass