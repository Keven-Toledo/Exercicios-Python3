def red(txt):
    print(f'\033[1;31m{txt}\033[m')


def blue(txt):
    print(f'\033[1;34m{txt}\033[m')


def leiaint(txt):
    while True:
        try:
            numero = int(input(txt))
        except (ValueError, TypeError):
            red('Erro: Número não informado!')
        except KeyboardInterrupt:
            red('O usuário desistiu de informar valores')
            break
        else:
            return numero


def titulo(txt):
    linha = len(txt) + 20
    print('-' * linha)
    print(f'{txt:^{linha}}'.upper())
    print('-' * linha)


def menu(cabecalho, lista):
    titulo(cabecalho)
    for indice, opcao in enumerate(lista):
        print(f'\033[1;34m{indice+1} - {opcao}\033[m')
    print('-' * (len(cabecalho) + 20))
    escolha = leiaint('\033[1;32mSua Opcão: \033[m')
    return escolha
