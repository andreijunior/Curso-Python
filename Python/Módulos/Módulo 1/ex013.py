# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento #

salário = float(input('Digite o salário de um funcionário: R$'))
novo_salário = salário + (salário * 15 / 100)
print('Seu funcionário tem um salário no valor R${:.2f}\n'
      'Com seu aumento de 15%, o salário do seu funcionário ficará R${:.2f}'.format(salário, novo_salário))
