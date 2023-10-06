from django import forms
from project.models import User
from captcha.fields import CaptchaField

class LoginCaptchaForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = CaptchaField()

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nome', 'email', 'password']  # Lista dos campos que você deseja incluir no formulário

    # Adicione campos personalizados, como confirmar senha, se necessário
    confirm_password = forms.CharField(max_length=128, widget=forms.PasswordInput, label='Confirmar Senha')

    # Você pode adicionar validações personalizadas, se necessário
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('As senhas não coincidem.')

    # Você pode personalizar os widgets dos campos, se necessário
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput()
        self.fields['confirm_password'].widget = forms.PasswordInput()
