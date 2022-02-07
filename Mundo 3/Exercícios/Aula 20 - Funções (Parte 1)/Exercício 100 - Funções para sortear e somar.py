from random import randint
from time import sleep


def red(txt):
    cor = f'\033[1;34m{txt}'
    print(cor, end=' ')


def verde(txt):
    cor = f'\033[1;32m{txt}'
    print(cor)


def sorteia(lista):
    print(f'Sorteando 5 valores: ', end='')
    for ciclo in range(0, 5):
        sorteio = randint(1, 10)
        lista.append(sorteio)
        sleep(0.5)
        red(sorteio)


def SomaPar(lista):
    pares = 0
    for numero in lista:
        if numero % 2 == 0:
            pares += numero
    print('\033[m', f'\nA soma dos números pares vale: ', end='')
    sleep(1)
    verde(pares)
    sleep(1)


numeros = list()
sorteia(numeros)
SomaPar(numeros)
