from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_rotas, name='lista_rotas'),
    path('novo/', views.criar_rota, name='criar_rota'),
    path('editar/<int:id>/', views.editar_rota, name='editar_rota'),
    path('deletar/<int:id>/', views.deletar_rota, name='deletar_rota'),
]