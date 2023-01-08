from django import forms
from bookmyshowapp.models import MovieInfo
class MovieInfoForm(forms.ModelForm):
	class Meta:
		model=MovieInfo
		fields='__all__'