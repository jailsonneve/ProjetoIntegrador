from django import forms
from .models import Motorista
from core.utils import validar_telefone
import re

class MotoristaForm(forms.ModelForm):
    class Meta:
        model = Motorista
        fields = '__all__'
    
    # validar CNH
    def clean_cnh(self):
        cnh = self.cleaned_data['cnh'] 
        pattern = r'^\d{11}$' # regra que define que deve ter 11 numeros

        # nao eh valido
        if not re.fullmatch(pattern, cnh):
            raise forms.ValidationError("CNH com formato inválido!!")

        # verificar se ja esta cadastrado no banco
        if Motorista.objects.filter(cnh=cnh).exists():
            raise forms.ValidationError("CNH já cadastrada!!")

        # tudo ok'
        return cnh

    # validar telefone
    def clean_telefone(self):
        telefone = self.cleaned_data['telefone']

        resultado = validar_telefone(telefone)

        if resultado == 'invalido':
            raise forms.ValidationError("Telefone com formato inválido!!")

        if resultado == 'cadastrado':
            raise forms.ValidationError("Telefone já cadastrado!!")

        # tudo ok
        return telefone