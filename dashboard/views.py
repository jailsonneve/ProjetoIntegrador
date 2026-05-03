from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count

from clientes.models import Cliente
from motoristas.models import Motorista
from veiculos.models import Veiculo
from rotas.models import Rota
from fornecedores.models import Fornecedor
from diario.models import Diario


@login_required
def dashboard(request):
    total_clientes = Cliente.objects.count()
    total_motoristas = Motorista.objects.count()
    total_veiculos = Veiculo.objects.count()
    total_rotas = Rota.objects.count()
    total_fornecedores = Fornecedor.objects.count()
    total_diarios = Diario.objects.count()

    rotas_status = Rota.objects.values('status').annotate(total=Count('status'))

    context = {
        'total_clientes': total_clientes,
        'total_motoristas': total_motoristas,
        'total_veiculos': total_veiculos,
        'total_rotas': total_rotas,
        'total_fornecedores': total_fornecedores,
        'total_diarios': total_diarios,
        'rotas_status': rotas_status,
    }

    return render(request, 'dashboard/index.html', context)