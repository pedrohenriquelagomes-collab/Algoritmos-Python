# 25 - Receba a hora de início e de final de um jogo (HH,MM), calcular o tempo do jogo em horas e minutos, sabendo que o tempo máximo é menor que 24 horas e pode começar num dia e terminar noutro.

hi = 0
mi = 0 
hf = 0
mf = 0
dur_h = 0 
dur_m = 0

def ler():
    global hi, mi, hf, mf
    hi = int(input("Digite as horas que o jogo começou: "))
    mi = int(input("Digite os minutos que o jogo começou: "))
    hf = int(input("Digite as horas que o jogo terminou: "))
    mf = int(input("Digite os minutos que o jogo terminou: "))

def calcular():
    global hi, mi, hf, mf, dur_h, dur_m
    if (hf < hi or (hf == hi and mf < mi)):
        hf += 24
    if mf < mi:
        mf += 60
        hf -= 1

    dur_h = hf - hi
    dur_m = mf - mi
    

def mostrar():
    global dur_h, dur_m
    print(f"O jogo durou {dur_h}:{dur_m:02d}")

def main():
    ler()
    calcular()
    mostrar()

if __name__ == "__main__":
    main()