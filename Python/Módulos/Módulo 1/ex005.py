# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor #

n = int(input('Digite um número: '))
ant = n - 1
suc = n + 1
print('O número {}, tem como seu antecessor o número {} e como seu sucessor o número {}'.format(n, ant, suc))
