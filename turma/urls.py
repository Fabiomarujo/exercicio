from django.urls import path

from . import views

app_name = 'turma'

urlpatterns = [
    path("listar", views.listar, name="listar"),  
    path('cadastro', views.cadastro, name="cadastro"), 
    path('registro', views.registro, name="registro"),
]