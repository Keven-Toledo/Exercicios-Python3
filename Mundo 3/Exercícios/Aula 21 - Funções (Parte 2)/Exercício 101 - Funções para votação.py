from datetime import date


def voto(nasci):
    ano = date.today().year
    idade = ano - nasci
    if idade < 16:
        return f'Com {idade} anos: Não vota'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: Voto Opcional'
    else:
        return f'Com {idade} anos: Voto Obrigatório'


print(voto(int(input('Ano de Nascimento: '))))
