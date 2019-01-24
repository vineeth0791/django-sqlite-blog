from django import forms

class UploadFileForm(forms.Form):
	file = forms.FileField()

class UploadFileForm1(forms.Form):
	file  = forms.FileField() # for creating file input  