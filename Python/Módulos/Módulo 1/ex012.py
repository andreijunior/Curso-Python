# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto #

preço = float(input('Digite o preço do produto: R$'))
np = preço - (preço * 5 / 100)
print('O preço do produto que era R${}, agora está com desconto de 5%, ficando com o preço de R${:.2f}'.format(preço, np))
