# Cria lista e dionário
info = dict()
gols = list()
# inseri nome e partidas no dicionário
info['Nome'] = str(input('Nome do jogador: ')).strip().capitalize()
info['Partidas'] = int(input('Partidas jogadas: '))
# Quantidade de Gols
for ciclo in range(1, info['Partidas'] + 1):
    gols.append(int(input(f'Gols na {ciclo}ª partida: ')))
# Total de gols
info['Total de gols'] = sum(gols)
# Apresentar informações
print('-=' * 25)
print(f'O jogador {info["Nome"]} jogou {info["Partidas"]} partidas.')
for partida, gol in enumerate(gols):
    print(f'>>> Na {partida + 1}ª partida, fez {gol} gols')
print(f'Totalizando {info["Total de gols"]} gols')
