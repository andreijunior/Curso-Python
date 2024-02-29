# Crie um projeto em que o produto tenha um preço, tenha desconto de 10% à vista #
# Caso leve entre 3 e 5 produtos do mesmo tenha 20% e 30% caso leve mais de 8 produtos #
# Caso seja parcelado o produto não tenha desconstos, em até 3 vezes no cartão você parcela sem juros #
# A cima de 3 vezes no cartão tenha juros de forma crescente #

produto = float(input('Digite o preço do produto: R$'))
n10 = produto - (produto * 10 / 100)
print('O produto no valor de R${}, a vista está saindo por R${}'.format(produto, n10))
print('Caso você leve entre 3 e 5 produtos do mesmo, você ganha 20%.')
print('E caso você leve mais de 8 produtos, você ganha 30%.')
pergunta_1 = str(input('Você deseja levar mais produtos do mesmo? '))
q_produtos = int(input('Quantos você deseja levar? '))
n20 = produto - (produto * 20 / 100)
n30 = produto - (produto * 30 / 100)
q_n20 = q_produtos  ()

