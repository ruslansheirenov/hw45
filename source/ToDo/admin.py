from django.contrib import admin

from ToDo.models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status']
    list_filter = ['title']
    search_field = ['title', 'description']
    fields = ['title', 'status', 'description', 'date_of_completion']

admin.site.register(Task, TaskAdmin)