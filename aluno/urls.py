from django.urls import path

from . import views

app_name = 'aluno'

urlpatterns = [
    path("lista", views.listar, name="listar"),  
    path('cadastro', views.cadastro, name="cadastro"), 
    # path('cadastrar', views.cadastrar, name="cadastrar"), 
]