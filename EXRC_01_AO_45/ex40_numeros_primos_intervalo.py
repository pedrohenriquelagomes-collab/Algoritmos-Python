
#Receba 2 números inteiros. Verifique e mostre todos os números primos existentes entre eles.

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

if num1 > num2:
    maior = num1
    menor = num2
else:
    maior = num2
    menor = num1

for numero in range(menor, maior):
    if numero > 1:
        primo = True

        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                primo = False
                break
        if primo:
            print(f"Os numeros primos entre {maior} e {menor} são: {numero}")