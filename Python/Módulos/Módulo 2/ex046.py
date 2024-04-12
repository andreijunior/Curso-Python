# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificios, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
print('{:=^55}'.format('CONTAGEM REGRESSIVA DA VIRADA DO ANO!!'))
for c in range(0, 10+1):
    print(c, sleep(1))
print('''FIM DA CONTAGEM REGRESSIVA
FELIZ ANO NOVO!!!''')


# Exercício feito pelo professor

'''from time import sleep
for cont in range(10, -1, -1):
	print(cont)
	sleep(1)
print('Feliz Ano Novo!!!')'''
