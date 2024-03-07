# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.


valor_casa = float(input('Qual é o valor do imóvel? R$'))
salário = float(input('Quanto você recebe de salário? R$'))
anos = int(input('Em quantos anos você pretende pagar o imóvel? '))
prestação = valor_casa / (anos * 12)
mínimo = salário * 30 / 100
print('Para pagar um imóvel de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(valor_casa, anos, prestação))
# Validando diferença entre quanto sai a parcela realmente 
'''print('Diferença entre a prestação R${:.2f} e o limite de excedência R${:.2f}'.format(prestação, mínimo))'''
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')