

from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

class CreateUserForm(UserCreationForm):
    class Meta:

        model = User
        fields = ["username",'password1',"password2"]




class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']




