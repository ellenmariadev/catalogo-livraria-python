from utils import opcao_voltar


def cadastrar_livro(arquivo):
    with open(arquivo, 'r', encoding="utf-8") as arquivos:
        catalogo = arquivos.readlines() # Retorna os livros no formato de uma lista de strings.

    while True:
        print(f'\n\033[100m 7 \033[m \033[97mVoltar\033[m\n')
        titulo = input("◌ Insira o título do livro: ")
        if opcao_voltar(titulo):
            return
        _isbn = input("◌ Insira o ISBN do livro: ")
        if opcao_voltar(_isbn):
            return
        if len(_isbn) == 13 and _isbn.isdigit():
            # Retorna True se houver um mesmo ISBN em alguma linha da lista de livros.
            if any(linha.split(',')[1] == _isbn for linha in catalogo): 
                print('\033[31mEsse livro já está cadastrado no sistema.\033[m')
            else:
                break
        else:
            print('\033[31mO ISBN deve ter exatamente 13 dígitos e conter apenas números.\033[m')

    autor = input("◌ Insira o autor do livro: ")
    if opcao_voltar(autor):
        return
    editora = input("◌ Insira a editora do livro: ")
    if opcao_voltar(editora):
        return

    while True:
        try:
            _paginas = int(input("◌ Insira o número de páginas totais do livro: "))
            if opcao_voltar(str(_paginas)):
                return
            paginas = _paginas
            break
        except ValueError:
            print('\033[31mDigite apenas números.\033[m')

    idioma = input("◌ Insira o idioma do livro: ")
    if opcao_voltar(idioma):
        return

    while True:
        try:
            _classificacao = int(input("◌ Insira a classificação etária do livro: "))
            if opcao_voltar(str(_classificacao)):
                return
            classificacao = _classificacao
            break
        except ValueError:
            print('\033[31mDigite apenas números.\033[m')

    while True:
        try:
            _anopublicacao = int(input("◌ Insira o ano de publicação do livro: "))
            if opcao_voltar(str(_anopublicacao)):
                return
            anopublicacao = _anopublicacao
            break
        except ValueError:
            print('\033[31mDigite apenas números.\033[m')

    livro = (f"{len(catalogo)},{isbn},{titulo},{autor},{editora},{paginas},{idioma},{classificacao},{anopublicacao}\n")

    catalogo.append(livro)

    with open(arquivo, 'w', encoding="utf-8") as arquivos:
        arquivos.writelines(catalogo)

    print(f"\n\033[32mLivro [{titulo}] cadastrado.\033[m\n")

