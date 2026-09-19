# 19 - Receba 2 valores reais. Calcule e mostre o maior deles

n1 = 0
n2 = 0
maior = 0

def ler():
    global n1, n2
    n2 = float(input("Digite o segundo valor:"))
    n1 = float(input("Digite o primeiro valor:"))

def processar():
    global n1, n2, maior
    if n1 > n2:
        maior = n1
    else:
        maior = n2

def mostrar():
    global maior
    print(f"O maior numero é: {maior}")

def main():
    ler()
    processar()
    mostrar()

if __name__ == '__main__':
    main()




