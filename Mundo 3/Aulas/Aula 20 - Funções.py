# Introdução a Funções
# Código antes:
"""print('=' * 20)
print(f'{"Olá, mundo!":>15}')
print('=' * 20)"""


# Código usando Função (S/ parâmetro)
"""def linha():
    print('=' * 20)


linha()
print(f'{"Olá, Mundo!":>15}')
linha()"""


# Função usando parâmetros
"""def mensagem(texto):
    print('-=' * 15)
    print(f'{texto:>23}')
    print('-=' * 15)


mensagem('Sistema de alunos')    # Função(parametro)"""


# Cálculo com Função
"""def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'{a} + {b} = {s}')


# Programa Principal
soma(2, 2)
soma(4, 4)"""


# Empacotar Parâmetros (Tupla gerada automaticamente)
"""def contador(* num):
    quantidade = len(num)
    soma = sum(num)
    print(f'A tupla {num} possui {quantidade} elementos')
    print(f'A soma vale: {soma}')


contador(2, 3, 5, 6)
contador(2, 6, 8, 9)"""


# Usando Listas em Função
"""def dobrar(numeros):
    cont = 0
    while cont < len(numeros):
        numeros[cont] *= 2
        cont += 1


valores = [6, 4, 2, 8, 9]
dobrar(valores)
print(valores)"""
