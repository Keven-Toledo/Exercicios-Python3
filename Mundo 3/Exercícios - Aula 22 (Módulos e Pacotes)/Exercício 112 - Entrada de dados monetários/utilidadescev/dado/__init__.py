def red(txt):
    print(f'\033[1;31m{txt}\033[m')


def leiadinheiro(txt):
    while True:
        entrada = str(input(txt)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == "":
            red(f'ERRO: \"{entrada}\" não é válido')
        else:
            break
    return float(entrada)
