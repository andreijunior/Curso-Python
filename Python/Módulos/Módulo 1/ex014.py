# Escreva um programa que converta uma temperatura digitada em °C e converta °F #

grau_C = float(input('Dgigite o calor de temperatura em °C: '))
grau_F = grau_C * 1.8 + 32 # podemos calcular da seguinte forma também ((9 * grau_C) / 5) + 32 #
print('O valor digitado de {}°C, tem seu valor convertido em {}°F!'.format(grau_C, grau_F))
