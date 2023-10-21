from django.views.generic import DetailView
from account.models import User


class UserDetailView(DetailView):
    model = User