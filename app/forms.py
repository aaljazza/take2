from django import forms
from .models import Restaurant
from django.contrib.auth.models import User


class RestaurantForm(forms.ModelForm):
	class Meta:
		model = Restaurant
		exclude = ['created_on', 'updated_on', 'owner']

		widgets = {
		}


class SignupForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password']

		widgets = {
			"password": forms.PasswordInput()
		}

class SigninForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())