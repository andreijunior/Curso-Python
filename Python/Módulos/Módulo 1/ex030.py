# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR #

num = int(input('Digite um número: '))
res = num % 2
print('O resultado foi {}'.format(res))

if res == 0:
    print('O número que você digitou é PAR')
else:
    print('O número que você digitou é IMPAR')