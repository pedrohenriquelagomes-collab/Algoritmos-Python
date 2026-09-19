#Receba 2 valores inteiros e diferentes. Mostre seus valores em ordem crescente.

print("---DIGITE DOIS VALORES PARA FICAR EM ORDEM CRESCENTE---")
n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))

if n1 >= n2:
    print(f"Os valores em ordem crescente são: {n2},{n1}")
else:
    print(f"Os valores em ordem crescente são: {n1},{n2}")
