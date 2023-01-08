from django import forms

class EmployeeForm(forms.Form):
	emp_id=forms.CharField(max_length=50)
	name=forms.CharField(max_length=50)
	email=forms.EmailField()
	address=forms.CharField(widget=forms.Textarea)

	def clean_emp_id(self):
		input_emp_id=self.cleaned_data['emp_id']
		print("Validating of id field")
		return input_emp_id

	def clean_name(self):
		input_name=self.cleaned_data['name']
		print("Validating of name field")
		if len(input_name)<3:
			raise forms.ValidationError(" name should be <3 characters")
		return input_name

	def clean_email(self):
		input_email=self.cleaned_data['email']
		print("Validating email field")
		return input_email

	def clean_address(self):
		input_address=self.cleaned_data['address']
		print("Validating address field")
		if len(input_address) <5:
			raise forms.ValidationError(" Adress should be <5 characters")
		return input_address





