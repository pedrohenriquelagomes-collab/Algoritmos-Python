''' Receba o preço atual e a média mensal de um produto. Calcule e mostre o novo preço sabendo que:
Venda Mensal	   Preço Atual	      Preço Novo
< 500	             < 30	           + 10%
>= 500 e < 1000	    >= 30 e < 80	   +15%
>= 1000	             >= 80	           - 5%
Obs.: para outras condições, preço novo será igual ao preço atual. '''


def ler():
    preco = float(input("Digite o preço atual: "))
    venda = int(input("Digite a média mensal de vendas: "))
    return preco, venda


def calcular(preco, venda):
    if venda < 500 and preco < 30:
        novo_preco = preco * 1.10
    elif venda >= 500 and venda < 1000 and preco >= 30 and preco < 80:
        novo_preco = preco * 1.15
    elif venda >= 1000 and preco >= 80:
        novo_preco = preco * 0.95
    else:
        novo_preco = preco
    return novo_preco


def mostrar(novo_preco):
    print(f"Novo preço: R$ {novo_preco:.2f}")


def main():
    preco, venda = ler()
    novo_preco = calcular(preco, venda)
    mostrar(novo_preco)


if __name__ == '__main__':
    main()