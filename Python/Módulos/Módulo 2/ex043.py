# Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo: 
# Abaixo de 18.5: Abaixo do Peso
# Entre 18.5 e 25:  Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida

peso = float(input('Digite seu peso? (Kg) '))
altura = float(input('Digite sua altura? (m) '))

print('VAMOS CALCULAR SEU IMC!')

imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.2f}.'.format(imc))
if imc < 18.5:
    print('Seu IMC está ABAIXO DO PESO.')
elif imc < 25:
    print('Seu IMC está no PESO IDEAL.')
elif imc < 30:
    print('Seu IMC já chegou em SOBREPESO.')
elif imc < 40:
    print('Seu IMC chegou no estado de OBESIDADE.')
else:
    print('Seu IMC chegou em OBESIDADE MÓRBIDA.')
    print('Procure um médico Urgente.')