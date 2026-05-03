from django import forms
from .models import Motorista

class MotoristaForm(forms.ModelForm):
    class Meta:
        model = Motorista
        fields = '__all__'