#criando dicionario
User = {
    "Nome": "Rafael",
    "Idade": 18,
    "Cidade": "Rio de Janeiro"
}
#add profissão
User["Profissão"] = "Programador"
#manipulando dicionario
User["Cidade"] = "Nova Iguaçu"
#removendo um intem do dicionario
del User["Idade"]

print(User)

#lista dos numeros a virarem quadrado.
nmr_quadrado = {
    1,2,3,4,5
}

#formula do numero ao quadrado
nmr_quadrado = {numero: numero**2 for numero in range(1, 6)}

print(nmr_quadrado)

#criando uma lista
Nome = {"Nome":"João",
        "Idade":"19",
        "Cidade":"Novaiguaçu"}
#verificando se na lista criada existe o nome joão
if Nome["nome"] == "João":
    print("sim") #se existe ele manda pra ca caso contrario exibe nao
else:
    print("não")
#nao fiz
frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)
        
