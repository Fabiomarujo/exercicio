from django.shortcuts import render

def listar(request):
    return render(request, 'aluno/listarAlunos.html')

def cadastro(request):
    return render(request, 'aluno/cadastroAluno.html')


