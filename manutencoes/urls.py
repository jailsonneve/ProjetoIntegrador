from django.urls import path

from . import views

# Sem app_name, como nos outros apps do projeto (lista_veiculos, criar_veiculo...)
urlpatterns = [
    path('', views.ManutencaoListView.as_view(), name='lista_manutencoes'),
    path('novo/', views.ManutencaoCreateView.as_view(), name='criar_manutencao'),
]
