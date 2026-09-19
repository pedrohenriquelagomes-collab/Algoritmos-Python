#Receba 3 coeficientes A, B e C de uma equação do 2º grau da fórmula AX²+BX+C=0. Verifique e mostre a existência de raízes reais e se caso exista, calcule e mostre.

a = int(input("Digite o valor de A: "))


if a == 0:
    print("O valor de A não pode ser zero em uma equação do 2º grau.")
else:
    b = int(input("Digite o valor de B: "))
    c = int(input("Digite o valor de C: "))

    delt = (b * b) - (4 * a * c)

    if delt < 0:
        print(f"O valor de delta é {delt}, a equação não possui raízes reais.")
    elif delt == 0:
        x1 = -b / (2 * a)
        print(f"O valor de delta é 0. A equação possui apenas uma raiz: {x1:.2f}")
    else:
        x1 = (-b + (delt ** 0.5)) / (2 * a)
        x2 = (-b - (delt ** 0.5)) / (2 * a)
        print(f"O valor da primeira raiz é: {x1:.2f}")
        print(f"O valor da segunda raiz é: {x2:.2f}")

