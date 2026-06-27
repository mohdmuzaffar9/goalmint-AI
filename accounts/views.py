from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import RegisterForm, LoginForm
from .models import Profile 
from goals.models import Goal
from tasks.models import Task
from django.contrib.auth.decorators import login_required


def register_view(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']

            username = email

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )
            

            messages.success(
                request,
                "Account created successfully. Please login."
            )

            return redirect('login')

    else:

        form = RegisterForm()

    return render(
        request,
        'accounts/register.html',
        {'form': form}
    )


def login_view(request):

    if request.method == "POST":

        form = LoginForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(
                request,
                username=email,
                password=password
            )

            if user is not None:

                login(request, user)

                return redirect('dashboard')

            messages.error(
                request,
                "Invalid email or password."
            )

    else:

        form = LoginForm()

    return render(
        request,
        'accounts/login.html',
        {'form': form}
    )


def logout_view(request):

    logout(request)

    return redirect('login')

@login_required
def profile_view(request):

    user = request.user

    profile = user.profile

    goals = Goal.objects.filter(
        user=user
    )

    tasks = Task.objects.filter(
        user=user
    )

    total_goals = goals.count()

    active_goals = goals.filter(
        status="Active"
    ).count()

    completed_goals = goals.filter(
        status="Completed"
    ).count()

    completed_tasks = tasks.filter(
        status="Completed"
    ).count()

    overall_progress = 0

    if total_goals > 0:

        overall_progress = int(
            sum(goal.progress for goal in goals) / total_goals
        )

    context = {

        "profile": profile,

        "total_goals": total_goals,

        "active_goals": active_goals,

        "completed_goals": completed_goals,

        "completed_tasks": completed_tasks,

        "overall_progress": overall_progress,

    }

    return render(
        request,
        "accounts/profile.html",
        context
    )