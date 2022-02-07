from time import sleep


# Criar função titulos
def titulo(txt):
    tamanho = len(txt) + 4
    print('=' * tamanho)
    print(f'{txt: <{tamanho}}')


# Criar função Contadora
def contador(a, b, c):
    if c == 0:
        c = 1
    if c < 0:
        c *= -1

    if a < b:
        an = a
        while an <= b:
            sleep(0.5)
            print(an, end=' ')
            an += c
        print()
    elif a > b:
        an = a
        while an >= b:
            sleep(0.5)
            print(an, end=' ')
            an -= c
        print()


titulo('Contagem de 1 até 10, de 1 em 1')
contador(1, 10, 1)

titulo('Contagem de 10 até 0, de 2 em 2')
contador(10, 0, 2)

titulo('AGORA É SUA VEZ!')
while True:
    print('=' * 20)
    inicio = int(input('Início: '))
    fim = int(input('Fim:    '))
    passo = int(input('Passo:  '))

    if passo == 0:
        titulo(f'Contagem de {inicio} até {fim}, de 1 em 1')
    else:
        titulo(f'Contagem de {inicio} até {fim}, de {passo} em {passo}')

    contador(inicio, fim, passo)
    print('-' * 20)

    pergunta = str(input('Deseja continuar? ')).strip().upper()[0]
    while pergunta not in 'SN':
        print('\033[1;31mInválido!\033[m')
        pergunta = str(input('Deseja continuar? ')).strip().upper()[0]
    if pergunta == 'N':
        break
