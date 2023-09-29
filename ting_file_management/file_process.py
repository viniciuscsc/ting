from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


def process(path_file: str, instance: Queue):
    for arquivo in instance.queue:
        if arquivo["nome_do_arquivo"] == path_file:
            return None

    linhas_arquivo = txt_importer(path_file)
    arquivo_processado = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(linhas_arquivo),
        "linhas_do_arquivo": linhas_arquivo,
    }
    instance.enqueue(arquivo_processado)
    print(arquivo_processado)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
