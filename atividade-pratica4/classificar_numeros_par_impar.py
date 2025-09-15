# Classificador de Números

pares = 0
impares = 0

while True:
    entrada = input("Digite um número (ou 'sair' para encerrar): ")
    if entrada.lower() == "sair":
        break
    numero = int(entrada)
    
    if numero % 2 == 0:
        pares += 1
        print(f"{numero} é PAR")
    else:
        impares += 1
        print(f"{numero} é ÍMPAR")

print(f"Total de números pares: {pares}")
print(f"Total de números ímpares: {impares}")
