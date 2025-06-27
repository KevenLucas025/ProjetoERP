from PySide6.QtWidgets import QLineEdit, QToolButton,QTableWidgetItem,QMessageBox,QMainWindow,QVBoxLayout,QWidget,QLabel
from PySide6.QtGui import QPixmap, QIcon,QColor,QBrush,QGuiApplication
from PySide6.QtCore import Qt
from database import DataBase
import sqlite3
import pandas as pd

class Clientes:
    def __init__(self, line_clientes: QLineEdit,main_window,btn_adicionar_cliente_juridico,
                 btn_editar_clientes,btn_excluir_clientes,btn_visualizar_clientes,btn_enviaremail_clientes,
                 btn_gerar_relatorio_clientes,btn_marcar_como_clientes,btn_historico_clientes):
        self.line_clientes = line_clientes
        self.imagem_line()
        self.db = DataBase("banco_de_dados.db")
        self.main_window = main_window
        self.table_clientes_juridicos = self.main_window.table_clientes_juridicos  # Referência para a tabela no main window
        self.btn_adicionar_cliente_juridico = btn_adicionar_cliente_juridico
        self.btn_editar_clientes = btn_editar_clientes
        self.btn_excluir_clientes = btn_excluir_clientes
        self.btn_visualizar_clientes = btn_visualizar_clientes
        self.btn_enviaremail_clientes = btn_enviaremail_clientes
        self.btn_gerar_relatorio_clientes = btn_gerar_relatorio_clientes
        self.btn_marcar_como_clientes = btn_marcar_como_clientes
        self.btn_historico_clientes = btn_historico_clientes

        self.btn_adicionar_cliente_juridico.clicked.connect(self.cadastrar_cliente_juridico)



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
        FROM clientes_juridicos
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
        self.botao_lupa.move(self.line_clientes.width() - altura + 45, 2)

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
        QMessageBox.information(
            None,
            "Aviso",
            "Essa função ainda não está disponível"
        )

    def cadastrar_cliente_juridico(self):
        self.janela_cadastro = QMainWindow()
        self.janela_cadastro.resize(800,650)
        self.janela_cadastro.setWindowTitle("Cadastro do Cliente")
        self.janela_cadastro.setStyleSheet("""
                background-color: rgb(0, 80, 121);
            """)

        # Exibe a janela no centro da tela
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_geometry = self.janela_cadastro.frameGeometry()
        window_geometry.moveCenter(screen_geometry.center())
        self.janela_cadastro.move(window_geometry.topLeft())

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        central_widget.setStyleSheet("""
            QLineEdit {
                color: black;
                background-color: rgb(240, 240, 240);
                border: 2px solid rgb(50, 150,250);
                border-radius: 6px;
                padding: 3px;
            }
            QLineEdit::placeholderText {
                color: black;
            }
        """)

        label_nome = QLabel("Nome do Cliente: ")
        txt_nome = QLineEdit()
        label_cnpj = QLabel("CNPJ: ")
        txt_cnpj = QLineEdit()
        label_telefone = QLabel("Telefone: ")
        txt_telefone = QLineEdit()
        label_cep = QLabel("CEP: ")
        txt_cep  = QLineEdit()
        label_endereco = QLabel("Endereço: ")
        txt_endereco = QLineEdit()
        label_numero = QLabel("Número: ")
        txt_numero = QLineEdit()
        label_cidade = QLabel("Cidade: ")
        txt_cidade = QLineEdit()
        label_bairro = QLabel("Bairro: ")
        txt_bairro = QLineEdit()
        label_nacionalidade = QLabel("Nacionalidade: ")
        txt_nacionalidade = QLineEdit()
        label_status_cliente = QLabel("Status do Cliente: ")
        txt_status_cliente = QLineEdit()
        label_categoria = QLabel("Categoria do Cliente: ")
        txt_categoria = QLineEdit()

        # Adiciona os widgets ao layout
        layout.addWidget(label_nome)
        layout.addWidget(txt_nome)
        layout.addWidget(label_cnpj)
        layout.addWidget(txt_cnpj)
        layout.addWidget(label_telefone)
        layout.addWidget(txt_telefone)
        layout.addWidget(label_cep)
        layout.addWidget(txt_cep)
        layout.addWidget(label_endereco)
        layout.addWidget(txt_endereco)
        layout.addWidget(label_numero)
        layout.addWidget(txt_numero)
        layout.addWidget(label_cidade)
        layout.addWidget(txt_cidade)
        layout.addWidget(label_bairro)
        layout.addWidget(txt_bairro)
        layout.addWidget(label_nacionalidade)
        layout.addWidget(txt_nacionalidade)
        layout.addWidget(label_status_cliente)
        layout.addWidget(txt_status_cliente)
        layout.addWidget(label_categoria)
        layout.addWidget(txt_categoria)
        
        

        self.janela_cadastro.setCentralWidget(central_widget)
        self.janela_cadastro.show()


