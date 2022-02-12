from ferramentas import numeros
num = int(input('Digite um número: '))
fat = numeros.fatorial(num)
print(f'{num}! = {fat}')
print(f'{num} X 2 = {numeros.dobro(num)}')
print(f'{num} X 3 = {numeros.triplo(num)}')


"""Nessa aula aprendemos a criar módulos que facilitam
a manutenção de um código deixando-o mais limpo e organizado.
Também foi ensinado a criar pacotes que armanezam vários
módulos com o objetivo de organizar ainda mais módulos."""