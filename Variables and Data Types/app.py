# Variáveis em Python
# Uma variável é usada para armazenar dados na memória. Em Python, 
# você não precisa declarar explicitamente o tipo da variável; 
# o Python faz isso automaticamente com base no valor que você atribui.

x = 5  # inteiro
nome = "Pedro" # string

# Tipos de Dados em Python Python possui vários tipos de dados embutidos. Alguns dos mais comuns são:

# Inteiros (int): Números inteiros, como 1, 0, -5.
x = 10

# Ponto flutuante (float): Números com casas decimais.
preco = 19.99

# Strings (str): Sequências de caracteres entre aspas simples ou duplas.
nome = "Pedro"

# Booleanos (bool): Representam valores lógicos, sendo True (verdadeiro) ou False (falso).
ativo = True

# Listas (list): Estruturas que podem armazenar múltiplos itens, de diferentes tipos.
numeros = [1, 2, 3, 4]

# Tuplas (tuple): Semelhantes às listas, mas imutáveis, ou seja, não podem ser modificadas.
cores = ("vermelho", "azul", "verde")

# Dicionários (dict): Armazenam pares de chave-valor.
aluno = {"nome": "Pedro", "idade": 21}

# Conjuntos (set): Coleção de elementos únicos e não ordenados.
frutas = {"maçã", "banana", "laranja"}


# Mudança Dinâmica de Tipos
# Python é uma linguagem de tipagem dinâmica, o que significa que você pode mudar o tipo de uma variável atribuindo um novo valor a ela.
x = 10    # x é um inteiro
x = "Olá" # Agora x é uma string


# Verificar o Tipo de uma Variável você pode verificar o tipo de uma variável usando a função type().
x = 5
print(type(x))  # Saída: <class 'int'>

nome = "Pedro"
print(type(nome))  # Saída: <class 'str'>



