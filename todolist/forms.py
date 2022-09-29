from django.forms import ModelForm
from django import forms
from .models import Task
from django.contrib.auth.models import User

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
