from django import forms

from todo2app.models import Task


class Taskform(forms.ModelForm):
    class Meta:
        model=Task
        fields=["task","priority","date"]