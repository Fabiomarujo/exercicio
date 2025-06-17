from django.shortcuts import render, redirect
from instrutor.forms import InstrutorForm, InstrutorAtualizarForm
from instrutor.models import Instrutor

def listar(request):
    lista_instrutor = Instrutor.objects.all()
    contexto = {
        'instrutor': lista_instrutor,
    }
    return render(request, 'instrutor/listarInstrutores.html', context=contexto)

def cadastro(request):
    return render(request, 'instrutor/cadastroInstrutor.html')

def cadastrar(request):
    form = InstrutorForm(request.POST)
    if form.is_valid():
        dados_instrutor = form.cleaned_data       
        instrutor = Instrutor(
            rg=dados_instrutor['rg'],
            nome=dados_instrutor['nome'],
            dataNascimento=dados_instrutor['dataNascimento'],
            telefone=dados_instrutor['telefone'],
            ddd=dados_instrutor['ddd']
        )
        instrutor.save()
    return render(request, 'instrutor/cadastroInstrutor.html')

def excluir(request, codigo):
    instrutor = Instrutor.objects.get(pk=codigo)

    instrutor.delete()

    return redirect('instrutor:listar')

# Carregar instrutor para ATUALIZAR
def carregar_instrutor(request, codigo):
    # obter titulo e atualizar baseado no codigo informado
    instrutor = Instrutor.objects.get(pk=id)
    contexto ={
        'instrutor': instrutor,
    }
    return render(request, 'instrutor/atualizarInstrutor.html', context=contexto)

# Atualizar a base de dados para o titulo selecionado
def atualizar(request):
    if request.method == 'POST':
        form = InstrutorAtualizarForm(request.POST)
        if form.is_valid():
            dados_instrutor = form.cleaned_data
            codigo = dados_instrutor['codigo']
            instrutor = Instrutor.objects.get(pk=codigo)
            instrutor.descricao = dados_instrutor['descricao']
            instrutor.save()
        # Apresenta no console os erros 
        else:
            print(form.errors)
    return redirect('instrutor:listar')
    
