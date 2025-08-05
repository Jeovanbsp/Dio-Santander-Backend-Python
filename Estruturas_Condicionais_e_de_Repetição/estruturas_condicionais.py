#Estruturas Condicionais 
#Objetivo Geral : Entender o que são estruturas condicionais e como utilizá-las
#ETAPA 1: IF / IF - ELSE / ELIF
#ETAPA 2: IF alinhado
#ETAPA 3: IF Ternário

#O que são ? A Estrutura Condicional permite o desvio de fluxo de Controle, Quando determinadas expressões lógicas são atendidas.

#IF  - > Para criar estruturas condicional simples, composta por uma único desvio, podemos utilizar a palavra reservada IF, O comando irá testar a expressão lógica, e em caso de retorno verdadeiro as ações presentes no bloco de código do IF serão executadas.
#Exenplo:
saldo = 2000
saque = float(input('Informe o valor do saque: '))
if saldo >= saque:
    print('Realizado Saque!')
if saldo < saque:
    print('Saldo insuficiente!')

#IF - ELSE -> Para criar uma estrutura condicional com dois desvios,podemos utilizar as palavras reservadas IF e ELSE, Como sabemos se a expressão lógica testada no IF for verdadeira, então o bloco de código do IF será executado, caso contrário o bloco de código do ELSE será executado.
#Exemplo:
saldo = 2000
saque = float(input('Informe o valor do saque: '))
if saldo >= saque:
    print('Realizado Saque!') 
else:
    print('Saldo insuficiente!')

#IF - ELIF - ELSE -> Em alguns cenários queremos mais de dois desvios,para isso podemos utilizar a palavra reservada ELIF. O ELIF é composto por uma nova expressão lógica, que será testada e caso retorne verdadeiro, o bloco de código do ELIF será executado, caso contrário o fluxo de controle seguirá para o próximo desvio, que pode ser um novo ELIF ou o ELSE.
#Exemplo:
opcao = int(input('Informe a opção : [1] Sacar \n [2] Extrato: '))
if opcao == 1:
    valor = float(input('Informe o valor do saque: '))
    #...
elif opcao == 2:
    print('Exibindo Extrato...')
else:
    sys.exit('Opção inválida!')

#Exemplo ::

Maior_Idade = 18
Idade_especial = 17

idade = int(input('Informe a sua idade: '))
#Ira Pergunta a Idade do usuário e verificar se ele é maior de idade ou não.

if idade >= Maior_Idade:
    print('Você é maior de idade,Pode tirar CNH!') 

if idade < Maior_Idade:
    print('Você é menor de idade, Não pode tirar CNH!')

if idade >= Maior_Idade:
    print('Você é maior de idade,Pode tirar CNH!')

else :
    print('Você é menor de idade, Não pode tirar CNH!')

#Idade Especial (ELIF)

if idade >= Maior_Idade:
    print('Você é maior de idade,Pode tirar CNH!')
elif idade == Idade_especial
    print('Pode fazer aulas teoricas, mas não pode fazer aulas práticas!')
else :
    print('Você é menor de idade, Não pode tirar CNH!')


#IF Alinhado -> Podemos criar estruturas condicionais alinhadas, para isso basta adicionar estruturas IF/ELIF/ELSE dentro do bloco de código de estruturas IF/ELIF/ELSE, e assim sucessivamente, criando uma estrutura condicional alinhada.
#Exemplo:
conta_normal = True
conta_univesitaria = False

saldo = 2000
saque = 500
chque_especial = 450


if conta_normal:
    if saldo >= saque:
        print('Realizado Saque!')
    elif saque <= (saldo + cheque_especial):
        print('Realizado Saque com cheque especial!')
    else:
        print('Não foi possível realizar o saque,Saldo insuficiente!')
elif conta_univesitaria:
    if saldo >= saque:
        print('Saque Realizado com Sucesso!')
    else:
        print('Saldo insuficiente!')
else:
    print('Sistema não reconheceu seu tipo de conta, entre em contato com o seu gerente!')

        

# IF Ternário -> O IF ternário permite escrever uma condição em uma única linha. Ele é composto por três partes, a Primeira parte é o retorno caso a expressão retorne verdadeiro, a segunda parte é a expressão lógica e a terceira parte é o retorno caso a expressão não seja atendida
saldo = 2000
saque 2500

status = "Sucesso" if saldo >= saque else "Falha"
print(f'Saque {status} ao realizar o saque!')