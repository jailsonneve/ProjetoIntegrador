from django import forms
from .models import Fornecedor
from core.utils import validar_telefone

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = '__all__'
    
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