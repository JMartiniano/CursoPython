'''
# O QUE SÃO VARIÁVEIS

Variáveis são espaços reservados na memória para armazenar dados temporários necessários para a execução de um código.
Quando estamos codificando um programa é inevitável o uso de variável, já que sempre será necessário armazenar algum dado que será processado e que gere o efeito desejado quando o código for executado.

Exemplos de dados que podemos precisar em um código: quando criamos um código para obter informações de um cliente de uma academia, iremos precisar de dados sobre este cliente, os dados que podemos imaginar é: altura, peso, idade, sexo e também dados pessoais como o nome e endereço desse aluno. Então se nosso código vai trabalhar com todos esses dados é necessário armazenar cada um desses dados em uma variável


# TIPOS DE VARIÁVEIS

[1] String (str): armazena somente valores em forma de texto, qualquer coisa armazenada em uma variável do tipo string é considerada um caractere textual. Comumente usada para armazenar palavras, frases ou até mesmo números mas que não terão valores matemáticos (não dá para fazer cálculo com esse número).

[2] Inteiro (int): armazena somente valores numéricos do tipo inteiro, ou seja, números inteiros que têm valor matemático (dá pra fazer cálculo com esse número). Valores inteiros são números que não possuem pontos ou vírgula. Exemplo: 1, 10, 345, 4837263, 584938237459584637. (O tamanho do número é infinito).

[3] Float (float): armazena somente valores numéricos fracionários, ou seja, números com ponto que têm valor matemático. Exemplo: 1.75, 2.487, 45.6, 6548.6214. (O tamanho do número é infinito).


# CRIANDO UMA VARIÁVEL

[1] Dê um nome à variável e iguale ela ao seu valor:
    nome = valor

[2] Quando damos nomes à uma variável temos que seguir regras:
    - Não contém acentuação ou caracteres especiais
    - Não contém espaços
    - Não começa com letras maiúsculas
'''

# Inicando as práticas

pesoDoCliente = 85 # Criando a variável pesoDoCliente com o valor inteiro 85
alturaDoCliente = 1.82 # Criando a variável alturaDoCliente com o valor float 1.75
nomeDoCliente = "Arlindo" # Criando a variável nomeDoCliente com o valor string Arlindo

print(type(pesoDoCliente)) # Mostra na tela o tipo da variável pesoDoCliente
print(type(alturaDoCliente)) # Mostra na tela o tipo da variável alturaDoCliente 
print(type(nomeDoCliente)) # Mostra na tela o tipo da variável nomeDoCliente

'''
# ENTENDENDO O QUE ACONTECEU NAS LINHAS 14, 15 e 16

[1] O comando print() mostra na tela tudo aquilo que for indicando para ele.
    Algo é indicado para um comando quando é posto dentro dos seus parênteses, logo, quando eu faço: 
        print("Batata")
    Eu estou indicando ao comando print a string Batata, com isso será mostrada na tela a palavra Batata.

[2] O comando type() retornar a informação sobre o tipo do dado que foi indicado para ele.
    Quando eu faço:
        type("Batata")
    Eu estou indicando ao comando type a sting Batata, com isso será verificado o tipo deste dado (string, inteiro ou float).

Mas somente o comando print() é capaz de mostrar algo na tela, o comando type consegue verificar o tipo de qualquer dado, porém é incapaz de mostrar isso na tela. Para resolver esse problema eu posso unir o comando type com o comando print.

Então vamos pensar: 

    [1] Eu quero verificar o tipo da variável pesoDoCliente, como posso fazer isso:
            Resposta: usando o comando type, desta forma: 
            type(pesoDoCliente)
    [2] Eu também quero que seja mostrado na minha tela o tipo da variável pesoDoCliente, como posso fazer isso:
            Resposta: usando o comando print, ele pode me mostrar o que o type verificou. Desta forma: 
            print(type(pesoDoCliente))
'''

pesoDoCliente = str(pesoDoCliente) # Muda o tipo da variável pesoDoCliente para o tipo string

'''
# ENTENDENDO O QUE ACONTECEU NA LINHA 44

[1] O comando str(), int() e float() convertem, respectivimante, qualquer valor que for indicado para eles em valores do tipo string, inteiro e float.
    Logo, quando faço:
        str(variavelqualquer)
    Eu estou convertendo para string o valor contido na variável variavelqualquer

[2] Quando o comando str(), int() ou float() é usado, essa conversão não fica armazenada em local nenhum, à menos que eu indique para este comando uma variável onde ele deve armazenar o dado convertido.

[3] Já sabemos que uma variável deve ser criada com um nome, um sinal de igual e seu valor ( nome = valor ), então vamos criar uma varíável nova para adicionar à ela o valor da conversão do str(). (O mesmo pode ser feito com int() e float()).

[4] Quando falamos em conversão de variáveis não faz sentido mudar o nome dela, então abrimos uma nova variável com o mesmo nome da variável que estamos convertendo e passamos como valor o comando de conversão:
    pesoDoCliente = str(pesoDoCliente)

Se eu quisesse mudar o nome desta variável convertida era só dar um nome diferente:
    pesoDoClienteConvertido = str(pesoDoCliente)
'''

print(type(pesoDoCliente)) # Mostra na tela o tipo da variável pesoDoCliente
print(type(alturaDoCliente)) # Mostra na tela o tipo da variável alturaDoCliente
print(type(nomeDoCliente)) # Mostra na tela o tipo da variável nomeDoCliente