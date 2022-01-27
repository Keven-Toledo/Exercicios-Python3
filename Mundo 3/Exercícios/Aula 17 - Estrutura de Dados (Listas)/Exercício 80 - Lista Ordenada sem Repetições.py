valores = list()

for ciclo in range(0, 5):
    numero = int(input('Digite um valor: '))
    if ciclo == 0 or numero > valores[-1]:
        valores.append(numero)
        print(f'O número {numero} foi adicionado na última posição')
    else:
        indice = 0
        while indice < len(valores):
            if numero <= valores[indice]:
                valores.insert(indice, numero)
                print(f'O número {numero} foi adicionado na {indice}º posição')
                break
            indice += 1

print(f'A lista formada foi: {valores}')
