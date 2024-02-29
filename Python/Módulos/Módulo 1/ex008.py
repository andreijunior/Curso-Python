# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros #
# Valores de converção abaixo: #
# 1 metro = 1000 centímetros #
# 1 metro = 10000 milímetros #

n = float(input('Digite um valor em metros: '))
cm = n * 100
mm = n * 1000
print('O valor de {} m, tem {} cm convertido e {} mm convertido'. format(n, cm, mm))


# Melhorando o exercício #
# decâmetro: 1 decâmetro corresponde a 10 metros #
# hectômetro: 1 hectômetro corresponde a 100 metros #
# quilômetro: 1 quilômetro corresponde a 1000 metros #
# decímetro: 10 decímetros corresponde a 1 metro #
# centímetro: 100 centímetros corresponde a 1 metro #
# milímetro: 1000 milímetros corresponde a 1 metro #

m = float(input('Digite uma distância em metros: '))
dam = m * 10
hm = m * 100
km = m * 1000
dm = m * 10
cm = m * 100
mm = m * 1000

print('A distância {} em metros corresponde à {} decâmetros'.format(m, dam))
print('A distância {} em metros corresponde à {} hectômetros'.format(m, hm))
print('A distância {} em metros corresponde à {} quilômetros'.format(m, km))
print('A distância {} em metros corresponde à {} decímetros'.format(m, dm))
print('A distância {} em metros corresponde à {} centímetros'.format(m, cm))
print('A distância {} em metros corresponde à {} milímetros'.format(m, mm))