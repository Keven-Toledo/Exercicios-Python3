def titulo():
    x = len('Analisando os valores passados...') + 4
    print('=' * x)
    print(f'{"Analisando os valores passados...": ^{x}}')
    print('=' * x)


def maior(* var):
    cres = sorted(var)
    maximo = max(var)
    total = len(var)
    titulo()
    for n in cres:
        if len(cres) == 1 and n == 0:
            print('Não houveram números informados')
            break
    else:
        print('Numeros ordenados: ', end='')
        for numero in cres:
            print(f'{numero}', end=' ')
        print(f'\nTotal de números: {total}')
        print(f'Maior valor: {maximo}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
