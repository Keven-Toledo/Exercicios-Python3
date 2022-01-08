listagem = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-' * 40)
print(f'{"Lista de compras":^40}')
print('-' * 40)

for ciclo in range(0, len(listagem)):
    if ciclo % 2 == 0:
        print(f'{listagem[ciclo]:.<30}', end='')
    else:
        print(f'R${listagem[ciclo]:>7.2f}')

