from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def cadastro(request):
    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('login')

    return render(request, 'auth/cadastro.html', {'form': form})

from django.contrib.auth.decorators import login_required
from clientes.models import Cliente
from motoristas.models import Motorista
from veiculos.models import Veiculo
from rotas.models import Rota
from fornecedores.models import Fornecedor
from diario.models import Diario

@login_required
def dashboard(request):
    context = {
        'clientes': Cliente.objects.count(),
        'motoristas': Motorista.objects.count(),
        'veiculos': Veiculo.objects.count(),
        'rotas': Rota.objects.count(),
        'fornecedores': Fornecedor.objects.count(),
        'diarios': Diario.objects.count(),
    }
    return render(request, 'dashboard/index.html', context)