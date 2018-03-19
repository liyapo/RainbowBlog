from django import forms
from .models import Articles
from django.contrib.auth.models import User

# this class is used for edit/delete articles 
class ArticlesForm(forms.ModelForm):

    class Meta:
        model = Articles
        fields = ('title', 'author', 'description')

# this class is used to create articles when logged
class ArticlesUserForm(forms.ModelForm):

    class Meta:
        model = Articles
        fields = ('title', 'description')

# form to sign up, password is hashed
class UserSignUpForm(forms.ModelForm):

	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('username','password', 'email')

		help_texts = {
            'username': None,
            }

# form to log in, password is hashed
class UserLoginForm(forms.ModelForm):

	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('username','password')

		help_texts = {
            'username': None,
            }