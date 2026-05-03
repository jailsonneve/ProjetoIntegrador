from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_motoristas, name='lista_motoristas'),
    path('novo/', views.criar_motorista, name='criar_motorista'),
    path('editar/<int:id>/', views.editar_motorista, name='editar_motorista'),
    path('deletar/<int:id>/', views.deletar_motorista, name='deletar_motorista'),
]