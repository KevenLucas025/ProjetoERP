from PySide6.QtWidgets import (QDialog, QPushButton, QVBoxLayout, QTableWidget, 
                               QTableWidgetItem, QMessageBox, QCheckBox, QLabel, QLineEdit, 
                               QLabel,QGridLayout,QFileDialog,QWidget,QHBoxLayout,
                               QComboBox,QDialogButtonBox,QHeaderView,QMainWindow)
from PySide6 import QtWidgets
from PySide6.QtGui import QPixmap, Qt
from PySide6.QtCore import QDate, Qt,QTimer
from database import DataBase, sqlite3
import base64
import locale
import pandas as pd
import openpyxl
import os
from datetime import datetime
from utils import Temas
import json


class TabelaProdutos(QMainWindow):
    def __init__(self, main_window, date_edit, parent=None):
        super().__init__(parent)
        self.main_window = main_window
        self.date_edit = date_edit
        self.edit_mode = False  # Inicializando o modo de edição como falso
        self.codigo_item_original = None
        self.filtragem_aplicada = False  # Inicializa a variável
        self.db = DataBase()  # Inicializando o atributo db
        self.temas = Temas()
        
        self.setWindowTitle("Tabela de Produtos")
        self.setMinimumWidth(800)
        self.setMinimumHeight(600)
    

        self.frame_valor_total_produtos = QtWidgets.QFrame()
        self.frame_valor_do_desconto = QtWidgets.QFrame()
        self.frame_valor_desconto = QtWidgets.QFrame()
        self.frame_quantidade = QtWidgets.QFrame()

        label_imagem_produto = None

        self.checkboxes = []  # Inicializa a lista de checkboxes

        # Inicialize a variável de estado
        self.todos_selecionados = False
        # Variável para rastrear se a coluna de checkboxes está visível
        self.coluna_checkboxes_produtos_adicionada = False


        cursor = None

        config = self.temas.carregar_config_arquivo()
        tema = config.get("tema", "claro")
        

        # Tabela para exibir os produtos
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(12)  # Definindo o número de colunas
        self.table_widget.setObjectName("tabelaProdutos")
        self.setStyleSheet(self.aplicar_tema(tema))
        self.table_widget.setHorizontalHeaderLabels(["ID", "Produto", "Quantidade", "Valor do Produto", 
                                                     "Desconto","Valor Total", "Data do Cadastro", "Código do Produto", 
                                                     "Cliente", "Descrição do Produto","Usuário","Status da Saída"])  # Definindo os rótulos das colunas
        
         # Widget central e layout principal vertical
        widget_central = QWidget()
        # Layout principal da janela
        layout = QVBoxLayout(widget_central)
        
        # Personalizar o estilo dos cabeçalhos de linha e coluna
        font = self.table_widget.horizontalHeader().font()
        self.table_widget.horizontalHeader().setFont(font)
        self.table_widget.verticalHeader().setFont(font)

        # Botão para apagar produto, dentro da tabela produtos
        self.btn_apagar_produto = QPushButton("Apagar Produto")
        layout.addWidget(self.btn_apagar_produto)

        self.btn_editar_produto = QPushButton("Atualizar Produto")
        layout.addWidget(self.btn_editar_produto)

        self.btn_filtrar_produtos = QPushButton("Filtrar Produtos")
        layout.addWidget(self.btn_filtrar_produtos)

        
        self.btn_ordenar_produtos = QPushButton("Ordenar Produtos")
        layout.addWidget(self.btn_ordenar_produtos)

        self.btn_visualizar_imagem = QPushButton("Visualizar Imagem")
        layout.addWidget(self.btn_visualizar_imagem)

        self.btn_atualizar_tabela_produtos = QPushButton("Atualizar Tabela")
        layout.addWidget(self.btn_atualizar_tabela_produtos)

        self.btn_gerar_excel = QPushButton("Gerar arquivo Excel")
        layout.addWidget(self.btn_gerar_excel)

        self.btn_duplicar_produto = QPushButton("Duplicar Produto")
        layout.addWidget(self.btn_duplicar_produto)

        self.checkbox_selecionar_produtos = QCheckBox("Selecionar")
        layout.addWidget(self.checkbox_selecionar_produtos)

        # Adicionar a tabela ao layout
        layout.addWidget(self.table_widget)
        
        # Definir o layout da janela
        self.setCentralWidget(widget_central)

        self.preencher_tabela_produtos()

        botoes = [
            self.btn_apagar_produto,
            self.btn_duplicar_produto,
            self.btn_gerar_excel,
            self.btn_atualizar_tabela_produtos,
            self.btn_visualizar_imagem,
            self.btn_ordenar_produtos,
            self.btn_filtrar_produtos,
            self.btn_editar_produto
        ]
        for btn in botoes:
            btn.setCursor(Qt.PointingHandCursor)
 

        self.btn_apagar_produto.clicked.connect(self.apagar_produto_confirmado)
        self.btn_editar_produto.clicked.connect(self.editar_produto_tabela)
        self.btn_filtrar_produtos.clicked.connect(self.filtrar_produtos)
        self.btn_ordenar_produtos.clicked.connect(self.ordenar_produtos)
        self.btn_visualizar_imagem.clicked.connect(self.visualizar_imagem)
        self.btn_atualizar_tabela_produtos.clicked.connect(self.atualizar_tabela_products)
        self.btn_duplicar_produto.clicked.connect(self.duplicar_produto)
        self.btn_gerar_excel.clicked.connect(self.gerar_arquivo_excel)
        self.checkbox_selecionar_produtos.clicked.connect(self.selecionar_individual)


    def aplicar_tema(self, tema: str) -> str:
        # Definições de tema
        if tema == "escuro":
            bg_cor = "#202124"
            text_cor = "white"
            lineedit_bg = "#303030"

            button_style = """
                QPushButton {
                    border-radius: 8px;
                    background: qlineargradient(
                        x1:0, y1:0, x2:0, y2:1,
                        stop:0 rgb(60, 60, 60),   /* topo */
                        stop:1 rgb(100, 100, 100) /* base */
                    );
                    font-size: 12px;
                    padding: 3px;
                }
                QPushButton:hover {
                    background-color: #444444;
                }
                QPushButton:pressed {
                    background-color: #555555;
                    border: 2px solid #888888;
                }
            """
            combobox_style = """
                QComboBox {
                    color: #f0f0f0;
                    border: 2px solid #ffffff;
                    border-radius: 6px;
                    padding: 4px 10px;
                    background-color: #2b2b2b;
                }
                QComboBox QAbstractItemView::item:hover {
                    background-color: #444444;
                    color: #f0f0f0;
                }
                QComboBox QAbstractItemView::item:selected {
                    background-color: #696969;
                    color: #f0f0f0;
                }
                QComboBox QAbstractItemView::item {
                    height: 24px;
                }
                QComboBox QScrollBar:vertical {
                    background: #ffffff;
                    width: 12px;
                    border-radius: 6px;
                }
                QComboBox QScrollBar::handle:vertical {
                    background: #555555;
                    border-radius: 6px;
                }
                
            """
            
            scroll_style = """
            /* Scrollbar vertical */
            QScrollBar:vertical {
                background: #ffffff;   /* fundo do track */
                width: 12px;
                margin: 0px;
                border-radius: 6px;
            }

            QScrollBar::handle:vertical {
                background: #555555;   /* cor do handle */
                border-radius: 6px;
                min-height: 20px;
            }

            QScrollBar::handle:vertical:hover {
                background: #777777;   /* hover no handle */
            }

            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical {
                background: none;
                height: 0px;
            }

            QScrollBar::add-page:vertical,
            QScrollBar::sub-page:vertical {
                background: none;
            }
            """
            table_view_style = """
             /* QTableView com seleção diferenciada */
            QTableView {
                background-color: #202124;
                color: white;
                gridline-color: #555555;
                selection-background-color: #7a7a7a;
                selection-color: white;
            }
            /* Coluna dos cabeçalhos */
            QHeaderView::section {
                background-color: #ffffff;
                color: black;
                border: 1px solid #aaaaaa;
                padding: 1px;
            }

            /* QTabWidget headers brancos */
            QTabWidget::pane {
                border: 1px solid #444444;
                background-color: #202124;
            }
            /* Estiliza a barra de rolagem horizontal */
            QTableView QScrollBar:horizontal {
                border: none;
                background-color: #ffffff;
                height: 12px;
                margin: 0px;
                border-radius: 5px;
            }

            /* Estiliza a barra de rolagem vertical */
            QTableView QScrollBar:vertical {
                border: none;
                background-color: #ffffff;  
                width: 12px;
                margin: 0px;
                border-radius: 5px;
            }

            /* QTabWidget headers brancos */
            QTabWidget::pane {
                border: 1px solid #444444;
                background-color: #202124;
            }
            /* Estiliza a barra de rolagem horizontal */
            QTableView QScrollBar:horizontal {
                border: none;
                background-color: none;
                height: 12px;
                margin: 0px;
                border-radius: 5px;
            }

            /* Estiliza a barra de rolagem vertical */
            QTableView QScrollBar:vertical {
                border: none;
                background-color: none; 
                width: 12px;
                margin: 0px;
                border-radius: 5px;
            }
            

            /* Parte que você arrasta */
            QTableView QScrollBar::handle:vertical {
                background-color: #777777;  /* cinza médio */
                min-height: 22px;
                border-radius: 5px;
            }

            QTableView QScrollBar::handle:horizontal {
                background-color: #777777;
                min-width: 22px;
                border-radius: 5px;
            }

            /* Groove horizontal */
            QTableView QScrollBar::groove:horizontal {
                background-color: transparent;
                border-radius: 5px;
                height: 15px;
                margin: 0px 10px 0px 10px;
            }

            /* Groove vertical */
            QTableView QScrollBar::groove:vertical {
                background-color: transparent;
                border-radius: 5px;
                width: 25px;
                margin: 10px 0px 10px 10px;
            }

            /* Estilo para item selecionado */
            QTableWidget::item:selected {
                background-color: #555555;  /* cinza de seleção */
                color: white;
            }
            /* CornerButton (canto superior esquerdo) */
            QTableCornerButton::section {
                background-color: #ffffff;
                border: 1px solid #aaaaaa;
                padding: 2px;
            }
            /* Forçar cor do texto do QCheckBox */
            QCheckBox {
                color: white;
            }

            """
            lineedit_style = f"""
                QLineEdit {{
                    background-color: {lineedit_bg};
                    color: {text_cor};
                    border: 2px solid white;
                    border-radius: 6px;
                    padding: 3px;
                }}
            """
        elif tema == "claro":
            bg_cor = "white"
            text_cor = "black"
            lineedit_bg = "white"

            button_style = """
                QPushButton {
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                                stop:0 rgb(50,150,250),
                                                stop:1 rgb(100,200,255));
                    color: black;
                    border-radius: 8px;
                    font-size: 16px;
                    border: 2px solid rgb(50,150,250);
                    padding: 6px;
                }
                QPushButton:hover {
                    background-color: #e5f3ff;
                }
                QPushButton:pressed {
                    background-color: #cce7ff;
                    border: 2px solid #3399ff;
                }
            """
            combobox_style = """
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
                    border: 1px solid #ccc;
                    selection-background-color: #e5e5e5;
                    selection-color: black;
                }
                QComboBox QScrollBar:vertical {
                    background: #f5f5f5;
                    width: 12px;
                    border: none;
                }
                QComboBox QScrollBar::handle:vertical {
                    background: #cccccc;
                    min-height: 20px;
                    border-radius: 5px;
                }
                
            """
            scroll_style = """
                /* Scrollbar vertical */
                QScrollBar:vertical {
                    background: #f0f0f0;  /* trilho claro */
                    width: 12px;
                    margin: 0px;
                    border-radius: 6px;
                }

                QScrollBar::handle:vertical {
                    background: #b0b0b0;  /* cor do handle */
                    border-radius: 6px;
                    min-height: 20px;
                }

                QScrollBar::handle:vertical:hover {
                    background: #a0a0a0;  /* hover no handle */
                }

                QScrollBar::add-line:vertical,
                QScrollBar::sub-line:vertical {
                    background: none;
                    height: 0px;
                }

                QScrollBar::add-page:vertical,
                QScrollBar::sub-page:vertical {
                    background: none;
                }
                """
            table_view_style = """
                /* QTableView com seleção diferenciada */
                QTableView {
                    background-color: white;
                    color: black;
                    gridline-color: #cccccc;
                    selection-background-color: #d0e7ff;  /* azul claro */
                    selection-color: black;
                }

                /* Cabeçalhos da tabela */
                QHeaderView::section {
                    background-color: #eaeaea;
                    color: black;
                    border: 1px solid #cccccc;
                    padding: 2px;
                }

                /* QTabWidget */
                QTabWidget::pane {
                    border: 1px solid #cccccc;
                    background-color: white;
                }

                /* Scrollbars horizontais e verticais */
                QTableView QScrollBar:horizontal,
                QTableView QScrollBar:vertical {
                    background-color: #f0f0f0;
                    border: none;
                    height: 12px;
                    width: 12px;
                    margin: 0px;
                    border-radius: 5px;
                }

                /* Handle */
                QTableView QScrollBar::handle:vertical,
                QTableView QScrollBar::handle:horizontal {
                    background-color: #b0b0b0;
                    border-radius: 5px;
                    min-height: 22px;
                    min-width: 22px;
                }

                /* Groove */
                QTableView QScrollBar::groove:vertical {
                    background-color: transparent;
                    border-radius: 5px;
                    width: 25px;
                    margin: 10px 0px 10px 10px;
                }

                QTableView QScrollBar::groove:horizontal {
                    background-color: transparent;
                    border-radius: 5px;
                    height: 15px;
                    margin: 0px 10px 0px 10px;
                }

                /* Estilo para item selecionado */
                QTableWidget::item:selected {
                    background-color: #cce5ff;  /* azul leve */
                    color: black;
                }

                /* Botão de canto da tabela */
                QTableCornerButton::section {
                    background-color: #eaeaea;
                    border: 1px solid #cccccc;
                    padding: 2px;
                }

                /* Forçar cor do texto do QCheckBox */
                QCheckBox {
                    color: black;
                }
                """


            lineedit_style = """
                QLineEdit {
                    background-color: white;
                    color: black;
                    border: 2px solid rgb(50,150,250);
                    border-radius: 6px;
                    padding: 3px;
                }
            """
        else:  # clássico
            bg_cor = "rgb(0,80,121)"
            text_cor = "white"
            lineedit_bg = "white"

            button_style = """
                QPushButton {
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                                stop:0 rgb(0,120,180),
                                                stop:1 rgb(0,150,220));
                    color: white;
                    border-radius: 8px;
                    font-size: 16px;
                    border: 2px solid rgb(0,100,160);
                    padding: 6px;
                }
                QPushButton:hover {
                    background-color: #007acc;
                }
                QPushButton:pressed {
                    background-color: #006bb3;
                    border: 2px solid #005c99;
                }
            """

            combobox_style = """
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
                QComboBox QScrollBar:vertical {
                    background: #f5f5f5;
                    width: 12px;
                    border: none;
                }
                QComboBox QScrollBar::handle:vertical {
                    background: #cccccc;
                    min-height: 20px;
                    border-radius: 5px;
                }
            """

            # 🔹 Scroll geral (scroll_style)
            scroll_style = """
                QScrollBar:vertical {
                    border: none;
                    background-color: rgb(255, 255, 255); /* branco */
                    width: 30px;
                    margin: 0px 10px 0px 10px;
                }
                QScrollBar::handle:vertical {
                    background-color: rgb(180, 180,180);  /* cinza */
                    min-height: 30px;
                    border-radius: 5px;
                }
            """

            # 🔹 Estilo específico para QTableView (table_view_style)
            table_view_style = """
                QTableView {
                    gridline-color: black;
                    color: white;
                    border: 1px solid white;
                    selection-color: white;
                }

                QTableView QScrollBar:horizontal {
                    border: none;
                    background-color: rgb(255, 255, 255);
                    height: 15px;
                    margin: 0px 10px 0px 10px;
                }

                QTableView QScrollBar:vertical {
                    border: none;
                    background-color: rgb(255, 255, 255); /* branco */
                    width: 35px;
                    margin: 0px 10px 0px 10px;
                }

                QTableView QScrollBar::handle:vertical {
                    background-color: rgb(180, 180,150);  /* cinza */
                    min-height: 30px;
                    border-radius: 5px;
                }

                QTableView QScrollBar::handle:horizontal{
                    background-color: rgb(180,180,150);
                    min-height: 30px;
                    border-radius: 5px;
                }

                QTableView QScrollBar::add-line:vertical,
                QTableView QScrollBar::sub-line:vertical {
                    height: 0px;
                    width: 0px;
                    border: none;
                    background: none;
                }

                QTableView QScrollBar::groove:horizontal {
                    background-color: rgb(100,240,240);
                    border-radius: 2px;
                    height: 15px;
                    margin: 0px 10px 0px 10px;
                }

                QTableWidget::item:selected {
                    background-color: rgb(0, 120, 215);
                    color: white;
                }
            """

            lineedit_style = """
                QLineEdit {
                    background-color: white;
                    color: black;
                    border: 2px solid rgb(50,150,250);
                    border-radius: 6px;
                    padding: 3px;
                }
            """

        estilo_completo = f"""
        QMainWindow {{
            background-color: {bg_cor};
        }}
        {button_style}
        {lineedit_style}
        {combobox_style}
        {table_view_style}
        {scroll_style}
        """
        return estilo_completo

#*******************************************************************************************************
    def preencher_tabela_produtos(self):
        # Limpar a tabela antes de preencher
        self.table_widget.setRowCount(0)

        # Conectar ao banco de dados
        db = DataBase()
        try:
            db.connecta()

            # Obter os produtos do banco de dados
            produtos = db.get_products()

            # Preencher a tabela com os dados dos produtos
            for produto in produtos:
                row_position = self.table_widget.rowCount()
                self.table_widget.insertRow(row_position)
                for col, data in enumerate(produto):
                    item = QTableWidgetItem(str(data))
                    self.table_widget.setItem(row_position, col, item)
            self.table_widget.resizeColumnsToContents()  # Ajustar as colunas para o conteúdo
            self.table_widget.resizeRowsToContents()  # Ajustar as linhas para o conteúdo

            # Verificar se a tabela está vazia
            if self.table_widget.rowCount() == 0:
                self.exibir_mensagem_sem_produtos()
            else:
                self.ocultar_mensagem_sem_produtos()

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao acessar o banco de dados: {str(e)}")
        finally:
            pass
#*******************************************************************************************************
    def exibir_mensagem_sem_produtos(self):
        # Verificar se a QLabel já existe
        if not hasattr(self, 'label_sem_produto'):
            self.label_sem_produto = QLabel("Produtos cadastrados serão exibidos aqui...")
            self.label_sem_produto.setAlignment(Qt.AlignCenter)
            self.label_sem_produto.setStyleSheet("font-size: 16px; color: black;")
            
            # Verificar se o widget tem um layout
            if not self.table_widget.layout():
                self.main_layout = QVBoxLayout(self.table_widget)
                self.table_widget.setLayout(self.main_layout)
            else:
                self.main_layout = self.table_widget.layout()

            self.main_layout.addWidget(self.label_sem_produto)

        self.label_sem_produto.show()
#*******************************************************************************************************
    def ocultar_mensagem_sem_produtos(self):
        # Oculta a mensagem caso existam produtos na tabela
        if hasattr(self, 'label_sem_produto'):
            self.label_sem_produto.hide()
#*******************************************************************************************************
    def recuperar_imagem_do_banco(self, produto_id):
        imagem_blob = None
        
        try:
            connection = self.db.connecta()
            if connection:
                cursor = connection.cursor()
                cursor.execute("SELECT Imagem FROM products WHERE id = ?", (produto_id,))
                result = cursor.fetchone()

                if result:
                    imagem_blob = result[0]
                else:
                    print(f"Imagem não encontrada para o produto: {produto_id}")
                    return None

        except Exception as e:
            print(f"Erro ao recuperar imagem do banco de dados: {str(e)}")
            return None

        if imagem_blob and isinstance(imagem_blob,str) and imagem_blob.strip().lower() != "não cadastrado":
            try:
                imagem_data = base64.b64decode(imagem_blob)
                return imagem_data  # Retorna bytes decodificados
                
            except Exception as e:
                print(f"Erro ao decodificar imagem: {str(e)}")
                return None
        else:
            print(f"Imagem não cadastrada ou inválida para o produto: {produto_id}")
            return None
#*******************************************************************************************************
    def atualizar_tabela_produtos_filtrada(self, produtos):
    # Limpar a tabela antes de preencher com os produtos filtrados
        self.table_widget.setRowCount(0)

        # Preencher a tabela com os produtos filtrados
        for produto in produtos:
            row_position = self.table_widget.rowCount()
            self.table_widget.insertRow(row_position)
            for col, data in enumerate(produto):
                item = QTableWidgetItem(str(data))
                self.table_widget.setItem(row_position, col, item)
#*******************************************************************************************************
    def obter_produtos_por_id(self, id):
        query = "SELECT * FROM products WHERE ID = ?"
        parameters = (id,)

        cursor = None  # Inicialize o cursor como None
        
        try:
            db = DataBase()  # Cria uma instância da classe DataBase
            connection = db.connecta()  # Obtemos uma conexão
            cursor = connection.cursor()  # Criamos um cursor a partir da conexão
            cursor.execute(query, parameters)
            
            produtos = cursor.fetchall()
            
            return produtos
        except Exception as e:
            print("Erro ao consultar produtos por ID:", e)
            return []
        finally:
            if cursor:
                cursor.close()  # Fechamos o cursor apenas se ele não for None
#*******************************************************************************************************          
    def obter_produtos_por_codigo(self, codigo):
        query = "SELECT * FROM products WHERE Código_Item = ?"
        parameters = (codigo,)

        cursor = None  # Inicialize o cursor como None
        
        try:
            db = DataBase()  # Cria uma instância da classe DataBase
            connection = db.connecta()  # Obtemos uma conexão
            cursor = connection.cursor()  # Criamos um cursor a partir da conexão
            cursor.execute(query, parameters)
            
            produtos = cursor.fetchall()
            
            return produtos
        except Exception as e:
            print("Erro ao consultar produtos por código:", e)
            return []
        finally:
            if cursor:
                cursor.close()  # Fechamos o cursor apenas se ele não for None
#*******************************************************************************************************
    def obter_produtos_por_nome(self, nome):
        query = "SELECT * FROM products WHERE Produto LIKE ?"
        parameters = (f"%{nome}%",)  # Usamos LIKE com % para fazer a consulta parcial

        cursor = None  # Inicialize o cursor como None
        
        try:
            db = DataBase()  # Cria uma instância da classe DataBase
            connection = db.connecta()  # Obtemos uma conexão
            cursor = connection.cursor()  # Criamos um cursor a partir da conexão
            cursor.execute(query, parameters)
            
            produtos = cursor.fetchall()
            
            return produtos
        except Exception as e:
            print("Erro ao consultar produtos:", e)
            return []
        finally:
            if cursor:
                cursor.close()  # Fechamos o cursor apenas se ele não for None
#*******************************************************************************************************
    def filtrar_produtos(self): 

        # Verificar se a tabela está vazia
        if self.table_widget.rowCount() == 0:
            QMessageBox.warning(self, "Aviso", "Nenhum produto cadastrado para filtrar.")
            return  # Se a tabela estiver vazia, encerra a função sem prosseguir
           
        # Criar um QDialog para a caixa de confirmação
        mensagem_box = QDialog(self)
        mensagem_box.setWindowTitle("Filtrar Produtos")
        
        layout = QVBoxLayout(mensagem_box)
        
        # Adiciona a mensagem de confirmação
        lbl_mensagem = QLabel("Deseja filtrar os produtos?", mensagem_box)
        layout.addWidget(lbl_mensagem)
        
        # Botões de Sim e Não com QDialogButtonBox
        botoes = QDialogButtonBox(QDialogButtonBox.StandardButtons(0), Qt.Horizontal, mensagem_box)
        
        botao_sim = botoes.addButton("Sim", QDialogButtonBox.AcceptRole)
        botao_nao = botoes.addButton("Não", QDialogButtonBox.RejectRole)
        
        layout.addWidget(botoes)
        
        # Funções para lidar com os cliques dos botões
        def on_sim():
            mensagem_box.accept()  # Fechar a caixa de diálogo
            self.abrir_criterio_dialog()  # Abrir o diálogo de critérios
        
        def on_nao():
            mensagem_box.reject()  # Fechar a caixa de diálogo
        
        botao_sim.clicked.connect(on_sim)
        botao_nao.clicked.connect(on_nao)
        
        # Executa a caixa de diálogo e espera pela resposta
        mensagem_box.exec()
#*******************************************************************************************************
    def abrir_criterio_dialog(self):
        # Criar um QDialog para a seleção do critério de filtragem
        criterio_dialog = QDialog(self)
        criterio_dialog.setWindowTitle("Escolha o Critério de Filtragem")
        
        layout = QVBoxLayout(criterio_dialog)
        
        # Criar e adicionar os botões de seleção de critério
        btn_nome = QPushButton("Filtrar pelo Nome do Produto", criterio_dialog)
        btn_id = QPushButton("Filtrar pelo ID", criterio_dialog)
        btn_codigo = QPushButton("Filtrar pelo Código do Item", criterio_dialog)
        
        # Botão de Voltar
        btn_voltar = QPushButton("Voltar", criterio_dialog)
        
        def selecionar_criterio(criterio):
            criterio_dialog.close()
            self.abrir_dialogo_filtro(criterio)
        
        def voltar():
            criterio_dialog.close()
            self.filtrar_produtos()  # Volta para a janela anterior
        
        btn_nome.clicked.connect(lambda: selecionar_criterio('nome'))
        btn_id.clicked.connect(lambda: selecionar_criterio('id'))
        btn_codigo.clicked.connect(lambda: selecionar_criterio('codigo'))
        btn_voltar.clicked.connect(voltar)
        
        layout.addWidget(btn_nome)
        layout.addWidget(btn_id)
        layout.addWidget(btn_codigo)
        layout.addWidget(btn_voltar)
        
        criterio_dialog.setLayout(layout)
        criterio_dialog.exec_()
#*******************************************************************************************************
    def abrir_dialogo_filtro(self, criterio):
        # Abre um diálogo para inserir o valor de filtragem com base no critério selecionado
        dialog = QDialog(self)
        dialog.setWindowTitle(f"Filtrar por {criterio.capitalize()}")
        
        layout = QVBoxLayout(dialog)
        
        # Label e campo de entrada baseado no critério
        lbl_criterio = QLabel(dialog)
        txt_criterio = QLineEdit(dialog)
        
        if criterio == 'nome':
            lbl_criterio.setText("Nome do Produto:")
        elif criterio == 'id':
            lbl_criterio.setText("ID do Produto:")
        elif criterio == 'codigo':
            lbl_criterio.setText("Código do Item:")
        
        layout.addWidget(lbl_criterio)
        layout.addWidget(txt_criterio)
        
        # Botão para aplicar o filtro
        btn_filtrar = QPushButton("Filtrar", dialog)
        
        # Botão de Voltar
        btn_voltar = QPushButton("Voltar", dialog)
        
        def aplicar_filtro():
            valor = txt_criterio.text()
            print(f"Filtrando por {criterio.capitalize()}: {valor}")
            
            if criterio == 'nome':
                produtos = self.obter_produtos_por_nome(valor)
            elif criterio == 'id':
                produtos = self.obter_produtos_por_id(valor)
            elif criterio == 'codigo':
                produtos = self.obter_produtos_por_codigo(valor)
            
            self.atualizar_tabela_produtos_filtrada(produtos)
            dialog.close()  # Fechar o diálogo de filtragem após aplicar o filtro
            self.filtragem_aplicada = True  # Marca que a filtragem foi aplicada
        
        def voltar():
            dialog.close()
            self.abrir_criterio_dialog()  # Volta para a janela anterior
        
        btn_filtrar.clicked.connect(aplicar_filtro)
        btn_voltar.clicked.connect(voltar)
        
        layout.addWidget(btn_filtrar)
        layout.addWidget(btn_voltar)
        
        dialog.setLayout(layout)
        dialog.exec()
#*******************************************************************************************************
    def atualizar_valores_frames_apos_recuperar(self, valor_total, valor_com_desconto, valor_do_desconto, quantidade):
        # Verificar e formatar os valores corretamente
        valor_total_formatado = locale.currency(valor_total, grouping=True)

        # Valor com desconto: se não houver desconto, mostrar "Sem desconto"
        valor_com_desconto_formatado = (
            "Sem desconto" if valor_do_desconto == 0 else locale.currency(valor_com_desconto, grouping=True)
        )

        # Valor do desconto: se for numérico e maior que 0, formatar
        if isinstance(valor_do_desconto, (int, float)) and valor_do_desconto > 0:
            valor_do_desconto_formatado = locale.currency(valor_do_desconto, grouping=True)
        else:
            valor_do_desconto_formatado = "Sem desconto"

        # Atualizar os textos das labels 
        self.main_window.label_valor_do_desconto.setText(valor_do_desconto_formatado)
        self.main_window.label_valor_desconto.setText(valor_com_desconto_formatado)
        self.main_window.label_quantidade.setText("{:.0f}".format(quantidade))
        self.main_window.label_valor_total_produtos.setText(valor_total_formatado)

        # Centralizar o texto dentro dos labels
        self.main_window.label_valor_total_produtos.setAlignment(Qt.AlignCenter)
        self.main_window.label_valor_do_desconto.setAlignment(Qt.AlignCenter)
        self.main_window.label_valor_desconto.setAlignment(Qt.AlignCenter)
        self.main_window.label_quantidade.setAlignment(Qt.AlignCenter)
#*******************************************************************************************************
    def apagar_produto_confirmado(self):
        produtos_para_remover = []
        linhas_para_remover = []

        # Verificar se a tabela está vazia
        if self.table_widget.rowCount() == 0:
            QMessageBox.warning(self, "Aviso", "Nenhum produto cadastrado para apagar.")
            return  # Se a tabela estiver vazia, encerra a função sem prosseguir

        # 1. Verificar checkboxes marcadas
        if self.coluna_checkboxes_produtos_adicionada:
            total_rows = self.table_widget.rowCount()
            for row in range(total_rows):
                if row < len(self.checkboxes):
                    checkbox = self.checkboxes[row]
                    if checkbox and checkbox.isChecked():
                        item_id = self.table_widget.item(row, 1)  # ID do produto (coluna 1)
                        nome_item = self.table_widget.item(row, 2)  # Nome do produto (coluna 2)

                        if item_id and nome_item:
                            produto_id = item_id.text().strip()
                            nome_produto = nome_item.text().strip()

                            print(f"Produto (checkbox) na linha {row + 1}: Nome = '{nome_produto}', ID = '{produto_id}'")  # Depuração

                            # Verificando se o ID do produto é um número válido
                            if produto_id.isdigit():  # Verifica se o ID é numérico
                                # Evitar duplicados entre seleção direta e checkboxes
                                if (int(produto_id), nome_produto) not in produtos_para_remover:
                                    produtos_para_remover.append((int(produto_id), nome_produto))
                                    linhas_para_remover.append(row)
                            else:
                                QMessageBox.warning(self, "Erro", f"ID inválido para o produto na linha {row + 1}. Esperado um número.")

        # 2. Verificar linhas selecionadas utilizando selectedIndexes, se não houver seleção por checkbox
        if not produtos_para_remover:  # Só verificar `selectedIndexes()` se não houver produtos selecionados via checkbox
            selecionados = self.table_widget.selectedIndexes()

            if selecionados:
                # Usando um conjunto para garantir que cada linha seja processada apenas uma vez
                linhas_selecionadas = set(index.row() for index in selecionados)

                for row in linhas_selecionadas:
                    item_id = self.table_widget.item(row, 0)  # ID do produto (coluna 1)
                    nome_item = self.table_widget.item(row, 1)  # Nome do produto (coluna 2)

                    if item_id and nome_item:
                        produto_id = item_id.text().strip()  # Pega o ID e remove espaços extras
                        nome_produto = nome_item.text().strip()

                        # Verificando se o ID do produto é um número válido
                        if produto_id.isdigit():  # Verifica se o ID é numérico
                            produtos_para_remover.append((int(produto_id), nome_produto))
                            linhas_para_remover.append(row)
                        else:
                            QMessageBox.warning(self, "Erro", f"ID inválido para o produto na linha {row + 1}: '{produto_id}'. Esperado um número.")
                    else:
                        QMessageBox.warning(self, "Erro", f"Produto na linha {row + 1} não tem dados válidos.")

        # 3. Validar se há produtos para remover
        if produtos_para_remover:
            num_produtos = len(produtos_para_remover)
            mensagem = "Você tem certeza que deseja apagar o produto selecionado?" if num_produtos == 1 else "Você tem certeza que deseja apagar os produtos selecionados?"

            # Criar a caixa de confirmação
            msgbox = QMessageBox(self)
            msgbox.setWindowTitle("Confirmar")
            msgbox.setText(mensagem)

            # Adicionar botões personalizados
            btn_sim = QPushButton("Sim")
            btn_nao = QPushButton("Não")
            msgbox.addButton(btn_sim, QMessageBox.ButtonRole.YesRole)
            msgbox.addButton(btn_nao, QMessageBox.ButtonRole.NoRole)

            msgbox.setDefaultButton(btn_nao)
            resposta = msgbox.exec()

            # Se o usuário confirmar a ação
            if msgbox.clickedButton() == btn_sim:
                db = DataBase()
                try:
                    db.connecta()
                    for produto_id, nome_produto in produtos_para_remover:
                        db.remover_produto(produto_id)

                        # Registrar no histórico após a remoção do produto
                        descricao = f"Produto {nome_produto} (ID: {produto_id}) foi removido."
                        self.main_window.registrar_historico("Remoção de Produto", descricao)

                    # Remover as linhas da tabela
                    for row in sorted(linhas_para_remover, reverse=True):
                        self.table_widget.removeRow(row)

                    # Sucesso
                    QMessageBox.information(self, "Sucesso", "Produtos removidos com sucesso!")

                except Exception as e:
                    QMessageBox.critical(self, "Erro", f"Erro ao remover os produtos: {str(e)}")
        else:
            QMessageBox.warning(self, "Aviso", "Nenhum produto selecionado para apagar.")

#*******************************************************************************************************
    def editar_produto_tabela(self):
        produto_id = None
        
        # Verificar se a tabela está vazia
        if self.table_widget.rowCount() == 0:
            QMessageBox.warning(self, "Aviso", "Nenhum produto cadastrado para atualizar.")
            return  # Se a tabela estiver vazia, encerra a função sem prosseguir

        # Verifica se a coluna de checkboxes está ativa
        if self.coluna_checkboxes_produtos_adicionada:
            produtos_selecionados = []
            total_rows = self.table_widget.rowCount()

            for row in range(total_rows):
                if row < len(self.checkboxes):
                    checkbox = self.checkboxes[row]
                    if checkbox is not None:  # Verifica se o checkbox ainda existe
                        try:
                            if checkbox.isChecked():
                                item = self.table_widget.item(row, 1) # Quando checkbox ativo, ID está na coluna 1
                                if item:
                                    produto_id = int(item.text())
                                    produtos_selecionados.append(produto_id)
                        except RuntimeError:
                            # O checkbox foi deletado, então ignore essa linha
                            continue

            if len(produtos_selecionados) > 1:
                QMessageBox.warning(None, "Erro", "Somente um produto por vez poderá ser editado.")
                return

            if len(produtos_selecionados) == 1:
                produto_id = produtos_selecionados[0]
            else:
                QMessageBox.warning(self, "Erro", "Nenhum produto selecionado para editar.")
                return
        else:
            if self.table_widget.currentRow() >= 0:
                row_index = self.table_widget.currentRow()
                produto_id = int(self.table_widget.item(row_index, 0).text())
            else:
                QMessageBox.warning(self, "Erro", "Nenhum produto selecionado para editar.")
                return

        imagem_data = self.recuperar_imagem_do_banco(produto_id)

        coluna_id = 1 if self.coluna_checkboxes_produtos_adicionada else 0
        coluna_nome = coluna_id + 1                  # Produto
        coluna_quantidade = coluna_nome + 1          # Quantidade
        coluna_valor = coluna_quantidade + 1         # Valor do Produto
        coluna_desconto = coluna_valor + 1           # Desconto
        # Pula coluna de Valor Total (frame separado)
        coluna_dateEdit = coluna_desconto + 2        # Data do Cadastro
        coluna_codigo_item = coluna_dateEdit + 1     # Código do Produto
        coluna_cliente = coluna_codigo_item + 1      # Cliente
        coluna_descricao = coluna_cliente + 1        # Descrição

        # Econtrar a linha onde está o produto id
        linha_produto = None
        for row in range(self.table_widget.rowCount()):
            item = self.table_widget.item(row, coluna_id)
            if item and item.text() == str(produto_id):
                linha_produto = row
                break
        if linha_produto is None:
            QMessageBox.warning(self, "Erro", f"Produto com ID {produto_id} não encontrado na tabela.")
            return
        # ATIVAR MODO DE EDIÇÃO AQUI
        self.main_window.is_editing_produto = True

        # Pegar os dados da linha selecionada
        produto_nome = self.table_widget.item(linha_produto, coluna_nome).text()
        produto_quantidade = self.table_widget.item(linha_produto, coluna_quantidade).text()
        produto_valor_real = self.table_widget.item(linha_produto, coluna_valor).text()
        produto_desconto = self.table_widget.item(linha_produto, coluna_desconto).text()
        produto_dateEdit = self.table_widget.item(linha_produto, coluna_dateEdit).text()
        produto_codigo_item = self.table_widget.item(linha_produto, coluna_codigo_item).text()
        produto_cliente = self.table_widget.item(linha_produto, coluna_cliente).text()
        produto_descricao = self.table_widget.item(linha_produto, coluna_descricao).text()

        
        # Tratar a conversão do desconto para evitar erro
        desconto_str = produto_desconto.replace('%', '').replace(',', '.').strip()
        # Se o desconto for "Sem desconto" ou vazio, define como 0.0 para cálculo
        if not desconto_str or not desconto_str.replace('.','').isdigit() or desconto_str.lower() == "sem desconto":
            desconto = 0.0
            desconto_exibicao = "Sem desconto"
        else:
            desconto = float(desconto_str)
            desconto_exibicao = f"{desconto}%"

        # Atualizar os campos visuais
        self.main_window.txt_desconto_3.setText(desconto_exibicao)

        # Armazenar o estado original do produto selecionado
        self.main_window.produto_selecionado = {
            "produto": produto_nome if produto_nome.strip() else "Não Cadastrado",
            "quantidade": int(produto_quantidade) if produto_quantidade.strip() else "Não Cadastrado",
            "valor_produto": float(produto_valor_real.replace('R$', '').replace('.', '').replace(',', '.').strip()) if produto_valor_real.strip() else "Não Cadastrado",
            "desconto": desconto if desconto else "Sem desconto", # Tratado como número para cálculos
            "data_cadastro": produto_dateEdit if produto_dateEdit.strip() else "Não Cadastrado",
            "codigo_item": produto_codigo_item if produto_codigo_item.strip() else "Não Cadastrado",
            "cliente": produto_cliente if produto_cliente.strip() else "Não Cadastrado",
            "descricao_produto": produto_descricao if produto_descricao.strip() else "Não Cadastrado",
            }
        
        self.main_window.produto_original = self.main_window.produto_selecionado.copy()

        self.main_window.txt_produto.setText(produto_nome)
        self.main_window.txt_quantidade.setText(produto_quantidade)
        self.main_window.txt_valor_produto_3.setText(produto_valor_real)
        self.date_edit.setDate(QDate.fromString(produto_dateEdit, "dd/MM/yyyy"))
        self.main_window.txt_codigo_item.setText(produto_codigo_item)
        self.main_window.txt_cliente_3.setText(produto_cliente)
        self.main_window.txt_descricao_produto_3.setText(produto_descricao)

        self.main_window.is_editing_produto = True
        self.codigo_item_original = produto_codigo_item
        self.main_window.produto_id = produto_id

        try:
            # Remover símbolo da moeda e converter para float
            valor_produto_str = produto_valor_real.replace('R$', '').replace('.', '').replace(',', '.').strip()
            if not valor_produto_str:
                self.main_window.txt_valor_produto_3.setText("Não Cadastrado")
                produto_valor_real = 0.0
            else:
                produto_valor_real = float(valor_produto_str)

            # Converter quantidade para inteiro
            quantidade_str = produto_quantidade.strip()
            if not quantidade_str:
                self.main_window.txt_quantidade.setText("Não Cadastrado")
                produto_quantidade = 0
            else:
                produto_quantidade = int(quantidade_str)

            # Converter desconto para float e tratá-lo como porcentagem
            desconto_str = produto_desconto.replace('%', '').replace(',', '.').strip()
            
            # Aqui, fazemos a conversão correta para percentual
            produto_desconto = float(desconto_str)  if desconto_str else 0

            # Calcular valores
            valor_total = produto_valor_real * produto_quantidade
            valor_desconto = valor_total * (produto_desconto / 100)
            valor_com_desconto = valor_total - valor_desconto

            # Atualizar os frames com os valores corretos
            self.atualizar_valores_frames_apos_recuperar(valor_total, valor_com_desconto, valor_desconto, produto_quantidade)

            # Registrar a edição no histórico
            descricao_edicao = f"Produto {produto_nome} foi editado. Novos valores: quantidade {produto_quantidade}, valor {produto_valor_real}, desconto {produto_desconto}%."
            self.main_window.registrar_historico("Edição de Produto", descricao_edicao)


            if imagem_data:
                try:
                    pixmap = QPixmap()
                    pixmap.loadFromData(imagem_data)

                    if pixmap.isNull():
                        QMessageBox.warning(self, "Aviso", "Não foi possível carregar a imagem.")
                        return
                    else:
                        print("Pixmap carregado com sucesso.")
                        print("Pixmap carregado pelo botão EDITAR: ", pixmap)

                    self.label_imagem = QLabel(self.main_window.frame_imagem_produto_3)
                    frame_size = self.main_window.frame_imagem_produto_3.size()
                    self.label_imagem.setFixedSize(frame_size.width(), frame_size.height())
                    pixmap = pixmap.scaled(self.label_imagem.width(), self.label_imagem.height(), Qt.KeepAspectRatio)
                    self.label_imagem.setPixmap(pixmap)
                    self.label_imagem.setAlignment(Qt.AlignCenter)
                    self.label_imagem.show()
                    self.label_imagem.repaint()

                except Exception as e:
                    print(f"Erro ao processar imagem: {str(e)}")
            else:
                print("Imagem não encontrada no banco de dados.")
                if self.main_window.frame_imagem_produto_3.layout():
                    old_layout = self.main_window.frame_imagem_produto_3.layout()
                    while old_layout.count():
                        item = old_layout.takeAt(0)
                        widget = item.widget()
                        if widget:
                            widget.deleteLater()
                self.main_window.frame_imagem_produto_3.setLayout(None)
            try:
                db = DataBase()
                db.connecta()
                cursor = db.connection.cursor()
                
                data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")
                
                cursor.execute("""
                    UPDATE clientes_juridicos
                    SET "Última Atualização" = ?
                    WHERE "Nome do Cliente" = ?
                """, (data_hora,produto_cliente))
                db.connection.commit()
                
            except Exception as e:
                print(f"Erro ao atualizar Última Atualização: {e}")
            self.accept()

        except ValueError as e:
            print(f"Erro ao converter valores: {str(e)}")
#*******************************************************************************************************
    def selecionar_todos(self):
        if not self.coluna_checkboxes_produtos_adicionada:
            self.selecionar_individual()
            return

        if not hasattr(self,"checkbox_header_produtos") or self.checkbox_header_produtos is None:
            return # evita o erro

        estado = self.checkbox_header_produtos.checkState()

        if estado == Qt.Unchecked and all(not cb.isChecked() for cb in self.checkboxes):
            self.selecionar_individual()
            return
        
        # Marca ou desmarca todos os checkboxes individuais de acordo com o estado do cabeçalho
        estado_checked = estado == Qt.Checked
        for checkbox in self.checkboxes:
            checkbox.blockSignals(True)
            checkbox.setChecked(estado_checked)
            checkbox.blockSignals(False)

#*******************************************************************************************************
    # Função para adicionar checkboxes selecionar_individual na tabela de histórico
    def selecionar_individual(self):
        if self.table_widget.rowCount() == 0:
            QMessageBox.warning(self, "Aviso", "Nenhum histórico para selecionar.")
            # Desmarca o checkbox visualmente
            if hasattr(self, "checkbox_selecionar_produtos") and isinstance(self.checkbox_selecionar_produtos, QCheckBox):
                QTimer.singleShot(0, lambda: self.checkbox_selecionar_produtos.setChecked(False))
            return

        # Se a coluna já está adicionada, remove-a
        if self.coluna_checkboxes_produtos_adicionada:
            # Remove sinais para evitar efeitos colaterais
            if hasattr(self, "checkbox_header_produtos") and self.checkbox_header_produtos:
                self.checkbox_header_produtos.blockSignals(True)

            # Remove a coluna
            self.table_widget.removeColumn(0)
            self.table_widget.verticalHeader().setVisible(True)
            self.coluna_checkboxes_produtos_adicionada = False

            # Remove o header checkbox
            if hasattr(self, "checkbox_header_produtos") and self.checkbox_header_produtos:
                self.checkbox_header_produtos.setParent(None)
                self.checkbox_header_produtos.deleteLater()
                self.checkbox_header_produtos = None

            # Limpa lista de checkboxes
            self.checkboxes.clear()
            return

        # Caso contrário, adiciona a coluna novamente
        self.table_widget.insertColumn(0)
        self.table_widget.setHorizontalHeaderItem(0, QTableWidgetItem(""))
        self.table_widget.setColumnWidth(0, 30)
        self.table_widget.horizontalHeader().setMinimumSectionSize(30)
        self.table_widget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)

        # Checkbox do cabeçalho
        header = self.table_widget.horizontalHeader()
        self.checkbox_header_produtos = QCheckBox(header.viewport())
        self.checkbox_header_produtos.setToolTip("Selecionar todos")
        self.checkbox_header_produtos.setChecked(False)
        self.checkbox_header_produtos.setStyleSheet("QCheckBox{background: transparent;}")
        self.checkbox_header_produtos.stateChanged.connect(self.selecionar_todos)
        self.checkbox_header_produtos.setFixedSize(20, 20)
        self.checkbox_header_produtos.show()

        # Aguarda o layout estar pronto para centralizar corretamente
        QTimer.singleShot(0, self.atualizar_posicao_checkbox_header_produtos)

        # Limpa lista de checkboxes e adiciona novos
        self.checkboxes.clear()
        for row in range(self.table_widget.rowCount()):
            checkbox = QCheckBox()
            checkbox.stateChanged.connect(self.atualizar_selecao_todos)

            container = QWidget()
            layout = QHBoxLayout(container)
            layout.addWidget(checkbox)
            layout.setAlignment(Qt.AlignCenter)
            layout.setContentsMargins(0, 0, 0, 0)

            self.table_widget.setCellWidget(row, 0, container)
            self.checkboxes.append(checkbox)

        self.table_widget.verticalHeader().setVisible(False)
        self.table_widget.horizontalScrollBar().valueChanged.connect(self.atualizar_posicao_checkbox_header_produtos)
        header.sectionResized.connect(self.atualizar_posicao_checkbox_header_produtos)
        header.geometriesChanged.connect(self.atualizar_posicao_checkbox_header_produtos)
        self.coluna_checkboxes_produtos_adicionada = True


    def atualizar_selecao_todos(self):
        self.checkbox_header_produtos.blockSignals(True)

        all_checked = all(checkbox.isChecked() for checkbox in self.checkboxes if checkbox)
        any_checked = any(checkbox.isChecked() for checkbox in self.checkboxes if checkbox)

        if all_checked:
            self.checkbox_header_produtos.setCheckState(Qt.Checked)
        elif any_checked:
            self.checkbox_header_produtos.setCheckState(Qt.PartiallyChecked)
        else:
            self.checkbox_header_produtos.setCheckState(Qt.Unchecked)

        self.checkbox_header_produtos.blockSignals(False)


    def atualizar_posicao_checkbox_header_produtos(self):
        if hasattr(self, "checkbox_header_produtos") and self.coluna_checkboxes_produtos_adicionada:
            header = self.table_widget.horizontalHeader()

            # largura da seção da coluna 0
            section_width = header.sectionSize(0)
            section_pos = header.sectionViewportPosition(0)

            # centralizar horizontalmente
            x = section_pos + (section_width - self.checkbox_header_produtos.width()) // 2 + 4

            # centralizar verticalmente
            y = (header.height() - self.checkbox_header_produtos.height()) // 2

            self.checkbox_header_produtos.move(x, y)


#*******************************************************************************************************
    def ordenar_produtos(self):
        # Verificar se a tabela está vazia
        if self.table_widget.rowCount() == 0:
            QMessageBox.warning(self, "Aviso", "Nenhum produto cadastrado para ordenar.")
            return  # Se a tabela estiver vazia, encerra a função sem prosseguir
        
        # Cria e exibe um QDialog para confirmação
        confirmar_dialogo = QDialog(self)
        confirmar_dialogo.setWindowTitle("Confirmar Ordenação")
        
        layout = QVBoxLayout(confirmar_dialogo)
        mensagem = QLabel("Você deseja ordenar os produtos?", confirmar_dialogo)
        layout.addWidget(mensagem)
        
        botoes = QDialogButtonBox(QDialogButtonBox.StandardButtons(0), Qt.Horizontal, confirmar_dialogo)
        
        botao_sim = botoes.addButton("Sim", QDialogButtonBox.AcceptRole)
        botao_nao = botoes.addButton("Não", QDialogButtonBox.RejectRole)
        
        layout.addWidget(botoes)
        
        botao_sim.clicked.connect(lambda: self.abre_dialogo_ordenacao(confirmar_dialogo))
        botao_nao.clicked.connect(confirmar_dialogo.reject)
        
        confirmar_dialogo.exec()

    def abre_dialogo_ordenacao(self, confirmar_dialogo):
        confirmar_dialogo.accept()
        
        # Cria e exibe um QDialog para escolher a ordenação
        ordenar_dialogo = QDialog(self)
        ordenar_dialogo.setWindowTitle("Escolher Ordenação")
        
        layout = QVBoxLayout(ordenar_dialogo)
        
        # Opções de ordenação
        ordenar_por_label = QLabel("Ordenar por:", ordenar_dialogo)
        layout.addWidget(ordenar_por_label)
        
        ordem_combo = QComboBox(ordenar_dialogo)
        ordem_combo.addItems(["A a Z", "Z a A", "Menor para Maior", "Maior para Menor"])
        layout.addWidget(ordem_combo)
        
        botoes = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, ordenar_dialogo)
        layout.addWidget(botoes)
        
        botoes.button(QDialogButtonBox.Ok).clicked.connect(lambda: self.aplicar_ordenacao(ordem_combo.currentText(), ordenar_dialogo))
        botoes.button(QDialogButtonBox.Cancel).clicked.connect(ordenar_dialogo.reject)
        
        ordenar_dialogo.exec()

    def aplicar_ordenacao(self, ordem, ordenar_dialogo):
        ordenar_dialogo.accept()
        
        ordem_map = {
            "A a Z": Qt.AscendingOrder,
            "Z a A": Qt.DescendingOrder,
            "Menor para o Maior": Qt.AscendingOrder,
            "Maior para o Menor": Qt.DescendingOrder
        }
        
        ordem = ordem_map.get(ordem, Qt.AscendingOrder)
        
        self.table_widget.sortItems(ordem)
#*******************************************************************************************************
    def visualizar_imagem(self):
        # Se a coluna de checkboxes está ativa, usar os checkboxes para saber os selecionados
        if self.coluna_checkboxes_produtos_adicionada:
            selecionados = [i for i, cb in enumerate(self.checkboxes) if cb.isChecked()]
        
            
            if not selecionados:
                QMessageBox.warning(self, "Aviso", "Nenhum produto selecionado para visualizar a imagem.")
                return
            
            if len(selecionados) > 1:
                QMessageBox.warning(self, "Aviso", "Só é possível visualizar a imagem de um produto por vez.")
                return
            
            row_index = selecionados[0]

        else:
            row_index = self.table_widget.currentRow()
            if row_index < 0:
                QMessageBox.warning(self, "Aviso", "Selecione um produto para visualizar a imagem.")
                return
            
        # Pega o ID da coluna correta (0 se não tiver coluna de checkbox, 1 se tiver)
        coluna_id = 1 if self.coluna_checkboxes_produtos_adicionada else 0
        item = self.table_widget.item(row_index, coluna_id)

        if item is None:
            QMessageBox.warning(self, "Erro", "Não foi possível identificar o ID do produto.")
            return
        try:
            produto_id = int(item.text())
        except ValueError:
            QMessageBox.warning(self, "Erro", "ID de produto inválido.")
            return

        imagem_data = self.recuperar_imagem_do_banco(produto_id)
            
        if imagem_data:
            try:
                print("Dados da imagem recuperados com sucesso para visualização.")
                
                pixmap = QPixmap()
                pixmap.loadFromData(imagem_data)
                
                if pixmap.isNull():
                    print("Aviso: pixmap é nulo")
                    QMessageBox.warning(self, "Aviso", "Não foi possível carregar a imagem.")
                    return
                else:
                    print("Pixmap carregado com sucesso para visualização.")


                # Salvar imagem temporariamente para visualização
                caminho_pasta = "imagens_temporarias"
                os.makedirs(caminho_pasta,exist_ok=True)  # Cria a pasta se não existir

                caminho_arquivo = os.path.join(caminho_pasta, "imagem_produto.png")

                with open(caminho_arquivo, 'wb') as f:
                    f.write(imagem_data)
                
                # Tentar abrir o arquivo com um visualizador de imagens padrão
                os.startfile(caminho_arquivo)
                
            except Exception as e:
                print(f"Erro ao processar imagem: {str(e)}")
        else:
            QMessageBox.warning(self, "Aviso", "Imagem não encontrada.")
#*******************************************************************************************************
    def obter_produtos_por_nome(self, nome):
        query = "SELECT * FROM products WHERE Produto LIKE ?"
        parameters = (f"%{nome}%",)  # Usamos LIKE com % para fazer a consulta parcial

        cursor = None  # Inicialize o cursor como None

        # Verificar se a tabela está vazia
        if self.table_widget.rowCount() == 0:
            QMessageBox.warning(self, "Aviso", "Nenhum produto cadastrado para ordenar.")
            return  # Se a tabela estiver vazia, encerra a função sem prosseguir
        
        try:
            db = DataBase()  # Cria uma instância da classe DataBase
            connection = db.connecta()  # Obtemos uma conexão
            cursor = connection.cursor()  # Criamos um cursor a partir da conexão
            cursor.execute(query, parameters)
            
            produtos = cursor.fetchall()
            
            return produtos
        except Exception as e:
            print("Erro ao consultar produtos:", e)
            return []
        finally:
            if cursor:
                cursor.close()  # Fechamos o cursor apenas se ele não for None
            db.close_connection()  # Fechamos a conexão usando a instância de DataBase
#*******************************************************************************************************
    def get_label_imagem(self):
        label_imagem = None
        for widget in self.main_window.frame_imagem_produto_3.children():
            if isinstance(widget, QLabel):
                label_imagem = widget
                break

        # Se não houver QLabel, criar um novo
        if label_imagem is None:
            label_imagem = QLabel(self.main_window.frame_imagem_produto_3)
            label_imagem.setObjectName("label_imagem_produto")

            # Adicionar o QLabel ao layout do frame, se houver
            layout = self.main_window.frame_imagem_produto_3.layout()
            if layout is None:
                layout = QVBoxLayout(self.main_window.frame_imagem_produto_3)
                self.main_window.frame_imagem_produto_3.setLayout(layout)

            layout.addWidget(label_imagem)
     

            # Definir tamanho do QLabel para ser o mesmo que o QFrame
            frame_size = self.main_window.frame_imagem_produto_3.size()
            label_imagem.resize(frame_size.size())


            # Ajustar o alinhamento da imagem no QLabel
            label_imagem.setAlignment(Qt.AlignCenter)
            label_imagem.setStyleSheet("background-color: red;")  # Adicionar um fundo temporário para debug

        return label_imagem
    
    def carregar_tabela_produtos(self):
        with sqlite3.connect('banco_de_dados.db') as cn:
            cursor = cn.cursor()
            cursor.execute('SELECT id, Produto, Quantidade, Valor_Real, Desconto, "Valor Total", "Data do Cadastro", '
                        'Código_Item, Cliente, Descrição_Produto, "Usuário" '
                        'FROM products ORDER BY id ASC')  # Ordem crescente

            registros = cursor.fetchall()

        self.table_widget.setSortingEnabled(False)  # Impede bagunça enquanto carrega
        self.table_widget.clearContents()
        self.table_widget.setRowCount(len(registros))

        deslocamento = 1 if self.coluna_checkboxes_produtos_adicionada else 0
        self.checkboxes = []  # Zera os checkboxes

        for i, (id, produto, quantidade, valor_real, desconto, valor_total, data_cadastro,
                codigo_item, cliente, descricao_produto, usuario) in enumerate(registros):

            if self.coluna_checkboxes_produtos_adicionada:
                checkbox = QCheckBox()
                checkbox.setStyleSheet("margin-left:9px; margin-right:9px;")
                self.table_widget.setCellWidget(i, 0, checkbox)
                self.checkboxes.append(checkbox)

            self.table_widget.setItem(i, 0 + deslocamento, QTableWidgetItem(str(id)))
            self.table_widget.setItem(i, 1 + deslocamento, QTableWidgetItem(produto))
            self.table_widget.setItem(i, 2 + deslocamento, QTableWidgetItem(str(quantidade)))
            self.table_widget.setItem(i, 3 + deslocamento, QTableWidgetItem(str(valor_real)))
            self.table_widget.setItem(i, 4 + deslocamento, QTableWidgetItem(str(desconto)))
            self.table_widget.setItem(i, 5 + deslocamento, QTableWidgetItem(str(valor_total)))  # Valor Total
            self.table_widget.setItem(i, 6 + deslocamento, QTableWidgetItem(data_cadastro))
            self.table_widget.setItem(i, 7 + deslocamento, QTableWidgetItem(codigo_item))
            self.table_widget.setItem(i, 8 + deslocamento, QTableWidgetItem(cliente))
            self.table_widget.setItem(i, 9 + deslocamento, QTableWidgetItem(descricao_produto))
            self.table_widget.setItem(i, 10 + deslocamento, QTableWidgetItem(usuario))

        # Agora sim: organiza pela coluna de ID (em ordem crescente)
        self.table_widget.sortItems(0 + deslocamento, Qt.AscendingOrder)
        self.table_widget.setSortingEnabled(True)


    def atualizar_tabela_products(self):
        QMessageBox.information(None, "Sucesso", "Dados carregados com sucesso!")
        self.carregar_tabela_produtos()

    def gerar_arquivo_excel(self):
        # Obtém o número de linhas e colunas da tabela
        num_linhas = self.table_widget.rowCount()
        num_colunas = self.table_widget.columnCount()

        # Verificar se a tabela está vazia
        if self.table_widget.rowCount() == 0:
            QMessageBox.warning(self, "Aviso", "Nenhum produto cadastrado para gerar arquivo excel.")
            return  # Se a tabela estiver vazia, encerra a função sem prosseguir

        # Extrai os dados da tabela para uma lista de listas
        dados = []
        for linha in range(num_linhas):
            linha_dados = []
            for coluna in range(num_colunas):
                item = self.table_widget.item(linha, coluna)
                linha_dados.append(item.text() if item else "")
            dados.append(linha_dados)

        # Obtém os cabeçalhos da tabela
        cabecalhos = []
        for coluna in range(num_colunas):
            cabecalho_item = self.table_widget.horizontalHeaderItem(coluna)
            cabecalhos.append(cabecalho_item.text() if cabecalho_item else "")

        # Cria um DataFrame do pandas com os dados da tabela
        df = pd.DataFrame(dados, columns=cabecalhos)

        # Abre um diálogo para salvar o arquivo
        caminho_arquivo, _ = QFileDialog.getSaveFileName(self, "Salvar Arquivo Excel", "Tabela Produtos", "Arquivo Excel (*.xlsx)")
        
        if caminho_arquivo:
            # Salva o DataFrame como um arquivo Excel
            df.to_excel(caminho_arquivo, index=False)
            QMessageBox.information(self,"Aviso","Arquivo excel gerado com sucesso")

    def duplicar_produto(self):
        # Verificar se há uma linha selecionada
        linha_selecionada = self.table_widget.currentRow()

        # Verificar se a tabela está vazia
        if self.table_widget.rowCount() == 0:
            QMessageBox.warning(self, "Aviso", "Nenhum produto cadastrado para duplicar.")
            return  # Se a tabela estiver vazia, encerra a função sem prosseguir
        
        if linha_selecionada == -1:
            # Se nenhuma linha estiver selecionada, mostrar um aviso
            QMessageBox.warning(self, "Aviso", "Nenhum produto selecionado para duplicar.")
            return

        # Obter os dados da linha selecionada
        dados_produto = []
        for coluna in range(self.table_widget.columnCount()):
            item = self.table_widget.item(linha_selecionada, coluna)
            dados_produto.append(item.text() if item is not None else "")

        # Adicionar uma nova linha na tabela
        linha_nova = self.table_widget.rowCount()
        self.table_widget.insertRow(linha_nova)

        # Preencher a nova linha com os dados duplicados
        for coluna, dado in enumerate(dados_produto):
            self.table_widget.setItem(linha_nova, coluna, QTableWidgetItem(dado))

        # Inserir o produto duplicado no banco de dados
        try:
            # Preparar os dados para inserção, omitindo o ID
            produto = dados_produto[1]  # Assumindo que o primeiro dado é o nome do produto
            quantidade = dados_produto[2]
            valor_real = dados_produto[3]
            desconto = dados_produto[4]
            data_cadastro = dados_produto[5]
            valor_total = dados_produto[6]
            codigo_item = dados_produto[7]
            cliente = dados_produto[8]
            descricao_produto = dados_produto[9]
            imagem = dados_produto[10] if len(dados_produto) > 8 else None

            # Inserir o produto no banco de dados usando a função do módulo database
            self.db.insert_product(produto, quantidade, valor_real, desconto, data_cadastro, 
                        valor_total,codigo_item, cliente, descricao_produto, imagem)

            # Exibir uma mensagem de sucesso
            QMessageBox.information(self, "Sucesso", "Produto duplicado e cadastrado com sucesso.")
        
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Falha ao cadastrar o produto: {str(e)}")



