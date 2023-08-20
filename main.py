from sistema.adicionar import cadastrar_livro
from sistema.buscar_titulo import buscar_titulo
from sistema.buscar_editora import buscar_editora
from sistema.editar import editar_livro
from sistema.remover import remover_livro
from sistema.listar import catalogo_livros


# Texto em negrito e centralizado
def titulo(txt):
    print('-=-' * 14)
    print(f'\033[1m{txt.center(42)}\033[m')
    print('-=-' * 14)


# Lista de opções do menu numerada e com cores
def menu(lista_opcoes):
    titulo("CATÁLOGO LIVRARIA")
    for index, item in enumerate(lista_opcoes, 1):
        if (index == 7):
            print(f'\n\033[101;1m {index} \033[m \033[31m{item}\033[m')
        else:
            print(f'\n\033[100m {index} \033[m \033[97m{item}\033[m')
    print('-=-' * 14)


while True:
    lista_opcoes = ['Cadastrar Livro', 'Buscar Livro por Título',
                    'Buscar Livros por Editora', 'Acessar Catálogo', 'Editar Livro', 'Remover Livro', 'Sair']
    menu(lista_opcoes)

    entrada = input("> Sua Opção: ")

    if entrada == "1":
        titulo("CADASTRAR")
        cadastrar_livro()
    elif entrada == "2":
        titulo("BUSCAR")
        buscar_titulo()
    elif entrada == "3":
        titulo("BUSCAR")
        buscar_editora()
    elif entrada == "4":
        titulo("CATÁLOGO")
        catalogo_livros()
    elif entrada == "5":
        titulo("EDITAR")
        editar_livro()
    elif entrada == "6":
        titulo("REMOVER")
        remover_livro()
    elif entrada == "7":
        print("Saindo do sistema...")
        break
    else:
        print('\033[31mDigite uma opção válida.\033[m')
