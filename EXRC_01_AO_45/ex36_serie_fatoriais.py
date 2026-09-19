#Receba um número N. Calcule e mostre a série 1 + 1/1! + 1/2! + ... + 1/N!

n = int(input("Digite um numero: "))
fatorial = 1
soma = 1

for i in range(1, n + 1):
    fatorial *= i
    soma += 1 / fatorial
    print(f"O resultado da série para N = {n} é: {soma:.6f}")
