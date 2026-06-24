from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'daily_available_hours',
        'preferred_study_time',
        'current_streak',
        'longest_streak',
        'google_calendar_connected',
        'created_at',
    )

    list_filter = (
        'preferred_study_time',
        'google_calendar_connected',
        'notification_enabled',
        'email_notifications',
    )

    search_fields = (
        'user__username',
        'user__email',
        'user__first_name',
        'user__last_name',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
    )