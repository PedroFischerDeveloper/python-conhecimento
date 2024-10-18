# Conditionals (ou condicionais) 
# são estruturas que permitem executar diferentes blocos de código com base em condições específicas. 
# O principal comando condicional em Python é o if, que pode ser complementado por elif (else if) e else.

condição1 = True
condição2 = False

if condição1:
    # Código a ser executado se condição1 for verdadeira
    print("Condição 1 é verdadeira")
elif condição2:
    # Código a ser executado se condição1 for falsa e condição2 for verdadeira
    print("Condição 2 é verdadeira")
else:
    # Código a ser executado se todas as condições acima forem falsas
    print("Nenhuma condição é verdadeira")


idade = 18
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")


nota = 75
if nota >= 90:
    print("Aprovado com louvor")
elif nota >= 70:
    print("Aprovado")
elif nota >= 50:
    print("Recuperação")
else:
    print("Reprovado")


# Operadores de Comparação
# Você pode usar operadores de comparação nas condições, como:

# == (igual a)
# != (diferente de)
# > (maior que)
# < (menor que)
# >= (maior ou igual a)
# <= (menor ou igual a)
# Operadores Lógicos
# Além disso, você pode combinar condições usando operadores lógicos:

# and: Verdadeiro se ambas as condições forem verdadeiras.
# or: Verdadeiro se pelo menos uma das condições for verdadeira.
# not: Inverte o valor da condição.