from django.shortcuts import render, redirect
from utilitarios import utils

def contato(request): 
    return render(request, 'utilitarios/contato.html')

def popular_bd(request):
    utils.truncar_tabelas()
    utils.popular_tiposdeatividades()
    utils.popular_titulo()
    utils.popular_aluno()
    utils.popular_instrutor()
    utils.popular_turma()

    return redirect('/')