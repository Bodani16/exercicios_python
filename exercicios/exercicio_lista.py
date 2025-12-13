#lista com respectivos valores
nomes = ["Rafael","Maria","João","Felipe"]
ano_nascimento = 2007
ano_atual = 2025
anos = [ano_nascimento, ano_atual]
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"Lista de números:{numeros} ")
print(f"Lista de anos: {anos}")
print(f"Lista de nomes: {nomes}")

#exibir cada elemento da lista numeros
for cadaum in numeros:
    print(f"Elemento da lista: {cadaum}")

#soma dos numeros impar dentro de 1, 25
soma_impar = 0
for numero in range(1,25):
    if numero % 2 != 0: #verificando se o número é par
        soma_impar += numero
print(f"Soma deu: {soma_impar}")

#exibir numero em ordem descrescente
for numeros_descrescente in range(25, 0, -1):
    print(numeros_descrescente)

#calcular tabuada:
numero_tabuada = int(input("Qual seu numero: "))
for i in range(1, 11):
    print(f"{numero_tabuada} x {i} = {numero_tabuada * i}")


somar_numero = [1,2,3,4,5]

try:
    somar = 0
    for fish in somar_numero:
        somar += fish
    print(f"Soma dos elementos: {somar}")
except ValueError:
    print("Não é um numero")
except Exception as error:
    print(f"ocorreu um erro: {error}")