import os

nome: str = ''
nota1: float = 0.0
nota2: float = 0.0
nota3: float = 0.0
nota4: float = 0.0
valor_media: float = 0.0
dir: str = ''
arq: str = ''


def med(n1, n2, n3, n4):
    media: float = 0
    media = (n1 + n2 + n3 + n4)/ 4
    return media

def entrada():
    global nome, nota1, nota2, nota3, nota4, valor_media

    nome = input('Nome do aluno: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    nota3 = float(input('Nota 3: '))
    nota4 = float(input('Nota 4: '))

    valor_media = med(nota1, nota2, nota3, nota4)

    print(f'Média de {nome}: {valor_media}')

    cadastro(nome, nota1, nota2, nota3, nota4, valor_media)

def cadastro(nm, nt1, nt2, nt3, nt4, vlr_med):
    global dir, arq

    linha: str = ''

    linha = (
        nm + ';' +
        str(nt1) + ';' +
        str(nt2) + ';' +
        str(nt3) + ';' +
        str(nt4) + ';' +
        str(vlr_med) + '\n'
    )

    caminho = dir
    arquivo = arq

    escreveArq(caminho, arquivo, linha)

def escreveArq(caminho, arquivo, linha_cad):
    file: str = ''
    tipo: str = ''
    enc: str = ''

    file = os.path.join(caminho, arquivo)
    tipo = 'w'
    enc = 'utf-8'

    if os.path.exists(caminho) and os.path.isdir(caminho):
        if os.path.isfile(file):
            tipo = 'a'

        with open(file, tipo, encoding=enc) as arq_txt:
            arq_txt.write(linha_cad)
 
def main():
    global dir, arq

    contador: int = 0

    dir = 'tmp/exercicios/'
    arq = 'ex21.txt'

    os.makedirs(dir, exist_ok=True)
    os.chmod(dir, 0o744)

    while contador < 5:
        contador += 1
        entrada()

if __name__ == '__main__':
    main()