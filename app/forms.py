from django import forms
from django.contrib.auth.models import User
from .models import *


class SignInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class DetailsForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = ['name', 'email', 'mobile', 'linkedin', 'carrearobject']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['collagename', 'university', 'branch', 'yearofpass', 'programinglang', 'frontendlng', 'framework','cgpa']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['projecttitle', 'prodescrip']

class PersonaldetailsForm(forms.ModelForm):
    class Meta:
        model = Personaldetails
        fields = ['dob', 'gender','nationality','fathername','address','strength','hobbies']
