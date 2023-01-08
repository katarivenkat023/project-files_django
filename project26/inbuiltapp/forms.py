from django import forms
from django.core import validators


class StudentForm(forms.Form):
	name=forms.CharField(max_length=50)
	rollno=forms.IntegerField()
	email=forms.EmailField(validators=[validators.EmailValidator()])
	address=forms.CharField(widget=forms.Textarea,validators=[validators.MinLengthValidator(4),validators.MaxLengthValidator(10)])
