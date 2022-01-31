from time import sleep
# Lista principal e auxiliar
sala = list()
alunos = list()
cont = 0
cont_listas = [0]
while True:
    nome = str(input('Nome do Aluno: ')).strip().capitalize()
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    media = (nota_1 + nota_2) / 2
    alunos.append(nome)
    alunos.append(nota_1)
    alunos.append(nota_2)
    alunos.append(media)
    sala.append(alunos[:])
    alunos.clear()
    continuar = str(input('Cadastrar mais alunos? ')).strip().upper()[0]
    while continuar not in 'SN':
        print('\033[1;31mInválido! Escreva "Sim" ou "Não".\033[m')
        continuar = str(input('Cadastrar mais alunos? ')).strip().upper()[0]
    if continuar == 'N':
        break
    cont += 1
    cont_listas.append(cont)

print('-=' * 20)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 30)
for lista in range(0, len(sala)):
    print(f'{lista:<4}{sala[lista][0]:<10}{sala[lista][3]:>8}')
print('-' * 30)

contador = 1
while True:
    if contador == 1:
        pergunta = str(input('Deseja ver a nota de algum aluno? ')).strip().upper()[0]
        while pergunta not in 'SN':
            print('\033[1;31mInválido! Escreva "Sim" ou "Não".\033[m')
            pergunta = str(input('Deseja ver a nota de algum aluno? ')).strip().upper()[0]
        if pergunta == 'S':
            contador += 1
            numero = int(input('Qual aluno? Nº: '))
            print('=' * 30)
            while numero not in cont_listas:
                print('\033[1;31mInválido! Lista Não Encontrada.\033[m')
                numero = int(input('Qual aluno? Nº: '))
            print(f'As notas de {sala[numero][0]} são {sala[numero][1]} e {sala[numero][2]}')
            print('=' * 30)
        else:
            break
    else:
        sleep(1)
        pergunta = str(input('Deseja continuar? ')).strip().upper()[0]
        while pergunta not in 'SN':
            print('\033[1;31mInválido! Escreva "Sim" ou "Não".\033[m')
            pergunta = str(input('Deseja continuar? ')).strip().upper()[0]
        if pergunta == 'S':
            contador += 1
            numero = int(input('Qual aluno? Nº: '))
            print('=' * 30)
            while numero not in cont_listas:
                print('\033[1;31mInválido! Lista Não Encontrada\033[m')
                numero = int(input('Qual aluno? Nº: '))
            print(f'As notas de {sala[numero][0]} são {sala[numero][1]} e {sala[numero][2]}')
            print('=' * 30)
        else:
            break

print('\033[1;33mFINALIZANDO PESQUISA...')
sleep(1)
print('\033[1;32mPROGRAMA FINALIZADO!')
