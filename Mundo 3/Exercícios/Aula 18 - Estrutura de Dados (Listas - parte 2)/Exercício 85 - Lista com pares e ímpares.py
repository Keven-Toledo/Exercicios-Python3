lista_principal = [[], []]
for ciclos in range(1, 8):
    numero = int(input(f'Digite o {ciclos}º número: '))
    if numero % 2 == 0:
        lista_principal[0].append(numero)
    else:
        lista_principal[1].append(numero)

print(f'Lista dos Pares: {sorted(lista_principal[0])}')
print(f'Lista dos ímpares: {sorted(lista_principal[1])}')
