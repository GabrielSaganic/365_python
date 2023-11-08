from django.urls import path

from front_page.views import TaskDetailView, RunCodeView, SolutionListView


urlpatterns = [
    path("task-of-day/", TaskDetailView.as_view(), name="task_of_day"),   
    path("run-code/", RunCodeView.as_view(), name="run_code"),   
    path("solution-list/", SolutionListView.as_view(), name="solution_list"),
]
