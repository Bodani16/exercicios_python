#entrada
peso = float(input("Digite seu peso em KG: "))
alt = float(input("Digite seu altura em M: "))
#processamento
IMC = peso / (alt**2)

print(f"seu peso é: {peso}")

if IMC < 18.5:
    print("Abaixo do peso")
elif IMC < 25:
    print("Peso normal ")
else:
    print("Obeso!")