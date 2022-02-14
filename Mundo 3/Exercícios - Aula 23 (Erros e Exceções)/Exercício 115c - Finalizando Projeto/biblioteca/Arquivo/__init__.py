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
        titulo('Cadastros')
        for cadastro in abrir:
            cliente = cadastro.split(';')
            cliente[1] = cliente[1].replace('\n', '')
            print(f'{cliente[0]:<26}{cliente[1]:>3} anos')
        abrir.close()


def cadastrar(file, name='desconhecido', age='0'):
    try:
        add = open(file, 'at')
    except:
        print('Não foi possível abrir o arquivo.')
    else:
        try:
            add.write(f'{name}; {age}\n')
        except:
            print('Não foi possível add o cadastro.')
        else:
            print(f'Novo registro: {name} adicionado')
            add.close()
