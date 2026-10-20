import os
os.system('cls')

# Pontuações do Jogador
pontuacao = [80, 100, 60, 120]

# Inicializando as variáveis para coletar estatísticas
soma = 0
maior = pontuacao[0] #80
menor = pontuacao[0] #80

# # 1º Rodada
# soma = soma + pontuacao[0]
# #2º Rodada
# soma = soma + pontuacao[1]
# #3º Rodada
# soma = soma + pontuacao[2]
# #4º Rodada
# soma = soma + pontuacao[3]

# if (pontuacao[0] > maior):
#     maior = pontuacao[0]
# if (pontuacao[1] > maior):
#     maior = pontuacao[1]
# if (pontuacao[2] > maior):
#     maior = pontuacao[2]
# if (pontuacao[3] > maior):
#     maior = pontuacao[3]

# for i in range(4):
    
#     if pontuacao[i] > maior:
#         maior = pontuacao[i]

#     soma += pontuacao[i]
# print(maior)
# print(soma)

# for i in range(4):
    
#     if pontuacao[i] < menor:
#         menor = pontuacao[i]

#     soma += pontuacao[i]
# print(menor)
# print(soma)

for i in range(4):
    if pontuacao[i] > maior:
        maior = pontuacao[i]
    if pontuacao[i] < menor:
        menor = pontuacao[i]
    soma += pontuacao[i]

print(maior)
print(menor)
print(soma)