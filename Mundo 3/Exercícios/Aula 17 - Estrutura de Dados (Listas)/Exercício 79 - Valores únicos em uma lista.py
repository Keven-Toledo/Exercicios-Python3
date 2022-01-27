valores = list()
while True:
    print('=' * 20)
    numero = int(input('Digite um valor: '))
    if numero not in valores:
        valores.append(numero)
        pergunta = str(input('Deseja continuar? ')).strip().upper()[0]
        while pergunta not in 'SN':
            print('\033[31mEscolha entre Sim ou Não\033[m')
            pergunta = str(input('Deseja continuar? ')).strip().upper()[0]
        if pergunta == 'N':
            break
    else:
        print(f'''\033[31mO número {numero} já existe na lista.
Sendo assim, não será adicionado\033[m''')

valores.sort()
print(f'A lista formada foi: {valores}')
