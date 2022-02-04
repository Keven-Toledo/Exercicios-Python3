# Importar biblioteca
from random import randint
from time import sleep
from operator import itemgetter
# Girar os dados
jogadas = {'jogador_1': randint(1, 6),
           'jogador_2': randint(1, 6),
           'jogador_3': randint(1, 6),
           'jogador_4': randint(1, 6)}

# Mostrar números sorteados
print('-=' * 3, 'Números sorteados', '-=' * 3)
for key, value in jogadas.items():
    print(f'    O {key} sorteou {value}')
    sleep(1)

# Ordenando um dicionário
ranking = list()
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)


# Mostrar ranking dos jogadores
print('-=' * 3, f'{"Ranking dos jogadores"}', '-=' * 3)
for ciclo in range(0, 4):
    print(f'{ciclo+1}º lugar - {ranking[ciclo][0]} sorteou {ranking[ciclo][1]}')

