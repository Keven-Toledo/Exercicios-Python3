def red(txt):
    print(f'\033[1;31m{txt} \033[m')


def leiaint(nume):
    while True:
        num = str(input(nume))
        if num.isnumeric():
            valor = int(num)
            break
        else:
            red('Erro! Digite um número inteiro.')
    return valor


n = leiaint('Digite um número: ')
print(f'Você digitou {n}')
