# Type Casting
# Type Casting é o processo de converter uma variável de um tipo de dado para outro. 
# Em Python, isso é feito usando funções embutidas. Aqui estão alguns exemplos comuns:

# num = int(4.5)  # num será 4
num = int(4.5)  # num será 4


# float(): Converte um valor para um ponto flutuante.
num = float(5)  # num será 5.0


# str(): Converte um valor para uma string.
text = str(10)  # text será '10'

# list(): Converte um iterável em uma lista.
tup = (1, 2, 3)
lst = list(tup)  # lst será [1, 2, 3]

# tuple(): Converte um iterável em uma tupla.
lst = [1, 2, 3]
tup = tuple(lst)  # tup será (1, 2, 3)


# Exceptions

# Exceptions são erros que ocorrem durante a execução de um programa. 
# Em Python, você pode lidar com exceções usando blocos try e except. 
# Isso permite que você capture e trate erros sem interromper a execução do programa. 
# Aqui está um exemplo:

try:
    x = 10 / 0  # Tentativa de divisão por zero
except ZeroDivisionError:
    print("Erro: Divisão por zero!")


# Você também pode capturar múltiplas exceções:

try:
    x = int(input("Digite um número: "))  # Pode gerar um ValueError
    y = 10 / x  # Pode gerar um ZeroDivisionError
except ValueError:
    print("Erro: Por favor, insira um número válido.")
except ZeroDivisionError:
    print("Erro: Divisão por zero!")


# Usando finally
# O bloco finally é executado independentemente de uma exceção ter sido levantada ou não. 
# É útil para liberar recursos, como arquivos ou conexões de banco de dados.
try:
    f = open('file.txt', 'r')
    # Lê o arquivo
except FileNotFoundError:
    print("Arquivo não encontrado.")
finally:
    f.close()  # Garante que o arquivo seja fechado


# Resumo
# Type Casting: Converte tipos de dados usando funções como int(), float(), str(), etc.
# Exceptions: Erros que podem ser tratados com try, except e finally.
# Se precisar de exemplos específicos ou mais detalhes sobre algum dos tópicos, é só avisar!