from django.shortcuts import render

def listar(request):
    return render(request, 'tiposdeatividades/listarTiposAtividade.html')

def cadastro(request):
    return render(request, 'tiposdeatividades/cadastroTiposAtividade.html')
