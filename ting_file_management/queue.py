from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.queue = list()

    def __len__(self) -> int:
        return len(self.queue)

    def enqueue(self, value) -> None:
        self.queue.append(value)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        raise IndexError("Fila vazia")

    def search(self, index: int):
        if 0 <= index <= len(self.queue) - 1:
            return self.queue[index]
        raise IndexError("Índice Inválido ou Inexistente")
