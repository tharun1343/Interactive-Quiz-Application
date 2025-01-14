from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,quiz,QuesModel
from django.db import models


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username","email","password1","password2","first_name","last_name")

    def save(self,commit=True):
        user = super(RegisterForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','address','contact','alt_contact','Date_Of_Birth']

class addQues(forms.ModelForm):
    class Meta:
        model = QuesModel
        fields = "__all__"

class quizform(forms.ModelForm):
    class Meta:
        model = quiz
        fields = ['quiz_name'] 