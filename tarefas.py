class TarefaManager:
    def __init__(self):
        self.tarefas = []

    def adicionar(self, texto):
        self.tarefas.append(texto)

    def remover(self, texto):
        if texto in self.tarefas:
            self.tarefas.remove(texto)

    def listar(self):
        return self.tarefas
