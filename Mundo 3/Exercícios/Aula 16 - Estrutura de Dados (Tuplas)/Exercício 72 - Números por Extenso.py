extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze',
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

print('=' * 30)
print('Escolha um número entre 0 e 20')
print('=' * 30)
while True:
    numero = int(input('Escolha um número: '))
    while numero not in range(0, 21):
        print('Valor inválido! Tente novamente.')
        numero = int(input('Escolha um número: '))

    print(f'Você digitou o número {extenso[numero]}')
    opcao = str(input('Deseja continuar? ')).strip().upper()[0]
    if opcao == 'N':
        break
