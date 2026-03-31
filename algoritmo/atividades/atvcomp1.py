from datetime import date

print("===== EXERCÍCIO 1 =====")
nome = input("Qual é o seu nome? ")
print(f"Olá, {nome}! Seja bem-vinda ao Python!")

print("\n===== EXERCÍCIO 2 =====")
numero = int(input("Digite um número: "))
dobro = numero * 2
print(f"O dobro de {numero} é {dobro}")

print("\n===== EXERCÍCIO 3 =====")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
soma = num1 + num2
print(f"A soma de {num1} e {num2} é {soma}")

print("\n===== EXERCÍCIO 4 =====")
ano_nascimento = int(input("Digite seu ano de nascimento: "))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
print(f"Você tem {idade} anos")

print("\n===== EXERCÍCIO 5 =====")
salario = float(input("Digite seu salário atual: "))
aumento = salario * 0.10
novo_salario = salario + aumento
print(f"Salário atual: R$ {salario:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")

print("\n===== EXERCÍCIO 6 =====")
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C equivale a {fahrenheit}°F")

print("\n===== EXERCÍCIO 7 =====")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
cidade = input("Digite sua cidade: ")
print(f"Nome: {nome} | Idade: {idade} anos | Cidade: {cidade}")

print("\n===== EXERCÍCIO 8 =====")
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

print(f"Soma: {a + b}")
print(f"Subtração: {a - b}")
print(f"Multiplicação: {a * b}")

if b != 0:
    print(f"Divisão: {a / b}")
    print(f"Divisão inteira: {a // b}")
    print(f"Resto: {a % b}")
else:
    print("Não é possível dividir por zero")

print("\n===== EXERCÍCIO 9 =====")
valor_hora = float(input("Digite o valor por hora: "))
horas = float(input("Digite a quantidade de horas trabalhadas: "))
salario = valor_hora * horas
desconto = salario * 0.11
salario_liquido = salario - desconto

print(f"Salário bruto: R$ {salario:.2f}")
print(f"Desconto INSS: R$ {desconto:.2f}")
print(f"Salário líquido: R$ {salario_liquido:.2f}")

print("\n===== EXERCÍCIO 10 =====")
reais = float(input("Digite o valor em reais: "))
cotacao = 5.10
dolares = reais / cotacao
print(f"R$ {reais:.2f} equivale a US$ {dolares:.2f}")
