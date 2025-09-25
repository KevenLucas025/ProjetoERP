from PySide6.QtWidgets import (QWidget,QMenu, QVBoxLayout, 
                               QProgressBar,QApplication,QDialog,QMessageBox,
                               QToolButton,QMainWindow,QPushButton,QLabel,
                               QLineEdit,QTableWidget,QTextEdit)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QIcon,QKeySequence,QColor,QBrush,QTextDocument
import os
import json
from login import Login
import sys
from configuracoes import Configuracoes_Login
from dialogos import ComboDialog,DialogoEstilizado
from mane_python import Ui_MainWindow
import subprocess
from html import escape

class Pagina_Configuracoes(QWidget):
    def __init__(self,
                main_window, paginas_sistemas, frame_botoes_navegacoes, centralwidget, 
                 frame_2, frame_page_estoque, frame_5, frame_cadastro_usuario,
                 pg_cadastro_usuario, btn_avancar, btn_retroceder, btn_opcoes, btn_home, btn_verificar_estoque,
                 btn_cadastrar_produto, btn_cadastro_usuario, btn_clientes,
                 btn_importar, btn_gerar_saida, btn_estorno, btn_abrir_planilha, line_excel,
                 label_cadastramento, label_cadastramento_produtos,frame_valor_total_produtos,
                 frame_valor_do_desconto, frame_valor_desconto,frame_quantidade,parent=None):
        super().__init__(parent)
        self.atalhos = {}  # dicionário para guardar atalhos
        self.main_window = main_window
        self.paginas_sistemas = paginas_sistemas
        self.frame_botoes_navegacoes = frame_botoes_navegacoes
        self.centralwidget = centralwidget
        self.frame_2 = frame_2
        self.frame_page_estoque = frame_page_estoque
        self.frame_5 = frame_5
        self.frame_cadastro_usuario = frame_cadastro_usuario
        self.pg_cadastro_usuario = pg_cadastro_usuario
        self.btn_avancar = btn_avancar
        self.btn_retroceder = btn_retroceder
        self.btn_opcoes = btn_opcoes
        self.btn_home = btn_home
        self.btn_verificar_estoque = btn_verificar_estoque
        self.btn_cadastro_usuario = btn_cadastro_usuario
        self.btn_clientes = btn_clientes
        self.btn_cadastrar_produto = btn_cadastrar_produto
        self.btn_abrir_planilha = btn_abrir_planilha
        self.btn_importar = btn_importar
        self.btn_gerar_saida = btn_gerar_saida
        self.btn_estorno = btn_estorno
        self.line_excel = line_excel
        self.label_cadastramento = label_cadastramento
        self.label_cadastramento_produtos = label_cadastramento_produtos
        self.frame_valor_total_produtos = frame_valor_total_produtos
        self.frame_valor_do_desconto = frame_valor_do_desconto
        self.frame_valor_desconto = frame_valor_desconto
        self.frame_quantidade = frame_quantidade
       
        self.estilo_original_classico = Ui_MainWindow()
        self.config = Configuracoes_Login(main_window=main_window)
        
        
        if self.config.tema == "escuro":
            self.aplicar_modo_escuro_sem_progress()
        elif self.config.tema == "claro":
            self.aplicar_modo_claro_sem_progress()
        else:
            self.aplicar_modo_classico_sem_progress()
    

        self.line_excel.setObjectName("line_excel")


        layout_principal = QVBoxLayout(self)
        self.setLayout(layout_principal)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setTextVisible(True)
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                background-color: #eeeeee;
                border: 1px solid #aaaaaa;
                border-radius: 5px;
                height: 10px;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #4caf50;
                border-radius: 5px;
            }
        """)
        self.progress_bar.setValue(0)

        layout_principal.addWidget(self.progress_bar)
        layout_principal.addStretch()

    def aplicar_tema_escuro(self):
        # Estilo geral dos botões (modo escuro)
        style_sheet = """
            QMainWindow, QStackedWidget, QWidget {
                background-color: #202124;
                color: #ffffff;
            }
            /* Estiliza apenas o QTableView das tables abaixo */
            QTableView#table_ativos,
            QTableView#table_inativos,
            QTableView#table_base,
            QTableView#table_saida,
            QTableView#table_massa_usuarios,
            QTableView#table_massa_produtos,
            QTableView#table_clientes_juridicos,
            QTableView#table_clientes_fisicos {    
                gridline-color: white;
                border: 1px solid white;
                color: black;
                selection-color: white;
            }
            /* QTableView com seleção diferenciada */
            QTableView {
                background-color: #ffffff;
                color: black;
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
                background-color: #3a3a3a;  /* faixa mais clara */
                border-radius: 5px;
                height: 15px;
                margin: 0px 10px 0px 10px;
            }

            /* Groove vertical */
            QTableView QScrollBar::groove:vertical {
                background-color: #3a3a3a;
                border-radius: 5px;
                width: 25px;
                margin: 10px 0px 10px 10px;
            }

            /* Estilo para item selecionado */
            QTableWidget::item:selected {
                background-color: #555555;  /* cinza de seleção */
                color: white;
            }
            QTabWidget#tab_clientes_todos::pane {
                border: none;
            }
            
            QTabBar::tab {
                background-color: #ffffff; /* fundo branco */
                color: black;
                padding: 6px 12px;
                border: 1px solid #888888;
                border-bottom: none;
            }

            QTabBar::tab:selected {
                background-color: #d6d6d6;   /* cinza médio para destacar */
                color: black;                /* texto bem visível */
                font-weight: bold;           /* destaque no selecionado */
            }

            QTabBar::tab:hover {
                background-color: #f5f5f5;
            }
            
            QPushButton#btn_mostrar_senha{
                qproperty-icon: url("imagens/olho_branco.png");
                qproperty-iconSize: 16px 16px;
                background: transparent;
                border: none;  
            }
            QPushButton#btn_mostrar_senha::pressed{
                padding-left: 1px;
                padding-top: 1px;      
            }
            QPushButton#botao_lupa_juridicos,
            QPushButton#botao_lupa_fisicos {
                qproperty-icon: url("imagens/botao_lupa_branco.png");
                qproperty-iconSize: 16px 16px;
                background: transparent;
                border: none;
            }
            

            /* Botões gerais */
            QPushButton {
                border-radius: 8px;
                background: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgb(60, 60, 60),   /* topo */
                    stop:1 rgb(100, 100, 100) /* base */
                );      
                min-height: 24px;  /* Adicione esta linha */
            }

            QPushButton:hover {
                background-color: #444444;
            }

            QPushButton:pressed {
                background-color: #555555;
                border: 2px solid #888888;
            }
            /* Botões de menu principal */
            QPushButton#btn_home,
            QPushButton#btn_verificar_estoque,
            QPushButton#btn_verificar_usuarios,
            QPushButton#btn_cadastrar_produto,
            QPushButton#btn_cadastrar_usuarios,
            QPushButton#btn_clientes {
                border-radius: 8px;
                background: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgb(60, 60, 60),   /* topo */
                    stop:1 rgb(100, 100, 100) /* base */
                );
                color: #ffffff; /* texto branco */
                min-width: 130px;   /* largura mínima */
                min-height: 21px;   /* altura mínima */
            }

            QPushButton#btn_home:hover,
            QPushButton#btn_verificar_estoque:hover,
            QPushButton#btn_verificar_usuarios:hover,
            QPushButton#btn_cadastrar_produto:hover,
            QPushButton#btn_cadastrar_usuarios:hover,
            QPushButton#btn_clientes:hover{
                background: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgb(90, 90, 90),
                    stop:1 rgb(130, 130, 130)
                );
            }

            QPushButton#btn_home:pressed,
            QPushButton#btn_verificar_estoque:pressed,
            QPushButton#btn_verificar_usuarios:pressed,
            QPushButton#btn_cadastrar_produto:pressed,
            QPushButton#btn_cadastrar_usuarios:pressed,
            QPushButton#btn_clientes:pressed{
                background: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgb(50, 50, 50),
                    stop:1 rgb(80, 80, 80)
                );
            }
            /* Botão de login */
            QPushButton#btn_login {
                border-radius: 8px;
                width: 120px;   /* largura mínima */
                min-height: 21px;   /* altura mínima */
                background: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgb(60, 60, 60),   /* topo */
                    stop:1 rgb(100, 100, 100) /* base */
                );
            }
            QPushButton#btn_login:hover{
                background: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgb(90, 90, 90),
                    stop:1 rgb(130, 130, 130)
                );
            }
            /* Botão de login */
            QPushButton#btn_opcoes_extras {
                border-radius: 8px;
                width: 120px;   /* largura mínima */
                min-height: 21px;   /* altura mínima */
                background: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgb(60, 60, 60),   /* topo */
                    stop:1 rgb(100, 100, 100) /* base */
                );
            }
            QPushButton#btn_avancar,
            QPushButton#btn_retroceder{
                background: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgb(60, 60, 60),   /* topo */
                    stop:1 rgb(100, 100, 100) /* base */
                );
            
            }
            QPushButton#btn_avancar:hover,
            QPushButton#btn_retroceder:hover{
                background: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgb(90, 90, 90),
                    stop:1 rgb(130, 130, 130)
                ); 
            }
            QPushButton#btn_avancar:pressed,
            QPushButton#btn_retroceder:pressed{
                background: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgb(50, 50, 50),
                    stop:1 rgb(80, 80, 80)
                );
                border: 2px solid #888888;
            }

            /* Campos de entrada */
            QLineEdit#txt_senha,
            QLineEdit#txt_usuario {
                border: 2px solid #555555;      /* borda sutil em cinza escuro */
                border-radius: 5px;             /* bordas arredondadas */
                padding: 5px;                   /* espaçamento interno */
                background-color: #2e2e2e;      /* fundo escuro */
                color: #ffffff;                 /* texto branco */
            }
            /* Placeholder */
            QLineEdit#txt_usuario::placeholder,
            QLineEdit#txt_senha::placeholder {
                color: #bbbbbb;  /* placeholder cinza claro */
            }
            QLineEdit#line_excel_usuarios,
            QLineEdit#line_edit_massa_usuarios,
            QLineEdit#line_edit_massa_produtos,
            QLineEdit#line_excel,
            QLineEdit#line_excel_usuarios{
              color: #ffffff; /* texto branco */
                background-color: #202124; /* fundo escuro */
                border: 3px solid #ffffff; /* branco */
                border-radius: 13px; /* cantos arredondados */
                padding: 3px;
                selection-background-color: #3296fa; /* fundo da seleção */
                selection-color: #ffffff; /* texto da seleção */  
            }
            QLineEdit{
                color: #ffffff; /* texto branco */
                background-color: #202124; /* fundo escuro */
                border: 2px solid #ffffff; /* branco */
                border-radius: 6px; /* cantos arredondados */
                padding: 3px;
                selection-background-color: #3296fa; /* fundo da seleção */
                selection-color: #ffffff; /* texto da seleção */
            }

            QLineEdit::placeholderText {
                color: #bbbbbb; /* placeholder em cinza claro */
            }

            QComboBox#perfil_estado,
            QComboBox#perfil_usuarios{
                color: #f0f0f0;                 /* Texto claro */
                border: 2px solid #ffffff;      /* Borda branca */
                border-radius: 6px;
                padding: 4px 10px;
                background-color: #2b2b2b; /* Fundo do combobox */
            
            }
            QComboBox#perfil_estado QAbstractItemView::item:hover,
            QComboBox#perfil_usuarios QAbstractItemView::item:hover {
                background-color: #444444; /* Cor de fundo quando o mouse passa por cima */
                color: #f0f0f0;            /* Cor do texto quando o mouse passa por cima */
            }
            QComboBox#perfil_estado QAbstractItemView::item:selected,
            QComboBox#perfil_usuarios QAbstractItemView::item:selected {
                background-color: #696969; /* Fundo do item selecionado */
                color: #f0f0f0;            /* Texto do item selecionado */
            }


            /* Scroll dentro do menu suspenso */
            QComboBox#perfil_estado QAbstractItemView::item,
            QComboBox#perfil_usuarios QAbstractItemView::item {
                height: 24px; /* Altura de cada item */
            }

            /* Fundo da barra do  scroll */
            QComboBox#perfil_estado QScrollBar:vertical,
            QComboBox#perfil_usuarios QScrollBar:vertical {
                background: #ffffff;
                width: 12px;
                margin: 0px 0px 0px 0px;
                border-radius: 6px;
            }
            /* Barra do scroll na cor cinza */
            QComboBox#perfil_estado QScrollBar::handle:vertical,
            QComboBox#perfil_usuarios QScrollBar::handle:vertical {
                background: #555555;
                border-radius: 6px;
            }

            QToolButton{
                border-radius: 8px;
                background: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgb(60, 60, 60),
                    stop:1 rgb(100, 100, 100)
                );
                color: #ffffff;
                min-width: 120px;
                min-height: 30px;      
            }
            QToolButton:hover{
                background: qlineargradient(
                x1:0, y1:0, x2:0, y2:1,
                stop:0 rgb(90, 90, 90),
                stop:1 rgb(130, 130, 130)
            );
            }
            QToolButton:pressed {
                background: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgb(50, 50, 50),
                    stop:1 rgb(80, 80, 80)
                );
            }
            QToolButton#btn_opcoes_extras{
                border-radius: 10px;
                min-width: 21px;
                min-height: 21px;
            }
            QToolButton#btn_opcoes_extras::menu-indicator{
                image: none;
            }
    
            QMenu::item:selected {
                background-color: #696969;
                color: white;
            }

            /* Frames com valores */
            QFrame#frame_valor_total_produtos,
            QFrame#frame_valor_do_desconto,
            QFrame#frame_valor_com_desconto1,
            QFrame#frame_quantidade {
                background: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 #3a3b3e,   /* topo mais claro */
                    stop:1 #2a2b2e    /* base mais escura */
                );
                color: #ffffff;
                border: 1px solid #444444;
                border-radius: 10px;
            }
            QLabel#label_titulo,
            QLabel#label_valor{
                font-size: 14px; color: white; 
                font-family: Arial; font-weight: normal;
                background: transparent;
            }
            QLabel#label_cadastramento_produtos,
            QLabel#label_cadastramento,
            QLabel#label_ativos,
            QLabel#label_inativos,
            QLabel#label_estoque,
            QLabel#label_saida{
                text-align: center; /* Centraliza o texto horizontalmente */
                vertical-align: middle; /* Centraliza o texto verticalmente */
                border: 3px solid white;
            }
            QMessageBox {
                background-color: #2b2b2b;   /* fundo escuro */
                color: #f0f0f0;              /* texto claro */
                border: 2px solid #555555;
                border-radius: 10px;
            }
            QMessageBox QLabel {
                color: #f0f0f0;              /* cor do texto */
                font-size: 14px;
                background: transparent;
            }
            QMessageBox QDialogButtonBox QPushButton {
                background-color: #444444;
                color: #ffffff;
                border-radius: 6px;
                padding: 4px 10px;
            }
            QMessageBox QDialogButtonBox QPushButton:hover {
                background-color: #666666;
            }
            QMessageBox QDialogButtonBox QPushButton:pressed {
                background-color: #888888;
            }

           QDialog{
                background-color: #2b2b2b;
           } 
           QLabel{
                background: transparent;
           }
           QDialog QPushButton {
                background-color: #444444;
                color: #ffffff;
                border-radius: 6px;
                padding: 4px 10px;
            }
            QDialog QPushButton:hover {
                background-color: #666666;    /* Hover do botão */
            }
            QDateEdit {
                color: white; 
                background-color: #3b3b3b;  /* fundo escuro */
                border: 2px solid #ffffff;
                border-radius: 5px;
                padding: 2px 5px;
            }

            QDateEdit QCalendarWidget {
                background-color: #2b2b2b;   /* fundo escuro do popup */
                border: 1px solid #555555;
            }

            QDateEdit QCalendarWidget QAbstractItemView:enabled {
                background-color: #2b2b2b;
                color: white;
                selection-background-color: #555555;
                selection-color: white;
            }

            QDateEdit QCalendarWidget QToolButton {
                color: white;   /* setas claras */
                min-width: 20px;     /* menor largura dos botões de navegação */
                min-height: 20px;    /* menor altura */
                padding: 1px;
                background: transparent;
            }

            QDateEdit QCalendarWidget QToolButton:hover {
                background: #444444;
            }

            QDateEdit QCalendarWidget QMenu {
                background-color: #3b3b3b;
                color: white;
            }

            QDateEdit QCalendarWidget QMenu::item:selected {
                background: #555555;
                color: white;
            }
            QDateEdit QCalendarWidget QToolButton::menu-indicator {
                image: none;   /* remove o ícone padrão */
                width: 0px;    /* remove o espaço reservado */
            }
            QProgressBar {
                color: white;                        /* texto branco */
                border: 3px solid #ffffff;           /* borda branca  */
                border-radius: 13px;                 /* bordas arredondadas */
                background-color: #202124;           /* fundo escuro */
                text-align: center;                   /* centraliza o texto do progresso */
            }

            QProgressBar::chunk {
                background-color: #4682b4;           /* azul do progresso preenchido */
                border-radius: 12px;                  /* mantém arredondado */
            }
            QFrame#frame_page_verificar_usuarios,
            QFrame#frame_pag_estoque,
            QFrame#frame_pg_clientes,
            QFrame#frame_10,
            QFrame#frame_8{
                border: 2px solid white;
            }
            QLabel#label_foto_sistema{
                border: none;
            }
            QFrame#frame_2 {
                border-radius: 12px;
                border: 2px solid qlineargradient(
                    spread:pad, 
                    x1:0, y1:0, x2:1, y2:0,
                    stop:0 #ff7f50;   /* laranja neon */
                    stop:1 #ffff00;   /* amarelo neon */
                );
            }



            
        """
        app = QApplication.instance()
        for widget in app.allWidgets():
            widget.setStyleSheet(style_sheet)

        self.btn_opcoes.setIcon(QIcon("imagens/imagens_modo_escuro/seta direita preta.png")) #Esse botão é o botão de retroceder, nomenclatura errada
        self.btn_retroceder.setIcon(QIcon("imagens/imagens_modo_escuro/seta esquerda preta.png")) # Esse botão é o botão avançar, nomenclatura errada
        

        self.btn_retroceder.setGeometry(40, 5, 30, 30)  # Define a geometria do botão 'btn_retroceder'


    def aplicar_modo_escuro(self):
        if self.config.tema == "escuro":
            QMessageBox.information(self, "Tema", "Você já está no modo Escuro.")
            return

        progress_dialog = ProgressDialog("Escuro", self)
        progress_dialog.show()

        def update_progress(value):
            progress_dialog.update_progress(value)

        update_progress(10)
        QTimer.singleShot(1000, lambda: update_progress(50))
        QTimer.singleShot(2000, lambda: update_progress(80))
        QTimer.singleShot(3000, lambda: update_progress(100))

        QTimer.singleShot(3000, lambda: self.finalizar_aplicacao_modo_escuro(progress_dialog))


    def finalizar_aplicacao_modo_escuro(self, progress_dialog):
        if self.config.tema == "escuro":
            # Já está no modo escuro, não precisa pedir reinício
            return
        if progress_dialog is not None:
            progress_dialog.accept()

        resposta = QMessageBox.question(
            None,
            "Reinício Necessário",
            "Para aplicar completamente o tema Escuro, é necessário reiniciar a aplicação.\nDeseja reiniciar agora?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No 
        )

        if resposta == QMessageBox.Yes:
            self.config.tema = "escuro"
            self.config.salvar(self.config.usuario, self.config.senha, self.config.mantem_conectado)
            self.reiniciar_sistema()
        else:
            QMessageBox.information(
                None,
                "Tema não aplicado",
                "O tema Escuro será aplicado apenas após a reinicialização."
            )

        

    # --- Modo escuro na inicialização (sem progress) ---
    def aplicar_modo_escuro_sem_progress(self):
        self.finalizar_aplicacao_modo_escuro(progress_dialog=None)

    def aplicar_modo_claro_sem_progress(self):
        self.finalizar_aplicacao_modo_claro(progress_dialog=None)

    def aplicar_modo_classico_sem_progress(self):
        self.finalizar_aplicacao_modo_classico(progress_dialog=None)

    def aplicar_tema_claro(self):
        style_sheet = """
            QMainWindow, QStackedWidget, QWidget {
                background-color: #ffffff;
                color: #000000;
            }
            /* QTableView com seleção diferenciada */
            QTableView {
                background-color: #ffffff;
                color: black;
                gridline-color: #cccccc;
                selection-background-color: #0078d7; /* azul Windows */
                selection-color: #ffffff;
                border: 1px solid #dddddd;
            }
            QTableView::item {
                color: black;
            }

            /* Cabeçalhos da tabela */
            QHeaderView::section {
                background-color: #f5f5f5;
                color: #000000;
                border: 1px solid #cccccc;
                padding: 4px;
            }

            /* Estilo para item selecionado */
            QTableWidget::item:selected {
                background-color: #0078d7; /* Azul moderno */
                color: #ffffff;
            }

            /* QTabWidget - modo claro */
            QTabWidget::pane {
                border: 1px solid #cccccc;
                background-color: #ffffff;
            }

            QTabWidget#tab_clientes_todos::pane {
                border: none;
            }

            /* Scrollbar horizontal */
            QTableView QScrollBar:horizontal {
                border: none;
                background-color: #f0f0f0;
                height: 12px;
                margin: 0px;
                border-radius: 5px;
            }

            /* Scrollbar vertical */
            QTableView QScrollBar:vertical {
                border: none;
                background-color: #f0f0f0;
                width: 12px;
                margin: 0px;
                border-radius: 5px;
            }

            /* Parte que você arrasta - Handle */
            QTableView QScrollBar::handle:vertical {
                background-color: #b0b0b0;  /* cinza claro */
                min-height: 22px;
                border-radius: 5px;
            }

            QTableView QScrollBar::handle:horizontal {
                background-color: #b0b0b0;
                min-width: 22px;
                border-radius: 5px;
            }

            /* Groove horizontal */
            QTableView QScrollBar::groove:horizontal {
                background-color: #e0e0e0;
                border-radius: 5px;
                height: 15px;
                margin: 0px 10px 0px 10px;
            }

            /* Groove vertical */
            QTableView QScrollBar::groove:vertical {
                background-color: #e0e0e0;
                border-radius: 5px;
                width: 15px;
                margin: 10px 0px 10px 0px;
            }
            QTableCornerButton::section {
                background-color: #f5f5f5;
                border: 1px solid #cccccc;
                padding: 2px;
            }


            QMessageBox {
                background: qlineargradient(
                    x1: 0, y1: 0,
                    x2: 0, y2: 1,
                    stop: 0 #ffffff,       /* branco puro no topo */
                    stop: 0.2 #f5f5f5,     /* branco acinzentado na faixa */
                    stop: 1 #c0c0c0       /* branco acinzentado no resto */
                );
                color: black;
            }
            QMessageBox QLabel{
                background: transparent;
                color: black
            }
            QMessageBox QPushButton {
                background-color: #ffffff;
                color: black;
                border: 1px solid #0078d7;
                padding: 2px 10px;
                border-radius: 6px;
                min-width: 40px;
                min-height: 10px; 
                font-size: 12px; 
            }
            
            QMessageBox QPushButton:hover {
                background-color: #e6f0fa;
            }

            QMessageBox QPushButton:pressed {
                background-color: #c7d7f9;
            }
            /* Botões gerais  */
            QPushButton {
                border-radius: 8px;
                background: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgb(220, 220, 220),  /* topo */
                    stop:1 rgb(245, 245, 245)   /* base */
                );
                font-size: 14px;
                color: #000000; /* texto escuro */
            }

            QPushButton:hover {
                background-color: #e0e0e0;
            }

            QPushButton:pressed {
                background-color: #d0d0d0;
                border: 2px solid #aaaaaa;
            }
            QPushButton#btn_login {
                font-size: 16px;
                border: 3px solid transparent;
            }

            QMenu {
                background-color: white;
                color: black;
                border: 1px solid gray;
            }

            QMenu::item {
                background-color: white;
                color: black;
            }

            QMenu::item:selected {
                background-color: #0078d7; /* Azul para item selecionado */
                color: white;
            }
            QMenu::separator {
                height: 1px;
                background: gray;
                margin: 5px 10px;
            }
            
            QPushButton#botao_lupa_juridicos,
            QPushButton#botao_lupa_fisicos {
                qproperty-icon: url("imagens/botao_lupa.png");
                qproperty-iconSize: 16px 16px;
                background: transparent;
                border: none;
            }
            QPushButton#btn_mostrar_senha{
                qproperty-icon: url("imagens/olho_preto.png");
                qproperty-iconSize: 16px 16px;
                background: transparent;
                border: none;  
            }
            QLineEdit#txt_usuario,
            QLineEdit#txt_senha{
                border: 2px solid #0078d4;  /* Cor da borda */
                border-radius: 5px;          /* Bordas arredondadas */
                padding: 5px;                /* Espaçamento interno */
                color: black
        
            }
            QLineEdit {
                color: #000000; /* texto preto */
                background-color: #ffffff; /* fundo branco */
                border: 2px solid #0078d4; /* azul moderno, como nos botões */
                border-radius: 6px;
                padding: 3px;
                selection-background-color: #cce4f7; /* azul claro na seleção */
                selection-color: #000000; /* texto preto na seleção */
            }

            QLineEdit::placeholderText {
                color: #888888; /* placeholder em cinza médio */
            }
            QLineEdit:focus {
                border: 2px solid #005a9e; /* Azul mais escuro ao focar */
                background-color: #f0f8ff; /* Leve destaque no fundo */
            }
            QLabel#label_estoque,
            QLabel#label_saida,
            QLabel#label_ativos,
            QLabel#label_inativos,
            QLabel#label_cadastramento_produtos,
            QLabel#label_cadastramento{
                border: 3px solid  #cccccc;
            }
            QComboBox#perfil_estado,
            QComboBox#perfil_usuarios {
                color: #2b2b2b;                 /* Texto escuro */
                border: 2px solid #0078d4;      /* Borda cinza clara */
                border-radius: 6px;
                padding: 4px 10px;
                background-color: #ffffff;      /* Fundo branco */
            }

            /* Hover em itens do dropdown */
            QComboBox#perfil_estado QAbstractItemView::item:hover,
            QComboBox#perfil_usuarios QAbstractItemView::item:hover {
                background-color: #f0f0f0;      /* Cinza muito claro ao passar o mouse */
                color: #000000;                 /* Texto preto */
            }

            /* Item selecionado no dropdown */
            QComboBox#perfil_estado QAbstractItemView::item:selected,
            QComboBox#perfil_usuarios QAbstractItemView::item:selected {
                background-color: #d0d0d0;      /* Cinza médio claro */
                color: #000000;                 /* Texto preto */
            }

            /* Altura dos itens */
            QComboBox#perfil_estado QAbstractItemView::item,
            QComboBox#perfil_usuarios QAbstractItemView::item {
                height: 24px;
            }

            /* Fundo da barra de scroll */
            QComboBox#perfil_estado QScrollBar:vertical,
            QComboBox#perfil_usuarios QScrollBar:vertical {
                background: #f0f0f0;            /* Cor de fundo do scroll */
                width: 12px;
                margin: 0px;
                border-radius: 6px;
            }

            /* Parte que você arrasta (scroll handle) */
            QComboBox#perfil_estado QScrollBar::handle:vertical,
            QComboBox#perfil_usuarios QScrollBar::handle:vertical {
                background: #b0b0b0;            /* Cinza claro */
                border-radius: 6px;
            }
            QToolButton {
                border-radius: 8px;
                background: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgb(220, 220, 220),  /* topo */
                    stop:1 rgb(245, 245, 245)   /* base */
                );
                color: #000000; /* texto escuro */
                min-width: 120px;
                min-height: 30px; 
        
            }
            QToolButton:hover {
                background-color: #e0e0e0;
            }

            QToolButton:pressed {
                background-color: #d0d0d0;
                border: 2px solid #aaaaaa;
            }
            QToolButton#btn_opcoes_extras{
                border-radius: 10px;
                min-width: 21px;
                min-height: 21px;
            }
            QToolButton#btn_opcoes_extras::menu-indicator{
                image: none;
            }
            QDateEdit {
                color: #2b2b2b;                     /* Texto escuro */
                background-color: #ffffff;         /* Fundo branco */
                border: 2px solid #0078d4;         /* Borda cinza clara */
                border-radius: 5px;
                padding: 2px 5px;
            }

            QDateEdit QCalendarWidget {
                background-color: #ffffff;         /* Fundo branco do calendário */
                border: 1px solid #cccccc;
            }

            QDateEdit QCalendarWidget QAbstractItemView:enabled {
                background-color: #ffffff;         /* Fundo branco da grade */
                color: #2b2b2b;                    /* Texto escuro */
                selection-background-color: #d0d0d0; /* Fundo do item selecionado */
                selection-color: #000000;          /* Texto do item selecionado */
            }

            QDateEdit QCalendarWidget QToolButton {
                color: #2b2b2b;                    /* Setas escuras */
                min-width: 20px;
                min-height: 20px;
                padding: 1px;
                background: transparent;
            }

            QDateEdit QCalendarWidget QToolButton:hover {
                background: #e0e0e0;               /* Hover em botão de navegação */
            }

            QDateEdit QCalendarWidget QMenu {
                background-color: #ffffff;         /* Fundo do menu */
                color: #2b2b2b;                    /* Texto do menu */
            }

            QDateEdit QCalendarWidget QMenu::item:selected {
                background: #d0d0d0;               /* Fundo item selecionado */
                color: #000000;                    /* Texto item selecionado */
            }
            QDateEdit QCalendarWidget QToolButton::menu-indicator {
                image: none;   /* remove o ícone padrão */
                width: 0px;    /* remove o espaço reservado */
            }
            QFrame#frame_valor_total_produtos,
            QFrame#frame_valor_do_desconto,
            QFrame#frame_valor_com_desconto1,
            QFrame#frame_quantidade{
                background-color: #d9d9d9;
                border-radius: 15px;
            
            }
            QLabel{
                background-color: transparent;
            }
            QProgressBar#progress_massa_produtos,
            QProgressBar#progress_massa_usuarios,
            QProgressBar#progress_excel_usuarios,
            QProgressBar#progress_excel{
                border-radius: 13px;
                text-align: center; /* centraliza o texto */
                font-size: 14px;
                color: #000000; /* texto escuro */
                background: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgb(220, 220, 220),  /* topo */
                    stop:1 rgb(245, 245, 245)   /* base */
                );
            }
            /* Parte preenchida da barra */
            QProgressBar#progress_massa_produtos::chunk,
            QProgressBar#progress_massa_usuarios::chunk,
            QProgressBar#progress_excel_usuarios::chunk,
            QProgressBar#progress_excel::chunk {
                border-radius: 13px;
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:0,
                    stop:0 #4caf50,  /* verde inicial */
                    stop:1 #81c784   /* verde mais claro no final */
                );
            }
            QFrame#frame_page_verificar_usuarios,
            QFrame#frame_pag_estoque,
            QFrame#frame_pg_clientes,
            QFrame#frame_10,
            QFrame#frame_8{
                border: 2px solid #eaeaea;
            }      
            QLabel#label_foto_sistema{
                border: none;
            }
            QFrame#frame_2 {
                border-radius: 12px;
                border: 2px solid qlineargradient(
                    spread:pad,
                    x1:0, y1:0, x2:1, y2:0,
                    stop:0 #36d1dc,   /* turquesa */
                    stop:1 #5b86e5    /* azul claro */
                );
            }

            
        """
        # Iterar sobre todos os widgets da aplicação e aplicar o estilo
        app = QApplication.instance()
        for widget in app.allWidgets():
            widget.setStyleSheet(style_sheet)
        
        # Salvar no JSON que o tema agora é claro
        self.config.tema = "claro"
        self.config.salvar(self.config.usuario, self.config.senha, self.config.mantem_conectado)


    def aplicar_modo_claro(self):
        if self.config.tema == "claro":
            QMessageBox.information(self, "Tema", "Você já está no modo Claro.")
            return
        progress_dialog = ProgressDialog("Claro", self)
        progress_dialog.show()

        def update_progress(value):
            progress_dialog.update_progress(value)

        update_progress(10)
        QTimer.singleShot(1000, lambda: update_progress(50))
        QTimer.singleShot(2000, lambda: update_progress(80))
        QTimer.singleShot(3000, lambda: update_progress(100))

        QTimer.singleShot(3000, lambda: self.finalizar_aplicacao_modo_claro(progress_dialog))

    def finalizar_aplicacao_modo_claro(self,progress_dialog):
        if self.config.tema == "claro":
            # Já está no modo classico, não precisa pedir reinício
            return
        if progress_dialog is not None:
            progress_dialog.accept()

        resposta = QMessageBox.question(
            None,
            "Reinício Necessário",
            "Para aplicar completamente o tema Claro, é necessário reiniciar a aplicação.\nDeseja reiniciar agora?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No 
        )

        if resposta == QMessageBox.Yes:
            self.config.tema = "claro"
            self.config.salvar(self.config.usuario, self.config.senha, self.config.mantem_conectado)
            self.reiniciar_sistema()
        else:
            QMessageBox.information(
                None,
                "Tema não aplicado",
                "O tema Clássico será aplicado apenas após a reinicialização."
            )


    def finalizar_aplicacao_modo_classico(self, progress_dialog):
        if self.config.tema == "classico":
            # Já está no modo classico, não precisa pedir reinício
            return
        if progress_dialog is not None:
            progress_dialog.accept()

        resposta = QMessageBox.question(
            None,
            "Reinício Necessário",
            "Para aplicar completamente o tema Clássico, é necessário reiniciar a aplicação.\nDeseja reiniciar agora?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No 
        )

        if resposta == QMessageBox.Yes:
            self.config.tema = "classico"
            self.config.salvar(self.config.usuario, self.config.senha, self.config.mantem_conectado)
            self.reiniciar_sistema()
        else:
            QMessageBox.information(
                None,
                "Tema não aplicado",
                "O tema Clássico será aplicado apenas após a reinicialização."
            )

    def aplicar_modo_classico(self):
        if self.config.tema == "classico":
            QMessageBox.information(self, "Tema", "Você já está no modo Clássico.")
            return
        progress_dialog = ProgressDialog("Clássico", self)
        progress_dialog.show()

        def update_progress(value):
            progress_dialog.update_progress(value)

        update_progress(10)
        QTimer.singleShot(1000, lambda: update_progress(50))
        QTimer.singleShot(2000, lambda: update_progress(80))
        QTimer.singleShot(3000, lambda: update_progress(100))

        QTimer.singleShot(3000, lambda: self.finalizar_aplicacao_modo_classico(progress_dialog))

    def aplicar_tema_classico(self):
        style_sheet = """
            QMainWindow, QStackedWidget, QWidget, QFrame {
                background-color: #005079;
                color: #ffffff;
            }
            QMessageBox {
                background: qlineargradient(
                    x1: 0, y1: 0,
                    x2: 0, y2: 1,
                    stop: 0 #ffffff,       /* branco puro no topo */
                    stop: 0.2 #f5f5f5,     /* branco acinzentado na faixa */
                    stop: 1 #c0c0c0       /* branco acinzentado no resto */
                );
                color: black;
            }
            QMessageBox QLabel{
                background: transparent;
                color: black
            }
            QMessageBox QPushButton {
                background-color: #ffffff;
                color: black;
                border: 1px solid #0078d7;
                padding: 2px 10px;
                border-radius: 6px;
                min-width: 40px;
                min-height: 10px; 
                font-size: 12px; 
            }
            
            QMessageBox QPushButton:hover {
                background-color: #e6f0fa;
            }

            QMessageBox QPushButton:pressed {
                background-color: #c7d7f9;
            }
            QMenu {
                background-color: white;
                color: black;
                border: 1px solid gray;
            }

            QMenu::item {
                background-color: white;
                color: black;
            }

            QMenu::item:selected {
                background-color: #0078d7; /* Azul para item selecionado */
                color: white;
            }

            QMenu::separator {
                height: 1px;
                background: gray;
                margin: 5px 10px;
            }

            QPushButton#botao_lupa_juridicos,
            QPushButton#botao_lupa_fisicos {
                qproperty-icon: url("imagens/botao_lupa.png");
                qproperty-iconSize: 16px 16px;
                background: transparent;
                border: none;
            }
            QPushButton#btn_mostrar_senha{
                qproperty-icon: url("imagens/olho_preto.png ");
                qproperty-iconSize: 16px 16px;
                background: transparent;
                border: none;  
            }
            QPushButton#btn_incluir_produto_sistema{
                font-size: 12px;
            }
            QPushButton{
                color: rgb(255, 255, 255);
                border-radius: 8px;
                font-size: 16px;
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */
                border: 4px solid transparent;
            }
            

            QPushButton:hover{
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                stop:0 rgb(100, 180, 255), 
                stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */
                color: black;
            }

            QPushButton#btn_opcoes_extras{
                color: rgb(255, 255, 255);
                border-radius: 10px;
                border:  transparent;
                background-color: rgb(100, 200, 255);
            }
            QPushButton#btn_login {
                font-size: 16px;
                border: 3px solid transparent;
            }
            QPushButton#btn_login:hover {
                color: black;
            }

            QLineEdit#txt_usuario,
            QLineEdit#txt_senha{
                border: 2px solid #0078d4;  /* Cor da borda */
                border-radius: 5px;          /* Bordas arredondadas */
                padding: 5px;                /* Espaçamento interno */
        
            }
            QLineEdit#txt_usuario,
            QLineEdit#txt_senha{
                color: black;  /* Cor do placeholder */
            }
            QLineEdit#line_clientes,
            QLineEdit#line_clientes_fisicos {
                color: black;
                background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */
                border: 2px solid rgb(50, 150,250); /* Borda azul */
                border-radius: 6px; /* Cantos arredondados */
                padding: 3px; /* Espaçamento interno */
            }

            QLineEdit#line_clientes::placeholderText,
            QLineEdit#line_clientes_fisicos::placeholderText {
                color: black; /* Cor do texto do placeholder */
            }
            QLineEdit#txt_nome,
            QLineEdit#txt_usuario_cadastro,
            QLineEdit#txt_senha_cadastro,
            QLineEdit#txt_confirmar_senha,
            QLineEdit#txt_cep,
            QLineEdit#txt_endereco,
            QLineEdit#txt_numero,
            QLineEdit#txt_cidade,
            QLineEdit#txt_bairro,
            QLineEdit#txt_complemento,
            QLineEdit#txt_telefone,
            QLineEdit#txt_email,
            QLineEdit#txt_data_nascimento,
            QLineEdit#txt_rg,
            QLineEdit#txt_cpf,
            QLineEdit#txt_cnpj,
            QLineEdit#txt_produto,
            QLineEdit#txt_quantidade,
            QLineEdit#txt_valor_produto_3,
            QLineEdit#txt_desconto_3,
            QLineEdit#txt_codigo_item,
            QLineEdit#txt_cliente_3,
            QLineEdit#txt_descricao_produto_3,
            QLineEdit#line_edit_massa_usuarios,
            QLineEdit#line_edit_massa_produtos,
            QLineEdit#line_excel_usuarios,
            QLineEdit#line_excel{
                color: black;
                background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */
                border: 2px solid rgb(50, 150, 250);  /* Borda azul */
                border-radius: 6px;                   /* Cantos arredondados */
                padding: 3px;                         /* Espaçamento interno */
            }

            QLineEdit#txt_nome::placeholderText,
            QLineEdit#txt_usuario_cadastro::placeholderText,
            QLineEdit#txt_senha_cadastro::placeholderText,
            QLineEdit#txt_confirmar_senha::placeholderText,
            QLineEdit#txt_cep::placeholderText,
            QLineEdit#txt_endereco::placeholderText,
            QLineEdit#txt_numero::placeholderText,
            QLineEdit#txt_cidade::placeholderText,
            QLineEdit#txt_bairro::placeholderText,
            QLineEdit#txt_complemento::placeholderText,
            QLineEdit#txt_telefone::placeholderText,
            QLineEdit#txt_email::placeholderText,
            QLineEdit#txt_data_nascimento::placeholderText,
            QLineEdit#txt_rg::placeholderText,
            QLineEdit#txt_cpf::placeholderText,
            QLineEdit#txt_cnpj::placeholderText,
            QLineEdit#txt_produto::placeholderText,
            QLineEdit#txt_quantidade::placeholderText,
            QLineEdit#txt_valor_produto_3::placeholderText,
            QLineEdit#txt_desconto_3::placeholderText,
            QLineEdit#txt_codigo_item::placeholderText,
            QLineEdit#txt_cliente_3::placeholderText,
            QLineEdit#line_edit_massa_usuarios::placeholderText,
            QLineEdit#line_edit_massa_produtos::placeholderText,
            QLineEdit#line_excel_usuarios::placeholderText,
            QLineEdit#line_excel::placeholderText,
            QLineEdit#txt_descricao_produto_3::placeholderText {
                color: black; /* Cor do texto do placeholder */
            }
                
            /* Estilo geral do QDateEdit */
            QDateEdit {
                color: black; 
                background-color: white; 
                border: 3px solid rgb(50,150,250);
                border-radius: 5px;
                padding: 2px 5px;
            }

            /* Remove o fundo das setas */
            QDateEdit::up-button, 
            QDateEdit::down-button {
                background: transparent;
                border: none;
            }

            /* Cor de fundo do calendário popup */
            QDateEdit QCalendarWidget {
                background-color: white;
                border: 1px solid rgb(150, 150, 150);
            }

            /* Dias normais */
            QDateEdit QCalendarWidget QAbstractItemView:enabled {
                background-color: white;
                color: black;
                selection-background-color: rgb(0, 120, 215); /* Azul no dia selecionado */
                selection-color: white;
            }
            /* Botões de navegação (setas) do calendário */
            QDateEdit QCalendarWidget QToolButton {
                background: transparent;   /* tira o fundo azul */
                color: black;              /* deixa as setas pretas */
                border: none;              /* sem borda */
                icon-size: 16px 16px;      /* ajusta o tamanho do ícone */
                padding: 2px;
            }
            QDateEdit QCalendarWidget QToolButton:hover {
                background: rgb(220, 220, 220); /* cinza claro no hover */
                border-radius: 4px;
            }
            /* Popup de meses/anos do calendário (QMenu) */
            QDateEdit QCalendarWidget QMenu {
                background-color: white;
                border: 1px solid #ccc;
                color: black;
            }

            QDateEdit QCalendarWidget QMenu::item {
                background: transparent;
                color: black;
                padding: 6px 16px;
            }

            QDateEdit QCalendarWidget QMenu::item:selected {
                background: rgb(0, 120, 215);
                color: white;
            }
            QDateEdit QCalendarWidget QToolButton::menu-indicator {
                image: none;   /* remove o ícone padrão */
                width: 0px;    /* remove o espaço reservado */
            }
                
            QComboBox { 
                background-color: white; 
                border:  2px solid rgb(50,150,250); 
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

            QTableView{
                gridline-color: black;
                color: black;
                selection-color: white;
                border: 2px solid white;
            }
            /* Cabeçalho das colunas */
            QHeaderView::section {
                color: black;
            }
            /* Estiliza a barra de rolagem horizontal */
            QTableView QScrollBar:horizontal {
                border: none;
                background-color: rgb(255, 255, 255);
                height: 10px;
                margin: 0px 10px 0px 10px;
            }
            QTableView QScrollBar::handle:horizontal{
                background-color: rgb(180,180,150);
                min-width: 10px;
                border-radius: 5px;
            }
            /* Estiliza a barra de rolagem vertical */
            QTableView QScrollBar:vertical {
                border: none;
                background-color: rgb(255, 255, 255); /* branco */
                width: 30px;
                margin: 0px 10px 0px 10px;
            }
            /* Parte que você arrasta */
            QTableView QScrollBar::handle:vertical {
                background-color: rgb(180, 180,150);  /* cinza */
                min-height: 26px;
                border-radius: 5px;
            }

            /* Remove os botões */
            QTableView QScrollBar::add-line:vertical,
            QTableView QScrollBar::sub-line:vertical {
                height: 0px;
                width: 0px;
                border: none;
                background: none;
            }

            QTableView QScrollBar::groove:horizontal{
                background-color: rgb(100,240,240);
                border-radius: 2px;
                height: 15px;
                margin: 0px 10px 0px 10px;
            }

            /* Estilo para item selecionado */
            QTableView::item:selected {
                background-color: rgb(0, 120, 215);
                color: white;
            }
            QTabBar::tab {
                color: black;  /* Cor do texto de todas as tabs */
                }
            QTabBar::tab:selected {
                color: black;
            }
            QTabBar#tb_base::tab {
                color: transparent; /* Esconde o texto */
                height: 1px;         /* Opcional: aba bem pequena */
                width: 1px;          /* Opcional: aba bem pequena */
            }
            QToolButton {
                background-color: rgb(50, 150, 250);
                color: white;
                border-radius: 5px;
                border: 2px solid rgb(50, 150, 250);
                padding: 5px 10px;
            }

            QToolButton:hover {
                background-color: rgb(100, 180, 255);
                border: 2px solid rgb(100, 180, 255);
            }
            

            /* Menu do btn_mais_opcoes */
            QToolButton#btn_mais_opcoes QMenu {
                background-color: white;     
                border: 1px solid #ccc;
                color: black;
            }

            /* Itens dentro desse menu */
            QToolButton#btn_mais_opcoes QMenu::item {
                background-color: transparent;
                color: black;
                padding: 6px 20px;
            }

            /* Item em hover/selecionado */
            QToolButton#btn_mais_opcoes QMenu::item:selected {
                background-color: rgb(0, 120, 215);
                color: white;
            }

            QFrame#frame_valor_total_produtos,
            QFrame#frame_valor_do_desconto,
            QFrame#frame_valor_com_desconto1,
            QFrame#frame_quantidade{
                background-color: rgb(100, 200, 100); 
                border-radius: 10px;
            }
            QLabel#label_titulo,
            QLabel#label_valor{
                font-size: 14px; color: white; 
                font-family: Arial; font-weight: normal;
                background: transparent;
            }
            QLabel#label_cadastramento_produtos,
            QLabel#label_cadastramento,
            QLabel#label_ativos,
            QLabel#label_inativos,
            QLabel#label_estoque,
            QLabel#label_saida{
                text-align: center; /* Centraliza o texto horizontalmente */
                vertical-align: middle; /* Centraliza o texto verticalmente */
                border: 3px solid white;
            }
            QProgressBar {
                color: black;
                border: 3px solid rgb(50,150,250);
                border-radius: 13px;  /* Aumentei o valor para deixar a borda mais redonda */
                background-color: #f0f0f0;  /* Cor cinza claro */
                min-height: 10px;  
            }

            QProgressBar::chunk {
                background-color: #4682b4;  /* Cor do progresso preenchido (azul) */
                border-radius: 12px;  /* Faz com que o progresso também tenha bordas arredondadas */
            }
            QToolButton#btn_classe_atalhos{
                font-size: 14px;
            
            }
            QToolButton#btn_classe_tema,
            QToolButton#btn_classe_atualizacoes,
            QToolButton#btn_classe_hora,
            QToolButton#btn_classe_fonte,
            QToolButton#btn_classe_notificacoes{
                color: rgb(255, 255, 255);
                border-radius: 8px;
                font-size: 16px;
                width: 120px;
                background: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgb(50, 150, 250),
                    stop:1 rgb(100, 200, 255)
                ); /* Gradiente de azul claro para azul mais claro */
                border: 4px solid transparent;
            }

            QToolButton#btn_classe_tema:hover,
            QToolButton#btn_classe_atualizacoes:hover,
            QToolButton#btn_classe_hora:hover,
            QToolButton#btn_classe_fonte:hover,
            QToolButton#btn_classe_notificacoes:hover,
            QToolButton#btn_classe_atalhos:hover {
                background: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgb(100, 180, 255),
                    stop:1 rgb(150, 220, 255)
                ); /* Gradiente de azul mais claro para azul ainda mais claro */
                color: black;
            }
            QToolButton#btn_opcoes_extras{
                border: transparent;
                border-radius: 10px;
                max-width: 21px;
                max-height: 21px;
                }
            QToolButton#btn_opcoes_extras::menu-indicator{
                image: none;
            }  
            QMenu#menu_classe_tema,
            QMenu#menu_classe_atualizacoes,
            QMenu#menu_classe_hora,
            QMenu#menu_classe_fonte,
            QMenu#menu_classe_notificacoes,
            QMenu#menu_classe_atalhos {
                background-color: white;
                color: black;
                border: 1px solid gray;
            }

            QMenu#menu_classe_tema::item:selected,
            QMenu#menu_classe_atualizacoes::item:selected,
            QMenu#menu_classe_hora::item:selected,
            QMenu#menu_classe_fonte::item:selected,
            QMenu#menu_classe_notificacoes::item:selected,
            QMenu#menu_classe_atalhos::item:selected {
                background-color: #0078d7;
                color: white;
            }
            QFrame#frame_page_verificar_usuarios,
            QFrame#frame_pag_estoque,
            QFrame#frame_10,
            QFrame#frame_8{
                border: 2px solid white;
            }  
            QLabel#label_foto_sistema{
                border: none;
                background: transparent;
            }
            QFrame#frame_2 {
                border-radius: 12px;
                border: 2px solid qlineargradient(
                    spread:pad, 
                    x1:0, y1:0, x2:1, y2:0,
                    stop:0 #1de9b6, 
                    stop:1 #0d47a1
                );
            } 
            
        """
        # Iterar sobre todos os widgets da aplicação e aplicar o estilo
        app = QApplication.instance()
        for widget in app.allWidgets():
            widget.setStyleSheet(style_sheet)
        
        # Salvar no JSON que o tema agora é clássico
        self.config.tema = "classico"
        self.config.salvar(self.config.usuario, self.config.senha, self.config.mantem_conectado)


    def configurar_menu_opcoes(self, parent_button):
        # Criar a janela de configurações
        self.janela_config = QMainWindow()
        self.janela_config.setWindowTitle("Configurações")
        self.janela_config.setMinimumSize(600, 500)
        
        # Aplica o style_sheet atual do sistema à janela de configurações
        self.janela_config.setStyleSheet(self.styleSheet())

        central = QWidget()
        layout = QVBoxLayout(central)
        self.janela_config.setCentralWidget(central)

        # ------------------- MENU TEMA -------------------
        btn_tema = QToolButton(self.janela_config)
        btn_tema.setText("Tema do Sistema")
        btn_tema.setPopupMode(QToolButton.InstantPopup)
        btn_tema.setToolButtonStyle(Qt.ToolButtonTextOnly)
        btn_tema.setCursor(Qt.PointingHandCursor)
        btn_tema.setObjectName("btn_classe_tema") 
        btn_tema.setFixedHeight(38)
        menu_tema = QMenu(self.janela_config)
        menu_tema.addAction("Modo escuro", self.aplicar_modo_escuro)
        menu_tema.addAction("Modo claro", self.aplicar_modo_claro)
        menu_tema.addAction("Modo clássico", self.aplicar_modo_classico)
        btn_tema.setMenu(menu_tema)
        layout.addWidget(btn_tema)

        # ------------------- BOTÃO ATUALIZAÇÕES -------------------
        btn_atualizacoes = QToolButton(self.janela_config)
        btn_atualizacoes.setText("Atualizações")
        btn_atualizacoes.setPopupMode(QToolButton.InstantPopup)
        btn_atualizacoes.setToolButtonStyle(Qt.ToolButtonTextOnly)
        btn_atualizacoes.setCursor(Qt.PointingHandCursor)
        btn_atualizacoes.setObjectName("btn_classe_atualizacoes")
        btn_atualizacoes.setFixedHeight(38)
        menu_atualizacoes = QMenu(self.janela_config)
        menu_atualizacoes.addAction("Definir atualizações automaticamente")
        menu_atualizacoes.addAction("Não definir atualizações automáticas")
        menu_atualizacoes.addAction("Verificar se há atualizações")
        menu_atualizacoes.addAction("Exibir histórico de atualizações")
        btn_atualizacoes.setMenu(menu_atualizacoes)
        layout.addWidget(btn_atualizacoes)


        # ------------------- MENU FONTE -------------------
        btn_fonte = QToolButton(self.janela_config)
        btn_fonte.setText("Fonte")
        btn_fonte.setPopupMode(QToolButton.InstantPopup)
        btn_fonte.setToolButtonStyle(Qt.ToolButtonTextOnly)
        btn_fonte.setCursor(Qt.PointingHandCursor)
        btn_fonte.setObjectName("btn_classe_fonte")
        btn_fonte.setFixedHeight(38)
        menu_fonte = QMenu(self.janela_config)
        # Lista de percentuais como no Windows
        percentuais = [100, 125, 150, 175, 200, 225]
        for p in percentuais:
            acao = menu_fonte.addAction(f"{p}%")
            acao.triggered.connect(lambda checked, x=p: self.main_window.definir_tamanho_fonte(x))
        
        btn_fonte.setMenu(menu_fonte)
        layout.addWidget(btn_fonte)

        # ------------------- MENU NOTIFICAÇÕES -------------------
        btn_notificacoes = QToolButton(self.janela_config)
        btn_notificacoes.setText("Notificações")
        btn_notificacoes.setPopupMode(QToolButton.InstantPopup)
        btn_notificacoes.setToolButtonStyle(Qt.ToolButtonTextOnly)
        btn_notificacoes.setCursor(Qt.PointingHandCursor)
        btn_notificacoes.setObjectName("btn_classe_notificacoes")
        btn_notificacoes.setFixedHeight(38)
        menu_notificacoes = QMenu(self.janela_config)
        menu_notificacoes.addAction("Definir notificação de boas-vindas")
        btn_notificacoes.setMenu(menu_notificacoes)
        layout.addWidget(btn_notificacoes)

        # ------------------- MENU ATALHOS -------------------
        btn_atalhos = QToolButton(self.janela_config)
        btn_atalhos.setText("Atalhos do Teclado")
        btn_atalhos.setPopupMode(QToolButton.InstantPopup)
        btn_atalhos.setToolButtonStyle(Qt.ToolButtonTextOnly)
        btn_atalhos.setCursor(Qt.PointingHandCursor)
        btn_atalhos.setObjectName("btn_classe_atalhos")
        btn_atalhos.setFixedHeight(38)
        menu_atalhos = QMenu(self.janela_config)
        menu_atalhos.addAction("Mapear teclas de atalhos",self.mapear_teclas_atalhos)
        menu_atalhos.addAction("Abrir painel de atalhos")
        menu_atalhos.addAction("Editar atalhos")
        menu_atalhos.addAction("Sobre atalhos")
        btn_atalhos.setMenu(menu_atalhos)
        layout.addWidget(btn_atalhos)

        # Mostrar janela
        self.janela_config.show()
        
    def mapear_teclas_atalhos(self):
        # 1. Perguntar qual ação o usuário quer mapear 
        opcoes = ["Pesquisar", "Fechar Sistema", "Abrir Mais Opções"] 
        dialog = ComboDialog("Mapear Teclas", "Escolha a ação que deseja mapear:", opcoes, parent=self.janela_config) 

        if dialog.exec() != QDialog.Accepted: 
            return  # usuário cancelou
        acao = dialog.escolha() 

        # 2. Abrir mini janela para capturar a tecla 
        captura = DialogoEstilizado(parent=self.janela_config) 
        captura.setWindowTitle(f"Definir atalho para {acao}") 

        layout = QVBoxLayout(captura) 
        layout.addWidget(QLabel(f"Pressione a tecla para '{acao}':")) 

        input_tecla = TeclaLineEdit() 
        layout.addWidget(input_tecla)

        btn_salvar = QPushButton("Salvar") 
        btn_salvar.clicked.connect(captura.accept) 
        layout.addWidget(btn_salvar)

        # Só entra aqui se o usuário clicar em "Salvar"
        if captura.exec() == QDialog.Accepted: 
            tecla = input_tecla.text().strip()
            if tecla:
                # garante que não salva vazio
                if not hasattr(self, "atalhos"): 
                    self.atalhos = {} 
                    self.atalhos[acao] = tecla 
                    print("Atalhos definidos:", self.atalhos)

                #  Salvar no JSON usando Configuracoes_Login
                self.config.salvar_atalho(acao,tecla)

                #  Registrar no sistema
                self.main_window.registrar_atalhos(acao,tecla)
    
    def abrir_painel_atalhos(self):
        print("Abrir painel de atalhos")

    def editar_atalhos(self):
        print("Editar atalhos")

    def sobre_atalhos(self):
        QMessageBox.information(
            self,
            "Sobre Atalhos",
            "Aqui você pode configurar os atalhos")
        
    def configurar_pesquisa(self):
        self.main_window.caixa_pesquisa.returnPressed.connect(self.executar_pesquisa)

    def executar_pesquisa(self):
        texto = self.main_window.caixa_pesquisa.text().strip().lower()
        diferenciar_maiusculas = self.main_window.checkbox_maiusculas.isChecked()

        self.resetar_destaques(self.main_window.centralWidget())

        if not texto:
            return

        pagina_atual = self.main_window.paginas_sistemas.currentWidget()  # <- só a página ativa
        encontrado = self.procurar_widget(pagina_atual, texto,diferenciar_maiusculas)

        if not encontrado:
            QMessageBox.warning(
                self,
                "Pesquisa",
                f"Nenhum resultado encontrado para: {texto}"
            )

    def procurar_widget(self, widget, texto,case_sensitive=False):
        """Percorre todos os widgets dentro da página atual e procura o texto"""
        encontrado = False

        if isinstance(widget, QLabel):
            conteudo = widget.text()

            '''if conteudo.strip().lower().startswith("<html>"):
                return False'''

            # salva o texto original no property (se ainda não tiver salvo)
            if widget.property("texto_original") is None:
                widget.setProperty("texto_original", conteudo)

            # Extrai apenas o texto visível (mesmo que conteudo_original seja HTML)
            doc = QTextDocument()
            doc.setHtml(conteudo)
            texto_visivel = doc.toPlainText()

            texto_sem_destaque  = conteudo
            conteudo_visivel = conteudo

            # comparar com ou sem distinção de maiúsculas
            if not case_sensitive:
                texto_base = texto_visivel.lower()
                texto_procura = texto.lower()
            else:
                texto_procura = texto
                texto_base = texto_visivel


            if texto_base in conteudo_visivel:
                start = conteudo_visivel.find(texto_base)
                end = start + len(texto)

                # escapa HTML para evitar quebra em letras soltas (ex: <b>, <i>, etc)
                conteudo_escapado = escape(texto_sem_destaque )

                destaque = (
                    conteudo_escapado[:start] +
                     f"<span style='background-color: yellow'>{escape(texto_sem_destaque [start:end])}</span>" +
                    conteudo_escapado[end:]
                )

                widget.setTextFormat(Qt.RichText)
                widget.setText(destaque)
                encontrado = True
            else:
                widget.setText(conteudo)

        elif isinstance(widget, QTableWidget):
            for row in range(widget.rowCount()):
                for col in range(widget.columnCount()):
                    item = widget.item(row, col)
                    if item:
                        item_texto = item.text()
                        item_texto_cmp = item_texto if case_sensitive else item_texto.lower()
                        texto_cmp = texto if case_sensitive else texto.lower()
                        if texto_cmp in item_texto_cmp:
                            item.setBackground(QColor("yellow"))
                            widget.scrollToItem(item)
                            encontrado = True
                        else:
                            item.setBackground(QColor())

        # Recursivamente percorre filhos
        for tipo in (QLabel, QLineEdit, QTextEdit, QTableWidget):
            for child in widget.findChildren(tipo):
                if self.procurar_widget(child, texto,case_sensitive):
                    encontrado = True

        return encontrado
    
    
    def resetar_destaques(self, widget):
        """Limpa todos os destaques e seleções de todos os widgets recursivamente"""

        if isinstance(widget, QLabel):
            # restaura texto original se existir
            texto_original = widget.property("texto_original")
            if texto_original is not None:
                widget.setText(texto_original)
                widget.setProperty("texto_original", None)

        elif isinstance(widget, (QLineEdit, QTextEdit)):
            widget.setStyleSheet("")  # remove fundo amarelo

        elif isinstance(widget, QTableWidget):
            for row in range(widget.rowCount()):
                for col in range(widget.columnCount()):
                    item = widget.item(row, col)
                    if item:
                        item.setBackground(QBrush())
            widget.clearSelection()

        # percorre todos os filhos recursivamente
        for child in widget.findChildren(QWidget):
            self.resetar_destaques(child)

    def fechar_pesquisa(self):
        """Fecha a barra de pesquisa e limpa todos os destaques"""
        # Garanta que o resetar_destaques seja chamado para a página atual
        pagina_atual = self.main_window.paginas_sistemas.currentWidget()
        if pagina_atual:
            self.resetar_destaques(pagina_atual)
        # Limpa a caixa de pesquisa
        self.main_window.caixa_pesquisa.clear()
        self.main_window.widget_pesquisa.hide()

        
    def reiniciar_sistema(self):
        python = sys.executable
        script = os.path.abspath(sys.argv[0])
        # Fecha o app atual
        QApplication.quit()
        # Reinicia com subprocess (mais robusto para caminhos com espaço)
        subprocess.Popen([python, script] + sys.argv[1:])
        sys.exit()


class ProgressDialog(QDialog):
    def __init__(self, tema="Escuro", parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"Aplicando Modo {tema}")
        self.setWindowModality(Qt.ApplicationModal)
        self.setFixedSize(300, 100)

        layout = QVBoxLayout(self)
        
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setTextVisible(True)
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                background-color: #eeeeee;
                border: 1px solid #aaaaaa;
                border-radius: 5px;
                height: 10px;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #4caf50;
                border-radius: 5px;
            }
        """)
        self.progress_bar.setValue(0)

        layout.addWidget(self.progress_bar)

    def update_progress(self, value):
        self.progress_bar.setValue(value)
        QApplication.processEvents()

class TeclaLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_unknown:
            return

        key = event.key()
        modifiers = event.modifiers()

        # Pega o valor inteiro do bitmask de modificadores
        seq_int = modifiers.value | key

        # Cria QKeySequence a partir do inteiro
        seq = QKeySequence(seq_int)

        # Mostra o atalho no QLineEdit
        self.setText(seq.toString(QKeySequence.NativeText))

        event.accept()