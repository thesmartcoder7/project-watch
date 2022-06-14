from django import forms
from .models import *


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
    class Meta:
        model = Rating
        fields = [
            'design',
            'usability',
            'content'
        ]