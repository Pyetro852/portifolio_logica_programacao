import os
os.system('cls')

prateleiras = ['Prateleira1', 'Prateleira2', 'Prateleira3', 'Prateleira4', 'Prateleira5']

produtos = ['Produto1', 'Produto2', 'Produto3', 'Produto4']

# print(prateleiras[0], produtos[0])
# print(prateleiras[0], produtos[1])
# print(prateleiras[0], produtos[2])
# print(prateleiras[0], produtos[3])
# print(prateleiras[1], produtos[0])

for i in range(5):
    for j in range(4):
        print(prateleiras[i],produtos[j])

# for prateleira in prateleiras:
#     for produto in produtos:
#         print(prateleira, produto)

# print(f'Prateleira , produto')