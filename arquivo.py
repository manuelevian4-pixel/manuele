def calcular_soma(numero1, numero2):
    """
    Retorna a soma de dois números.
    """
    return numero1 + numero2


numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

resultado = calcular_soma(numero1, numero2)

print("A soma é:", resultado)