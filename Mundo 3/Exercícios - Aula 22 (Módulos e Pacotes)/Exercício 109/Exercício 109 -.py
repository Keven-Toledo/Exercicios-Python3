from ex109 import moeda
preco = float(input('Preço do Produto: R$'))
print(f"""
A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}
O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}
Aumentando 10%, temos {moeda.aumentar(preco, 10, True)}
Reduzindo 13%, temos {moeda.diminuir(preco, 13)}""")
