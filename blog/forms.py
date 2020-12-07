from django import forms
from .models import Comment


class AddComment(forms.ModelForm):
    model = Comment
    fields = ('name', 'body')

    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'body': forms.Textarea(attrs={'class': 'form-control'}),
    }
