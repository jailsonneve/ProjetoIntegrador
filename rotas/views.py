from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Rota
from .forms import RotaForm
from core.models import FilialRotas


@login_required
def lista_rotas(request):
    filial = request.user.perfil.filial
    fr = FilialRotas.objects.filter(
        filial=filial
    )
    rotas = [f.rotas for f in fr]
    return render(request, 'rotas/lista.html', {'rotas': rotas})


@login_required
def criar_rota(request):
    form = RotaForm(request.POST or None)

    if form.is_valid():
        rota = form.save()
        filial = request.user.perfil.filial

        FilialRotas.objects.create(
            rotas=rota,
            filial=filial
        )
        return redirect('lista_rotas')

    return render(request, 'rotas/form.html', {'form': form})


@login_required
def editar_rota(request, id):
    rota = get_object_or_404(Rota, id=id)
    form = RotaForm(request.POST or None, instance=rota)

    if form.is_valid():
        form.save()
        return redirect('lista_rotas')

    return render(request, 'rotas/form.html', {'form': form})


@login_required
def deletar_rota(request, id):
    rota = get_object_or_404(Rota, id=id)

    if request.method == 'POST':
        rota.delete()
        return redirect('lista_rotas')

    return render(request, 'rotas/deletar.html', {'rota': rota})