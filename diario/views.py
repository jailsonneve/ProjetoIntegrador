from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Diario
from .forms import DiarioForm
from core.models import FilialDiario


@login_required
def lista_diario(request):
    diarios = Diario.objects.select_related('rota')
    return render(request, 'diario/lista.html', {'diarios': diarios})


@login_required
def criar_diario(request):
    form = DiarioForm(request.POST or None)

    if form.is_valid():
        diario = form.save()
        filial = request.user.perfil.filial

        FilialDiario.objects.create(
            diario=diario,
            filial=filial
        )
        return redirect('lista_diario')

    return render(request, 'diario/form.html', {'form': form})


@login_required
def editar_diario(request, id):
    diario = get_object_or_404(Diario, id=id)
    form = DiarioForm(request.POST or None, instance=diario)

    if form.is_valid():
        form.save()
        return redirect('lista_diario')

    return render(request, 'diario/form.html', {'form': form})


@login_required
def deletar_diario(request, id):
    diario = get_object_or_404(Diario, id=id)

    if request.method == 'POST':
        diario.delete()
        return redirect('lista_diario')

    return render(request, 'diario/deletar.html', {'diario': diario})