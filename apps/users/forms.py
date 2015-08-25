from django import forms
from django.contrib.auth.models import User

from .models import UserProfile
# from .helpers import UserHelper, UserProfileHelper


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    # def __init__(self, *args, **kwargs):
    #     super(UserForm, self).__init__(*args, **kwargs)
    #     self.helper = UserHelper()

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(UserProfileForm, self).__init__(*args, **kwargs)
    #     self.helper = UserProfileHelper()

    class Meta:
        model = UserProfile
        fields = ('twitter', 'facebook', 'image')

class LoginForm(forms.Form):
    username = forms.EmailField(
        label='username',
        widget=forms.TextInput()
    )
    password = forms.CharField(
        max_length=100,
        label='password',
        widget=forms.PasswordInput()
    )