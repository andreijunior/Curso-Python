# Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.

print('=' * 5, 'DESAFIO 02', '=' * 5)
dia = input('Qual seu dia de nascimento? ')
mês = input('Qual seu mês de nascimento? ')
ano = input('Qual seu ano de nascimento? ')
print('Você nasceu no dia {} de {} de {}. Correto? '.format(dia, mês, ano))
