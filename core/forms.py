from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Perfil

from .models import Filial


class CadastroForm(UserCreationForm):
    email = forms.EmailField()
    telefone = forms.CharField(max_length=20)

    filial = forms.ModelChoiceField(
        queryset=Filial.objects.all()
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'telefone',
            'filial',
            'password1',
            'password2'
        ]

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("E-mail já cadastrado!")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data['email']

        if commit:
            user.save()

            perfil = user.perfil
            perfil.telefone = self.cleaned_data['telefone']
            perfil.filial = self.cleaned_data['filial']
            perfil.save()

        return user

class EditarPerfilForm(forms.ModelForm):

    first_name = forms.CharField(label='Nome')
    last_name = forms.CharField(label='Sobrenome')
    email = forms.EmailField(label='Email')

    class Meta:
        model = Perfil
        fields = ['telefone']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')

        super().__init__(*args, **kwargs)

        self.fields['first_name'].initial = user.first_name
        self.fields['last_name'].initial = user.last_name
        self.fields['email'].initial = user.email