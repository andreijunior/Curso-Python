# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessário para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m² #

larg = float(input('Digite o valor da largura da parede: '))
alt = float(input('Digite o valor da altura da parede: '))
área = larg * alt
tinta = área / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(larg, alt, área))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))
