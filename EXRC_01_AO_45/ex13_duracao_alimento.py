quilos = int(input("Digite os Kilos do alimento: "))

gramas_totais = quilos * 1000

dias = gramas_totais / 50

print(f"Com {quilos}kg de alimento, ele durará {dias:.0f} dias.")