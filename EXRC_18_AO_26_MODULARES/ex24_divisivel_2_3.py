# 24 - Receba um valor inteiro. Verifique e mostre se é divisível por 2 e 3.

n1 = 0
resultado = ''

def ler():
    global n1
    n1 = int(input("Digite o valor: "))

def calcular():
    global resultado
    if n1 % 2 == 0 and n1 % 3 == 0:
        resultado = "O valor é divisivel por 2 e 3"
    else:
        resultado = "O valor não é divisível por 2 e 3."

def mostrar():
    print(resultado)

def main():
    ler()
    calcular()
    mostrar()


if __name__ == "__main__":
    main()
        
