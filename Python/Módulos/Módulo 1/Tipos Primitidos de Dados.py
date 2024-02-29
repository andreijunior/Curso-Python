# Exercício inicial #

n1 = input('Digite um número: ')
n2 = input('Digite maus um número: ')
s = n1 + n2
print ('A soma vale',s)

# Adicionando um tipo Primitivo #

n1 = int(input('Digite um número: '))
n2 = int(input('Digite maus um número: '))
s = n1 + n2
print ('A soma vale', s)

# Exemplos #
# int = 7 -4 0 9875 #
# float = 4.5 0.076 -15.223 7.0 #
# bool = True e False #
# str = 'Olá' '7.5' '' #

# Utilizando o print de cima deixando ele mais organizado #

print ('A soma vale {}'.format(s))

# Trazendo o tipo Primitivo da variável #

n1 = input('Digite um valor: ')
print(type(n1))

# Desafio extra #

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
print('A soma entre {} e {} vale {} '.format(n1, n2, s))

# Auba 6b trazendo outros exemplos de Tipos Primitivos #
n = bool(input(Digite um valor: ))
print(type(n))
print(n.isnumeric())
print(n.isalpha())
print(n.isalnum())
print(n.isupper())
print(n.islower())
