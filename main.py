#*********************************************************************************************************************
import re
from PySide6.QtCore import (Qt, QTimer, QDate, QBuffer, QByteArray, QIODevice, Signal,
                            QEvent,QPropertyAnimation,QEasingCurve,QSize,QPoint)
from PySide6 import QtCore
from PySide6.QtWidgets import (QMainWindow, QMessageBox, QPushButton,
                               QLabel, QFileDialog, QVBoxLayout,
                               QMenu,QTableWidgetItem,QCheckBox,QApplication,QToolButton,QHeaderView,QCompleter,
                               QComboBox,QInputDialog,QProgressDialog)
from PySide6.QtGui import (QDoubleValidator, QIcon, QColor, QPixmap,QBrush,
                           QAction,QMovie,QImage,QShortcut,QKeySequence)
from PySide6 import QtWidgets
from login import Login
from mane_python import Ui_MainWindow
from database import DataBase
import sys
import locale
from config_senha import TrocarSenha
from atualizarprodutos import AtualizarProduto
from tabelaprodutos import TabelaProdutos
from configuracoes import Configuracoes_Login
from tabelausuario import TabelaUsuario
from atualizarusuario import AtualizarUsuario
from pg_configuracoes import Pagina_Configuracoes
from estoqueprodutos import EstoqueProduto
from historicousuario import Pagina_Usuarios
from utils import MostrarSenha,configurar_frame_valores
from clientes_juridicos import Clientes_Juridicos
from clientes_fisicos import Clientes_Fisicos
import json
import sqlite3
import os
import datetime
from datetime import datetime
import base64
import random
import string
import socket
from  plyer import notification
import subprocess
import pandas as pd
from openpyxl.utils import get_column_letter
from openpyxl.styles import Alignment
from openpyxl import load_workbook
import requests
import shutil




class MainWindow(QMainWindow, Ui_MainWindow):
    fechar_janela_login_signal = Signal(str)
    def __init__(self, user=None, login_window=None, tipo_usuario=None, connection=None):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de Gerenciamento")
        self.historico_pausado = False
        self.historico_pausado_clientes_juridicos = False
        self.historico_pausado_clientes_fisicos = False
        self.historico_usuario_pausado = False
        self.imagem_removida_usuario = False
        self.usuario_tem_imagem_salva = False
        
        # Atalho F5 global
        self.atalho_f5 = QShortcut(QKeySequence("F5"), self)
        self.atalho_f5.activated.connect(self.tratar_f5_global)


        # Inicialize o banco de dados antes de qualquer operação que dependa dele
        self.db = DataBase('banco_de_dados.db')
        self.login_window = login_window
        # Se já vier uma conexão, usa ela. Caso contrário, cria uma nova
        if connection is None:
            self.connection = sqlite3.connect('banco_de_dados.db')
        else:
            self.connection = connection

        self.login_window = login_window

        self.exibir_senha = MostrarSenha(self,self.txt_senha)
        self.exibir_senha_usuario = MostrarSenha(self,self.txt_confirmar_senha)

        #Cria as tabelas no banco de dados sempre que executar o sistema em um novo ambiente
        self.db.create_table_products()
        self.db.create_table_products_saida()
        self.db.create_table_users()
        self.db.create_table_historico()
        self.db.create_table_users_inativos()
        self.db.create_table_historico_usuario()
        self.db.create_table_clientes_juridicos()
        self.db.create_table_clientes_fisicos()
        self.db.create_table_historico_fisico()
        self.db.create_table_historico_juridico()

        # Mapeia os campos com identificadores únicos
        self.campos_com_autocomplete = {
            "txt_nome": self.txt_nome,
            "txt_cep": self.txt_cep,
            "txt_cliente_3": self.txt_cliente_3,
            "txt_codigo_item": self.txt_codigo_item,
            "txt_complemento": self.txt_complemento,
            "txt_confirmar_senha": self.txt_confirmar_senha,
            "txt_senha": self.txt_senha,
            "txt_data_nascimento": self.txt_data_nascimento,
            "txt_cpf": self.txt_cpf,
            "txt_descricao_produto_3": self.txt_descricao_produto_3,
            "txt_endereco": self.txt_endereco,
            "txt_numero": self.txt_numero,
            "txt_produto": self.txt_produto,
            "txt_valor_produto_3": self.txt_valor_produto_3,
            "txt_telefone": self.txt_telefone,
            "txt_email": self.txt_email,
            "txt_rg": self.txt_rg,
            "txt_quantidade": self.txt_quantidade,
            "line_clientes": self.line_clientes,
            "txt_usuario": self.txt_usuario,
            "txt_cnpj": self.txt_cnpj
        }
        

        self.table_base.verticalHeader().setVisible(True)
        self.table_saida.verticalHeader().setVisible(True)
        self.table_ativos.verticalHeader().setVisible(True)
        self.table_saida.horizontalHeader().setVisible(True)
        self.table_inativos.verticalHeader().setVisible(True)
        self.table_clientes_fisicos.verticalHeader().setVisible(True)
        self.table_base.setShowGrid(True)
        self.table_saida.setShowGrid(True)
        self.table_ativos.setShowGrid(True)
        self.table_inativos.setShowGrid(True)
        

        # funções que precisam do banco de dados
        self.erros_frames_produtos()
        self.erros_frames_usuarios()
        
        # Carregar informações ao iniciar
        self.carregar_informacoes_tabelas()

        # Exibir notificação de status de conexão
        #self.exibir_notificacao(self)

        # Inicializar as configurações antes de chamar fazer_login_automatico
        self.config = Configuracoes_Login(self)
        self.config.carregar()
        self.fazer_login_automatico()

        # Aplica completer individual a cada campo
        for nome_campo, campo in self.campos_com_autocomplete.items():
            historico = self.config.carregar_historico_autocompletar(nome_campo)
            completer = QCompleter(historico)
            completer.setCaseSensitivity(Qt.CaseInsensitive)
            campo.setCompleter(completer)
            campo.editingFinished.connect(lambda nc=nome_campo, c=campo: self.auto_completar(nc, c))

            campo.mouseDoubleClickEvent = lambda event, nc=nome_campo, c=campo: self.completar_por_duplo_clique(event, nc, c)
        

        # Caminho para o arquivo GIF
        gif_path = os.path.abspath("imagens/oie_3193441C0mFhFhk.gif") 

        # Configurar o QMovie com o GIF
        self.movie = QMovie(gif_path)
        self.label_imagem_sistema.setMovie(self.movie)
        # Iniciar a animação
        self.movie.start()

        # Configuração do produto
        self.produto_original = {}
        self.produtos_pendentes = []
        self.imagem_carregada_produto = None
    
        # Variáveis para armazenar o estado de edição e o ID do usuário selecionado
        self.is_editing = False
        self.selected_user_id = None
        self.is_editing_produto = False
        self.selected_produto_id = None

        self.pagina_clientes_juridicos = Clientes_Juridicos(self.line_clientes,self,self.btn_adicionar_cliente_juridico,self.btn_editar_clientes,
                                        self.btn_excluir_clientes,self.btn_gerar_relatorio_clientes,self.btn_marcar_como_clientes,
                                        self.btn_historico_clientes)
        
        self.pagina_clientes_fisicos = Clientes_Fisicos(self.line_clientes_fisicos,self,self.btn_adicionar_cliente_fisico,self.btn_editar_clientes_fisicos,
                                                        self.btn_excluir_clientes_fisicos,self.btn_gerar_relatorio_clientes_fisicos,self.btn_historico_clientes_fisicos,
                                                        self.btn_marcar_como_clientes_fisicos)

        # Crie o layout para o frame_imagem_cadastro e adicione o QLabel
        self.label_imagem_usuario = QLabel(self)
        layout_usuario = QVBoxLayout()  # Definindo layout_usuario aqui
        layout_usuario.addWidget(self.label_imagem_usuario)
        self.frame_imagem_cadastro.setLayout(layout_usuario)

        '''self.label_exibir_usuario = QLabel(self)
        layout_exibir_usuario = QVBoxLayout()
        layout_exibir_usuario.addWidget(self.label_exibir_usuario)
        self.label_exibir_usuario.setGeometry(1265,5,600,30)'''

        # Atualizar o nome do usuário logado
        #self.atualizar_usuario_logado(self.config.obter_usuario_logado())
        
        self.frame_imagem_produto_3.setLayout(QVBoxLayout())
        self.label_imagem_produto = QLabel(self.frame_imagem_produto_3)
        self.label_imagem_produto.setGeometry(0, 0, self.frame_imagem_produto_3.width(), self.frame_imagem_produto_3.height())
        self.label_imagem_produto.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_imagem_produto.setScaledContents(False)
        self.frame_imagem_produto_3.layout().addWidget(self.label_imagem_produto)  # Adicionar QLabel ao layout do frame
        self.imagem_carregada_produto = False


        # Criação dos botões      
        self.btn_avancar = QPushButton(self)
        self.btn_avancar.setIcon(QIcon("imagens/seta_direita-removebg-preview.png"))  # Adicione o caminho do ícone de avançar
        self.btn_avancar.setGeometry(35, 5, 30, 30)
        self.btn_avancar.setToolTip("Avançar")  # Adiciona uma dica de ferramenta
      
        
        self.btn_retroceder = QPushButton(self)
        self.btn_retroceder.setIcon(QIcon("imagens/seta esquerda 2.png"))  # Adicione o caminho do ícone de retroceder
        self.btn_retroceder.setGeometry(5, 5, 30, 30) 
        self.btn_retroceder.setToolTip("Retroceder") # Adiciona uma dica de ferramenta

        self.btn_opcoes_navegacao = QPushButton(self)
        self.btn_opcoes_navegacao.setIcon(QIcon("imagens/54206.png"))
        self.btn_opcoes_navegacao.setIconSize(QSize(30,30))
        self.btn_opcoes_navegacao.setGeometry(10,10,150,80)
        self.btn_opcoes_navegacao.setCursor(Qt.PointingHandCursor)
        estilo_botao_opcoes_navegacao = """
            QPushButton {
                border: none;
                background: transparent;
            }

        """
        self.btn_opcoes_navegacao.setStyleSheet(estilo_botao_opcoes_navegacao)


        # Criar o menu dentro do botão btn_opcoes
        self.menu_opcoes = QMenu(self.btn_mais_opcoes)
        

       # Definir o estilo do menu
        estilo_botao_menu = """
            QMenu {
                background-color: white;
                color: black;
                border: 1px solid lightgray;
            }
            QMenu::item {
                padding: 5px 20px;
            }
            QMenu::item:selected {
                background-color: rgb(0, 120, 215); /* Azul Windows */
                color: white;
            }
        """
        self.menu_opcoes.setStyleSheet(estilo_botao_menu)


        # Criar as ações do menu
        self.action_sair = QAction("Sair do Sistema", self)
        self.action_configuracoes = QAction("Configurações", self)
        self.action_contato = QAction("Contato", self)
        self.action_reiniciar = QAction("Reiniciar Sistema", self)
        self.action_planilhas_exemplo = QAction("Planilhas de exemplo", self)
        self.action_em_massa_produtos = QAction("Cadastrar produtos em massa", self)
        self.action_em_massa_usuarios = QAction("Cadastrar usuários em massa", self)
        self.action_informacoes_sistema = QAction("Informações do sistema", self)
        self.action_limpar_cache = QAction("Limpar Cache", self)
        

        # Adicionar as ações ao menu (FUNDAMENTAL!)
        self.menu_opcoes.addAction(self.action_sair)
        self.menu_opcoes.addAction(self.action_configuracoes)
        self.menu_opcoes.addAction(self.action_contato)
        self.menu_opcoes.addAction(self.action_reiniciar)
        self.menu_opcoes.addAction(self.action_planilhas_exemplo)
        self.menu_opcoes.addAction(self.action_em_massa_produtos)
        self.menu_opcoes.addAction(self.action_em_massa_usuarios)
        self.menu_opcoes.addAction(self.action_informacoes_sistema)
        self.menu_opcoes.addAction(self.action_limpar_cache)
        

        # Associar o menu ao botão
        self.btn_mais_opcoes.setMenu(self.menu_opcoes)
        self.btn_mais_opcoes.setPopupMode(QToolButton.InstantPopup)



        # Conectar as ações do menu aos slots correspondentes
        self.action_sair.triggered.connect(self.desconectarUsuario)
        self.action_configuracoes.triggered.connect(self.combobox_caixa)
        self.action_contato.triggered.connect(self.show_pg_contato)
        self.action_reiniciar.triggered.connect(self.reiniciar_sistema)
        self.action_planilhas_exemplo.triggered.connect(self.exibir_planilhas_exemplo)
        self.action_em_massa_produtos.triggered.connect(self.pagina_cadastro_em_massa_produtos)
        self.action_em_massa_usuarios.triggered.connect(self.pagina_cadastro_em_massa_usuarios)
        self.action_informacoes_sistema.triggered.connect(self.show_mensagem_sistema)
        self.action_limpar_cache.triggered.connect(self.limpar_cache_sistema)

        self.fechar_janela_login_signal.connect(self.fechar_janela_login)


        

        # Defina a visibilidade do botão de cadastro de usuário com base no tipo de usuário
        user = tipo_usuario.lower() if tipo_usuario else ""
        if user in ["usuário", "user"]:
            self.btn_cadastro_usuario.setVisible(False)
        elif user in ["convidado", "convidado"]:
            self.btn_cadastrar_produto.setVisible(False)
            self.btn_cadastro_usuario.setVisible(False)
            self.btn_clientes.setVisible(False)

        self.carregar_configuracoes()
        

        self.pagina_usuarios = Pagina_Usuarios(self, self.btn_abrir_planilha_usuarios,self.btn_cadastrar_novo_usuario,
                                               self.btn_historico_usuarios,self.btn_atualizar_ativos,
                                               self.btn_atualizar_inativos,self.btn_limpar_tabelas_usuarios,self.btn_gerar_saida_usuarios,
                                               self.line_excel_usuarios,self.progress_excel_usuarios,self.btn_importar_usuarios,
                                               self.btn_abrir_planilha_massa_usuarios,self.btn_fazer_cadastro_massa_usuarios,self.progress_massa_usuarios,
                                               self.line_edit_massa_usuarios)

        self.estoque_produtos = EstoqueProduto(self,self.btn_gerar_pdf,self.btn_gerar_estorno,
                                               self.btn_gerar_saida,self.btn_importar,self.btn_limpar_tabelas,
                                               self.btn_atualizar_saida,self.btn_atualizar_estoque,self.btn_historico,
                                               self.btn_abrir_planilha,self.line_excel,self.progress_excel,
                                               self.btn_incluir_produto_sistema,self.btn_fazer_cadastro_massa_produtos,
                                               self.btn_abrir_planilha_massa_produtos,self.progress_massa_produtos,self.line_edit_massa_produtos)
        
        self.configuracoes_senha = TrocarSenha(self)  

        

        # Criar instância de TabelaProdutos passando uma referência à MainWindow
        self.atualizar_produto_dialog = AtualizarProduto(self)

        # Criar instância de AtualizarProduto passando uma referência à MainWindow e à tabela de produtos
        self.tabela_produtos_dialog = TabelaProdutos(self, self.dateEdit_3)

        # Criar instância da TabelaUsuario
        self.tabela_usuario_dialogo = TabelaUsuario(self)
        
        self.produto_id = None

        self.criar_botoes_avancar_voltar()

        self.dateEdit_3.setDate(QDate.currentDate())

        self.txt_cep.textChanged.connect(self.formatar_cep)
        self.txt_cpf.textChanged.connect(self.formatar_cpf)
        self.txt_rg.textChanged.connect(self.formatar_rg)
        self.txt_cnpj.textChanged.connect(self.formatar_cnpj)
        self.txt_data_nascimento.textChanged.connect(self.formatar_data_nascimento)
        self.txt_telefone.textChanged.connect(self.formatar_telefone)
   

        self.btn_editar_cadastro.clicked.connect(self.mostrar_tabela_usuarios)
        self.btn_carregar_imagem_4.clicked.connect(self.carregar_imagem_usuario)
 

        # Lista de páginas na ordem desejada
        self.paginas = [self.home_pag, self.pag_estoque, self.pg_cadastrar_produto, 
                        self.pg_cadastrar_usuario, self.pg_clientes, self.pg_configuracoes, 
                        self.pg_contato]
        self.pagina_atual_index = 0  # Índice da página atual na lista
        self.historico_paginas = []  # Lista para armazenar o histórico de páginas

        # Configurar a página inicial
        self.paginas_sistemas.setCurrentWidget(self.paginas[self.pagina_atual_index])

        self.label_valor_total_produtos = configurar_frame_valores(self.frame_valor_total_produtos, "Valor total de produtos sem desconto")
        self.label_valor_do_desconto = configurar_frame_valores(self.frame_valor_do_desconto, "Valor do desconto")
        self.label_valor_desconto = configurar_frame_valores(self.frame_valor_com_desconto1, "Valor do produto com desconto")
        self.label_quantidade = configurar_frame_valores(self.frame_quantidade, "Quantidade total de produtos",valor_monetario=False)


        # Centralizar o texto 
        for label in [
            self.label_valor_total_produtos,
            self.label_valor_do_desconto,
            self.label_valor_desconto,
            self.label_quantidade,
        ]:
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("font-size: 20px; color: white; font-family: 'Arial'; font-weight: bold;")

        validator = QDoubleValidator()
        validator.setNotation(QDoubleValidator.StandardNotation)  
        validator.setDecimals(2)
        validator.setTop(1000000000)  
        self.txt_valor_produto_3.setValidator(validator)


        self.txt_valor_produto_3.editingFinished.connect(self.formatar_moeda)

        validador = QDoubleValidator()
        validador.setNotation(QDoubleValidator.StandardNotation)  
        validador.setRange(0.00, 100.00)  
        validador.setDecimals(2)
        self.txt_desconto_3.setValidator(validador)
        self.txt_desconto_3.editingFinished.connect(self.formatar_porcentagem)


        self.btn_home.clicked.connect(lambda: self.paginas_sistemas.setCurrentWidget(self.home_pag))
        self.btn_clientes.clicked.connect(lambda: self.paginas_sistemas.setCurrentWidget(self.pg_clientes))
        self.btn_cadastrar_usuarios.clicked.connect(lambda: self.paginas_sistemas.setCurrentWidget(self.pg_cadastrar_usuario))
        self.btn_configuracoes.clicked.connect(lambda: self.paginas_sistemas.setCurrentWidget(self.pg_configuracoes))      
        self.btn_cadastrar_produto.clicked.connect(lambda: self.paginas_sistemas.setCurrentWidget(self.pg_cadastrar_produto))
        self.btn_ver_item.clicked.connect(lambda: self.paginas_sistemas.setCurrentWidget(self.pag_estoque))
        self.btn_novo_produto.clicked.connect(lambda: self.paginas_sistemas.setCurrentWidget(self.pg_cadastrar_produto))
        self.btn_verificar_usuarios.clicked.connect(lambda: self.paginas_sistemas.setCurrentWidget(self.page_verificar_usuarios))
        self.btn_ver_usuario.clicked.connect(lambda: self.paginas_sistemas.setCurrentWidget(self.page_verificar_usuarios))
        self.btn_cadastrar_novo_usuario.clicked.connect(lambda: self.paginas_sistemas.setCurrentWidget(self.pg_cadastrar_usuario))
        self.btn_editar_massa_produtos.clicked.connect(lambda: self.paginas_sistemas.setCurrentWidget(self.pg_cadastrar_produto))
        self.btn_editar_massa_usuario.clicked.connect(lambda: self.paginas_sistemas.setCurrentWidget(self.pg_cadastrar_usuario))
        

        self.btn_remover_imagem.clicked.connect(self.retirar_imagem_produto)
        self.btn_limpar_campos.clicked.connect(self.apagar_campos_produtos)
        self.btn_adicionar_produto.clicked.connect(self.adicionar_produto)
        self.btn_confirmar.clicked.connect(self.confirmar_produtos)
        self.btn_atualizar_cadastro.clicked.connect(self.atualizar_usuario_no_bd)
        self.btn_verificar_estoque.clicked.connect(self.mostrar_page_estoque)
        self.btn_ver_clientes_juridicos.clicked.connect(self.mostrar_page_clientes)
        self.btn_apagar_cadastro.clicked.connect(self.eliminar_campos_usuarios)
        self.btn_remover_imagem_usuario.clicked.connect(self.retirar_imagem_usuario)
        self.btn_sair_modo_edicao.clicked.connect(self.sair_modo_edicao_usuarios)
        self.btn_sair_modo_edicao_produtos.clicked.connect(self.sair_modo_edicao_produto)

        self.btn_fazer_cadastro.clicked.connect(self.subscribe_user)
        self.btn_editar.clicked.connect(self.exibir_tabela_produtos)
        self.btn_atualizar_produto.clicked.connect(self.atualizar_produto)
        self.btn_carregar_imagem.clicked.connect(self.carregar_imagem_produto)
        self.btn_opcoes_navegacao.clicked.connect(self.abrir_menu_opcoes)
        
        

        self.txt_cep.editingFinished.connect(self.on_cep_editing_finished)

        
        
        self.pagina_configuracoes = Pagina_Configuracoes(self.tool_tema,self.tool_atalhos,
                                                         self.tool_hora,self.tool_fonte,self.tool_atualizacoes,self.tool_notificacoes,
                                                         self.frame_botoes_configuracoes,self.frame_pg_configuracoes,self,self,
                                                         self.frame_botoes_navegacoes,self.label_configuracoes,self.centralwidget,
                                                         self.frame_pag_estoque,self.frame_2,self.paginas_sistemas,
                                                         self.pg_cadastrar_usuario,self.frame_pag_cadastrar_usuario,
                                                         self.btn_mais_opcoes,self.btn_avancar,self.btn_retroceder,self.btn_home,self.btn_verificar_estoque,
                                                         self.btn_cadastrar_produto, self.btn_cadastrar_usuarios, self.btn_clientes,self.btn_configuracoes,
                                                         self.btn_abrir_planilha,self.btn_importar,self.btn_gerar_saida,
                                                         self.line_excel,self.btn_gerar_estorno,
                                                         self.label_cadastramento,self.label_cadastramento_produtos,self.frame_valor_total_produtos,
                                                         self.frame_valor_do_desconto,self.frame_valor_com_desconto1,self.frame_quantidade)


    def abrir_menu_opcoes(self):
        # Verifica se já armazenamos a posição original da página
        if not hasattr(self, "posicao_original_paginas"):
            self.posicao_original_paginas = self.paginas_sistemas.pos().x()

        largura_atual = self.frame_botoes_navegacoes.width()  # Obtém a largura atual
        nova_largura = 200 if largura_atual == 9 else 9  # Expande ou recolhe o menu

        # Posição do botão
        posicao_botao_x = self.btn_opcoes_navegacao.x()
        
        # Definir deslocamento das páginas
        deslocamento_x = 60  # Ajuste conforme necessário

        # Determinar nova posição das páginas
        if nova_largura == 9:  # Se o menu for recolhido, mover para a esquerda
            nova_posicao_paginas_x = self.posicao_original_paginas - deslocamento_x
        else:  # Se o menu for expandido, voltar para a posição original
            nova_posicao_paginas_x = self.posicao_original_paginas

        # Duração da animação
        duracao_animacao = 400  

        # Animação do frame de navegação (expande/recolhe)
        self.animacao_frame = QPropertyAnimation(self.frame_botoes_navegacoes, b"maximumWidth")
        self.animacao_frame.setDuration(duracao_animacao)
        self.animacao_frame.setStartValue(largura_atual)
        self.animacao_frame.setEndValue(nova_largura)
        self.animacao_frame.setEasingCurve(QEasingCurve.InOutQuart)

        # Animação das páginas
        self.animacao_paginas = QPropertyAnimation(self.paginas_sistemas, b"pos")
        self.animacao_paginas.setDuration(duracao_animacao)
        self.animacao_paginas.setStartValue(self.paginas_sistemas.pos())
        self.animacao_paginas.setEndValue(QPoint(nova_posicao_paginas_x, self.paginas_sistemas.y()))
        self.animacao_paginas.setEasingCurve(QEasingCurve.InOutQuart)

        # Inicia as animações
        self.animacao_frame.start()
        self.animacao_paginas.start()

    def boas_vindas(self):
        if self.config.nao_mostrar_mensagem_boas_vindas:
            return
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Boas Vindas")
        msg.setText(f"{self.config.obter_usuario_logado()}, seja bem-vindo(a) ao sistema de gerenciamento.\n"
                    "É um prazer tê-lo(a) conosco em nosso sistema.\n"
                    "Esperamos que as informações aqui contidas sejam de grande ajuda.\n"
                    "Pedimos que sempre que possível, você possa avaliar e sugerir melhorias.")
        msg.setStandardButtons(QMessageBox.Ok)

        checkbox_nao_mostrar_mensagem = QCheckBox("Não mostrar mensagem novamente")
        msg.setCheckBox(checkbox_nao_mostrar_mensagem)
        msg.exec()

        if checkbox_nao_mostrar_mensagem.isChecked():
            self.config.nao_mostrar_mensagem_boas_vindas = True
            self.config.salvar_configuracoes(self.config.usuario, self.config.senha, self.config.mantem_conectado)

    '''def atualizar_usuario_logado(self, user):
        if user:
            usuario_logado = f"Usuário logado: {user}"
        else:
            usuario_logado = "Nenhum usuário logado"

        self.label_exibir_usuario.setText(usuario_logado)
        self.label_exibir_usuario.setStyleSheet("font-size: 15px; font-weight: bold; color: white;")
        print(usuario_logado)'''


    '''def verificar_conexao(self):
        """Verifica se há conexão com a internet."""
        try:
            # Tenta conectar ao Google para verificar a internet
            socket.create_connection(("8.8.8.8", 53), timeout=5)
            return True
        except OSError:
            return False
 
    def exibir_notificacao(self):
        """Exibe uma notificação de status de conexão."""
        conectado = self.verificar_conexao()
        if conectado:
            mensagem = "Você está conectado à internet."
        else:
            mensagem = "Sem conexão com a internet."

        # Exibir notificação
        notification.notify(
            title="Status da Conexão",
            message=mensagem,
            app_name="Sistema de Gerenciamento",
            timeout=5  # Duração em segundos
        )'''
            
    def criar_item(self, texto):
        item = QTableWidgetItem(texto)
        item.setTextAlignment(Qt.AlignCenter)  # Centraliza o texto
        item.setForeground(QBrush(QColor(255, 255, 255)))  # Define a cor do texto como branco
        return item
    

    def carregar_informacoes_tabelas(self):
        # Limpa as tabelas antes de carregar novas informações
        self.table_base.setRowCount(0)
        self.table_saida.setRowCount(0)
        self.table_ativos.setRowCount(0)
        self.table_inativos.setRowCount(0)

        # Carregar dados da `table_base`
        produtos_base = self.db.obter_produtos_base()
        for produto in produtos_base:
            row_position = self.table_base.rowCount()
            self.table_base.insertRow(row_position)
            for col, data in enumerate(produto):
                self.table_base.setItem(row_position, col, self.criar_item(str(data)))

        # Ajusta colunas e linhas automaticamente após preencher
        self.table_base.resizeColumnsToContents()
        self.table_base.resizeRowsToContents()

        # Ajuste refinado nas colunas da table_base
        header = self.table_base.horizontalHeader()
        for i in range(self.table_base.columnCount() - 1):
            header.setSectionResizeMode(i, QHeaderView.ResizeToContents)

        # Última coluna ("Usuário") com tamanho fixo
        header.setSectionResizeMode(self.table_base.columnCount() - 1, QHeaderView.Interactive)
        self.table_base.setColumnWidth(self.table_base.columnCount() - 1, 120)
            

        # Carregar dados da `table_saida`
        produtos_saida = self.db.obter_produtos_saida()
        for produto in produtos_saida:
            row_position = self.table_saida.rowCount()
            self.table_saida.insertRow(row_position)
            for col, data in enumerate(produto):
                self.table_saida.setItem(row_position, col, self.criar_item(str(data)))
        
        self.table_saida.resizeColumnsToContents()
        self.table_saida.resizeRowsToContents()

        # Carregar dados da `table_ativos`   
        usuarios_ativos = self.db.obter_usuarios_ativos()
        for usuario in usuarios_ativos:
            row_position = self.table_ativos.rowCount()
            self.table_ativos.insertRow(row_position)
            for col, data in enumerate(usuario):
                self.table_ativos.setItem(row_position, col,self.criar_item(str(data)))

        self.table_ativos.resizeColumnsToContents()
        self.table_ativos.resizeRowsToContents()

        # Carregar dados da `table_inativos` 
        usuarios_inativos = self.db.obter_usuarios_inativos()
        for usuario in usuarios_inativos:
            row_position = self.table_inativos.rowCount()
            self.table_inativos.insertRow(row_position)
            for col, data in enumerate(usuario):
                self.table_inativos.setItem(row_position, col,self.criar_item(str(data)))

        # Carregar dados da table_clientes_juridicos
        clientes = self.db.obter_clientes_juridicos()
        for cliente in clientes:
            row_position = self.table_clientes_juridicos.rowCount()
            self.table_clientes_juridicos.insertRow(row_position)
            for col, data in enumerate(cliente):
                self.table_clientes_juridicos.setItem(row_position, col,self.criar_item(str(data)))

        # Carregar dados da table_clientes_fisicos
        clientes_fisicos = self.db.obter_clientes_fisicos()
        for cliente in clientes_fisicos:
            row_position = self.table_clientes_fisicos.rowCount()
            self.table_clientes_fisicos.insertRow(row_position)
            for col, data in enumerate(cliente):
                self.table_clientes_fisicos.setItem(row_position,col,self.criar_item(str(data)))

        self.table_inativos.resizeColumnsToContents()
        self.table_inativos.resizeRowsToContents()
        self.table_massa_produtos.resizeColumnsToContents()
        self.table_massa_produtos.resizeRowsToContents()
        self.table_clientes_juridicos.resizeColumnsToContents()
        self.table_clientes_juridicos.resizeRowsToContents()
        self.table_clientes_fisicos.resizeColumnsToContents()
        self.table_clientes_fisicos.resizeRowsToContents()
    
    

    def show_mensagem_sistema(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Informação")
        msg.setText("Versão do Sistema: 1.0.1\n"
                    "Desenvolvedor: Keven Lucas\n"
                    "Sistema liberado para uso privado e público\n"
                    "Sua versão é gratuita\n"
                    "Todos os direitos reservados\n"
                    "Para quaisquer uso não autorizado de código fonte e/ou tentativa de usa-ló sem autorização prévia do desenvolvedor"
                    " o mesmo estará sujeito a penalização por crime de origem cibernética. O sistema detecta  uso de pessoas não autorizado"
                    " ocasionando no bloqueio temporário e conforme insistência permanente do acesso. Em versão disto, saliento que o uso do sistema"
                    " seja feito de forma responsável. ")
                    
        msg.exec()
        

    def mostrar_page_estoque(self):
        # Navegar para a página de estoque
        self.paginas_sistemas.setCurrentWidget(self.pag_estoque)
        
        # Atualizar a tabela na página de estoque
        self.estoque_produtos.tabela_estoque()
    def mostrar_page_clientes(self):
        # Navegar para a página de estoque
        self.paginas_sistemas.setCurrentWidget(self.pg_clientes)
        

    # EXIBE A PÁGINA DE CONFIGURAÇÕES AO CLICAR NA OPÇÃO CONFIGURAÇÕES DENTRO DO MENU DO BOTÃO MAIS OPÇÕES
    def combobox_caixa(self):
        selected_action = self.sender()  # A ação que acionou o slot
        if selected_action == self.action_configuracoes:
            self.paginas_sistemas.setCurrentWidget(self.pg_configuracoes)

    def show_combobox(self):
        self.combobox.show()
        
    # EXIBE A PÁGINA DE CONTATO AO CLICAR NA OPÇÃO CONTATO DENTRO DO MENU DO BOTÃO MAIS OPÇÕES
    def show_pg_contato(self):
        selected_action = self.sender()
        if selected_action == self.action_contato:
            self.paginas_sistemas.setCurrentWidget(self.pg_contato)
#*********************************************************************************************************************
    def atualizar_usuario_no_bd(self):
        if not self.db.verificar_conexao():
            QMessageBox.critical(self, "Erro", "Conexão com o banco de dados não estabelecida!")
            return
        self.connection = self.db.connection 

        if not self.is_editing or not self.selected_user_id:
            QMessageBox.warning(None, "Erro", "Nenhum usuário selecionado para atualizar")
            return

        tem_imagem = (
            hasattr(self, 'label_imagem_usuario') and 
            self.label_imagem_usuario is not None and 
            self.label_imagem_usuario.pixmap() is not None
        )

        if getattr(self, 'usuario_tem_imagem_salva', False) and tem_imagem and not self.imagem_removida_usuario:
            QMessageBox.warning(None, "Remoção de Imagem",
                                "Remova a imagem do usuário e inclua novamente para seguir com a atualização")
            return

        try:        
            cursor = self.connection.cursor()
            cursor.execute("SELECT COUNT(1) FROM users WHERE id = ?", (self.selected_user_id,))
            user_exists = cursor.fetchone()[0]

            if not user_exists:
                QMessageBox.warning(self, "Aviso", "Usuário não encontrado!")
                return
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao verificar usuário: {str(e)}")
            return

        # Obter os dados da interface
        usuario_nome = self.txt_nome.text()
        usuario_usuario = self.txt_usuario.text()
        usuario_telefone = self.txt_telefone.text()
        usuario_endereco = self.txt_endereco.text()
        usuario_numero = self.txt_numero.text()
        usuario_complemento = self.txt_complemento.text()
        usuario_cidade = self.txt_cidade.text()
        usuario_bairro = self.txt_bairro.text()
        usuario_email = self.txt_email.text()
        usuario_data_nascimento = self.txt_data_nascimento.text()
        usuario_rg = self.txt_rg.text()
        usuario_cpf = self.txt_cpf.text()
        usuario_cnpj = self.txt_cnpj.text()
        usuario_cep = self.txt_cep.text()
        usuario_estado = self.perfil_estado.currentText()
        usuario_senha = self.txt_senha.text()
        usuario_confirmar_senha = self.txt_confirmar_senha.text()

        # Verificar campos obrigatórios
        campos_nao_preenchidos_usuarios = []
        if not usuario_nome: campos_nao_preenchidos_usuarios.append("nome")
        if not usuario_usuario: campos_nao_preenchidos_usuarios.append("usuario")
        if not usuario_telefone: campos_nao_preenchidos_usuarios.append("telefone")
        if not usuario_endereco: campos_nao_preenchidos_usuarios.append("endereco")
        if not usuario_numero: campos_nao_preenchidos_usuarios.append("numero")
        if not usuario_complemento: campos_nao_preenchidos_usuarios.append("complemento")
        if not usuario_cidade: campos_nao_preenchidos_usuarios.append("cidade")
        if not usuario_bairro: campos_nao_preenchidos_usuarios.append("bairro")
        if not usuario_email: campos_nao_preenchidos_usuarios.append("email")
        if not usuario_data_nascimento: campos_nao_preenchidos_usuarios.append("data_nascimento")
        if not usuario_rg: campos_nao_preenchidos_usuarios.append("rg")
        if not usuario_cpf: campos_nao_preenchidos_usuarios.append("cpf")
        if not usuario_cnpj: campos_nao_preenchidos_usuarios.append("cnpj")
        if not usuario_cep: campos_nao_preenchidos_usuarios.append("cep")
        if not usuario_estado: campos_nao_preenchidos_usuarios.append("estado")
        if not usuario_senha: campos_nao_preenchidos_usuarios.append("senha")
        if not usuario_confirmar_senha: campos_nao_preenchidos_usuarios.append("confirmar_senha")

        if campos_nao_preenchidos_usuarios:
            self.exibir_asteriscos_usuarios(campos_nao_preenchidos_usuarios)
            QMessageBox.warning(None, "Aviso", "Todos os campos obrigatórios devem ser preenchidos!")
            return

        if usuario_senha != usuario_confirmar_senha:
            self.exibir_asteriscos_usuarios(["senha", "confirmar_senha"])
            QMessageBox.warning(None, "Aviso", "As senhas não coincidem!")
            return

        if not self.validar_cpf(usuario_cpf):
            self.exibir_asteriscos_usuarios(["cpf"])
            QMessageBox.warning(None, "Aviso", "CPF inválido!")
            return

        if not self.validar_email(usuario_email):
            self.exibir_asteriscos_usuarios(["email"])
            QMessageBox.warning(None, "Aviso", "E-mail inválido!")
            return

        if not self.validar_telefone(usuario_telefone):
            self.exibir_asteriscos_usuarios(["telefone"])
            QMessageBox.warning(None, "Aviso", "Número de telefone inválido!")
            return

        # Obter imagem, se houver
        usuario_imagem = None
        if tem_imagem:
            pixmap = self.label_imagem_usuario.pixmap()
            if pixmap:
                byte_array = QByteArray()
                buffer = QBuffer(byte_array)
                buffer.open(QIODevice.WriteOnly)
                pixmap.save(buffer, "PNG")
                usuario_imagem = str(byte_array.toBase64(), encoding='utf-8')

        # SQL e valores
        if usuario_imagem:
            sql = """
                UPDATE users 
                SET Nome=?, Telefone=?, Endereço=?, Número=?, Cidade=?, Bairro=?, Complemento=?, 
                    Email=?, "Data de Nascimento"=?, RG=?, CPF=?, CNPJ=?, CEP=?, Estado=?, 
                    Senha=?, Imagem=?, "Confirmar Senha"=?
                WHERE id=?
            """
            valores = (
                usuario_nome, usuario_telefone, usuario_endereco, usuario_numero, usuario_cidade, usuario_bairro, usuario_complemento,
                usuario_email, usuario_data_nascimento, usuario_rg, usuario_cpf, usuario_cnpj, usuario_cep, usuario_estado,
                usuario_senha, usuario_imagem, usuario_confirmar_senha, self.selected_user_id
            )
        else:
            sql = """
                UPDATE users 
                SET Nome=?, Telefone=?, Endereço=?, Número=?, Cidade=?, Bairro=?, Complemento=?, 
                    Email=?, "Data de Nascimento"=?, RG=?, CPF=?, CNPJ=?, CEP=?, Estado=?, 
                    Senha=?, "Confirmar Senha"=?
                WHERE id=?
            """
            valores = (
                usuario_nome, usuario_telefone, usuario_endereco, usuario_numero, usuario_cidade, usuario_bairro, usuario_complemento,
                usuario_email, usuario_data_nascimento, usuario_rg, usuario_cpf, usuario_cnpj, usuario_cep, usuario_estado,
                usuario_senha, usuario_confirmar_senha, self.selected_user_id
            )

        try:
            with self.connection:
                cursor = self.connection.cursor()
                cursor.execute(sql, valores)
            QMessageBox.information(self, "Sucesso", "Usuário atualizado com sucesso!")
            self.limpar_campos_após_atualizar_usuario()
            self.is_editing = False
            self.selected_user_id = None
            descricao = f"O usuário {usuario_usuario} foi atualizado com sucesso"
            self.registrar_historico_usuarios("Atualização de Usuário", descricao)
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao atualizar o usuário: {str(e)}")
      
#*********************************************************************************************************************
    def mostrar_tabela_usuarios(self):
        # Criar uma instância da classe AtualizarUsuario
        self.tabela_usuario_dialogo = AtualizarUsuario(self)
        # Exibir a janela da tabela de usuários
        self.tabela_usuario_dialogo.show()
        self.tabela_usuario_dialogo.listar_usuarios()

#*********************************************************************************************************************
    def carregar_dados_usuario(self, user_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
            usuario = cursor.fetchone()
            
            if usuario:
                # Supondo que o resultado esteja na ordem dos campos
                self.txt_nome.setText(usuario[1])
                self.txt_usuario.setText(usuario[2])
                self.txt_telefone.setText(usuario[3])
                self.txt_endereco.setText(usuario[4])
                self.txt_numero.setText(usuario[5])
                self.txt_complemento.setText(usuario[6])
                self.txt_email.setText(usuario[7])
                self.txt_data_nascimento.setText(usuario[8])
                self.txt_rg.setText(usuario[9])
                self.txt_cpf.setText(usuario[10])
                self.txt_cep.setText(usuario[11])
                self.txt_estado.setText(usuario[12])
                self.txt_senha.setText(usuario[13])
                self.txt_confirmar_senha.setText(usuario[14])
                
                # Se tiver uma imagem, carregar a imagem
                if usuario[15]:
                    self.exibir_imagem_em_label_usuario(usuario[15])

                
                self.is_editing = True
                self.selected_user_id = user_id
            else:
                QMessageBox.warning(self, "Aviso", "Usuário não encontrado!")
        
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao carregar os dados do usuário: {str(e)}")

#*********************************************************************************************************************    

    def validar_cpf(self, cpf):
        # Remover caracteres não numéricos
        cpf = re.sub('[^0-9]', '', cpf)

        # Verificar se o CPF tem 11 dígitos
        if len(cpf) != 11:
            return False

        return True
#*********************************************************************************************************************
    def validar_email(self, email, widget):
        # Expressão regular para e-mail
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(regex, email))


#*********************************************************************************************************************
    def validar_cnpj(self, cnpj):
        # Remover caracteres não numéricos
        cnpj = re.sub('[^0-9]', '', cnpj)

        # Verificar se o CNPJ tem 14 dígitos
        if len(cnpj) != 14:
            return False

        return True

#*********************************************************************************************************************
    def validar_telefone(self, telefone):
        # Remover caracteres não numéricos
        telefone = re.sub('[^0-9]', '', telefone)

        # Verificar se o telefone tem o formato válido
        if len(telefone) != 11:
            return False

        return True
#*********************************************************************************************************************
    def criar_botoes_avancar_voltar(self):
        # Conectar os botões aos slots correspondentes
        self.btn_avancar.clicked.connect(self.avancar_pagina)
        self.btn_retroceder.clicked.connect(self.retroceder_pagina)

        # Definir o estilo para os botões
        estilo_botao_avancar_retroceder = """
        QPushButton {
            color: rgb(255, 255, 255);
            border-radius: 3px;
            font-size: 16px;
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */
            border: 3px solid transparent;
        }
        QPushButton:hover {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */
            color: black;
        }
        """
        self.btn_avancar.setStyleSheet(estilo_botao_avancar_retroceder)
        self.btn_retroceder.setStyleSheet(estilo_botao_avancar_retroceder)
#*********************************************************************************************************************
    def exibir_botao_mostrar_usuarios(self):
        self.tabela_usuario_dialogo.btn_mostrar_usuarios.setVisible(True)
#*********************************************************************************************************************
    def carregar_imagem_usuario(self):
        # Abrir uma caixa de diálogo de seleção de arquivo
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Imagens (*.png *.jpg *.jpeg *.gif)")
        file_dialog.setViewMode(QFileDialog.Detail)
        file_dialog.setFileMode(QFileDialog.ExistingFile)
 
        if file_dialog.exec():
            # Obter o caminho do arquivo selecionado
            file_paths = file_dialog.selectedFiles()[0]
            pixmap = QPixmap(file_paths)
            if file_paths:
                # Carregar a imagem selecionada no caminho do arquivo
                if not pixmap.isNull():
                    # Redimensionar a imagem para o tamanho do QLabel
                    pixmap = pixmap.scaled(self.frame_imagem_cadastro.size(), Qt.KeepAspectRatio)
                    # Definir a imagem no QLabel
                    self.label_imagem_usuario.setPixmap(pixmap)

                else:
                    QMessageBox.warning(self, "Aviso", "Não foi possível carregar a imagem.")
#*********************************************************************************************************************
    def avancar_pagina(self):
        # Armazenar a página atual no histórico de páginas
        self.historico_paginas.append(self.pagina_atual_index)
        
        # Avançar para a próxima página na lista
        self.pagina_atual_index += 1
        if self.pagina_atual_index >= len(self.paginas):
            self.pagina_atual_index = 0  # Voltar para a primeira página se atingir o final da lista
        self.paginas_sistemas.setCurrentWidget(self.paginas[self.pagina_atual_index])
#*********************************************************************************************************************
    def retroceder_pagina(self):
        if self.historico_paginas:
            # Remover a página atual do histórico de páginas
            self.historico_paginas.pop()
            
            # Verificar se há páginas no histórico
            if self.historico_paginas:
                # Retroceder para a página anterior no histórico
                self.pagina_atual_index = self.historico_paginas[-1]
            else:
                # Se não houver mais páginas no histórico, retroceder para a página anterior na lista
                self.pagina_atual_index -= 1
                if self.pagina_atual_index < 0:
                    self.pagina_atual_index = len(self.paginas) - 1
            self.paginas_sistemas.setCurrentWidget(self.paginas[self.pagina_atual_index])
#*********************************************************************************************************************
# Configuração do local
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
#*********************************************************************************************************************
    def formatar_moeda(self):
        sender = self.sender()
        valor = sender.text()

        if valor:
            try:
                # Converte a string para float, substituindo vírgula por ponto
                valor = valor.replace(",", ".")
                valor_float = float(valor)
            except ValueError:
                QMessageBox.warning(self, "Erro", "Valor inválido")
                return

            if valor_float < 10:
                self.mostrar_detalhes_erro()
                return

            # Formata o valor como moeda, agrupando milhares
            valor_formatado = locale.currency(valor_float, grouping=True)

            sender.setText(valor_formatado)
#*********************************************************************************************************************
    def desconectarUsuario(self):   
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setText("Tem certeza que deseja sair?")
        msgBox.setWindowTitle("Aviso")
        
        # Definindo os botões em português
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        
        yes_button = msgBox.button(QMessageBox.Yes)
        yes_button.setText("Sim")
        
        
        no_button = msgBox.button(QMessageBox.No)
        no_button.setText("Não")

        # Mostrar mensagem de confirmação
        resposta = msgBox.exec()

        if resposta == QMessageBox.Yes:
            # Limpar configurações de login
            self.login_window.config.salvar_configuracoes("","",False)

            # Limpar os campos de login e desmarcar "Manter conectado"
            self.login_window.limpar_campos()
            self.login_window.btn_manter_conectado.setChecked(False)

            # Fechar a janela principal e abrir a janela de login
            self.close()
            self.login_window.show()
#*********************************************************************************************************************
    def fazer_login_automatico(self):
        if self.config.verificar_credenciais_salvas():
            usuario = self.config.usuario
            senha = self.config.obter_senha_salva()
            tipo_usuario = self.db.check_user(usuario, senha)
            if tipo_usuario:
                print("Login automático bem sucedido!")
                self.fechar_janela_login_signal.emit(tipo_usuario)
                self.show()  # Mostra a janela principal atual  
#*********************************************************************************************************************
    def fechar_janela_login_delay(self):
        if self.login_window.isVisible():
            self.login_window.close()
        else:
            print("Janela de login não está visível.")

    def fechar_janela_login(self):
        QTimer.singleShot(100, self.fechar_janela_login_delay)
#********************************************************************************************************************* 
    def obter_senha_salva(self):
        try:
            query = "SELECT Senha FROM users WHERE Usuário = ?"
            cursor = self.connection.cursor()
            cursor.execute(query, (self.config.usuario,))
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                return ""
        except Exception as e:
            print("Erro ao obter senha:", e)
            return ""
#*********************************************************************************************************************            
    def carregar_configuracoes(self):
        self.txt_usuario.setText(self.config.usuario if self.config.usuario else "")
        self.login_window.btn_manter_conectado.setChecked(self.config.mantem_conectado)
#*********************************************************************************************************************
    def mostrar_detalhes_erro(self):
        detalhes_msg = QMessageBox()
        detalhes_msg.setIcon(QMessageBox.Warning)
        detalhes_msg.setWindowTitle("Erro")
        detalhes_msg.setText("Não é possível incluir um valor menor que R$ 10,00.")

        ok_btn = QPushButton("OK")
        detalhes_msg.addButton(ok_btn, QMessageBox.RejectRole)

        detalhes_btn = QPushButton("Detalhes")
        detalhes_msg.addButton(detalhes_btn, QMessageBox.ActionRole)

        detalhes_msg.setDefaultButton(ok_btn)
        detalhes_msg.exec()

        if detalhes_msg.clickedButton() == detalhes_btn:
            detalhes_msg_detalhes = QMessageBox()
            detalhes_msg_detalhes.setIcon(QMessageBox.Information)
            detalhes_msg_detalhes.setWindowTitle("Detalhes do Erro")
            detalhes_msg_detalhes.setText("O valor não pode ser menor que R$ 10,00. \n Por favor adicione um valor maior que R$ 10,00")
            detalhes_msg_detalhes.exec()
#*********************************************************************************************************************
    def formatar_porcentagem(self):
        valor = self.txt_desconto_3.text()
        if valor:
            try:
                valor_int = int(float(valor))  # Converte para inteiro, mesmo se digitar "12.0"
            except ValueError:
                QMessageBox.warning(self, "Erro", "Valor inválido")
                return
            if valor_int < 5:
                self.mostrar_erro_desconto()
                return
            valor_formatado = f"{valor_int}%"
            self.txt_desconto_3.setText(valor_formatado)
#*********************************************************************************************************************
    def mostrar_erro_desconto(self):
        detalhes_msg = QMessageBox()
        detalhes_msg.setIcon(QMessageBox.Warning)
        detalhes_msg.setWindowTitle("Erro")
        detalhes_msg.setText("Por favor adicione um valor de desconto correto.")

        ok_btn = QPushButton("OK")
        detalhes_msg.addButton(ok_btn, QMessageBox.RejectRole)

        detalhes_btn = QPushButton("Detalhes")
        detalhes_msg.addButton(detalhes_btn, QMessageBox.ActionRole)

        detalhes_msg.setDefaultButton(ok_btn)
        detalhes_msg.exec()

        if detalhes_msg.clickedButton() == detalhes_btn:
            detalhes_msg_detalhes = QMessageBox()
            detalhes_msg_detalhes.setIcon(QMessageBox.Information)
            detalhes_msg_detalhes.setWindowTitle("Detalhes do Erro")
            detalhes_msg_detalhes.setText("O seu desconto não pode ser menor que 5%. \n Somente descontos maiores serão válidos para esta ação")
            detalhes_msg_detalhes.exec()
#*********************************************************************************************************************
    def subscribe_user(self):
        # Verificar se está no modo de edição
        if self.is_editing:
            QMessageBox.warning(None, "Modo de Edição Ativo", 
                                "Você está editando um usuário.\nAtualize o cadastro em vez de criar um novo.")
            return

        try:
            db = DataBase()
            db.connecta()

            # Coleta de dados dos campos
            nome = self.txt_nome.text().strip()
            usuario = self.gerar_codigo_usuarios()
            senha = self.txt_senha.text()
            confirmar_senha = self.txt_confirmar_senha.text()
            cep = self.txt_cep.text().strip()
            endereco = self.txt_endereco.text().strip()
            numero = self.txt_numero.text().strip()
            cidade = self.txt_cidade.text().strip()
            bairro = self.txt_bairro.text().strip()
            estado = self.perfil_estado.currentText()
            complemento = self.txt_complemento.text().strip()
            telefone = self.txt_telefone.text().strip()
            email = self.txt_email.text().strip()
            data_nascimento = self.txt_data_nascimento.text().strip()
            rg = self.txt_rg.text().strip()
            cpf = self.txt_cpf.text().strip()
            cnpj = self.txt_cnpj.text().strip()
            imagem = self.converter_imagem_usuario()
            segredo = "Não Cadastrado"
            acesso = self.perfil_usuarios.currentText()

            usuario_logado = self.config.obter_usuario_logado()
            db.salvar_usuario_logado(usuario_logado)

            # Validação de campos obrigatórios
            campos_vazios = []
            for campo, widget in self.campos_obrigatorios_usuarios.items():
                valor = widget.currentText() if isinstance(widget, QComboBox) else widget.text()
                if valor.strip() == "":
                    campos_vazios.append(campo)

            if campos_vazios:
                self.exibir_asteriscos_usuarios(campos_vazios)
                QMessageBox.warning(None, "Erro", f"O campo {campos_vazios[0]} é obrigatório.")
                return

            # Validação de senha
            if senha != confirmar_senha:
                self.exibir_asteriscos_usuarios(["senha", "confirmar senha"])
                QMessageBox.warning(None, "Erro", "As senhas não coincidem.")
                return
            
            # Verifica se a senha é válida
            if not self.configuracoes_senha.validar_senha(senha,confirmar_senha):
                self.exibir_asteriscos_usuarios(["senha", "confirmar senha"])
                QMessageBox.warning(None, "Erro", "A senha deve conter pelo menos 8 caracteres, incluindo letras e números.")
                return
                

            # Validação de e-mail
            if not self.email_valido(email):
                self.exibir_asteriscos_usuarios(["email"])
                QMessageBox.warning(None, "Erro", "E-mail inválido.")
                return
            

            # Verificar se usuário já existe
            campo_duplicado = db.user_exists(usuario,telefone,email,rg,cpf,cnpj)
            if campo_duplicado:
                mensagens = {
                    'usuario': f"Já existe um usuário cadastrado com o login {usuario}.",
                    'telefone': f"Já existe um usuário cadastrado com o telefone {telefone}.",
                    'email': f"Já existe um usuário cadastrado com o e-mail {email}.",
                    'rg': f"Já existe um usuário cadastrado com o RG {rg}.",
                    'cpf': f"Já existe um usuário cadastrado com o CPF {cpf}.",
                    'cnpj': f"Já existe um usuário cadastrado com o CNPJ {cnpj}.",
                }
                # Exibe o asterisco no campo duplicado
                self.exibir_asteriscos_usuarios([campo_duplicado])
                # Exibe a mensagem de erro
                QMessageBox.warning(None, "Erro de Cadastro", mensagens[campo_duplicado])
                return
                

            # Inserir novo usuário
            db.insert_user(
                nome=nome,
                usuario=usuario,
                senha=senha,
                confirmar_senha=confirmar_senha,
                cep=cep,
                endereco=endereco,
                numero=numero,
                cidade=cidade,
                bairro=bairro,
                estado=estado,
                complemento=complemento,
                telefone=telefone,
                email=email,
                data_nascimento=data_nascimento,
                rg=rg,
                cpf=cpf,
                cnpj=cnpj,
                segredo=segredo,
                imagem=imagem,
                usuario_logado=usuario_logado,
                acesso=acesso,
            )

            self.registrar_historico_usuarios("Cadastro de Usuários", f"Usuário {usuario} cadastrado com sucesso.")
            QMessageBox.information(None, "Cadastro de Usuário", "Cadastro realizado com sucesso.")

            '''db.update_dados_cliente_juridico_endereco(
                nome_cliente=nome,
                cnpj=cnpj,
                telefone=telefone,
                cep=cep,
                endereco=endereco,
                numero=numero,
                cidade=cidade,
                bairro=bairro
            )'''


            # Limpar campos após cadastro
            self.txt_nome.clear()
            self.txt_usuario.clear()
            self.txt_senha.clear()
            self.txt_confirmar_senha.clear()
            self.txt_cpf.clear()
            self.txt_cnpj.clear()
            self.txt_email.clear()
            self.txt_numero.clear()
            self.txt_endereco.clear()
            self.txt_bairro.clear()
            self.txt_cidade.clear()
            self.txt_cnpj.clear()
            self.txt_cep.clear()
            self.txt_complemento.clear()
            self.txt_rg.clear()
            self.txt_telefone.clear()
            self.txt_data_nascimento.clear()
            self.perfil_estado.setCurrentIndex(0)
            self.perfil_usuarios.setCurrentIndex(0)
            self.label_imagem_usuario.clear()

        except Exception as e:
            QMessageBox.critical(None, "Erro", f"Erro ao cadastrar usuário: {str(e)}")


    def buscar_cep(self,cep:str):
        cep = cep.replace("-", "").strip()
        if len(cep) != 8 or not cep.isdigit():
            QMessageBox.warning(None, "ERRO", "CEP inválido")
            return
        try:
            url = f"https://viacep.com.br/ws/{cep}/json/"
            resposta = requests.get(url)
            if resposta.status_code == 200:
                dados = resposta.json()
                if "erro"  in dados:
                    QMessageBox.warning(None, "ERRO", "CEP não encontrado")
                    return None
                return dados
            else:
                QMessageBox.warning(None,"Erro de conexão","Não foi possível consultar o CEP")
                return None
        except Exception as e:
            QMessageBox.warning(None,"Erro ao consultar CEP",f"Erro: {str(e)}")
            return None

    def preencher_campos_cep(self, dados):
        if dados is None:
            return  # Não faz nada se não tem dados
        
        self.txt_endereco.setText(dados.get("logradouro", ""))
        self.txt_bairro.setText(dados.get("bairro", ""))
        self.txt_cidade.setText(dados.get("localidade", ""))


        complemento = dados.get("complemento", "")
        if any(char.isdigit() for char in complemento):
            self.txt_numero.setText(complemento)
        #self.txt_complemento.setText(complemento)
        # Só ajustar o estado, já que é o único campo extra que você tem
        estado = dados.get("uf", "")
        index_estado = self.perfil_estado.findText(estado)
        if index_estado != -1:
            self.perfil_estado.setCurrentIndex(index_estado)


    def on_cep_editing_finished(self):
        cep_digitado = self.txt_cep.text()
        dados_cep = self.buscar_cep(cep_digitado)
        if dados_cep:
            self.preencher_campos_cep(dados_cep)

    def eliminar_campos_usuarios(self):
        # Limpar campos de texto
        self.txt_nome.clear()
        self.txt_usuario.clear()
        self.txt_telefone.clear()
        self.txt_endereco.clear()
        self.txt_cidade.clear()
        self.txt_bairro.clear()
        self.txt_numero.clear()
        self.txt_complemento.clear()
        self.txt_email.clear()
        self.txt_data_nascimento.clear()
        self.txt_rg.clear()
        self.txt_cpf.clear()
        self.txt_cep.clear()
        self.txt_senha.clear()
        self.txt_cnpj.clear()
        self.txt_confirmar_senha.clear()
        # Limpar campos de combo box
        self.perfil_estado.setCurrentIndex(0)  # Se for um combo box, o índice padrão é 0 (ou o valor inicial)
        self.perfil_usuarios.setCurrentIndex(0)
        frame = self.frame_imagem_cadastro
        if frame:
            if frame is not None:
                for widget in frame.children():
                    if isinstance(widget,QLabel) and widget.pixmap():
                        widget.clear()
                        widget.setPixmap(QPixmap())
                        widget.hide()
                        print("Imagem do usuário removida com sucesso!!")
                       
            else:
                QMessageBox.warning(None, "Erro","Não foi possível remover a imagem do usuário\n"
                                                "Tente remover pelo botão  remover imagem")

        QMessageBox.information(None,"Sucesso","Todos os campos foram limpos com sucesso! ")
#*********************************************************************************************************************
    def converter_imagem_usuario(self):
        # Verificar se há uma imagem carregada no QLabel
        if self.label_imagem_usuario.pixmap():
            # Obter o pixmap da imagem
            pixmap = self.label_imagem_usuario.pixmap()
            # Obter a imagem como uma sequência de bytes
            bytes_array = QByteArray()
            buffer = QBuffer(bytes_array)
            buffer.open(QIODevice.WriteOnly)
            pixmap.save(buffer, "PNG")  # Salvar a imagem como PNG
            # Retornar a sequência de bytes da imagem
            return bytes_array.toBase64().data()

        return None  # Retornar None se não houver imagem carregada
#*********************************************************************************************************************    
    def exibir_imagem_em_label_usuario(self, imagem_base64):
        if imagem_base64:
            try:
                imagem_bytes = base64.b64decode(imagem_base64)
                imagem = QImage.fromData(imagem_bytes)
                pixmap = QPixmap.fromImage(imagem)
                if not pixmap.isNull():
                    self.label_imagem_usuario.setPixmap(pixmap.scaled(
                        self.label_imagem_usuario.size(),
                        Qt.KeepAspectRatio,
                        Qt.SmoothTransformation
                    ))
                    print("Imagem definida no QLabel")
                else:
                    print("Pixmap está nulo. Imagem pode estar corrompida.")
            except Exception as e:
                print("Erro ao decodificar imagem:", e)
        else:
            print("Imagem base64 vazia ou inválida.")
#*********************************************************************************************************************
    def erros_frames_produtos(self):
        print("Inicializando erros_frames_produtos")
        # Definir os campos obrigatórios e seus respectivos frames de erro
        self.campos_obrigatorios = {
            'produto': self.txt_produto,
            'quantidade': self.txt_quantidade,
            'valor_produto': self.txt_valor_produto_3,
            'data_cadastro': self.dateEdit_3,
            'cliente': self.txt_cliente_3,
            'descricao': self.txt_descricao_produto_3
        }

        self.frames_erros = {
            'produto': self.frame_erro_produto,
            'quantidade': self.frame_erro_quantidade,
            'valor_produto': self.frame_erro_valor_produto,
            'data_cadastro': self.frame_erro_data_cadastro,
            'cliente': self.frame_erro_cliente,
            'descricao': self.frame_erro_descricao
        }

        # Esconder todos os frames de erro inicialmente
        for frame in self.frames_erros.values():
            frame.hide()

        # Conectar o sinal focusIn ao método esconder_asteriscos
        for widget in self.campos_obrigatorios.values():
            widget.installEventFilter(self)
#*********************************************************************************************************************
    def exibir_asteriscos_produtos(self, campos_nao_preenchidos):
        for campo in campos_nao_preenchidos:
            frame = self.frames_erros.get(campo)
            if frame is None:
                print(f"[ERRO] Campo '{campo}' não tem frame correspondente! ")
                continue
            name_label_asterisco_produtos = f'label_asterisco_produtos_{campo}'

            if not hasattr(self,name_label_asterisco_produtos):
                #Define o QLabel de asterisco correspondente ao campo
                label = QLabel(frame)
                #Carregar a imagem do frame do asterisco, redimensionando para 12x12, mantendo a proporção original
                asterisco_produtos_pixmap = QPixmap("imagens/Imagem1.png").scaled(12,12,Qt.KeepAspectRatio, Qt.SmoothTransformation)
                # Definir o tamanho do QLabel para ser o mesmo que o QFrame
                label.setPixmap(asterisco_produtos_pixmap)
                # Alinhar o QLabel ao centro do frame
                label.setAlignment(Qt.AlignCenter)
                # Aplicar um layout ao frame
                layout = QVBoxLayout(frame)
                layout.setContentsMargins(0,0,0,0) # Remover margens
                # Adicionar o QLabel ao layout
                layout.addWidget(label)
                setattr(self, name_label_asterisco_produtos,label) # Armazena a referência do QLabel
                # Adiciona o print para verificar se o asterisco foi realmente adicionado
                print(f"Asterisco adicionado ao campo de: {campo}")
            else:
                label = getattr(self, name_label_asterisco_produtos)
                label.show()  # Exibir o QLabel do asterisco

            # Exibir o frame de erro
            frame.show()

    def esconder_asteriscos_produtos(self):
        for campo, frame in self.frames_erros.items():
            frame.hide()
            label_name = f'label_asterisco_produtos_{campo}'
            if hasattr(self, label_name):
                getattr(self, label_name).hide()  # Esconder o QLabel do asterisco
#*********************************************************************************************************************
    def erros_frames_usuarios(self):
        print("Inicializando erros_frames_usuarios")
        self.campos_obrigatorios_usuarios = {
        'nome': self.txt_nome,
        'usuario': self.txt_usuario,
        'telefone': self.txt_telefone,
        'endereco': self.txt_endereco,            # <--- corrigido
        'numero': self.txt_numero,          # <--- corrigido
        'complemento': self.txt_complemento,
        'email': self.txt_email,               # <--- corrigido
        'data_nascimento': self.txt_data_nascimento,  # <--- corrigido
        'rg': self.txt_rg,
        'cpf': self.txt_cpf,
        'cnpj': self.txt_cnpj,
        'cep': self.txt_cep,
        'estado': self.perfil_estado,
        'senha': self.txt_senha,
        'confirmar senha': self.txt_confirmar_senha,
        'perfil': self.perfil_usuarios
        }

        self.frames_erros_usuarios = {
            'nome': self.frame_erro_nome,
            'usuario': self.frame_erro_usuario,
            'telefone': self.frame_erro_telefone,
            'endereco': self.frame_erro_endereco,
            'cidade': self.frame_erro_cidade,
            'bairro': self.frame_erro_bairro,
            'numero': self.frame_erro_numero,
            'complemento': self.frame_erro_complemento,
            'email': self.frame_erro_email,
            'data_nascimento': self.frame_data_nascimento,
            'rg': self.frame_erro_rg,
            'cpf': self.frame_erro_cpf,
            'cnpj': self.frame_erro_cnpj,
            'cep': self.frame_erro_cep,
            'estado': self.frame_erro_estado,
            'senha': self.frame_senha,
            'confirmar senha': self.frame_confirmar_senha,
            'perfil': self.frame_erro_perfil
        }

        # Esconder todos os frames de erro inicialmente
        for frame in self.frames_erros_usuarios.values():
            frame.hide()

        # Conectar o sinal focusIn ao método esconder_asteriscos
        for widget in self.campos_obrigatorios_usuarios.values():
            widget.installEventFilter(self)
#*********************************************************************************************************************
    def exibir_asteriscos_usuarios(self, campos_nao_preenchidos_usuarios):
        for campo in campos_nao_preenchidos_usuarios:
            frame = self.frames_erros_usuarios.get(campo)
            if frame is None:
                print(f"[ERRO] Campo '{campo}' não tem frame correspondente!")
                continue

            name_label_asterisco = f'label_asterisco_usuarios_{campo}'

            if not hasattr(self,name_label_asterisco):
                # Define o QLabel para o asterisco
                label = QLabel(frame)
                # Carregar a imagem do asterisco, redimensionando para 12x12, mantendo a proporção original
                asterisco_pixmap = QPixmap("imagens/Imagem1.png").scaled(12, 12, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                # Definir o tamanho do QLabel para ser o mesmo que o QFrame
                label.setPixmap(asterisco_pixmap)
                # Alinhar o QLabel ao centro do frame
                label.setAlignment(Qt.AlignCenter)
                # Aplicar um layout ao frame
                layout = QVBoxLayout(frame)
                layout.setContentsMargins(0, 0, 0, 0)  # Remove margens
                # Adicionar o QLabel ao layout
                layout.addWidget(label)
                setattr(self, name_label_asterisco, label)  # Armazena a referência do QLabel
                # Adiciona o print para verificar se o asterisco foi realmente adicionado
                print(f"Asterisco adicionado ao frame de: {campo}")
            else:
                label = getattr(self, name_label_asterisco)
                label.show()  # Exibir o QLabel do asterisco
            
            # Exibir o frame de erro
            frame.show()
#*********************************************************************************************************************
    def esconder_asteriscos_usuarios(self):
        for campo, frame in self.frames_erros_usuarios.items():
            frame.hide()
            label_name = f'label_asterisco_usuarios_{campo}'
            if hasattr(self, label_name):
                getattr(self, label_name).hide()
#*********************************************************************************************************************
    def eventFilter(self, obj, event):
        if event.type() == QEvent.FocusIn:
            # Esconder somente o erro do campo de USUÁRIO que recebeu foco
            for campo, widget in self.campos_obrigatorios_usuarios.items():
                if obj is widget:
                    frame = self.frames_erros_usuarios.get(campo)
                    if frame:
                        frame.hide()
                    label_name = f'label_asterisco_usuarios_{campo}'
                    if hasattr(self, label_name):
                        getattr(self, label_name).hide()
                    break 
            # Esconder somente o erro do campo de PRODUTO que recebeu foco
            for campo, widget in self.campos_obrigatorios.items():
                if obj is widget:
                    frame = self.frames_erros.get(campo)
                    if frame:
                        frame.hide()
                    label_name = f'label_asterisco_produtos{campo}'
                    if hasattr(self, label_name):
                        getattr(self, label_name).hide()
                    break
        return super().eventFilter(obj, event)
#*********************************************************************************************************************  
    def atualizar_valores_frames_na_hora_do_cadastro(self, quantidade, valor_do_desconto, valor_com_desconto):
        # Formatar os valores corretamente
        valor_com_desconto_formatado = locale.currency(valor_com_desconto, grouping=True)

        valor_do_desconto_formatado = (
            "Sem desconto" if valor_do_desconto == 0 else locale.currency(valor_do_desconto, grouping=True)
        )

        valor_total_formatado = locale.currency(valor_com_desconto + valor_do_desconto, grouping=True)

        # Atualizar os textos das LABELS (não dos frames!)
        self.label_valor_desconto.setText(valor_com_desconto_formatado)
        self.label_valor_do_desconto.setText(valor_do_desconto_formatado)
        self.label_quantidade.setText("{:.0f}".format(quantidade))
        self.label_valor_total_produtos.setText(valor_total_formatado)

        # Garantir que os textos fiquem centralizados nos labels
        self.label_valor_total_produtos.setAlignment(Qt.AlignCenter)
        self.label_valor_do_desconto.setAlignment(Qt.AlignCenter)
        self.label_valor_desconto.setAlignment(Qt.AlignCenter)
        self.label_quantidade.setAlignment(Qt.AlignCenter)
#*********************************************************************************************************************
    def confirmar_produtos(self):
        if self.is_editing_produto:
            QMessageBox.warning(None, "Modo de Edição Ativo",
                                "Você está editando um produto.\nAtualize o produto em vez de criar um novo.")
            return
        # Verificar se há produtos pendentes para confirmar
        if not self.produtos_pendentes:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Erro")  
            msg.setText("Não há produtos preenchidos para confirmar.")
            msg.exec()
            return None
        
        

        # Verificar se todos os campos obrigatórios estão preenchidos
        if not self.campos_obrigatorios_preenchidos():
            return
            
        # Verificar se a imagem está carregada
        if not self.imagem_carregada_produto:
            # Perguntar ao usuário se ele deseja seguir sem uma imagem
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Question)
            msgBox.setText("O produto não contém imagem. Deseja confirmar mesmo assim?")
            msgBox.setWindowTitle("Aviso")

            # Adicionando os botões de forma apropriada
            button_sim = msgBox.addButton("Sim", QMessageBox.YesRole)
            button_nao = msgBox.addButton("Não", QMessageBox.NoRole)

            resposta = msgBox.exec()

            if msgBox.clickedButton() == button_nao:
                return
                
        # Perguntar ao usuário se ele tem certeza de que deseja cadastrar o produto
        confirmar_msg = QMessageBox()
        confirmar_msg.setIcon(QMessageBox.Question)
        confirmar_msg.setWindowTitle("Confirmação")
        confirmar_msg.setText("Tem certeza de que deseja cadastrar o produto?")

        button_sim = confirmar_msg.addButton("Sim", QMessageBox.YesRole)
        button_nao = confirmar_msg.addButton("Não", QMessageBox.NoRole)
        
        resposta = confirmar_msg.exec()

        if confirmar_msg.clickedButton() == button_nao:
            return
                
        # Salvar os produtos pendentes no banco de dados
        for produto in self.produtos_pendentes:
            self.inserir_produto_no_bd(produto)

        # Limpar a lista de produtos pendentes
        self.produtos_pendentes.clear()

        # Limpar os campos de entrada
        self.limpar_campos_produtos()
        
        # Limpar a imagem
        self.label_imagem_produto.clear()
        self.imagem_carregada_produto = None

        self.dateEdit_3.setDate(QDate.currentDate())  # Define a data atual

        # Exibir mensagem de sucesso apenas se todos os campos estiverem preenchidos
        self.mostrar_mensagem_sucesso()
#*********************************************************************************************************************
    def inserir_produto_no_bd(self, produto_info,registrar_historico=True):
        try:
            db = DataBase()
            db.connecta()
            cursor = db.connection.cursor()
            
             #  Verificar se o cliente existe antes de continuar
            cursor.execute("""
                SELECT 1 FROM clientes_juridicos WHERE "Nome do Cliente" = ?
            """, (produto_info["cliente"],))
            cliente_existe = cursor.fetchone()
            
            #  Cliente existe, continuar cadastro do produto
            if not cliente_existe:
                return # Impede o restante do código de continuar

            # Formatando o valor_real com o símbolo "R$" e duas casas decimais
            valor_real_formatado = produto_info['valor_produto']

            # Se o desconto for zero, inserir "Sem desconto", caso contrário, formatar com porcentagem
            desconto_formatado = "Sem desconto" if produto_info['desconto'] == 0 else f"{int(produto_info['desconto'])}%"

            # Carregar a imagem e convertê-la para bytes
            imagem_bytes = None
            if self.imagem_carregada_produto:
                pixmap = self.label_imagem_produto.pixmap()
                byte_array = QByteArray()
                buffer = QBuffer(byte_array)
                buffer.open(QIODevice.WriteOnly)
                pixmap.save(buffer, "PNG")
                imagem_bytes = byte_array.toBase64().data().decode()

            usuario_logado = self.get_usuario_logado()  # Obtenha o usuário logado aqui

            # Inserindo os dados formatados no banco de dados, incluindo a imagem
            db.insert_product(
                produto_info["produto"],
                produto_info["quantidade"],
                valor_real_formatado,
                desconto_formatado,
                produto_info["valor_total"],
                produto_info["data_cadastro"],
                produto_info["codigo_item"],
                produto_info["cliente"],
                produto_info["descricao_produto"],
                usuario_logado,  # Passando o usuário logado
                imagem_bytes  # Adicionando a imagem aqui
            )
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao cadastrar produto: {str(e)}")
            
        # Atualizar "Valor Gasto Total" e "Última Compra"   
        cursor = db.connection.cursor()
        cursor.execute("""
            SELECT "Valor Total" FROM products WHERE "Cliente" = ?
        """,(produto_info["cliente"],))
        
        linhas = cursor.fetchall()
        valor_total_cliente = 0.0
        
        for linha in linhas:
            valor_str = str(linha[0]).replace("R$", "").replace(".", "").replace(",", ".")
            try:
                valor_total_cliente += float(valor_str)
            except:
                pass
            
        # 2. Formatar para padrão BR
        valor_total_formatado = f"R$ {valor_total_cliente:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

        # 3. Atualizar a tabela clientes_juridicos
        cursor.execute("""
            UPDATE clientes_juridicos
            SET "Valor Gasto Total" = ?, "Última Compra" = ?
            WHERE "Nome do Cliente" = ?
        """, (valor_total_formatado, produto_info["data_cadastro"], produto_info["cliente"]))

        db.connection.commit()

        if registrar_historico:
            # Registrar no histórico após a inserção do produto
            descricao = f"Produto {produto_info['produto']} foi cadastrado com quantidade {produto_info['quantidade']} e valor {valor_real_formatado}."
            self.registrar_historico("Cadastro de Produto", descricao)

#*********************************************************************************************************************
    def subscribe_produto(self): 
        # Verificar se todos os campos obrigatórios estão preenchidos
        campos_nao_preenchidos = [
            campo for campo, widget in self.campos_obrigatorios.items()
            if not widget.text()
        ]

        if campos_nao_preenchidos:
            self.exibir_asteriscos_produtos(campos_nao_preenchidos)  # Mostrar os asteriscos nos campos obrigatórios
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Erro")
            msg.setText("Todos os campos obrigatórios precisam ser preenchidos.")
            msg.exec()
            return
        
        # Verificar se o nome do produto começa com um número ou caractere especial
        if re.match(r'^[\d\W]', self.txt_produto.text()):
            self.exibir_asteriscos_produtos(["produto"])  # Mostrar o asterisco ao lado do campo Produto

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Erro")
            msg.setText("O nome do produto não pode começar com um número ou caractere especial.")
            msg.exec()
            return
        else:
            self.esconder_asteriscos_produtos()  # Esconder os asteriscos se não houver erro

        # Verificar se não estamos no modo de edição
        if not self.is_editing_produto:
            codigo_item = self.gerar_codigo_aleatorio()
            self.txt_codigo_item.setText(codigo_item)

        # Obter os valores dos campos
        valor_produto_str = self.txt_valor_produto_3.text().replace('R$', '').replace('.', '').replace(',', '.').strip()
        if not valor_produto_str:
            self.txt_valor_produto_3.setText("Não Cadastrado")
            valor_produto = 0.0
        else:
            valor_produto = float(valor_produto_str)

        quantidade_str = self.txt_quantidade.text().strip()
        if not quantidade_str:
            self.txt_quantidade.setText("Não Cadastrado")
            quantidade = 0
        else:
            quantidade = int(quantidade_str)

        desconto_str = self.txt_desconto_3.text().replace('%', '').strip().replace(',', '.')  # Removendo o símbolo de porcentagem
        desconto = float(desconto_str) if desconto_str and desconto_str != 'Sem desconto' else 0.0

        # Atualizar o valor do desconto na QLineEdit
        self.txt_desconto_3.setText("Sem desconto" if desconto == 0 else f"{int(desconto)}%")

        # Atualizar o valor do desconto na QLineEdit se não tiver desconto
        if desconto == 0:
            self.txt_desconto_3.setText("Sem desconto")
            desconto = 0.0  # Definir desconto como zero para cálculo e banco de dados

        # Calcular o valor total do produto antes do desconto
        valor_total = quantidade * valor_produto
        valor_desconto = valor_total * (desconto / 100) # Cálculo usando porcentagem real
        valor_com_desconto = valor_total - valor_desconto

        # Formatando o valor para padrão nacional
        valor_formatado = f"R$ {valor_produto:,.2f}".replace('.', '#').replace(',', '.').replace('#', ',')
        valor_total_formatado = f"R$ {valor_com_desconto:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

        # Adicionar os dados do produto aos produtos pendentes
        produto_info = {
            "produto": self.txt_produto.text(),
            "quantidade": quantidade,
            "valor_produto": valor_formatado,   
            "desconto": desconto,
            "valor_total": valor_total_formatado,
            "data_cadastro": self.dateEdit_3.date().toString("dd/MM/yyyy"),
            "codigo_item": self.txt_codigo_item.text(),
            "cliente": self.txt_cliente_3.text(),
            "descricao_produto": self.txt_descricao_produto_3.text()
        }
         # Verificar se o cliente existe antes de adicionar
        db = DataBase()
        db.connecta()
        cursor = db.connection.cursor()
        cursor.execute("""
                SELECT 1 FROM clientes_juridicos WHERE "Nome do Cliente" = ?
        """,(produto_info["cliente"],))
        clientes_existe = cursor.fetchone()

        if not clientes_existe:
            QMessageBox.warning(
                None,"Cliente não Encontrado",
                f"O cliente {produto_info["cliente"]} precisa estar cadastrado antes de adicionar um produto"
            )
            return
            

        if not self.is_editing_produto:
            self.produtos_pendentes.clear() # Limpa produtos anteriores inválidos
            self.produtos_pendentes.append(produto_info)
        else:
            # Apenas cálculo foi feito, mas o produto não será adicionado
            pass
        # Retornar os valores calculados para exibição
        return quantidade, valor_desconto, valor_com_desconto
#*********************************************************************************************************************
    def get_usuario_logado(self):
        # Obtenha o usuário logado das configurações
        return self.config.obter_usuario_logado()
#*********************************************************************************************************************
    def verificar_alteracoes_produto(self, produto_original):
        try:
            valor_produto = float(self.txt_valor_produto_3.text().replace('R$', '').replace('.', '').replace(',', '.').strip())
        except ValueError:
            valor_produto = 0.0

        try:
            desconto_str = self.txt_desconto_3.text().replace('%', '').replace(',', '.').strip()
            desconto = float(desconto_str) if desconto_str and desconto_str.lower() != 'sem desconto' else 0.0
        except ValueError:
            desconto = 0.0

        produto_atual = {
            "produto": self.txt_produto.text().strip(),
            "quantidade": int(self.txt_quantidade.text()) if self.txt_quantidade.text().isdigit() else 0,
            "valor_produto": round(valor_produto, 2),
            "desconto": round(desconto, 2),
            "data_cadastro": self.dateEdit_3.date().toString("dd/MM/yyyy"),
            "codigo_item": self.txt_codigo_item.text().strip(),
            "cliente": self.txt_cliente_3.text().strip(),
            "descricao_produto": self.txt_descricao_produto_3.text().strip()
        }

        print("Produto Original:", produto_original)
        print("Produto Atual   :", produto_atual)

        for chave in produto_atual:
            valor_original = produto_original.get(chave)
            valor_atual = produto_atual[chave]
            if valor_original != valor_atual:
                print(f"[ALTERADO] Campo '{chave}': Original = {valor_original}, Atual = {valor_atual}")
                return True

        return False

#*********************************************************************************************************************
    def exibir_tabela_produtos(self):
        dialog_atualizacao = AtualizarProduto(self)
        dialog_atualizacao.exec()
#*********************************************************************************************************************
    def adicionar_produto(self):
        # Verificar se todos os campos estão preenchidos
        campos_preenchidos = all([
            self.txt_produto.text().strip(),
            self.txt_quantidade.text().strip(),
            self.txt_valor_produto_3.text().strip(),
            self.dateEdit_3.date().isValid(),
            self.txt_cliente_3.text().strip(),
            self.txt_descricao_produto_3.text().strip()
        ])

        # Gerar código automaticamente se estiver vazio
        if campos_preenchidos and (not self.txt_codigo_item.text().strip() or self.txt_codigo_item.text() == "0"):
            self.txt_codigo_item.setText(self.gerar_codigo_aleatorio())

        produto_original = self.produto_selecionado if hasattr(self, 'produto_selecionado') else None
        produto_info = self.subscribe_produto()

        if produto_info is not None:
            quantidade, valor_do_desconto, valor_com_desconto = produto_info

            # Verificar se houve alteração
            if produto_original and not self.verificar_alteracoes_produto(produto_original):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Informação")
                msg.setText("Nenhuma alteração foi feita no produto.")
                msg.exec()
                return
            
            self.atualizar_valores_frames_na_hora_do_cadastro(quantidade, valor_do_desconto, valor_com_desconto)

            # Limpar produto selecionado após a adição
            self.produto_selecionado = None
    
#*********************************************************************************************************************    
    def gerar_codigo_aleatorio(self, length=12):
        caracteres = string.ascii_uppercase + string.digits
        codigo_aleatorio = ''.join(random.choice(caracteres) for _ in range(length))
        return codigo_aleatorio
#*********************************************************************************************************************
    def gerar_codigo_usuarios(self, length=7,prefixo="SIG"):
        caracteres = string.ascii_uppercase + string.digits
        tentativa_maxima = 1000  # Para evitar loop infinito
        for _ in range(tentativa_maxima):
            codigo_aleatorio = ''.join(random.choice(caracteres) for _ in range(length - len(prefixo)))
            return codigo_aleatorio
#*********************************************************************************************************************
    def selecionar_produto_tabela(self):
        produto = self.obter_produto_selecionado()

        if produto and produto.imagem_caminho:
            pixmap = QPixmap(produto.imagem_caminho)
            if not pixmap.isNull():
                self.limpar_imagem_produto()  # Limpar imagem anterior
                self.label_imagem_produto.setPixmap(pixmap)
                self.label_imagem_produto.show()
                self.imagem_carregada_produto = True
            else:
                self.limpar_imagem_produto()
                self.imagem_carregada_produto = False
        else:
            self.limpar_imagem_produto()
#*********************************************************************************************************************
    def retirar_imagem_produto(self):
        frame = self.frame_imagem_produto_3
        if frame is not None:
            for widget in frame.children():
                if isinstance(widget, QLabel) and widget.pixmap() is not None and not widget.pixmap().isNull():
                    widget.clear()  # Limpar o QLabel
                    widget.setPixmap(QPixmap())  # Definir um pixmap vazio ou padrão
                    widget.hide()  # Esconder o QLabel para garantir que não fique visível
                    print("Imagem removida com sucesso")
                    msg_box = QMessageBox(QMessageBox.Information, "Sucesso", "Imagem removida com sucesso")
                    msg_box.exec()
                    return
        print("Não há imagem do produto para remover.")
        msg_box = QMessageBox(QMessageBox.Warning, "Erro", "Não há imagem para remover")
        msg_box.exec()
#*********************************************************************************************************************
    def retirar_imagem_usuario(self):
        frame = self.frame_imagem_cadastro
        if frame is not None:
            for widget in frame.children():
                if isinstance(widget,QLabel) and widget.pixmap() is not None and not widget.pixmap().isNull():
                    widget.clear()
                    widget.setPixmap(QPixmap())
                    widget.hide()
                    self.imagem_removida_usuario = True
                    print("Imagem removida do usuário com sucesso")
                    msg_box = QMessageBox(QMessageBox.Information, "Sucesso", "Imagem removida do usuário com sucesso")
                    msg_box.exec()
                    return
        print("Não há imagem do usuário para remover.")
        msg_box = QMessageBox(QMessageBox.Warning, "Erro", "Não há imagem do usuário para remover")
        msg_box.exec()
#*********************************************************************************************************************
    def carregar_imagem_produto(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Selecionar Imagem", "", "Imagens (*.png *.xpm *.jpg *.gif);;Todos os Arquivos (*)", options=options)
        
        if fileName:
            pixmap = QPixmap(fileName)
            if not pixmap.isNull():
                self.limpar_imagem_produto()  # Limpar qualquer QLabel existente no frame

                # Verificar se já existe um QLabel para a imagem
                label_imagem = None
                for widget in self.frame_imagem_produto_3.children():
                    if isinstance(widget, QLabel):
                        label_imagem = widget
                        break

                # Se não houver QLabel, criar um novo
                if label_imagem is None:
                    label_imagem = QLabel(self.frame_imagem_produto_3)
                    label_imagem.setObjectName("label_imagem_produto")

                # Definir tamanho do QLabel para ser o mesmo que o QFrame
                frame_size = self.frame_imagem_produto_3.size()
                label_imagem.setFixedSize(frame_size.width(), frame_size.height())

                # Redimensionar o pixmap para se ajustar ao QLabel
                pixmap = pixmap.scaled(label_imagem.width(), label_imagem.height(), Qt.KeepAspectRatio)

                # Definir o pixmap no QLabel
                label_imagem.setPixmap(pixmap)

                # Ajustar o alinhamento da imagem no QLabel
                label_imagem.setAlignment(Qt.AlignCenter)

                # Mostrar o QLabel
                label_imagem.show()
                self.imagem_carregada_produto = True

                # Salvar a imagem carregada para o atributo nova_imagem
                self.nova_imagem = fileName
            else:
                QMessageBox.warning(self, "Aviso", "Não foi possível carregar a imagem.")
        else:
            QMessageBox.warning(self, "Aviso", "Nenhuma imagem foi selecionada.")
#*********************************************************************************************************************
    def limpar_imagem_produto(self):
        for widget in self.frame_imagem_produto_3.children():
            if isinstance(widget, QLabel):
                widget.clear()
                widget.setPixmap(QPixmap())
                widget.hide()  # Esconder o QLabel para garantir que não fique visível
        self.imagem_carregada_produto = False
#*********************************************************************************************************************
    def carregar_nova_imagem_produto(self, nova_imagem):
        # Este método simula o carregamento de uma nova imagem no QLabel dentro do frame_imagem_produto
        for widget in self.frame_imagem_produto_3.children():
            if isinstance(widget, QLabel):
                widget.setPixmap(QPixmap(nova_imagem))
                widget.show()  # Mostrar o QLabel novamente após carregar a nova imagem
                self.imagem_carregada_produto = True
                return
#*********************************************************************************************************************
    def limpar_imagem_produto_após_atualizar(self):
        frame = self.frame_imagem_produto_3
        if frame is not None:
            for widget in frame.children():
                if isinstance(widget, QLabel):
                    widget.deleteLater()

            # Adiciona um QLabel vazio de volta ao frame
            novo_label = QLabel(frame)
            novo_label.setPixmap(QPixmap())
            layout = frame.layout()
            if layout is None:
                layout = QVBoxLayout(frame)
                frame.setLayout(layout)
            layout.addWidget(novo_label)
            self.label_imagem_produto = novo_label  # Atualiza a referência ao novo QLabel
#*********************************************************************************************************************
    def atualizar_produto(self):
        if not self.is_editing_produto or not self.produto_id:
            QMessageBox.warning(None, "Erro", "Nenhum produto selecionado para atualizar")
            return

        if not hasattr(self, 'produto_id') or not self.produto_id:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setText("Não há produto selecionado para seguir.")
            msgBox.setWindowTitle("Aviso")
            detalhes_button = msgBox.addButton("Detalhes", QMessageBox.ActionRole)
            msgBox.addButton(QMessageBox.Ok)
            clicked_button = msgBox.exec()

            if clicked_button == QMessageBox.Ok:
                return
            elif msgBox.clickedButton() == detalhes_button:
                detalhesMsgBox = QMessageBox()
                detalhesMsgBox.setIcon(QMessageBox.Information)
                detalhesMsgBox.setText("Para usar essa opção deverá ser necessário editar um produto")
                detalhesMsgBox.setWindowTitle("Detalhes")
                detalhesMsgBox.exec()
                return

        # Verificar se a imagem foi alterada
        imagem_alterada = False
        produto_imagem = None
        if hasattr(self, 'nova_imagem') and self.nova_imagem:
            pixmap = QPixmap(self.nova_imagem)
            if not pixmap.isNull():
                imagem_alterada = True
                byte_array = QByteArray()
                buffer = QBuffer(byte_array)
                buffer.open(QIODevice.WriteOnly)
                pixmap.save(buffer, "PNG")
                produto_imagem = byte_array.toBase64().data().decode()

        # Verificar se os campos foram alterados
        alteracao_campo = False
        if hasattr(self, 'produto_original'):
            alteracao_campo = self.verificar_alteracoes_produto(self.produto_original)

        # Se nada foi alterado, exibir mensagem e retornar
        if not alteracao_campo and not imagem_alterada:
            QMessageBox.information(None, "Aviso", "Nenhuma alteração foi feita no produto.")
            return

        # Obter os dados dos campos
        produto_nome = self.txt_produto.text()
        produto_quantidade = self.txt_quantidade.text()
        produto_valor_real = self.txt_valor_produto_3.text()
        produto_desconto = self.txt_desconto_3.text()
        produto_data_cadastro = self.dateEdit_3.date().toString("dd/MM/yyyy")
        produto_codigo_item = self.txt_codigo_item.text()
        produto_cliente = self.txt_cliente_3.text()
        produto_descricao = self.txt_descricao_produto_3.text()
        produto_id = self.produto_id

        # Conectar ao banco de dados
        db = DataBase()
        try:
            db.connecta()
            db.atualizar_produto(
                produto_id, produto_nome, produto_quantidade, produto_valor_real,
                produto_desconto, produto_data_cadastro,
                produto_codigo_item, produto_cliente, produto_descricao, produto_imagem
            )
            msgBox2 = QMessageBox(QMessageBox.Information, "Sucesso", "Produto atualizado com sucesso!")
            msgBox2.exec()
            self.limpar_imagem_produto_após_atualizar()
            self.limpar_campos_produtos()
            self.is_editing_produto = False
            self.selected_produto_id = None
            if hasattr(self, 'produto_original'):
                del self.produto_original
        except Exception as e:
            QMessageBox.critical(None, "Erro", f"Erro ao atualizar o produto: {str(e)}")

#*******************************************************************************************************
    def registrar_historico(self, acao, descricao):
        # Verifica se o histórico está pausado
        if self.historico_pausado:
            print("Histórico pausado. Registro não será feito.")
            return  # Se o histórico estiver pausado, não faz nada

        usuario = self.get_usuario_logado()  # Obtenha o usuário logado
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        with sqlite3.connect('banco_de_dados.db') as cn:
            cursor = cn.cursor()
            cursor.execute("""
                INSERT INTO historico ('Data e Hora', Usuário, Ação, Descrição)
                VALUES (?, ?, ?, ?)
            """, (data_hora, usuario, acao, descricao))
            cn.commit()
#*******************************************************************************************************
    def registrar_historico_usuarios(self,acao,descricao):
        #Verifica se o histórico está pausado
        if self.historico_usuario_pausado:
            print("Histórico pausado. Registro não será feito")
            return # Se o histórico estiver pausado, não faz 
        usuario = self.get_usuario_logado()
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        with sqlite3.connect('banco_de_dados.db') as cn:
            cursor = cn.cursor()
            cursor.execute("""
                INSERT INTO historico_usuarios('Data e Hora', Usuário, Ação, Descrição)
                VALUES (?,?,?,?)
        """,(data_hora,usuario,acao,descricao))
        cn.commit()
#*******************************************************************************************************        
    def registrar_historico_clientes_juridicos(self,acao,descricao):
        # Verifica se o histórico está pausado
        if self.historico_pausado_clientes_juridicos:
            print("Histórico pausado. Registro não será feito")
            return # Se o histórico estiver pausado, não faz nada
        usuario = self.get_usuario_logado()  # Obtenha o usuário logado
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")
        
        with sqlite3.connect('banco_de_dados.db') as cn:
            cursor = cn.cursor()
            cursor.execute("""
                INSERT INTO historico_clientes_juridicos ('Data e Hora', Usuário, Ação, Descrição)
                VALUES (?,?,?,?)
            """,(data_hora,usuario,acao,descricao))
            cn.commit()

    def registrar_historico_clientes_fisicos(self,acao,descricao):
        # Verifica se o histórico está pausado
        if self.historico_pausado_clientes_fisicos:
            print("Histórico pausado. O registro não será feito")
            return # Se o histórico estiver pausado, não faz nada
        usuario = self.get_usuario_logado()
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")

        with sqlite3.connect("banco_de_dados.db") as cn:
            cursor = cn.cursor()
            cursor.execute("""
                INSERT INTO historico_clientes_fisicos ('Data e Hora',Usuário,Ação,Descrição)
                VALUES (?,?,?,?)
            """,(data_hora,usuario,acao,descricao))
            cn.commit()

#*******************************************************************************************************
    def campos_obrigatorios_preenchidos(self):
        # Verificar se todos os campos obrigatórios estão preenchidos
        campos = [
            self.txt_produto.text(),
            self.txt_quantidade.text(),
            self.txt_valor_produto_3.text(),
            self.dateEdit_3.text(),
            self.txt_codigo_item.text(),
            self.txt_cliente_3.text(),
            self.txt_descricao_produto_3.text()
        ]
        for campo in campos:
            if not campo:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Erro")
                msg.setText("Todos os campos precisam ser preenchidos.")
                msg.exec()
                return False
        return True
#*********************************************************************************************************************
    def mostrar_mensagem_sucesso(self):
        success_msg = QMessageBox()
        success_msg.setIcon(QMessageBox.Information)
        success_msg.setWindowTitle("Sucesso")
        success_msg.setText("Produtos confirmados e cadastrados com sucesso.")
        success_msg.setStyleSheet("color: black;")
        success_msg.exec()
#*********************************************************************************************************************
    def formatar_cep(self, text, widget):
        numero_limpo = ''.join(filter(str.isdigit, text))[:8]
        if len(numero_limpo) >= 5:
            cep_formatado = f"{numero_limpo[:5]}-{numero_limpo[5:]}"
        else:
            cep_formatado = numero_limpo

        widget.blockSignals(True)
        widget.setText(cep_formatado)
        widget.blockSignals(False)
#*********************************************************************************************************************
    def formatar_cpf(self, text, widget):
        if text == "Não Cadastrado":
            widget.setText(text)
            return

        numero_cpf = ''.join(filter(str.isdigit, text))[:11]  # Limita a 11 dígitos

        if len(numero_cpf) >= 9:
            cpf_formatado = "{}.{}.{}-{}".format(
                numero_cpf[:3], numero_cpf[3:6], numero_cpf[6:9], numero_cpf[9:]
            )
        else:
            cpf_formatado = numero_cpf

        widget.blockSignals(True)
        widget.setText(cpf_formatado)
        widget.blockSignals(False)
#*********************************************************************************************************************
    def formatar_cnpj(self, text, widget):
        if text == "Não Cadastrado":
            widget.setText(text)
            return

        # Remover caracteres não numéricos
        numero_cnpj = ''.join(filter(str.isdigit, text))

        # Verifica se há pelo menos 14 dígitos
        if len(numero_cnpj) >= 14:
            numero_cnpj = numero_cnpj[:14]  # Limita a 14 dígitos

            # Formata para o padrão nacional: 11.111.111/1111-11
            cnpj_formatado = "{}.{}.{}/{}-{}".format(
                numero_cnpj[:2],
                numero_cnpj[2:5],
                numero_cnpj[5:8],
                numero_cnpj[8:12],
                numero_cnpj[12:]
            )

            # Atualiza o texto do widget com formatação
            widget.blockSignals(True)
            widget.setText(cnpj_formatado)
            widget.blockSignals(False)
        else:
            widget.blockSignals(True)
            widget.setText(numero_cnpj)
            widget.blockSignals(False)
#*********************************************************************************************************************
    def formatar_rg(self, text,widget):
        if text == "Não Cadastrado":
            widget.setText(text)
            return
    
        # Remover caracteres não numéricos
        numero_rg = ''.join(filter(str.isdigit, text))
        
        # Verificar se o RG tem pelo menos 9 dígitos
        if len(numero_rg) >= 9:
            # Formatar o RG com pontos e hífen
            rg_formatado = "{}.{}.{}-{}".format(numero_rg[:2], numero_rg[2:5], numero_rg[5:8], numero_rg[8:9])

            # Atualiza o texto do widget com formatação
            widget.blockSignals(True)
            widget.setText(rg_formatado)
            widget.blockSignals(False)
        else:
            # Atualiza o texto do widget com formatação
            widget.blockSignals(True)
            widget.setText(numero_rg)
            widget.blockSignals(False)

    def formatar_cnh(self, text, widget):
        if text == "Não Cadastrado":
            widget.setText(text)
            return
        
        # Remove tudo que não for dígito
        apenas_numeros = ''.join(filter(str.isdigit, text))
        
        # Limita a 11 dígitos
        cnh_formatada = apenas_numeros[:11]
        
        # Atualiza o campo
        widget.setText(cnh_formatada)

#*********************************************************************************************************************
    def formatar_data_nascimento(self, text,widget):
        if text == "Não Cadastrado":
            widget.setText(text)
            return
        
        # Remover todos os caracteres que não são dígitos
        numeros = ''.join(filter(str.isdigit, text))

        # Definir um valor padrão para data_formatada
        data_formatada = ""

        # Verificar se existem dígitos suficientes para formar uma data
        if len(numeros) >= 1:
            # Pegar os dois primeiros dígitos e adicionar a '/'
            data_formatada = numeros[:2] + "/"
            # Verificar se há pelo menos 3 dígitos para o mês
            if len(numeros) >= 3:
                # Adicionar os próximos dois dígitos ao mês
                data_formatada += numeros[2:4] + "/"
                # Verificar se há pelo menos 5 dígitos para o ano
                if len(numeros) >= 5:
                    # Adicionar os próximos quatro dígitos ao ano
                    data_formatada += numeros[4:8]

        # Atualiza o texto do widget com formatação
            widget.blockSignals(True)
            widget.setText(data_formatada)
            widget.blockSignals(False)
        else:
            # Atualiza o texto do widget com formatação
            widget.blockSignals(True)
            widget.setText(numeros)
            widget.blockSignals(False)
#*********************************************************************************************************************
    def formatar_telefone(self, text, widget):
        numero_limpo = ''.join(filter(str.isdigit, text))[:14]

        if len(numero_limpo) >= 2:
            numero_formatado = f"({numero_limpo[:2]}) "

            if len(numero_limpo) >= 8:
                numero_formatado += f"{numero_limpo[2:7]}-{numero_limpo[7:11]}"
            else:
                numero_formatado += numero_limpo[2:]

            widget.blockSignals(True)
            widget.setText(numero_formatado)
            widget.blockSignals(False)

#*******************************************************************************************************
    def conectar_botao_adicionar_produto(self):
        self.btn_adicionar_produto.clicked.connect(self.adicionar_produto)
#*********************************************************************************************************************
    def selecionar_imagem_usuario(self, row):
    # Obter o ID do usuário selecionado
        id_usuario = self.tabela_usuario_dialogo.item(row, 0).text()
        self.produto_id = id_usuario
        
        # Atualizar os campos e a imagem com base no produto selecionado
        self.atualizar_imagem()
#*******************************************************************************************************
    def mostrar_erro_desconto(self):
        detalhes_msg_detalhes = QMessageBox()
        detalhes_msg_detalhes.setIcon(QMessageBox.Information)
        detalhes_msg_detalhes.setWindowTitle("Detalhes do Erro")
        detalhes_msg_detalhes.setText("Os campos obrigatórios precisam estar preenchidos.")
        detalhes_msg_detalhes.exec()
#*******************************************************************************************************
    def limpar_campos_produtos(self):
        self.txt_produto.clear()
        self.txt_quantidade.clear()
        self.txt_valor_produto_3.clear()
        self.txt_desconto_3.clear()
        self.dateEdit_3.clear()
        self.txt_codigo_item.clear()
        self.txt_cliente_3.clear()
        self.txt_descricao_produto_3.clear()
        
        # Resetar os QLabel dos frames para valores padrão
        self.label_valor_total_produtos.setText("R$ 0,00")
        self.label_valor_desconto.setText("R$ 0,00")
        self.label_quantidade.setText("0")  # Quantidade é um número simples
        self.label_valor_do_desconto.setText("R$ 0,00")

        
        # Limpar o campo dateEdit e configurar para a data atual
        self.dateEdit_3.setDate(QDate.currentDate())
#*******************************************************************************************************
    def apagar_campos_produtos(self):
        # Verificar se algum campo já está preenchido
        if any([
            self.txt_produto.text(),
            self.txt_quantidade.text(),
            self.txt_valor_produto_3.text(),
            self.txt_desconto_3.text(),
            self.txt_codigo_item.text(),
            self.txt_cliente_3.text(),
            self.txt_descricao_produto_3.text()
        ]):
            # Limpar todos os campos das QLineEdit
            self.limpar_campos_produtos()

            # Limpar a imagem
            self.apagar_imagem_produto_btn_apagar_campos()

            # Mensagem de sucesso
            successMsgBox = QMessageBox()
            successMsgBox.setIcon(QMessageBox.Information)
            successMsgBox.setText("Campos limpos com sucesso!")
            successMsgBox.setWindowTitle("Sucesso")
            successMsgBox.exec()
        else:
            # Mostrar mensagem de aviso se nenhum campo estiver preenchido
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("Não há campos preenchidos para limpar.")
            msgBox.setWindowTitle("Aviso")
            msgBox.exec()
#*******************************************************************************************************
    def apagar_imagem_produto_btn_apagar_campos(self):
        # Verificar se o QFrame contém um QLabel para imagem
        if self.frame_imagem_produto_3 is not None:
            for widget in self.frame_imagem_produto_3.children():
                if isinstance(widget, QLabel):
                    widget.clear()  # Limpar o QLabel
                    widget.setPixmap(QPixmap())  # Definir um pixmap vazio ou padrão
#*******************************************************************************************************
    def email_valido(self, email):
        email = email.strip()
        email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        return bool(email_pattern.match(email))
# **********************************************************************************************************************
    def configurar_geometria_frames(self):
        altura = 101
        largura = 335
        self.frame_valor_total_produtos.setGeometry(335, 101, largura, altura)
#**********************************************************************************************************************
     # Método para limpar o frame após o cadastro do usuário
    def limpar_frame_cadastro_usuario(self): 
        # Remover imagem do QLabel
        self.frame_imagem_cadastro.clear()
#*******************************************************************************************************
    def atualizar_imagem(self):
        if hasattr(self, 'produto_imagem') and self.produto_imagem:
            caminho_imagem = self.produto_imagem
            if caminho_imagem:
                # Carregar a imagem e exibi-la em um QLabel
                pixmap = QPixmap(caminho_imagem)
                if not pixmap.isNull():
                    # Redimensionar a imagem para se ajustar ao QLabel (se necessário)
                    pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio)
                    self.label_imagem_produto.setPixmap(pixmap)
                else:
                    QMessageBox.warning(self, "Aviso", "Não foi possível carregar a imagem.")
            else:
                QMessageBox.warning(self, "Aviso", "Não foi possível encontrar o caminho da imagem.")
        else:
            QMessageBox.warning(self, "Aviso", "Nenhuma imagem definida para o produto.")
#**************************************************************************************************************            
    def limpar_campos_após_atualizar_usuario(self):
        self.txt_nome.clear()
        self.txt_usuario.clear()
        self.txt_telefone.clear()
        self.txt_endereco.clear()
        self.txt_numero.clear()
        self.txt_cidade.clear()
        self.txt_bairro.clear()
        self.txt_complemento.clear()
        self.txt_email.clear()
        self.txt_data_nascimento.clear()
        self.txt_rg.clear()
        self.txt_cep.clear()
        self.txt_cpf.clear()
        self.txt_cnpj.clear()
        self.txt_senha.clear()
        self.txt_confirmar_senha.clear()
        self.perfil_estado.setCurrentIndex(0)
        self.perfil_usuarios.setCurrentIndex(0)
        self.label_imagem_usuario.clear()


    def reiniciar_sistema(self):
        python = sys.executable
        script = os.path.abspath(sys.argv[0])
        # Fecha o app atual
        QApplication.quit()
        # Reinicia com subprocess (mais robusto para caminhos com espaço)
        subprocess.Popen([python, script] + sys.argv[1:])
        sys.exit()

    def auto_completar(self, nome_campo, campo):
        texto = campo.text().strip()
        if texto:
            self.config.adicionar_ao_historico(nome_campo, texto)

            # Atualiza o modelo do QCompleter para refletir o novo histórico
            historico = self.config.carregar_historico_autocompletar(nome_campo)
            novo_completer = QCompleter(historico)
            novo_completer.setCaseSensitivity(Qt.CaseInsensitive)
            campo.setCompleter(novo_completer)

    # Método para tratar o duplo clique e preencher o campo
    def completar_por_duplo_clique(self, event, nome_campo, campo):
        if event.type() == QEvent.MouseButtonDblClick:
            # Recupera o completador e o modelo de dados
            completer = campo.completer()
            model = completer.model()

            # Pegando o primeiro item de sugestão do modelo
            if model.rowCount() > 0:
                index = model.index(0, 0)  # Pega o primeiro item
                texto_completo = model.data(index)  # Pega o texto do item
                campo.setText(texto_completo)  # Preenche o campo com a sugestão

                # Atualiza o histórico de autocompletar
                self.config.adicionar_ao_historico(nome_campo, texto_completo)
                return True
        return False


    def exibir_planilhas_exemplo(self):
        opcoes = ["Planilha de Exemplo 1", "Planilha de Exemplo 2"]
        escolha, ok = QInputDialog.getItem(
            None,
            "Escolher Planilha de Exemplo", 
            "Selecione uma planilha de exemplo:",
            opcoes,
            0,  # Índice padrão
            False,  # Não permitir edição
        )
        if not ok or not escolha:
            print("Operação cancelada pelo usuário.")
            return

        # Agora, a escolha é diretamente mapeada
        if escolha == "Planilha de Exemplo 1":
            nome_sugestao = "Produtos Exemplo.xlsx"
            sheet_name = 'Produtos'
            dados = {
                "Produto": ["Exemplo 1", "Exemplo 2", "Exemplo 3", "Exemplo 4"],
                "Quantidade": [10, 50, 5, 20],
                "Valor do Produto": [4500.00, 150.00, 1200.00, 900.00],
                "Desconto": [5, "Sem desconto", 10, "Sem desconto"],
                "Valor Total": ["R$ 1,000.00","R$ 1,500,00","R$ 300,00","R$ 150,00"],
                "Data do Cadastro": ["10/05/2024", "10/04/2024", "10/03/2024", "10/02/2024"],
                "Código do Item": ["AUTO12345", "AUTO67890", "AUTO11223", "AUTO33445"],
                "Cliente": ["João da Silva", "Maria Oliveira", "Pedro Santos", "Carla Lima"],
                "Descrição": [
                    "Notebook com 16GB RAM, SSD",
                    "Mouse sem fio, modelo M170",
                    "Impressora multifuncional",
                    "Monitor 24”, Full HD"
                ]
            }
        else:
            nome_sugestao = "Usuários Exemplos.xlsx"
            sheet_name = 'Usuários'
            dados = {
                "Nome": ["Keven Lucas da Silva Jesus", "Maria Oliveira da Silva", "Pedro Santos Reis", "Carla Lima Medeiros"],
                "Usuário": ["Gerado automaticamente", "Gerado automaticamente", "Gerado automaticamente", "Gerado automaticamente"],
                "Senha": ["senha123", "senha456", "senha789", "senha101"],
                "Confirmar Senha": ["senha123", "senha456", "senha789", "senha101"],
                "CEP": ["00000-0001", "00000-0002", "00000-0003", "00000-0004"],
                "Endereço": ["Rua A, 123", "Rua B, 456", "Rua C, 789", "Rua D, 101"],
                "Número": [123, 456, 789, 101],
                "Cidade": ["Vila Madalena", "Sumaré", "Campinas", "Monte Mor"],
                "Bairro": ["Centro", "Zona Sul", "Zona Norte", "Zona Leste"],
                "Estado": ["SP", "RJ", "MG", "PR"],
                "Complemento": ["Apto 1", "Opcional", "Opcional", "465"],
                "Telefone": ["(11) 00000-0001", "(21) 00000-0002", "(31) 00000-0003", "(41) 00000-0004"],
                "E-mail": ["keven.lucas00@dhdfge.com", "mariolieira1000@gmail.com","pedrosantos00123@gmail.com","carlalima14520@gmail.com"],
                "Data de Nascimento": ["01/01/2000", "02/02/1995", "03/03/1990", "04/04/1985"],
                "RG": ["00.000.000-1", "00.000.000-2", "00.000.000-3", "00.000.000-4"],
                "CPF": ["000.000.000-01", "000.000.000-02", "000.000.000-03", "000.000.000-04"],
                "CNPJ": ["00.000.000/0001-01", "00.000.000/0001-02", "00.000.000/0001-03", "00.000.000/0001-04"],   
                "Acesso": ["Convidado", "Usuário", "Usuário", "Convidado"]
            }
        # Gerar a planilha com os dados corretos
        df = pd.DataFrame(dados)

        file_path, _ = QFileDialog.getSaveFileName(
            None,
            "Salvar Planilha de Exemplo",
            nome_sugestao,
            "Excel Files (*.xlsx)"
        )

        if not file_path:
            print("Operação cancelada pelo usuário.")
            return

        # Salvar usando openpyxl para aplicar estilos
        df.to_excel(file_path, index=False, engine='openpyxl', sheet_name=sheet_name)

        # Abrir a planilha para formatação
        wb = load_workbook(file_path)
        ws = wb[sheet_name]  # Usar o nome da aba dinamicamente

        # Formatar as colunas
        for col in ws.columns:
            max_length = 0
            col_letter = get_column_letter(col[0].column)
            for cell in col:
                # Centralizar
                cell.alignment = Alignment(horizontal='center', vertical='center')
                try:
                    if cell.value:
                        max_length = max(max_length, len(str(cell.value)))
                except:
                    pass
                # Ajustar largura da coluna
                ws.column_dimensions[col_letter].width = max_length + 2

        # Salvar as alterações
        wb.save(file_path)

        # Mostrar a mensagem de sucesso
        QMessageBox.information(
            None,
            "Sucesso",
            f"Planilha '{escolha}' salva com sucesso em {file_path}!",
            QMessageBox.Ok
        )
     
    def pagina_cadastro_em_massa_produtos(self):
        selected_action = self.sender()
        if selected_action == self.action_em_massa_produtos:
            self.paginas_sistemas.setCurrentWidget(self.page_cadastrar_massa_produtos)
        
    def pagina_cadastro_em_massa_usuarios(self):
        selected_action = self.sender()
        if selected_action == self.action_em_massa_usuarios:
            self.paginas_sistemas.setCurrentWidget(self.page_cadastrar_massa_usuarios)

    # Sair do modo edição na página de cadastrar usuários
    def sair_modo_edicao_usuarios(self):
        if not self.is_editing:
            QMessageBox.warning(None, "Aviso", "Você não está no modo de edição.")
            return

        self.is_editing = False
        self.selected_user = None
         # Limpa todos os campos (pode reaproveitar o trecho do subscribe_user)
        self.txt_nome.clear()
        self.txt_usuario.clear()
        self.txt_senha.clear()
        self.txt_confirmar_senha.clear()
        self.txt_cpf.clear()
        self.txt_cnpj.clear()
        self.txt_email.clear()
        self.txt_numero.clear()
        self.txt_endereco.clear()
        self.txt_bairro.clear()
        self.txt_cidade.clear()
        self.txt_cep.clear()
        self.txt_complemento.clear()
        self.txt_rg.clear()
        self.txt_telefone.clear()
        self.txt_data_nascimento.clear()
        self.perfil_estado.setCurrentIndex(0)
        self.perfil_usuarios.setCurrentIndex(0)
        self.label_imagem_usuario.clear()

        # Se quiser mostrar visualmente que saiu do modo edição (opcional)
        QMessageBox.information(None, "Edição cancelada", "Você saiu do modo de edição.")

    def sair_modo_edicao_produto(self):
        if not self.is_editing_produto:
            QMessageBox.warning(None, "Aviso", "Você não está no modo de edição de produtos.")
            return

        self.is_editing_produto = False
        self.selected_produto_id = None

        # Se quiser mostrar visualmente que saiu do modo edição (opcional)
        QMessageBox.information(None, "Edição cancelada", "Você saiu do modo de edição.")
    
    def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS  # PyInstaller cria essa pasta temporária
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
    
    
    def formatar_tamanho(self,bytes_tamanho):
        for unidade in ['B', 'KB', 'MB', 'GB']:
            if bytes_tamanho < 1024:
                return f"{bytes_tamanho:.2f} {unidade}"
            bytes_tamanho /= 1024
        return f"{bytes_tamanho:.2f} TB"

    
    def limpar_cache_sistema(self):
        pasta_cache = "imagens_temporarias"

        if not os.path.exists(pasta_cache):
            QMessageBox.information(self, "Limpeza de Cache", "Nenhum cache encontrado para limpar.")
            return

        # Calcular tamanho total antes de apagar
        tamanho_total = 0
        # Remover arquivos individualmente
        for root, dirs, files in os.walk(pasta_cache):
            for file in files:
                caminho = os.path.join(root, file)
                try:
                    os.remove(caminho)
                except PermissionError:
                    print(f"Arquivo em uso ou protegido: {caminho}")
                except Exception as e:
                    print(f"Erro ao remover {caminho}: {e}")

        tamanho_formatado = self.formatar_tamanho(tamanho_total)

        # Criar progress dialog
        progresso = QProgressDialog("Limpando cache do sistema...", "Cancelar", 0, 0, self)
        progresso.setWindowTitle("Limpeza de Cache")
        progresso.setWindowModality(Qt.ApplicationModal)
        progresso.show()
        QApplication.processEvents()  # Atualiza a interface imediatamente

        try:
            shutil.rmtree(pasta_cache)  # Remove a pasta inteira
            os.makedirs(pasta_cache)    # Recria a pasta limpa
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao limpar cache: {str(e)}")
            progresso.close()
            return

        progresso.close()

        QMessageBox.information(
            self,
            "Limpeza concluída",
            f"Cache do sistema limpo com sucesso.\nEspaço liberado: {tamanho_formatado}\n\nReinicie o sistema para garantir que tudo funcione corretamente."
        )

    def mostrar_menu_limpeza(self):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Limpar Cache")
        msg_box.setText("Selecione o que deseja limpar:")
        msg_box.setIcon(QMessageBox.Question)

        btn_limpar_cache = msg_box.addButton("Cache (imagens temporárias)", QMessageBox.ActionRole)
        btn_resetar_config = msg_box.addButton("Resetar configurações (config.json)", QMessageBox.ActionRole)
        btn_cancelar = msg_box.addButton("Cancelar", QMessageBox.RejectRole)

        msg_box.exec()

        if msg_box.clickedButton() == btn_limpar_cache:
            self.limpar_cache_sistema()
        elif msg_box.clickedButton() == btn_resetar_config:
            self.resetar_configuracoes()

    def resetar_configuracoes(self):    
        config_padrao = {
            "tema": "claro",
            "tamanho_janela": [800, 600],
            "idioma": "pt-BR"
            # ... outros padrões
        }

        try:
            with open("config.json", "w", encoding="utf-8") as f:
                json.dump(config_padrao, f, indent=4, ensure_ascii=False)
            QMessageBox.information(self, "Configurações", "As configurações foram redefinidas com sucesso.")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao resetar configurações: {str(e)}")

    def tratar_f5_global(self):
        pagina_atual = self.paginas_sistemas.currentWidget()
        print(f"[DEBUG] Página atual: {type(pagina_atual)}")

        if pagina_atual == self.pg_clientes:
            if self.pagina_clientes_juridicos.table_clientes_juridicos.isVisible():
                QMessageBox.information(None,"Aviso","Dados atualizados com sucesso!")
                self.pagina_clientes_juridicos.carregar_clientes_juridicos()
            elif self.pagina_clientes_fisicos.table_clientes_fisicos.isVisible():
                QMessageBox.information(None,"Aviso","Dados atualizados com sucesso!")
                self.pagina_clientes_fisicos.carregar_clientes_fisicos()
            else:
                print("⚠️ Nenhuma tabela de cliente visível")
        else:
            print("⚠️ Página atual não tem método de atualização com F5.")


# Função principal
if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = Login(login_window=None)
    main_window = MainWindow (user=None, tipo_usuario=None, login_window=login_window)
    
    # Usa estilo nativo do Windows explicitamente
    app.setStyle("WindowsVista")
    app.setWindowIcon(QIcon("imagens/ícone_sistema_provisório.png"))
    
    
    login_window.show()
    sys.exit(app.exec())