# A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 25 anos: SÊNIOR
# Acima: MASTER

from datetime import date

atual = date.today().year
ano = int(input('Digite seu ano de nascimento: '))
idade = atual - ano
print('AGUARDE ESTAMOS ANALISANDO SEU DADOS...')
print('Caso se enquadre dentro de uma das categorias iremos informar!')

if idade <= 9:
    print('O atleta tem {} anos.'.format(idade))
    print('Classificação: MIRIM')
elif idade <= 14:
    print('O atleta tem {} anos.'.format(idade))
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('O atleta tem {} anos.'.format(idade))
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('O atleta tem {} anos.'.format(idade))
    print('Classificação: SÊNIOR')
else:
    print('O atleta tem {} anos.'.format(idade))
    print('Classificação: MASTER')
