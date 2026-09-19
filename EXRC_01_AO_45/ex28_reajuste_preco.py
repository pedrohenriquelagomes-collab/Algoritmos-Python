''' Receba o preço atual e a média mensal de um produto. Calcule e mostre o novo preço sabendo que:
Venda Mensal	   Preço Atual	      Preço Novo
< 500	             < 30	           + 10%
>= 500 e < 1000	    >= 30 e < 80	   +15%
>= 1000	             >= 80	           - 5%
Obs.: para outras condições, preço novo será igual ao preço atual. '''

venda_mensal = float(input("Digite a média de venda mensal: "))
preco_atual = float(input("Digite o preço atual do produto: "))

if venda_mensal < 500 and preco_atual < 30:
    novo_preco = preco_atual * 1.10


elif (500 <= venda_mensal < 1000) and (30 <= preco_atual < 80):
    novo_preco = preco_atual * 1.15


elif venda_mensal >= 1000 and preco_atual >= 80:
    novo_preco = preco_atual * 0.95

else:
    novo_preco = preco_atual

print(f"O novo preço do produto é: R$ {novo_preco:.2f}")