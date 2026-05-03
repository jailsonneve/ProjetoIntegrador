from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_fornecedores, name='lista_fornecedores'),
    path('novo/', views.criar_fornecedor, name='criar_fornecedor'),
    path('editar/<int:id>/', views.editar_fornecedor, name='editar_fornecedor'),
    path('deletar/<int:id>/', views.deletar_fornecedor, name='deletar_fornecedor'),
]