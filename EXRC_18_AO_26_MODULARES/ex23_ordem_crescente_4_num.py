# 23 - Receba 3 valores obrigatoriamente em ordem crescente e um 4º valor não necessariamente em ordem. Mostre os 4 números em ordem crescente.

n1 = 0
n2 = 0
n3 = 0
n4 = 0
ordem = 0

def ler():
    global n1, n2, n3, n4
    n1 = int(input("Digite o 1º valor: "))
    n2 = int(input("Digite o 2º valor (maior que o 1º): "))
    n3 = int(input("Digite o 3º valor (maior que o 2º): "))
    n4 = int(input("Digite o 4º valor: "))

def calcular():
    global ordem
    if n4 < n1:
        ordem = n4, n1, n2, n3
    elif n4 < n2:
        ordem = n1, n4, n2, n3
    elif n4 < n3:
        ordem = n1, n2, n4, n3
    else:
        ordem = n1, n2, n3, n4

def mostrar():
    print(ordem)



def main():
    ler()
    calcular()
    mostrar()

if __name__ == "__main__":
    main()