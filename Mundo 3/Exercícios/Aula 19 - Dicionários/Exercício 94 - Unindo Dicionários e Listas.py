from time import sleep
# Cria as estruturas de dados
clientes = list()
cadastro = dict()
# Total de cadastrados
total = 0
# Lista de idades
idades = list()
# Lista de Mulheres
mulheres = list()
# Inserir ER While True
while True:
    print('-=' * 15)
    nome = str(input('Nome do Cliente: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).strip().upper()[0:4]
    while sexo not in ('MASC', 'FEMI'):
        print('\033[1;31mInválido! Tente novamente.\033[m')
        sexo = str(input('Sexo: ')).strip().upper()[0:4]
# Adicionar no dicionário e na lista
    cadastro = {
        'Nome': nome,
        'Sexo': sexo,
        'Idade': idade
    }
    idades.append(cadastro['Idade'])
    clientes.append(cadastro.copy())
    # Adicionar mais um cadastro no Operador Contador
    total += 1
    # Adicionar mulheres na lista de mulheres
    if sexo == 'FEMI':
        mulheres.append(nome)

# Encerramento da ER while True
    print('--' * 15)
    resposta = str(input('Deseja continuar? ')).strip().upper()[0]
    while resposta == 'SN':
        resposta = str(input('Deseja continuar? ')).strip().upper()[0]
    if resposta == 'N':
        break
# Média das idades
media = sum(idades) / total
# Pessoas acima da idade média
acima_media = list()
for dicionario in clientes:
    if dicionario['Idade'] > media:
        acima_media.append(dicionario["Nome"])

# Informações
sleep(2)
print('-=' * 15)
print(f'''Cadastros: {total}
Média da Idades: {media:.1f} anos''')
# Nome das pessoas acima da média das idades
print(f'Pessoas acima da média: ', end='')
for indice, nome in enumerate(acima_media):
    print(f'{nome}' if indice + 1 == len(acima_media) else f'{nome} e ', end='')
# Nome das mulheres cadastradas
print(f'\nMulheres cadastradas: ', end='')
for indice, mulher in enumerate(mulheres):
    print(f'{mulher}' if indice + 1 == len(mulheres) else f'{mulher} e ', end=' ')
