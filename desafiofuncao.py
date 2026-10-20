import os
os.system('cls')

def pedir_nome():
    nome = str(input('digite seu nome:'))
    print(f'seu nome é {nome}')
pedir_nome()

def pedir_nome_parametro(nome):
    return f'seu nome é {nome}'
nome_da_pessoa = pedir_nome_parametro('pyetro')
print(nome_da_pessoa)
