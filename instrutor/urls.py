from django.urls import path

from . import views

app_name = 'instrutor'

urlpatterns = [
    path("cadastro", views.cadastro, name="cadastro"), 
    path("listar", views.listar, name="listar"),         
]