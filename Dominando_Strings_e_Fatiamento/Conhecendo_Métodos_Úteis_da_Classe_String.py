#Etapa 1: Conhecendo Métodos Úteis da Classe String
#String e Fatiamento
#Objetivo Geral: Conhecer métodos úteis para manipular objetos do Tipo String, Como interpolar valores de Variáveis e entender como funciona o fatiamento de Strings.

#A classe String do Python é famosa por ser rica em métodos e possuir uma interface muito fácil de trabalhar.
#Em algumas linguagens manipular sequências de caracteres não é um trabalho trivial, porém, em python esse trabalho é muito simples.

#Maiscula, Minúscula e Título

Curso = "pYtHon"

print(Curso.upper())  # Converte para maiúsculas
# >>> PYTHON 

print(Curso.lower())  # Converte para minúsculas
# >>> python

print(Curso.title())  # Converte a primeira letra de cada palavra para maiúscula
# >>> Python

#Eliminado Espaços em Branco 
Curso = "   Python   "

print(Curso.strip())  # Remove espaços em branco no início e no final
# >>> Python

print(Curso.lstrip())  # Remove espaços em branco apenas no início (left strip)
# >>> Python

print(Curso.rstrip())  # Remove espaços em branco apenas no final (right strip)
# >>> "   Python"

#Junções e Centralização
Curso = "Python"

print(Curso.center(10, '*'))  # Centraliza a string em um campo de 20 caracteres, preenchendo com '*'

# >>> **Python***

print(".".join(curso)) # Junta os caracteres da string com '.' como separador
# >>> P.y.t.h.o.n