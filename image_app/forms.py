from django import forms
from .models import ImageCollector


class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageCollector
        fields = ('name', 'title', 'photo', 'description')
