# Condição: Sempre um bloco verdadeiro é executado ou um bloco falso, nunca será os dois ao mesmo tempo #

# Em situações mais detalhadas tempos esse método abaixo: #
'''tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('--FIM--')'''

# Em situações mais simples temos esse método abaixo: #

'''tempo = int(input('Quantos anos tem seu carro? '))
print('Carro novo' if tempo<= 3 else'Carro velho')
print('--FIM--')'''

# Estrutura condicional simples, quando não possuí o else #
'''nome =  str(input('Qual é seu nome? '))
if nome == 'Andrei':
    print('Que nome lindo você tem!')
print('Bom dia, {}!'.format(nome))'''

# Estrutura condicional compusta, quando possuí o else #

'''n = str(input('Qual é seu nome? '))
if n == 'Andrei':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(n))'''

# Ex: #

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('Sua média é {:.1f}!'.format(m))
if m >= 6.0:
    print('Meus parabéns!')
else:
    print('Uhh... Uma pena estude mais!')