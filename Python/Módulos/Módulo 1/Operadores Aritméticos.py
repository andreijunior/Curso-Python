# Operadores #

# (+, -, *, /, **, //, %) #

# 5 + 2 = 7 #
# 5 - 2 = 3 #
# 5 * 2 = 10 #
# 5 / 2 = 2.5 #
# 5 ** 2 = 25 (Potência) #
# 5 // 2 = 2 (Divisão inteira) #
# 5 % 2 = 1 (Resto da Divisão) #

# Oredem de procedência ((), **, (*, /, //, %), (+, -)) #

# 1 () #
# 2 ** #
# 3 *, /, //, % #
# 4 +, - #

# Exemplo 1: #
# 5 + 3 * 2 = 11 #

# Exemplo 2: #
# 3 * 5 + 4 ** 2 =  31 #

# Exemplo 3: #
# 3 * (5 + 4) ** 2 = 243 #

# nome = input('Qual é seu nome? ') #
# print('Prazer em te conhecer {:20}!'.format(nome)) #

# Podemos usar alinhamentos para organizar o nome que digitarmos #
# <, >, ^, #

# print('Prazer em te conhecer {:>20}!'.format(nome)) #
# print('Prazer em te conhecer {:<20}!'.format(nome)) #
# print('Prazer em te conhecer {:^20}!'.format(nome)) #
# print('Prazer em te conhecer {:=^20}!'.format(nome)) #

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
print('A soma vale {}'.format(n1 + n2))

# Também podemos usar uma variável para utilizar a soma #
# para quebrar a linha \n, para não quebrar a linha end=' '#

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
r = n1 % n2
print('A Soma é {}, \nA Multiplicação é {} \nA Divisão é {:.3f}'.format(s, m, d))
print('Divisão Inteira {}, \nPotência {} \nO Resto {}'.format(di, e, r))