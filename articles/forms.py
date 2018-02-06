from django import forms

from .models import Articles
from django.contrib.auth.models import User

class ArticlesForm(forms.ModelForm):

    class Meta:
        model = Articles
        fields = ('title', 'author', 'description',)



class UserForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('username','password', 'email')

		help_texts = {
            'username': None,
        }