from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','first_name','last_name','email','password1','password2']
		widgets = {
		'username': forms.TextInput(attrs={'placeholder': 'Username','class':'form-control'}),
		'first_name': forms.TextInput(attrs={'placeholder': 'First Name','class':'form-control'}),
		'last_name': forms.TextInput(attrs={'placeholder': 'Last Name','class':'form-control'}),
		'email': forms.TextInput(attrs={'placeholder': 'E-mail','class':'form-control'}),
		'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
		'password2': forms.TextInput(attrs={'placeholder': 'Retype password','class':'form-control'}),
		}

	def save(self,commit=True):
		user = super().save(commit=False)
		if commit:
			user.save()
		return user