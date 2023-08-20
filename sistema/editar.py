from utils import opcao_voltar
from utils import arquivo
from utils import dados
from utils import validar_input_int
from utils import validar_input_str


def editar_livro():
    with open(arquivo, 'r', encoding="utf-8") as file:
        livros_lista = file.readlines()

    while True:
        print(f'\n\033[100m 7 \033[m \033[97mVoltar\033[m\n')
        _isbn = input("> Informe o ISBN do livro: ").lower()

        if (opcao_voltar(_isbn)):
            return

        finder = False

        for i, livro in enumerate(livros_lista):
            propriedade = livro.strip().split(",")
            livros = dados(propriedade)

            if livros["isbn"] == _isbn:
                finder = True

                titulo = validar_input_str("◌ Altere o título do livro: ", opcao_voltar)
                autor = validar_input_str("◌ Altere o autor do livro: ", opcao_voltar)
                editora = validar_input_str("◌ Altere a editora do livro: ", opcao_voltar)
                idioma = validar_input_str("◌ Altere o idioma do livro: ", opcao_voltar)
    
                paginas = validar_input_int("◌ Altere o número de páginas totais do livro: ", opcao_voltar)
                classificacao = validar_input_int("◌ Altere a classificação etária do livro: ", opcao_voltar)
                anopublicacao = validar_input_int("◌ Altere o ano de publicação do livro: ", opcao_voltar)
    
                livros["isbn"] = _isbn
                livros["titulo"] = titulo
                livros["autor"] = autor
                livros["editora"] = editora
                livros["paginas"] = paginas
                livros["idioma"] = idioma
                livros["classificacao"] = classificacao
                livros["anopublicacao"] = anopublicacao

                livros_lista[i] = (
                    f"{livros['id']},{livros['isbn']},{livros['titulo']},{livros['autor']},{livros['editora']},{livros['paginas']},{livros['idioma']},{livros['classificacao']},{livros['anopublicacao']}\n")

                with open(arquivo, "w", encoding="utf-8") as arquivos:
                    arquivos.writelines(livros_lista)

                print(f"\n\033[32mLivro [{titulo}] atualizado.\033[m\n")
                
                break

        if not finder:
            print("\033[31mEsse livro não existe no catálogo, verifique se o ISBN está correto.\033[m")
