atividade_A = int(input("Informe os dias para atividade A: "))
atividade_B = int(input("Informe os dias para atividade B: "))
atividade_C = int(input("Informe os dias para atividade C: "))


if atividade_A >= 0 and atividade_B >= 0 and atividade_C >= 0:
    tempo_total = atividade_A + atividade_B + atividade_C
    print(f"Seu tempo total foi: {tempo_total}")
else:
    print("Error: os dias não podem ser numeros negativos")