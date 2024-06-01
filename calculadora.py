import time
import matplotlib.pyplot as plt
import numpy as np

def linha():
    print(60 * "-")

def pausa(x):
    time.sleep(x)

def menu_principal():
    linha()
    print("1-Conjuntos numéricos\n2-Funções de segundo grau\n3-Funções exponenciais\n4-Matrizes\n0-Sair")
    linha()
    escolha = int(input("Escolha uma opção para prosseguir: "))
    return escolha
def menu_conjuntos():
    linha()
    print("1-Verificar se o subconjunto a é subconjunto próprio de b(A ⊂ B)\n2-Realizar operação de união(A ∪ B)\n3-Calcular intersecção(A ∩ B)\n4-Calcular diferença(A - B)\n0-Sair")
    linha()
    escolha2 = int(input("Escolha uma das opções acima: \n"))
    return escolha2

def menu_funcao_segundo():
    linha()
    print("1-Calcular raízes\n2-Calcular função em x pedido\n3-Calcular vértice\n4-Gerar gráfico\n0-Sair")
    linha()
    escolha2 = int(input("Escolha uma das opções acima\n"))
    return escolha2

def menu_funcao_exponencial():
    linha()
    print("1-Verificar se é crescente ou decrescente\n2-Calcular função em x pedido\n3-Gerar gráfico\n0-Sair")
    linha()
    escolha2 = int(input("Escolha uma das opções acima\n"))
    return escolha2

def menu_matrizes():
    linha()
    print("1-Verificar se é matriz quadrada e se for, calcular determinante\n2-Multiplicação\n3-Matriz transposta\n0-Sair")
    linha()
    escolha2 = int(input("Escolha uma das opções acima\n"))
    return escolha2

def verificar_subconjunto(A, B):
    if A.issubset(B) and A != B:
        print("A é um subconjunto próprio de B")
    else:
        print("A não é um subconjunto próprio de B")

def realizar_uniao(A, B):
    uniao = A.union(B)
    print(f"União de A e B: {uniao}")

def calcular_intersecao(A, B):
    intersecao = A.intersection(B)
    print(f"Interseção de A e B: {intersecao}")

def calcular_diferenca(A, B):
    if A.issubset(B):
        print("A é um subconjunto de B, portanto a diferença A - B é vazia.")
    else:
        diferenca = A.difference(B)
        print(f"Diferença de A - B: {diferenca}")

def calcular_raizes(a, b, c):
    delta = b**2 - 4*a*c
    raiz1 = (-b + delta**0.5) / (2*a)
    raiz2 = (-b - delta**0.5) / (2*a)
    if delta < 0:
        print(f"A equação não possui raízes reais. delta {delta}, raiz1 {raiz1} e raiz2 {raiz2}")
    elif delta == 0:
        raizReal = -b / (2*a)
        print(f"A equação possui uma raiz real: {raizReal}")
    else:
        print(f"A equação possui duas raízes reais: {raiz1} e {raiz2}")
def calcular_funcao_segundo_grau(a, b, c, x):
    y = a*x**2 + b*x + c
    print(f"O valor da função para x = {x} é y = {y}")

def calcular_vertice(a, b, c):
    xv = -b / (2*a)
    yv = a*xv**2 + b*xv + c
    tipo_vertice = "máximo" if a < 0 else "mínimo"
    print(f"O vértice da parábola é (Xv: {xv}, Yv: {yv}) e é um ponto de {tipo_vertice}")

def gerar_grafico_segundo_grau(a, b, c):
    x = np.linspace(-10, 10, 400)
    y = a*x**2 + b*x + c
    plt.plot(x, y)
    plt.title('Gráfico da Função de Segundo Grau')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.show()

def verificar_crescimento(a):
    if a > 1:
        print("A função é crescente.")
    elif 0 < a < 1:
        print("A função é decrescente.")
    else:
        print("A função não é uma função exponencial válida.")

def calcular_funcao_exponencial(a, b, x):
    fx = a * (b ** x)
    print(f"O valor da função para x = {x} é fx = {fx}")

def gerar_grafico_exponencial(a, b):
    x = np.linspace(-10, 10, 400)
    y = b * (a ** x)
    plt.plot(x, y)
    plt.title('Gráfico da Função Exponencial')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.show()

def gerar_matriz(n_linhas, n_colunas):
    matriz = []
    for i in range(n_linhas):
        linha = []
        for j in range(n_colunas):
            elemento = int(input(f"Informe o elemento da matriz na linha {i + 1} e coluna {j + 1}: "))
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def imprimir_matriz(matriz):
    for linha in matriz:
        print(linha)


def determinante_matriz_quadrada(matriz):
    n_linhas = len(matriz)
    n_colunas = len(matriz[0])

    if n_linhas != n_colunas:
        print("A matriz não é quadrada.")
        return None

    if n_linhas <2 or n_linhas >3:
        print("A função de determinante só suporta matrizes 2x2 e 3x3.")
        return None

    def determinante_2x2(mat):
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]

    def determinante_3x3(mat):
        a = mat[0][0]
        b = mat[0][1]
        c = mat[0][2]
        d = mat[1][0]
        e = mat[1][1]
        f = mat[1][2]
        g = mat[2][0]
        h = mat[2][1]
        i = mat[2][2]
        return a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)

    if n_linhas == 2:
        det = determinante_2x2(matriz)
    elif n_linhas == 3:
        det = determinante_3x3(matriz)

    print(f"O determinante da matriz é: {det}")
    return det

def multiplicar_matrizes(matriz1, matriz2):
    if len(matriz1[0]) != len(matriz2):
        print("Erro: As matrizes não podem ser multiplicadas.")
        return

    resultado = [[0 for _ in range(len(matriz2[0]))] for _ in range(len(matriz1))]
    for i in range(len(matriz1)):
        for j in range(len(matriz2[0])):
            for k in range(len(matriz2)):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]

    print("Resultado da multiplicação:")
    imprimir_matriz(resultado)

def transposta(matriz):
    transposta = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
    print("Matriz transposta:")
    imprimir_matriz(transposta)

def executar_menu():
    while True:
        escolha = menu_principal()
        if escolha == 0:
            pausa(1)
            print("Saindo do programa...")
            break
        elif escolha == 1:
            A = set(map(int, input("Digite os elementos do conjunto A separados por espaço: ").split()))
            B = set(map(int, input("Digite os elementos do conjunto B separados por espaço: ").split()))
            while True:
                escolha2 = menu_conjuntos()
                if escolha2 == 0:
                    pausa(1)
                    print("Voltando ao menu principal...")
                    break
                elif escolha2 == 1:
                    pausa(1)
                    print
                    verificar_subconjunto(A, B)
                elif escolha2 == 2:
                    pausa(1)
                    realizar_uniao(A, B)
                elif escolha2 == 3:
                    pausa(1)
                    calcular_intersecao(A, B)
                elif escolha2 == 4:
                    pausa(1)
                    calcular_diferenca(A, B)
        elif escolha == 2:
            a = float(input("Digite o coeficiente a: "))
            b = float(input("Digite o coeficiente b: "))
            c = float(input("Digite o coeficiente c: "))
            while True:
                escolha2 = menu_funcao_segundo()
                if escolha2 == 0:
                    pausa(1)
                    print("Voltando ao menu principal...")
                    break
                elif escolha2 == 1:
                    pausa(1)
                    calcular_raizes(a, b, c)
                elif escolha2 == 2:
                    pausa(1)
                    x = float(input("Digite o valor de x: "))
                    calcular_funcao_segundo_grau(a, b, c, x)
                elif escolha2 == 3:
                    pausa(1)
                    calcular_vertice(a, b, c)
                elif escolha2 == 4:
                    pausa(1)
                    gerar_grafico_segundo_grau(a, b, c)
        elif escolha == 3:
            a = float(input("Digite o coeficiente a: "))
            b = float(input("Digite o coeficiente b: "))
            while True:
                escolha2 = menu_funcao_exponencial()
                if escolha2 == 0:
                    pausa(1)
                    print("Voltando ao menu principal...")
                    break
                elif escolha2 == 1:
                    pausa(1)
                    verificar_crescimento(a)
                elif escolha2 == 2:
                    pausa(1)
                    x = float(input("Digite o valor de x: "))
                    calcular_funcao_exponencial(a, b, x)
                elif escolha2 == 3:
                    pausa(1)
                    gerar_grafico_exponencial(a, b)
        elif escolha == 4:
            n_linhas = int(input("Informe o número de linhas da matriz: "))
            n_colunas = int(input("Informe o número de colunas da matriz: "))
            matriz = gerar_matriz(n_linhas, n_colunas)
            imprimir_matriz(matriz)
            while True:
                escolha2 = menu_matrizes()
                if escolha2 == 0:
                    pausa(1)
                    print("Voltando ao menu principal...")
                    break
                elif escolha2 == 1:
                    pausa(1)
                    determinante_matriz_quadrada(matriz)
                elif escolha2 == 2:
                    pausa(1)
                    n_linhas2 = int(input("Informe o número de linhas da segunda matriz: "))
                    n_colunas2 = int(input("Informe o número de colunas da segunda matriz: "))
                    matriz2 = gerar_matriz(n_linhas2, n_colunas2)
                    imprimir_matriz(matriz2)
                    multiplicar_matrizes(matriz, matriz2)
                elif escolha2 == 3:
                    pausa(1)
                    transposta(matriz)

executar_menu()
