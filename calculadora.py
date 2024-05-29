import time

def linha():
    print(60*"-")

def pausa(x):
    time.sleep(x)

def menu_principal():
    linha()
    print("1-Conjuntos numéricos\n2- Funções de segundo grau\n3-Funções exponenciais\n4-Matrizes\n0-Sair")
    linha()
    escolha=int(input("Escolha alguma das opções para prosseguir: \n"))
    return escolha

def menu_conjuntos():
    linha()
    print("1-Verificar se o subconjunto a é subconjunto próprio de b(A ∈ B)\n2-Realizar operação de união(A ∪ B)\n3-calcular intersecção(A ∩ B)\n4-calcular diferença(A - B)\n0-Sair")
    linha()
    escolha2=int(input("Escolha umas das opções acima: \n"))
    return escolha2

def menu_funcao_segundo():
    linha()
    print("1-Calcular raízes\n2-Calcular função em x pedido\n3-Calcular vértice\n4-Gerar gráfico\n0-Sair")
    linha()
    escolha2=int(input("Escolha uma das opções acima\n"))
    return escolha2

def menu_funcao_exponencial():
    linha()
    print("1-Verificar se é crescente ou decresecente\n2-Calcular função em x pedido\n3-Gerar gráfico\n0-Sair")
    linha()
    escolha2=int(input("Escolha uma das opções acima\n"))
    return escolha2

def menu_matrizes():
    linha()
    print("1-Verificar se é matriz quadradaz\n2*Multiplicação\n3-Matriz transposta\n0-Sair")
    linha()
    escolha2=int(input("Escolha uma das opções acima\n"))
    return escolha2

# 1. SUBCONJUNTO
def verificar_subconjunto(A, B):
    if A.issubset(B) and A != B:
        print("A é subconjunto próprio de B")
    else:
        print("A não é subconjunto próprio de B")

def realizar_uniao(A, B):
    uniao = A.union(B)
    print("União de A e B:", uniao)

def calcular_intersecao(A, B):
    intersecao = A.intersection(B)
    print("Interseção de A e B:", intersecao)

def calcular_diferenca(A, B):
    diferenca = A.difference(B)
    print("Diferença de A - B:", diferenca)



def gerarMatriz(nlinhas, nColunas):
    matriz=[]
    for i in range(0, nlinhas):
        linha= []
        for j in range(0, nColunas):
            elemento = int(input(f"Informe  Matriz: linha {i} e coluna {j}\n"))
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def imprimirMatriz(matriz):
    for linha in matriz:
        print(linha)


def execucao_menu():
    while True:
        escolha=menu_principal()
        if escolha==0:
            pausa(1)
            print("Saindo do programa...")
            break
        if escolha==1:
            A = set(map(int, input("Digite os elementos do conjunto A separados por espaço: ").split()))
            B = set(map(int, input("Digite os elementos do conjunto B separados por espaço: ").split()))
            while True:
                escolha2=menu_conjuntos()
                if escolha2==0:
                    pausa(1)
                    print("Voltando ao menu principal...")
                    break
                if escolha2==1:
                    pausa(1)
                    print("Verificar se o subconjunto a é subconjunto próprio de b(A ∈ B)")
                    verificar_subconjunto(A, B)
                elif escolha2 == 2:
                    pausa(1)
                    print("Realizar operação de união(A ∪ B)")
                    realizar_uniao(A, B)
                elif escolha2 == 3:
                    pausa(1)
                    print("Calcular intersecção(A ∩ B)")
                    calcular_intersecao(A, B)
                elif escolha2 == 4:
                    pausa(1)
                    print("Calcular diferença(A - B)")
                    if len(B) > len(A):
                        print("Erro: O conjunto B é maior que o conjunto A.")
                    else:
                        calcular_diferenca(A, B)


        elif escolha == 2:
            while True:
                escolha2 = menu_funcao_segundo()
                if escolha2 == 0:
                    pausa(1)
                    print("Voltando ao menu principal...")
                    break
                elif escolha2 == 1:
                    pausa(1)
                    print("Calcular raízes")
                elif escolha2 == 2:
                    pausa(1)
                    print("Calcular função em x pedido")
                elif escolha2 == 3:
                    pausa(1)
                    print("Calcular vértice")
                elif escolha2 == 4:
                    pausa(1)
                    print("Gerar gráfico")


        elif escolha == 3:
            while True:
                escolha2 = menu_funcao_exponencial()
                if escolha2 == 0:
                    pausa(1)
                    print("Voltando ao menu principal...")
                    break
                elif escolha2 == 1:
                    pausa(1)
                    print("Verificar se é crescente ou decrescente")
                elif escolha2 == 2:
                    pausa(1)
                    print("Calcular função em x pedido")
                    pausa(1)
                elif escolha2 == 3:
                    pausa(1)
                    print("Gerar gráfico")

        elif escolha == 4:
            linhas= int(input("Informe o número de linhas "))
            colunas= int(input("Informe o número de colunas "))
            matriz=gerarMatriz(linhas, colunas)
            imprimirMatriz(matriz)
            while True: 
                escolha2 = menu_matrizes()
                if escolha2 == 0:
                    pausa(1)
                    print("Voltando ao menu principal...")
                    break
                elif escolha2 == 1:
                    pausa(1)
                    print("Verificar se é determinante")
                elif escolha2 == 2:
                    pausa(1)
                    print("Multiplicação")
                elif escolha2 == 3:
                    pausa(1)
                    print("Matriz transposta")
execucao_menu()
