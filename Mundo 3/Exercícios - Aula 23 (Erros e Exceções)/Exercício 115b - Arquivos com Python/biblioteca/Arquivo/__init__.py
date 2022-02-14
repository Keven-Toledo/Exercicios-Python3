def titulo(txt):
    linha = len(txt) + 20
    print('-' * linha)
    print(f'{txt:^{linha}}'.upper())
    print('-' * linha)


def arquivoexiste(file):
    try:
        arquivo = open(file, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(file):
    try:
        criar = open(file, 'wt+')    # W = Write, T = Text, + = criar
    except:
        print('Houve um Erro na criação do arquivo!')
    else:
        print(f'Arquivo {file} criado com sucesso!')


def mostrararquivo(file):
    try:
        abrir = open(file, 'rt')
    except:
        print('Não foi possível ler o arquivo!')
    else:
        titulo('lista de cadastro')
        print(abrir.read())

