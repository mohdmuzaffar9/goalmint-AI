from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from goals.models import Roadmap


@login_required
def generate_tasks_view(request, roadmap_id):

    roadmap = Roadmap.objects.get(
        id=roadmap_id
    )

    return render(
        request,
        'tasks/preview_tasks.html',
        {
            'roadmap': roadmap
        }
    )


@login_required
def task_list_view(request, roadmap_id):

    roadmap = Roadmap.objects.get(
        id=roadmap_id
    )

    return render(
        request,
        'tasks/task_list.html',
        {
            'roadmap': roadmap
        }
    )