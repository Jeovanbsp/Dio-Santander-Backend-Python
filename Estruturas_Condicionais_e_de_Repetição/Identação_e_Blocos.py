#Identação e Blocos
#Objetivo Geral: Aprender como o Interpretador Python utiliza a identação do código para delimitar os blocos de comandos.


#Estética > Identar código é uma forma de manter o código fonte mais légivel e manutenível. Mas em Python ela exerce um segundo papel, através da identação o interpretador consegue determinar onde um bloco de comando incia e onde ele termina.

#Bloco de Comando > As linguagens de Programação constumam utilizar caracteres ou palavras reservadas para terminar o início e fim do bloco. Em Java e C por exemplo, utilizamos Chaves:

#Bloco em Java

 Void sacar (double valor) { // início do bloco do método
                 if (this.saldo >= valor) { // início do bloco do if
                        this.saldo -= valor;
     } // fim do bloco do if
 } // fim do bloco do método 

#Bloco em java sem Formatar

Void sacar (double valor) { // início do bloco do método
if (this.saldo >= valor) { // início do bloco do if
this.saldo -= valor;
} // fim do bloco do if
} // fim do bloco do método

#Utilizando espaços > Existe uma convenção em Python, que define as boas práticas para escria de código na linguagem. Nesse documento é indicado utilizar 4 espaços em branco por nível de indentação, ou seja, a cada novo bloco adicionamos 4 novos espaços em branco.

#Bloco em Python
def sacar(self,valor: float): -> # início do bloco do método
    if self.saldo >= valor: -> # início do bloco do if
        self.saldo -= valor -> 
    # fim do bloco do if
# fim do bloco do método

#Bloco em Python sem Formatar
def sacar(self,valor: float): -> # início do bloco do método
if self.saldo >= valor: -> # início do bloco do if
self.saldo -= valor ->
# fim do bloco do if
# fim do bloco do método

#Versão mais fácil para ler 
def sacar(self, valor: float):
    if self.saldo >= valor:
        self.saldo -= valor



#Exemplo de código 
def sacar (valor): # início do bloco do método
   saldo = 500     # início do bloco do método


   if saldo >= valor:  # início do bloco do if
      print("Saldo insuficiente") # fim do bloco do if
      print("Retire o seu dinheiro na boca do caixa") # fim do bloco do if

    print ('Obrigado por utilizar nosso sistema de saque') # fim do bloco do método

def depositar (valor): # início do bloco do método
    saldo = 500 # início do bloco do método
    saldo += valor # fim do bloco do método

sacar (10000) # Chamada do método