def moeda(moeda):
    din = float(moeda)
    return f'R${din:.2f}'


def aumentar(numero, porcentagem):
    etapa1 = porcentagem / 100
    etapa2 = etapa1 * numero
    etapa3 = numero + etapa2
    return f'{etapa3}'


def diminuir(numero, porcentagem):
    etapa1 = porcentagem / 100
    etapa2 = etapa1 * numero
    etapa3 = numero - etapa2
    return f'{etapa3}'


def dobro(numero):
    dob = numero * 2
    return f'{dob}'


def metade(numero):
    met = numero / 2
    return f'{met}'
