# 18 - Receba 2 valores inteiros. Calcule e mostre o resultado da diferença do maior pelo menor valor.

n1 = 0
n2 = 0
res = 0


def ler():
  global n1, n2
  n1 = int(input("Número 1: "))
  n2 = int(input("Número 2: "))


def processar():
  global n1, n2, res
  if n1 > n2:
    res = n1 - n2
  else:
    res = n2 - n1


def mostrar():
  global res
  print("Resultado:", res)


def main():
  ler()
  processar()
  mostrar()


if __name__ == "__main__":
  main()