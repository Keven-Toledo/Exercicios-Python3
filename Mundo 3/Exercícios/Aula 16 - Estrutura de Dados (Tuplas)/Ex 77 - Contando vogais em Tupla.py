palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
            'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR',
            'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

vogais = ('A', 'E', 'I', 'O', 'U')
contador = 0
for palavra in palavras:
    print(f'\n Na palavra {palavra} temos ', end='')
    for letra in palavra:
        if letra in vogais:
            print(letra.lower(), end=' ')
    contador += 1
