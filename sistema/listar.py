from utils import print_livro


def catalogo_livros(arquivo, dados):
    with open(arquivo, 'r', encoding="utf-8") as arquivos:
        next(arquivos)  # Ignora a primeira linha com o nome das propriedades.
        lista = []
        for livro in arquivos:
            propriedade = livro.strip().split(",")
            lista.append(propriedade)
            livros = dados(propriedade)

            print_livro(livros, "listar_estoque")
        print(f"\033[32mA livraria possui [{len(lista)}] livros no catálogo.\033[m")