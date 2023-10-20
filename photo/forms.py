from django.forms import ModelForm
from .models import PhotoPost, Material
from django import forms

class PhotoPostForm(ModelForm):
    class Meta:
        model = PhotoPost
        fields = ['category', 'title', 'comment', 'image1', 'image2']

class MaterialForm(ModelForm):
    class Meta:
        model = Material
        fields = ['class_name', 'user', 'title', 'content', 'file']
    file = forms.FileField(required=False)