from django.contrib.auth.forms import UserCreationForm
from user.models import User

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','nickname','email','age','sex']