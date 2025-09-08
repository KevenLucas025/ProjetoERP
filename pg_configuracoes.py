from PySide6.QtWidgets import (QWidget,QMenu, QVBoxLayout, 
                               QProgressBar,QApplication,QDialog,QMessageBox,QToolButton,QMainWindow,QSizePolicy)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QIcon
import os
import json
from login import Login
import sys
from configuracoes import Configuracoes_Login
from mane_python import Ui_MainWindow

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
        if progress_dialog is not None:
            progress_dialog.accept()  # Oculta o diálogo de progresso


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
            QPushButton#btn_abrir_planilha,
            QPushButton#btn_abrir_planilha_usuarios{
                
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
            /* Item em hover/selecionado */
            QToolButton#btn_mais_opcoes QMenu::item:selected {
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

            
        """
        
         # Iterar sobre todos os widgets da aplicação e aplicar o estilo
        app = QApplication.instance()
        for widget in app.allWidgets():
            widget.setStyleSheet(style_sheet)

        self.btn_opcoes.setIcon(QIcon("imagens/imagens_modo_escuro/seta direita preta.png")) #Esse botão é o botão de retroceder, nomenclatura errada
        self.btn_retroceder.setIcon(QIcon("imagens/imagens_modo_escuro/seta esquerda preta.png")) # Esse botão é o botão avançar, nomenclatura errada
        

        self.btn_retroceder.setGeometry(40, 5, 30, 30)  # Define a geometria do botão 'btn_retroceder'

        # Salvar no JSON que o tema agora é escuro
        self.config.tema = "escuro"
        self.config.salvar(self.config.usuario, self.config.senha, self.config.mantem_conectado)
        

    # --- Modo escuro na inicialização (sem progress) ---
    def aplicar_modo_escuro_sem_progress(self):
        self.finalizar_aplicacao_modo_escuro(progress_dialog=None)

    def aplicar_modo_claro_sem_progress(self):
        self.finalizar_aplicacao_modo_claro(progress_dialog=None)

    def aplicar_modo_classico_sem_progress(self):
        self.finalizar_aplicacao_modo_classico(progress_dialog=None)


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
        if progress_dialog is not None:
            progress_dialog.accept()  # Oculta o diálogo de progresso

        style_sheet = """
            QMainWindow {
                background-color: #ffffff;
                color: #000000;
            }

            QToolButton {
                background-color: #f0f0f0;
                color: #000000;
            }
        """
        # Iterar sobre todos os widgets da aplicação e aplicar o estilo
        app = QApplication.instance()
        for widget in app.allWidgets():
            widget.setStyleSheet(style_sheet)
        
        # Salvar no JSON que o tema agora é escuro
        self.config.tema = "claro"
        self.config.salvar(self.config.usuario, self.config.senha, self.config.mantem_conectado)

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

    def finalizar_aplicacao_modo_classico(self,progress_dialog):
        style_sheet = """
            QMainWindow, QStackedWidget, QWidget, QFrame,QTableWidget {
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
                qproperty-icon: url("imagens/botão_lupa.png");
                qproperty-iconSize: 16px 16px;
                background: transparent;
                border: none;
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
                border: 3px solid #ffffff;
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
                height: 15px;
                margin: 0px 10px 0px 10px;
            }
            /* Estiliza a barra de rolagem vertical */
            QTableView QScrollBar:vertical {
                border: none;
                background-color: rgb(255, 255, 255); /* branco */
                width: 35px;
                margin: 0px 10px 0px 10px;
            }
            /* Parte que você arrasta */
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
                min-height: 10px;  /* <- Adicione isso */
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
            
            
        """
        # Iterar sobre todos os widgets da aplicação e aplicar o estilo
        app = QApplication.instance()
        for widget in app.allWidgets():
            widget.setStyleSheet(style_sheet)
        
        # Salvar no JSON que o tema agora é escuro
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
        btn_tema.setObjectName("btn_classe_tema")  # identifica para o modo clássico
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

        # ------------------- MENU HORA -------------------
        btn_hora = QToolButton(self.janela_config)
        btn_hora.setText("Hora e Data")
        btn_hora.setPopupMode(QToolButton.InstantPopup)
        btn_hora.setToolButtonStyle(Qt.ToolButtonTextOnly)
        btn_hora.setCursor(Qt.PointingHandCursor)
        btn_hora.setObjectName("btn_classe_hora")
        btn_hora.setFixedHeight(38)
        menu_hora = QMenu(self.janela_config)
        menu_hora.addAction("Exibir os segundos")
        menu_hora.addAction("Exibir relógio analógico")
        menu_hora.addAction("Exibir relógio digital")
        menu_hora.addAction("Exibir calendário")
        menu_hora.addAction("Definir fuso horário automaticamente")
        menu_hora.addAction("Definir fuso horário manualmente")
        menu_hora.addAction("Definir horário automaticamente")
        menu_hora.addAction("Não exibir relógio")
        btn_hora.setMenu(menu_hora)
        layout.addWidget(btn_hora)

        # ------------------- MENU FONTE -------------------
        btn_fonte = QToolButton(self.janela_config)
        btn_fonte.setText("Fonte")
        btn_fonte.setPopupMode(QToolButton.InstantPopup)
        btn_fonte.setToolButtonStyle(Qt.ToolButtonTextOnly)
        btn_fonte.setCursor(Qt.PointingHandCursor)
        btn_fonte.setObjectName("btn_classe_fonte")
        btn_fonte.setFixedHeight(38)
        menu_fonte = QMenu(self.janela_config)
        for i in range(8, 37, 2):
            menu_fonte.addAction(str(i))
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
        menu_atalhos.addAction("Mapear teclas de atalhos")
        menu_atalhos.addAction("Abrir painel de atalhos")
        menu_atalhos.addAction("Editar atalhos")
        menu_atalhos.addAction("Sobre atalhos")
        btn_atalhos.setMenu(menu_atalhos)
        layout.addWidget(btn_atalhos)

        # Mostrar janela
        self.janela_config.show()
    
    


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
