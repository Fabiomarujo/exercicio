from django.urls import path
from . import views

app_name = 'instrutor'

urlpatterns = [
    path("cadastro/", views.cadastro, name="cadastro"), 
    path("cadastrar/", views.cadastrar, name="cadastrar"),
    path("listar/", views.listar, name="listar"), 
    path('excluir/<int:codigo>', views.excluir, name="excluir_instrutor"),
    path('carregar_instrutor/<int:codigo>', views.carregar_instrutor, name="carregar_instrutor"),
    path('atualizar_instrutor/', views.atualizar, name='atualizar_instrutor'),        
]