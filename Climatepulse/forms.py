from django import forms
from blog.models import blogPost


class postfrom(forms.ModelForm):
    class Meta:
        model = blogPost
        fields = ['title', 'content']
        widgets  = {
            'title': forms.TextInput(attrs={'class': 'form-control mt-2 mb-5'}),
            'content': forms.Textarea(attrs={'class': 'form-control mt-2 ' ,'rows':'30'})
        }
