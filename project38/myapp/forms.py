from django import forms

class LoginForm(forms.Form):
	name=forms.CharField(max_length=50)
	age=forms.IntegerField()
	gf=forms.CharField(max_length=50)