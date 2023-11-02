from django.urls import path

from front_page.views import TaskDetailView, RunCodeView


urlpatterns = [
    path("task-of-day/", TaskDetailView.as_view(), name="task_of_day"),   
    path("run-code/", RunCodeView.as_view(), name="run_code"),   
    
]
