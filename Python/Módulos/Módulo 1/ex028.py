# Escreva um programa que faça o computador "pensar" entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computado. #
# O programa deverá escrever na tela se o usuário venceu ou perdeu #

import random
import emoji

print('-=-' * 25)
print('Olá, que tal jogar comigo...')
print('Eu vou pensar um número entre 0 a 5 e você tem que adivinhar...')
print('-=-' * 25)
num = int(input('Digite um número entre 0 e 5: ')) # Jogador tenta adivinhar
n = random.randint(0, 5) # Computador pensa

print('PROCESSANDO OS DADOS DO JOGADOR...')
if num == n:
    print('Nossa você é Bom(a), MEUS PARABÉNS VOCÊ ACERTOU!')
else:
    print(emoji.emojize('HAHAHA!! VOCÊ ERROU E EU GANHEI :zany_face:', language='alias'))
print('Eu pensei no número {}!'.format(n))
print('FIM DO JOGO, ATÉ A PRÓXIMA!!!')

