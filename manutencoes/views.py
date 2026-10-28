from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import ManutencaoForm
from .models import Manutencao


class FilialMixin(LoginRequiredMixin):
    """Login obrigatório + acesso à filial do usuário (request.user.perfil.filial)."""

    def get_filial(self):
        return self.request.user.perfil.filial


class ManutencaoListView(FilialMixin, ListView):
    model = Manutencao
    template_name = 'manutencoes/manutencao_list.html'
    context_object_name = 'manutencoes'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset().select_related('veiculo', 'fornecedor')
        filial = self.get_filial()
        if filial is None:
            return qs.none()
        # a manutenção pertence à filial do veículo
        return qs.filter(veiculo__filialveiculos__filial=filial)


class ManutencaoCreateView(FilialMixin, CreateView):
    model = Manutencao
    form_class = ManutencaoForm
    template_name = 'manutencoes/manutencao_form.html'
    success_url = reverse_lazy('lista_manutencoes')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['filial'] = self.get_filial()
        return kwargs

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, 'Manutenção registrada com sucesso!')
        return response
