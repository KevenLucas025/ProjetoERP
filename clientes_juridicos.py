from PySide6.QtWidgets import QLineEdit, QToolButton,QTableWidgetItem
from PySide6.QtGui import QPixmap, QIcon,QColor,QBrush
from PySide6.QtCore import Qt
from database import DataBase
import sqlite3
import pandas as pd

class Clientes:
    def __init__(self, line_clientes: QLineEdit,main_window):
        self.line_clientes = line_clientes
        self.imagem_line()
        self.db = DataBase("banco_de_dados.db")
        self.main_window = main_window
        self.table_clientes_juridicos = self.main_window.table_clientes_juridicos  # Referência para a tabela no main window











    # Função auxiliar para criar um QTableWidgetItem com texto centralizado
    def formatar_texto_juridico(self, text):
        item = QTableWidgetItem(text)
        item.setTextAlignment(Qt.AlignCenter)  # Centraliza o texto
        item.setForeground(QBrush(QColor("white"))) 
        return item


    def carregar_dados_clientes_juridicos(self):
        cn = sqlite3.connect("banco_de_dados.db")

        query = """
        SELECT "Nome do Cliente", "Data da Inclusão", CNPJ, Telefone, CEP, Endereço, Número,
            Cidade, Bairro, "Status do Cliente", "Categoria do Cliente", "Última Atualização",
            "Origem do Cliente", "Valor Gasto Total", "Última Compra"
        FROM table_clientes_juridicos
        """

        df = pd.read_sql_query(query, cn)

        if df.empty:
            print("Nenhum dado encontrado no banco de dados 'clientes_juridicos'")
            return

        # Limpar tabela antes de preencher
        self.table_clientes_juridicos.clearContents()
        self.table_clientes_juridicos.setRowCount(0)
        self.table_clientes_juridicos.setColumnCount(len(df.columns))

        # Preencher a tabela
        for row_index, row_data in df.iterrows():
            self.table_clientes_juridicos.insertRow(row_index)
            for col_index, data in enumerate(row_data):
                item = self.formatar_texto_juridico(str(data))
                self.table_clientes_juridicos.setItem(row_index, col_index, item)


    def imagem_line(self):
        # Criar botão da lupa
        self.botao_lupa = QToolButton(self.line_clientes)
        self.botao_lupa.setCursor(Qt.PointingHandCursor)  # Muda o cursor ao passar o mouse
        self.botao_lupa.setIcon(QIcon(QPixmap("imagens/pngegg.png")))  # Substitua pelo caminho correto
        self.botao_lupa.setStyleSheet("border: none; background: transparent;")  # Sem fundo e sem borda
        
        # Definir tamanho do botão
        altura = self.line_clientes.height() - 4  # Ajustar altura conforme a LineEdit
        self.botao_lupa.setFixedSize(altura, altura)

        # Posicionar o botão no canto direito da LineEdit
        self.botao_lupa.move(self.line_clientes.width() - altura - 2, 2)

        # Ajustar padding para o texto não sobrepor o botão
        self.line_clientes.setStyleSheet(
            "QLineEdit {"
            "    color: black;"
            "    background-color: rgb(240, 240, 240);"
            "    border: 2px solid rgb(50, 150, 250);"
            "    border-radius: 6px;"
            "    padding: 3px;"  # Padding normal
            f"    padding-right: {altura + 5}px;"  # Ajuste para o botão
            "}"
            "QLineEdit::placeholderText {"
            "    color: black;"
            "}"
        )

        # Conectar clique do botão a uma função
        self.botao_lupa.clicked.connect(self.buscar)

    def buscar(self):
        texto = self.line_clientes.text()
        print(f"Pesquisando por: {texto}")  # Aqui você pode implementar a lógica de pesquisa
