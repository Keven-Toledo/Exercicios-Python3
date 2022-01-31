# Criação de uma lista composta
'''teste = list()
teste.append('Keven')
teste.append(21)
galera = list()
galera.append(teste[:])
teste[0] = 'Karen'
teste[1] = 18
galera.append(teste[:])
print(galera)'''

# Listas dentro de listas
'''galera = [['Keven', 21], ['Karen', 18], ['Leoni', 18]]
print(galera[0])
print(galera[0][0])
print(galera[2][1])
for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos')'''

# Validação de dados
"""Lista_principal = list()
Lista_temporaria = list()
maior_idade = menor_idade = 0
for ciclo in range(0, 3):
    Lista_temporaria.append(str(input('Nome: ')).strip().capitalize())
    Lista_temporaria.append(int(input('Idade: ')))
    Lista_principal.append(Lista_temporaria[:])
    Lista_temporaria.clear()
print(Lista_principal)
for pessoa in Lista_principal:
    if pessoa[1] >= 21:
        print(f'{pessoa[0]} é maior de idade')
        maior_idade += 1
    else:
        print(f'{pessoa[0]} não é maior de idade')
        menor_idade += 1
print(f'''Há {maior_idade} pessoas maior de idade e
{menor_idade} menor de idade''')"""
