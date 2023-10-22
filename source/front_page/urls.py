from django.urls import path

from front_page.views import TaskDetailView


urlpatterns = [
    path("task-of-day/", TaskDetailView.as_view(), name="task_of_day"),   
]
