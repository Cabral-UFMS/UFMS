from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("Gerenciador de Tarefas")
        MainWindow.resize(400, 300)

        self.centralwidget = QWidget(MainWindow)
        self.layout = QVBoxLayout(self.centralwidget)

        self.inputTarefa = QLineEdit()
        self.inputTarefa.setPlaceholderText("Digite uma nova tarefa")

        self.btnAdicionar = QPushButton("Adicionar Tarefa")
        self.btnRemover = QPushButton("Remover Tarefa Selecionada")
        self.listaTarefas = QListWidget()

        self.layout.addWidget(self.inputTarefa)
        self.layout.addWidget(self.btnAdicionar)
        self.layout.addWidget(self.btnRemover)
        self.layout.addWidget(self.listaTarefas)

        MainWindow.setCentralWidget(self.centralwidget)
