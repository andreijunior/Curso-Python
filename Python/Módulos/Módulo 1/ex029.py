# Escreva um programa que leia a velocidade de um carro. #
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. #
# A multa vai custar R$7,00 por cada Km acima do limite #


velocidade = float(input('Quantos Km/h você estava na via? '))
multa = (velocidade - 80) * 7.00

if velocidade <= 80.00:
    print('Meus parabéns você não foi multado por estar dentro dos limites permitidos!')
else:
    print('Infelizmente terei que lhe multar, você estava acima da velocidade permitida.')
    print('Você tem que pagar R${:.2f}.'.format(multa))
print('Tenha um excelente dia, dirija com cuidado!!')
print('FIM DO PROGRAMA!!!')