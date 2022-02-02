pessoas = list()    # Lista Principal
cadastro = list()   # Lista Auxiliar
while True:
    print('=' * 20)
    cadastro.append(str(input('Primeiro nome? ')).strip().capitalize())
    cadastro.append(float(input('Qual o peso? ')))
    pessoas.append(cadastro[:])
    cadastro.clear()
    print('-' * 20)
    resposta = str(input('\033[1;32mDeseja continuar? \033[m')).strip().upper()[0]
    while resposta not in 'SN':
        print('\033[1;31m=-' * 20)
        print('\033[1;31mInválido! Responda "Sim" ou "Não"')
        print('=-' * 20, '\033[m')
        resposta = str(input('\033[1;33mDeseja continuar? \033[m')).strip().upper()[0]
    if resposta == 'N':
        break

# Pessoas Cadastradas
nomes = list()
for ciclo in range(0, len(pessoas)):
    nomes.append(pessoas[ciclo][0])
print()
print('-=' * 5, f'{"Informações":^5}', '-=' * 5)
print(f'Cadastrados: {len(nomes)} usuários')

# Criar lista de pesos
pesos = list()
for lista in pessoas:
    pesos.append(lista[1])

# Verificar maior e menor valor
pesado = max(pesos)
leve = min(pesos)

# Nome das pessoas mais pesadas
print(f'O maior peso foi de {pesado}Kg, referente a ', end='')
contador_pesado = 0
for pessoa in pessoas:
    if pessoa[1] == pesado:
        contador_pesado += 1
        if contador_pesado == 1:
            print(f'{pessoa[0]}', end='')
        elif contador_pesado > 1:
            print(f', {pessoa[0]}', end='')
# Nome das pessoas mais leves
print(f'\nO menor peso foi de {leve}Kg, referente a ', end='')
contador_leve = 0
for pessoa in pessoas:
    if pessoa[1] == leve:
        contador_leve += 1
        if contador_leve == 1:
            print(f'{pessoa[0]}', end='')
        elif contador_leve > 1:
            print(f', {pessoa[0]}', end='')
