#Receba o valor de um depósito em poupança. Calcule e mostre o valor após 1 mês de aplicação sabendo que rende 1,3% a. m.

deposito = int(input("Digite o valor do seu depósito: R$"))

valor_novo = deposito * 1.013 

print(f"O valor após 1 mês sera: R${valor_novo:.2f}")