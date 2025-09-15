# Conversor de Temperatura

print("Unidades disponíveis: Celsius (C), Fahrenheit (F), Kelvin (K)")
valor = float(input("Digite a temperatura: "))
origem = input("Informe a unidade de origem (C/F/K): ").upper()
destino = input("Informe a unidade de destino (C/F/K): ").upper()

resultado = None

# Converter para Celsius como base
if origem == "C":
    temp_c = valor
elif origem == "F":
    temp_c = (valor - 32) * 5/9
elif origem == "K":
    temp_c = valor - 273.15
else:
    print("Unidade de origem inválida!")

# Converter para destino
if destino == "C":
    resultado = temp_c
elif destino == "F":
    resultado = (temp_c * 9/5) + 32
elif destino == "K":
    resultado = temp_c + 273.15
else:
    print("Unidade de destino inválida!")

if resultado is not None:
    print(f"{valor:.2f} {origem} = {resultado:.2f} {destino}")
