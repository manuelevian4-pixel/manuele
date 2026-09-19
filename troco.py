dinheiro = float(input("Dinheiro: "))
valor = float(input("Valor: "))

troco = dinheiro - valor
print(f"Seu troco é de: {troco}")

if troco < 0:
    print("Dinheiro insuficiente para a compra.")