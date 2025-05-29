from django.shortcuts import render

def listar(request):
    return render(request, 'titulo/listarTitulos.html')

def cadastro(request):
    return render(request, 'titulo/cadastroTitulos.html')