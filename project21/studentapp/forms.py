from django import forms 

class StudentForm(forms.Form):
    # TODO: Define form fields here
    name = forms.CharField()
    password = forms.CharField()
    re_password = forms.CharField()
    date = forms.DateField()
    studyonline_id = forms.CharField()
    mail_id = forms.EmailField()
    phone_number = forms.CharField()
    feedback = forms.CharField(widget=forms.Textarea)
