#Receba 3 valores obrigatoriamente em ordem crescente e um 4º valor não necessariamente em ordem. Mostre os 4 números em ordem crescente.

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o tercerio numero: "))
n4 = int(input("Digite o quarto numero: "))

if n4 > n3:
    print(f"Ordem crecente: {n1},{n2},{n3},{n4}")
elif n4 < n3:
    print(f"Ordem crecente: {n1},{n2},{n4},{n3}")
elif n4 < n2:
    print(f"Ordem crecente: {n1},{n4},{n2},{n3}")
else:
    print(f"Ordem crecente: {n4},{n3},{n2},{n3}")

