from django.contrib import admin
from .models import Goal, Roadmap


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'user',
        'goal_type',
        'goal_category',
        'status',
        'success_probability',
        'target_date',
    )

    list_filter = (
        'goal_type',
        'goal_category',
        'status',
    )

    search_fields = (
        'title',
        'user__email',
        'user__first_name',
        'user__last_name',
    )


@admin.register(Roadmap)
class RoadmapAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'goal',
        'order',
        'estimated_days',
        'completed',
    )

    list_filter = (
        'completed',
    )

    search_fields = (
        'title',
        'goal__title',
    )