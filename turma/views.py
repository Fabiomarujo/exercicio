from django.shortcuts import render

def listar(request):
    return render(request, 'turma/listarTurmas.html')

def cadastro(request):
    return render(request, 'turma/cadastroTurma.html')

def registro(request):
    return render(request, 'turma/registroAusencia.html')