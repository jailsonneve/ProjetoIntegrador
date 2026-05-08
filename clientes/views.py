from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cliente
from core.models import FilialCliente, Perfil
from .forms import ClienteForm


@login_required
def lista_clientes(request):
    filial = request.user.perfil.filial
    fc = FilialCliente.objects.filter(
        filial=filial
    )
    clientes = [f.cliente for f in fc]
    return render(request, 'clientes/lista.html', {'clientes': clientes})


@login_required
def criar_cliente(request):
    form = ClienteForm(request.POST or None)

    if form.is_valid():

        # salva cliente
        cliente = form.save()

        # pega filial do usuário logado
        filial = request.user.perfil.filial

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