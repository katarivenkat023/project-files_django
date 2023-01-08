from django import forms
from modelbasedform.models import StudentTable
class StudentForm(forms.ModelForm):
	class Meta:
		model=StudentTable
		fields='__all__'