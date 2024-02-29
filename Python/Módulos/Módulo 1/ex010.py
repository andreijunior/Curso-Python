# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar #

din = float(input('Digite o valor que tem em dinheiro na carteira: R$'))
dólar = din / 4.97
euro = din / 5.35
print('Você pode comprar ${:.2f} ou €{:.2f} com R${}'.format(dólar, euro, din))
