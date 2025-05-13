import os
from pyfiglet import Figlet
from colorama import Fore,Back,Style
Itens_Carrinho = {}
def adicionar_itens(dicionario_itens):
    os.system("cls")
    print(Fore.GREEN + "*** CADASTRAR - PRAIAS ***\n" + Fore.WHITE)
    print("Limite de cadastro de 4 Praias por evento.\n")    
    id = 0
    for i in range(0,3):
        id = id+1              
        Template_dados = {"Nome_Produto":None,"dist_centro":None,"n_veranistas":None,"t_acesso":None}
        Template_dados["Nome_Produto"] = input("\nQual o nome da PRAIA para cadastrar? ")        
        Template_dados["dist_centro"] = input("Qual a distância em Km para o Centro? ")
        Template_dados["n_veranistas"] = input("Qual a média de veranistas desta Praia? ")
        Template_dados["t_acesso"] = input("Entre com 0 - Acesso não asfaltado ou 1 - Acesso asfaltado: ")          
        Itens_Carrinho[id] = Template_dados.copy()
          

def RelatorioPraia(DicionarioProduto):
    os.system("cls")
    print("*** SISTEMA - RELATÓRIO PRAIAS CADASTRADAS ***\n")
    DicionarioProduto = Itens_Carrinho
    print(DicionarioProduto)
    return DicionarioProduto
 
def Dist_Praia(DistanciaPraia):
    os.system("cls")
    print("*** SISTEMA PRAIAS - NÚMERO DE PRAIAS COM MAIS DE 15 KM ***\n")
    DistanciaPraia = Itens_Carrinho
   
    # print(DistanciaPraia[id]["dist_centro"])
    while(True):         
        
        for b in DistanciaPraia:
            total = sum(DistanciaPraia[slice]["dist_centro"].values())
            print(total[b])
        else:
            print("Erro!")
        

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
    
   
