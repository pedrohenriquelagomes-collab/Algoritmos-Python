# Receba um número inteiro. Calcule e mostre a série de Fibonacci até o seu N’nésimo termo.

n = int(input("Digite um número N: "))

anterior = 0
atual = 1

for i in range(1, n + 1):
    print(atual)  
    prox = anterior + atual 
    anterior = atual         
    atual = prox