# Faça um program que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de se alistar.
# Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
atual = date.today().year
ano = int(input('Digite o ano de nascimento: '))
idade = atual - ano
print('Quem nasceu em {} tem {} anos em {}, que é o ano atual.'.format(ano, idade, atual))
if idade == 18:
    print('Você tem que comparecer ao serviço militar IMEDIATAMENTE.')
elif idade < 18:
    saldo = 18 - idade
    print('Você não possui 18 anos. Ainda lhe faltam {} anos para se alistar.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Já passou do tempo de se alistar, isso foi a {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi {}.'.format(ano))


