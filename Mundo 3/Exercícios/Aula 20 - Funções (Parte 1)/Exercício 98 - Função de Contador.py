from time import sleep


# Criar função titulos
def titulo(txt):
    tamanho = len(txt) + 4
    print('=' * tamanho)
    print(f'{txt: <{tamanho}}')


# Criar função Contadora
def contador(a, b, c):
    if a < b:
        if c != 0:
            an = a
            while an <= b:
                sleep(0.3)
                print(an, end=' ')
                an = an + c
            print()
        else:
            an = a
            while an <= b:
                sleep(0.3)
                print(an, end=' ')
                an = an + 1
            print()
    elif a > b:
        if c > 0:
            an = a
            while an >= b:
                sleep(0.2)
                print(an, end=' ')
                an = an - c
            print()
        elif c < 0:
            an = a
            while an >= b:
                sleep(0.2)
                print(an, end=' ')
                an = an - (-c)
            print()
        elif c == 0:
            an = a
            while an >= b:
                sleep(0.2)
                print(an, end=' ')
                an = an - 1
            print()


titulo('Contagem de 1 até 10')
contador(1, 10, 1)

titulo('Contagem de 10 até 0')
contador(10, 0, 2)

titulo('AGORA É SUA VEZ!')
while True:
    print('=' * 20)
    inicio = int(input('Início: '))
    fim = int(input('Fim:    '))
    passo = int(input('Passo:  '))
    if passo != 0:
        titulo(f'Contagem de {inicio} até {fim} (passo = {passo})')
    else:
        titulo(f'Contagem de {inicio} até {fim} (passo = 1)')
    contador(inicio, fim, passo)
    print('-' * 20)
    pergunta = str(input('Deseja continuar? ')).strip().upper()[0]
    while pergunta not in 'SN':
        print('\033[1;31mInválido!\033[m')
        pergunta = str(input('Deseja continuar? ')).strip().upper()[0]
    if pergunta == 'N':
        break
