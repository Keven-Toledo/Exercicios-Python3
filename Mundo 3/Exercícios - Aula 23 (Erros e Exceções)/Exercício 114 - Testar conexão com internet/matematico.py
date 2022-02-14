def red(txt):
    print(f'\033[1;31m{txt}\033[m')


def green(txt):
    print(f'\033[1;32m{txt}\033[m')


def leiaint(txt):
    while True:
        try:
            numero = int(input(txt))
        except (ValueError, TypeError):
            red('Erro: O número não é inteiro válido!')
        except KeyboardInterrupt:
            red('O usuário desistiu de informar valores')
            return 0
        else:
            return numero


def leiafloat(txt):
    while True:
        try:
            numero = float(input(txt))
        except (TypeError, ValueError):
            red('Erro: O valor não é válido!')
            continue
        except KeyboardInterrupt:
            red('O usuário desistiu de informar valores')
            return 0
        else:
            return numero
