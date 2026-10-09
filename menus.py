import os
from arquivos import edita_arquivo, cria_arquivo
def mini_menu_edtArquivo():
    arquivos = os.listdir()

    for arquivo in arquivos:
        if arquivo.endswith(".txt"):
            print(f"\n{arquivo}")

    print("\n1 - Editar arquivos existentes")
    print("2 - Criar novo arquivo")
    print("3 - Sair")

    opcao_mini_menu = input(":")

    if opcao_mini_menu == "1":
        edita_arquivo()
    elif opcao_mini_menu == "2":
        cria_arquivo()
    elif opcao_mini_menu == "3":
        return