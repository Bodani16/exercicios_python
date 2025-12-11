#Ex.01
print("Descubra se seu numero é par ou impar: \n")

par_impar = int(input("Digite seu número: "))

formula_impar_par = par_impar % 2

if formula_impar_par == 0:
    print("Seu numero é: Par")
else:
    print("Seu numero é: Ímpar")