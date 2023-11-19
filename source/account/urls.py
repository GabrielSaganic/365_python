from django.urls import path

from account.views import UserDetailView, LoginView, LogoutView, SignUpView

urlpatterns = [
    path("profile/<int:pk>/", UserDetailView.as_view(), name="user_detail"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
