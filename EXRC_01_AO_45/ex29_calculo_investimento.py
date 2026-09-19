# Receba o tipo de investimento (1 = poupança e 2 = renda fixa) e o valor do investimento. Calcule e mostre o valor corrigido em 30 dias sabendo que a poupança = 3% e a renda fixa = 5%. Demais tipos não serão considerados.

escolha = None

while escolha != 0:
    print("----ESCOLHA O TIPO DE INVESTIMENTO----")
    print("1 - poupança")
    print("2 - renda fixa")
    print("0 - sair")
    escolha = int(input("Digite sua escolha: "))

    if escolha == 1:
        valor_poupanca = int(input("Insira o valor: R$"))
        valor_crgd = (valor_poupanca * 1.03)
        print(f"O valor corrigido em 30 dias é R${valor_crgd:.2f}")
    elif escolha == 2:
        valor_renda = int(input("Insira o valor: R$"))
        valor_crgd = (valor_renda * 1.05)
        print(f"O valor corrigido em 30 dias é R${valor_crgd:.2f}")
    elif escolha == 0:
        print("Saindo....")



