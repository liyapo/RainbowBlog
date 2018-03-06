from django import forms
from .models import Articles
from django.contrib.auth.models import User

class ArticlesForm(forms.ModelForm):

    class Meta:
        model = Articles
        fields = ('title', 'author', 'description')

class ArticlesUserForm(forms.ModelForm):

    class Meta:
        model = Articles
        fields = ('title', 'description')

class UserSignUpForm(forms.ModelForm):
    
	class Meta:
		model = User
		fields = ('username', 'password', 'email')
        #password = forms.CharField(widget = forms.PasswordInput())

		help_texts = {
            'username': None,
        }


class UserLoginForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'password')
        #password = forms.CharField(widget = forms.PasswordInput())

		help_texts = {
            'username': None,
        }
