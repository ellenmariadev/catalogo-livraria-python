from utils import opcao_voltar
from utils import print_livro

# TODO: Lidar com os acentos no termo de busca.


def buscar_titulo(arquivo, dados):
    while True:
        print(f'\n\033[100m 7 \033[m \033[97mVoltar\033[m\n')
        _titulo = str(input("> Digite o título do livro: ").lower())
        finder = False

        if opcao_voltar(_titulo):
            break

        with open(arquivo, 'r', encoding="utf-8") as arquivos:
            # Armazena os livros que contém o termo de busca.
            livros_lista = []

            for livro in arquivos:
                propriedade = livro.strip().split(",")
                livros = dados(propriedade)

                if _titulo in livros["titulo"].lower():
                    livros_lista.append(livros)
                    finder = True

            if finder:
                for livro in livros_lista:
                    print_livro(livro, "buscar_titulo")
            else:
                print(
                    "\033[31mNão existe nenhum livro com esse título no catálogo.\033[m\n")
