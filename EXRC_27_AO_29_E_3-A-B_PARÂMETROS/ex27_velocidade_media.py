# Receba o número de voltas, a extensão do circuito (em metros) e o tempo de duração (minutos). Calcule e mostre a velocidade média em km/h.

def ler():
    voltas = int(input("Digite o numero de voltas do circuito: "))
    extensao = int(input("Digite a extensão do circuito (metros): "))
    tempo = int(input("Digite o tempo de duração (minutos): "))
    return voltas,extensao, tempo

def calcular(voltas, extensao, tempo):
    distancia = (voltas * extensao) / 1000
    tempo_horas = tempo / 60
    velocidade = distancia / tempo_horas
    return velocidade

def mostrar(velocidade):
    print(f"velocidade média {velocidade:.2f} km/h")

def main():
    voltas,extensao,tempo = ler()
    velocidade = calcular(voltas,extensao,tempo)
    mostrar(velocidade)
    

if __name__ == "__main__":
    main()
