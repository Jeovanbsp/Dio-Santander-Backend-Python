#Precedencia de Operadores
#Na matemática existe uma regra que indica quais operações devem ser executadas primeiro. Isso é útil pois ao analisar uma expressão, a depender da ordem das operações o valor pode ser diferente: 

# x = 10 - 5 * 2
# x é igual a 10 ou 0 ?
# A Definição indica a seguinda ordem como a correta:
#Parêntesis / Expoêntes / Multiplicação e Divisões (Da Esquerda para a Direita) / Somas e Substração (Da esquerda para a Direita)

print (10 - 5 * 2)
>>> 0

print((10 - 5) * 2)
>>> 10

print (10 ** 2 * 2)
>>> 200

print (10 ** (2 * 2))
>>> 10000

prit (10 / 2 * 4)
>>> 20.0