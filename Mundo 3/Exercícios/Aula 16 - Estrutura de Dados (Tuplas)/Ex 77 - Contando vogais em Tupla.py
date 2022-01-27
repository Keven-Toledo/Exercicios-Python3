palavras = ()
contador = 0
while True:
    palavra = str(input('Digite uma palavra: ')).strip().upper()
    contador += 1
    palavras += palavra,
    if contador == 12:
        break

'''palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
            'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR',
            'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')'''

vogais = ('A', 'E', 'I', 'O', 'U')
for palavra in palavras:
    print(f'\n Na palavra {palavra} temos ', end='')
    for letra in palavra:
        if letra in vogais:
            print(letra.lower(), end=' ')
