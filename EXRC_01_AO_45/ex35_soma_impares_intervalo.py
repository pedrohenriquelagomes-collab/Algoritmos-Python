# Receba 2 números inteiros, verifique qual o maior entre eles. Calcule e mostre o resultado da somatória dos números ímpares entre esses valores.

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
soma = 0

if num1 > num2:
    maior = num1
    menor = num2
else:
    maior = num2
    menor = num1

for i in range(menor, maior + 1):
    if i % 2 !=0:
        soma += i
        print(f"numero impar à ser somado = {i}")
        print(f"A somatoria é {soma}")