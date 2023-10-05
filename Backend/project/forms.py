from django import forms 

class CaptchaForm(forms.Form):
    nome = forms.CharField(max_length=50)
    email = forms.EmailField()
    
