from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    # what the form is displaying
    class Meta:
        # extra info about form
        model = Todo
        fields = ['name', 'due_date']
