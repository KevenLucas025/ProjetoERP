from PySide6.QtWidgets import (QLineEdit, QToolButton,QTableWidgetItem,
                               QMessageBox,QMainWindow,QVBoxLayout,QWidget,QLabel,QCheckBox,QPushButton,QScrollArea,QComboBox)
from PySide6.QtGui import QPixmap, QIcon,QColor,QBrush,QGuiApplication
from PySide6.QtCore import Qt
from database import DataBase
import sqlite3
import pandas as pd
from configuracoes import Configuracoes_Login
import datetime

class Clientes:
    def __init__(self, line_clientes: QLineEdit,main_window,btn_adicionar_cliente_juridico,
                 btn_editar_clientes,btn_excluir_clientes,btn_visualizar_clientes,btn_enviaremail_clientes,
                 btn_gerar_relatorio_clientes,btn_marcar_como_clientes,btn_historico_clientes):
        self.line_clientes = line_clientes
        self.imagem_line()
        self.db = DataBase("banco_de_dados.db")
        self.config = Configuracoes_Login(self)
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
        self.btn_adicionar_cliente_juridico.clicked.connect(self.exibir_janela_cadastro_cliente)



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

    def exibir_janela_cadastro_cliente(self):
        self.janela_cadastro = QMainWindow()
        self.janela_cadastro.resize(700, 550)
        self.janela_cadastro.setWindowTitle("Cadastro do Cliente")
        self.janela_cadastro.setStyleSheet("""
            background-color: rgb(0, 80, 121);
        """)
 
        # Centralizar a janela
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_geometry = self.janela_cadastro.frameGeometry()
        window_geometry.moveCenter(screen_geometry.center())
        self.janela_cadastro.move(window_geometry.topLeft())
 
        # Conteúdo do formulário
        conteudo = QWidget()
        layout = QVBoxLayout(conteudo)
        conteudo.setStyleSheet("""
            QLineEdit {
                color: black;
                background-color: rgb(240, 240, 240);
                border: 2px solid rgb(50, 150, 250);
                border-radius: 6px;
                padding: 3px;
            }
            QLineEdit::placeholderText {
                color: black;
            }
        """)

        # Função genérica para adicionar campos
        def add_linha(titulo,widget=None):
            layout.addWidget(QLabel(titulo))
            if widget is None:
                layout.addWidget(QLineEdit())
            else:
                layout.addWidget(widget)
 
        add_linha("Nome do Cliente:")
        add_linha("CNPJ:")
        add_linha("Telefone:")
        add_linha("CEP:")
        add_linha("Endereço:")
        add_linha("Número:")
        add_linha("Cidade:")
        add_linha("Bairro:")
        add_linha("Nacionalidade:")
        add_linha("Categoria do Cliente:")
        

        combobox_status_cliente = QComboBox()
        combobox_status_cliente.setStyleSheet("""
                QComboBox { 
                    background-color: white; 
                    border: 3px solid rgb(50,150,250); 
                    border-radius: 5px; 
                    color: black; 
                    padding: 5px;
                }
                QComboBox QAbstractItemView {
                    background-color: white; 
                    color: black; 
                    border: 1px solid #ccc; 
                    selection-background-color: #e5e5e5; 
                    selection-color: black;
                }
                QComboBox QAbstractItemView QScrollBar:vertical {
                    background: #f5f5f5; 
                    width: 12px; 
                    border: none;
                }
                QComboBox QAbstractItemView QScrollBar::handle:vertical {
                    background: #cccccc; 
                    min-height: 20px; 
                    border-radius: 5px;
                }
                QComboBox QAbstractItemView QScrollBar::add-line:vertical, 
                QComboBox QAbstractItemView QScrollBar::sub-line:vertical {
                    background: none;
                    height: 0px;  /* Remove os botões de linha (setas de cima e baixo) */
                }
                QComboBox QAbstractItemView QScrollBar::add-page:vertical, 
                QComboBox QAbstractItemView QScrollBar::sub-page:vertical {
                    background: none;
                }


            """)
        add_linha("Status do Cliente:",combobox_status_cliente)    

        btn_fazer_cadastro = QPushButton("Fazer o Cadastro")
        btn_fazer_cadastro.clicked.connect(self.cadastrar_clientes_juridicos)
        btn_fazer_cadastro.setStyleSheet("""
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
        """)
        layout.addWidget(btn_fazer_cadastro)
 
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(conteudo)
 
        self.janela_cadastro.setCentralWidget(scroll_area)
        self.janela_cadastro.show()


    def cadastrar_clientes_juridicos(self):
        try:
            with self.db.connecta() as conexao:
                cursor = conexao.cursor()
                usuario_logado = self.config.obter_usuario_logado()

                # Coletar dados dos campos
                get = lambda campo: self.campos_cliente_juridico[campo].text().strip() if isinstance(self.campos_cliente_juridico[campo], QLineEdit) else self.campos_cliente_juridico[campo].currentText()

                nome = get("Nome do Cliente:")
                cnpj = get("CNPJ:")
                telefone = get("Telefone:")
                cep = get("CEP:")
                endereco = get("Endereço:")
                numero = get("Número:")
                cidade = get("Cidade:")
                bairro = get("Bairro:")
                nacionalidade = get("Nacionalidade:")
                categoria = get("Categoria do Cliente:")
                status = get("Status do Cliente:")

                # Você pode adicionar lógica para validar campos aqui
                if not nome or not cnpj:
                    QMessageBox.warning(self, "Atenção", "Nome e CNPJ são obrigatórios.")
                    return
                # Inserir no banco
                cursor.execute("""
                    INSERT INTO clientes_juridicos(
                        "Nome do Cliente", CNPJ,Telefone,CEP,Endereço,Número,Cidade,Bairro,"Status do Cliente","Categoria do Cliente"
                        "Origem do Cliente"
                )VALUES(?,?,?,?,?,?,?,?,?,?,?)
                """,(nome,cnpj,telefone,cep,endereco,numero,cidade,bairro,nacionalidade,categoria,status))

                conexao.commit()

                QMessageBox.information(self, "Sucesso", "Cliente cadastrado com sucesso!")
            self.janela_cadastro.close()

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao cadastrar cliente: \n{e}")