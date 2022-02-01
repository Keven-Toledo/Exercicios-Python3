numeros = ()
contador = 0
while True:
    num = int(input('Digite um numero: '))
    contador += 1
    numeros += num,
    if contador == 5:
        break

print(f'Os números digitados foram: {numeros}')

if 9 in numeros:
    print(f'O 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O 3 apareceu na {numeros.index(3) + 1}ª posição')

print('Os valores pares foram: ', end='')
for ciclo in numeros:
    if ciclo % 2 == 0:
        print(f'{ciclo},', end=' ')
