#Seção : Operadores de Associação
#Objetivo: O que são operadores de associação e como utilizá-los
#Etapa 1: Conhecendo os Operadores de Associação
#O que são ? São operadores utilizados para verificar se um objeto está presente em uma sequência.

#Exemplo :
curso = 'Curso de Python'
frutas = ['laranja','uva','limão']
saque = [1500, 100]

#O Operador 'in' verifica se um elemento está presente na sequência.
#O Operador 'not in' verifica se um elemento não está presente na sequência.

'Python' in curso  # Verifica se 'python' está em 'Curso de Python'
#>>> True

'maça' not in frutas  # Verifica se 'maça' não está na lista de frutas
#>>> True

200 in saque  # Verifica se 200 está na lista de saques
#>>> False


frutas ['limão', 'uva', 'laranja']

print('laranja' in frutas)  # Verifica se 'laranja' está na lista de frutas
#>>> True

#O l tem que ser minúsculo para ser encontrado
print('Laranja' in frutas)  # Verifica se 'Laranja' está na lista de frutas
#>>> False

print ('limão' in frutas)  # Verifica se 'limão' está na lista de frutas
#>>> True