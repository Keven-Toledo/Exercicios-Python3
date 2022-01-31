from random import randint
from time import sleep
Jogos = list()     # Lista Principal
cadastro_jogo = list()   # Lista Auxiliar

print('-' * 30)
print('      JOGA NA MEGA SENA     ')
print('-' * 30)
pergunta = int(input('Quantos jogos deseja fazer? '))

for jogos in range(0, pergunta):
    for ciclo in range(1, 7):
        numero = randint(1, 60)
        if numero not in cadastro_jogo:
            cadastro_jogo.append(numero)
        else:
            while numero in cadastro_jogo:
                numero = randint(1, 60)
            cadastro_jogo.append(numero)
    cadastro_jogo.sort()
    Jogos.append(cadastro_jogo[:])
    cadastro_jogo.clear()

print()

print('-=' * 4, f'SORTEANDO {pergunta} JOGOS', '-=' * 4)
for ciclo in range(0, len(Jogos)):
    print(f'Jogo {ciclo + 1}: {Jogos[ciclo]}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
