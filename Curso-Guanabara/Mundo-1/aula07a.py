nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))

numero_1 = int(input('Um valor: '))
numero_2 = int(input('Outro valor: '))

soma = numero_1 + numero_2
multiplicacao = numero_1 * numero_2
divisao = numero_1 / numero_2
divisao_inteira = numero_1 // numero_2
exponenciacao = numero_1 ** numero_2
subtracao = numero_1 - numero_2
resto_da_divisao = numero_1 % numero_2

print('A soma entre {} e {} é {}.'.format(numero_1, numero_2, soma))
print('A subtração entre {} e {} é {}.'.format(numero_1, numero_2, subtracao))
print('A multiplicação entre {} e {} é {}.'.format(numero_1, numero_2, multiplicacao))
print('A divisão entre {} e {} é {:.2f}.'.format(numero_1, numero_2, divisao))
print('A divisão inteira entre {} e {} é {}.'.format(numero_1, numero_2, divisao_inteira))
print('O resto da divisão entre {} e {} é {}.'.format(numero_1, numero_2, resto_da_divisao))
print('A exponênciação entre {} e {} é {}.'.format(numero_1, numero_2, exponenciacao))

# Caso eu queira deixar tudo em uma linha dentro de print você coloca .format(x, y, z), end=' ') dentro da aspas tem um espaço para ter um espaço entre as palavras

print('=' * 75)
print('O resto da divisão entre {} e {} é {}.'.format(numero_1, numero_2, resto_da_divisao), end=' ')
print('E divisão inteira entre {} e {} é {}.'.format(numero_1, numero_2, divisao_inteira))

# Se quiser quebrar a linha você usa o \n assim a segunda parte da mensagem em print vai aparece na linha de baixo.

print('=' * 75)
print('O primeiro valor é {} \nO segundo valor é {} \nE o ultimo é {}.'.format(numero_1, numero_2, soma))

# Depois ele passou uma lista de exercícios...

# Crie um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor.

numero = int(input('Digite um número: '))

print('O número digitado foi {}, ele tem {} como seu sucessor e {} como seu antecessor.'.format(numero, numero + 1, numero - 1))

# Crie um program que leia um número e mostre o seu dobro, triplo e raiz quadrada.

numero = int(input('Difigte um número: '))
dobro = numero * 2
triplo = numero * 3
quadrada = numero ** 0.5

print('O número digitado foi {}\n Seu dobro é {}\n Seu triplo é {}\n Sua raiz quadrada é {:.2f}'.format(numero, dobro, triplo, quadrada))

# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
media = (nota_1 + nota_2) / 2

print('A média da nota {} e {} é igual a {}.'.format(nota_1, nota_2, media))

# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milimetros.

# Aqui vamos fazer diferente pois peguei outras metragens na internet

valor = int(input('Digite um valor em metros para sua conversão: '))

decimetros = 10 # 10 decímetros correpondem a 1 metro
centimetros = 100 # 100 centímetros corresponde a 1 metro
milimetros = 1000 # 1000 milímetros corresponde a 1 metro
decametros = 10 # 1 decâmetro corresponde a 10 metros
hectometros = 100 # 1 hectômetro corresponde a 100 metros
quilometros = 1000 # 1 quilômetro corresponde a 1000 metros

print('Você digitou {} seu número convertido em centímetros é {}'.format(valor, valor * centimetros))
print('Você digitou {} seu número convertido em decímetros é {}'.format(valor, valor * decimetros))
print('Você digitou {} seu número convertido em milímetros é {}'.format(valor, valor * milimetros))
print('Você digitou {} seu número convertido em decâmetros é {}'.format(valor, valor / decametros))
print('Você digitou {} seu número convertido em hectômetros é {}'.format(valor, valor / hectometros))
print('Você digitou {} seu número convertido em quilômetros é {}'.format(valor, valor / quilometros))

# Faça um programa que leia o número inteiro qualquer e mostre na tela a sua tabuada.
