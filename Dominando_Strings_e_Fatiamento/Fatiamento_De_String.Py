#Fatiamento de Strings
#Etapa 3
#Introdução : Fatiamento de Strings é uma técnica utilizada para retornar substrings (Partes de Strings Original), informando inicio (Start), fim (Stop) e passo (Step): [Start:Stop[,Step]]

nome = "Guilherme Arthur de Carvalho"

nome [0] # Retorna o primeiro caractere
# >>> 'G'

nome [:9] # Retorna os primeiros 9 caracteres
# >>> 'Guilherme'

nome [10:] # Retorna do 10º caractere até o final
# >>> 'Arthur de Carvalho'

nome [10:16] # Retorna do 10º ao 16º caractere
# >>> 'Arthur'

nome [10:16:2] # Retorna do 10º ao 16º caractere, pulando de 2 em 2
# >>> 'Ahu'

nome [:] # Retorna a string completa
# >>> 'Guilherme Arthur de Carvalho'

nome [::-1] # Retorna a string completa, mas invertida
# >>> 'olhavraC ed ruhtrA emrehliG'
