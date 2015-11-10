from .models import User, Club
from django import forms


class UserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'fname'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'lname'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'password', 'class': 'validate'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'id': 'email', 'class': 'validate'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'id': 'username'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'password', 'email', 'username' )


class ClubForm(forms.ModelForm):
    club_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'club_name'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'id': 'description', 'class': 'materialize-textarea'}))

    class Meta:
        model = Club
        fields = ('club_name', 'description')