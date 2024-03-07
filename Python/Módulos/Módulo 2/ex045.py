# Crie um programa que faça o computador jogar JOKENPÔ com você.

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')


'''from random import randint'''
'''print('{:=^40}'.format(' BEM VINDO AO JOGO JOKENPÔ '))
print(
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA)
pergunta = int(input('Digite 1 para continuar e jogar ou 2 para não: '))
if pergunta == 1:
    jogador = int(input('Qual é a sua jogada? '))
    computador = randint (1, 3)
    lista = [1, 2, 3]
    if computador == 1 and jogador == 1:
        print('Sua escolha foi igual a do computador os dois jogaram PEDRA, deu impate.')
    elif computador == 1 and jogador == 2:
        print('Sua escolha ganhou do computador você jogou PAPEL')
    elif computador == 1 and jogador == 3:
        print('Sua escolha foi Tesoura, computaodor GANHOU.')
elif pergunta == 2:
    print('Até a próxima!!!')'''