from ex107 import moeda
preco = float(input('Preço do Produto: R$'))
print(f"""
A metade de {preco} é {moeda.metade(preco)}
O dobro de {preco} é {moeda.dobro(preco)}
Aumentando 10%, temos {moeda.aumentar(preco, 10)}
Reduzindo 13%, temos {moeda.diminuir(preco, 13)}""")
