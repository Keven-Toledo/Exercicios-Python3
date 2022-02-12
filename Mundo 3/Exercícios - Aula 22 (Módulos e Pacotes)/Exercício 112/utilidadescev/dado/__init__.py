def red(txt):
    print(f'\033[1;31m{txt}\033[m')


def leiadinheiro(txt):
    valor = 0
    while True:
        num = str(input(txt))
        if num.isnumeric():
            valor = float(num)
            break
        else:
            if num.strip() == '':
                red(f'Erro: " " não é válido')
            else:
                red(f'Erro: {num} não é válido')
    return valor
