import sys


def txt_importer(path_file: str):
    try:
        with open(path_file, "r") as arquivo_noticias:
            if not path_file.endswith(".txt"):
                print("Formato inválido", file=sys.stderr)
                return []

            linhas_arquivo = arquivo_noticias.read().split("\n")
            return linhas_arquivo

    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return []
