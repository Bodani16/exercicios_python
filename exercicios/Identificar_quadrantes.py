x = float(input("Qual é o seu valor x: "))
y = float(input("Qual é o seu valor y: "))

if x > 0 and y > 0:
    print("Primeiro quadrante")
elif x < 0 and y > 0:
    print("segundo quadrante")
elif x < 0 and y < 0:
    print("terceiro quadrante")
elif x > 0 and y < 0:
    print("Quarto quadrante")
else:
    print("O ponto está localizado no eixo ou origem.")