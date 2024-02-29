# Desenvolva um programa que lei as duas notas do aluno, calcule e mostre a sua média #

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
nf = (n1 + n2) / 2
print('A soma da nota {}, com a nota {}, tem como média {}'. format(n1, n2, nf))

# Desenvolva um programa que lei as três notas do aluno, sendo uma delas nota de trabalho, #
# Resolva a média com as duas notas primeiro e depois use a nota do trabalho como bônus, #
# Somando junta a média e realizando uma nova média, depois mostre a sua média #

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
nt = float(input('Digite a nota do trabalho: '))
nf = ((n1 + n2) / (2) + nt) / 2
print('A soma da nota {}, com a nota {} e a nota do trabalho {}, tem como nota final {:.2}'.format(n1, n2, nt, nf))