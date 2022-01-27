valores = list()
maior = menor = 0
valor = ''
for ciclo in range(0, 5):
    valores.append(int(input(f'Digite o {ciclo + 1}ª valor: ')))
    valor = valores[-1]
    if ciclo == 0:
        maior = menor = valor
    else:
        if valor > maior:
            maior = valor
        elif valor < menor:
            menor = valor

print(f'Lista: {valores}')
print(f'Maior valor: {maior} na Posição: ', end='')
for indice, valor in enumerate(valores):
    if valor == maior:
        print(f'{indice}...', end='')
print()
print(f'Menor valor: {menor} na Posição: ', end='')
for indice, valor in enumerate(valores):
    if valor == menor:
        print(f'{indice}...', end='')
print()
