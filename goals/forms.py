from django import forms

from .models import Goal


class GoalForm(forms.ModelForm):

    class Meta:

        model = Goal

        fields = [
            'title',
            'description',
            'goal_type',
            'goal_category',
            'priority',
            'target_date',
            'daily_hours',
        ]

        widgets = {
            'target_date': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            )
        }

