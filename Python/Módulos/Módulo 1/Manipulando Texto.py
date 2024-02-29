'''Fatiamento'''

'''Frase = Curso em Vídeo Python'''
''' frase [9] = Identifica a letra que está na cadeia com númeração 9'''
''' frase [9:13] = Identifica a do 9 até o 13, mas ele Inclui o 9 e remove o 13'''
''' frase [9:21] = Identifica somente do 9 até o 20 mesmo não tendo o 21 '''
''' frase [9:21:2] = Começa no 9 salta de 2 em 2 e mostra a letra que tiver no segundo pulo '''
''' frase [:5] = :5 quer dizer que antes dos dois pontos ele começa e depois dos dois pontos ele termina'''
''' frase [15:] = 15: quer dizer que ele começa no 15 e mostra todo o resto '''
''' frase [9::3] = Começa no 9 e vai até o final pulando de 3 em 3 e mostrando a letra do terceiro pulo '''

'''Análise'''

''' len(frase) = Ele mostra o comprimento da frase '''
''' frase.count('o') = Conta quantas vezes temos a letra o '''
''' frase.count('o',0,13) = Aqui já podemos fazer um fatiamento junto a análise, ele mostra o comprimento do 0 ao 12, pois o 0 é contado '''
''' frase.find('deo') = Indica quando começou o deo, neste caso o deo começa na posição 11, então ele mostra o 11 '''
''' frase.find('Android') = Quando utilizado uma string que simplesmente não existe ele trás o valor -1 indicando que não existe a posição -1. pois começa no 0 '''
''' 'Curso' in frase = O operador in vai te indicar se exite a palavra curso em frase '''

'''Transformação'''

''' frase.replace('Python','Android') = Ele vai procurar por Python e substituir por Android '''
''' frase.upper() = Vai jogar todas as letras que estiverem em minúsculas para maiúsculas '''
''' frase.lower() = Faz o contrário de upper transforma as letras de maiúsculas para minúsculas '''
''' frase.capitalize() = Pega a primeira letra e deixa em maiúcula e o resto deixa em minúscula '''
''' frase.title() = Faz uma análise mais profunda, quantas palavras, quando tiver espaços vai processar como uma quebra de palavra e assim a próxima ele deixa com a letra inicial maiúscula '''
''' frase.strip() = Ele remove os espaços inicio e final de uma frase '''
''' frase.estrip() = Ele remove somente os ultimos espaços '''
''' frase.lstrip() = Ele remove somente os primeiros espaços '''

'''Divisão'''

''' frase.split() = Remove todos os espaços de uma frase e reinicia a numeração ou indexação '''

'''Junção'''

''' '-'.join(frase) = Junta todos os elemendos de frase e volta a frase como era antes '''

# Em Python tudo é um objeto #

frase = 'Curso em Vídeo Python'
dividido = frase.split()
'''print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15:2])
print(frase[::2])
print(frase.upper().count('O'))
print(len(frase.strip()))
print(frase.replace('Python', 'Android'))'''

print('Curso' in frase)
print(frase.find('Curso'))
print(frase.lower().find('Curso'))
print(dividido[2][3])

print("""Oi, eu sou Goku!
Tu é Vegeta ou você é Gohan, Trunks você
vai lutar?  """)


