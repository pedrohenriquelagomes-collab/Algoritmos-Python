def fatorial(n):
    fat = 1
    for i in range(1, n + 1):
        fat = fat * i

    return fat

def dividir(n1, n2):
    return n1 / n2

def main():
    n = int(input("Digite o valor de N: "))
    soma = 1
    for i in range(1, n + 1):
        fat = fatorial(i)
        parcela = dividir(1, fat)
        soma = soma + parcela

    print("Resultado:", soma)
    

if __name__ == '__main__':
    main()