from django.urls import path

from account.views import UserDetailView

urlpatterns = [
    path("profile/<int:pk>/", UserDetailView.as_view(), name="user_detail"),
]
