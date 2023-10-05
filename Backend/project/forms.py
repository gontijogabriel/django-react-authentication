from django import forms
from captcha.fields import CaptchaField

class CaptchaForm(forms.Form):
    nome = forms.CharField(max_length=50)
    email = forms.EmailField()
    captcha = CaptchaField()

    
    
