# Criar variável dicionário
estudante = dict()
# Inserir key e value dentro dela
estudante['Nome'] = str(input('Nome: ')).strip().capitalize()
estudante['Media'] = float(input(f'Média do aluno {estudante["Nome"]}: '))

# Verificar a média do estudante criando mesmo key com value diferente
if estudante['Media'] >= 7:
    estudante['Situação'] = 'Aprovado'
elif estudante['Media'] >= 5:
    estudante['Situação'] = 'Recuperação'
else:
    estudante['Situação'] = 'Reprovado'

# Mostrar key e value na tela usando ER for
print('-=' * 20)
for key, value in estudante.items():
    print(f'{key}: {value}')
