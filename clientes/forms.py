import re
from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from .models import Cliente
from validate_docbr import CPF
from core.utils import validar_cnh, validar_cpf, validar_telefone

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'telefone', 'cpf', 'cnh', 'email', 'endereco']
    
    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')

        # remove máscara
        cpf = cpf.replace('.', '').replace('-', '')

        resultado = validar_cpf(
            cpf,
            ignorar_id=self.instance.id
        )

        if resultado == 'invalido':
            raise forms.ValidationError('CPF inválido.')

        if resultado == 'cadastrado':
            raise forms.ValidationError('CPF já cadastrado.')

        return cpf    

    # validar telefone
    def clean_telefone(self):
        telefone = self.cleaned_data['telefone']
        
        telefone = re.sub(r'\D', '', telefone)

        resultado = validar_telefone(telefone, self.instance.id)

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
    
    def clean_cnh(self):
        cnh = self.cleaned_data.get('cnh')

        if cnh:
            cnh = re.sub(r'\D', '', cnh)

            resultado = validar_cnh(cnh, self.instance.id)

            if resultado == 'invalido':
                raise forms.ValidationError('CNH inválida.')

            if resultado == 'cadastrado':
                raise forms.ValidationError('CNH já cadastrada.')

            return cnh

        return cnh
