# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. #
# Para salários superiores a R$1.250,00, calcule um aumento de 10%. #
# Para os inferiores ou iguais, o aumento é de 15%. #

salário = float(input('Digite o seu salário: R$'))
n10 = salário + (salário * 10 / 100)
n15 = salário + (salário * 15 / 100)


if salário > 1250.00:
    print('Você recebeu 10% de aumento, seu salário será de R${:.2f}.'.format(n10))
else: 
    print('Você recebeu 15% de aumento, seu salário é de R${:.2f}.'.format(n15))

'''salário = float(input('Qual é o salário do funcionário? R$'))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('Quem ganahava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salário, novo))'''