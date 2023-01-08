from django import forms
from iplteamapp.models import Mumbaidetails

class MumbaiForm(forms.ModelForm):
	class Meta:
		model=Mumbaidetails
		fields='__all__'
