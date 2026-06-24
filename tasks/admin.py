from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'user',
        'goal',
        'priority',
        'status',
        'completion_percentage',
        'due_date',
    )

    list_filter = (
        'priority',
        'status',
        'is_ai_generated',
    )

    search_fields = (
        'title',
        'description',
        'user__email',
        'goal__title',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
        'completed_at',
    )

    ordering = (
        '-created_at',
    )