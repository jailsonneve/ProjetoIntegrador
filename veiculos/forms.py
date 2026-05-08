from django import forms
from .models import Veiculo
import re
class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'

    # validar placa
    def clean_placa(self):
        placa = self.cleaned_data['placa']
        placa = placa.upper()

        # formato mercosul
        pattern_mercosul = r'[A-Z]{3}\d[A-Z]\d{2}'

        # formato antigo
        pattern_antigo = r'^[A-Z]{3}\d{4}$'

        placa_mercosul = re.fullmatch(
            pattern_mercosul,
            placa
        )

        placa_antiga = re.fullmatch(
            pattern_antigo,
            placa
        )

        # nao bateu com nenhum formato
        if not placa_mercosul and not placa_antiga:
            raise forms.ValidationError("Placa com formato inválido!!")

        # verificar se ja esta cadastrado no banco
        if Veiculo.objects.filter(placa=placa).exists():
            raise forms.ValidationError("Placa já cadastrada!!")

        # tudo ok
        return placa
