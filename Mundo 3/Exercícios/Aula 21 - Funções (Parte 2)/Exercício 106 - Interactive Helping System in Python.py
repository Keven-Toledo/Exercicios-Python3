from time import sleep
cores = ['\033[m',         # 0 — sem cor
         '\033[0;30;41m',  # 1 — vermelho
         '\033[0;30;42m',  # 2 — verde
         '\033[0;30;43m',  # 3 — amarelo
         '\033[0;30;44m',  # 4 — azul
         '\033[1;106m',  # 5 — roxo
         '\033[1;30m'      # 6 — branco
         ]


def helping(txt):
    titulo(f'Acessando o manual do comando {txt}', 4)
    sleep(0.5)
    print(cores[3], end='')
    help(txt)
    print(cores[0], end='')
    sleep(1)


def titulo(txt, cor=0):
    tam = len(txt) + 4
    print(cores[cor], end='')
    print('=' * tam)
    print(f'{txt:^{tam}}')
    print('=' * tam)
    print(cores[0], end='')


while True:
    titulo('Sistema de Ajuda Pyhelp', 2)
    fun = str(input('Biblioteca ou Função: '))
    if fun == 'fim':
        break
    helping(fun)
titulo('Tchau', 1)
