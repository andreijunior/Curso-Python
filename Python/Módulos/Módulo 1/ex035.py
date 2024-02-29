# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo. #

r1 = float(input('Digite o valor de comprimento da primeira reta: '))
r2 = float(input('Digite o valor de comprimento da segunda reta: '))
r3 = float(input('Digite o valor de comprimento da terceira reta: '))

nr1 = r1 + r2
nr2 = r1 + r3
nr3 = r3 + r2

if nr1 > r3 and nr2 > r2 and nr3 > r1:
    print('É possívle fazer um triângulo com os comprimentos {:.2f}, {:.2f} e {:.2f}.'.format(r1, r2, r3))
else:
    print('Não é possível fazer um triângulo com os comprimentos {:.2f}. {:.2f} e {:.2f}.'.format(r1, r2, r3))