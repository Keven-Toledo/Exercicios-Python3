from random import randint

numero = (randint(1, 10), randint(1, 10), randint(1, 10),
          randint(1, 10), randint(1, 10))

print(f'Os valores sorteados foram: ', end=' ')

for ciclo in numero:
    print(f'{ciclo}', end=' ')
print(f'\nO maior valor foi {max(numero)}')
print(f'O menor valor foi {min(numero)}')
