''' 21 - Receba 4 notas bimestrais de um aluno. Calcule e mostre a média aritmética. Mostre a mensagem de acordo com a média:
        a. Se a média for >= 6,0 exibir “APROVADO”;
        b. Se a média for >= 3,0 E < 6,0 exibir “EXAME”;
        c. Se a média for < 3,0 exibir “RETIDO”. '''

n1 = 0.0
n2 = 0.0
n3 = 0.0
n4 = 0.0
media = 0.0

def ler():
    global n1, n2, n3, n4
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    n4 = float(input("Digite a quarta nota: "))

def calcular():
    global n1, n2, n3, n4, media
    media = (n1 + n2 + n3 + n4) / 4

def mostrar():
    if media >= 6:
        print("APROVADO")
    elif media >= 3:
        print("EXAME")
    else:
        print("RETIDO")

def main():
    ler()
    calcular()
    mostrar()


if __name__ == "__main__":
    main()