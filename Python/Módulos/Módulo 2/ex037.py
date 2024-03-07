#Escreva um programa que leias um número inteiro qualquer e peça para o usuário escolher qualç será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

num = int(input('Digite um número: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL ''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('O número {} convertido em BINÁRIO fica {}.'.format(num, bin(num)[2:]))
elif opção == 2:
    print('O número {} convertido para OCTAL fica {}.'.format(num, oct(num)[2:]))
elif opção == 3:
    print('O número {} convertido para HEXADECIMAL fica {}.'.format(num, hex(num)[2:]))
else:
    print('Opção inválida tente novamente!')