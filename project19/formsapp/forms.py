from django import forms

class student(forms.Form):
	name=forms.CharField()
	age=forms.IntegerField()
	address=forms.CharField()