from time import sleep
# Cria listas e Dicionários
jogadores = list()
cadastro = dict()
gols = list()
# Contabilizar IDS (micro-banco de dados)
cont = 0
IDS = [0]
# Inserir informações de cada jogador
while True:
    print('--' * 15)
    nome = str(input('Nome do Jogador: ')).strip().upper()
    partidas = int(input('Partidas jogadas: '))
    # Gols por partida
    for partida in range(1, partidas + 1):
        gols.append(int(input(f'Gols da {partida}ª partida: ')))
    # Total de gols
    total_gols = sum(gols)
    cadastro = {
        'Nome': nome,
        'Partidas': partidas,
        'Gols': gols.copy(),
        'Total de Gols': total_gols
    }
    jogadores.append(cadastro.copy())
    # Limpar gols
    gols.clear()
    # Encerramento da ER while True
    print('=-' * 15)
    resposta = str(input('Deseja continuar? ')).strip().upper()[0]
    while resposta not in 'SN':
        print('\033[1;31m--' * 15)
        print('\033[1;31mInválido! Digite "SIM" ou "NÃO"')
        print('--' * 15, '\033[m')
        resposta = str(input('Deseja continuar? ')).strip().upper()[0]
    if resposta == 'N':
        break
    # Adicionar mais um ID na lista IDS
    cont += 1
    IDS.append(cont)
# Mostrar informações
print('-=' * 18)
print(f'{"ID":<4}{"Nome":<10}{"Partidas":>8}{"Gols(total)":>16}')
for indice, jogador in enumerate(jogadores):
    print(f'{indice:<4}{jogador["Nome"]:<10}{jogador["Partidas"]:^8}{jogador["Total de Gols"]:^16}')
# Diferenciar pergunta
cont_ciclos = 1
# Mais detalhes
while True:
    if cont_ciclos == 1:
        continuar = str(input('Deseja ver mais informações? ')).strip().upper()[0]
        while continuar not in 'SN':
            print('\033[1;31m--' * 15)
            print('\033[1;31mInválido! Digite "SIM" ou "NÃO"')
            print('--' * 15, '\033[m')
            continuar = str(input('Deseja ver mais informações? ')).strip().upper()[0]
        if continuar == 'S':
            if cont_ciclos == 1:
                print('--' * 15)
                ID = int(input('Escreva o ID: '))
                # Verificar se o ID existe
                while ID not in IDS:
                    print('\033[1;31m--' * 15)
                    print('Inválido! Valor não encontrado')
                    print('--' * 15, '\033[m')
                    ID = int(input('Escreva o ID: '))
                # Detalhes do jogador escolhido
                sleep(1)
                print('--' * 16)
                print(f'>> DETALHES DAS PARTIDAS DE {jogadores[ID]["Nome"]}')
                for partida, gol in enumerate(jogadores[ID]['Gols']):
                    print(f'{partida + 1}ª partida fez {gol}')
        else:
            break
    else:
        continuar = str(input('Deseja continuar? ')).strip().upper()[0]
        while continuar not in 'SN':
            print('\033[1;31m--' * 15)
            print('\033[1;31mInválido! Digite "SIM" ou "NÃO"')
            print('--' * 15, '\033[m')
            continuar = str(input('Deseja continuar? ')).strip().upper()[0]
        if continuar == 'S':
            if cont_ciclos == 1:
                print('--' * 15)
                ID = int(input('Escreva o ID: '))
                # Verificar se o ID existe
                while ID not in IDS:
                    print('\033[1;31m--' * 15)
                    print('Inválido! Valor não encontrado')
                    print('--' * 15, '\033[m')
                    ID = int(input('Escreva o ID: '))
                # Detalhes do jogador escolhido
                sleep(1)
                print('--' * 16)
                print(f'>> DETALHES DAS PARTIDAS DE {jogadores[ID]["Nome"]}')
                for partida, gol in enumerate(jogadores[ID]['Gols']):
                    print(f'{partida + 1}ª partida fez {gol}')
        else:
            break
