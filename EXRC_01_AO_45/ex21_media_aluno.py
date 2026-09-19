'''     21. Receba 4 notas bimestrais de um aluno. Calcule e mostre a média aritmética. Mostre a mensagem de acordo com a média:
        a. Se a média for >= 6,0 exibir “APROVADO”;
        b. Se a média for >= 3,0 E < 6,0 exibir “EXAME”;
        c. Se a média for < 3,0 exibir “RETIDO”. '''

b1 = int(input("Digite a nota do primeiro bimestre: "))
b2 = int(input("Digite a nota do segundo bimestre: "))
b3 = int(input("Digite a nota do terceiro bimestre: "))
b4 = int(input("Digite a nota do quarto bimestre: "))

media = ((b1 + b2 + b3 + b4) / 4)

if media >= 6:
    print("APROVADO")
elif media >= 3:
    print("EXAME")
else:
    print("RETIDO")