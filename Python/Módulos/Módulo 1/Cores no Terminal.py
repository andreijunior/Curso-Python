# Style: 0, 1, 4, 7
# Text: 30, 31, 32, 33, 34, 35, 36, 37
# Back: 40, 41, 42, 43, 44, 45, 46, 47

print('\033[4;32;45mOlá Mundo!\033[m')

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))

nome = 'Andrei'

# Dicionário de  cores criado pela gente
cores = {'limpa':'\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}

# Usando as cores do dicionário criado pela gente
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['amarelo'], nome, cores['limpa']))

# Sem usar cores do dicionário criado pela gente
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

r = 19 // 2
r2 = 19 % 2
print('Resposta: {} e {}'.format(r, r2))
