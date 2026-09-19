''' Calcule a quantidade de grãos contidos em um tabuleiro de xadrez onde:
Casa: 1 2 3 4 ... 64
Qdte: 1 2 4 8 ... N '''

graos_na_casa = 1  
total_de_graos = 0

for casa in range(1, 65): 
    total_de_graos += graos_na_casa  
    print(f"Casa {casa}: {graos_na_casa} grãos")
    
    graos_na_casa *= 2 
    
print(f"\nTotal acumulado no tabuleiro: {total_de_graos}")
