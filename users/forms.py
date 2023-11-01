from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        label="Nome do Usuário",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: João Silva"
            }
        )
    )
    password = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )
    
class RegisterForm(forms.Form):
    username = forms.CharField(
        label="Usuário de Acesso",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: João Silva"
            }
        )
    )
    email = forms.EmailField(
        label="Endereço de E-mail",
        required=True,
        max_length=255,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: joao@exemple.com"
            }
        )
    )
    password = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Escolha uma senha"
            }
        )
    )
    repassword = forms.CharField(
        label="Confirme a Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Confirme a sua senha"
            }
        )
    )
    
    def clean_username(self):
        username = self.cleaned_data("username")
        if username:
            username = username.strip()
            if " " in username:
                raise forms.ValidationError("O formato do nome de usuário não é valido.")
            else:
                return username