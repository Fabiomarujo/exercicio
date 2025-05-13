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

