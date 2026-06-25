from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from goals.models import Roadmap
from ai_engine.services import generate_tasks
from tasks.models import Task


@login_required
def generate_tasks_view(request, roadmap_id):

    roadmap = Roadmap.objects.get(
        id=roadmap_id
    )

    existing_tasks = Task.objects.filter(
    roadmap=roadmap
    )

    if existing_tasks.exists():
        return redirect(
            'task_list',
            roadmap_id=roadmap.id
        )

    session_key = f"tasks_{roadmap_id}"

    if session_key in request.session:

        task_steps = request.session[
            session_key
        ]

    else:

        try:

            task_text = generate_tasks(
                roadmap.goal.title,
                roadmap.title
            )

            task_steps = [
                task.strip()
                for task in task_text.split('\n')
                if task.strip()
            ]

        except Exception:

            task_steps = [
                "Study Concepts",
                "Watch Tutorials",
                "Practice Exercises",
                "Build Mini Project",
                "Review Progress",
                "Complete Assessment",
            ]

        request.session[
            session_key
        ] = task_steps

    return render(
        request,
        'tasks/preview_tasks.html',
        {
            'roadmap': roadmap,
            'task_steps': task_steps,
        }
    )

@login_required
def task_list_view(request, roadmap_id):

    roadmap = Roadmap.objects.get(
        id=roadmap_id
    )

    tasks = Task.objects.filter(
        roadmap=roadmap
    )

    return render(
        request,
        'tasks/task_list.html',
        {
            'roadmap': roadmap,
            'tasks': tasks
        }
    )

@login_required
def accept_tasks_view(request, roadmap_id):

    roadmap = Roadmap.objects.get(
        id=roadmap_id
    )

    existing_tasks = Task.objects.filter(
    roadmap=roadmap
    )

    if existing_tasks.exists():
        return redirect(
            'task_list',
            roadmap_id=roadmap.id
    )

    session_key = f"tasks_{roadmap_id}"

    task_steps = request.session.get(
        session_key,
        []
    )

    for task in task_steps:

        Task.objects.create(
            user=request.user,
            goal=roadmap.goal,
            roadmap=roadmap,
            title=task
        )

    if session_key in request.session:
        del request.session[session_key]

    return redirect(
        'task_list',
        roadmap_id=roadmap.id
    )