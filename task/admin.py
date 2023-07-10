from django.contrib import admin

from .models import *

class TaskStateInline(admin.TabularInline):
    model = TaskState
    extra = 1

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    inlines = [TaskStateInline]