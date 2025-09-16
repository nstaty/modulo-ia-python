# Programa que calcula dias de vida

from datetime import datetime

data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
dia, mes, ano = map(int, data_nascimento.split("/"))
nascimento = datetime(ano, mes, dia)

hoje = datetime.now()
dias_de_vida = (hoje - nascimento).days

print(f"Você está vivo há aproximadamente {dias_de_vida} dias.")
