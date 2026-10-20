import os
os.system('cls')

#acumulador = contador = 0

acumulador = 0
contador = 0

for i in range(3):
    print('Bem vindo')
    item = float(input('Digite o valor do item '))
    contador = contador + 1
    acumulador += item
    #acumulador = acumulador + item
    #contador += 1

print(f'Rodou {contador} vezes')
print(f'O preço final foi de R${acumulador}')