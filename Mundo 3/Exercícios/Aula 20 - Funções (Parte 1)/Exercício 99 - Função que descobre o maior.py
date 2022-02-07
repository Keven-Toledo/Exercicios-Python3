def titulo(txt):
    x = len(txt) + 4
    print('=' * x)
    print(f'{txt: ^{x}}')
    print('=' * x)


def maior(numbers):
    total = len(numbers)
    titulo('Analisando os valores passados...')
    contador = maio = 0

    print('Numeros: ', end='')
    while contador < len(numbers):
        if contador == 1:
            maio = numbers[contador]
        else:
            if numbers[contador] > maio:
                maio = numbers[contador]

        if len(numbers) == 1 and numbers[0] == 0:
            print('Não houveram números informados')
            break

        print(numbers[contador], end=' ')
        contador += 1
    print(f'\nQuantidade de números: {total}')
    print(f'Maior valor: {maio}')


titulo('Crie sua lista')
numeros = list()
cont = 1
while True:
    num = int(input(f'{cont}ª valor: '))
    numeros.append(num)
    continuar = str(input('Continuar? ')).strip().upper()[0]
    if continuar == 'N':
        break
    cont += 1
maior(numeros)

