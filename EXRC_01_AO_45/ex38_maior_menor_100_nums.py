#Receba 100 números inteiros reais. Verifique e mostre o maior e o menor valor. Obs.: somente valores positivos.

for i in range(1, 100):
    numero = int(input("Digite um valor: "))
    if numero > 0:
        if i == 1:
            maior = numero
            menor = numero
        elif numero > maior:
            maior = numero
        else:
            menor = numero
    else:
        print("Somente valores positivos")
print(f"O maior numero é {maior}")
print(f"O menor numero é {menor}")

