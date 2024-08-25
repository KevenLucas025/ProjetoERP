from PySide6.QtWidgets import (QDialog, QPushButton, QVBoxLayout, QMessageBox, QAbstractItemView)
from tabelaprodutos import TabelaProdutos
import sys

class AtualizarProduto(QDialog):
    def __init__(self, main_window, parent=None):
        super().__init__(parent)
        self.main_window = main_window
        self.setWindowTitle("Atualizar Produto")

        # Definir layout para a janela de diálogo
        layout = QVBoxLayout()
        
        # Botão para abrir a lista de produtos
        btn_mostrar_produtos = QPushButton("Mostrar Produtos")
        btn_mostrar_produtos.clicked.connect(self.atualizar_tabela_produtos)
        layout.addWidget(btn_mostrar_produtos)
        
        # Adicionar o layout à janela de diálogo
        self.setLayout(layout)

        self.resize(300, 100)

    def atualizar_tabela_produtos(self):
        dialog_tabela = TabelaProdutos(self.main_window, self.main_window.dateEdit)
        dialog_tabela.preencher_tabela_produtos()
        dialog_tabela.exec()

        self.close()

       
