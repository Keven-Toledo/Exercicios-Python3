def moeda(moeda):
    din = float(moeda)
    return f'R${din:.2f}'


def aumentar(numero, porcentagem, show=False):
    etapa1 = porcentagem / 100
    etapa2 = etapa1 * numero
    etapa3 = numero + etapa2
    if show:
        return moeda(f'{etapa3}')
    else:
        return f'{etapa3}'


def diminuir(numero, porcentagem, show=False):
    etapa1 = porcentagem / 100
    etapa2 = etapa1 * numero
    etapa3 = numero - etapa2
    if show:
        return moeda(f'{etapa3}')
    else:
        return f'{etapa3}'


def dobro(numero, show=False):
    dob = numero * 2
    if show:
        return moeda(f'{dob}')
    else:
        return f'{dob}'


def metade(numero, show=False):
    met = numero / 2
    if show:
        return moeda(f'{met}')
    else:
        return f'{met}'
