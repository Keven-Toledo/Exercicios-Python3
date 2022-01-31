expressao = str(input('Digite sua expressão: '))
parenteses_abertos = list()
parenteses_fechados = list()
for elemento in expressao:
    if elemento == '(':
        parenteses_abertos.append(elemento)
    elif elemento == ')':
        parenteses_fechados.append(elemento)
if len(parenteses_abertos) == len(parenteses_fechados):
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')
