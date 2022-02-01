times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians',
         'Bragantino', 'Fluminense', 'América-MG', 'Atlético-GO', 'Santos',
         'Ceará', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá',
         'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')

print('=' * 30, '\n Os cinco primeiros colocados: ', '\n', '=' * 30)
for ciclo in range(0, 5):
    print(f'{ciclo + 1}ª - {times[ciclo]}')

print('=' * 30, '\n Os quatro últimos colocados', '\n', '=' * 30)
for ciclo in range(len(times) - 4, len(times)):
    print(f'{ciclo + 1}ª - {times[ciclo]}')

print('=' * 30, '\n Tabela em ordem alfabética', '\n', '=' * 30)
for ciclo in range(0, 20):
    print(f'{ciclo + 1}º - {sorted(times)[ciclo]}')

print('=' * 30, '\n Tabela em ordem alfabética', '\n', '=' * 30)
print(times.index('Chapecoense') + 1)
