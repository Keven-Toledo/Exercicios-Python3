valores = list()
while True:
    print('=' * 20)
    numero = int(input('Digite um número: '))
    valores.append(numero)
    resposta = str(input('Deseja continuar? ')).strip().upper()[0]
    while resposta not in 'SN':
        print('\033[1;31m-' * 30)
        print('Inválido! Responda Sim ou Não')
        print('-' * 30, '\033[m')
        resposta = str(input('Deseja continuar? ')).strip().upper()[0]
    if resposta == 'N':
        break

reverse = sorted(valores, reverse=True)
print('=' * 30)
print(f'''
Lista em ordem decrescente: {reverse}
Quantidade de elementos da lista: {len(valores)}''')
if 5 in valores:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista')
