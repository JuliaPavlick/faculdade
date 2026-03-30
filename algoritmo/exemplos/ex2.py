# SEM conversão (erro ao somar)
valor = input('Digite um numero: ')
# valor é '5' (string), não 5
# COM conversão (correto)
valor = int(input('Digite um numero: '))
# agora valor é 5 (inteiro)
resultado = valor + 10
print(resultado) # 15

# O input() sempre retorna o valor digitado como texto (string).
# Sem conversão, não é possível fazer operações matemáticas corretamente,
# pois o Python entende o valor como texto, não como número.

# Por isso, usamos int() para converter a entrada em um número inteiro.
# Assim, o valor pode ser utilizado em cálculos normalmente.

# No exemplo, o usuário digita um número (ex: 5),
# o valor é convertido para inteiro, somado com 10,
# e o resultado (15) é exibido no terminal.