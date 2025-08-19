#Interpolação de Variáveis
#Etapa 2 
#Em Python temos 3 formas de interpolar variáveis em strings, a primeira é usando o sinal %, a segunda é utilizar o método format e a última é utilizar f strings. A Primeira Forma não é atualmente recomendada e seu uso em Python 3 é raro.

#Old Style %
nome = 'Guilherme'
idade = 28
profissao = 'Programador'
linguagem = 'Python'

print('Olá, me chamo %s.Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s.' % (nome, idade, profissao, linguagem))
# >>> Olá, me chamo Guilherme.Eu tenho 28 anos de idade, trabalho como Programador e estou matriculado no curso de Python.

#A % (variável) é para interpolação de variáveis, e dentro da string, %s é um espaço reservado para uma string, %d para um inteiro e %f para um float
#A %s é utilizada para strings, %d para inteiros e %f para floats.


#Método format

nome = 'Guilherme'
idade = 28
profissao = 'Programador'
linguagem = 'Python'

print('Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.'.format(nome, idade, profissao, linguagem))
# >>> Olá, me chamo Guilherme. Eu tenho 28 anos de idade, trabalho como Programador e estou matriculado no curso de Python.

#A função format() é utilizada para interpolar variáveis em strings, e dentro da string, {} é um espaço reservado para uma variável.

print ('Olá, me chamo {0}. Eu tenho {1} anos de idade, trabalho como {2} e estou matriculado no curso de {3}.'.format(nome, idade, profissao, linguagem))
# >>> Olá, me chamo Guilherme. Eu tenho 28 anos de idade, trabalho como Programador e estou matriculado no curso de Python.
#Esse método permite que você especifique a ordem das variáveis dentro da string, utilizando índices numéricos.

print ('Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.'.format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))
# >>> Olá, me chamo Guilherme. Eu tenho 28 anos de idade, trabalho como Programador e estou matriculado no curso de Python.
#Esse método é mais legível e fácil de entender, além de permitir a utilização de nomes de variáveis dentro da string.

pessoas = {'nome': nome, 'idade': idade, 'profissao': profissao, 'linguagem': linguagem}
print('Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.'.format(**pessoas))
# >>> Olá, me chamo Guilherme. Eu tenho 28 anos de idade, trabalho como Programador e estou matriculado no curso de Python.
#Esse método permite que você utilize um dicionário para interpolar variáveis em strings, utilizando o operador ** para desempacotar o dicionário.


#Formatar Strings com f strings
PI = 3.14159

print(f'O valor de PI é {PI:.2f}.')
# >>> O valor de PI é 3.14.

print(f'O valor de PI é {PI:10.2f}.')
# >>> O valor de PI é      3.14.

print (f'Nome: {nome}, Idade: {idade}, Profissão: {profissao}, Linguagem: {linguagem}')

#A f string é uma forma mais moderna e recomendada de interpolar variáveis em strings, onde você pode utilizar expressões dentro das chaves {} e o prefixo f antes da string.



#Resumo : Aprendemos 3 formas de interpolar variáveis em Strings em Python, a primeira é usando o sinal %, a segunda é utilizar o método format e a última é utilizar f strings. A primeira forma não é atualmente recomendada e seu uso em Python 3 é raro. A segunda forma é mais legível e fácil de entender, além de permitir a utilização de nomes de variáveis dentro da string. A terceira forma é a mais moderna e recomendada, onde você pode utilizar expressões dentro das chaves {} e o prefixo f antes da string.

#Oque é Interpolação de Variáveis?
#Interpolação de variáveis é o processo de inserir valores de variáveis dentro de uma string

