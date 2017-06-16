from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'username',
                'class': 'login'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'password',
                'class': 'login'
            }
        ),
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        user = authenticate(
            username=username,
            password=password,
        )
        if user is not None:
            self.cleaned_data['user'] = user
        else:
            raise forms.ValidationError(
                'Login Credentials not valid'
            )  # 이 오류는 기본적으로 is_valid() 값이 False가 되도록 내부적으로 설정이 되어 있음.from
        return self.cleaned_data
