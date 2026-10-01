# Receba o tipo de investimento (1 = poupança e 2 = renda fixa) e o valor do investimento. Calcule e mostre o valor corrigido em 30 dias sabendo que a poupança = 3% e a renda fixa = 5%. Demais tipos não serão considerados.

def ler():
    tipo = int(input("Digite o tipo de investimento (1 - Poupança / 2 - Renda Fixa): "))
    valor = float(input("Digite o valor do investimento: "))

    return tipo, valor


def calcular(tipo, valor):
    if tipo == 1:
        valor_corrigido = valor * 1.03

    elif tipo == 2:
        valor_corrigido = valor * 1.05

    return valor_corrigido


def mostrar(valor_corrigido):
    print(f"Valor corrigido: R$ {valor_corrigido:.2f}")


def main():
    tipo, valor = ler()
    valor_corrigido = calcular(tipo, valor)
    mostrar(valor_corrigido)


if __name__ == '__main__':
    main()