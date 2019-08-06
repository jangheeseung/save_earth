from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, ReadOnlyPasswordHashField
from django.utils.translation import ugettext_lazy as _

from .models import User, UserManager

class UserCreationForm(forms.ModelForm):
    # 사용자 생성 폼
    
    email = forms.EmailField(
        label=_('Email'),
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Email address'),
                'required': 'True',
            }
        )
    )
    name = forms.CharField(
        label=_('name'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('User name'),
                'required': 'True',
            }
        )
    )
    password1 = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Password'),
                'required': 'True',
            }
        )
    )
    password2 = forms.CharField(
        label=_('Password confirmation'),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Password confirmation'),
                'required': 'True',
            }
        )
    )    
    address = forms.CharField(
        label=_('Address'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Address'),
                'required': 'True',
            }
        )
    )
    tel = forms.CharField(
        label=_('Phone number'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Phone number'),
                'required': 'True',
            }
        )
    )

    class Meta:
        model = User
        fields = ('email', 'name', 'password1', 'password2', 'address', 'tel') #User모델에 정의된 필드 중 입력양식으로 받을 필드들

    def clean_password2(self):
        # 두 비밀번호 입력 일치 확인
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    # def save(self, commit=True):
    #     # Save the provided password in hashed format
    #     user = super(UserCreationForm, self).save(commit=False)
    #     user.email = UserManager.normalize_email(self.cleaned_data['userId'])
    #     user.set_password(self.cleaned_data["userPassword1"])
    #     if commit:
    #         user.save()
    #     return user


class UserChangeForm(forms.ModelForm):
    # 비밀번호 변경 폼
    password = ReadOnlyPasswordHashField(
        label=_('Password')
    )

    class Meta:
        model = User
        # fields = ('email', 'password', 'last_name', 'first_name', 'is_active', 'is_superuser')
        fields = ('email', 'password', 'name', 'is_superuser')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class UserLoginForm(AuthenticationForm):
    #로그인 폼
    email = forms.CharField(
        max_length=45,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Email address'),
                'required': 'True',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Password'),
                'required': 'True',
            }
        )
    )
    class Meta:
        model = User
        fields = ('email', 'password1')