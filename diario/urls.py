from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_diario, name='lista_diario'),
    path('novo/', views.criar_diario, name='criar_diario'),
    path('editar/<int:id>/', views.editar_diario, name='editar_diario'),
    path('deletar/<int:id>/', views.deletar_diario, name='deletar_diario'),
]