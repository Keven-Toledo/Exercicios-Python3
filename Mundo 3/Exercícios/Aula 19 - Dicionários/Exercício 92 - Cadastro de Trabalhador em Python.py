from datetime import date
# Criar dicionário
cadastro = dict()
# Inserir primeiros valores
cadastro['Nome'] = str(input('Seu nome: ')).strip().capitalize()
cadastro['Nascimento'] = int(input('Ano de Nascimento: '))
# Cálculo da idade
idade = date.today().year - cadastro['Nascimento']
cadastro['Idade'] = idade
# Verificar se possui CTPS
pergunta = str(input('Possui Carteira de Trabalho? ')).strip().upper()[0]
while pergunta not in 'SN':
    print('\033[1;31mInválido! Escreva sim ou não.\033[m')
    pergunta = str(input('Possui Carteira de Trabalho? ')).strip().upper()[0]
# Prosseguir caso haja CTPS
if pergunta == 'S':
    cadastro['CTPS'] = int(input('CTPS: '))
# Tempo para aponsetadoria
    contratacao = int(input('Ano de Contratação: '))
    aponsen = idade + 35
    cadastro['Salário'] = float(input('Salário: '))
    cadastro['Aposentadoria'] = aponsen

# Apresentar informações
print()
print('=-' * 5, 'Informações', '=-' * 5)
NNC = ('Nome', 'Nascimento', 'CTPS')
IA = ('Idade', 'Aposentadoria')
for key, value in cadastro.items():
    if key in NNC:
        print(f'{key}: {value}')
    elif key in IA:
        print(f'{key}: {value} anos')
    elif key == 'Salário':
        print(f'{key}: R${value}')
