#Seção : Operadores de Lógica
#Objetivo geral : O que são operadores lógicos e como utilizá-los
#Etapa 1: Conhecendo os Operadores Lógicos
#O que são ? São operadores utilizados em conjunto com os osperadores ded comparação, para montar uma expressão lógica. Quando um operador de comparação é utilizado, o resultado é um valor booleano (True ou False), dessa forma podemos combinar operadores de comparação com os operadores lógicos, Exemplo: op_comparação + op_lógico + op_comparação... N ...

#Exemplo : Operador de Comparação
Saldo = 1000
Saque = 200
Limite = 100

Saldo >= Saque
# >>> True

Saque <= Limite
# >>> False

#Operador E 
Saldo = 2000
Saque = 200
Limite = 100

Saldo >= Saque and Saque <= Limite
#As Duas condições devem ser verdadeiras para que o resultado seja True (Expressão Lógica)
# >>> False

#Operador OU
Saldo = 2000
Saque = 200
Limite = 100

Saldo >= Saque or Saque <= Limite
#Apenas uma das condições deve ser verdadeira para que o resultado seja True (Expressão Lógica)
# >>> True

#Operador Negação
#O operador not inverte o valor booleano da expressão
#Se a expressão for True, o resultado será False, e vice-versa.
contatos_emergenciais = []

not 1000 > 1500
#A negação inverte o valor booleano da expressão
# >>> True

not contatos_emergenciais
# A expressão contatos_emergenciais é uma lista vazia, que é avaliada como False
# >>> True

not "Saque 1500;"
# A expressão "Saque 1500;" é uma string não vazia, que é avaliada como True
# >>> False

not ""
# A expressão "" é uma string vazia, que é avaliada como False
# >>> True

#Parênteses
#Podemos utilizar parênteses para agrupar expressões lógicas e controlar a ordem de avaliação
Saldo = 1000
Saque = 250
Limite = 200
contatos_emergenciais = True

exp1 = Saldo >= Saque and Saque <= Limite or contatos_emergenciais and Saldo >= Saque
# A expressão é avaliada da seguinte forma:
# 1. Saldo >= Saque (True)
# 2. Saque <= Limite (False)
# 3. contatos_emergenciais (True)
# 4. Saldo >= Saque (True)
# O resultado final é True, pois a expressão é avaliada como (True and False) or (True and True)
# >>> True

print (exp1)

exp2 = (Saldo >= Saque and Saque <= Limite) or (contatos_emergenciais and Saldo >= Saque)
# A expressão é avaliada da seguinte forma:
# 1. (Saldo >= Saque and Saque <= Limite) (True and
# False) => False
# 2. (contatos_emergenciais and Saldo >= Saque) (True and True) => True
# O resultado final é True, pois a expressão é avaliada como False or True
# >>> True

print (exp2)

conta_normal_com_saldo_suficiente = Saldo >= Saque and Saque <= Limite
conta_especial_com_saldo_suficiente = contatos_emergenciais and Saldo >= Saque

exp3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
# A expressão é avaliada da seguinte forma:
# 1. conta_normal_com_saldo_suficiente (True)
# 2. conta_especial_com_saldo_suficiente (True)
# O resultado final é True, pois a expressão é avaliada como True or True
print (exp3)

#Operador AND (E)
# O operador and retorna True se ambas as condições forem verdadeira

print (True and True )
# As duas condições são verdadeiras, então o resultado é True
print (True and False)
# Apenas uma das condições é verdadeira, então o resultado é False
print (False and False)
# Ambas as condições são falsas, então o resultado é False

#Operador OR (OU)
# O operador or retorna True se pelo menos uma das condições for verdadeira

print (True or True)
# Ambas as condições são verdadeiras, então o resultado é True
print (True or False)
# Apenas uma das condições é verdadeira, então o resultado é True
print (False or False)
# Ambas as condições são falsas, então o resultado é False

