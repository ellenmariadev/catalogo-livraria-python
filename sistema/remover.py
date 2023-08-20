from utils import opcao_voltar
from utils import print_livro


def remover_livro(arquivo, dados):
    while True:
        print(f'\n\033[100m 7 \033[m \033[97mVoltar\033[m\n')
        _isbn = input("> Informe o ISBN do livro: ").lower()
        finder = False

        if opcao_voltar(_isbn):
            break

        with open(arquivo, 'r') as arquivos:
            arsenal = arquivos.readlines()

        with open(arquivo, 'w') as arquivos:
            for livro in arsenal:
                propriedade = livro.strip().split(",")
                livros = dados(propriedade)

                if livros["isbn"] == _isbn:
                    finder = True
                    print(f"\033[32mLivro ISBN-{_isbn} removido.\033[m")
                    print_livro(livros, "remover_livro")
                else:
                    arquivos.write(livro)
        if not finder:
            print(
                "\033[31mEsse livro não existe no catálogo, verifique se o ISBN está correto.\033[m")
