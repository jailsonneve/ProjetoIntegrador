from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_clientes, name='lista_clientes'),
    path('novo/', views.criar_cliente, name='criar_cliente'),
    path('editar/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('deletar/<int:id>/', views.deletar_cliente, name='deletar_cliente'),
]