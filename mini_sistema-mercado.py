produtos = []

def adicionar_produto():
    nome = input("Nome: ")
    peso = float(input("Peso: "))
    estoque = int(input("Estoque: "))
    preco = float(input("Preço: "))

    produto = {"nome": nome, "peso": peso, "estoque": estoque, "preco": preco}
    produtos.append(produto)

    print(f"Produto {nome} adicionado com Sucesso!")

def mostrar_produtos():
    if not produtos:
        print("Não tem produtos cadastrados ainda.")
        return

    for produto in produtos:
        total = produto['estoque'] * produto['preco']
        print(f"\nNome: {produto['nome']}")
        print(f"Peso(un): {produto['peso']}")
        print(f"Estoque: {produto['estoque']}")
        print(f"Custo total em estoque: R$ {total:,.2f}")

def buscar_produto():
    nome = input("Digite o nome do produto: ")
    encontrado = False
    for produto in produtos:
        total = produto['estoque'] * produto['preco']
        if produto["nome"].lower() == nome.lower():
            print(f"\nProduto encontrado!")
            print(f"Nome: {produto['nome']}, Peso(un): {produto['peso']}, Estoque: {produto['estoque']}, Custo Total: R$ {total:,.2f}")
            encontrado = True
            break
    if not encontrado:
        print("Produto não encontrado")

def remover_produto():
    nome = input("Digite o nome do produto que deseja remover: ")
    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            produtos.remove(produto)
            print("Produto Removido com Sucesso!")
            return
    print("Produto não encontrado")

def main():
    while True:
        print("\n|============ MENU ============|")
        print("|[1] Adicionar Produto         |")
        print("|[2] Mostrar todos os Produtos |")
        print("|[3] Buscar Produto por nome   |")
        print("|[4] Remover Produto           |")
        print("|[5] Sair                      |")
        print("|==============================|")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            mostrar_produtos()
        elif opcao == "3":
            buscar_produto()
        elif opcao == "4":
            remover_produto()
        elif opcao == "5":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
