from urllib import request

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import GoalForm, GoalUpdateForm
from .models import Goal, Roadmap
from datetime import datetime

from ai_engine.services import generate_roadmap


@login_required
def create_goal_view(request):

    if request.method == 'POST':

        form = GoalForm(request.POST)

        if form.is_valid():

           goal_data = form.cleaned_data.copy()

           goal_data['target_date'] = str(
           goal_data['target_date']
          )

           request.session['goal_data'] = goal_data

           return redirect('preview_roadmap')

        else:

            print(form.errors)

    else:

        form = GoalForm()

        return render(
        request,
        'goals/create_goal.html',
        {
            'form': form
        }
    )


@login_required
def my_goals_view(request):

    goals = Goal.objects.filter(
        user=request.user
    ).order_by("-created_at")

    # Search
    search = request.GET.get("search")

    if search:
        goals = goals.filter(
            title__icontains=search
        )

    goal_type = request.GET.get("goal_type")

    if goal_type:
        goals = goals.filter(
            goal_type=goal_type
        )    

    # Status Filter
    status = request.GET.get("status")

    if status:
        goals = goals.filter(
            status=status
        )

    # Priority Filter
    priority = request.GET.get("priority")

    if priority:
        goals = goals.filter(
            priority=priority
        )

    return render(
        request,
        "goals/my_goals.html",
        {
            "goals": goals,
        }
    )

@login_required
def goal_detail_view(request, goal_id):

    goal = Goal.objects.get(
        id=goal_id,
        user=request.user
    )

    return render(
        request,
        'goals/goal_detail.html',
        {
            'goal': goal
        }
    )

@login_required
def accept_roadmap_view(request):

    goal_data = request.session.get('goal_data')

    if not goal_data:
        return redirect('create_goal')

    goal = Goal.objects.create(
        user=request.user,
        title=goal_data['title'],
        description=goal_data['description'],
        goal_type=goal_data['goal_type'],
        goal_category=goal_data['goal_category'],
        priority=goal_data['priority'],
        target_date=datetime.strptime(
            goal_data['target_date'],
            '%Y-%m-%d'
        ).date(),
        daily_hours=goal_data['daily_hours'],
    )

    roadmap_steps = request.session.get(
        'roadmap_steps',
        []
    )

    for index, step in enumerate(
        roadmap_steps,
        start=1
    ):

        Roadmap.objects.create(
            goal=goal,
            title=step,
            description=step,
            order=index
        )

    del request.session['goal_data']

    if 'roadmap_steps' in request.session:
        del request.session['roadmap_steps']

    return redirect('my_goals')

@login_required
def preview_roadmap_view(request):

    goal_data = request.session.get(
        'goal_data'
    )

    if not goal_data:
        return redirect('create_goal')
    
    if request.method == 'POST':
        edited_steps = []

        for key, value in request.POST.items():
            if key.startswith('phase_'):
                edited_steps.append(
                    value.strip()
                )

        request.session[
            'roadmap_steps'
        ] = edited_steps

        return redirect(
            'preview_roadmap'
        )

    if 'roadmap_steps' in request.session:

        roadmap_steps = request.session[
            'roadmap_steps'
        ]

    else:

        try:

            roadmap_text = generate_roadmap(
                goal_data
            )

            roadmap_steps = [
                step.strip()
                for step in roadmap_text.split('\n')
                if step.strip()
            ]

        except Exception:

            roadmap_steps = [
                "Learn Fundamentals",
                "Learn Core Skills",
                "Build Projects",
                "Advanced Concepts",
                "Portfolio Building",
                "Interview Preparation",
            ]

        request.session[
            'roadmap_steps'
        ] = roadmap_steps

    return render(
        request,
        'goals/preview_roadmap.html',
        {
            'goal_data': goal_data,
            'roadmap_steps': roadmap_steps,
        }
    )
@login_required
def roadmap_view(request, goal_id):

    goal = Goal.objects.get(
        id=goal_id,
        user=request.user
    )

    roadmaps = Roadmap.objects.filter(
        goal=goal
    ).order_by('order')

    return render(
        request,
        'goals/roadmap.html',
        {
            'goal': goal,
            'roadmaps': roadmaps
        }
    )

@login_required
def edit_goal_view(request, goal_id):

    goal = Goal.objects.get(
        id=goal_id,
        user=request.user
    )

    if request.method == 'POST':

        form = GoalUpdateForm(
            request.POST,
            instance=goal
        )

        if form.is_valid():

            form.save()

            return redirect(
                'goal_detail',
                goal_id=goal.id
            )

    else:

        form = GoalUpdateForm(
            instance=goal
        )

    return render(
        request,
        'goals/edit_goal.html',
        {
            'form': form,
            'goal': goal
        }
    )

@login_required
def delete_goal_view(request, goal_id):

    goal = Goal.objects.get(
        id=goal_id,
        user=request.user
    )

    goal.delete()

    return redirect(
        'my_goals'
    )