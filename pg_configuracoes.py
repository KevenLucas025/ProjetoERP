from PySide6.QtWidgets import (QWidget,QMenu, QVBoxLayout, 
                               QProgressBar,QApplication,QDialog,QMessageBox)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QIcon
import os
import json
from login import Login
import sys

class Pagina_Configuracoes(QWidget):
    def __init__(self, tool_tema, tool_atalhos,tool_hora, tool_fonte,tool_atualizacoes,tool_notificacoes,
                 frame_pg_configuracoes, frame_pg_configuracoes1, 
                 main_window, paginas_sistemas, frame_botoes_navegacoes, label_8, centralwidget, 
                 frame_2, frame_page_estoque, frame_5, frame_cadastro_usuario,
                 pg_cadastro_usuario, btn_avancar, btn_retroceder, btn_opcoes, btn_home, btn_verificar_estoque,
                 btn_cadastrar_produto, btn_cadastro_usuario, btn_clientes, btn_configuracoes,
                 btn_importar, btn_gerar_saida, btn_estorno, btn_abrir_planilha, line_excel,
                 label_cadastramento, label_cadastramento_produtos,frame_valor_total_produtos,
                 frame_valor_do_desconto, frame_valor_desconto,frame_quantidade,parent=None):
        super().__init__(parent)

        self.main_window = main_window
        self.paginas_sistemas = paginas_sistemas
        self.frame_botoes_navegacoes = frame_botoes_navegacoes
        self.label_8 = label_8
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
        self.btn_configuracoes = btn_configuracoes
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




        self.frame_pg_configuracoes = frame_pg_configuracoes
        self.frame_pg_configuracoes.setObjectName("frame_pg_configuracoes")
        self.frame_pg_configuracoes1 = frame_pg_configuracoes1
        self.frame_pg_configuracoes1.setObjectName("frame_pg_configuracoes1")

        self.line_excel.setObjectName("line_excel")

        self.tool_tema = tool_tema
        self.tool_atalhos = tool_atalhos
        self.tool_hora = tool_hora
        self.tool_fonte = tool_fonte
        self.tool_atualizacoes = tool_atualizacoes
        self.tool_notificacoes = tool_notificacoes

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

        self.tool_tema.clicked.connect(self.mostrar_menu_tema)
        self.tool_atalhos.clicked.connect(self.mostrar_menu_atalhos)
        self.tool_hora.clicked.connect(self.mostrar_menu_hora)
        self.tool_fonte.clicked.connect(self.mostrar_menu_fonte)
        self.tool_atualizacoes.clicked.connect(self.mostrar_menu_atualizacoes)
        self.tool_notificacoes.clicked.connect(self.mostrar_menu_notificacoes)

    def mostrar_menu_tema(self):
        menu_tema = QMenu(self)
        menu_tema.setStyleSheet("""
            QMenu {
                background-color: white;
                color: black;
            }
            QMenu::item:selected {
                background-color: rgb(100, 180, 255);
                color: white;
            }
        """)

        modo_escuro_action = menu_tema.addAction("Modo escuro")
        modo_claro_action = menu_tema.addAction("Modo claro")
        modo_classico_action = menu_tema.addAction("Modo clássico")

        modo_escuro_action.triggered.connect(self.aplicar_modo_escuro)
        modo_claro_action.triggered.connect(self.aplicar_modo_claro)
        modo_classico_action.triggered.connect(self.aplicar_modo_classico)

        menu_tema.exec(self.tool_tema.mapToGlobal(self.tool_tema.rect().bottomLeft()))

    def aplicar_modo_escuro(self):
        progress_dialog = ProgressDialog(self)
        progress_dialog.show()

        def update_progress(value):
            progress_dialog.update_progress(value)

        update_progress(10)
        QTimer.singleShot(1000, lambda: update_progress(50))
        QTimer.singleShot(2000, lambda: update_progress(80))
        QTimer.singleShot(3000, lambda: update_progress(100))

        QTimer.singleShot(3000, lambda: self.finalizar_aplicacao_modo_escuro(progress_dialog))

    def finalizar_aplicacao_modo_escuro(self, progress_dialog):
        progress_dialog.accept()  # Oculta o diálogo de progresso

        # Aplicar o estilo de modo escuro apenas após a conclusão da progress bar
        style_sheet = """
            QMainWindow, QStackedWidget, QWidget, QFrame, QLabel, QToolButton, QPushButton {
                background-color: #202124;
                color: #ffffff;
            }
            QPushButton {
                border-radius: 5px;
                border: 2px solid #ffffff;
                background-color: #ffffff;
                color: #000000;
            }
            QPushButton:hover {
                background-color: #dddddd;
                border: 2px solid #aaaaaa;
            }
            QPushButton:pressed {
                background-color: #bbbbbb;
                border: 2px solid #888888;
            }
            QToolButton {
                border-radius: 5px;
                border: 2px solid #ffffff;
                background-color: white;
                color: black;
            }
            QToolButton:hover {
                background-color: #dddddd;
                border: 2px solid #aaaaaa;
            }
            QToolButton:pressed {
                background-color: #bbbbbb;
                border: 2px solid #888888;
            }
            #frame_pg_configuracoes{
                background-color: #202124;
                color: #ffffff;
                border: 2px solid #ffffff;
            }
            #frame_valor_total_produtos,#frame_valor_do_desconto, #frame_valor_desconto,#frame_quantidade{
                background-color: #2a2b2e;
                color: #ffffff;
                border: 2px solid #ffffff;
                border-radius: 10px;
            }
            #label_valor_total_produtos,#label_valor_do_desconto,#label_valor_desconto,#label_quantidade_2{
                background-color: #2a2b2e;
                color: #ffffff;
            }
            #label_8,#label_cadastramento_produtos,#label_10,#label_base, #label_saida{
                border: 4px solid #ffffff;
            }
            #frame_page_estoque{
                background-color: #202124;
                color: #ffffff;
            }
        """  
         # Iterar sobre todos os widgets da aplicação e aplicar o estilo
        app = QApplication.instance()
        for widget in app.allWidgets():
            widget.setStyleSheet(style_sheet)

        self.btn_opcoes.setIcon(QIcon("imagens/imagens_modo_escuro/seta esquerda preta.png")) #Esse botão é o botão de retroceder, nomenclatura errada
        self.btn_retroceder.setIcon(QIcon("imagens/imagens_modo_escuro/seta direita preta.png")) # Esse botão é o botão avançar, nomenclatura errada

        self.btn_retroceder.setGeometry(40, 5, 30, 30)  # Define a geometria do botão 'btn_retroceder'




    def aplicar_modo_claro(self):
        style_sheet = """
            QMainWindow {
                background-color: #ffffff;
                color: #000000;
            }
            #frame_pg_configuracoes {
                background-color: #ffffff;
                color: #000000;
                border: 2px solid #000000;
            }
            #frame_pg_configuracoes1 {
                background-color: #ffffff;
                color: #000000;
                border: 2px solid #000000;
            }
            QToolButton {
                background-color: #f0f0f0;
                color: #000000;
            }
        """
        self.main_window.setStyleSheet(style_sheet)

    def aplicar_modo_classico(self):
        style_sheet = """
            QMainWindow {
                background-color: #005079;
                color: #ffffff;
            }
            #paginas_sistemas {
                background-color: #005079;
                color: #ffffff;
            }
            QStackedWidget {
                background-color: #005079;
                color: #ffffff;
            }
            #frame_pg_configuracoes {
                background-color: #005079;
                color: #ffffff;
                border: 2px solid #ffffff;
            }
            #frame_pg_configuracoes1 {
                background-color: #005079;
                color: #ffffff;
            }
            #frame_botoes_navegacoes {
                background-color: #005079;
                color: #ffffff;
            }
        """
        self.main_window.setStyleSheet(style_sheet)
        self.paginas_sistemas.setStyleSheet(style_sheet)
        self.frame_pg_configuracoes.setStyleSheet(style_sheet)
        self.frame_pg_configuracoes1.setStyleSheet(style_sheet)
        self.frame_botoes_navegacoes.setStyleSheet(style_sheet)



    def mostrar_menu_atalhos(self):
        menu_atalhos = QMenu(self)
        menu_atalhos.setStyleSheet("""
            QMenu {
                background-color: white;
                color: black;
            }
            QMenu::item:selected {
                background-color: rgb(100, 180, 255);
                color: white;
            }
        """)

        menu_atalhos.addAction("Mapear teclas de atalhos")
        menu_atalhos.addAction("Abrir painel de atalhos")
        menu_atalhos.addAction("Editar atalhos")
        menu_atalhos.addAction("Sobre atalhos")

        menu_atalhos.exec(self.tool_atalhos.mapToGlobal(self.tool_atalhos.rect().bottomLeft()))

    def mostrar_menu_hora(self):
        menu_hora = QMenu(self)
        menu_hora.setStyleSheet("""
            QMenu {
                background-color: white;
                color: black;
            }
            QMenu::item:selected {
                background-color: rgb(100, 180, 255);
                color: white;
            }
        """)

        menu_hora.addAction("Exibir os segundos")
        menu_hora.addAction("Exibir relógio análogico")
        menu_hora.addAction("Exibir relógio digital")
        menu_hora.addAction("Exibir calendário")
        menu_hora.addAction("Definir fuso horário automaticamente")
        menu_hora.addAction("Definir fuso horário manualmente")
        menu_hora.addAction("Definir horário automaticamente")
        menu_hora.addAction("Não exibir relógio")

        menu_hora.exec(self.tool_hora.mapToGlobal(self.tool_hora.rect().bottomLeft()))

    def mostrar_menu_fonte(self):
        menu_fonte = QMenu(self)
        menu_fonte.setStyleSheet("""
            QMenu {
                background-color: white;
                color: black;
            }
            QMenu::item:selected {
                background-color: rgb(100, 180, 255);
                color: white;
            }
        """)

        tamanhos = [str(i) for i in range(8, 37, 2)]
        for tamanho in tamanhos:
            menu_fonte.addAction(tamanho)

        menu_fonte.exec(self.tool_fonte.mapToGlobal(self.tool_fonte.rect().bottomLeft()))

    def mostrar_menu_atualizacoes(self):
        menu_atualizacoes = QMenu(self)
        menu_atualizacoes.setStyleSheet("""
            QMenu {
                background-color: white;
                color: black;
            }
            QMenu::item:selected {
                background-color: rgb(100, 180, 255);
                color: white;
            }
        """)

        menu_atualizacoes.addAction("Definir atualizações automaticamente")
        menu_atualizacoes.addAction("Não definir atualizações automáticas")
        menu_atualizacoes.addAction("Verificar se há atualizações")
        menu_atualizacoes.addAction("Exibir histórico de atualizações")

        menu_atualizacoes.exec(self.tool_atualizacoes.mapToGlobal(self.tool_atualizacoes.rect().bottomLeft()))

    def mostrar_menu_notificacoes(self):
        menu_notificacoes = QMenu(self)
        menu_notificacoes.setStyleSheet("""
            QMenu{
                background-color: white;
                color: black;
            }
            QMenu::item:selected {
                background-color: rgb(100, 180, 255);
                color: white;
            }      
        """)
        menu_notificacoes.addAction("Definir notificação de boas vinda")
        
        menu_notificacoes.exec(self.tool_notificacoes.mapToGlobal(self.tool_notificacoes.rect().bottomLeft()))

    def mousePressEvent_atualizacoes(self, event):
        if event.button() == Qt.LeftButton:
            self.mostrar_menu_atualizacoes()

    def mousePressEvent_fonte(self, event):
        if event.button() == Qt.LeftButton:
            self.mostrar_menu_fonte()

    def mousePressEvent_hora(self, event):
        if event.button() == Qt.LeftButton:
            self.mostrar_menu_hora()

    def mousePressEvent_atalhos(self, event):
        if event.button() == Qt.LeftButton:
            self.mostrar_menu_atalhos()

    def mousePressEvent_tema(self, event):
        if event.button() == Qt.LeftButton:
            self.mostrar_menu_tema()

    def  mousePressEvent_notificacao(self, event):
        if event.button() == Qt.LeftButton:
            self.mostrar_menu_notificacoes()



class ProgressDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Aplicando Modo Escuro")
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
                text-align: center; /* Alinhar o texto ao centro */
                                        
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



        