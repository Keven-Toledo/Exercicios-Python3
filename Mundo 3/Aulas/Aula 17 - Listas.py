"""num = [2, 5, 9, 1]
num[3] = 4
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
num.remove(2)
if 0 in num:
    num.remove(0)
else:
    print('Não existe 0')

print(num)
print(f'Essa lista em {len(num)} elementos')"""

"""valores = list()
# valores.append(9)
# valores.append(5)
# valores.append(4)
for ciclo in range(1, 5):
    valores.append(int(input('Digite um valor: ')))

for valor in valores:
    print(valor)

for indice, valor in enumerate(valores):
    print(f'Na posição {indice} encontrei o valor {valor}')
print('Fim da busca')"""

# Ligando duas listas (uma altera a outra)
a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista 1A: {a}')
print(f'Lista 1B: {b}')

# Copiando uma lista da outra
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista 2A: {a}')
print(f'Lista 2B: {b}')
