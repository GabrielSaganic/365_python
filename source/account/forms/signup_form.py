from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

class SignUpForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username", "email", "avatar")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["avatar"].widget.attrs["id"] = "imageUpload"
