# 26 - Receba 2 números inteiros. Verifique e mostre se o maior número é múltiplo do menor.

n1 = 0
n2= 0
maior = 0
menor = 0
resultado = ''

def ler():
    global n1, n2
    n1 = (int(input("Digite o primeiro numero: ")))
    n2 = (int(input("Digite o segundo numero: ")))
    

def calcular():
    global maior, menor, resultado
    if n1 > n2:
        maior = n1
        menor = n2
    else:
        maior = n2
        menor = n1

    if maior % menor == 0:
        resultado = 'É multiplo'
    else:
        resultado = 'Não é multiplo'

def mostrar():
    print(resultado)

def main():
    ler()
    calcular()
    mostrar()

if __name__ == '__main__':
    main()
        
