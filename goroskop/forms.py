from django import forms
from .models import UserProfile, Sex, Country, Compatibility
from django.contrib.auth import (
    authenticate,
    get_user_model

)

User = get_user_model()


class UserLoginForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField()

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]
        help_texts = {
            'username': None,
        }


class UserSex(forms.ModelForm):
    sex = forms.CharField()

    class Meta:
        model = Sex
        fields = ['sex']


class UserProfileRegisterForm(forms.ModelForm):
    birthdate = forms.CharField()
    hobby = forms.CharField()

    class Meta:
        model = UserProfile
        fields = [
            'name',
            'birthdate',
            'hobby',
            'avatar'
        ]


class UserCountry(forms.ModelForm):
    country = forms.CharField()

    class Meta:
        model = Country
        fields = ['country']


class CompatibilityForm(forms.ModelForm):
    partnersex = forms.CharField()
    zodiac = forms.CharField()
    class Meta:
        model = Compatibility
        fields =[
            'partnersex'
            ]

