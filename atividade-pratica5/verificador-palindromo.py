# Função para verificar palíndromo

def eh_palindromo(texto: str) -> bool:
    texto_limpo = ''.join(c.lower() for c in texto if c.isalnum())
    return texto_limpo == texto_limpo[::-1]

# Exemplo de uso
frase = input("Digite uma palavra ou frase: ")
if eh_palindromo(frase):
    print("Sim, é palíndromo!")
else:
    print("Não, não é palíndromo.")
