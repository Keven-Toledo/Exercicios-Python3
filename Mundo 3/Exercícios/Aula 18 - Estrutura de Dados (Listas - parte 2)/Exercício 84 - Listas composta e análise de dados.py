pessoas = list()    # Lista Principal
cadastro = list()   # Lista Auxiliar
while True:
    cadastro.append(str(input('Qual o seu nome? ')).strip().capitalize())
    cadastro.append(float(input('Qual o seu peso? ')))
    pessoas.append(cadastro[:])
    cadastro.clear()
    resposta = str(input('Deseja continuar? ')).strip().upper()[0]
    while resposta not in 'SN':
        print('Inválido! Responda "Sim" ou "Não"')
        resposta = str(input('Deseja continuar? ')).strip().upper()[0]
    if resposta == 'N':
        break

# Pessoas Cadastradas
nomes = list()
for ciclo in range(0, len(pessoas)):
    nomes.append(pessoas[ciclo][0])
print(f'Foram cadastrados {len(nomes)} nomes')

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
