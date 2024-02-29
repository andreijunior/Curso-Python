# Faça um progrma que leia o nome completo de uma pessoa, mostrando um seguida o primeiro e o último nome separadamente. #
# Ex: Ana Maria de Souza #
# Ana #
# Souza #


n = str(input('Digite o nome completo: ')).strip()
nome = n.split()
print('Analisando dados...')
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu Último nome é {}'.format(nome[len(nome)-1]))

