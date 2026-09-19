# Receba 2 números inteiros. Verifique e mostre se o maior número é múltiplo do menor.

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1

if maior % menor == 0:
    print(f"O numero {maior} é multiplo do numero {menor}.")
else:
    print(f"Os numeros apresentados não são multiplos.")