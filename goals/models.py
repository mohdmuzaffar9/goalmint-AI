from django.db import models
from django.contrib.auth.models import User

from datetime import date


class Goal(models.Model):

    GOAL_TYPE_CHOICES = [
        ('Long Term', 'Long Term'),
        ('Short Term', 'Short Term'),
    ]

    GOAL_CATEGORY_CHOICES = [
        ('Career', 'Career'),
        ('JEE', 'JEE'),
        ('NEET', 'NEET'),
        ('Government Exam', 'Government Exam'),
        ('Skill Learning', 'Skill Learning'),
        ('Fitness', 'Fitness'),
        ('Custom', 'Custom'),
    ]

    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Paused', 'Paused'),
        ('Completed', 'Completed'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='goals'
    )

    title = models.CharField(
        max_length=255
    )

    description = models.TextField()

    goal_type = models.CharField(
        max_length=20,
        choices=GOAL_TYPE_CHOICES,
        default='Long Term'
    )

    goal_category = models.CharField(
        max_length=50,
        choices=GOAL_CATEGORY_CHOICES,
        default='Custom'
    )

    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='Medium'
    )

    target_date = models.DateField()

    daily_hours = models.PositiveIntegerField(
        default=2
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Active'
    )

    success_probability = models.PositiveIntegerField(
        default=0
    )

    is_ai_generated = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    @property
    def risk_level(self):

        if self.status == 'Completed':
            return 'Completed'
        
        if self.status == 'Paused':
            return 'Paused' 
        
        days_left = (
            self.target_date - date.today()
        ).days

        if self.goal_type == 'Short Term':

            if days_left <= 3:
                return 'High Risk'

            elif days_left <= 7:
                return 'Medium Risk'

            return 'Low Risk'

        else:  # Long Term

            if days_left <= 15:
                return 'High Risk'

            elif days_left <= 30:
                return 'Medium Risk'

            return 'Low Risk'


    def __str__(self):
        return self.title
    
    @property
    def progress(self):

        total_tasks = self.tasks.count()

        if total_tasks == 0:
            return 0

        completed_tasks = self.tasks.filter(
            status="Completed"
        ).count()

        return int(
            (completed_tasks / total_tasks) * 100
        )
    
    @property
    def completed_tasks(self):

        return self.tasks.filter(
            status="Completed"
        ).count()


    @property
    def total_tasks(self):

        return self.tasks.count()


    @property
    def completed_roadmaps(self):

        completed = 0

        for roadmap in self.roadmaps.all():

            if roadmap.status == "Completed":
                completed += 1

        return completed


    @property
    def total_roadmaps(self):

        return self.roadmaps.count()


class Roadmap(models.Model):

    goal = models.ForeignKey(
        Goal,
        on_delete=models.CASCADE,
        related_name='roadmaps'
    )

    title = models.CharField(
        max_length=255
    )

    description = models.TextField()

    order = models.PositiveIntegerField(
        default=1
    )

    estimated_days = models.PositiveIntegerField(
        default=7
    )

    completed = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.goal.title} - {self.title}"
    
    @property
    def status(self):

        total_tasks = self.tasks.count()

        if total_tasks == 0:
            return "Not Started"

        completed_tasks = self.tasks.filter(
            status="Completed"
        ).count()

        if completed_tasks == 0:
            return "Not Started"

        if completed_tasks == total_tasks:
            return "Completed"

        return "In Progress"