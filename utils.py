def opcao_voltar(entrada):
    if entrada == "7" or entrada == "sair":
        return True
    return False


def print_livro(livro, func):

    if (func == "buscar_editora"):
        print(f'''
  ▸ ISBN: {livro["isbn"]}
    \033[93m{livro["titulo"].upper()}\033[m
    Autor: {livro["autor"]}
    \033[35mEditora: {livro["editora"]}\033[m
    Nº de Páginas: {livro["paginas"]}
    Classificação Etária: {livro["classificacao"]}
    Ano de Publicação: {livro["anopublicacao"]}
        ''')

    elif (func == "remover_livro"):
        print(f'''\033[31m
    Id: {livro["id"]}

    ISBN: {livro["isbn"]}
    \033[93m{livro["titulo"].upper()}\033[m
    Autor: {livro["autor"]}
    Editora: {livro["editora"]}
    Nº de Páginas: {livro["paginas"]}
    Classificação Etária: {livro["classificacao"]}
    Ano de Publicação: {livro["anopublicacao"]}
        \033''')

    else:
        print(f'''
  ▸ ISBN: {livro["isbn"]}
    \033[93m{livro["titulo"].upper()}\033[m
    Autor: {livro["autor"]}
    Editora: {livro["editora"]}
    Nº de Páginas: {livro["paginas"]}
    Classificação Etária: {livro["classificacao"]}
    Ano de Publicação: {livro["anopublicacao"]}
        ''')
