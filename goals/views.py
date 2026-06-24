from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import GoalForm
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
    ).order_by('-created_at')

    return render(
        request,
        'goals/my_goals.html',
        {
            'goals': goals
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

    roadmap_text = generate_roadmap(
        goal_data
    )

    roadmap_steps = [
        step.strip()
        for step in roadmap_text.split('\n')
        if step.strip()
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