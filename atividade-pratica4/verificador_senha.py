# Verificador de Senha

senha = input("Digite sua senha: ")

tem_numero = any(char.isdigit() for char in senha)

if len(senha) >= 8 and tem_numero:
    print("✅ Senha válida!")
else:
    print("❌ Senha inválida! Ela deve ter pelo menos 8 caracteres e conter pelo menos 1 número.")
