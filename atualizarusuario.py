from PySide6.QtWidgets import (
    QApplication, QDialog, QPushButton,
    QVBoxLayout, QTableWidget, QTableWidgetItem, QMessageBox, QCheckBox
)
import re
from database import DataBase
import sys 
from tabelausuario import TabelaUsuario

class AtualizarUsuario(QDialog):
    def __init__(self, main_window, parent=None):
        super().__init__(parent)
        self.main_window = main_window
        self.setWindowTitle("Atualizar Usuário")

        # Definir layout para a janela de diálogo
        layout = QVBoxLayout()
        
        # Botão para abrir a lista de produtos
        self.btn_mostrar_usuarios = QPushButton("Mostrar Usuário")
        self.btn_mostrar_usuarios.clicked.connect(self.atualizar_tabela_usuarios)
        layout.addWidget(self.btn_mostrar_usuarios)
        
        # Adicionar o layout à janela de diálogo
        self.setLayout(layout)

        self.resize(300, 100)

    def atualizar_tabela_usuarios(self):
        # Preencher a tabela de usuários com os dados do banco de dados
        dialog_tabela = TabelaUsuario(self.main_window)
        dialog_tabela.preencher_tabela_usuario()
        dialog_tabela.exec()

        self.close()
    
    def listar_usuarios(self):
        self.btn_mostrar_usuarios.setVisible(True)

    
    