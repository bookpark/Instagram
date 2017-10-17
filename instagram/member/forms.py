from django import forms
from django.contrib.auth import get_user_model, login, authenticate

User = get_user_model()


class SignupForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    # clean_<field_name>
    def clean_username(self):
        data = self.cleaned_data['username']
        if User.objects.filter(username=data).exists():
            raise forms.ValidationError(f'Username {data} already exists.')
        return data


class SigninForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    # 초기화 함수 __init__, self.user 사용 위해 정의
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        self.user = authenticate(
            username=username,
            password=password,
        )
        if not self.user:
            raise forms.ValidationError('Login failed')
        else:
            # 동적으로 작동
            setattr(self, 'signin', self._signin)

    def _signin(self, request):
        """

        :param request: django.auth.login()에 주어질 HttpRequest 객체
        :return:
        """
        if self.user:
            login(request, self.user)
