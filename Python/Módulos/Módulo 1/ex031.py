# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passgem, cobrando R$0,50, pro Km para viagens de até 200Km e R$0,45 para viagens mais longas #

distancia = float(input('Digite a distância de viagem em Km: '))

km1 = distancia * 0.50
km2 = distancia * 0.45

if distancia <= 200.00:
    print('O valor para viagem de distância {}Km, é de R${:.2f}.'.format(distancia, km1))
else:
    print('O valor para viagem de distância {}Km, é de R${:.2f}.'.format(distancia, km2))


'''if distancia <= 200.00:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))'''

'''preço = distancia * 0.50 if distancia <= 200.00 else distancia * 0.45
print('E o preço da dua passagem será de R${:.2f}.'.format(preço))'''