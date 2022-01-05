from django import forms
from .models import Person

from django.contrib.auth import (
	get_user_model
	)

User = get_user_model()


class PersonForm(forms.Form):
	name = forms.CharField()
	std = forms.CharField()
	college = forms.CharField()
	branch = forms.CharField()

class StudentForm(forms.Form):
	name = forms.CharField()
	regno = forms.CharField()
	subject = forms.CharField()


class PerForm(forms.ModelForm):
	class Meta:
		model = Person
		fields = [
			'name',
			'std',
			'college',
			'branch'
		]


class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

class SignupForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	confirm_password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'password',
			'confirm_password'
		]