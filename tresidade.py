import os
os.system('cls')
soma = 0
for contador in range(1,4):
    item = float(input(f'Digite o valor do item {contador}: '))
    soma = soma +item
print(soma)
