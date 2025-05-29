from django.shortcuts import render

def cadinstrutor(request):
    return render(request, 'instrutor/cadastroInstrutor.html')

def listarInst(request):
    return render(request, 'instrutor/listarInsrutores.html')

