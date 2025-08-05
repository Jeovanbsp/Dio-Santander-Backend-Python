#Estruturas de Repetições
#Objetivo Geral: Conhecer as Estruturas de Repetição For e While e quando utilizá-las
#Etapa 1: O que são estruturas de repetição?
#Etapa 2: Comando For e a função Built-in range()
#Etapa 3: Comando While


#O que são estruturas de repetição?
# São estruturas utilizadas para repetir um trecho de código um determinado número de vezes. Esse número pode ser conhecido previamente ou dedtermiado através de uma expressão lógica.
#Exemplo : Receba um número do teclado e exiba os 02 números seguintes.
a = int(input('Informe um número Inteiro:'))
print (a)

a += 1
print (a)

a += 1
print (a)

#Exemplo 2: Receba um número do teclado e exiba os 02 números seguintes.

a = int(input('Informe um número Inteiro:'))

for i in range(2):
    a += 1
    print(a)

#Comando For : O comando for é usado para pecorrer um objeto iterável.Faz sentido usar for quando sabemos o número exato de vezes que nosso bloco de código deve ser executado, ou quando queremos percorrer um objeto iterável.

texto = input('Informe um texto: ')
VOGAIS = 'AEIOU'
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=' ')
else:
print() #adciona uma quebra de linha

#Função Range : Range é uma função built-in do Python, ela é usada para produzir uma sequência de números inteiros a partir de um ínicio (inclusivo) para um fim (exclusivo). Se ursamor range (i,j) será produzido: i , i+1 , i+2, i+3, ..., j-1.  Ela recebe 3 argumentos:stop (obrigatório), start (opcional) e step opcional.

#range(stop) -> range object
#range(start, stop[, step]) -> range object

list(range(4)) >> # [0, 1, 2, 3]


#Utilizando range com o comando for
for numero in range(0,11):
    print(numero, end=' ')

# >>> 0 1 2 3 4 5 6 7 8 9 10

#Exibindo a Tabuada do 5
for numero in range(0, 51 , 5):  #Contando de 0 a 50 de 5 em 5
    print(numero, end=' ')

# >>> 0 5 10 15 20 25 30 35 40 45 50


#Comando While: O comando wile é usado para repetir um bloco de código várias vezes. Faz sentido usar while quando não sabemos o número exato de vezes que nosso bloco de código deve ser executado.


opção = 1

while opção != 0:
    opção = int(input('[1] Sacar \n [2] Depositar \n [0] Sair \n Escolha uma opção: '))
    if opção == 1:
        print('Sacando...')
    elif opção == 2:
        print('Depositando...')
    elif opção == 0:
        print('Saindo...')
else:
    print('Obrigado por usar nosso sistema Bancário, Até logo.')


#Exemplo  de uso do comando Break: O comando break é usado para interromper um loop antes que ele tenha terminado naturalmente. Ele pode ser usado em loops for e while.
while True:
    número = int(input('Informe um número:'))

    if número == 10:
        break

print(número)

for número in range (100):
    if número == 10:
        break
    print(número)


#Exemplo de uso do comando Continue: O comando continue é usado para pular a iteração atual de um loop e continuar com a próxima iteração. Ele pode ser usado em loops for e while.

for número in range (100):
    if número == 12:
        continue
    print(número)


