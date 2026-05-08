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
from .forms import CadastroForm
from core.models import FilialCliente, FilialDiario, FilialFornecedores, FilialMotoristas, FilialRotas, FilialVeiculos


def cadastro(request):
    form = CadastroForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('login')

    return render(request, 'auth/cadastro.html', {'form': form})


@login_required
def dashboard(request):
    tipo = request.GET.get('tipo')
    filial = request.user.perfil.filial

    ff = FilialFornecedores.objects.filter(
        filial=filial
    )

    fornecedores_qs = Fornecedor.objects.filter(
        id__in=[f.fornecedor.id for f in ff]
    )

    if tipo:
        fornecedores_qs = fornecedores_qs.filter(
            tipo_servico=tipo
        )

    fornecedores_por_tipo = (
        fornecedores_qs
        .values('tipo_servico')
        .annotate(total=Count('id'))
    )

    fc = FilialCliente.objects.filter(
        filial=filial
    )
    clientes = [f.cliente for f in fc]

    fd = FilialDiario.objects.filter(
        filial=filial
    )
    diarios = [f.diario for f in fd]

    fm = FilialMotoristas.objects.filter(
        filial=filial
    )
    motoristas = [f.motorista for f in fm]

    fr = FilialRotas.objects.filter(
        filial=filial
    )
    print(fr)
    rotas = [f.rotas for f in fr]

    fv = FilialVeiculos.objects.filter(
        filial=filial
    )
    veiculos = [f.veiculos for f in fv]

    context = {
        'clientes': len(clientes),
        'motoristas': len(motoristas),
        'veiculos': len(veiculos),
        'rotas': len(rotas),

        # número (card)
        'fornecedores': fornecedores_qs.count(),

        'diarios': len(diarios),

        # lista
        'lista_fornecedores': fornecedores_qs,

        # gráfico
        'fornecedores_por_tipo': list(fornecedores_por_tipo),

        'tipo_selecionado': tipo
    }

    return render(request, 'dashboard/index.html', context)

@login_required
def perfil(request):
    profile = request.user.perfil

    context = {
        'user': request.user,
        'profile': profile
    }

    return render(request, 'core/perfil.html', context)