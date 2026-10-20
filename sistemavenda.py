import os
os.system('cls || clear')
print('digite o valor total')
total = float(input())
if (total> 100) and (total< 500):
 print("você ganhou 5% de desconto", total * 0.05)
if (total > 500):
 print("você ganhou 10% de desconto", total * 0.10)
if(total < 200):
 print('você possui um frete de 15 reais')
  