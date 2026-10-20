import os
os.system('cls')
contador = 0
lista_de_alunos= ['pyetro','arthur', 'alexandre','thuanny','michelle']
for alunos in lista_de_alunos:
    print(f"alunos da sala:{alunos}")
    contador += 1

print(f'A sala possui {contador} alunos')
