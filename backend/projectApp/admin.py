from django.contrib import admin
from projectApp.models import Project, Tag, Status

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'status',
        'is_active',
        'date_of_updated',
        'date_of_end',
        'date_of_created'
    )
    list_display_links = ('title',)
    list_filter = ('status', 'is_active')
    readonly_fields = ('date_of_updated', 'date_of_created')
    fields = (
        'title',
        'slug',
        'preview',
        ('short_description', 'full_description'),
        'number_of_people',
        'is_active',
        ('date_of_updated', 'date_of_end', 'date_of_created')
    )
    save_on_top = True

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    list_display_links = ('title',)

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title',)
