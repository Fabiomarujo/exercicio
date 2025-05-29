from django.urls import path
from . import views

app_name = 'tiposdeatividades'

urlpatterns = [
    path('listar', views.listar, name="listar"),  
    path('cadastro', views.cadastro, name="cadastro"),
]