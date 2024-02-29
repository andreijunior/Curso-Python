# Faça um programa que leia três números e mostre qual é o maior e qual é o menor. #

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

# Analisando o maior digitado:
max = n1
if n2 > n1:
    max = n2
if n3 > n1:
    max = n3

# Analisando o menor digitado:
min = n1
if n2 < n1:
    min = n2
if n3 < n1:
    min = n3

print('Maior: {}.'.format(max))
print('Menor: {}.'.format(min))

