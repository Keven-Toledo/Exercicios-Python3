def escreva(txt):
    larg = len(txt) + 4
    print('=' * larg)
    print(f'{txt: ^{larg}}')
    print('=' * larg)


texto = str(input('Digite algo: ')).strip().capitalize()
escreva(texto)
