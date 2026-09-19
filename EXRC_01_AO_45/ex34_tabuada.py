# Receba um número. Calcule e mostre os resultados da tabuada desse número.

numero = int(input("Digite um numero para mostrar sua tabuada: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
