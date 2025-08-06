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


class Clientes_Juridicos(QWidget):
    def __init__(self, line_clientes: QLineEdit,main_window,btn_adicionar_cliente_juridico,
                 btn_editar_clientes,btn_excluir_clientes,btn_gerar_relatorio_clientes,btn_marcar_como_clientes,
                 btn_historico_clientes):
        super().__init__()
        self.line_clientes = line_clientes
        self.db = DataBase("banco_de_dados.db")
        self.config = Configuracoes_Login(self)
        self.coluna_checkboxes_clientes_adicionada = False
        self.checkboxes_clientes = []
        
        self.timer_buscar = QTimer()
        self.timer_buscar.setSingleShot(True)
        self.timer_buscar.timeout.connect(self._executar_busca_dinamica_juridicos)
        self.line_clientes.textChanged.connect(self._iniciar_timer_busca_juridicos)
        
        
        self.main_window = main_window
        self.table_clientes_juridicos = self.main_window.table_clientes_juridicos  # Referência para a tabela no main window
        self.btn_adicionar_cliente_juridico = btn_adicionar_cliente_juridico
        self.btn_editar_clientes = btn_editar_clientes
        self.btn_excluir_clientes = btn_excluir_clientes
        self.btn_gerar_relatorio_clientes = btn_gerar_relatorio_clientes
        self.btn_marcar_como_clientes = btn_marcar_como_clientes
        self.btn_historico_clientes = btn_historico_clientes
        
        
        
        self.btn_excluir_clientes.clicked.connect(self.excluir_clientes_juridicos)
        self.btn_marcar_como_clientes.clicked.connect(self.marcar_como_clientes)
        self.btn_adicionar_cliente_juridico.clicked.connect(self.exibir_janela_cadastro_cliente)
        self.btn_editar_clientes.clicked.connect(self.editar_cliente_juridico)
        self.btn_historico_clientes.clicked.connect(self.historico_clientes_juridicos)
        self.btn_gerar_relatorio_clientes.clicked.connect(self.abrir_janela_relatorio_clientes_juridicos)
        
        self.line_clientes.returnPressed.connect(self.buscar_dinamico)
        self.line_clientes.textChanged.connect(self.buscar_dinamico)

        self.imagem_line()
        #self.configurar_line_clientes()


        
        self.installEventFilter(self)
        self.table_clientes_juridicos.viewport().installEventFilter(self)

    def _iniciar_timer_busca_juridicos(self, texto):
        self.ultimo_texto = texto
        self.timer_buscar.start(300)  # espera 300ms após digitar

    def _executar_busca_dinamica_juridicos(self):
        self.buscar_dinamico(self.ultimo_texto)

    # Função auxiliar para criar um QTableWidgetItem com texto centralizado
    def formatar_texto_juridico(self, text):
        item = QTableWidgetItem(text)
        item.setTextAlignment(Qt.AlignCenter)  # Centraliza o texto
        item.setForeground(QBrush(QColor("white")))
        return item
                
    def carregar_clientes_juridicos(self):
        try:
            with self.db.connecta() as conexao:
                cursor = conexao.cursor()

                cursor.execute("""
                    SELECT 
                        "Nome do Cliente",
                        "Razão Social",
                        "Data da Inclusão",
                        CNPJ,
                        RG,
                        CPF,
                        CNH,
                        "Categoria da CNH",
                        "Data de Nascimento",
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
                    ORDER BY "Data da Inclusão" DESC
                """)

                dados = cursor.fetchall()

                # Limpa a tabela antes de recarregar
                self.table_clientes_juridicos.clearContents()
                self.table_clientes_juridicos.setRowCount(0)

                deslocamento = 1 if self.coluna_checkboxes_clientes_adicionada else 0
                self.checkboxes_clientes = []

                for linha_idx, linha_dados in enumerate(dados):
                    self.table_clientes_juridicos.insertRow(linha_idx)

                    # Adiciona checkbox se estiver ativado
                    if self.coluna_checkboxes_clientes_adicionada:
                        checkbox = QCheckBox()
                        checkbox.setStyleSheet("margin-left: 9px; margin-right: 9px;")
                        self.table_clientes_juridicos.setCellWidget(linha_idx, 0, checkbox)
                        self.checkboxes_clientes.append(checkbox)

                    # Preenche os dados nas colunas (com deslocamento)
                    for coluna_idx, dado in enumerate(linha_dados):
                        item = self.formatar_texto_juridico(str(dado))
                        self.table_clientes_juridicos.setItem(linha_idx, coluna_idx + deslocamento, item)

                self.table_clientes_juridicos.resizeColumnsToContents()
                self.table_clientes_juridicos.resizeRowsToContents()

        except Exception as e:
            QMessageBox.critical(self.main_window, "Erro", f"Erro ao carregar clientes:\n{e}")

    def imagem_line(self):
        # Criar botão da lupa
        self.botao_lupa = QToolButton(self.line_clientes)
        self.botao_lupa.setCursor(Qt.PointingHandCursor)  # Muda o cursor ao passar o mouse
        self.botao_lupa.setIcon(QIcon(QPixmap("imagens/botão_lupa.png")))  # Substitua pelo caminho correto
        self.botao_lupa.setStyleSheet("border: none; background: transparent;")  # Sem fundo e sem borda
        
        # Definir tamanho do botão
        altura = self.line_clientes.height() - 4  # Ajustar altura conforme a LineEdit
        self.botao_lupa.setFixedSize(altura, altura)

        # Posicionar o botão no canto direito da LineEdit
        self.botao_lupa.move(self.line_clientes.width() - altura + 1, 2)

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
        self.botao_lupa.clicked.connect(self.buscar_dinamico)

    def buscar_dinamico(self, texto):
        texto = texto.strip()

        # Se quiser, não faz nada quando texto vazio
        if not texto:
            # limpar tabela ou mostrar todos, ou nada.
            # Exemplo: mostrar todos (chame a função carregar todos, se tiver)
            self.carregar_clientes_juridicos()  # ou limpar a tabela
            return

        # Conectar ao banco de dados
        with sqlite3.connect('banco_de_dados.db') as conn:
            cursor = conn.cursor()

            try:
                cursor.execute("""
                    SELECT  
                        "Nome do Cliente",
                        "Razão Social",
                        "Data da Inclusão",
                        CNPJ,
                        RG,
                        "Data de Emissão do RG",
                        "Órgão Emissor",
                        CPF,
                        "Título de Eleito",
                        "Data de Emissão do Título",
                        "Estado Civil",
                        CNH,
                        "Categoria da CNH",
                        "Data de Emissão da CNH",
                        "Data de Vencimento da CNH",
                        "Data de Nascimento",
                        "Nome do Representante Legal",
                        "CPF do Representante Legal",
                        "RG do Representante Legal",
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
                        LOWER("Razão Social") LIKE LOWER(?) OR
                        LOWER(CNPJ) LIKE LOWER(?) OR
                        LOWER(Telefone) LIKE LOWER(?)
                """, (f'%{texto}%', f'%{texto}%', f'%{texto}%', f'%{texto}%'))

                resultados = cursor.fetchall()

                # Atualizar tabela com resultados
                self.preencher_resultado_busca(resultados)

            except Exception as e:
                # Só loga erro, não mostra mensagem durante digitação
                print(f"Erro na busca dinâmica: {e}")


    def preencher_resultado_busca(self, resultados):
        self.table_clientes_juridicos.setRowCount(0)

        for row_data in resultados:
            row_index = self.table_clientes_juridicos.rowCount()
            self.table_clientes_juridicos.insertRow(row_index)
            for col_index, data in enumerate(row_data):
                item = self.formatar_texto_juridico(str(data))
                self.table_clientes_juridicos.setItem(row_index, col_index, item)

    def formatar_e_buscar_cep(self, widget):
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
                
    def exibir_edicao_clientes(self, dados_cliente: dict):
        self.dados_originais_cliente = dados_cliente.copy()
        self.alteracoes_realizadas = False
        self.janela_editar_cliente = QMainWindow()
        self.janela_editar_cliente.setWindowTitle("Editar Cliente")
        self.janela_editar_cliente.resize(683, 600)
        self.janela_editar_cliente.setStyleSheet("background-color: rgb(0, 80, 121);")

        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_geometry = self.janela_editar_cliente.frameGeometry()
        window_geometry.moveCenter(screen_geometry.center())
        self.janela_editar_cliente.move(window_geometry.topLeft())

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
            "Nome do Cliente", "Razão Social", "Data da Inclusão", "CNPJ","RG","Data de Emissão do RG","Órgão Emissor",
            "CPF","Título de Eleitor","Data de Emissão do Título","Estado Civil","CNH","Categoria da CNH","Data de Emissão da CNH",
            "Data de Vencimento da CNH","Nome do Representante Legal","CPF do Representante Legal","RG do Representante Legal",
            "Data de Nascimento", "Telefone","CEP", "Endereço", "Número", "Complemento", "Cidade", "Bairro","Estado", 
            "Status do Cliente","Categoria do Cliente","Última Atualização", "Origem do Cliente", "Valor Gasto Total", "Última Compra"
        ]

        self.campos_cliente = {}

        for i, campo in enumerate(colunas):
            label = QLabel(campo + ":")
            label.setStyleSheet("color: white; font-weight: bold;")
            label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

            if campo in ["Estado", "Status do Cliente","Categoria da CNH","Órgão Emissor","Estado Civil"]:
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
                elif campo == "Categoria da CNH":
                    entrada.addItems(["Selecione","AB","A","B","C","D","E","Nenhuma"])
                elif campo == "Estado Civil":
                    entrada.addItems(["Selecione", "Casado", "Solteiro", "Divorciado", "Viúvo", "União Estável"])
                elif campo == "Órgão Emissor":
                    entrada.addItems([
                        "Selecione", "SSP-AC", "SSP-AL", "SSP-AM", "SSP-AP", "SSP-BA", "SSP-DS", "SSP-DF",
                        "SSP-ES", "SSP-GO", "SSP-MA", "SSP-MG", "SSP-MS", "SSP-MT", "SSP-PA", "SSP-PB",
                        "SDS-PE", "SSP-PI", "SSP-PR", "SSP-RJ", "ITEP-RN", "SSP-RO", "SSP-RR", "SSP-RS",
                        "SSP-SC", "SSP-SE", "SSP-SP", "SSP-TO"
                    ])
                index = entrada.findText(dados_cliente.get(campo, "Selecione"))
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
            if campo == "CNPJ":
                entrada.textChanged.connect(lambda texto, w=entrada: self.main_window.formatar_cnpj(texto,w))
            elif campo == "RG":
                entrada.textChanged.connect(lambda texto, w=entrada: self.main_window.formatar_rg(texto, w))
                self.main_window.formatar_rg(dados_cliente[campo],entrada)
            elif campo == "CPF":
                entrada.textChanged.connect(lambda texto, w=entrada: self.main_window.formatar_cpf(texto,w))
            elif campo == "CNH":
                entrada.textChanged.connect(lambda texto, w=entrada: self.main_window.formatar_cnh(texto,w))
            elif campo == "Data de Nascimento":
                entrada.textChanged.connect(lambda texto, w=entrada: self.main_window.formatar_data_nascimento(texto,w))
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

        self.janela_editar_cliente.setCentralWidget(scroll_area)
        self.janela_editar_cliente.show()  
    
                
    def editar_cliente_juridico(self):
        linha_selecionada = self.table_clientes_juridicos.currentRow()
        if linha_selecionada < 0:
            QMessageBox.warning(None, "Aviso", "Nenhum cliente selecionado para edição.")
            return
        
        coluna_offset = 1 if self.coluna_checkboxes_clientes_adicionada else 0

        colunas = [
            "Nome do Cliente", "Razão Social", "Data da Inclusão", "CNPJ","RG","Data de Emissão do RG","Órgão Emissor",
            "CPF","Título de Eleitor","Data de Emissão do Título","Estado Civil","CNH","Categoria da CNH","Data de Emissão da CNH",
            "Data de Vencimento da CNH","Nome do Representante Legal","CPF do Representante Legal","RG do Representante Legal",
            "Data de Nascimento", "Telefone","CEP", "Endereço", "Número", "Complemento", "Cidade", "Bairro","Estado", 
            "Status do Cliente","Categoria do Cliente","Última Atualização", "Origem do Cliente", "Valor Gasto Total", "Última Compra"
        ]
        

        dados_cliente = {}
        for col, nome_coluna in enumerate(colunas):
            item = self.table_clientes_juridicos.item(linha_selecionada, col + coluna_offset)
            dados_cliente[nome_coluna] = item.text() if item else ""

        self.exibir_edicao_clientes(dados_cliente)   

    def atualizar_dados_clientes(self):
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
            cnpj = dados_atualizados["CNPJ"]  # Supondo que o CNPJ seja identificador único

            query = """
                UPDATE clientes_juridicos SET
                    `Nome do Cliente` = ?, `Razão Social` = ?, `Data da Inclusão` = ?, CNPJ = ?,
                    RG = ?,  = ?, CPF = ?,CNH = ?, `Categoria da CNH` = ?, `Data de Emissão da CNH` = ?, 
                    `Data de Vencimento da CNH` = ?,`Data de Nascimento` = ?, Telefone = ?, CEP = ?, Endereço = ?, 
                    Número = ?, Complemento = ?,Cidade = ?, Bairro = ?, Estado = ?, `Status do Cliente` = ?, `Categoria do Cliente` = ?,
                    `Última Atualização` = ?, `Origem do Cliente` = ?, `Valor Gasto Total` = ?, `Última Compra` = ?
                WHERE CNPJ = ?
            """
            valores = (
                dados_atualizados["Nome do Cliente"], dados_atualizados["Razão Social"], dados_atualizados["Data da Inclusão"], dados_atualizados["CNPJ"],
                dados_atualizados["RG"], dados_atualizados["CPF"],dados_atualizados["CNH"], dados_atualizados["Categoria da CNH"], dados_atualizados["Data de Emissão da CNH"], 
                dados_atualizados["Data de Vencimento da CNH"], dados_atualizados["Telefone"], dados_atualizados["CEP"], dados_atualizados["Endereço"], dados_atualizados["Número"], dados_atualizados["Complemento"],
                dados_atualizados["Cidade"], dados_atualizados["Bairro"], dados_atualizados["Estado"], dados_atualizados["Status do Cliente"], dados_atualizados["Categoria do Cliente"],
                dados_atualizados["Última Atualização"], dados_atualizados["Origem do Cliente"], dados_atualizados["Valor Gasto Total"], dados_atualizados["Última Compra"],
                cnpj
            )


            cursor.execute(query, valores)
            self.db.connection.commit()
            QMessageBox.information(None, "Sucesso", "Cliente atualizado com sucesso.")
            self.janela_editar_cliente.close()
            self.carregar_clientes_juridicos()  
        except Exception as e:
            QMessageBox.critical(None, "Erro", f"Erro ao atualizar cliente: {e}")

    

    def exibir_janela_cadastro_cliente(self):
        self.campos_cliente_juridico = {}
        self.informacoes_obrigatorias_clientes()
        
        self.janela_cadastro = QMainWindow()
        self.janela_cadastro.resize(700, 550)
        self.janela_cadastro.setWindowTitle("Cadastro do Cliente")
        self.janela_cadastro.setStyleSheet("background-color: rgb(0, 80, 121);")

        # Centralizar a janela
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_geometry = self.janela_cadastro.frameGeometry()
        window_geometry.moveCenter(screen_geometry.center())
        self.janela_cadastro.move(window_geometry.topLeft())

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
            label = QLabel(titulo)
            label.setStyleSheet("color: black; font-weight: bold;")
            layout.addWidget(label)
            if widget is None:
                widget = QLineEdit()
            layout.addWidget(widget)
            chave_sem_ponto = titulo.rstrip(":")
            self.campos_cliente_juridico[chave_sem_ponto] = widget
            return label, widget

        # ComboBox Categoria CNH criado antecipadamente para uso no formulário
        combobox_categoria_cnh = QComboBox()
        combobox_categoria_cnh.addItems(["Selecionar", "AB", "A", "B", "C", "D", "E", "Nenhuma"])
        combobox_categoria_cnh.setCurrentIndex(0)
        combobox_categoria_cnh.setStyleSheet("""
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
                height: 0px;
            }
            QComboBox QAbstractItemView QScrollBar::add-page:vertical, 
            QComboBox QAbstractItemView QScrollBar::sub-page:vertical {
                background: none;
            }
        """)


        # Adicionar campos na ordem correta
        add_linha("Nome do Cliente")
        add_linha("Razão Social")
        add_linha("CNPJ")
        cnpj_widget = self.campos_cliente_juridico["CNPJ"]
        cnpj_widget.textChanged.connect(lambda text: self.main_window.formatar_cnpj(text, cnpj_widget))

        add_linha("RG")
        self.campos_cliente_juridico["RG"].setPlaceholderText("Opcional")
        rg_widget = self.campos_cliente_juridico["RG"]
        rg_widget.textChanged.connect(lambda text: self.main_window.formatar_rg(text, rg_widget))

        add_linha("CPF")
        cpf_widget = self.campos_cliente_juridico["CPF"]
        cpf_widget.textChanged.connect(lambda text: self.main_window.formatar_cpf(text, cpf_widget))

        add_linha("Email")
        email_widget = self.campos_cliente_juridico["Email"]
        email_widget.textChanged.connect(lambda text: self.main_window.validar_email(text,email_widget))

        add_linha("CNH")
        self.campos_cliente_juridico["CNH"].setPlaceholderText("Opcional")
        label_categoria_cnh, widget_categoria_cnh = add_linha("Categoria da CNH", combobox_categoria_cnh)

        # Campos Data Emissão e Vencimento CNH, inicialmente escondidos
        label_emissao_cnh, widget_emissao_cnh = add_linha("Data de Emissão da CNH")
        label_vencimento_cnh, widget_vencimento_cnh = add_linha("Data de Vencimento da CNH")

        # Aplicar formatação de data (mesma usada em Data de Nascimento)
        widget_emissao_cnh.textChanged.connect(lambda text: self.main_window.formatar_data_nascimento(text, widget_emissao_cnh))
        widget_vencimento_cnh.textChanged.connect(lambda text: self.main_window.formatar_data_nascimento(text, widget_vencimento_cnh))
        label_emissao_cnh.hide()
        widget_emissao_cnh.hide()
        label_vencimento_cnh.hide()
        widget_vencimento_cnh.hide()

        cnh_widget = self.campos_cliente_juridico["CNH"]
        cnh_widget.textChanged.connect(lambda text: self.main_window.formatar_cnh(text, cnh_widget))

        # Função para mostrar/esconder datas da CNH conforme categoria selecionada
        def on_categoria_cnh_change(text):
            if text not in ("Selecionar", "Nenhuma"):
                label_emissao_cnh.show()
                widget_emissao_cnh.show()
                label_vencimento_cnh.show()
                widget_vencimento_cnh.show()
            else:
                label_emissao_cnh.hide()
                widget_emissao_cnh.hide()
                label_vencimento_cnh.hide()
                widget_vencimento_cnh.hide()
                widget_emissao_cnh.clear()
                widget_vencimento_cnh.clear()

        combobox_categoria_cnh.currentTextChanged.connect(on_categoria_cnh_change)

        add_linha("Telefone")
        telefone_widget = self.campos_cliente_juridico["Telefone"]
        telefone_widget.textChanged.connect(lambda text: self.main_window.formatar_telefone(text, telefone_widget))

        add_linha("CEP")
        cep_widget = self.campos_cliente_juridico["CEP"]
        cep_widget.textChanged.connect(lambda text: self.main_window.formatar_cep(text, cep_widget))
        cep_widget.editingFinished.connect(lambda: self.on_cep_editing_finished_cadastro(cep_widget))

        add_linha("Endereço")
        add_linha("Número")
        add_linha("Complemento")
        self.campos_cliente_juridico["Complemento"].setPlaceholderText("Opcional")
        add_linha("Cidade")
        add_linha("Bairro")

        # ComboBox Estado
        combobox_estado_cliente = QComboBox()
        combobox_estado_cliente.addItems([
            "Selecionar","AC","AL","AP","AM","BA","CE","DF","ES","GO","MA","MT",
            "MS","MG","PA","PB","PR","PE","PI","RJ","RN","RS","RO","RR","SC","SP","SE","TO"
        ])
        combobox_estado_cliente.setCurrentIndex(0)
        combobox_estado_cliente.setStyleSheet("""
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
                height: 0px;
            }
            QComboBox QAbstractItemView QScrollBar::add-page:vertical, 
            QComboBox QAbstractItemView QScrollBar::sub-page:vertical {
                background: none;
            }
        """)
        add_linha("Estado", combobox_estado_cliente)
        add_linha("Categoria do Cliente")

        combobox_status_cliente = QComboBox()
        combobox_status_cliente.addItems(["Selecionar","Ativo","Inativo","Pendente","Bloqueado"])
        combobox_status_cliente.setCurrentIndex(0)
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
                height: 0px;
            }
            QComboBox QAbstractItemView QScrollBar::add-page:vertical, 
            QComboBox QAbstractItemView QScrollBar::sub-page:vertical {
                background: none;
            }
        """)
        add_linha("Status do Cliente:", combobox_status_cliente)

        btn_fazer_cadastro = QPushButton("Fazer o Cadastro")
        btn_fazer_cadastro.clicked.connect(self.cadastrar_clientes_juridicos)
        btn_fazer_cadastro.setStyleSheet("""
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
        layout.addWidget(btn_fazer_cadastro)

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

        self.janela_cadastro.setCentralWidget(scroll_area)
        self.janela_cadastro.show()

    def informacoes_obrigatorias_clientes(self):
        self.campos_obrigatorios_clientes = {
            "Nome do Cliente": "O campo Nome do Cliente é obrigatório.",
            "Razão Social": "O campo de Razão Social é obrigatório",
            "CNPJ": "O campo CNPJ é obrigatório.",
            "RG": "O campo de RG é obrigatório.",
            "CPF": "O campo de CPF é obrigatório",
            "Email": "O campo de E-mail é obrigatório",
            "Telefone": "O campo Telefone é obrigatório.",
            "CEP": "O campo CEP é obrigatório.",
            "Endereço": "O campo Endereço é obrigatório.",
            "Número": "O campo Número é obrigatório.",
            "Cidade": "O campo Cidade é obrigatório.",
            "Bairro": "O campo Bairro é obrigatório.",
            "Estado": "O campo de Estado é obrigatório",
            "Categoria do Cliente": "O campo Categoria do Cliente é obrigatório.",
            "Status do Cliente": "Você deve selecionar um status válido para o cliente.",
        }

        # Verifica se a Categoria da CNH foi preenchida (diferente de "Selecionar")
        categoria_widget = self.campos_cliente_juridico.get("Categoria da CNH")
        if categoria_widget and isinstance(categoria_widget, QComboBox):
            categoria_cnh = categoria_widget.currentText().strip()
            if categoria_cnh and categoria_cnh != "Selecionar":
                self.campos_obrigatorios_clientes["Data de Emissão da CNH"] = "A Data de Emissão da CNH é obrigatória quando há Categoria informada."
                self.campos_obrigatorios_clientes["Data de Vencimento da CNH"] = "A Data de Vencimento da CNH é obrigatória quando há Categoria informada."

    def cadastrar_clientes_juridicos(self):
        try:
            with self.db.connecta() as conexao:
                cursor = conexao.cursor()
                usuario_logado = self.config.obter_usuario_logado()

                # Coletar dados dos campos
                get = lambda campo: self.campos_cliente_juridico[campo].text().strip() \
                    if isinstance(self.campos_cliente_juridico[campo], QLineEdit) \
                    else self.campos_cliente_juridico[campo].currentText()

                nome = get("Nome do Cliente")
                razao_social = get("Razão Social")
                cnpj = get("CNPJ")
                rg = get("RG")
                cpf = get("CPF")
                email = get("Email")
                cnh = get("CNH")
                categoria_cnh = get("Categoria da CNH")
                data_emissao_cnh = get("Data de Emissão da CNH")
                data_vencimento_cnh = get("Data de Vencimento da CNH")
                telefone = get("Telefone")
                cep = get("CEP")
                endereco = get("Endereço")
                numero = get("Número")
                complemento = get("Complemento")
                cidade = get("Cidade")
                bairro = get("Bairro")
                estado = get("Estado")
                categoria = get("Categoria do Cliente")
                status = get("Status do Cliente")

                # Verificar se o cliente já existe
                cursor.execute("""
                    SELECT 1 FROM clientes_juridicos 
                    WHERE CNPJ = ? OR "Razão Social" = ?
                """, (cnpj, razao_social))

                if cursor.fetchone():
                    QMessageBox.warning(None, "Cliente já existe", "Já existe um cliente com este CNPJ ou Razão Social.")
                    return

                # Validação de todos os campos obrigatórios
                for campo, mensagem in self.campos_obrigatorios_clientes.items():
                    widget = self.campos_cliente_juridico[campo]
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
                        "Nome do Cliente", "Razão Social", "Data da Inclusão", CNPJ, RG, 
                         CPF,Email, CNH, "Categoria da CNH", "Data de Emissão da CNH", "Data de Vencimento da CNH",  
                        Telefone, CEP, Endereço, Número, Complemento, Cidade, Bairro, Estado, 
                        "Status do Cliente", "Categoria do Cliente", "Última Atualização", "Valor Gasto Total", "Última Compra"
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)
                """, (
                    nome, razao_social, data_inclusao, cnpj, rg, 
                    cpf,email, cnh, categoria_cnh, data_emissao_cnh, data_vencimento_cnh, 
                    telefone, cep, endereco, numero, complemento, cidade, bairro, estado, 
                    status, categoria, ultima_atualizacao, valor_gasto_total,ultima_compra
                ))
                conexao.commit()

                self.main_window.registrar_historico_clientes_juridicos(
                    "Cadastro de Cliente", f"Cliente {nome} cadastrado com sucesso"
                )
                
                QMessageBox.information(None, "Sucesso", "Cliente cadastrado com sucesso!")
                # Redimensiona apenas uma vez após preencher
                self.table_clientes_juridicos.resizeColumnsToContents()
                self.table_clientes_juridicos.resizeRowsToContents()
                self.limpar_campos_clientes()
                self.carregar_clientes_juridicos()
                

        except Exception as e:
            QMessageBox.critical(None, "Erro", f"Erro ao cadastrar cliente: \n{e}")

        
    def limpar_campos_clientes(self):
        for campo, widget in self.campos_cliente_juridico.items():
            if isinstance(widget,QLineEdit):
                widget.clear()
            elif isinstance(widget, QComboBox):
                widget.setCurrentIndex(0) # Volta para "Selecionar"
                    
    def on_cep_editing_finished_cadastro(self, cep_widget):
        cep_digitado = cep_widget.text()
        dados_cep = self.main_window.buscar_cep(cep_digitado)
        if dados_cep:
            self.preencher_campos_cep_cadastro(dados_cep)

    def preencher_campos_cep_cadastro(self, dados):
        if dados is None:
            return

        # Preencher os campos do seu formulário usando self.campos_cliente_juridico
        self.campos_cliente_juridico["Endereço"].setText(dados.get("logradouro", ""))
        self.campos_cliente_juridico["Bairro"].setText(dados.get("bairro", ""))
        self.campos_cliente_juridico["Cidade"].setText(dados.get("localidade", ""))

        complemento = dados.get("complemento", "")
        if any(char.isdigit() for char in complemento):
            self.campos_cliente_juridico["Número"].setText(complemento)

        estado = dados.get("uf", "")
        # Se tiver um combobox para estado, aqui você ajusta o índice
        if "Estado" in self.campos_cliente_juridico:
            estado_combobox = self.campos_cliente_juridico["Estado"]
            index_estado = estado_combobox.findText(estado)
            if index_estado != -1:
                estado_combobox.setCurrentIndex(index_estado)
                
    def excluir_clientes_juridicos(self):
        try:
            total_linhas = self.table_clientes_juridicos.rowCount()
            if total_linhas == 0:
                QMessageBox.warning(self, "Aviso", "Nenhum cliente encontrado para excluir.")
                return

            clientes_para_excluir = []

            if self.coluna_checkboxes_clientes_adicionada:
                # Modo com checkbox
                for linha in range(total_linhas):
                    checkbox_widget = self.table_clientes_juridicos.cellWidget(linha, 0)
                    if checkbox_widget:
                        checkbox = checkbox_widget.findChild(QCheckBox)
                        if checkbox and checkbox.isChecked():
                            nome_cliente = self.table_clientes_juridicos.item(linha, 1).text()
                            clientes_para_excluir.append((linha, nome_cliente))
            else:
                # Modo sem checkbox (seleção direta)
                linha_selecionadas = self.table_clientes_juridicos.selectionModel().selectedRows()
                if not linha_selecionadas:
                    QMessageBox.information(None, "Aviso", "Nenhum cliente selecionado para exclusão.")
                    return
                
                for index in linha_selecionadas:
                    linha = index.row()
                    nome_cliente = self.table_clientes_juridicos.item(linha,0).text()
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
                    DELETE FROM clientes_juridicos WHERE "Nome do Cliente" = ?
                """, (nome_cliente,))
                self.table_clientes_juridicos.removeRow(linha)

            db.connection.commit()
            
            nomes_excluidos = ", ".join(nome for _, nome in clientes_para_excluir)
            self.main_window.registrar_historico_clientes_juridicos(
                "Exclusão de Cliente(s)",
                f"Cliente(s) excluído(s): {nomes_excluidos}"
            )
            QMessageBox.information(self.main_window, "Sucesso", "Cliente(s) excluído(s) com sucesso.")
        except Exception as e:
            QMessageBox.critical(self.main_window, "Erro", f"Erro ao excluir clientes:\n{e}")
            
    def marcar_como_clientes(self):
        if self.table_clientes_juridicos.rowCount() == 0:
            QMessageBox.warning(None,"Aviso","Nenhum cliente cadastrado para selecionar.")
             # Desmarca o checkbox header visualmente
            if hasattr(self, "checkbox_header_clientes") and isinstance(self.checkbox_header_clientes, QCheckBox):
                QTimer.singleShot(0, lambda: self.checkbox_header_clientes.setChecked(False))

            return  # Impede que o restante da função execute!

        if self.coluna_checkboxes_clientes_adicionada:
            # Animação de saída (fade out)
            self.animar_coluna_checkbox(mostrar=False)
            QTimer.singleShot(300, lambda: self.remover_coluna_checkboxes())
            return

        # Adiciona a coluna de checkboxes
        self.table_clientes_juridicos.insertColumn(0)
        self.table_clientes_juridicos.setHorizontalHeaderItem(0, QTableWidgetItem(""))
        self.table_clientes_juridicos.setColumnWidth(0, 30)
        self.table_clientes_juridicos.horizontalHeader().setMinimumSectionSize(30)
        self.table_clientes_juridicos.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)

        # Checkbox no cabeçalho
        self.checkbox_header_clientes = QCheckBox(self.table_clientes_juridicos)
        self.checkbox_header_clientes.setToolTip("Selecionar todos")
        self.checkbox_header_clientes.setChecked(False)
        self.checkbox_header_clientes.stateChanged.connect(self.selecionar_todos_clientes)
        self.checkbox_header_clientes.setFixedSize(20, 20)
        self.checkbox_header_clientes.setStyleSheet("background-color: transparent; border: none;")
        self.checkbox_header_clientes.show()

        header = self.table_clientes_juridicos.horizontalHeader()
        header.sectionResized.connect(self.atualizar_posicao_checkbox_header_clientes)

        self.checkboxes_clientes = []

        for linha in range(self.table_clientes_juridicos.rowCount()):
            checkbox = QCheckBox()
            checkbox.stateChanged.connect(self.atualizar_selecao_todos_clientes)

            container = QWidget()
            layout = QHBoxLayout(container)
            layout.addWidget(checkbox)
            layout.setAlignment(Qt.AlignCenter)
            layout.setContentsMargins(0, 0, 0, 0)

            self.table_clientes_juridicos.setCellWidget(linha, 0, container)
            self.checkboxes_clientes.append(checkbox)

        QTimer.singleShot(0, self.atualizar_posicao_checkbox_header_clientes)

        self.coluna_checkboxes_clientes_adicionada = True
        
        # Animação de entrada (fade in)
        self.animar_coluna_checkbox(mostrar=True)
        
    def animar_coluna_checkbox(self, mostrar=True):
        self.animacoes_clientes = []

        for row in range(self.table_clientes_juridicos.rowCount()):
            widget = self.table_clientes_juridicos.cellWidget(row, 0)
            if widget:
                efeito = QGraphicsOpacityEffect(widget)
                widget.setGraphicsEffect(efeito)

                # Cria animação corretamente
                anim = QPropertyAnimation(efeito, b"opacity")
                anim.setDuration(300)
                anim.setStartValue(0.0 if mostrar else 1.0)
                anim.setEndValue(1.0 if mostrar else 0.0)
                anim.start()

                self.animacoes_clientes.append(anim)

                
    def remover_coluna_checkboxes(self):
        self.table_clientes_juridicos.removeColumn(0)
        self.table_clientes_juridicos.verticalHeader().setVisible(True)
        self.coluna_checkboxes_clientes_adicionada = False

        if hasattr(self, "checkbox_header_clientes"):
            self.checkbox_header_clientes.setChecked(False)
            self.checkbox_header_clientes.deleteLater()
            del self.checkbox_header_clientes

        self.checkboxes_clientes.clear()

        
    def selecionar_todos_clientes(self):
        # Evita erro ao clicar quando a coluna já foi removida
        if not getattr(self, "coluna_checkboxes_clientes_adicionada", False):
            return  # Simplesmente sai sem mostrar mensagem

        estado = self.checkbox_header_clientes.checkState() == Qt.Checked
        self.checkboxes_clientes.clear()

        for row in range(self.table_clientes_juridicos.rowCount()):
            widget = self.table_clientes_juridicos.cellWidget(row, 0)
            if widget is not None:
                checkbox = widget.findChild(QCheckBox)
                if checkbox:
                    checkbox.blockSignals(True)
                    checkbox.setChecked(estado)
                    checkbox.blockSignals(False)
                    self.checkboxes_clientes.append(checkbox)


    def atualizar_selecao_todos_clientes(self):
        self.checkbox_header_clientes.blockSignals(True)

        all_checked = all(cb.isChecked() for cb in self.checkboxes_clientes if cb)
        any_checked = any(cb.isChecked() for cb in self.checkboxes_clientes if cb)

        if all_checked:
            self.checkbox_header_clientes.setCheckState(Qt.Checked)
        elif any_checked:
            self.checkbox_header_clientes.setCheckState(Qt.PartiallyChecked)
        else:
            self.checkbox_header_clientes.setCheckState(Qt.Unchecked)

        self.checkbox_header_clientes.blockSignals(False)

    def atualizar_posicao_checkbox_header_clientes(self):
        if hasattr(self, "checkbox_header_clientes") and self.coluna_checkboxes_clientes_adicionada:
            header = self.table_clientes_juridicos.horizontalHeader()
            
            x = header.sectionViewportPosition(0) + (header.sectionSize(0) - self.checkbox_header_clientes.width()) // 2 + 20
            y = (header.height() - self.checkbox_header_clientes.height()) // 2
            self.checkbox_header_clientes.move(x, y)
            
    # Limpa a coluna selecionada clicando em qualquer lugar da tabela
    def eventFilter(self, source, event):
        if event.type() == QEvent.MouseButtonPress:
            if source == self.table_clientes_juridicos.viewport():
                index = self.table_clientes_juridicos.indexAt(event.pos())
                if not index.isValid():
                    self.table_clientes_juridicos.clearSelection() # remove a linha selecinada da tabela
                    self.table_clientes_juridicos.clearFocus() # remove o foco da tabela      
        return super().eventFilter(source,event)
    
    def exibir_janela_historico_clientes(self):
        pass
    
    def marcar_alteracao(self):
        self.alteracoes_realizadas = True


    def historico_clientes_juridicos(self):
        self.janela_historico_clientes = QMainWindow()
        self.janela_historico_clientes.resize(800,650)
        self.janela_historico_clientes.setWindowTitle("Histórico de Clientes")

        # Centralizar a janela na tela
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_geometry = self.janela_historico_clientes.frameGeometry()
        window_geometry.moveCenter(screen_geometry.center())
        self.janela_historico_clientes.move(window_geometry.topLeft())

        # Criação do layout e tabela para exibir o histórico
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # Tabela do histórico
        self.tabela_historico_clientes = QTableWidget()
        self.tabela_historico_clientes.setColumnCount(4)
        self.tabela_historico_clientes.setHorizontalHeaderLabels(["Data/Hora", "Usuário", "Ação", "Descrição"])

        # Botão Atualizar
        botao_atualizar = QPushButton("Atualizar Histórico")
        botao_atualizar.clicked.connect(self.atualizar_historico_clientes_jurididos)

        # Botão Apagar
        botao_apagar = QPushButton("Apagar Histórico")
        botao_apagar.clicked.connect(self.apagar_historico_cliente_juridicos)

        # Botão Exportar CSV
        botao_exportar_csv = QPushButton("Exportar para CSV")
        botao_exportar_csv.clicked.connect(self.exportar_csv_juridicos)

        
        # Botão Exportar Excel
        botao_exportar_excel = QPushButton("Exportar para Excel")
        botao_exportar_excel.clicked.connect(self.exportar_excel_juridicos)

        # Botão PDF
        botao_exportar_pdf = QPushButton("Exportar PDF")
        botao_exportar_pdf.clicked.connect(self.exportar_pdf_juridicos)

        botao_pausar_historico = QPushButton("Pausar Histórico")
        botao_pausar_historico.clicked.connect(self.pausar_historico_juridicos)


        botao_filtrar_historico = QPushButton("Filtrar Histórico")
        botao_filtrar_historico.clicked.connect(self.filtrar_historico_clientes_juridicos)

        botao_ordenar_historico = QPushButton("Ordenar Histórico")
        botao_ordenar_historico.clicked.connect(self.ordenar_historico_clientes_juridicos)


        # Criar checkbox "Selecionar Individualmente" toda vez que a janela for aberta
        self.checkbox_selecionar = QCheckBox("Selecionar")
        self.checkbox_selecionar.stateChanged.connect(self.selecionar_individual_juridicos)

        # Adicionar outros botões ao layout
        layout.addWidget(botao_atualizar)
        layout.addWidget(botao_apagar)
        layout.addWidget(botao_exportar_csv)
        layout.addWidget(botao_exportar_excel)
        layout.addWidget(botao_exportar_pdf)
        layout.addWidget(botao_pausar_historico)
        layout.addWidget(botao_ordenar_historico)
        layout.addWidget(botao_filtrar_historico)
        layout.addWidget(self.checkbox_selecionar)
        layout.addWidget(self.tabela_historico_clientes)
        


        # Configurar o widget central e exibir a janela
        self.janela_historico_clientes.setCentralWidget(central_widget)
        self.janela_historico_clientes.show()

         # Redimensionar colunas e linhas
        self.carregar_historico_clientes_juridicos()
        self.tabela_historico_clientes.resizeColumnsToContents()
        self.tabela_historico_clientes.resizeRowsToContents()

    def carregar_historico_clientes_juridicos(self):
            with sqlite3.connect('banco_de_dados.db') as cn:
                cursor = cn.cursor()
                cursor.execute('SELECT * FROM historico_clientes_juridicos ORDER BY "Data e Hora" DESC')
                registros = cursor.fetchall()

            self.tabela_historico_clientes.clearContents()
            self.tabela_historico_clientes.setRowCount(len(registros))

            deslocamento = 1 if self.coluna_checkboxes_clientes_adicionada else 0
            self.checkboxes_clientes = []  # Zerar e recriar lista de checkboxes

            for i, (data, usuario, acao, descricao) in enumerate(registros):
                if self.coluna_checkboxes_clientes_adicionada:
                    checkbox = QCheckBox()
                    checkbox.setStyleSheet("margin-left:9px; margin-right:9px;")
                    self.tabela_historico_clientes.setCellWidget(i,0,checkbox)
                    self.checkboxes_clientes.append(checkbox)
                self.tabela_historico_clientes.setItem(i, 0 + deslocamento, QTableWidgetItem(data))
                self.tabela_historico_clientes.setItem(i, 1 + deslocamento, QTableWidgetItem(usuario))
                self.tabela_historico_clientes.setItem(i, 2 + deslocamento, QTableWidgetItem(acao))
                self.tabela_historico_clientes.setItem(i, 3 + deslocamento, QTableWidgetItem(descricao))

    def atualizar_historico_clientes_jurididos(self):
        QMessageBox.information(None, "Sucesso", "Dados carregados com sucesso!")
        self.carregar_historico_clientes_juridicos()

    def confirmar_historico_cliente_juridicos_apagado(self, mensagem):
        msgbox = QMessageBox(self)
        msgbox.setWindowTitle("Confirmação")
        msgbox.setText(mensagem)

        btn_sim = QPushButton("Sim")
        btn_nao = QPushButton("Não")
        msgbox.addButton(btn_sim, QMessageBox.ButtonRole.YesRole)
        msgbox.addButton(btn_nao, QMessageBox.ButtonRole.NoRole)

        msgbox.setDefaultButton(btn_nao)
        resposta = msgbox.exec()

        return msgbox.clickedButton() == btn_sim
    
    def apagar_historico_cliente_juridicos(self):
        # Caso checkboxes estejam ativados
        if self.coluna_checkboxes_clientes_adicionada and self.checkboxes_clientes:
            linhas_para_remover = []
            datas_para_remover = []

            # Identificar as linhas com checkboxes selecionados
            for row, checkbox in enumerate(self.checkboxes_clientes):
                if checkbox and checkbox.isChecked():
                    linhas_para_remover.append(row)
                    coluna_data_hora = 0 if not self.coluna_checkboxes_clientes_adicionada else 1
                    item_data_widget = self.tabela_historico_clientes.item(row, coluna_data_hora)  # Coluna de Data/Hora
                    if item_data_widget:
                        data_text = item_data_widget.text().strip()
                        # Excluir com base na data e hora
                        if data_text:
                            datas_para_remover.append(data_text)
                        else:
                            print(f"[AVISO] Linha {row} com Data e Hora vazia.")
                    else:
                        print(f"[ERRO] Coluna 'Data e Hora' não encontrada na linha {row}.")

            if not datas_para_remover:
                QMessageBox.warning(self, "Erro", "Nenhum item válido foi selecionado para apagar!")
                return

            # Confirmar exclusão
            mensagem = (
                f"Você tem certeza que deseja apagar os {len(datas_para_remover)} itens selecionados?"
                if len(datas_para_remover) > 1
                else "Você tem certeza que deseja apagar o item selecionado?"
            )

            if not self.confirmar_historico_apagado_clientes(mensagem):
                return

            # Excluir do banco de dados
            with sqlite3.connect('banco_de_dados.db') as cn:
                cursor = cn.cursor()
                try:
                    for data in datas_para_remover:
                        cursor.execute('DELETE FROM historico_clientes_juridicos WHERE "Data e Hora" = ?', (data,))
                    cn.commit()
                except Exception as e:
                    QMessageBox.critical(self, "Erro", f"Erro ao excluir do banco de dados: {e}")
                    return

            # Remover as linhas na interface
            for row in sorted(linhas_para_remover, reverse=True):
                self.tabela_historico_clientes.removeRow(row)

            QMessageBox.information(self, "Sucesso", "Itens removidos com sucesso!")

        # Caso sem checkboxes (seleção manual)
        else:
            linha_selecionada = self.tabela_historico_clientes.currentRow()

            if linha_selecionada < 0:
                QMessageBox.warning(self, "Erro", "Nenhum item foi selecionado para apagar!")
                return

            # Capturar a Data/Hora da célula correspondente (coluna 0)
            coluna_data_hora = 0 if not self.coluna_checkboxes_clientes_adicionada else 1
            item_data_widget = self.tabela_historico_clientes.item(linha_selecionada, coluna_data_hora)  # Coluna de Data/Hora
            if not item_data_widget:
                QMessageBox.warning(self, "Erro", "Não foi possível identificar a Data/Hora do item a ser apagado!")
                return

            item_data_text = item_data_widget.text().strip()

            # Verificar se há um valor válido de data/hora
            if not item_data_text:
                QMessageBox.warning(self, "Erro", "Não foi possível identificar a Data/Hora do item a ser apagado!")
                return


            # Confirmar exclusão
            mensagem = "Você tem certeza que deseja apagar o item selecionado?"

            if not self.confirmar_historico_cliente_juridicos_apagado(mensagem):
                return

            # Excluir do banco de dados
            with sqlite3.connect('banco_de_dados.db') as cn:
                cursor = cn.cursor()
                try:
                    cursor.execute('DELETE FROM historico_clientes_juridicos WHERE "Data e Hora" = ?', (item_data_text,))
                    cn.commit()
                except Exception as e:
                    QMessageBox.critical(self, "Erro", f"Erro ao excluir do banco de dados: {e}")
                    return

            # Remover a linha da interface
            self.tabela_historico_clientes.removeRow(linha_selecionada)

            QMessageBox.information(self, "Sucesso", "Item removido com sucesso!")

    def selecionar_todos_clientes_juridicos(self):
        if not self.coluna_checkboxes_clientes_adicionada:
            QMessageBox.warning(self, "Aviso", "Ative a opção 'Selecionar Individualmente' antes.")
            if hasattr(self, "checkbox_header"):
                self.checkbox_header_juridicos.setChecked(False)
            return

        estado = self.checkbox_header_juridicos.checkState() == Qt.Checked
        self.checkboxes_clientes.clear()  # Reinicia a lista para manter consistência
        
        for row in range(self.tabela_historico_clientes.rowCount()):
            widget = self.tabela_historico_clientes.cellWidget(row, 0)
            if widget is not None:
                checkbox = widget.findChild(QCheckBox)
                if checkbox:
                    checkbox.blockSignals(True)
                    checkbox.setChecked(estado)
                    checkbox.blockSignals(False)



     # Função para adicionar checkboxes selecionar_individual na tabela de histórico
    def selecionar_individual_juridicos(self):
        if self.tabela_historico_clientes.rowCount() == 0:
            QMessageBox.warning(None, "Aviso", "Nenhum histórico para selecionar.")
            self.checkbox_selecionar_individual.setChecked(False)
            return

        if self.coluna_checkboxes_clientes_adicionada:
            self.tabela_historico_clientes.removeColumn(0)
            self.tabela_historico_clientes.verticalHeader().setVisible(True)
            self.coluna_checkboxes_clientes_adicionada = False

            if hasattr(self, "checkbox_header_juridicos"):
                self.checkbox_header_juridicos.deleteLater()
                del self.checkbox_header_juridicos

            self.checkboxes_clientes.clear()
            return

        self.tabela_historico_clientes.insertColumn(0)
        self.tabela_historico_clientes.setHorizontalHeaderItem(0, QTableWidgetItem(""))
        self.tabela_historico_clientes.setColumnWidth(0, 30)
        self.tabela_historico_clientes.horizontalHeader().setMinimumSectionSize(30)
        self.tabela_historico_clientes.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)

        # Checkbox do cabeçalho
        self.checkbox_header_juridicos = QCheckBox(self.tabela_historico_clientes)
        self.checkbox_header_juridicos.setToolTip("Selecionar todos")
        self.checkbox_header_juridicos.setChecked(False)
        self.checkbox_header_juridicos.stateChanged.connect(self.selecionar_todos_clientes_juridicos)
        self.checkbox_header_juridicos.setFixedSize(20, 20)
        self.checkbox_header_juridicos.show()

        header = self.tabela_historico_clientes.horizontalHeader()
        self.atualizar_posicao_checkbox_header_juridicos()
        header.sectionResized.connect(self.atualizar_posicao_checkbox_header_juridicos)

        self.checkboxes_clientes.clear()

        QTimer.singleShot(0,self.atualizar_posicao_checkbox_header_juridicos)

        for row in range(self.tabela_historico_clientes.rowCount()):
            checkbox = QCheckBox()
            checkbox.stateChanged.connect(self.atualizar_selecao_todos)

            container = QWidget()
            layout = QHBoxLayout(container)
            layout.addWidget(checkbox)
            layout.setAlignment(Qt.AlignCenter)
            layout.setContentsMargins(0, 0, 0, 0)

            self.tabela_historico_clientes.setCellWidget(row, 0, container)
            self.checkboxes_clientes.append(checkbox)

        self.tabela_historico_clientes.verticalHeader().setVisible(False)
        self.coluna_checkboxes_clientes_adicionada = True

    def atualizar_selecao_todos(self):
        self.checkbox_header_juridicos.blockSignals(True)

        all_checked = all(checkbox.isChecked() for checkbox in self.checkboxes_clientes if checkbox)
        any_checked = any(checkbox.isChecked() for checkbox in self.checkboxes_clientes if checkbox)

        if all_checked:
            self.checkbox_header_juridicos.setCheckState(Qt.Checked)
        elif any_checked:
            self.checkbox_header_juridicos.setCheckState(Qt.PartiallyChecked)
        else:
            self.checkbox_header_juridicos.setCheckState(Qt.Unchecked)

        self.checkbox_header_juridicos.blockSignals(False)

        
    def atualizar_posicao_checkbox_header_juridicos(self):
        if hasattr(self, "checkbox_header_juridicos") and self.coluna_checkboxes_clientes_adicionada:
            header = self.tabela_historico_clientes.horizontalHeader()

            x = header.sectionViewportPosition(0) + (header.sectionSize(0) - self.checkbox_header_juridicos.width()) // 2 + 4
            y = (header.height() - self.checkbox_header_juridicos.height()) // 2

            self.checkbox_header_juridicos.move(x, y)
            
    def ordenar_historico_clientes_juridicos(self):
        if hasattr(self, "checkbox_header_juridicos"):
            QMessageBox.warning(
                None,
                "Aviso",
                "Desmarque o checkbox antes de ordenar o histórico."
            )
            return
        # Obter a coluna pela qual o usuário deseja ordenar
        coluna = self.obter_coluna_para_ordenar_clientes_juridicos()  # Função fictícia para capturar escolha
        if coluna is None:
            return  # Cancela o processo todo
        
        # Determinar a direção de ordenação (ascendente ou descendente)
        direcao = self.obter_direcao_ordenacao_clientes_juridicos()  # Função fictícia para capturar escolha
        if direcao is None:
            return  # Cancela o processo todo
        
        # Mapeamento de colunas para índices (ajustar conforme sua tabela)
        colunas_para_indices = {
            "Data/Hora": 0,
            "Usuário": 1,
            "Ação": 2,
            "Descrição": 3
        }
        
        # Verificar se a coluna escolhida é válida
        if coluna not in colunas_para_indices:
            QMessageBox.warning(self, "Erro", "Coluna inválida para ordenação!")
            return
        
        # Obter o índice da coluna escolhida
        indice_coluna = colunas_para_indices[coluna]
        
        # Obter os dados atuais da tabela
        dados = []
        for row in range(self.tabela_historico_clientes.rowCount()):
            linha = [
                self.tabela_historico_clientes.item(row, col).text() if self.tabela_historico_clientes.item(row, col) else ""
                for col in range(self.tabela_historico_clientes.columnCount())
            ]
            dados.append(linha)
        
        # Ordenar os dados com base na coluna escolhida e direção
        dados.sort(key=lambda x: x[indice_coluna], reverse=(direcao == "Decrescente"))
        
        # Atualizar a tabela com os dados ordenados
        self.tabela_historico_clientes.setRowCount(0)  # Limpar tabela
        for row_data in dados:
            row = self.tabela_historico_clientes.rowCount()
            self.tabela_historico_clientes.insertRow(row)
            for col, value in enumerate(row_data):
                self.tabela_historico_clientes.setItem(row, col, QTableWidgetItem(value))

    def obter_coluna_para_ordenar_clientes_juridicos(self):
        colunas = ["Data/Hora", "Usuário", "Ação", "Descrição"]
        coluna, ok = QInputDialog.getItem(self, "Ordenar por", "Escolha a coluna:", colunas, 0, False)
        return coluna if ok else None

    def obter_direcao_ordenacao_clientes_juridicos(self):
        direcoes = ["Crescente", "Decrescente"]
        direcao, ok = QInputDialog.getItem(self, "Direção da Ordenação", "Escolha a direção:", direcoes, 0, False)
        return direcao if ok else None

    def filtrar_historico_clientes_juridicos(self):
        if hasattr(self,"checkbox_header_juridicos"):
            QMessageBox.warning(
                None,
                "Aviso",
                "Desmarque o checkbox antes de filtrar o histórico."
            )
            return
        
        # Criar a janela de filtro
        janela_filtro = QDialog(self)
        janela_filtro.setWindowTitle("Filtrar Histórico")
        layout = QVBoxLayout(janela_filtro)

        # Campo para inserir a data
        campo_data = QLineEdit()
        campo_data.setPlaceholderText("Digite a data no formato DD/MM/AAAA")
        
        # Conectar ao método de formatação, passando o texto
        campo_data.textChanged.connect(lambda: self.formatar_data(campo_data))


        # Campo para selecionar se quer o mais recente ou mais antigo (filtro por hora)
        grupo_hora = QGroupBox("Filtrar por Hora")
        layout_hora = QVBoxLayout(grupo_hora)

        radio_mais_novo = QRadioButton("Mais Recente")
        radio_mais_velho = QRadioButton("Mais Antigo")

        layout_hora.addWidget(radio_mais_novo)
        layout_hora.addWidget(radio_mais_velho)
        grupo_hora.setLayout(layout_hora)

        # Botão para aplicar o filtro
        botao_filtrar = QPushButton("Aplicar Filtro")
        botao_filtrar.clicked.connect(
            lambda: self.aplicar_filtro_clientes_juridicos(
                campo_data.text(),
                radio_mais_novo.isChecked(),
                radio_mais_velho.isChecked()
            )
        )

        # Adicionar widgets ao layout
        layout.addWidget(QLabel("Filtros Disponíveis"))
        layout.addWidget(campo_data)
        layout.addWidget(grupo_hora)
        layout.addWidget(botao_filtrar)

        # Exibir a janela de filtro
        janela_filtro.setLayout(layout)
        janela_filtro.exec()

    def formatar_data_clientes_juridicos(self, campo_data):
        # Obter o texto do campo de data
        texto_data = campo_data.text().replace("/", "")  # Remover as barras existentes
        texto_data = ''.join(filter(str.isdigit, texto_data))  # Permite apenas números

        # Verificar se há caracteres alfabéticos (letras)
        if any(char.isalpha() for char in texto_data):
            # Mostrar mensagem de erro caso haja letras
            QMessageBox.warning(self, "Erro", "Somente números são permitidos.")
            campo_data.clear()
            return  # Não aplica a formatação se houver letras

        # Limitar a entrada para no máximo 8 dígitos
        if len(texto_data) > 8:
            texto_data = texto_data[:8]

         # Formatar a data no formato DD/MM/AAAA
        if len(texto_data) >= 8:
            data_formatada = "{}/{}/{}".format(texto_data[:2], texto_data[2:4], texto_data[4:])  # DD/MM/AAAA
        elif len(texto_data) > 6:
            data_formatada = "{}/{}".format(texto_data[:2], texto_data[2:8])  # DD/MM
        else:
            data_formatada = texto_data[:8]  # Apenas o DD

        # Atualizar o texto do campo de data se houver mudança
        if campo_data.text() != data_formatada:
            campo_data.setText(data_formatada)  # Atualiza o texto do campo de data
            campo_data.setCursorPosition(len(data_formatada))  # Move o cursor para o final do texto

    def aplicar_filtro_clientes_juridicos(self, data, filtrar_novo, filtrar_velho):
        with sqlite3.connect('banco_de_dados.db') as cn:
            cursor = cn.cursor()

            query = "SELECT * FROM historico_clientes_juridicos"
            params = []

            # Filtrar pela data, se fornecida
            if data:
                try:
                    # Garantir que a data seja no formato correto (DD/MM/AAAA)
                    data_formatada = datetime.strptime(data, "%d/%m/%Y").strftime("%d/%m/%Y")  # Formato DD/MM/YYYY
                    query += " WHERE SUBSTR([Data e Hora], 1, 10) = ?"
                    params.append(data_formatada)
                except ValueError:
                    QMessageBox.warning(self, "Erro", "Data inválida. Use o formato DD/MM/AAAA.")
                    return

            # Ordenar por hora, se aplicável
            if filtrar_novo:
                query += " ORDER BY [Data e Hora] DESC LIMIT 1"
            elif filtrar_velho:
                query += " ORDER BY [Data e Hora] ASC LIMIT 1"

            # Executar a consulta
            cursor.execute(query, params)
            registros = cursor.fetchall()

        # Atualizar a tabela com os registros filtrados
        self.tabela_historico_clientes.clearContents()
        self.tabela_historico_clientes.setRowCount(len(registros))

        for i, row in enumerate(registros):
            self.tabela_historico_clientes.setItem(i, 0, QTableWidgetItem(row[0]))  # Data/Hora
            self.tabela_historico_clientes.setItem(i, 1, QTableWidgetItem(row[1]))  # Usuário
            self.tabela_historico_clientes.setItem(i, 2, QTableWidgetItem(row[2]))  # Ação
            self.tabela_historico_clientes.setItem(i, 3, QTableWidgetItem(row[3]))  # Descrição

        QMessageBox.information(self, "Filtro Aplicado", f"{len(registros)} registro(s) encontrado(s)!")
    
    def exportar_csv_juridicos(self):
        num_linhas = self.tabela_historico_clientes.rowCount()
        num_colunas = self.tabela_historico_clientes.columnCount()

        # Verificar se a tabela está vazia
        if self.tabela_historico_clientes.rowCount() == 0:
            QMessageBox.warning(self, "Aviso", "Nenhum histórico encontrado para gerar arquivo CSV.")
            return  # Se a tabela estiver vazia, encerra a função sem prosseguir

        nome_arquivo, _ = QFileDialog.getSaveFileName(
            self,
            "Salvar Arquivo CSV",
            "historico.csv",
            "Arquivos CSV (*.csv)"

        )

        if not nome_arquivo:
            return
        
        #Criar o arquivo CSV
        try:
            with open(nome_arquivo, mode="w",newline="",encoding="utf-8-sig") as arquivo_csv:
                escritor = csv.writer(arquivo_csv, delimiter=";")

                 # Adicionar cabeçalhos ao CSV
                cabecalhos = [self.tabela_historico_clientes.horizontalHeaderItem(col).text() for col in range (num_colunas)]
                escritor.writerow(cabecalhos)

                # Adicionar os dados da tabela ao CSV
                for linha in range(num_linhas):
                    dados_linhas = [
                        self.tabela_historico_clientes.item(linha, col).text() if self.tabela_historico_clientes.item(linha, col) else ""
                        for col in range(num_colunas)

                    ]
                    escritor.writerow(dados_linhas)

                    QMessageBox.information(self, "Sucesso", f"Arquivo CSV salvo com sucesso em:\n{nome_arquivo}")

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Falha ao salvar o arquivo CSV:\n{str(e)}")

    def exportar_excel_juridicos(self):
        num_linhas = self.tabela_historico_clientes.rowCount()
        num_colunas = self.tabela_historico_clientes.columnCount()

        # Verificar se a tabela está vazia
        if self.tabela_historico_clientes.rowCount() == 0:
            QMessageBox.warning(self, "Aviso", "Nenhum histórico encontrado para gerar arquivo Excel.")
            return  # Se a tabela estiver vazia, encerra a função sem prosseguir
        
        nome_arquivo, _ = QFileDialog.getSaveFileName(
            self,
            "Salvar Arquivo Excel",
            "historico.xlsx",
            "Arquivos Excel (*.xlsx)"

        )

        if not nome_arquivo:
            return
        
        # Garantir que o arquivo tenha extensão .xlsx
        if not nome_arquivo.endswith(".xlsx"):
            nome_arquivo += ".xlsx"

        # Criar uma lista para armazenar os dados da tabela
        dados = []


        for linha in range(num_linhas):
            linha_dados = []
            for coluna in range(num_colunas):
                item = self.tabela_historico_clientes.item(linha, coluna)
                linha_dados.append(item.text() if item else "") # Adicionar o texto ou vazio se o item for None
            dados.append(linha_dados)

        # Obter os cabeçalhos da tabela        
        cabecalhos = [self.tabela_historico_clientes.horizontalHeaderItem(coluna).text() for coluna in range (num_colunas)]

        try:
            # Criar um DataFrame do pandas com os dados e cabeçalhos
            df = pd.DataFrame(dados, columns=cabecalhos)

            # Exportar para Excel
            df.to_excel(nome_arquivo, index=False,engine="openpyxl")
            QMessageBox.information(self, "Sucesso",f"Arquivo Excel gerado com sucesso em: \n{nome_arquivo}")
        except Exception as e:
            QMessageBox.critical(self, "Erro",f"Erro ao salvar arquivo Excel: {str(e)}")

    def exportar_pdf_juridicos(self):
        num_linhas = self.tabela_historico_clientes.rowCount()
        num_colunas = self.tabela_historico_clientes.columnCount()

        # Verificar se a tabela está vazia
        if self.tabela_historico_clientes.rowCount() == 0:
            QMessageBox.warning(self, "Aviso", "Nenhum histórico encontrado para gerar arquivo PDF.")
            return  # Se a tabela estiver vazia, encerra a função sem prosseguir

        nome_arquivo, _ = QFileDialog.getSaveFileName(
            self,
            "Salvar Arquivo PDF",
            "historico.pdf",
            "Arquivos PDF (*.pdf)"
        )

        if not nome_arquivo:
            return

        # Garantir que o arquivo tenha extensão .pdf
        if not nome_arquivo.endswith(".pdf"):
            nome_arquivo += ".pdf"

        # Criar uma lista para armazenar os dados da tabela
        dados = []

        # Obter os cabeçalhos da tabela
        cabecalhos = [self.tabela_historico_clientes.horizontalHeaderItem(coluna).text() for coluna in range(num_colunas)]
        dados.append(cabecalhos)  # Adicionar os cabeçalhos como a primeira linha do PDF

        # Adicionar os dados da tabela
        for linha in range(num_linhas):
            linha_dados = []
            for coluna in range(num_colunas):
                item = self.tabela_historico_clientes.item(linha, coluna)
                linha_dados.append(item.text() if item else "")  # Adicionar o texto ou vazio se o item for None
            dados.append(linha_dados)

        try:
            # Criar o PDF
            pdf = SimpleDocTemplate(nome_arquivo, pagesize=landscape(letter))
            tabela = Table(dados)

            # Adicionar estilo à tabela
            estilo = TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Cabeçalho com fundo cinza
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Texto do cabeçalho branco
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Centralizar texto
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Fonte do cabeçalho
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Espaçamento inferior no cabeçalho
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  # Fundo das linhas de dados
                ('GRID', (0, 0), (-1, -1), 1, colors.black)  # Bordas da tabela
            ])
            tabela.setStyle(estilo)

            # Gerar o PDF
            pdf.build([tabela])
            QMessageBox.information(self, "Sucesso", f"Arquivo PDF gerado com sucesso em: \n{nome_arquivo}")

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao salvar arquivo PDF: {str(e)}")

    def pausar_historico_juridicos(self):
        # Criação da nova janela de histórico como QMainWindow
        self.janela_escolha = QMainWindow()
        self.janela_escolha.setWindowTitle("Pausar Histórico")
        self.janela_escolha.resize(255, 150)


        # Botão "Sim"
        botao_sim = QPushButton("Sim")
        botao_sim.clicked.connect(self.historico_ativo_juridicos)

        # Botão "Não"
        botao_nao = QPushButton("Não")
        botao_nao.clicked.connect(self.historico_inativo_juridicos)


        # Criação do layout e tabela para exibir o histórico
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # Texto centralizado
        label = QLabel("Deseja pausar o histórico?")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Alinha o texto ao centro

        layout.addWidget(label)  # Adiciona o texto centralizado
        layout.addWidget(botao_sim)
        layout.addWidget(botao_nao)

        self.janela_escolha.setCentralWidget(central_widget)
        self.janela_escolha.show()


    def historico_ativo_juridicos(self):
        # Atualiza o estado do histórico para ativo
        self.main_window.historico_pausado_clientes_juridicos = True  # Atualiza a variável no MainWindow
        QMessageBox.information(self, "Histórico", "O registro do histórico foi pausado.")
        self.janela_escolha.close()

    def historico_inativo_juridicos(self):
        # Atualiza o estado do histórico para inativo (continua registrando)
        self.main_window.historico_pausado_clientes_juridicos = False  # Atualiza a variável no MainWindow
        QMessageBox.information(self, "Histórico", "O registro do histórico continua ativo.")
        self.janela_escolha.close()
        

    def abrir_janela_relatorio_clientes_juridicos(self):
        self.janela_historico_clientes = QMainWindow()
        self.janela_historico_clientes.setWindowTitle("Relatório de Clientes Jurídicos")
        self.janela_historico_clientes.resize(800, 600)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        central_widget = QWidget()
        layout_principal = QVBoxLayout(central_widget)

        grupo_filtros = QGroupBox("Filtros do Relatório")
        layout_filtros = QFormLayout()

        self.combo_status = QComboBox()
        self.combo_status.addItems(["Todos", "Ativo", "Inativo", "Bloqueado", "Pendente"])
        layout_filtros.addRow("Status do Cliente:", self.combo_status)

        self.combo_categoria = QComboBox()
        layout_filtros.addRow("Categoria do Cliente:", self.combo_categoria)

        self.date_de = QDateEdit()
        self.date_de.setDate(QDate.currentDate().addMonths(-1))
        self.date_de.setCalendarPopup(True)

        self.date_ate = QDateEdit()
        self.date_ate.setDate(QDate.currentDate())
        self.date_ate.setCalendarPopup(True)

        layout_filtros.addRow("Última Compra - De:", self.date_de)
        layout_filtros.addRow("Última Compra - Até:", self.date_ate)

        self.combo_origem = QComboBox()
        layout_filtros.addRow("Origem do Cliente:", self.combo_origem)

        grupo_filtros.setLayout(layout_filtros)
        layout_principal.addWidget(grupo_filtros)

        self.carregar_opcoes_combo("Categoria do Cliente", self.combo_categoria)
        self.carregar_opcoes_combo("Origem do Cliente", self.combo_origem)

        grupo_campos = QGroupBox("Informações a Incluir no Relatório")
        layout_campos = QVBoxLayout()

        self.combo_selecionar_todos = QCheckBox("Selecionar Todos")
        self.combo_selecionar_todos.setChecked(True)
        self.combo_selecionar_todos.stateChanged.connect(self.selecionar_todos_checkboxes)
        layout_campos.addWidget(self.combo_selecionar_todos)

        checks = [
            "Nome", "Razão Social", "Data da Inclusão", "CNPJ",
            "Contato", "CEP", "Endereço", "Número", "Complemento", "Cidade", "Bairro", "Estado",
            "Status", "Categoria", "Última Atualização", "Origem",
            "Valor Gasto Total", "Última Compra"
        ]

        self.checkboxes_relatorio = []

        for texto in checks:
            check = QCheckBox(texto)
            check.setChecked(True)
            self.checkboxes_relatorio.append(check)
            layout_campos.addWidget(check)

        grupo_campos.setLayout(layout_campos)
        layout_principal.addWidget(grupo_campos)

        layout_botoes = QHBoxLayout()
        btn_gerar = QPushButton("Gerar Relatório em PDF")
        btn_gerar_excel = QPushButton("Gerar Relatório em Excel")
        btn_cancelar = QPushButton("Cancelar")

        layout_botoes.addStretch()
        layout_botoes.addWidget(btn_gerar)
        layout_botoes.addWidget(btn_gerar_excel)
        layout_botoes.addWidget(btn_cancelar)
        layout_principal.addLayout(layout_botoes)

        btn_cancelar.clicked.connect(self.janela_historico_clientes.close)
        btn_gerar.clicked.connect(self.gerar_pdf_clientes_juridicos)
        btn_gerar_excel.clicked.connect(self.gerar_excel_clientes_juridicos)

        scroll.setWidget(central_widget)
        self.janela_historico_clientes.setCentralWidget(scroll)
        self.janela_historico_clientes.show()
        
        configuracoes = Configuracoes_Login(self.main_window)
        if  configuracoes.nao_mostrar_mensagem_arquivo_excel:
            return
        
        # AVISO: Recomendação
        aviso = QMessageBox()
        aviso.setWindowTitle("Aviso")
        aviso.setIcon(QMessageBox.Information) # Ícone de aviso
        aviso.setText("Para uma melhor experiência recomendamos a geração do relatório em Excel.")
        aviso.setStandardButtons(QMessageBox.Ok)
        
        checkbox_nao_mostrar = QCheckBox("Não mostrar essa mensagem novamente")
        aviso.setCheckBox(checkbox_nao_mostrar)
        aviso.exec()

        # Verifica se o usuário marcou a opção para não mostrar novamente
        if checkbox_nao_mostrar.isChecked():
                configuracoes.nao_mostrar_mensagem_arquivo_excel = True # Define que o usuário não quer mais ver este aviso
                configuracoes.salvar(configuracoes.usuario,configuracoes.senha,configuracoes.mantem_conectado)


    def gerar_pdf_clientes_juridicos(self):
        status = self.combo_status.currentText()
        categoria = self.combo_categoria.currentText()
        origem = self.combo_origem.currentText()
        data_de = self.date_de.date().toPython()
        data_ate = self.date_ate.date().toPython()

        campos_selecionados = [
            checkbox.text()
            for checkbox in self.checkboxes_relatorio
            if checkbox.isChecked()
        ]

        if not campos_selecionados:
            QMessageBox.warning(None, "Aviso", "Selecione ao menos um campo para incluir no relatório.")
            return

        mapeamento_colunas = {
            "Nome": "Nome",
            "Razão Social": "Razão Social",
            "Data da Inclusão": "Data da Inclusão",
            "CNPJ": "CNPJ",
            "Contato": "Telefone",
            "CEP": "CEP",
            "Endereço": "Endereço",
            "Número": "Número",
            "Complemento": "Complemento",
            "Cidade": "Cidade",
            "Bairro": "Bairro",
            "Estado": "Estado",
            "Status": "Status",
            "Categoria": "Categoria",
            "Última Atualização": "Última Atualização",
            "Origem": "Origem",
            "Valor Gasto Total": "Valor Gasto Total",
            "Última Compra": "Última Compra"
        }

        colunas_sql = [f'"{mapeamento_colunas[nome]}"' for nome in campos_selecionados]
        sql = f"SELECT {', '.join(colunas_sql)} FROM clientes_juridicos WHERE 1=1 "

        params = []
        if status != "Todos":
            sql += " AND `Status do Cliente` = ?"
            params.append(status)
        if categoria != "Todos":
            sql += " AND `Categoria do Cliente` = ?"
            params.append(categoria)
        if origem != "Todos":
            sql += " AND `Origem do Cliente` = ?"
            params.append(origem)

        sql += """
            AND (
                `Última Compra` = 'Não Cadastrado' OR
                (
                    length(`Última Compra`) = 10 AND
                    substr(`Última Compra`, 3, 1) = '/' AND
                    substr(`Última Compra`, 6, 1) = '/' AND
                    substr(`Última Compra`, 7, 4) || '-' || 
                    substr(`Última Compra`, 4, 2) || '-' || 
                    substr(`Última Compra`, 1, 2)
                    BETWEEN ? AND ?
                )
            )
        """

        params.append(data_de.strftime("%Y-%m-%d"))
        params.append(data_ate.strftime("%Y-%m-%d"))

        try:
            conn = sqlite3.connect("banco_de_dados.db")
            cursor = conn.cursor()
            cursor.execute(sql, params)
            resultados = cursor.fetchall()
        except Exception as e:
            QMessageBox.critical(None, "Erro", f"Erro ao buscar dados: \n{e}")
            return

        if not resultados:
            QMessageBox.information(None, "Aviso", "Nenhum cliente encontrado com os filtros aplicados")
            return

        caminho_pdf, _ = QFileDialog.getSaveFileName(
            None,
            "Salvar Relatório",
            "relatorio_clientes_juridicos.pdf",
            "Arquivos PDF (*.pdf)"
        )

        if not caminho_pdf:
            return

        try:
            pdf = FPDF(orientation="L", format="A4")  # Cria um objeto PDF com orientação paisagem ("L") e tamanho A4
            pdf.set_left_margin(5) # Define as margens do PDF
            pdf.set_right_margin(5) # Define as margens do PDF
            pdf.add_page() # Adiciona uma página ao PDF, obrigatória antes de começar a escrever
            pdf.set_font("Arial", size=8) # Define a fonte para o texto:
            # Cria uma célula que ocupa toda a largura (0 = largura total da página),
            # com altura 10, com o texto "Relatório de Clientes Jurídicos",
            # quebra de linha após a célula (ln=True) e alinhamento centralizado
            pdf.cell(0, 10, "Relatório de Clientes Jurídicos", ln=True, align="C")
            pdf.ln(5) # Insere uma linha em branco com altura 5 para espaçamento vertical

            pdf.set_font("Arial", size=5) # tamanho da fonte
            cel_height = 5 # Define a altura das células que serão usadas para o cabeçalho da tabela


            larguras_automaticas = {}
            margem = 4  # margem interna da célula, para deixar texto mais confortável
            largura_minima = 10
            largura_maxima = 80  # máximo para evitar colunas absurdamente largas

            for i, campo in enumerate(campos_selecionados):
                # largura do cabeçalho
                largura_cabecalho = pdf.get_string_width(campo) + margem

                # largura máxima entre todos os textos daquela coluna
                largura_max = largura_cabecalho

                for linha in resultados:
                    item = linha[i]
                    texto = str(item) if item is not None else ""
                    largura_texto = pdf.get_string_width(texto) + margem
                    if largura_texto > largura_max:
                        largura_max = largura_texto

                # Limita largura para mínimo e máximo
                if largura_max < largura_minima:
                    largura_max = largura_minima
                elif largura_max > largura_maxima:
                    largura_max = largura_maxima

                larguras_automaticas[campo] = largura_max

            # Cabeçalho
            for campo in campos_selecionados:
                pdf.cell(larguras_automaticas[campo], cel_height, campo, border=1, align="C")
            pdf.ln()

            # Dados
            for linha in resultados:
                y_inicial = pdf.get_y()
                max_altura = cel_height
                for i, item in enumerate(linha):
                    campo = campos_selecionados[i]
                    largura = larguras_automaticas[campo]
                    texto = str(item) if item is not None else ""
                    x = pdf.get_x()
                    y = pdf.get_y()

                    # Usar multi_cell para texto que possa ter quebras, mas com largura suficiente para minimizar linhas
                    pdf.multi_cell(largura, cel_height, texto, border=1, align="L")
                    altura = pdf.get_y() - y
                    if altura > max_altura:
                        max_altura = altura
                    pdf.set_xy(x + largura, y)
                pdf.set_y(y_inicial + max_altura)
            pdf.output(caminho_pdf)
            QMessageBox.information(None, "Sucesso", "Relatório gerado com sucesso.")

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao gerar PDF:\n{e}")

    def gerar_excel_clientes_juridicos(self):
        status = self.combo_status.currentText()
        categoria = self.combo_categoria.currentText()
        origem = self.combo_origem.currentText()
        data_de = self.date_de.date().toPython()
        data_ate = self.date_ate.date().toPython()

        campos_selecionados = [
            checkbox.text()
            for checkbox in self.checkboxes_relatorio
            if checkbox.isChecked()
        ]

        if not campos_selecionados:
            QMessageBox.warning(None, "Aviso", "Selecione ao menos um campo para incluir no relatório.")
            return

        mapeamento_colunas = {
            "Nome": "Nome",
            "Razão Social": "Razão Social",
            "Data da Inclusão": "Data da Inclusão",
            "CNPJ": "CNPJ",
            "Contato": "Telefone",
            "CEP": "CEP",
            "Endereço": "Endereço",
            "Número": "Número",
            "Complemento": "Complemento",
            "Cidade": "Cidade",
            "Bairro": "Bairro",
            "Estado": "Estado",
            "Status": "Status",
            "Categoria": "Categoria",
            "Última Atualização": "Última Atualização",
            "Origem": "Origem",
            "Valor Gasto Total": "Valor Gasto Total",
            "Última Compra": "Última Compra"
        }

        colunas_sql = [f'"{mapeamento_colunas[nome]}"' for nome in campos_selecionados]
        sql = f"SELECT {', '.join(colunas_sql)} FROM clientes_juridicos WHERE 1=1 "

        params = []
        
        if status != "Todos":
            sql += " AND `Status do Cliente` = ?"
            params.append(status)
        if categoria != "Todos":
            sql += " AND `Categoria do Cliente` = ?"
            params.append(categoria)
        if origem != "Todos":
            sql += " AND `Origem do Cliente` = ?"
            params.append(origem)

        sql += """
            AND (
                `Última Compra` = 'Não Cadastrado' OR
                (
                    length(`Última Compra`) = 10 AND
                    substr(`Última Compra`, 3, 1) = '/' AND
                    substr(`Última Compra`, 6, 1) = '/' AND
                    substr(`Última Compra`, 7, 4) || '-' || 
                    substr(`Última Compra`, 4, 2) || '-' || 
                    substr(`Última Compra`, 1, 2)
                    BETWEEN ? AND ?
                )
            )
        """
        params.append(data_de.strftime("%Y-%m-%d"))
        params.append(data_ate.strftime("%Y-%m-%d"))

        try:
            conn = sqlite3.connect("banco_de_dados.db")
            cursor = conn.cursor()
            cursor.execute(sql, params)
            resultados = cursor.fetchall()
        except Exception as e:
            QMessageBox.critical(None, "Erro", f"Erro ao buscar dados: \n{e}")
            return

        if not resultados:
            QMessageBox.information(None, "Aviso", "Nenhum cliente encontrado com os filtros aplicados")
            return

        caminho_excel, _ = QFileDialog.getSaveFileName(
            None,
            "Salvar Relatório",
            "relatorio_clientes_juridicos.xlsx",
            "Arquivos Excel (*.xlsx)"
        )

        if not caminho_excel:
            return

        try:
            # Criar um DataFrame do pandas com os dados
            df = pd.DataFrame(resultados,columns=campos_selecionados)
            
            # Salva como Excel usando openpyxl
            sheet_name = "Relatório de Clientes Jurídicos"
            df.to_excel(caminho_excel,index=False,engine='openpyxl',sheet_name=sheet_name)
            
            # Reabre o Excel com openpyxl para aplicar formatações
            wb = load_workbook(caminho_excel)
            ws = wb[sheet_name]
            
            for col in ws.columns:
                max_length = 0
                col_letter = get_column_letter(col[0].column)
                for cell in col:
                    try:
                        if cell.value:
                            max_length = max(max_length,len(str(cell.value)))
                    except:
                        pass
                ws.column_dimensions[col_letter].width = max_length + 2  # Ajusta a largura da coluna    
            wb.save(caminho_excel)
            QMessageBox.information(None, "Sucesso", "Relatório Excel gerado com sucesso.")
        except Exception as e:
            QMessageBox.critical(None, "Erro", f"Erro ao gerar Excel:\n{e}")


    def selecionar_todos_checkboxes(self,estado):
        for checkbox in self.checkboxes_relatorio:
            checkbox.setChecked(bool(estado))

    def carregar_opcoes_combo(self, nome_coluna, combo_box):
        try:
            conn = sqlite3.connect("banco_de_dados.db")  # substitua com seu caminho
            cursor = conn.cursor()

            # Aspas duplas se o nome da coluna tiver espaços
            cursor.execute(f'''
                SELECT DISTINCT "{nome_coluna}"
                FROM clientes_juridicos
                WHERE "{nome_coluna}" IS NOT NULL AND "{nome_coluna}" != ''
            ''')
            resultados = cursor.fetchall()

            opcoes = sorted(set([row[0] for row in resultados]))
            combo_box.clear()
            combo_box.addItem("Todos")
            combo_box.addItems(opcoes)

        except Exception as e:
            print(f"Erro ao carregar opções de {nome_coluna}:", e)

    def confirmar_historico_apagado_clientes(self, mensagem):
        """
        Exibe uma caixa de diálogo para confirmar a exclusão.
        """
        msgbox = QMessageBox(self)
        msgbox.setWindowTitle("Confirmação")
        msgbox.setText(mensagem)

        btn_sim = QPushButton("Sim")
        btn_nao = QPushButton("Não")
        msgbox.addButton(btn_sim, QMessageBox.ButtonRole.YesRole)
        msgbox.addButton(btn_nao, QMessageBox.ButtonRole.NoRole)

        msgbox.setDefaultButton(btn_nao)
        resposta = msgbox.exec()

        return msgbox.clickedButton() == btn_sim
    