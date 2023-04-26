from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control form-floating mb-4", "placeholder": "Name*"}))
    email = forms.CharField(
        widget=forms.EmailInput(attrs={"class": "form-control form-floating mb-4", "placeholder": "Email*"}))
    body = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control form-floating mb-4", "placeholder": "Comment", "style": "height: 150px"}))

    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
