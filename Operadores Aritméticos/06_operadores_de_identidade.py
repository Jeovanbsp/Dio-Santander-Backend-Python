#Seção : Operadores de Identidade
#Objetivo: O que são os operadores de identidade e como utilizá-los
#Etapa 1: Conhecendo os operadores de identidade
#o que são ? São operadores utilizados para comprarar se os dois objetos testados ocupam a mesma posição na memória.

#Exemplo:
curso = 'Curso de Python'
nome_curso = curso
saldo , limite = 200, 200

#O operador is compara se os dois objetos ocupam a mesma posição na memória.
#O operador is not compara se os dois objetos não ocupam a mesma posição na memória.

curso is nome_curso
#>>> True
# curso e nome_curso ocupam a mesma posição na memória, por isso o operador is retorna Tru

curso is not nome_curso
#>>> False
# curso e nome_curso ocupam a mesma posição na memória, por isso o operador is not retorna False

saldo is limite #Valores Inteiros
#>>> True
# saldo e limite ocupam a mesma posição na memória, por isso o operador is retorna True


#Valores diferentes
saldo = 1000
limite = 500

print (saldo is limite) 
#Ele retorna False, pois saldo e limite ocupam posições diferentes na memória.
print (saldo is not limite)
#Ele retorna True, pois saldo e limite ocupam posições diferentes na memória.


#valores iguais
saldo = 1000
limite = 1000

print (saldo is limite)
#Ele retorna True, pois saldo e limite ocupam a mesma posição na memória.
print (saldo is not limite)
#Ele retorna False, pois saldo e limite ocupam a mesma posição na memória.