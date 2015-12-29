from django import forms
class nameform(forms.Form):
    yourname=forms.CharField(label="username",max_length=15)
    rj=(('cme','cme'),('ece','ece'),('eee','eee'))
    subject=forms.CharField(max_length=10)
    
	