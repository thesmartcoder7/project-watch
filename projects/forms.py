from django import forms
from .models import *
from django.core.validators import MinValueValidator, MaxValueValidator


class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'title',
            'image',
            'description',
            'link',
        ]


class RatingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
            super(RatingForm, self).__init__(*args, **kwargs)
            self.fields['design'].widget.attrs.update({'min': 0, 'max': 10, 'value': 0})
            self.fields['usability'].widget.attrs.update({'min': 0, 'max': 10, 'value': 0})
            self.fields['content'].widget.attrs.update({'min': 0, 'max': 10, 'value': 0})
      
    class Meta:
        model = Rating
        fields = [
            'design',
            'usability',
            'content'
        ]