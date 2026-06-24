from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    STUDY_TIME_CHOICES = [
        ('Morning', 'Morning'),
        ('Afternoon', 'Afternoon'),
        ('Evening', 'Evening'),
        ('Night', 'Night'),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        blank=True,
        null=True
    )

    bio = models.TextField(
        max_length=500,
        blank=True
    )

    timezone = models.CharField(
        max_length=100,
        default='Asia/Kolkata'
    )

    daily_available_hours = models.PositiveIntegerField(
        default=2
    )

    preferred_study_time = models.CharField(
        max_length=20,
        choices=STUDY_TIME_CHOICES,
        default='Evening'
    )

    notification_enabled = models.BooleanField(
        default=True
    )

    email_notifications = models.BooleanField(
        default=True
    )

    google_calendar_connected = models.BooleanField(
        default=False
    )

    current_streak = models.PositiveIntegerField(
        default=0
    )

    longest_streak = models.PositiveIntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.user.username} Profile"