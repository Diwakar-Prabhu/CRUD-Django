from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        labels = {
            'title': 'Title',
            'description': 'About',
            'auth_name':'Author',
            'img':'Picture'
        }
    