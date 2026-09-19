# 20 - Receba 3 coeficientes A, B e C de uma equação do 2º grau da fórmula AX²+BX+C=0. Verifique e mostre a existência de raízes reais e se caso exista, calcule e mostre.

a = 0.0
b = 0.0
c = 0.0
delta = 0.0
x1 = 0.0
x2 = 0.0

def ler():
    global a, b, c
    a = float(input("Digite o valor de A:"))
    b = float(input("Digite o valor de B:"))
    c = float(input("Digite o valor de C:"))

def calcular():
    global a, b, c, delta, x1, x2
    delta = (b**2) - (4 * a * c)

    if delta >= 0:
        x1 = (-b + (delta**0.5)) / (2 * a)
        x2 = (-b - (delta**0.5)) / (2 * a)

def mostrar():
  global delta, x1, x2
  if delta < 0:
    print("Não existem raízes reais (Delta negativo).")
  elif delta == 0:
    print("Existe apenas 1 raiz real:", x1)
  else:
    print("Raiz X1:", x1)
    print("Raiz X2:", x2)


def main():
  ler()
  calcular()
  mostrar()


if __name__ == "__main__":
  main()
