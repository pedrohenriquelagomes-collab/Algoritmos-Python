#Receba um número inteiro. Calcule e mostre o seu fatorial.

numero = int(input("Digite um numero inteiro: "))
fatorial = 1

for i in range(numero, 0, -1):
    fatorial *= i

print(f"O fatorial de {numero} é {fatorial}")