# Considere que, para cada uma das praias da região, tenha-se registrado o nome da praia, 
# a sua distância do centro da cidade, o número médio de veranistas da última temporada e o 
# tipo de acesso à praia (0 - acesso não asfaltado; 1 - acesso asfaltado). Construa um algoritimo que forneça:

# a) o número de praias que distam mais de 15km do centro:
# b) A quantidade média de veranistas, na última temporada, nas praias com acesso não asfaltado;
# c) O nome e a distância do centro, em km, de todas as praias de acesso asfaltado que tiveram menos de 1000 veranistas.

import os
from pyfiglet import Figlet
from colorama import Fore,Back,Style
from exercicio_10 import adicionar_itens,RelatorioPraia,Dist_Praia,Voltar_Sair
os.system("cls")
f = Figlet()
print(f.renderText('  SIS PRAIAS'))
"\033[0;30;41mTeste\033[m"

titulo1 = "\n\033[0;30;41m                                                        \033[m"
titulo2 = "\n\033[0;30;41m \033[m         SISTEMA DE GERENCIAMENTO DE PRAIAS           \033[0;30;41m \033[m"
titulo3 = "\n\033[0;30;41m                                                        \033[m"
titulo = titulo1+titulo2+titulo3
print(titulo)
nome_usuario = input("\nDigite o nome de usuário: ")
os.system("cls")
print(f"Seja bem vindo(a) \033[0;30;36m{nome_usuario}\033[m\n")
ListaOpcoes = {1:"[1] - Cadastrar Praias ao Dicionário",2:"[2] - Relatório das Praias Cadastradas",3:"[3] - O número de praias que distam mais de 15 km do centro?",4:"[4] - A quantidade média de veranistas, na ultima temporada, nas praias com acesso não asfaltado?",5:"[5] - O nome e a distância do centro, em km, de todas as praias de acesso asfaltado que tiveram menos de 1000 veranistas?",6:"[6] - Sair"}
Itens = {}

while(True):
    print("\033[0;30;32m** DIGITE UM COMANDO PELO NÚMERO **\033[m\n")
    for i in ListaOpcoes:
        print(ListaOpcoes[i])
    comando = int(input("\nDigite a opção > "))
    if comando == 1:
        adicionar_itens(Itens)
        print(Itens)        
    elif comando == 2:
        RelatorioPraia(Itens)
        print(Itens)
    elif comando == 3:
        Dist_Praia(Itens)
        print(Itens)
    elif comando == 4:
        M_Veran_1_Praia(Itens)
        print(Itens)
    elif comando == 5:
        N_Praia(Itens)
        print(Itens)
    elif comando == 6:
        print(Fore.YELLOW + "\nAguarde! Deslogando...\n" + Fore.WHITE)
        os.abort()  

# # Avaliar praias da região
# # entrada 
# # processamento
# # saida

# # classe Praia - caracteristicas da praia
# class Praia:
#     def __init__(self, nome, distancia_centro, media_veranistas, tipo_acesso):
#         self.nome = nome
#         self.distancia_centro = distancia_centro
#         self.media_veranistas = media_veranistas
#         self.tipo_acesso = tipo_acesso


# def obter_praias():
#     praias = []
#     continua = True

#     while continua:
#         nome_praia = input("Informe o nome da praia: ")
#         distancia_centro = float(input("Informe a distância em KM da praia ao centro de sua cidade: "))
#         media_veranistas = int(input("Informe a quantidade média de veranistas da última temporada: "))
#         tipo_acesso_praia = int(input("Informe o tipo de acesso à praia (0 - acesso não asfaltado OU 1 - acesso asfaltado): "))

#         praia = Praia(nome_praia, distancia_centro, media_veranistas, tipo_acesso_praia)
#         praias.append(praia)

#         # valida a resposta (S ou N)
#         continua_reposta = True
#         while continua_reposta:
#             resposta = input("Digite (S)im para nova praia ou (N)ão para sair: ")
#             if len(resposta) > 1 or not (resposta.upper().startswith('S') or resposta.upper().startswith('N')):
#                 print("Responda novamente, por favor! Digite (S)im ou (N)ão: ")
#             elif resposta.upper().startswith('N'):
#                 continua_reposta = False
#                 continua = False
#             else:
#                 continua_reposta = False

#     return praias


# # funcao para contar praias que distam mais de 15km do centro
# def calcular_praias_15km(lista_praias):
#     numero_praias = 0

#     for praia in lista_praias:
#         if praia.distancia_centro > 15:
#             numero_praias = numero_praias + 1
    
#     return numero_praias


# # funcao para calcular a qtd media de veranistas para praias não asfaltadas
# def calcular_media_veranistas(lista_praias):
#     media_veranistas_praias = 0
#     qtd_veranistas = 0
#     qtd_praias = 0

#     for praia in lista_praias:
#         if praia.tipo_acesso == 0:
#             qtd_praias += 1
#             qtd_veranistas = qtd_veranistas + praia.media_veranistas
    
#     if qtd_praias > 0:
#         media_veranistas_praias = qtd_veranistas / qtd_praias
    
#     return media_veranistas_praias


# # funcao para recuperar o nome e a distancia do centro de praias asfaltadas com menos de 1000 veranistas
# def recuperar_praias_asfaltadas_menos_1000_veranistas(lista_praias):
#     praias_asfaltadas = []
#     for praia in lista_praias:
#         if praia.tipo_acesso == 1 and praia.media_veranistas < 1000:
#             praia_selecionada = {"nome": praia.nome, "distancia_centro": praia.distancia_centro}
#             praias_asfaltadas.append(praia_selecionada)
    
#     return praias_asfaltadas


# def exibir_praias(cabecalho, lista_praias):
#     print()
#     print(cabecalho)
#     print('-'*len(cabecalho))
    
#     for praia in lista_praias:
#         print("Praia: ", praia["nome"], " -> ", f'Distância: {praia["distancia_centro"]:02d}', 'Km')
    
#     print()


# # programa principal
# # informar as praias
# praias = []
# praias = obter_praias()

# # processa a letra a
# numero_praias_15km = calcular_praias_15km(praias)

# # processa a letra b
# media_veranistas_praias_nao_asfaltadas = calcular_media_veranistas(praias)

# # processa a letra c
# praias_asfaltadas = recuperar_praias_asfaltadas_menos_1000_veranistas(praias)

# # imprimir resultados
# print()
# print(f"Número de praias que distam mais de 15km do centro: {numero_praias_15km:03d}")
# print(f"Quantidade média de veranistas para praias não asfaltadas: {media_veranistas_praias_nao_asfaltadas:.2f} veranistas")
# exibir_praias("Praias asfaltadas com menos de 1000 veranistas:", praias_asfaltadas)