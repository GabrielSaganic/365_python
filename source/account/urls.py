from django.urls import path

from account.views import UserDetailView, LoginView, LogoutView, SignUpView

app_name = "account"
urlpatterns = [
    path("profile/<int:pk>/", UserDetailView.as_view(), name="user_detail"),
    path("login/", LoginView.as_view(next_page="front_page:task_of_day"), name="login"),
    path("logout/", LogoutView.as_view(next_page="front_page:task_of_day"), name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
]
