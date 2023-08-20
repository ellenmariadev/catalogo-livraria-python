from utils import opcao_voltar
from utils import print_livro
from utils import arquivo
from utils import dados

# TODO: Lidar com os acentos no termo de busca.

def buscar_editora():
    while True:
        print(f'\n\033[100m 7 \033[m \033[97mVoltar\033[m\n')
        _editora = str(input("> Informe o nome da editora: ").lower())
        finder = False

        if (opcao_voltar(_editora)):
            break

        with open(arquivo, 'r', encoding="utf-8") as arquivos:
            for livro in arquivos:
                propriedade = livro.strip().split(",")
                livros = dados(propriedade)

                if livros["editora"].lower() == _editora:
                    finder = True
                    print_livro(livros, "buscar_editora")
            if not finder:
                print('\033[31mNão há nenhum livro dessa editora no catálogo.\033[m')
