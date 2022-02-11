def red(txt):
    print(f'\033[1;31m{txt} \033[m')


def leiaint(msg):
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            break
        else:
            red('Erro! Digite um número inteiro.')
    return valor


n = leiaint('Digite um número: ')
print(f'Você digitou {n}')
