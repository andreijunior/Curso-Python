# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: Reprovado
# Média entre 5.0 e 6.9: Recuperação
# Média 7.0 ou superior: Aprovado


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
# Dicionário de cores criado por mim
cores = {'Vermelha':'\033[31m',
         'Azul':'\033[34m',
         'Verde':'\033[32m'}

if m < 5.0:
    print('Sua média é {:.2f}.'.format(m))
    print('Você não atingiu a nota 5.00, necessária para fazer uma recuperação.')
    print('Você foi \033[31mREPROVADO.\033[m')
elif m == 5.0 or m <= 6.9:
    print('Sua média é {:.2f}.'.format(m))
    print('Você não atingiu uma nota para ser aprovado.')
    print('Você está em \033[34mRECUPERAÇÃO.\033[m')
elif m >= 7.0:
    print('Sua média é {:.2f}.'.format(m))
    print('Você conseguiu atingir uma nota para ser aprovado.')
    print('Meus \033[32mPARABÉNS\033[m você foi \033[32mAPROVADO.\033[m')