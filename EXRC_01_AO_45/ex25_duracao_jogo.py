# Receba a hora de início e de final de um jogo (HH,MM), calcular o tempo do jogo em horas e minutos, sabendo que o tempo máximo é menor que 24 horas e pode começar num dia e terminar noutro.

hi = int(input("Digite as horas do início do jogo: "))
mi = int(input("Digite os minutos do início do jogo: "))
hf = int(input("Digite as horas do fim do jogo: "))
mf = int(input("Digite os minutos do fim do jogo: "))

if hf < hi or (hf == hi and mf < mi):
    hf += 24

if mf < mi:
    mf += 60
    hf -= 1

duracao_horas = hf - hi
duracao_minutos = mf - mi

print(f"O jogo durou {duracao_horas} hora(s) e {duracao_minutos} minuto(s).")