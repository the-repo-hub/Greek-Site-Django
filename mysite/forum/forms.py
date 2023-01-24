from forum.models import *
from django import forms


class ThemeForm(forms.ModelForm):
    class Meta:
        model = Theme
        fields = ['head', 'text', 'image']