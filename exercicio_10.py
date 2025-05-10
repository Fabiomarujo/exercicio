import os
from pyfiglet import Figlet
from colorama import Fore,Back,Style

def adicionar_itens(dicionario_itens):
    os.system("cls")
    print(Fore.GREEN + "*** CADASTRAR - PRAIAS ***\n" + Fore.WHITE)
    print("Limite de cadastro de 4 Praias por evento.\n")
    Itens_Carrinho = {}
    Template_dados = {"dist_centro":None,"n_veranistas":None,"t_acesso":None}
    cont = 0
    for i in range(0,4):
        cont = cont+1
        Nome_Produto = input("\nQual o nome da PRAIA para cadastrar? ")
        Itens_Carrinho[Nome_Produto] = Template_dados.copy()
        Template_dados["dist_centro"] = input("Qual a distância do Centro? ")
        Template_dados["n-veranistas"] = input("Qual a média de veranistas desta Praia? ")
        Template_dados["t_acesso"] = input("Entre com 0 - Acesso não asfaltado ou 1 - Acesso asfaltado: ")

def RelatorioPraia(DicionarioProduto):
    os.system("cls")
    print("*** SISTEMA - RELATÓRIO PRAIAS CADASTRADAS ***\n")
    
def Voltar_Sair(L_Opcoes):
    L_Opcoes = {1:"[1] - Voltar ao Menu Inicial",2:"[2] - Sair"}
    while(True):
        print("\n*************************\n")
        for a in L_Opcoes:
            print(L_Opcoes[a])
        comando = int(input("\nDigite a opção desejada > "))
        if comando == 1:
            return
        else:   
            os.abort()        
    
   
