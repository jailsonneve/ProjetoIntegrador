from django import forms
from .models import Rota

class RotaForm(forms.ModelForm):
    class Meta:
        model = Rota
        fields = '__all__'