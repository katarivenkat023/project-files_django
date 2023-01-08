from django import forms

class LoginForm(forms.Form):
    # TODO: Define form fields here
	name = forms.CharField()