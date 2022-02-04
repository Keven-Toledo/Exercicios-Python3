# Funcionamento de um dicionário
"""pessoas = {'nome': 'Keven', 'sexo': 'M', 'idade': 21}
print(pessoas['nome'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')"""

# Key, Values e Items
'''print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for key in pessoas.keys():
    print(key)
for values in pessoas.values():
    print(values)

# O uso do Items para Dicionários
for key, values in pessoas.items():
    print(f'{key} = {values}')'''

# Deletar uma key
'''del pessoas['sexo']

print(pessoas)'''

# Substituir elementos do Dicionário
'''pessoas['nome'] = 'Karen'

print(pessoas)'''

# Adicionar elementos em um dicionário
'''Dicionário não usa o método append
pessoas['cor dos olhos'] = 'castanho escuro'
print(pessoas)'''

# Dicionário dentro de lista
'''brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[0]['sigla'])'''

# Inserindo elementos no dicionário com ER for
'''brasil = list()
estados = dict()
for ciclo in range(0, 2):
    estados['estado'] = str(input('Digite um estado: ')).strip().capitalize()
    estados['sigla'] = str(input('Digite a sigla do estado: ')).strip().upper()
    brasil.append(estados.copy())

for estado in brasil:
    print(f'UF: {estado["estado"]}, {estado["sigla"]}')

for estado in brasil:
    for elemento in estado.values():
        print(elemento, end='')
    print()'''

# Ordenando um dicionário
'''from operator import itemgetter
ranking = list()
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)'''