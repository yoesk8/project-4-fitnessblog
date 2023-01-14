from django import forms
from django.forms import TextInput, FileInput, Select, Textarea
from . import models


class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = [
            'title',
            'body',
            'slug',
            'thumb',
            'category'
        ]
        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Title'
                }),
            'body': Textarea(attrs={
                'class': "form-control",
                'style': 'max-width: 800px;',
                'placeholder': 'Your awesome article here'
                }),
            'slug': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Slug'
                }),
            'thumb': FileInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                }),
            'category': Select(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'margin-bottom': '10px',
                }),

        }
