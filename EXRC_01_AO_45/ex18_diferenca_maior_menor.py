#Receba 2 valores inteiros. Calcule e mostre o resultado da diferença do maior pelo menor valor.

val1 = int(input("Digite o valor do primeiro numero: "))
val2 = int(input("Digite o valor do segundo numero: "))

if val1 > val2:
    result = val1 - val2
else:
    result = val2 - val1

print(f"A diferença do maior numero para o menor é {result}")
