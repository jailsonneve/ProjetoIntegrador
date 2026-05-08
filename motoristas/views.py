from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Motorista
from core.models import FilialMotoristas
from .forms import MotoristaForm


@login_required
def lista_motoristas(request):
    filial = request.user.perfil.filial
    fm = FilialMotoristas.objects.filter(
        filial=filial
    )
    motoristas = [f.motorista for f in fm]
    return render(request, 'motoristas/lista.html', {'motoristas': motoristas})

@login_required
def criar_motorista(request):
    form = MotoristaForm(request.POST or None)

    if form.is_valid():
        motorista = form.save()
        filial = request.user.perfil.filial

        FilialMotoristas.objects.create(
            motorista=motorista,
            filial=filial
        )
        return redirect('lista_motoristas')

    return render(request, 'motoristas/form.html', {'form': form})


@login_required
def editar_motorista(request, id):
    motorista = get_object_or_404(Motorista, id=id)
    form = MotoristaForm(request.POST or None, instance=motorista)

    if form.is_valid():
        form.save()
        return redirect('lista_motoristas')

    return render(request, 'motoristas/form.html', {'form': form})


@login_required
def deletar_motorista(request, id):
    motorista = get_object_or_404(Motorista, id=id)

    if request.method == 'POST':
        motorista.delete()
        return redirect('lista_motoristas')

    return render(request, 'motoristas/deletar.html', {'motorista': motorista})