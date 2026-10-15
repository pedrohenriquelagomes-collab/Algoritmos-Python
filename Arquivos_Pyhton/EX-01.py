import os

valor: int = 0
dir: str = ''
arq: str = ''
arq: str = ''


def mult(vlr, tab):
    res = vlr * tab
    return res

def grava(c, rslt):
    global dir, arq

    file: str = ''
    tipo: str = ''
    enc: str = ''   
    linha: str = ''

    file = os.path.join(dir, arq)
    tipo = 'w'
    enc = 'utf-8'
    linha = str(rslt) + '\n'

    if os.path.exists(dir) and os.path.isdir(dir):
        if os.path.isfile(file):
            if c > 0:
                tipo = 'a'

        with open(file, tipo, encoding=enc) as arquivo:
            arquivo.write(linha)



def main():
    global valor, dir, arq

    contador: int = 0
    result: int = 0
   
    dir = '/tmp/exercicios/'
    arq = 'ex34.txt'

    os.makedirs(dir, exist_ok=True)
    os.chmod(dir, 0o744)
   

    valor = int(input('Digite um valor entre 1 e 10: '))

    while contador < 10:
        contador += 1
        result = mult(valor, contador)
        grava(contador, result)




if __name__ == '__main__':
    main()