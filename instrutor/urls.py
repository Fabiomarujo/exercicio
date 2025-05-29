from django.urls import path

from . import views

app_name = 'instrutor'

urlpatterns = [
    path("cadinstrutor", views.cadinstrutor, name="cadinstrutor"), 
    path("listarInst", views.listarInst, name="listarInst"),         
]