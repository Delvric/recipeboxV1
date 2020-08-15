from recipeboxapp.models import Author, Article
from django import forms


class AuthorForm(forms.Form):
    class Meta:
        model = Author
        fields = ["name"]


class RecipeForms(forms.Form):
    title = forms.CharField(max_length=200)
    description = forms.CharFieldField(widget=forms.Textarea)
    time_required = forms.CharFieldField(max_length=20)
    instructions = forms.CharField(widget=forms.Textarea)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)
