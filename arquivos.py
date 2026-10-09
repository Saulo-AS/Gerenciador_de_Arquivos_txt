import os

def deleta_arquivo():
    arquivos = os.listdir()
    nome = input("Nome do arquivo: ")
    nome += ".txt"

    for arq in arquivos:
        if arq == nome:
            os.remove(arq)


def cria_arquivo():
    nome = input("Nome do arquivo: ")
    nome += ".txt"

    with open(nome, "w") as arquivo:
        pass


def edita_arquivo():
    arquivos = os.listdir()
    nome_edtArquivo = input("Digite o nome do arquivo que deseja editar: ")
    nome_edtArquivo += ".txt"

    for arq in arquivos:
        if arq == nome_edtArquivo:
            with open(arq, "w") as arquivo:
                texto = input("Digite o novo conteúdo: ")
                arquivo.write(texto)