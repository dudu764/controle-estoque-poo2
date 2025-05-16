class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def exibir_detalhes(self):
        print(f"Produto: {self.nome}")
        print(f"Preço: R${self.preco:.2f}")
        print(f"Quantidade em estoque: {self.quantidade}")

    def repor_estoque(self, quantidade_adicional):
        if quantidade_adicional > 0:
            self.quantidade += quantidade_adicional
            print(f"{quantidade_adicional} unidades de '{self.nome}' adicionadas ao estoque.")
        else:
            print("Quantidade inválida para reposição.")

    def vender_produto(self, quantidade_venda):
        if quantidade_venda <= 0:
            print("Quantidade inválida para venda.")
        elif quantidade_venda > self.quantidade:
            print(f"Estoque insuficiente. Apenas {self.quantidade} unidades disponíveis.")
        else:
            self.quantidade -= quantidade_venda
            print(f"{quantidade_venda} unidades de '{self.nome}' vendidas com sucesso.")
