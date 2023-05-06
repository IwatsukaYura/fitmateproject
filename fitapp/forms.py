from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class SignupForm(UserCreationForm):
    
    email = forms.EmailField(
        max_length=254,
        help_text='必須 有効なメールアドレスを入力してください。',
        label='Eメールアドレス'
    )

    gender = forms.BooleanField(
    )

    age = forms.CharField(
        max_length=20
    )

    height = forms.FloatField()
    weight = forms.FloatField()
    target_weight = forms.FloatField()

    class Meta:
        model = CustomUser
        fields = [CustomUser.USERNAME_FIELD] + CustomUser.REQUIRED_FIELDS

class LoginForm(AuthenticationForm):
    pass