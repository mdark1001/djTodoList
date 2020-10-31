from django.contrib import admin

# Register your models here.
from .models import Tags, Task


@admin.register(Tags)
class TagAdminModel(admin.ModelAdmin):

    display_list = ['name', 'color']


@admin.register(Task)
class TaskAdminMoidel(admin.ModelAdmin):
    list_display = ['name', 'user', 'first_name','tag','state', 'created']
    search_fields = [
        'name',
        'user__username',
        'user__email',
    ]
    list_filter = [
        'created',
        'tag',
        'state',
    ]
