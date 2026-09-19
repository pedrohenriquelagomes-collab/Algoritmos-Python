#Receba um valor inteiro. Verifique e mostre se é divisível por 2 e 3.

vlrInt = int(input("Digite um valor inteiro para ser verificado: "))
if vlrInt % 2 == 0 and vlrInt % 3 == 0:
    print(f"O numero {vlrInt} é divisivel por 2 e por 3.")
else:
    print(f"O numero {vlrInt} não é divisivel por 2 ou por 3.")
