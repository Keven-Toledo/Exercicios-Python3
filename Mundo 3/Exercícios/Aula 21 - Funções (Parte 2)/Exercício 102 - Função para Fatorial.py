def fatorial(num, show=False):
    """
    Calcula o fatorial de um número
    :param num: O número a ser calculado
    :param show: (Opcional) mostrar a conta
    :param return: O valor do Fatorial de um número.
    """
    fat = 1
    for ciclo in range(num, 0, -1):
        if show:
            print(ciclo, end='')
            if ciclo > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fat *= ciclo
    return fat


print(fatorial(5, True))
help(fatorial)
