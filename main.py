import os
from arquivos import cria_arquivo, deleta_arquivo
from menus import mini_menu_edtArquivo

while True:
    print("\n===== GERENCIADOR DE ARQUIVOS =====")
    print("Obs: Todos os arquivos são .txt")
    print()
    print("1 - Criar arquivo")
    print("2 - Editar arquivo")
    print("3 - Excluir arquivo")
    print("4 - Mostrar arquivos")
    print("5 - Sair")

    opcao = input(": ")

    if opcao == "1":
        cria_arquivo()

    elif opcao == "2":
        mini_menu_edtArquivo()

    elif opcao == "3":
        deleta_arquivo()

    elif opcao == "4":
        arquivos = os.listdir()

        for arquivo in arquivos:
            if arquivo.endswith(".txt"):
                print(f"\n{arquivo} - {os.path.getsize(arquivo)} bytes")

    elif opcao == "5":
        break