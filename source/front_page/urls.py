from django.urls import path

from front_page.views import (
    TaskDetailView, 
    RunCodeView, 
    SolutionListView, 
    SolutionDetailView,
    CommentListView,
)

app_name = "front_page"
urlpatterns = [
    path("task-of-day/", TaskDetailView.as_view(), name="task_of_day"),   
    path("run-code/", RunCodeView.as_view(), name="run_code"),   
    path("solution-list/", SolutionListView.as_view(), name="solution_list"),
    path("solution-list/<int:pk>/", SolutionDetailView.as_view(), name="solution_detail"),
    path("solution-list/<int:pk>/", SolutionDetailView.as_view(), name="solution_detail"),
    path("comment-list/", CommentListView.as_view(), name="comment_list"),

]
