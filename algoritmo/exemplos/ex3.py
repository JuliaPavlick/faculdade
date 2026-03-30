nome = 'Ana'
idade = 20
altura = 1.65
# f-string básica
print(f'Nome: {nome}')
# → Nome: Ana
# Com múltiplas variáveis
print(f'{nome} tem {idade} anos')
# → Ana tem 20 anos
# Com expressão dentro
print(f'Nasceu em {2026 - idade}')
# → Nasceu em 2004

# As f-strings (strings formatadas) permitem inserir variáveis e expressões
# diretamente dentro de textos usando {}.

# No primeiro print, o valor da variável "nome" é inserido na frase,
# resultando em: Nome: Ana

# No segundo print, duas variáveis são usadas na mesma string,
# formando a frase completa: Ana tem 20 anos

# No terceiro print, há uma expressão matemática dentro das chaves.
# O Python calcula 2026 - idade (2026 - 20 = 2006) e mostra o resultado.
# Ou seja, além de variáveis, também é possível fazer cálculos dentro da f-string.