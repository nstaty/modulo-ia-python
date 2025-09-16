# Programa que calcula preço final com desconto

preco = float(input("Digite o preço do produto: R$ "))
desconto = float(input("Digite a porcentagem de desconto (%): "))

valor_desconto = preco * (desconto / 100)
preco_final = preco - valor_desconto

print(f"Preço original: R$ {preco:.2f}")
print(f"Desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")
