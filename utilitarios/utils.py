from tiposdeatividades.models import TipoDeAtividade
from titulo.models import Titulo
from aluno.models import aluno
from instrutor.models import Instrutor
from turma.models import Turma

from django.db import connection
from datetime import date
import random

# gerar valor aleatório
def gerar_numero_aleatorio_faixa(inicio, fim):
    return random.randint(inicio, fim)

def gerar_numero_aleatorio_sequencia(lista_valores):
    return random.choice(lista_valores)

# Gerar data aleatória
def gerar_data_aleatoria(tipo_data):
    dia = gerar_numero_aleatorio_faixa(1, 28)
    mes = gerar_numero_aleatorio_faixa(1, 12)
    ano = 0

    if tipo_data == 'inicial':
        ano = gerar_numero_aleatorio_faixa(1970, 2007)
    elif tipo_data == 'final':
        ano = gerar_numero_aleatorio_faixa(2021, 2024)
    elif tipo_data == 'nascimento':
        ano = gerar_numero_aleatorio_faixa(1970, 2000)
    else:
        ano = gerar_numero_aleatorio_faixa(1970, 2025)

    return date(ano, mes, dia)


# Truncar tabelas para zerar o contador de auto-incremento
def truncate_table(nome_tabela): 
    with connection.cursor() as cursor:
        cursor.execute(f'DELETE FROM {nome_tabela}')
        cursor.execute(f'DELETE FROM sqlite_sequence WHERE name = "{nome_tabela}"')

def truncar_tabelas(): 
    truncate_table('turma_turma')
    truncate_table('instrutor_instrutor')
    truncate_table('aluno_aluno')
    truncate_table('titulo_titulo')
    truncate_table('tiposdeatividades_tipodeatividade')
    
def popular_tiposdeatividades():
    lista_tiposdeatividades = []

    for i in range(1,10):
        tiposdeatividades = TipoDeAtividade(descricao='Atividade' + f'{i:02}')
        lista_tiposdeatividades.append(tiposdeatividades)       
    TipoDeAtividade.objects.bulk_create(lista_tiposdeatividades)

def popular_titulo():
    lista_titulo = []

    for i in range(1,10):
        titulo = Titulo(descricao='Titulo' + f'{i:02}')
        lista_titulo.append(titulo)
    Titulo.objects.bulk_create(lista_titulo)

def popular_aluno():
    lista_aluno = []
    for i in range(1,50):
        lista_aluno.append(aluno(nome = 'aluno' + f'{i:02}', datainicial = gerar_data_aleatoria('inicial')))          
    aluno.objects.bulk_create(lista_aluno)

def popular_instrutor():
    lista_instrutor = []

    lista_codigos_titulo = Titulo.objects.values_list('codigo', flat=True)
    codigo_selecionado = gerar_numero_aleatorio_sequencia(lista_codigos_titulo)
    titulo = Titulo.objects.get(pk=codigo_selecionado)

    # print(lista_codigos_titulo)
    # print(codigo_selecionado)
    # print(titulo.codigo)
    # print(titulo.descricao)

    for i in range(1,20):
        lista_instrutor.append(Instrutor(nome = 'instrutor' + f'{i:02}', rg = 'RG' + f'{i:09}', telefone = (f'{gerar_numero_aleatorio_faixa(1, 99999):05}'+"-"+f'{gerar_numero_aleatorio_faixa(1, 9999):04}'), dataNascimento = gerar_data_aleatoria('inicial'), ddd = "("f'{gerar_numero_aleatorio_faixa(1,60):03}'")"))          
    Instrutor.objects.bulk_create(lista_instrutor)

    # for i in range(1, 2):
    #     lista_instrutor.append(
    #         Instrutor(
    #             nome = 'Instrutor ' + f'{i:02}',
    #             data_nascimento =  gerar_data_aleatoria('nascimento'),
    #             rg = 'RG' + f'{i:013}',
    #             #rg = 'RG' + (100000000000000 + i)
    #             #rg = f'{gerar_numero_aleatorio_faixa(   9):015}',
    #             telefone = f'{i:09}',
    #             #telefone = 999999900 + i
    #             #telefone = f'{gerar_numero_aleatorio_faixa(1, 99999999):09}',
    #             ddd = f'{i:03}',
    #             #ddd = 20 + i
    #             #ddd = f'{gerar_numero_aleatorio_faixa(1, 60):03}',
    #             codigo_titulo = titulo
    #         )
    #     )

        # inst = Instrutor(
        #     nome = 'Instrutor ' + f'{i:02}',
        #     data_nascimento =  gerar_data_aleatoria('nascimento'),
        #     rg = 'RG' + f'{i:013}',
        #     #rg = 'RG' + (100000000000000 + i)
        #     #rg = f'{gerar_numero_aleatorio_faixa(   9):015}',
        #     telefone = f'{i:09}',
        #     #telefone = 999999900 + i
        #     #telefone = f'{gerar_numero_aleatorio_faixa(1, 99999999):09}',
        #     ddd = f'{i:03}',
        #     #ddd = 20 + i
        #     #ddd = f'{gerar_numero_aleatorio_faixa(1, 60):03}',
        #     codigo_titulo = titulo
        # )

        # print(inst.id)
        # print(inst.rg)
        # print(inst.data_nascimento)
        # print(inst.codigo_titulo.codigo)
        # print(inst.codigo_titulo.descricao)

    Instrutor.objects.bulk_create(lista_instrutor)

def popular_turma():
    pass