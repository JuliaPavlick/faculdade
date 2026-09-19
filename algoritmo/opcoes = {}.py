opcoes = {}

def cadastrar_opcao():
    nome = input("Digite o nome da nova opção: ").strip()
    if nome in opcoes:
        print("Essa opção já existe.")
    else:
        opcoes[nome] = 0
        print(f"Opção '{nome}' cadastrada com sucesso.")

def listar_opcoes():
    if not opcoes:
        print("Nenhuma opção cadastrada.")
        return
    print("\nOpções cadastradas:")
    for nome in opcoes:
        print(f"- {nome}")

def registrar_voto():
    if not opcoes:
        print("Nenhuma opção cadastrada para votar.")
        return
    listar_opcoes()
    escolha = input("Digite o nome da opção em que deseja votar: ").strip()
    if escolha in opcoes:
        opcoes[escolha] += 1
        print("Voto registrado com sucesso.")
    else:
        print("Opção inválida.")

def consultar_quantidade_votos():
    if not opcoes:
        print("Nenhuma opção cadastrada.")
        return
    print("\nQuantidade de votos por opção:")
    for nome, votos in opcoes.items():
        print(f"- {nome}: {votos} voto(s)")

def mostrar_resultado():
    if not opcoes:
        print("Nenhuma opção cadastrada.")
        return
    total_votos = sum(opcoes.values())
    print("\nResultado da enquete:")
    if total_votos == 0:
        for nome in opcoes:
            print(f"- {nome}: 0 voto(s) (0.00%)")
    else:
        for nome, votos in opcoes.items():
            percentual = (votos / total_votos) * 100
            print(f"- {nome}: {votos} voto(s) ({percentual:.2f}%)")

def mostrar_opcao_vencedora():
    if not opcoes:
        print("Nenhuma opção cadastrada.")
        return
    total_votos = sum(opcoes.values())
    if total_votos == 0:
        print("Ainda não há votos registrados.")
        return
    maior_votos = max(opcoes.values())
    vencedoras = [nome for nome, votos in opcoes.items() if votos == maior_votos]
    if len(vencedoras) == 1:
        print(f"\nOpção vencedora: {vencedoras[0]} com {maior_votos} voto(s).")
    else:
        print(f"\nEmpate entre as opções: {', '.join(vencedoras)}, cada uma com {maior_votos} voto(s).")

def exibir_menu():
    print("\n===== MENU =====")
    print("1. Cadastrar opção")
    print("2. Listar opções")
    print("3. Registrar voto")
    print("4. Consultar quantidade de votos")
    print("5. Mostrar resultado")
    print("6. Mostrar opção vencedora")
    print("7. Encerrar")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_opcao()
        elif opcao == "2":
            listar_opcoes()
        elif opcao == "3":
            registrar_voto()
        elif opcao == "4":
            consultar_quantidade_votos()
        elif opcao == "5":
            mostrar_resultado()
        elif opcao == "6":
            mostrar_opcao_vencedora()
        elif opcao == "7":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()