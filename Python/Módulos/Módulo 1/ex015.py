# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado. #

km = float(input('Quantos Km você percorreu? '))
dia = int(input('Quantos dias ele foi alugado? '))
o_dia = 60 * dia
km_rodado = km * 0.15
a_pagar = o_dia + km_rodado
print('Você terá que pagar R${} pelos Km rodados e R${}, por dias alugados!'.format(km_rodado, o_dia))
print('O total a pagar pelos dias alugados e kms rodados é de R${}!'.format(a_pagar))