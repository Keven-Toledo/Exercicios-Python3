def titulo(txt):
    print('=' * 32)
    print(f'{txt:^32}')
    print('=' * 32)


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


def resumo(num, aumento, desconto):
    desc = int(desconto)
    aument = int(aumento)
    numero = float(num)
    tabela = {
        'Preço analisado:': moeda(numero),
        'Dobro do Preço:': dobro(numero, True),
        'Metade do preço:': metade(numero, True),
        'de Aumento': aumentar(numero, aument, True),
        'de Desconto': diminuir(numero, desc, True)
    }
    titulo('INFORMAÇÕES')
    for topico, info in tabela.items():
        if topico in 'de Aumento':
            print(f'{aumento}% {topico:<18}{info:>7}')
        elif topico in 'de Desconto':
            print(f'{desconto}% {topico:<18}{info:>7}')
        else:
            print(f'{topico:<22}{info:>7}')
    print('=' * 32)
