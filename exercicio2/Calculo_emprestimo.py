renda = float(input("Digite sua renda aqui: "))
parcela = float(input("Digite sua parcela aqui: "))

if renda > 2000 and parcela <= 0.3 * renda:
    print("Emprestimo concedido! ")
elif renda <= 2000:
    print("Emprestimo negado: renda insuficiente. ")
else:
    print("Emprestimo negado: parcela acima da renda.")