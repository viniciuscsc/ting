from ting_file_management.queue import Queue


def exists_word(word: str, instance: Queue):
    palavras = []
    arquivos = instance.queue

    for arquivo in arquivos:
        ocorrencias = []

        for indice, texto_linha in enumerate(arquivo["linhas_do_arquivo"]):
            if word.lower() in texto_linha.lower():
                ocorrencias.append({"linha": indice + 1})

        if len(ocorrencias) > 0:
            palavras.append(
                {
                    "palavra": word,
                    "arquivo": arquivo["nome_do_arquivo"],
                    "ocorrencias": ocorrencias,
                }
            )

    return palavras


def search_by_word(word, instance):
    """Aqui irá sua implementação"""


# arquivo_processado = {
#         "nome_do_arquivo": path_file,
#         "qtd_linhas": len(linhas_arquivo),
#         "linhas_do_arquivo": linhas_arquivo,
#     }
