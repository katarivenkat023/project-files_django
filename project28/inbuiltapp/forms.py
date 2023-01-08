from django import forms
from django.core import validators

class StudentForm(forms.Form):
	name=forms.CharField(max_length=50)
	rollno=forms.IntegerField()
	email=forms.EmailField()
	address=forms.CharField(widget=forms.Textarea)
	def clean(self):
		print("Total form validation")
		total_clean_data=super().clean()
		input_name=total_clean_data['name']
		
		if input_name[0].lower!="K":
			raise forms.ValidationError("Name should strts with K ")
		input_roll=total_clean_data['rollno']
		if input_roll<10:
			raise forms.ValidationError("Roll number should be >10 ")