matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
soma_pares = soma_coluna = 0
segunda_lista = list()

# Inserindo valores na Matriz e somando pares e terceira coluna
for lista in range(0, 3):
    for posicao in range(0, 3):
        numero = int(input(f'Digite um valo para [{lista}, {posicao}]: '))
        matriz[lista][posicao] = numero
        if numero % 2 == 0:
            soma_pares += numero
        if posicao == 2:
            soma_coluna += numero
        if lista == 1:
            segunda_lista.append(numero)

# Printando bonitinho
print('-=' * 25)
for lista in range(0, 3):
    for posicao in range(0, 3):
        print(f'[{matriz[lista][posicao]:^5}]', end='')
    print()
print('-=' * 25)

# Apresentando dados
print(f'A soma dos Nº Pares vale: {soma_pares}')
print(f'A soma dos Nº da 3º coluna vale: {soma_coluna}')
print(f'O maior valor da segunda lista/linha foi: {max(segunda_lista)}')
