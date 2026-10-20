import os
os.system('cls')

matriz = [[2,5,1,4],
          [7,0,3,8],
          [6,9,2,5]]

numeroLinhas = len(matriz)
numeroColunas = len(matriz[0])
totalElementos = numeroColunas * numeroLinhas

print(f'A matriz tem {numeroLinhas} linhas e {numeroColunas} colunas, possuindo {totalElementos} elementos')

listaDaMatriz = []

for linha in range(numeroLinhas):
    for coluna in range(numeroColunas):
        # print(matriz[linha][coluna])
        listaDaMatriz.append(matriz[linha][coluna])

print(f'A Matriz em Row-Major fica dessa forma:\n {listaDaMatriz}')

linha = int(input('Em qual linha está o número da matriz que você deseja descobrir a nova posição na lista row-major?'))
coluna = int(input('Em qual coluna está o número da matriz que você deseja descobrir a nova posição na lista row-major?'))

offSet = (linha - 1) * numeroColunas + (coluna - 1) 

print(f'O número {matriz[linha-1][coluna-1]} da matriz está na posição {offSet} da lista ROW-MAJOR')