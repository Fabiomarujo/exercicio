from django.shortcuts import render

def cadastro(request):
    return render(request, 'instrutor/cadastroInstrutor.html')

def listar(request):
    return render(request, 'instrutor/listarInstrutores.html')

