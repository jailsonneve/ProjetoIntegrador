from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_veiculos, name='lista_veiculos'),
    path('novo/', views.criar_veiculo, name='criar_veiculo'),
    path('editar/<int:id>/', views.editar_veiculo, name='editar_veiculo'),
    path('deletar/<int:id>/', views.deletar_veiculo, name='deletar_veiculo'),
]