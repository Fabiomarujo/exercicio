from django.urls import path

from . import views

app_name = 'utilitarios'

urlpatterns = [
    path('contato', views.contato, name="contato"),
]