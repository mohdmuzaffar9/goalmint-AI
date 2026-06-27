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

            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "e.g. Become AI Backend Developer"
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Describe your goal in detail..."
                }
            ),

            "goal_type": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "goal_category": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "priority": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "target_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date"
                }
            ),

            "daily_hours": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 1,
                    "max": 24
                }
            ),
        }
        
class GoalUpdateForm(forms.ModelForm):

    class Meta:

        model = Goal

        fields = [
            'priority',
            'status',
            'daily_hours',
            'target_date',
        ]

        widgets = {
            'target_date': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            )
        }

class GoalUpdateForm(forms.ModelForm):

    class Meta:

        model = Goal

        fields = [
            "priority",
            "status",
            "daily_hours",
            "target_date",
        ]

        widgets = {

            "priority": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "status": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "daily_hours": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 1,
                    "max": 24
                }
            ),

            "target_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date"
                }
            ),

        }        

