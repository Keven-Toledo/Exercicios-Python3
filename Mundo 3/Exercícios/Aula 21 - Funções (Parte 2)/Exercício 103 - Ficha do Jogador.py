def ficha(nome="<desconhecido>", gols=0):
    print(f'O jogador {nome} fez {gols} gols no campeonato')


jogador = str(input('Nome do Jogador: '))
gol = str(input('Gols: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if jogador.strip() == '':
    ficha(gols=gol)
else:
    ficha(jogador, gol)
