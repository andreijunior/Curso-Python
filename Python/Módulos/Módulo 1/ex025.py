# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome. #

nome = str(input('Digite um nome: ')).strip()
print('O seu nome tem SILVA? {}'.format('SILVA' in nome.upper()))
