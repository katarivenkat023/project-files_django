from django import forms
from django.core import validators

def start_with_v(data):
	if data[0].lower!="V":
		raise forms.ValidationError("Name should strts with V ")
def roll_number(value):
	if value<100:
		raise forms.ValidationError("roll number should have >100")
class StudentForm(forms.Form):
	name=forms.CharField(max_length=50,validators=[start_with_v])
	rollno=forms.IntegerField(validators=[roll_number])
	email=forms.EmailField()
	address=forms.CharField(widget=forms.Textarea)
