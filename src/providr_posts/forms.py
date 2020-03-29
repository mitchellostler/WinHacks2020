from django import forms
from .models import UserPost

class UserPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget = forms.Textarea)

class UserPostModelForm(forms.ModelForm):
    class Meta:
        model = UserPost
        fields = ['title', 'slug', 'content']
    

    #validation for unique titles, not necessary
    # def clean_title(self, *args, **kwargs):
    #     title = self.cleaned_data.get('title')
    #     qs = BlogPost.objects.filter(title_iexact=title)
    #     if qs.exists():
    #         raise forms.ValidationError("This is not a valid title.")
    #     return title