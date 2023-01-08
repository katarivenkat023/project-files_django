from django import forms
from django.core import validators


class StudentForm(forms.Form):
    # TODO: Define form fields here
    name = forms.CharField()
    mail_id = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    re_password = forms.CharField(label='Password(Again)',widget=forms.PasswordInput)
    trainer_name = forms.CharField()
    feedback = forms.CharField(widget=forms.Textarea)
    bot_handler = forms.CharField(required=False,widget=forms.HiddenInput)

    def clean(self):
        print('Validating the Total form')
        total_cleaned_data=super().clean()

        input_name=total_cleaned_data['name']
        if len(input_name)<3:
            raise forms.ValidationError('Please enter more than 3 characters')

        input_password=total_cleaned_data['password']
        input_re_password=total_cleaned_data['re_password']
        if input_password!=input_re_password:
            raise forms.ValidationError('Password Mismatch!!!!')

        input_bot_handler=total_cleaned_data['bot_handler']
        if len(input_bot_handler)>0:
            raise forms.ValidationError('Thanks BOT...do not try to automate you fool !!!!')





   




   
   