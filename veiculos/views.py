from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Veiculo
from .forms import VeiculoForm


@login_required
def lista_veiculos(request):
    veiculos = Veiculo.objects.select_related('motorista')
    return render(request, 'veiculos/lista.html', {'veiculos': veiculos})


@login_required
def criar_veiculo(request):
    form = VeiculoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_veiculos')

    return render(request, 'veiculos/form.html', {'form': form})


@login_required
def editar_veiculo(request, id):
    veiculo = get_object_or_404(Veiculo, id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)

    if form.is_valid():
        form.save()
        return redirect('lista_veiculos')

    return render(request, 'veiculos/form.html', {'form': form})


@login_required
def deletar_veiculo(request, id):
    veiculo = get_object_or_404(Veiculo, id=id)

    if request.method == 'POST':
        veiculo.delete()
        return redirect('lista_veiculos')

    return render(request, 'veiculos/deletar.html', {'veiculo': veiculo})