from utils import opcao_voltar


def editar_livro(arquivo, dados):
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
                titulo = input("Altere o título do livro: ")
                if (opcao_voltar(titulo)):
                    return

                while True:
                    isbn = input("Altere o ISBN do livro: ")
                    if opcao_voltar(isbn):
                        return
                    if len(isbn) == 13 and isbn.isdigit():
                        break
                    else:
                        print(
                            '\033[31mO ISBN deve ter exatamente 13 dígitos e conter apenas números.\033[m')

                autor = input("Altere o autor do livro: ")
                if (opcao_voltar(autor)):
                    return
                editora = input("Altere a editora do livro: ")
                if (opcao_voltar(editora)):
                    return

                while True:
                    try:
                        _paginas = int(
                            input("Altere o número de páginas totais do livro: "))
                        if (opcao_voltar(_paginas)):
                            return
                        paginas = _paginas
                        break
                    except ValueError:
                        print('\033[31mDigite apenas números.\033[m')

                idioma = input("Altere o idioma do livro: ")
                if (opcao_voltar(idioma)):
                    break

                while True:
                    try:
                        _classificacao = int(
                            input("Altere a classificação etária do livro: "))
                        if (opcao_voltar(str(_classificacao))):
                            return
                        classificacao = _classificacao
                        break
                    except ValueError:
                        print('\033[31mDigite apenas números.\033[m')

                while True:
                    try:
                        _anopublicacao = int(
                            input("Altere o ano de publicação do livro: "))
                        if (opcao_voltar(str(_anopublicacao))):
                            return
                        anopublicacao = _anopublicacao
                        break
                    except ValueError:
                        print('\033[31mDigite apenas números.\033[m')

                livros["isbn"] = isbn
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
            print(
                "\033[31mEsse livro não existe no catálogo, verifique se o ISBN está correto.\033[m")
