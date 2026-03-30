# Programa completo: cadastro simples
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura (m): '))
# Cálculo simples
ano_nascimento = 2024 - idade
# Exibindo resultados formatados
print()
print(f'=== Dados de {nome} ===')
print(f'Idade: {idade} anos')
print(f'Altura: {altura}m')
print(f'Ano de nascimento: {ano_nascimento}')

# Este programa realiza um cadastro simples de uma pessoa.
# Primeiro, ele solicita ao usuário que digite seu nome, idade e altura.
# O input() captura os dados como texto, então usamos:
# - int() para converter a idade em número inteiro
# - float() para converter a altura em número decimal

# Em seguida, o programa calcula o ano de nascimento
# subtraindo a idade do ano atual (no caso, 2024).

# Depois disso, ele exibe os dados no terminal de forma organizada,
# utilizando f-strings para inserir as variáveis dentro do texto.

# O print() vazio serve apenas para pular uma linha e deixar a saída mais organizada.

# Exemplo de saída no terminal:
# (supondo que o usuário digite: Ana, 20, 1.65)

# === Dados de Ana ===
# Idade: 20 anos
# Altura: 1.65m
# Ano de nascimento: 2004