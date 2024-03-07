# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes

r1 = float(input('Digite o valor de comprimento da primeira reta: '))
r2 = float(input('Digite o valor de comprimento da segunda reta: '))
r3 = float(input('Digite o valor de comprimento da terceira reta: '))

nr1 = r1 + r2
nr2 = r1 + r3
nr3 = r3 + r2

if nr1 > r3 and nr2 > r2 and nr3 > r1:
    print('É possívle fazer um triângulo com os comprimentos {:.2f}, {:.2f} e {:.2f}.'.format(r1, r2, r3))
    if r1 == r2 == r3:
        print('Esse triângulo é EQUILÁTERO "Todos os lados são iguais".')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Esse triângulo é ISÓSCELES "Dois dos lados iguais".')
    else:
        print('Esse triângulo é ESCALENO "Todos os lados são diferentes".')
else:
    print('Não é possível fazer um triângulo com os comprimentos {:.2f}. {:.2f} e {:.2f}.'.format(r1, r2, r3))
