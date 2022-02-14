from biblioteca.interface import *
from biblioteca.Arquivo import *
from time import sleep

arquivo = 'cursoemvideo'
if not arquivoexiste(arquivo):
    criararquivo(arquivo)


while True:
    resposta = menu('Menu Principal', ['Lista de Cadastro', 'Cadastrar', 'Sair do Sistema'])
    if resposta == 1:
        mostrararquivo(arquivo)

    elif resposta == 2:
        titulo('Novo Cadastro')
        nome = str(input('Nome: ')).strip().capitalize()
        idade = leiaint('Idade: ')
        cadastrar(arquivo, nome, idade)
    elif resposta == 3:
        red('Saindo do Sistema...')
        sleep(1)
        break
    else:
        red('Erro! Tente Novamente')
    sleep(1)
