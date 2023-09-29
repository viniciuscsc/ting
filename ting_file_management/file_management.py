def txt_importer(path_file):
    try:
        with open(path_file, "r") as arquivo_noticias:
            linhas_arquivo = arquivo_noticias.read().split("\n")
            return linhas_arquivo

    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado")
        return []
