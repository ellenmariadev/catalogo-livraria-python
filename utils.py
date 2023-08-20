arquivo = "catalogo.csv"

# Recebe os dados em formato de lista []
# Retorna os dados no formato de um dicionário {"chave": "valor"}
def dados(propriedade):
    livro = {
        "id": propriedade[0],
        "isbn": propriedade[1],
        "titulo": propriedade[2],
        "autor": propriedade[3],
        "editora": propriedade[4],
        "paginas": propriedade[5],
        "idioma": propriedade[6],
        "classificacao": propriedade[7],
        "anopublicacao": propriedade[8],
    }
    return livro


def opcao_voltar(entrada):
    if entrada == "7" or entrada == "sair":
        return True

# VALIDAR INPUTS
def validar_input_int(prompt, opcao_voltar):
    while True:
        try:
            valor = int(input(prompt))
            if opcao_voltar(str(valor)):
                return
            return valor
        except ValueError:
            print('\033[31mDigite apenas números.\033[m')

def validar_input_str(prompt, opcao_voltar):
    while True:
        valor = input(prompt)
        if opcao_voltar(valor):
            return
        if not valor:
            print('\033[31mO campo não pode ficar vazio.\033[m')
        else:
            return valor


def print_livro(livro, func):

    if (func == "buscar_editora"):
        print(f'''
  ▸ ISBN: {livro["isbn"]}
    \033[93m{livro["titulo"].upper()}\033[m
    Autor: {livro["autor"]}
    \033[35mEditora: {livro["editora"]}\033[m
    Nº de Páginas: {livro["paginas"]}
    Classificação Etária: +{livro["classificacao"]} anos
    Ano de Publicação: {livro["anopublicacao"]}
        ''')

    elif (func == "remover_livro"):
        print(f'''
    \033[31mId: {livro["id"]}
    ISBN: {livro["isbn"]}
    {livro["titulo"].upper()}
    Autor: {livro["autor"]}
    Editora: {livro["editora"]}
    Nº de Páginas: {livro["paginas"]}
    Classificação Etária: {livro["classificacao"]}
    Ano de Publicação: {livro["anopublicacao"]}\033[m
    ''')

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
