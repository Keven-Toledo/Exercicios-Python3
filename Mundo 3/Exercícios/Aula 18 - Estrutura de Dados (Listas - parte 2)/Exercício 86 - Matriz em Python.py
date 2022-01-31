matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# Inserir valor na posição X e Y
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

# Print bonitinho
print('-=' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
