from django import forms

class UserPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget = forms.Textarea)