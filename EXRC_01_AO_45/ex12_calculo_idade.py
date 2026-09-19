#Receba o ano de nascimento e o ano atual. Calcule e mostre a sua idade e quantos anos terá daqui a 17 anos.

ano_nasc = int(input("Digite seu ano de nascimento: "))

ano_atual = int(input("Digte o ano atual: "))

idade_atual = ano_atual - ano_nasc

idade_futura = idade_atual + 17

print(f"Sua idade atual é: {idade_atual} anos")
print(f"Daqui a 17 anos você terá: {idade_futura} anos")