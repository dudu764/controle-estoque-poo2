from Produto import Produto
from ProdutoAlimenticio import ProdutoAlimenticio

produtos = []

def cadastrar_produto():
    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade: "))
    produto = Produto(nome, preco, quantidade)
    produtos.append(produto)

def cadastrar_alimenticio():
    nome = input("Nome do alimento: ")
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade: "))
    validade = input("Data de validade (dd/mm/aaaa): ")
    produto = ProdutoAlimenticio(nome, preco, quantidade, validade)
    produtos.append(produto)

def exibir_todos_produtos():
    print("\n--- Produtos Cadastrados ---")
    for p in produtos:
        p.exibir_produtos()

def menu():
    while True:
        print("\n1 - Cadastrar Produto Comum")
        print("2 - Cadastrar Produto Alimentício")
        print("3 - Exibir Produtos")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            cadastrar_alimenticio()
        elif opcao == "3":
            exibir_todos_produtos()
        elif opcao == "4":
            break
        else:
            print("Opção inválida!")

menu()
