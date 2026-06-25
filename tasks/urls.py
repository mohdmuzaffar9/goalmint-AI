from django.urls import path
from . import views

urlpatterns = [

    path('generate/<int:roadmap_id>/',views.generate_tasks_view,name='generate_tasks'),

    path('accept/<int:roadmap_id>/',views.accept_tasks_view,name='accept_tasks'),

    path('<int:roadmap_id>/',views.task_list_view,name='task_list'),

]