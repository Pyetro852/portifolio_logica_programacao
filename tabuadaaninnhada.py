import os
os.system('cls || clear')

# Loop externo para os números da tabuada (1 a 10)
for i in range(1, 11):
    print(f"Tabuada do {i}")
    
    # Loop interno para as multiplicações (1 a 10)
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
