from django import forms
from .models import Post , Comment

class PostForm(forms.ModelForm):
    body=forms.CharField(label='',widget=forms.Textarea(attrs={'rows':'3','placeholder':'say some thing'}))
    image=forms.ImageField(required=False)
    class Meta:
        
        model=Post
        fields=['body','image']