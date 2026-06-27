from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('ai-insights/',views.ai_insights_view,name='ai_insights'),
]