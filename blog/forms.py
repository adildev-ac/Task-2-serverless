from django import forms
from .models import BlogPost, BlogCategory


class BlogPostForm(forms.ModelForm):
    is_draft = forms.BooleanField(required=False, label="Save as Draft")

    class Meta:
        model = BlogPost
        fields = ['title', 'image', 'category', 'summary', 'content', 'is_draft']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter blog title'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'summary': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter a brief summary'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'placeholder': 'Write your blog content here'}),
            'is_draft': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
