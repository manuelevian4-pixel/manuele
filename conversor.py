seg = int(input("Digite o valor em segundos: "))

horas = seg // 3600
resto = seg % 3600
minutos = resto // 60
segundos = resto % 60
print(f"{seg} segundos são {horas} horas, {minutos} minutos e {segundos} segundos")