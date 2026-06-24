from django.urls import path

from . import views

urlpatterns = [
    path('create/',views.create_goal_view,name='create_goal'),
    path('my-goals/',views.my_goals_view,name='my_goals'),
    path('<int:goal_id>/',views.goal_detail_view,name='goal_detail'),
    path('<int:goal_id>/roadmap/',views.roadmap_view,name='roadmap'),
    path('preview-roadmap/',views.preview_roadmap_view,name='preview_roadmap'),
    path('accept-roadmap/',views.accept_roadmap_view,name='accept_roadmap'),
]