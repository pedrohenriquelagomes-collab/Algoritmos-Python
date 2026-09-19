# Receba um número. Calcule e mostre a série 1 + 1/2 + 1/3 + ... + 1/N.

numero = int(input("Digite um numero: "))
soma = 0

for i in range(1, numero + 1):
    soma += 1 / i

print (f"O valorm da soma é {soma:.4f}")