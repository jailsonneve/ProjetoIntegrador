from django import forms
from .models import Cliente
from core.utils import validar_telefone

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'telefone', 'email', 'endereco']
    
    # validar telefone
    def clean_telefone(self):
        telefone = self.cleaned_data['telefone']

        resultado = validar_telefone(telefone)

        if resultado == 'invalido':
            raise forms.ValidationError(
                "Telefone com formato inválido!!"
            )

        if resultado == 'cadastrado':
            raise forms.ValidationError(
                "Telefone já cadastrado!!"
            )

        # tudo ok
        return telefone
        
