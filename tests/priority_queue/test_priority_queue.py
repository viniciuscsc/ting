from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    arquivo_regular = {
        "nome_do_arquivo": "arquivo_regular.txt",
        "qtd_linhas": 6,
        "linhas_do_arquivo": ["L1", "L2", "L3", "L4", "L5", "L6"],
    }

    arquivo_prioritario = {
        "nome_do_arquivo": "arquivo_prioritario.txt",
        "qtd_linhas": 4,
        "linhas_do_arquivo": ["L1", "L2", "L3", "L4"],
    }

    fila_prioridade = PriorityQueue()

    # listas regular_priority e high_priority estão vazias
    assert len(fila_prioridade.regular_priority) == 0
    assert len(fila_prioridade.high_priority) == 0

    # arquivo_regular é inserido em regular_priority
    fila_prioridade.enqueue(arquivo_regular)
    assert len(fila_prioridade.regular_priority) == 1

    # arquivo_prioritario é inserido em high_priority
    fila_prioridade.enqueue(arquivo_prioritario)
    assert len(fila_prioridade.high_priority) == 1

    # primeiro arquivo removido é o arquivo_prioritario
    fila_prioridade.dequeue()
    assert len(fila_prioridade.high_priority) == 0
    assert len(fila_prioridade.regular_priority) == 1

    # se nao ha arquivo_prioritario, remove o arquivo_regular
    fila_prioridade.dequeue()
    assert len(fila_prioridade.high_priority) == 0
    assert len(fila_prioridade.regular_priority) == 0
