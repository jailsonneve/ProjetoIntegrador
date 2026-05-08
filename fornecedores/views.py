from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Fornecedor
from .forms import FornecedorForm
from core.models import FilialFornecedores


@login_required
def lista_fornecedores(request):
    filial = request.user.perfil.filial
    ff = FilialFornecedores.objects.filter(
        filial=filial
    )
    fornecedores = [f.fornecedor for f in ff]
    return render(request, 'fornecedores/lista.html', {'fornecedores': fornecedores})


@login_required
def criar_fornecedor(request):
    form = FornecedorForm(request.POST or None)

    if form.is_valid():
        fornecedor = form.save()
        filial = request.user.perfil.filial

        FilialFornecedores.objects.create(
            fornecedor=fornecedor,
            filial=filial
        )
        return redirect('lista_fornecedores')

    return render(request, 'fornecedores/form.html', {'form': form})


@login_required
def editar_fornecedor(request, id):
    fornecedor = get_object_or_404(Fornecedor, id=id)
    form = FornecedorForm(request.POST or None, instance=fornecedor)

    if form.is_valid():
        form.save()
        return redirect('lista_fornecedores')

    return render(request, 'fornecedores/form.html', {'form': form})


@login_required
def deletar_fornecedor(request, id):
    fornecedor = get_object_or_404(Fornecedor, id=id)

    if request.method == 'POST':
        fornecedor.delete()
        return redirect('lista_fornecedores')

    return render(request, 'fornecedores/deletar.html', {'fornecedor': fornecedor})