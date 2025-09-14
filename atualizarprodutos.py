from PySide6.QtWidgets import (QDialog, QPushButton, QVBoxLayout, QMessageBox, QAbstractItemView)
from tabelaprodutos import TabelaProdutos
from PySide6.QtCore import Qt
import sys

class AtualizarProduto(QDialog):
    def __init__(self, main_window, parent=None):
        super().__init__(parent)
        self.main_window = main_window
        self.setWindowTitle("Edição de Produtos")

        # Definir layout para a janela de diálogo
        layout = QVBoxLayout()

        # Carregar config
        config = self.main_window.carregar_config_arquivo()
        tema = config.get("tema", "claro")

         # Definir estilo do botão baseado no tema
        if tema == "escuro":
            button_style = """
                QPushButton {
                    border-radius: 8px;
                    background: qlineargradient(
                        x1:0, y1:0, x2:0, y2:1,
                        stop:0 rgb(60, 60, 60),   /* topo */
                        stop:1 rgb(100, 100, 100) /* base */
                    );
                    color: white;
                    padding: 6px;
                }
                QPushButton:hover {
                    background-color: #444444;
                }
                QPushButton:pressed {
                    background-color: #555555;
                    border: 2px solid #888888;
                }
            """
        else:  # claro
            button_style = """
                QPushButton {
                    color: rgb(255, 255, 255);
                    border-radius: 8px;
                    font-size: 16px;
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */
                    border: 4px solid transparent;
                }

                QPushButton:hover {
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */
                    color: black;
                }
            """
        
        # Botão para abrir a lista de produtos
        self.btn_mostrar_produtos = QPushButton("Exibir Tabela de Produtos")
        self.btn_mostrar_produtos.setCursor(Qt.PointingHandCursor)
        self.btn_mostrar_produtos.setStyleSheet(button_style)
        self.btn_mostrar_produtos.clicked.connect(self.atualizar_tabela_produtos)
        layout.addWidget(self.btn_mostrar_produtos)
        
        # Adicionar o layout à janela de diálogo
        self.setLayout(layout)

        self.resize(300, 100)

    def atualizar_tabela_produtos(self):
        self.dialog_tabela = TabelaProdutos(self.main_window, self.main_window.dateEdit_3)
        self.dialog_tabela.preencher_tabela_produtos()
        self.dialog_tabela.show()

        self.close()

    def listar_produtos(self):
        self.btn_mostrar_produtos.setVisible(True)

       
