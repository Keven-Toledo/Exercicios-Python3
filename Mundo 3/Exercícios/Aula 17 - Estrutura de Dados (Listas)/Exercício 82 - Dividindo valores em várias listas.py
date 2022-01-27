valores = list()
valores_pares = list()
valores_impares = list()

while True:
    print('=' * 20)
    numero = int(input('Digite um número: '))
    if numero not in valores:
        valores.append(numero)
        resposta = str(input('Deseja continuar? ')).strip().upper()[0]
        while resposta not in 'SN':
            print('\033[1;31m-' * 30)
            print('Inválido! Escreva Sim ou Não.')
            print('-' * 30, '\033[m')
            resposta = str(input('Deseja continuar? ')).strip().upper()[0]
        if resposta == 'N':
            break
    else:
        print('\033[1;31mNúmero existente na Lista\033[m')

for valor in valores:
    if valor % 2 == 0:
        valores_pares.append(valor)
    else:
        valores_impares.append(valor)

valores.sort()
valores_impares.sort()
valores_pares.sort()
print('=' * 40)
print(f'''
Lista completa: {valores}
Lista dos Nº pares: {valores_pares}
Lista do Nº ímpares: {valores_impares}''')
