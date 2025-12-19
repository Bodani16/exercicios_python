impar_par = int(input("Digite seu número: "))
verificar_impar_par = impar_par % 2

if verificar_impar_par == 0:
    print(f"Seu número {impar_par}, é par. ")
else:
    print(f"Seu número {impar_par}, é impar. ")