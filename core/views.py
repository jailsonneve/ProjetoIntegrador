from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Count

from clientes.models import Cliente
from motoristas.models import Motorista
from veiculos.models import Veiculo
from rotas.models import Rota
from fornecedores.models import Fornecedor
from diario.models import Diario


def cadastro(request):
    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('login')

    return render(request, 'auth/cadastro.html', {'form': form})


@login_required
def dashboard(request):
    tipo = request.GET.get('tipo')

    fornecedores_qs = Fornecedor.objects.all()

    if tipo:
        fornecedores_qs = fornecedores_qs.filter(tipo_servico=tipo)

    # 🔥 agrupamento por tipo (gráfico profissional)
    fornecedores_por_tipo = (
        fornecedores_qs
        .values('tipo_servico')
        .annotate(total=Count('id'))
    )

    context = {
        'clientes': Cliente.objects.count(),
        'motoristas': Motorista.objects.count(),
        'veiculos': Veiculo.objects.count(),
        'rotas': Rota.objects.count(),

        # número (card)
        'total_fornecedores': fornecedores_qs.count(),

        'diarios': Diario.objects.count(),

        # lista
        'lista_fornecedores': fornecedores_qs,

        # gráfico
        'fornecedores_por_tipo': list(fornecedores_por_tipo),

        'tipo_selecionado': tipo
    }

    return render(request, 'dashboard/index.html', context)