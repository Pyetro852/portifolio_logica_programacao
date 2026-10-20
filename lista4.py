import os
os.system('cls')

carros = ["gol quadrado", "astra", "vectra", "nivus"]

carros += ["creta"] #["gol quadrado", "astra", "vectra", "nivus", "creta"]

carros.append("civic") #["gol quadrado", "astra", "vectra", "nivus", "creta", "civic"]
#append adiciona item no final da lista

carros.insert(0, "fusca") #["fusca","gol quadrado", "astra", "vectra", "nivus", "creta", "civic"]
#insert adiciona um item a uma determinada posição
print(carros)

carros.remove("astra") #["fusca","gol quadrado", "vectra", "nivus", "creta", "civic"]
#remove deleta um item pelo seu valor
print(carros)

carros.pop(2)
#pop remove um item pelo seu index (posição)
print(carros) #["fusca","gol quadrado", "nivus", "creta", "civic"]

print(len(carros))
#len retorna o comprimento da lista
