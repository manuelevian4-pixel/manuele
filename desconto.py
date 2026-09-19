valor = float(input("Digite o valor do produto: "))
desconto = float(input("Digite o percentual de desconto (%): "))

if desconto < 0 or desconto > 100:
    print("Desconto inválido. Digite um valor entre 0 e 100%.")
else:
    valor_do_desconto = valor * (desconto / 100)
    valor_final = valor - valor_do_desconto

    print(f"Valor original: R$ {valor:.2f}")
    print(f"Desconto aplicado: {desconto:.0f}%")
    print(f"Valor do desconto: R$ {valor_do_desconto:.2f}")
    print(f"Valor com desconto: R$ {valor_final:.2f}")
