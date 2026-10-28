from django import forms

from fornecedores.models import Fornecedor
from veiculos.models import Veiculo

from .models import Manutencao


class ManutencaoForm(forms.ModelForm):
    class Meta:
        model = Manutencao
        fields = ['veiculo', 'fornecedor', 'data_manutencao', 'tipo', 'descricao', 'custo']
        widgets = {
            'veiculo': forms.Select(attrs={'class': 'form-select'}),
            'fornecedor': forms.Select(attrs={'class': 'form-select'}),
            'data_manutencao': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'class': 'form-control', 'type': 'date'},
            ),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'descricao': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 4,
                       'placeholder': 'Descreva o serviço realizado'}
            ),
            'custo': forms.NumberInput(
                attrs={'class': 'form-control', 'step': '0.01', 'min': '0',
                       'placeholder': '0.00'}
            ),
        }

    def __init__(self, *args, filial=None, **kwargs):
        super().__init__(*args, **kwargs)

        # Só aparecem veículos e oficinas da filial do usuário logado
        # (as filiais ficam nas tabelas FilialVeiculos / FilialFornecedores).
        if filial is None:
            veiculos = Veiculo.objects.none()
            oficinas = Fornecedor.objects.none()
        else:
            veiculos = Veiculo.objects.filter(filialveiculos__filial=filial)
            oficinas = Fornecedor.objects.filter(
                filialfornecedores__filial=filial,
                tipo_servico='manutencao',  # remova este filtro para listar todos os fornecedores
            )

        self.fields['veiculo'].queryset = veiculos
        self.fields['veiculo'].empty_label = 'Selecione o veículo'

        self.fields['fornecedor'].queryset = oficinas
        self.fields['fornecedor'].empty_label = 'Selecione a oficina (opcional)'
        self.fields['fornecedor'].label_from_instance = lambda f: f'{f.empresa} - {f.nome}'
