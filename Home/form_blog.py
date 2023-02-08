from django import forms
from froala_editor.fields import FroalaField
from .models import *


class Blogform(forms.ModelForm):
    class Meta:
        model= blog_model_new1
        fields=['content']
       