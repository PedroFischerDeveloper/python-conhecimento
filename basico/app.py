# Variáveis o python infere automaticamente o tipo de dado, ou seja não é necessário declarar o tipo.

numero_inteiro = 10     # inteiro
numero_decimal = 10.5   # float
nome = "Pedro Fischer"  # String
is_active = True        # Booleano

print(numero_inteiro)
print(numero_decimal)
print(nome)
print(is_active)

# O Python suporta operações aritiméticas básicas
soma = 10 + 5 
produto = 10 * 2 
divisao = 10 / 2  # Divisão (aqui retornamos um float)
divisao_exata = 7 // 2  # Divisão retornando inteiro
expoente = 2 ** 3 # Exponenciação

print(soma)
print(produto)
print(divisao)
print(divisao_exata)
print(expoente)

# Estruturas condicionais - note que o if não tem parenteses, usamos : ao final do if para ir para a próxima instrução
idade = 18
if idade >= 18:
    print("Maior de idade")
elif idade >= 16:
    print("Quase lá")
else:
    print("Menor de idade")



# CONSTANTE NÃO SÃO NATIVAS NO PYTHON, MAS POR CONVENÇÃO USAMOS LETRA MAISCULA PARA INDICAR CONSTANTE E QUE NÃO DEVE SER ALTERADA
# observe também que ao invés de usarmos else if -> utilizamos elif para indicar "se não se"
SEXO = "M"
if SEXO == "M":
    print("Masculino")
else:
    print("Feminino")


# LAÇOS DE REPETIÇÃO

ENDFOR = 5
# laço for REPETE até chegar ao valor pré definido
for i in range(ENDFOR):
    print(i) # imprimi os valores


# Repete até que a condição final seja falsa, no nosso caso enquanto for menor que 5
contador = 0
while contador < 5:
    print(contador)
    contador += 1


# Funções -> são definidas pela palavra pré definida def
def saudacao(nome):
    print(f"Olá, {nome}!") # observe o f (string formatada), isso permite inferir o valor direto na string dentro dos {} como demonstrado no exemplo

saudacao("Pedro")  # Imprimi Olá Pedro

# as funções também tem retorno
def saudacao_retorno(nome):  
    return f"Olá, {nome}!"

mensagem = saudacao_retorno("Pedro")  
print(mensagem) 


# Listas: são coleções ordenadas de itens que podem ser alterados.
frutas = ["maçã", "banana", "laranja"]
frutas.append("uva")  # Adiciona "uva" à lista
print(frutas[0])  # Imprime "maçã"

# Dicionários: armazenam pares chave-valor.
pessoa = {"nome": "Ana", "idade": 25}
print(pessoa["nome"])  # Imprime "Ana"


