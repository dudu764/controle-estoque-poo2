from produto import ProdutoAlimenticio

produto = ProdutoAlimenticio("Leite", 4.99, 20, "20/06/2025")

while True:
    print("\n=== MENU ===")
    print("1 - Exibir detalhes do produto")
    print("2 - Repor estoque")
    print("3 - Vender produto")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        produto.exibir_detalhes()

    elif opcao == "2":
        try:
            qtd = int(input("Digite a quantidade a adicionar ao estoque: "))
            produto.repor_estoque(qtd)
        except ValueError:
            print("Digite um número válido.")

    elif opcao == "3":
        try:
            qtd = int(input("Digite a quantidade a vender: "))
            produto.vender_produto(qtd)
        except ValueError:
            print("Digite um número válido.")

    elif opcao == "4":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")
