from django import forms

class ComplaintForm(forms.Form):
	docfile = forms.FileField(
		label='Select a file'
		)