from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import goals
from goals.models import Goal
from tasks.models import Task


@login_required
def dashboard_view(request):

    goals = Goal.objects.filter(
        user=request.user
    )

    tasks = Task.objects.filter(
        user=request.user
    )

    ai_insights = []

    if goals.count() == 0:

        ai_insights.append(
            "🎯 Create your first goal to start your AI journey."
        )

    else:

        if sum(1 for goal in goals if goal.risk_level == "High Risk") > 0:

            ai_insights.append(
                "⚠️ You have high-risk goals. Review deadlines today."
            )

        if tasks.filter(status="Completed").count() >= 10:

            ai_insights.append(
                "🔥 Great job! You're maintaining good consistency."
            )

        if goals.filter(status="Completed").count() > 0:

            ai_insights.append(
                "🏆 Congratulations! Keep completing more goals."
            )

        if tasks.filter(status="Completed").count() == 0:

            ai_insights.append(
                "📚 Complete your first task to start building progress."
            )

        if len(ai_insights) < 4:

            ai_insights.append(
                "💡 Focus on one goal at a time for better productivity."
            )

        if len(ai_insights) < 4:

            ai_insights.append(
                "🚀 Update your task status regularly to track progress."
            )

    context = {

        "total_goals": goals.count(),

        "active_goals": goals.filter(
            status="Active"
        ).count(),

        "completed_goals": goals.filter(
            status="Completed"
        ).count(),

        "high_risk_goals": sum(
            1
            for goal in goals
            if goal.risk_level == "High Risk"
        ),

        "completed_tasks": tasks.filter(
            status="Completed"
        ).count(),

        "recent_goals": goals.order_by(
            "-created_at"
        )[:5],

        "ai_insights": ai_insights,

    }

    return render(
        request,
        "core/dashboard.html",
        context
    )

@login_required
def ai_insights_view(request):

    goals = Goal.objects.filter(
        user=request.user
    )

    tasks = Task.objects.filter(
        user=request.user
    )

    high_risk_goals = [
        goal
        for goal in goals
        if goal.risk_level == "High Risk"
    ]

    context = {

        "total_goals": goals.count(),

        "completed_goals": goals.filter(
            status="Completed"
        ).count(),

        "active_goals": goals.filter(
            status="Active"
        ).count(),

        "completed_tasks": tasks.filter(
            status="Completed"
        ).count(),

        "high_risk_goals": high_risk_goals,

        "goals": goals,

    }

    return render(
        request,
        "core/ai_insights.html",
        context
    )