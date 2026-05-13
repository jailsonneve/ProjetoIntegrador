from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cliente
from core.models import FilialCliente, Perfil
from django.db.models import Q
from .forms import ClienteForm


@login_required
def lista_clientes(request):

    busca = request.GET.get('busca')

    # gerente/admin vê tudo
    if request.user.is_superuser or request.user.perfil.is_gerente:

        clientes = Cliente.objects.all()

    # funcionário vê apenas clientes da filial dele
    else:

        clientes = Cliente.objects.filter(
            filialcliente__filial=request.user.perfil.filial
        )

    # barra de pesquisa
    if busca:

        clientes = clientes.filter(
            Q(nome__icontains=busca) |
            Q(telefone__icontains=busca) |
            Q(email__icontains=busca)
        )

    # evita registros duplicados
    clientes = clientes.distinct().order_by('nome')

    context = {
        'clientes': clientes,
        'busca': busca
    }

    return render(
        request,
        'clientes/lista.html',
        context
    )


@login_required
def criar_cliente(request):
    form = ClienteForm(request.POST or None)

    if form.is_valid():

        # salva cliente
        cliente = form.save(commit=False)

        cliente.criado_por = request.user

        # pega filial do usuário logado
        filial = request.user.perfil.filial

        cliente.save()

        # cria relação cliente x filial
        FilialCliente.objects.create(
            cliente=cliente,
            filial=filial
        )

        return redirect('lista_clientes')

    return render(request, 'clientes/form.html', {'form': form})


@login_required
def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    form = ClienteForm(request.POST or None, instance=cliente)

    if form.is_valid():
        form.save()
        return redirect('lista_clientes')

    return render(request, 'clientes/form.html', {'form': form})


@login_required
def deletar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_clientes')

    return render(request, 'clientes/deletar.html', {'cliente': cliente})