#Calcule a quantidade de litros gastos em uma viagem, sabendo que o automóvel faz 12 km/l. Receber o tempo de percurso e a velocidade média.

tempo_percurso = int(input("Digite o tempo do percurso (em horas): "))
velocidade_media = int(input("Digite a velocidade média (em km/h): "))

distancia = tempo_percurso * velocidade_media
litros_gastos = distancia / 12

print(f"--- Resumo da Viagem ---")
print(f"Distância percorrida: {distancia:.2f} km")
print(f"Quantidade de combustível gasta: {litros_gastos:.2f} litros")
