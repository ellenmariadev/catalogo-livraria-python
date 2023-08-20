from utils import opcao_voltar
from utils import arquivo
from utils import validar_input_int
from utils import validar_input_str


def cadastrar_livro():
    with open(arquivo, 'r', encoding="utf-8") as arquivos:
        # Retorna os livros no formato de uma lista de strings.
        catalogo = arquivos.readlines()

    print(f'\n\033[100m 7 \033[m \033[97mVoltar\033[m\n')

    while True:
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
   
    titulo = validar_input_str("◌ Insira o título do livro: ", opcao_voltar)
    autor = validar_input_str("◌ Insira o autor do livro: ", opcao_voltar)
    editora = validar_input_str("◌ Insira a editora do livro: ", opcao_voltar)
    idioma = validar_input_str("◌ Insira o idioma do livro: ", opcao_voltar)

    paginas = validar_input_int("◌ Insira o número de páginas totais do livro: ", opcao_voltar)
    classificacao = validar_input_int("◌ Insira a classificação etária do livro: ", opcao_voltar)
    anopublicacao = validar_input_int("◌ Insira o ano de publicação do livro: ", opcao_voltar)

    livro = (f"{len(catalogo)},{_isbn},{titulo},{autor},{editora},{paginas},{idioma},{classificacao},{anopublicacao}\n")

    catalogo.append(livro)

    with open(arquivo, 'w', encoding="utf-8") as arquivos:
        arquivos.writelines(catalogo)

    print(f"\n\033[32mLivro [{titulo}] cadastrado.\033[m\n")