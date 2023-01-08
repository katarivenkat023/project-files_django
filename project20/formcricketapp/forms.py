from django import forms

class CricketForm(forms.Form):
	name=forms.CharField()
	matches=forms.IntegerField()
	innings=forms.IntegerField()
	runs=forms.IntegerField()
	balls=forms.IntegerField()
	not_out=forms.IntegerField()
	fours=forms.IntegerField()
	sixes=forms.IntegerField()
	fiftys=forms.IntegerField()
	hundreds=forms.IntegerField()