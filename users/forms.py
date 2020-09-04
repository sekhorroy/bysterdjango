from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MtAdminUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = MtAdminUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = MtAdminUser
        fields = ('email',)
