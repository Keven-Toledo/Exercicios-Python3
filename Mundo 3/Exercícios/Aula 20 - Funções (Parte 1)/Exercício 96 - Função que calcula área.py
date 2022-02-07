# Cabeçalho do Programa
def titulo(txt):
    print('=' * 30)
    print(f'{txt: >26}')
    print('=' * 30)


# Função Área
def area(a, b):
    resultado = a * b
    print(f'A área do terreno {a}x{b} é de {resultado}m²')


# Criar variáveis
titulo('Calculadora de Terrenos')
larg = float(input('Largura(m): '))
comp = float(input('Comprimento(m): '))
area(larg, comp)
