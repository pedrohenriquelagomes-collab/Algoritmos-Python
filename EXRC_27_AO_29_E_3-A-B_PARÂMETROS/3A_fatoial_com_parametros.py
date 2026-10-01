def fatorial(n):
    fat = 1
    for i in range(1, n + 1):
        fat = fat * i

    return fat

def main():
    n = int(input("Digite um número: "))
    resultado = fatorial(n)
    print("Fatorial:", resultado)

if __name__ == '__main__':
    main()