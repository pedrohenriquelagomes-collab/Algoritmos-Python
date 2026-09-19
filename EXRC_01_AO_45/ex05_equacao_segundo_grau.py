#Receba os coeficientes A, B e C de uma equação do 2o grau (AX2+BX+C=0). Calcule e mostre as raízes reais (considerar que a equação possui 2 raízes reais).

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B:"))
c = int(input("Digite o valor de C:"))

delt = (b * b) - (4*a*c)
x1 = (-b + (delt**0.5)) / (2*a)
x2 = (-b - (delt**0.5)) / (2*a)

print(f"A primeira raiz (X1) é: {x1}")
print(f"A segunda raiz (X2) é: {x2}")