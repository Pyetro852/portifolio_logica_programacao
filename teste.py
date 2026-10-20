import os
os.system('cls || clear')

print("digite sua idade")
idade = input()
print(" idade <16 nao pode entrar")
if (idade <16):
    print(" nao pode entrar")
if (idade >=17):
    print(" pode entrar junto dos responsaveis")  
if (idade >18):
    print(" entrada liberada")