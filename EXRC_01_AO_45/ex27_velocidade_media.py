# Receba o número de voltas, a extensão do circuito (em metros) e o tempo de duração (minutos). Calcule e mostre a velocidade média em km/h.

voltas = int(input("Digite o numero de voltas do circuito: "))
exten = int(input("Digite a extensão do circuito (metros): "))
tmp = int(input("Digite o tempo de duração (minutos): "))

km = (voltas * exten) / 1000

horas = tmp / 60

vel_med = km / horas

print(f"A velocidade média em km/h é {vel_med:.1f}")