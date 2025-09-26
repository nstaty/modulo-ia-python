# Este programa 

nome_produto = input("Digite o nome do produto: ")
preco_unitario = float(input("Digite o valor unitário do produto: "))   
quantidade = int(input("Digite a quantidade de produtos: "))

preco_total = preco_unitario * quantidade

print(f"\nProduto: {nome_produto}")
print(f "Preço unitário: R$ {preco_unitario:.2f}")
print(f "Quantidade: {quantidade}")
print(f "Total R$: {preco_total:.2f}")