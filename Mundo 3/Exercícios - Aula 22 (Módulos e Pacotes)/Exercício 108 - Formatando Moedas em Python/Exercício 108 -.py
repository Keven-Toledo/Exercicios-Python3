from ex108 import moeda
preco = float(input('Preço do Produto: R$'))
print(f"""
A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}
O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}
Aumentando 10%, temos {moeda.moeda(moeda.aumentar(preco, 10))}
Reduzindo 13%, temos {moeda.moeda(moeda.diminuir(preco, 13))}""")
