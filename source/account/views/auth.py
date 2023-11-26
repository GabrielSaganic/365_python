from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from account.forms import SignUpForm

class CustomLoginView(LoginView):
    template_name = "login.html"


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("account:login")


class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy("account:login")
        