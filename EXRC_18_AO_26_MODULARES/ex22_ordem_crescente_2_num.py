# 22 - Receba 2 valores inteiros e diferentes. Mostre seus valores em ordem crescente.

n1 = 0
n2 = 0
ordem = 0

def ler():
    global n1, n2
    n1 = int(input("Digite o primeiro numero: "))
    n2 = int(input("Digite o primeiro numero: "))

def calcular():
    global n1, n2, ordem
    if n1 < n2:
        ordem = n1, n2
    else:
        ordem = n2, n1

def mostrar():
    print(f"A ordem crescente é: {ordem}")

def main():
    ler()
    calcular()
    mostrar()

if __name__ == "__main__":
    main()
