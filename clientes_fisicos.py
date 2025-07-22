from PySide6.QtWidgets import (QLineEdit, QToolButton,QTableWidgetItem,
                               QMessageBox,QMainWindow,QVBoxLayout,QWidget,QLabel,QCheckBox,
                               QPushButton,QScrollArea,QComboBox,QGridLayout,QHeaderView,QHBoxLayout,
                               QGraphicsOpacityEffect,QTableWidget,QInputDialog,QDialog,
                               QRadioButton,QGroupBox,QFileDialog,QFormLayout,QDateEdit)
from PySide6.QtGui import QPixmap, QIcon,QColor,QBrush,QGuiApplication
from PySide6.QtCore import Qt,QTimer,QPropertyAnimation,QEvent,QDate
from database import DataBase
import sqlite3
import pandas as pd
from configuracoes import Configuracoes_Login
from datetime import datetime
from PySide6.QtGui import QKeySequence, QShortcut
import csv
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import letter,landscape,A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Alignment
from fpdf import FPDF


class Clientes_Fisicos(QWidget):
    def __init__(self,line_clientes_fisicos: QLineEdit,main_window,btn_adicionar_cliente_fisico,btn_editar_clientes_fisicos,
                 btn_excluir_clientes_fisicos,btn_gerar_relatorio_clientes_fisicos,
                 btn_historico_clientes_fisicos,btn_marcar_como_clientes_fisicos):
        super().__init__()
        self.line_clientes_fisicos = line_clientes_fisicos
        self.db = DataBase("banco_de_dados.db")
        self.config = Configuracoes_Login(self)
        self.coluna_checkboxes_clientes_fisicos_adicionada = False
        self.checkboxes_clientes_fisicos = []

        self.main_window = main_window
        self.table_clientes_fisicos = self.main_window.table_clientes_fisicos # Referência para a tabela no main window
        self.btn_adicionar_cliente_fisico = btn_adicionar_cliente_fisico
        self.btn_editar_clientes_fisicos = btn_editar_clientes_fisicos
        self.btn_excluir_clientes_fisicos = btn_excluir_clientes_fisicos
        self.btn_gerar_relatorio_clientes_fisicos = btn_gerar_relatorio_clientes_fisicos
        self.btn_historico_clientes_fisicos = btn_historico_clientes_fisicos
        self.btn_marcar_como_clientes_fisicos = btn_marcar_como_clientes_fisicos


        self.btn_excluir_clientes_fisicos.clicked.connect(self.excluir_clientes_fisicos)
        '''self.btn_marcar_como_clientes_fisicos.clicked.connect(self.marcar_como_clientes_fisicos)
        self.btn_adicionar_cliente_fisico.clicked.connect(self.exibir_janela_cadastro_cliente_fisicos)
        self.btn_editar_clientes_fisicos.clicked.connect(self.editar_cliente_fisicos)
        self.btn_historico_clientes_fisicos.clicked.connect(self.historico_clientes_fisicos)
        self.btn_gerar_relatorio_clientes_fisicos.clicked.connect(self.abrir_janela_relatorio_clientes_fisicos)'''













    # Função auxiliar para criar um QTableWidgetItem com texto centralizado
    def formatar_texto_fisico(self, text):
        item = QTableWidgetItem(text)
        item.setTextAlignment(Qt.AlignCenter)  # Centraliza o texto
        item.setForeground(QBrush(QColor("white")))
        return item
    
    def carregar_clientes_fisicos(self):
        try:
            with self.db.connecta() as conexao:
                cursor = conexao.cursor()

                cursor.execute("""
                    SELECT 
                        "Nome do Cliente",
                        "Data da Inclusão",
                        CPF, 
                        Telefone, 
                        CEP, 
                        Endereço, 
                        Número,
                        Complemento,
                        Cidade, 
                        Bairro,
                        Estado,
                        "Status do Cliente", 
                        "Categoria do Cliente",
                        "Última Atualização",
                        "Origem do Cliente",
                        "Valor Gasto Total",
                        "Última Compra"
                    FROM clientes_fisicos
                    ORDER BY "Data da Inclusão" DESC
                """)

                dados = cursor.fetchall()

                # Limpa a tabela antes de recarregar
                self.table_clientes_fisicos.clearContents()
                self.table_clientes_fisicos.setRowCount(0)

                deslocamento = 1 if self.coluna_checkboxes_clientes_adicionada else 0
                self.checkboxes_clientes = []

                for linha_idx, linha_dados in enumerate(dados):
                    self.table_clientes_fisicos.insertRow(linha_idx)

                    # Adiciona checkbox se estiver ativado
                    if self.coluna_checkboxes_clientes_adicionada:
                        checkbox = QCheckBox()
                        checkbox.setStyleSheet("margin-left: 9px; margin-right: 9px;")
                        self.table_clientes_fisicos.setCellWidget(linha_idx, 0, checkbox)
                        self.checkboxes_clientes.append(checkbox)

                    # Preenche os dados nas colunas (com deslocamento)
                    for coluna_idx, dado in enumerate(linha_dados):
                        item = self.formatar_texto_juridico(str(dado))
                        self.table_clientes_fisicos.setItem(linha_idx, coluna_idx + deslocamento, item)

                self.table_clientes_fisicos.resizeColumnsToContents()
                self.table_clientes_fisicos.resizeRowsToContents()

        except Exception as e:
            QMessageBox.critical(self.main_window, "Erro", f"Erro ao carregar clientes:\n{e}")

    def imagem_line_fisico(self):
        # Criar botão da lupa
        self.botao_lupa = QToolButton(self.line_clientes_fisicos)
        self.botao_lupa.setCursor(Qt.PointingHandCursor)  # Muda o cursor ao passar o mouse
        self.botao_lupa.setIcon(QIcon(QPixmap("imagens/botão_lupa.png")))  # Substitua pelo caminho correto
        self.botao_lupa.setStyleSheet("border: none; background: transparent;")  # Sem fundo e sem borda
        
        # Definir tamanho do botão
        altura = self.line_clientes_fisicos.height() - 4  # Ajustar altura conforme a LineEdit
        self.botao_lupa.setFixedSize(altura, altura)

        # Posicionar o botão no canto direito da LineEdit
        self.botao_lupa.move(self.line_clientes_fisicos.width() - altura + 1, 2)

        # Ajustar padding para o texto não sobrepor o botão
        self.line_clientes_fisicos.setStyleSheet(
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

    def buscar_cliente_fisico(self):
        texto = self.line_clientes.text().strip()

        if not texto:
            QMessageBox.warning(self, "Aviso", "Digite algo para buscar.")
            return

        # Conectar ao banco de dados
        with sqlite3.connect('banco_de_dados.db') as conn:
            cursor = conn.cursor()

            try:
                # Buscar em múltiplas colunas
                cursor.execute("""
                    SELECT  
                        "Nome do Cliente",
                        "Data da Inclusão",
                        CPF,
                        Telefone,
                        CEP,
                        Endereço,
                        Número,
                        Complemento,
                        Cidade,
                        Bairro,
                        Estado,
                        "Status do Cliente",
                        "Categoria do Cliente",
                        "Última Atualização",
                        "Origem do Cliente",
                        "Valor Gasto Total",
                        "Última Compra"
                    FROM clientes_juridicos
                    WHERE 
                        LOWER("Nome do Cliente") LIKE LOWER(?) OR
                        LOWER(CPF) LIKE LOWER(?) OR
                        LOWER(Telefone) LIKE LOWER(?)
                """, (f'%{texto}%', f'%{texto}%', f'%{texto}%', f'%{texto}%'))

                resultados = cursor.fetchall()

                if not resultados:
                    QMessageBox.information(self, "Resultado", "Nenhum cliente encontrado.")
                    return

                # Atualizar sua tabela ou interface com os resultados
                self.preencher_resultado_busca_fisica(resultados)
                

            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Erro ao buscar cliente: {e}")

    def preencher_resultado_busca_fisica(self, resultados):
        self.table_clientes_fisicos.setRowCount(0)

        for row_data in resultados:
            row_index = self.table_clientes_fisicos.rowCount()
            self.table_clientes_fisicos.insertRow(row_index)
            for col_index, data in enumerate(row_data):
                item = self.formatar_texto_juridico(str(data))
                self.table_clientes_fisicos.setItem(row_index, col_index, item)

    def formatar_e_buscar_cep_fisico(self, widget):
        texto_cep = widget.text()
        self.main_window.formatar_cep(texto_cep, widget)

        dados = self.main_window.buscar_cep(texto_cep)
        if dados:
            self.campos_cliente["Endereço"].setText(dados.get("logradouro", ""))
            self.campos_cliente["Complemento"].setText(dados.get("complemento", ""))
            self.campos_cliente["Bairro"].setText(dados.get("bairro", ""))
            self.campos_cliente["Cidade"].setText(dados.get("localidade", ""))
            
            estado = dados.get("uf", "")
            index_estado = self.campos_cliente["Estado"].findText(estado)
            if index_estado >= 0:
                self.campos_cliente["Estado"].setCurrentIndex(index_estado)

    def exibir_edicao_clientes_fisicos(self, dados_cliente: dict):
        self.dados_originais_cliente_fisico = dados_cliente.copy()
        self.alteracoes_realizadas = False
        self.janela_editar_cliente_fisico = QMainWindow()
        self.janela_editar_cliente_fisico.setWindowTitle("Editar Cliente")
        self.janela_editar_cliente_fisico.resize(683, 600)
        self.janela_editar_cliente_fisico.setStyleSheet("background-color: rgb(0, 80, 121);")

        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_geometry = self.janela_editar_cliente_fisico.frameGeometry()
        window_geometry.moveCenter(screen_geometry.center())
        self.janela_editar_cliente_fisico.move(window_geometry.topLeft())

        central_widget = QWidget()
        layout = QGridLayout(central_widget)
        layout.setSpacing(10)
        layout.setContentsMargins(30, 30, 30, 30)
        
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(central_widget)
        scroll_area.setStyleSheet("""
            QScrollBar:vertical {
                background: white;
                width: 6px;
                margin: 2px 0;
                border: none;
            }

            QScrollBar::handle:vertical {
                background: gray;
                min-height: 20px;
                border-radius: 3px;
            }

            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical {
                height: 0;
            }

            QScrollBar::add-page:vertical,
            QScrollBar::sub-page:vertical {
                background: transparent;
            }
        """)


        colunas = [
            "Nome do Cliente", "Data da Inclusão","CPF","RG", "Telefone","CEP",
            "CEP", "Endereço", "Número", "Complemento", "Cidade", "Bairro",
            "Estado", "Status do Cliente", "Categoria do Cliente",
            "Última Atualização", "Origem do Cliente", "Valor Gasto Total", "Última Compra"
        ]

        self.campos_cliente = {}

        for i, campo in enumerate(colunas):
            label = QLabel(campo + ":")
            label.setStyleSheet("color: white; font-weight: bold;")
            label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

            if campo in ["Estado", "Status do Cliente"]:
                entrada = QComboBox()
                entrada.setStyleSheet("""
                    QComboBox {
                        background-color: white;
                        border: 2px solid rgb(50,150,250);
                        border-radius: 5px;
                        color: black;
                        padding: 5px;
                    }

                    QComboBox QAbstractItemView {
                        background-color: white;
                        color: black;
                        selection-background-color: rgb(220, 220, 220);
                        border: 1px solid lightgray;
                    }

                    QComboBox QScrollBar:vertical {
                        border: none;
                        background: transparent;
                        width: 6px;
                        margin: 2px 0 2px 0;
                    }

                    QComboBox QScrollBar::handle:vertical {
                        background: gray;
                        min-height: 20px;
                        border-radius: 3px;
                    }

                    QComboBox QScrollBar::add-line:vertical,
                    QComboBox QScrollBar::sub-line:vertical {
                        height: 0;
                    }

                    QComboBox QScrollBar::add-page:vertical,
                    QComboBox QScrollBar::sub-page:vertical {
                        background: white;
                    }
                """)

                if campo == "Estado":
                    entrada.addItems(["Selecione", "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA",
                                    "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO",
                                    "RR", "SC", "SP", "SE", "TO"])
                elif campo == "Status do Cliente":
                    entrada.addItems(["Selecione", "Ativo", "Inativo", "Pendente", "Bloqueado"])
                index = entrada.findText(dados_cliente[campo])
                entrada.setCurrentIndex(index if index >= 0 else 0)
            else:
                entrada = QLineEdit()
                entrada.setText(dados_cliente[campo])
            if isinstance(entrada,QComboBox):
                entrada.currentTextChanged.connect(self.marcar_alteracao)
            else:
                entrada.textChanged.connect(self.marcar_alteracao)
                entrada.setStyleSheet("""
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
            if campo == "CPF":
                entrada.textChanged.connect(lambda texto, w=entrada: self.main_window.formatar_cpf(texto,w))
            elif campo == "Telefone":
                entrada.textChanged.connect(lambda texto, w=entrada: self.main_window.formatar_telefone(texto, w))
            elif campo == "CEP":
                entrada.textChanged.connect(lambda texto, w=entrada: self.main_window.formatar_cep(texto,w))
                entrada.editingFinished.connect(lambda e=entrada: self.formatar_e_buscar_cep(e))
                

            layout.addWidget(label, i, 0)
            layout.addWidget(entrada, i, 1)
            self.campos_cliente[campo] = entrada

        # Botão atualizar
        botao_atualizar = QPushButton("Atualizar")
        botao_atualizar.setStyleSheet("""
            QPushButton {
                background-color: white;
                padding: 8px;
                font-weight: bold;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: lightgray;
            }
        """)
        botao_atualizar.clicked.connect(self.atualizar_dados_clientes)
        layout.addWidget(botao_atualizar, len(colunas), 0, 1, 2, alignment=Qt.AlignCenter)

        self.janela_editar_cliente_fisico.setCentralWidget(scroll_area)
        self.janela_editar_cliente_fisico.show()

    def editar_cliente_fisico(self):
        linha_selecionada = self.table_clientes_fisicos.currentRow()
        if linha_selecionada < 0:
            QMessageBox.warning(None, "Aviso", "Nenhum cliente selecionado para edição.")
            return
        
        coluna_offset = 1 if self.coluna_checkboxes_clientes_fisicos_adicionada else 0

        colunas = [
            "Nome do Cliente",  "Data da Inclusão","CPF", "RG", "Telefone",
            "CEP", "Endereço", "Número", "Complemento", "Cidade", "Bairro",
            "Estado", "Status do Cliente", "Categoria do Cliente",
            "Última Atualização", "Origem do Cliente", "Valor Gasto Total", "Última Compra"
        ]
        

        dados_cliente = {}
        for col, nome_coluna in enumerate(colunas):
            item = self.table_clientes_fisicos.item(linha_selecionada, col + coluna_offset)
            dados_cliente[nome_coluna] = item.text() if item else ""

        self.exibir_edicao_clientes_fisicos(dados_cliente)   

    def atualizar_dados_clientes_fisicos(self):
        if not self.alteracoes_realizadas:
            QMessageBox.information(None, "Sem alterações", "Nenhuma modificação foi feita.")
            return
        
        dados_atualizados = {}
        for campo, widget in self.campos_cliente.items():
            if isinstance(widget, QComboBox):
                dados_atualizados[campo] = widget.currentText()
            else:
                dados_atualizados[campo] = widget.text()


        try:
            cursor = self.db.connection.cursor()
            cnpj = dados_atualizados["CPF"]  # Supondo que o CNPJ seja identificador único

            query = """
            UPDATE clientes_juridicos
            SET
                `Nome do Cliente` = ?, `Data da Inclusão` = ?,CPF,RG, Telefone = ?,
                CEP = ?, Endereço = ?, Número = ?, Complemento = ?, Cidade = ?, Bairro = ?,
                Estado = ?, `Status do Cliente` = ?, `Categoria do Cliente` = ?, `Última Atualização` = ?,
                `Origem do Cliente` = ?, `Valor Gasto Total` = ?, `Última Compra` = ?
            WHERE CNPJ = ?
            """

            valores = (
                dados_atualizados["Nome do Cliente"],
                dados_atualizados["Data da Inclusão"],
                dados_atualizados["CPF"],
                dados_atualizados["RG"],
                dados_atualizados["Telefone"],
                dados_atualizados["CEP"],
                dados_atualizados["Endereço"],
                dados_atualizados["Número"],
                dados_atualizados["Complemento"],
                dados_atualizados["Cidade"],
                dados_atualizados["Bairro"],
                dados_atualizados["Estado"],
                dados_atualizados["Status do Cliente"],
                dados_atualizados["Categoria do Cliente"],
                dados_atualizados["Última Atualização"],
                dados_atualizados["Origem do Cliente"],
                dados_atualizados["Valor Gasto Total"],
                dados_atualizados["Última Compra"],
                cnpj
            )

            cursor.execute(query, valores)
            self.db.connection.commit()
            QMessageBox.information(None, "Sucesso", "Cliente atualizado com sucesso.")
            self.janela_editar_cliente_fisico.close()
            self.carregar_clientes_fisicos()  # Se quiser recarregar a tabela
        except Exception as e:
            QMessageBox.critical(None, "Erro", f"Erro ao atualizar cliente: {e}")

    def exibir_janela_cadastro_cliente_fisico(self):
        self.campos_cliente_fisico = {}
        self.informacoes_obrigatorias_clientes_fisicos()
        
        self.janela_cadastro_fisico = QMainWindow()
        self.janela_cadastro_fisico.resize(700, 550)
        self.janela_cadastro_fisico.setWindowTitle("Cadastro do Cliente")
        self.janela_cadastro_fisico.setStyleSheet("""
            background-color: rgb(0, 80, 121);
        """)

        # Centralizar a janela
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_geometry = self.janela_cadastro_fisico.frameGeometry()
        window_geometry.moveCenter(screen_geometry.center())
        self.janela_cadastro_fisico.move(window_geometry.topLeft())

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

        def add_linha(titulo, widget=None):
            layout.addWidget(QLabel(titulo))
            if widget is None:
                widget = QLineEdit()
            layout.addWidget(widget)
            chave_sem_ponto = titulo.rstrip(":")  # remove ':' do final
            self.campos_cliente_fisico[chave_sem_ponto] = widget


        add_linha("Nome do Cliente")
        add_linha("Data da Inclusão")
        add_linha("CPF")
        cpf_widget = self.campos_cliente_fisico["CPF"]
        cpf_widget.textChanged.connect(lambda text: self.main_window.formatar_cpf(text, cpf_widget))
        add_linha("RG")
        rg_widget = self.campos_cliente_fisico["RG"]
        rg_widget.textChanged.connect(lambda text: self.main_window.formatar_rg(text,rg_widget))
        add_linha("Telefone")
        telefone_widget = self.campos_cliente_fisico["Telefone"]
        telefone_widget.textChanged.connect(lambda text: self.main_window.formatar_telefone(text, telefone_widget))        
        add_linha("CEP")
        cep_widget = self.campos_cliente_fisico["CEP"]
        # Formatação do CEP enquanto digita
        cep_widget.textChanged.connect(lambda text: self.main_window.formatar_cep(text,cep_widget))
        # Buscar dados do CEP ao terminar de digitar
        cep_widget.editingFinished.connect(lambda: self.on_cep_editing_finished_cadastro(cep_widget))
        add_linha("Endereço")
        add_linha("Número")
        add_linha("Complemento")
        self.campos_cliente_fisico["Complemento"].setPlaceholderText("Opcional")
        add_linha("Cidade")
        add_linha("Bairro")

        # Aqui adiciona Estado logo após Bairro
        combobox_estado_cliente_fisico = QComboBox()
        combobox_estado_cliente_fisico.addItems([
            "Selecionar","AC","AL","AP","AM","BA","CE","DF","ES","GO","MA","MT",
            "MS","MG","PA","PB","PR","PE","PI","RJ","RN","RS","RO","RR","SC","SP","SE","TO"
        ])
        combobox_estado_cliente_fisico.setCurrentIndex(0) # Seleciona "Selecionar" por padrão
        combobox_estado_cliente_fisico.setStyleSheet("""
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
        add_linha("Estado", combobox_estado_cliente_fisico)
        add_linha("Nacionalidade")
        add_linha("Categoria do Cliente")

        combobox_status_cliente = QComboBox()
        combobox_status_cliente.addItems(["Selecionar","Ativo","Inativo","Pendente","Bloqueado"])
        combobox_status_cliente.setCurrentIndex(0) # Seleciona "Selecionar" por padrão
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
        add_linha("Status do Cliente:", combobox_status_cliente)    

        btn_fazer_cadastro_fisico = QPushButton("Fazer o Cadastro")
        btn_fazer_cadastro_fisico.clicked.connect(self.cadastrar_clientes_fisicos)
        btn_fazer_cadastro_fisico.setStyleSheet("""
            QPushButton {
                color: rgb(255, 255, 255);
                border-radius: 8px;
                font-size: 16px;
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255));
                border: 4px solid transparent;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255));
                color: black;
            }
        """)
        layout.addWidget(btn_fazer_cadastro_fisico)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(conteudo)
        scroll_area.setStyleSheet("""
            QScrollBar:vertical {
                background: white;
                width: 6px;
                margin: 2px 0;
                border: none;
            }

            QScrollBar::handle:vertical {
                background: gray;
                min-height: 20px;
                border-radius: 3px;
            }

            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical {
                height: 0;
            }

            QScrollBar::add-page:vertical,
            QScrollBar::sub-page:vertical {
                background: transparent;
            }
        """)

        self.janela_cadastro_fisico.setCentralWidget(scroll_area)
        self.janela_cadastro_fisico.show()

    def cadastrar_clientes_fisicos(self):
        try:
            with self.db.connecta() as conexao:
                cursor = conexao.cursor()
                usuario_logado = self.config.obter_usuario_logado()

                # Coletar dados dos campos
                get = lambda campo: self.campos_cliente_fisico[campo].text().strip() \
                    if isinstance(self.campos_cliente_fisico[campo], QLineEdit) \
                    else self.campos_cliente_fisico[campo].currentText()

                nome = get("Nome do Cliente")
                cpf = get("CPF")
                rg = get("RG")
                telefone = get("Telefone")
                cep = get("CEP")
                endereco = get("Endereço")
                numero = get("Número")
                complemento = get("Complemento")
                cidade = get("Cidade")
                bairro = get("Bairro")
                estado = get("Estado")
                nacionalidade = get("Nacionalidade")
                categoria = get("Categoria do Cliente")
                status = get("Status do Cliente")

                # Verificar se o cliente já existe
                cursor.execute("""
                    SELECT 1 FROM clientes_fisicos
                    WHERE CPF = ? OR RG = ?
                """, (cpf, rg))

                if cursor.fetchone():
                    QMessageBox.warning(None, "Cliente já existe", "Já existe um cliente com este CPF ou RG.")
                    return

                # Validação de todos os campos obrigatórios
                for campo, mensagem in self.campos_obrigatorios_clientes.items():
                    widget = self.campos_cliente_fisico[campo]
                    valor = widget.text().strip() if isinstance(widget, QLineEdit) else widget.currentText()
                    
                    if not valor or (isinstance(widget, QComboBox) and valor == "Selecionar"):
                        QMessageBox.warning(None, "Atenção", mensagem)
                        return
                    

                data_inclusao = datetime.now().strftime("%d/%m/%Y %H:%M")
                
                # Valores padrão para os campos não preenchidos manualmente
                valor_gasto_total = "Não Cadastrado"
                ultima_compra = "Não Cadastrado"
                ultima_atualizacao = "Não Cadastrado"
                
                # Inserir no banco
                cursor.execute("""
                    INSERT INTO clientes_juridicos(
                        "Nome do Cliente",  "Data da Inclusão", CPF,RG, Telefone, CEP, Endereço, Número,
                        Complemento, Cidade, Bairro, Estado, "Status do Cliente", "Categoria do Cliente","Última Atualização", 
                        "Origem do Cliente","Valor Gasto Total", "Última Compra"
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?,?,?)
                """, (
                    nome,data_inclusao, cpf, rg, telefone, cep, endereco, numero,complemento, cidade,
                    bairro,estado, status, categoria, ultima_atualizacao,nacionalidade, valor_gasto_total, ultima_compra,
                ))
                conexao.commit()

                self.main_window.registrar_historico_clientes_fisicos(
                    "Cadastro de Cliente", f"Cliente {nome} cadastrado com sucesso"
                )
                
                QMessageBox.information(None, "Sucesso", "Cliente cadastrado com sucesso!")
                # Redimensiona apenas uma vez após preencher
                self.table_clientes_fisicos.resizeColumnsToContents()
                self.table_clientes_fisicos.resizeRowsToContents()
                self.limpar_campos_clientes_fisicos()
                self.carregar_clientes_fisicos()       
        except Exception as e:
            QMessageBox.critical(None, "Erro", f"Erro ao cadastrar cliente: \n{e}")

    def informacoes_obrigatorias_clientes_fisicos(self):
        self.campos_obrigatorios_clientes_fisicos = {
            "Nome do Cliente": "O campo Nome do Cliente é obrigatório.",
            "CPF": "O campo CPF é obrigatório.",
            "RG": "O campo de RG é obrigatório",
            "Telefone": "O campo Telefone é obrigatório.",
            "CEP": "O campo CEP é obrigatório.",
            "Endereço": "O campo Endereço é obrigatório.",
            "Número": "O campo Número é obrigatório.",
            "Cidade": "O campo Cidade é obrigatório.",
            "Bairro": "O campo Bairro é obrigatório.",
            "Estado": "O campo de Estado é obrigatório",
            "Nacionalidade": "O campo Nacionalidade é obrigatório.",
            "Categoria do Cliente": "O campo Categoria do Cliente é obrigatório.",
            "Status do Cliente": "Você deve selecionar um status válido para o cliente.",
        }
    def limpar_campos_clientes_fisicos(self):
        for campo, widget in self.campos_cliente_fisico.items():
            if isinstance(widget,QLineEdit):
                widget.clear()
            elif isinstance(widget, QComboBox):
                widget.setCurrentIndex(0) # Volta para "Selecionar"

    def on_cep_editing_finished_cadastro(self, cep_widget):
        cep_digitado = cep_widget.text()
        dados_cep = self.main_window.buscar_cep(cep_digitado)
        if dados_cep:
            self.preencher_campos_cep_cadastro_fisico(dados_cep)

    def preencher_campos_cep_cadastro_fisico(self, dados):
        if dados is None:
            return

        # Preencher os campos do seu formulário usando self.campos_cliente_juridico
        self.campos_cliente_fisico["Endereço"].setText(dados.get("logradouro", ""))
        self.campos_cliente_fisico["Bairro"].setText(dados.get("bairro", ""))
        self.campos_cliente_fisico["Cidade"].setText(dados.get("localidade", ""))

        complemento = dados.get("complemento", "")
        if any(char.isdigit() for char in complemento):
            self.campos_cliente_fisico["Número"].setText(complemento)

        estado = dados.get("uf", "")
        # Se tiver um combobox para estado, aqui você ajusta o índice
        if "Estado" in self.campos_cliente_fisico:
            estado_combobox = self.campos_cliente_fisico["Estado"]
            index_estado = estado_combobox.findText(estado)
            if index_estado != -1:
                estado_combobox.setCurrentIndex(index_estado)
                
    def excluir_clientes_juridicos(self):
        try:
            total_linhas = self.table_clientes_fisicos.rowCount()
            if total_linhas == 0:
                QMessageBox.warning(self, "Aviso", "Nenhum cliente encontrado para excluir.")
                return

            clientes_para_excluir = []

            if self.coluna_checkboxes_clientes_fisicos_adicionada:
                # Modo com checkbox
                for linha in range(total_linhas):
                    checkbox_widget = self.table_clientes_fisicos.cellWidget(linha, 0)
                    if checkbox_widget:
                        checkbox = checkbox_widget.findChild(QCheckBox)
                        if checkbox and checkbox.isChecked():
                            nome_cliente = self.table_clientes_fisicos.item(linha, 1).text()
                            clientes_para_excluir.append((linha, nome_cliente))
            else:
                # Modo sem checkbox (seleção direta)
                linha_selecionadas = self.table_clientes_fisicos.selectionModel().selectedRows()
                if not linha_selecionadas:
                    QMessageBox.information(None, "Aviso", "Nenhum cliente selecionado para exclusão.")
                    return
                
                for index in linha_selecionadas:
                    linha = index.row()
                    nome_cliente = self.table_clientes_fisicos.item(linha,0).text()
                    clientes_para_excluir.append((linha,nome_cliente))

            if not clientes_para_excluir:
                QMessageBox.information(None, "Aviso", "Nenhum cliente selecionado para exclusão.")
                return
            
            # Mensagem personalizada
            if len(clientes_para_excluir) == 1:
                _, nome = clientes_para_excluir[0]
                mensagem = f"Tem certeza que deseja excluir o cliente:\n\n• {nome}?"
            else:
                nomes = "\n• " + "\n• ".join(nome for _, nome in clientes_para_excluir)
                mensagem = f"Tem certeza que deseja excluir os seguintes clientes?\n{nomes}"

            # Criar QMessageBox manualmente para alterar os textos dos botões
            msgbox = QMessageBox()
            msgbox.setIcon(QMessageBox.Question)
            msgbox.setWindowTitle("Confirmar Exclusão")
            msgbox.setText(mensagem)
            msgbox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

            # Renomear os botões
            botao_sim = msgbox.button(QMessageBox.Yes)
            botao_nao = msgbox.button(QMessageBox.No)
            botao_sim.setText("Sim")
            botao_nao.setText("Não")

            resposta = msgbox.exec()

            if resposta != QMessageBox.Yes:
                return
            
            # Executa exclusão no banco e remove as linhas da tabela
            db = DataBase()
            db.connecta()
            cursor = db.connection.cursor()

            for linha, nome_cliente in reversed(clientes_para_excluir):
                cursor.execute("""
                    DELETE FROM clientes_fisicos WHERE "Nome do Cliente" = ?
                """, (nome_cliente,))
                self.table_clientes_fisicos.removeRow(linha)

            db.connection.commit()
            
            nomes_excluidos = ", ".join(nome for _, nome in clientes_para_excluir)
            self.main_window.registrar_historico_clientes_fisicos(
                "Exclusão de Cliente(s)",
                f"Cliente(s) excluído(s): {nomes_excluidos}"
            )
            QMessageBox.information(self.main_window, "Sucesso", "Cliente(s) excluído(s) com sucesso.")
        except Exception as e:
            QMessageBox.critical(self.main_window, "Erro", f"Erro ao excluir clientes:\n{e}")