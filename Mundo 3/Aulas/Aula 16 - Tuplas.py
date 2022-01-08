# Tuplas são Imutáveis
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

# Fatiamento de Tupla
'''print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])'''

# Formas de usar o for com tuplas

'''for comida in lanche:
    print(f'Eu vou comer {comida}')

for contagem in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[contagem]}')'''

# Saber o item e também sua posição
'''for contagem in range(0, len(lanche)):
    print(f'{lanche[contagem]} na posição {contagem}')

for posicao, comida in enumerate(lanche):
    print(f'{comida} na posição {posicao}')'''

# Podemos mostrar uma tupla de forma organizada alfabeticamente
'''print(sorted(lanche))   

print(lanche)'''

# Unir tuplas numéricas ou alfabéticas
'''a = (2, 5, 4)
b = (5, 4, 3, 6)
c = a + b
print(c)
print(len(c))       # quantidade de itens na Tupla
print(c.count(5))   # Quantas vezes o número 5 aparece na Tupla
print(c.index(5))   # Mostra a posição em que o número 5 está localizado na tupla
print(c.index(5, 2))  # Mostra a posição do número 5 a partir da posição 2, e não da 0'''

# Em uma mesma tupla inserir strings e caracteres numéricos
'''pessoa = ('Keven', 21, 'M', 53.5)
# del(pessoa)      # Essa função deleta uma variável, no caso uma tupla inteira, mesmo um item da tupla
print(pessoa)'''
