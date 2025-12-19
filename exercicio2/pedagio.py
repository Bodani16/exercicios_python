#entradas
distancia = int(input("Digite o valor percorrido: "))

if distancia <= 100:
   #entrada
    print("R$:10,00")
elif 100 < distancia <= 200:
    print("R$:20,00")
else:
    print("R$:30,00")