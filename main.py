import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_MainWindow
from tarefas import TarefaManager


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.manager = TarefaManager()

        self.ui.btnAdicionar.clicked.connect(self.adicionar_tarefa)
        self.ui.btnRemover.clicked.connect(self.remover_tarefa)

    def adicionar_tarefa(self):
        texto = self.ui.inputTarefa.text().strip()
        if texto:
            self.manager.adicionar(texto)
            self.ui.listaTarefas.addItem(texto)
            self.ui.inputTarefa.clear()

    def remover_tarefa(self):
        item = self.ui.listaTarefas.currentItem()
        if item:
            self.manager.remover(item.text())
            self.ui.listaTarefas.takeItem(self.ui.listaTarefas.row(item))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MainApp()
    janela.show()
    sys.exit(app.exec_())
