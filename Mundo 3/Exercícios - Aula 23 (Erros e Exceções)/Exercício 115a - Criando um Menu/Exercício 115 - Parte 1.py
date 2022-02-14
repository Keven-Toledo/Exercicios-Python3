from biblioteca.interface import *
from time import sleep

while True:
    resposta = menu('Menu Principal', ['Lista de Cadastro', 'Cadastrar', 'Sair do Sistema'])
    if resposta == 1:
        titulo('Opção 1')
    elif resposta == 2:
        titulo('Opcão 2')
    elif resposta == 3:
        red('Saindo do Sistema...')
        sleep(1)
        break
    else:
        red('Erro! Tente Novamente')
    sleep(1)
