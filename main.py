#*********************************************************************************************************************
import re
from PySide6.QtCore import (Qt, QTimer, QDate, QBuffer, QByteArray, QIODevice, Signal,
                            QEvent,QPropertyAnimation,QEasingCurve,QSize,QPoint)
from PySide6 import QtCore
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QPushButton,
                               QLabel, QFileDialog, QVBoxLayout, QTableWidget,
                               QMenu,QTableWidgetItem,QDialog)
from PySide6.QtGui import (QDoubleValidator, QIcon, QColor, QPixmap,QBrush,
                           QAction,QMovie)
from PySide6 import QtWidgets
from login import Login
from mane_python import Ui_MainWindow
from database import DataBase
from config_senha import TrocarSenha
import sys
import locale
from atualizarprodutos import AtualizarProduto
from tabelaprodutos import TabelaProdutos
from configuracoes import Configuracoes_Login
from tabelausuario import TabelaUsuario
from atualizarusuario import AtualizarUsuario
from pg_configuracoes import Pagina_Configuracoes
from estoqueprodutos import EstoqueProduto
from historicousuario import Pagina_Usuarios
from clientes import Clientes
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




class MainWindow(QMainWindow, Ui_MainWindow):
    fechar_janela_login_signal = Signal(str)
    def __init__(self, user=None, login_window=None, tipo_usuario=None, connection=None):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de Gerenciamento")
        self.historico_pausado = False

        # Inicialize o banco de dados antes de qualquer operação que dependa dele
        self.db = DataBase('banco_de_dados.db')
        self.connection = sqlite3.connect('banco_de_dados.db')
        self.login_window = login_window
        self.connection = connection
        #Cria as tabelas no banco de dados sempre que executar o sistema em um novo ambiente
        self.db.create_table_products()
        self.db.create_table_products_saida()
        self.db.create_table_users()
        self.db.create_table_historico()

        

        # funções que precisam do banco de dados
        self.erros_frames()
        

        # Carregar informações ao iniciar
        self.carregar_informacoes_tabela()

        # Exibir notificação de status de conexão
        #self.exibir_notificacao(self)

        # Inicializar as configurações antes de chamar fazer_login_automatico
        self.config = Configuracoes_Login(self)
        

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

        self.pagina_clientes = Clientes(self.line_clientes)

        # Crie o layout para o frame_imagem_cadastro e adicione o QLabel
        self.label_imagem_cadastro = QLabel(self)
        layout_usuario = QVBoxLayout()  # Definindo layout_usuario aqui
        layout_usuario.addWidget(self.label_imagem_cadastro)
        self.frame_imagem_cadastro.setLayout(layout_usuario)

        self.label_exibir_usuario = QLabel(self)
        layout_exibir_usuario = QVBoxLayout()
        layout_exibir_usuario.addWidget(self.label_exibir_usuario)
        self.label_exibir_usuario.setGeometry(1265,5,600,30)

        # Atualizar o nome do usuário logado
        self.atualizar_usuario_logado(self.config.obter_usuario_logado())
        
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
        # Criar o botão btn_opcoes
        self.btn_opcoes = QPushButton("Mais opções", self)

        # Criar o menu dentro do botão btn_opcoes
        self.menu_opcoes = QMenu(self.btn_opcoes)

        # Definir o estilo do menu
        estilo_botao_menu = """
            QMenu {
                background-color: white;
                color: black;
            }   
        """
        self.menu_opcoes.setStyleSheet(estilo_botao_menu)

        # Criar as ações do menu
        self.action_sair = QAction("Sair do Sistema", self)
        self.action_configuracoes = QAction("Configurações", self)
        self.action_modo_escuro = QAction("Alterar Tema", self)
        self.action_contato = QAction("Contato", self)
        self.action_cadastro_produto_massa = QAction("Cadastrar Produtos em Massa",self)
        self.action_cadastro_usuario_massa = QAction("Cadastrar Usuários em Massa",self)
        self.action_reiniciar = QAction("Reiniciar Sistema")
        self.action_historico = QAction("Histórico")
        self.action_informacoes_sistema = QAction("Informações do sistema")

        # Adicionar as ações ao menu
        self.menu_opcoes.addAction(self.action_sair)
        self.menu_opcoes.addAction(self.action_configuracoes)
        self.menu_opcoes.addAction(self.action_modo_escuro)
        self.menu_opcoes.addAction(self.action_contato)
        self.menu_opcoes.addAction(self.action_cadastro_produto_massa)
        self.menu_opcoes.addAction(self.action_cadastro_usuario_massa)
        self.menu_opcoes.addAction(self.action_reiniciar)
        self.menu_opcoes.addAction(self.action_historico)
        self.menu_opcoes.addAction(self.action_informacoes_sistema)

        # Associar o menu ao botão
        self.btn_opcoes.setMenu(self.menu_opcoes)

        # Ajustar a geometria do botão
        self.btn_opcoes.setGeometry(1550, 5, 120, 30)

        # Conectar as ações do menu aos slots correspondentes
        self.action_sair.triggered.connect(self.desconectarUsuario)
        self.action_configuracoes.triggered.connect(self.combobox_caixa)
        self.action_contato.triggered.connect(self.show_pg_contato)
        self.action_cadastro_produto_massa.triggered.connect(self.show_pg_cadastro_produto_massa)
        self.action_cadastro_usuario_massa.triggered.connect(self.show_pg_cadastro_usuario_massa)
        self.action_reiniciar.triggered.connect(self.reiniciar_sistema)
        self.action_historico.triggered.connect(self.show_pg_historico)
        self.action_informacoes_sistema.triggered.connect(self.show_mensagem_sistema)
        
        estilo_botao_mais_opcoes = """
            QPushButton {
                color: rgb(255, 255, 255);
                border-radius: 3px;
                font-size: 16px;
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255));
                border: 3px solid transparent;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255));
                color: black;
            }
        """
        self.btn_opcoes.setStyleSheet(estilo_botao_mais_opcoes)
        
        self.fechar_janela_login_signal.connect(self.fechar_janela_login)  


        self.fazer_login_automatico()

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
                                               self.btn_gerar_pdf_usuarios,self.btn_historico_usuarios,self.btn_atualizar_ativos,
                                               self.btn_atualizar_inativos,self.btn_limpar_tabelas_usuarios,self.btn_incluir_usuarios_sistema,
                                               self.btn_salvar_tables_usuarios,self.btn_gerar_saida_usuarios)

        self.estoque_produtos = EstoqueProduto(self,self.btn_gerar_pdf,self.btn_gerar_estorno,
                                               self.btn_gerar_saida,self.btn_limpar_tabelas,self.btn_salvar_tables,
                                               self.btn_atualizar_saida,self.btn_atualizar_estoque,self.btn_historico,
                                               self.btn_incluir_no_sistema,self.btn_abrir_planilha,self.btn_incluir_no_sistema) 

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

        self.frame_valor_total_produtos = QLabel(self.frame_valor_total_produtos)
        self.frame_valor_desconto = QLabel(self.frame_valor_com_desconto1)
        self.frame_quantidade = QLabel(self.frame_quantidade)
        self.frame_valor_do_desconto = QLabel(self.frame_valor_do_desconto)
        
        

        self.frame_valor_total_produtos.setStyleSheet("font-size: 20px; color: white; font-family: 'Arial'; font-weight: bold;")
        self.frame_valor_desconto.setStyleSheet("font-size: 20px; color: white; font-family: 'Arial'; font-weight: bold;")
        self.frame_quantidade.setStyleSheet("font-size: 20px; color: white; font-family: 'Arial'; font-weight: bold;")
        self.frame_valor_do_desconto.setStyleSheet("font-size: 20px; color: white; font-family: 'Arial'; font-weight: bold;")

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
        self.btn_ver_item.clicked.connect(lambda: self.paginas_sistemas.setCurrentWidget(self.page_estoque))
        self.btn_novo_produto.clicked.connect(lambda: self.paginas_sistemas.setCurrentWidget(self.pg_cadastrar_produto))
        self.btn_verificar_usuarios.clicked.connect(lambda: self.paginas_sistemas.setCurrentWidget(self.page_verificar_usuarios))
        


        self.btn_remover_imagem.clicked.connect(self.retirar_imagem_produto)
        self.btn_limpar_campos.clicked.connect(self.apagar_campos)
        self.btn_adicionar_produto.clicked.connect(self.adicionar_produto)
        self.btn_confirmar.clicked.connect(self.confirmar_produtos)
        self.btn_atualizar_cadastro.clicked.connect(self.atualizar_usuario_no_bd)
        self.btn_verificar_estoque.clicked.connect(self.mostrar_page_estoque)
        
        self.btn_fazer_cadastro.clicked.connect(self.subscribe_user)
        self.btn_editar.clicked.connect(self.exibir_tabela_produtos)
        self.btn_atualizar_produto.clicked.connect(self.atualizar_produto)
        self.btn_carregar_imagem.clicked.connect(self.carregar_imagem_produto)
        self.btn_opcoes_navegacao.clicked.connect(self.abrir_menu_opcoes)

        
        
        self.pagina_configuracoes = Pagina_Configuracoes(self.tool_tema,self.tool_atalhos,
                                                         self.tool_atualizacoes,self.tool_hora,self.tool_fonte,
                                                         self.frame_botoes_configuracoes,self.frame_pg_configuracoes,self,self,
                                                         self.frame_botoes_navegacoes,self.label_configuracoes,self.centralwidget,
                                                         self.frame_pag_estoque,self.frame_2,self.paginas_sistemas,
                                                         self.pg_cadastrar_usuario,self.frame_pag_cadastrar_usuario,
                                                         self.btn_opcoes,self.btn_avancar,self.btn_retroceder,self.btn_home,self.btn_verificar_estoque,
                                                         self.btn_cadastrar_produto, self.btn_cadastrar_usuarios, self.btn_clientes,self.btn_configuracoes,
                                                         self.btn_abrir_planilha,self.btn_importar,self.btn_gerar_saida,
                                                         self.line_excel,self.btn_gerar_estorno,
                                                         self.label_cadastramento,self.label_cadastramento_produtos,self.frame_valor_total_produtos,self.frame_valor_do_desconto,
                                                         self.frame_valor_desconto,self.frame_quantidade)
             
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



    '''def boas_vindas(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Boas Vindas")
        msg.setText(f"{self.config.obter_usuario_logado()}, seja bem-vindo(a) ao sistema de gerenciamento.\n"
                    "É um prazer tê-lo(a) conosco em nosso sistema.\n"
                    "Esperamos que as informações aqui contidas sejam de grande ajuda.\n"
                    "Pedimos que sempre que possível, você possa avaliar e sugerir melhorias.")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()'''
    

    def atualizar_usuario_logado(self, user):
        if user:
            usuario_logado = f"Usuário logado: {user}"
        else:
            usuario_logado = "Nenhum usuário logado"

        self.label_exibir_usuario.setText(usuario_logado)
        self.label_exibir_usuario.setStyleSheet("font-size: 15px; font-weight: bold; color: white;")
        print(usuario_logado)


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
    

    def carregar_informacoes_tabela(self):
        # Limpa as tabelas antes de carregar novas informações
        self.table_base.setRowCount(0)
        self.table_saida.setRowCount(0)

        # Carregar dados da `table_base`
        produtos_base = self.db.obter_produtos_base()
        for produto in produtos_base:
            row_position = self.table_base.rowCount()
            self.table_base.insertRow(row_position)
            for col, data in enumerate(produto):
                self.table_base.setItem(row_position, col, self.criar_item(str(data)))

        # Carregar dados da `table_saida`
        produtos_saida = self.db.obter_produtos_saida()
        for produto in produtos_saida:
            row_position = self.table_saida.rowCount()
            self.table_saida.insertRow(row_position)
            for col, data in enumerate(produto):
                self.table_saida.setItem(row_position, col, self.criar_item(str(data)))
     
    
    def reiniciar_sistema(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("ERRO")
        msg.setText("Essa função ainda não está disponível!")
        msg.exec()

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

    def show_pg_cadastro_produto_massa(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("ERRO")
        msg.setText("Essa função ainda não está disponível!")
        msg.exec()

    def show_pg_cadastro_usuario_massa(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("ERRO")
        msg.setText("Essa função ainda não está disponível!")
        msg.exec()

    def show_pg_historico(self):
        selected_action = self.sender()  # A ação que acionou o slot
        if selected_action == self.action_historico:
            # Navegar para a página de estoque
            self.paginas_sistemas.setCurrentWidget(self.pag_estoque)

            # Salvar o estilo original do botão
            original_style = self.btn_historico.styleSheet()
            destaque_style = """
                QPushButton {
                    border: 3px solid red; /* Borda vermelha */
                }
            """

            # Alternar entre os estilos
            def alternar_estilo():
                current_style = self.btn_historico.styleSheet()
                if current_style == destaque_style:
                    self.btn_historico.setStyleSheet(original_style)
                else:
                    self.btn_historico.setStyleSheet(destaque_style)

            # Criar o temporizador para piscar
            self.timer_piscar = QTimer(self)
            self.timer_piscar.timeout.connect(alternar_estilo)
            self.timer_piscar.start(500)  # Pisca a cada 500ms (0.5 segundo)

            # Parar o piscar após 5 segundos
            QTimer.singleShot(5000, lambda: self.timer_piscar.stop())
            QTimer.singleShot(5000, lambda: self.btn_historico.setStyleSheet(original_style))
#*********************************************************************************************************************
    def atualizar_usuario_no_bd(self):
        if not self.is_editing or not self.selected_user_id:
            # Criar uma mensagem personalizada
            mensagem = QMessageBox(self)
            mensagem.setIcon(QMessageBox.Warning)
            mensagem.setWindowTitle("Aviso")
            mensagem.setText("Nenhum usuário selecionado para atualização!")

            # Adicionar o botão OK com o estilo padrão
            mensagem.setStandardButtons(QMessageBox.Ok)
            
            # Estilizar a mensagem (fundo branco e texto preto)
            mensagem.setStyleSheet("""
                QLabel { 
                    color: black; 
                    background-color: white;
                }
                QMessageBox { 
                    background-color: white; 
                    border: none;
                }
                QPushButton {
                    background-color: #f0f0f0; 
                    border: 1px solid #0078d7;
                    padding: 3px 10px;
                    border-radius: 5px;
                    width: 55px;
        
                }
                QPushButton:hover {
                    background-color: #d0d0d0;
                    border: 1px solid #0078d7;  /* Azul claro */
                }
                QPushButton:pressed {
                    background-color: #a0a0a0;
                    border: 1px solid #8f8f8f;
                }
            """)

            # Executar a mensagem
            mensagem.exec()
            return

        # Obtendo os dados atualizados do usuário da interface
        usuario_nome = self.txt_nome.text() or "Não Cadastrado"
        usuario_usuario = self.txt_usuario.text() or "Não Cadastrado"
        usuario_telefone = self.txt_telefone.text() or "Não Cadastrado"
        usuario_endereco = self.txt_endereco.text() or "Não Cadastrado"
        usuario_numero = self.txt_numero.text() or "Não Cadastrado"
        usuario_complemento = self.txt_complemento.text() or "Não Cadastrado"
        usuario_email = self.txt_email.text() or "Não Cadastrado"
        usuario_data_nascimento = self.txt_data_nascimento.text() or "Não Cadastrado"
        usuario_rg = self.txt_rg.text() or "Não Cadastrado"
        usuario_cpf = self.txt_cpf.text() or "Não Cadastrado"
        usuario_cep = self.txt_cep.text() or "Não Cadastrado"
        usuario_estado = self.txt_estado.text() or "Não Cadastrado"
        usuario_senha = self.txt_senha.text() or "Não Cadastrado"
        usuario_confirmar_senha = self.txt_confirmar_senha.text() or "Não Cadastrado"
        usuario_imagem = None

        # Verificar se todos os campos obrigatórios estão preenchidos
        if (not usuario_nome or not usuario_usuario or not usuario_telefone or not usuario_endereco or
                not usuario_numero or not usuario_complemento or not usuario_email or not usuario_data_nascimento or not usuario_rg or
                not usuario_cpf or not usuario_cep or not usuario_estado or not usuario_senha or
                not usuario_confirmar_senha):
            QMessageBox.warning(self, "Aviso", "Todos os campos são obrigatórios!")
            return

        # Verificar se as senhas coincidem
        if usuario_senha != usuario_confirmar_senha:
            QMessageBox.warning(self, "Aviso", "As senhas não coincidem!")
            return

        # Verificar se o CPF é válido
        if not self.validar_cpf(usuario_cpf):
            QMessageBox.warning(self, "Aviso", "CPF inválido!")
            return

        # Verificar se o e-mail é válido
        if not self.validar_email(usuario_email):
            QMessageBox.warning(self, "Aviso", "E-mail inválido!")
            return

        # Verificar se o número de telefone é válido
        if not self.validar_telefone(usuario_telefone):
            QMessageBox.warning(self, "Aviso", "Número de telefone inválido!")
            return

        # Obtendo a imagem em base64
        usuario_imagem = None
        pixmap = self.label_imagem_cadastro.pixmap()
        if (pixmap and not pixmap.isNull()):
            byte_array = QByteArray()
            buffer = QBuffer(byte_array)
            buffer.open(QIODevice.WriteOnly)
            pixmap.save(buffer, "PNG")
            imagem_bytes = byte_array.toBase64()
            usuario_imagem = str(imagem_bytes, encoding='utf-8')

        # Construir a consulta SQL
        sql = """
            UPDATE users 
            SET Nome=?, Telefone=?, Endereço=?, Número=?, Complemento=?, 
            Email=?, Data_Nascimento=?, RG=?, CPF=?, CEP=?, Estado=?, Senha=?,
            "Confirmar Senha"=? 
            WHERE id=?
        """

        # Valores para substituir os placeholders
        valores = (usuario_nome, usuario_telefone, usuario_endereco, usuario_numero, usuario_complemento,
                usuario_email, usuario_data_nascimento, usuario_rg, usuario_cpf, usuario_cep,
                usuario_estado, usuario_senha, usuario_confirmar_senha, self.selected_user_id)

        # Se uma nova imagem foi selecionada, inclua-a na consulta SQL
        if usuario_imagem:
            sql = """
                UPDATE users 
                SET Nome=?, Telefone=?, Endereço=?, Número=?, Complemento=?, 
                Email=?, Data_Nascimento=?, RG=?, CPF=?, CEP=?, Estado=?, Senha=?, Imagem=?,
                "Confirmar Senha"=? 
                WHERE id=?
            """
            # Adicione a imagem aos valores
            valores = (usuario_nome, usuario_telefone, usuario_endereco, usuario_numero, usuario_complemento,
                    usuario_email, usuario_data_nascimento, usuario_rg, usuario_cpf, usuario_cep,
                    usuario_estado, usuario_senha, usuario_imagem, usuario_confirmar_senha, self.selected_user_id)

        # Tentar executar a consulta SQL
        try:
            with self.connection:
                cursor = self.connection.cursor()
                cursor.execute(sql, valores)
            QMessageBox.information(self, "Sucesso", "Usuário atualizado com sucesso!")
            # Resetar o estado de edição
            self.is_editing = False
            self.selected_user_id = None
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
                    imagem_bytes = QByteArray.fromBase64(usuario[15].encode('utf-8'))
                    pixmap = QPixmap()
                    pixmap.loadFromData(imagem_bytes, "PNG")
                    self.label_imagem_cadastro.setPixmap(pixmap)
                
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

    def validar_email(self, email):
        # Usando uma expressão regular para validar o formato do e-mail
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{3,}$'
        return bool(re.match(regex, email))

    def validar_telefone(self, telefone):
        # Remover caracteres não numéricos
        telefone = re.sub('[^0-9]', '', telefone)
        print("Número de digitos", len(telefone))

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
                    self.label_imagem_cadastro.setPixmap(pixmap)

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
            self.login_window.config.salvar_configuracoes("",False)

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
            senha = self.obter_senha_salva()
            
            tipo_usuario = self.login_window.check_user(usuario, senha)
            
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
                valor_float = float(valor)
            except ValueError:
                QMessageBox.warning(self, "Erro", "Valor inválido")
                return
            if valor_float < 5:
                self.mostrar_erro_desconto()
                return
            valor_porcentagem = valor_float / 100
            valor_formatado = "{:.2f}%".format(valor_porcentagem)
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
        # Verificar se todos os campos obrigatórios estão preenchidos
        if not all([self.txt_nome.text(), self.perfil_usuarios.currentText(), self.txt_senha.text(), 
                    self.txt_confirmar_senha.text(), self.txt_endereco.text(), self.txt_cep.text(), self.txt_cpf.text(), 
                    self.txt_numero.text(), self.perfil_estado.currentText(), self.txt_email.text(), self.txt_telefone.text(),
                    self.txt_data_nascimento.text(), self.txt_rg.text()]):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Erro")
            msg.setText("Todos os campos são obrigatórios.")
            msg.exec()
            return

        # Verificar se as senhas coincidem
        if self.txt_senha.text() != self.txt_confirmar_senha.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Erro")
            msg.setText("As senhas não são iguais")
            msg.exec()
            return

        # Verificar se o email é válido
        if not self.is_valid_email(self.txt_email.text()):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle('Erro')
            msg.setText("Por favor, insira um e-mail correto")
            msg.exec()
            return

        # Verificar se uma imagem foi carregada
        if not self.label_imagem_cadastro.pixmap():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Erro")
            msg.setText("É necessário inserir uma imagem antes de fazer o cadastro!! ")
            msg.exec()
            return

        # Extrair dados dos campos de entrada
        nome = self.txt_nome.text()
        user = self.txt_usuario.text()
        senha = self.txt_senha.text()
        confirmar_senha = self.txt_confirmar_senha.text()
        acesso = self.perfil_usuarios.currentText()
        endereco = self.txt_endereco.text()
        cep = self.txt_cep.text()
        cpf = self.txt_cpf.text()
        numero = self.txt_numero.text()
        estado = self.perfil_estado.currentText()
        email = self.txt_email.text()
        telefone = self.txt_telefone.text()
        rg = self.txt_rg.text()
        data_nascimento = self.txt_data_nascimento.text()
        complemento = self.txt_complemento.text()
        imagem = self.get_image_as_bytes()

        # Conectar ao banco de dados e inserir o usuário
        db = DataBase()
        db.connecta()

        try:
           
            # Obter o usuário logado
            usuario_logado = self.config.obter_usuario_logado()
            print(f"Usuário recebido: ",{usuario_logado})

            # Salvar o usuário logado no banco
            db.salvar_usuario_logado(usuario_logado)

            # Verificar se o usuário já está cadastrado pelo CPF ou nome de usuário
            user_exists_result = db.user_exists(cpf, user)
            if user_exists_result == 'cpf':
                QMessageBox.critical(None, "Erro", "O usuário com este CPF já está cadastrado. Por favor, insira um CPF diferente.")
                return
            elif user_exists_result == 'Usuário':
                QMessageBox.critical(None, "Erro", "Este nome de usuário já está em uso. Por favor, escolha um nome de usuário diferente.")
                return

            # Inserir o usuário no banco de dados
            db.insert_user(nome, user, senha, confirmar_senha, acesso, endereco, cep, cpf, numero, 
                        estado, email, telefone, rg, data_nascimento, complemento, usuario_logado, imagem)  
            db.close_connection()

            # Exibir mensagem de sucesso
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Cadastro de Usuário")
            msg.setText("Cadastro realizado com sucesso")
            msg.exec()

            # Limpar os campos de entrada após a conclusão do cadastro
            self.txt_nome.setText("")
            self.txt_usuario.setText("")
            self.txt_senha.setText("")
            self.txt_confirmar_senha.setText("")
            self.txt_cpf.setText("")
            self.txt_email.setText("")
            self.txt_numero.setText("")
            self.txt_endereco.setText("")
            self.txt_cep.setText("")
            self.txt_complemento.setText("")
            self.txt_rg.setText("")
            self.txt_telefone.setText("")
            self.txt_data_nascimento.setText("")
            
            if self.frame_imagem_cadastro.layout():
                old_layout = self.frame_imagem_cadastro.layout()
                while old_layout.count():
                    item = old_layout.takeAt(0)
                    widget = item.widget()
                    if widget:
                        widget.setParent(None)
                self.frame_imagem_cadastro.setLayout(None)

        except Exception as e:
            # Exibir mensagem de erro se ocorrer algum problema durante a inserção
            error_message = f"Erro ao cadastrar usuário {user}: {str(e)}"
            QMessageBox.critical(None, "Erro", error_message)

#*********************************************************************************************************************
    def get_image_as_bytes(self):
        # Verificar se há uma imagem carregada no QLabel
        if self.label_imagem_cadastro.pixmap():
            # Obter o pixmap da imagem
            pixmap = self.label_imagem_cadastro.pixmap()
            # Obter a imagem como uma sequência de bytes
            bytes_array = QByteArray()
            buffer = QBuffer(bytes_array)
            buffer.open(QIODevice.WriteOnly)
            pixmap.save(buffer, "PNG")  # Salvar a imagem como PNG
            # Retornar a sequência de bytes da imagem
            return bytes_array.toBase64().data()

        return None  # Retornar None se não houver imagem carregada
#*********************************************************************************************************************

    def erros_frames(self):
        # Definir os campos obrigatórios e seus respectivos frames de erro
        self.campos_obrigatorios = {
            'produto': self.txt_produto,
            'quantidade': self.txt_quantidade,
            'valor_produto': self.txt_valor_produto_3,
            'data_compra': self.dateEdit_3,
            'cliente': self.txt_cliente_3,
            'descricao': self.txt_descricao_produto_3
        }

        self.frames_erro = {
            'produto': self.frame_erro_produto,
            'quantidade': self.frame_erro_quantidade,
            'valor_produto': self.frame_erro_valor_produto,
            'data_compra': self.frame_erro_data_compra,
            'cliente': self.frame_erro_cliente,
            'descricao': self.frame_erro_descricao
        }

        # Esconder todos os frames de erro inicialmente
        for frame in self.frames_erro.values():
            frame.hide()

        # Conectar o sinal focusIn ao método esconder_asteriscos
        for widget in self.campos_obrigatorios.values():
            widget.installEventFilter(self)

    def exibir_asteriscos(self, campos_nao_preenchidos):
        for campo in campos_nao_preenchidos:
            frame = self.frames_erro.get(campo)
            if frame and not hasattr(self, f'label_asterisco_{campo}'):
                label = QLabel(frame)
                asterisco_pixmap = QPixmap("imagens/Imagem1.png").scaled(12, 12, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                label.setPixmap(asterisco_pixmap)
                label.setAlignment(Qt.AlignCenter)
                setattr(self, f'label_asterisco_{campo}', label)
            
            frame.show()
            getattr(self, f'label_asterisco_{campo}').show()

    def esconder_asteriscos(self):
        for frame in self.frames_erro.values():
            frame.hide()

    def eventFilter(self, obj, event):
        if event.type() == QEvent.FocusIn:
            for campo, widget in self.campos_obrigatorios.items():
                if obj == widget:
                    self.esconder_asteriscos()
        return super().eventFilter(obj, event)

    
#*********************************************************************************************************************  
    def atualizar_valores_frames(self, quantidade, valor_do_desconto, valor_com_desconto):
        # Verificar se o valor com desconto é zero e definir a mensagem apropriada
        valor_com_desconto_formatado = locale.currency(valor_com_desconto, grouping=True)
        valor_do_desconto_formatado = "Sem desconto" if valor_do_desconto == 0 else locale.currency(valor_do_desconto, grouping=True)
        valor_total_formatado = locale.currency(valor_com_desconto + valor_do_desconto, grouping=True)

        # Atualizar os textos dos frames
        self.frame_valor_desconto.setText(valor_com_desconto_formatado)
        self.frame_valor_do_desconto.setText(valor_do_desconto_formatado)
        self.frame_quantidade.setText("{:.0f}".format(quantidade))
        self.frame_valor_total_produtos.setText(valor_total_formatado)

        # Mostrar os frames
        self.frame_valor_total_produtos.show()
        self.frame_valor_do_desconto.show()
        self.frame_valor_desconto.show()
        self.frame_quantidade.show()

        # Configurar as geometrias dos frames
        altura = 101
        largura_default = 335

        # Ajustar a geometria do frame de desconto dependendo do valor
        if valor_do_desconto == 0:
            largura = 300  # Ajuste a largura para acomodar "Sem desconto"
            self.frame_valor_do_desconto.setGeometry(100, 50, largura, altura)
        else:
            largura = largura_default
            self.frame_valor_do_desconto.setGeometry(125, 45, largura, altura)

        # Ajustar a posição e a largura dos outros frames
        self.frame_valor_total_produtos.setGeometry(125, 45, largura, altura)
        self.frame_valor_desconto.setGeometry(115, 45, largura, altura)
        self.frame_quantidade.setGeometry(135, 50, largura, altura)    

        # Atualizar os frames para exibir os novos valores
        self.frame_valor_total_produtos.adjustSize()
        self.frame_valor_do_desconto.adjustSize()
        self.frame_valor_desconto.adjustSize()
        self.frame_quantidade.adjustSize()

#*********************************************************************************************************************
    def inserir_produto_no_bd(self, produto_info):
        try: 
            db = DataBase()
            db.connecta()

            # Formatando o valor_real com o símbolo "R$" e duas casas decimais
            valor_real_formatado = f"R$ {produto_info['valor_produto']:.2f}"

            # Se o desconto for zero, inserir "Sem desconto", caso contrário, formatar com porcentagem
            desconto_formatado = "Sem desconto" if produto_info['desconto'] == 0 else f"{produto_info['desconto']:.2f}%"

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
                produto_info["data_compra"],
                produto_info["codigo_item"],
                produto_info["cliente"],
                produto_info["descricao_produto"],
                usuario_logado,  # Passando o usuário logado
                imagem_bytes  # Adicionando a imagem aqui
            )
            db.close_connection()
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao cadastrar produto: {str(e)}")
        
        # Registrar no histórico após a inserção do produto
        descricao = f"Produto {produto_info['produto']} foi cadastrado com quantidade {produto_info['quantidade']} e valor {valor_real_formatado}."
        self.registrar_historico("Cadastro de Produto", descricao)
            
    def get_usuario_logado(self):
        # Obtenha o usuário logado das configurações
        return self.config.obter_usuario_logado()
#*********************************************************************************************************************
    def subscribe_produto(self):
        # Verificar se todos os campos obrigatórios estão preenchidos
        campos_nao_preenchidos = [
            campo for campo, widget in self.campos_obrigatorios.items()
            if not widget.text()
        ]

        if campos_nao_preenchidos:
            self.exibir_asteriscos(campos_nao_preenchidos)  # Mostrar os asteriscos nos campos obrigatórios
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Erro")
            msg.setText("Todos os campos obrigatórios precisam ser preenchidos.")
            msg.exec()
            return
        
        # Verificar se o nome do produto começa com um número ou caractere especial
        if re.match(r'^[\d\W]', self.txt_produto.text()):
            self.exibir_asteriscos(["produto"])  # Mostrar o asterisco ao lado do campo Produto

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Erro")
            msg.setText("O nome do produto não pode começar com um número ou caractere especial.")
            msg.exec()
            return
        else:
            self.esconder_asteriscos()  # Esconder os asteriscos se não houver erro

        # Verificar se não estamos no modo de edição
        if not self.is_editing:
            codigo_item = self.gerar_codigo_aleatorio()
            self.txt_codigo_item.setText(codigo_item)

        # Obter os valores dos campos
        valor_produto_str = self.txt_valor_produto_3.text().replace('R$', '').replace('.', '').replace(',', '.').strip()
        valor_produto = float(valor_produto_str) if valor_produto_str else 0.0

        quantidade_str = self.txt_quantidade.text().strip()
        quantidade = int(quantidade_str) if quantidade_str else 0

        desconto_str = self.txt_desconto_3.text().replace('%', '').strip().replace(',', '.')  # Removendo o símbolo de porcentagem
        desconto = float(desconto_str) if desconto_str and desconto_str != 'Sem desconto' else 0.0

        # Atualizar o valor do desconto na QLineEdit
        self.txt_desconto_3.setText("Sem desconto" if desconto == 0 else f"{desconto}%")

        # Atualizar o valor do desconto na QLineEdit se não tiver desconto
        if desconto == 0:
            self.txt_desconto_3.setText("Sem desconto")
            desconto = 0.0  # Definir desconto como zero para cálculo e banco de dados

        # Calcular o valor total do produto antes do desconto
        valor_total = quantidade * valor_produto
        valor_desconto = valor_total * desconto
        valor_com_desconto = valor_total - valor_desconto

        # Adicionar os dados do produto aos produtos pendentes
        produto_info = {
            "produto": self.txt_produto.text(),
            "quantidade": quantidade,
            "valor_produto": valor_produto,
            "desconto": desconto,
            "data_compra": self.dateEdit_3.date().toString("dd/MM/yyyy"),
            "codigo_item": self.txt_codigo_item.text(),
            "cliente": self.txt_cliente_3.text(),
            "descricao_produto": self.txt_descricao_produto_3.text()
        }

        # Adicionar produto na lista de produtos pendentes
        if produto_info not in self.produtos_pendentes:
            self.produtos_pendentes.append(produto_info)

        # Retornar os valores calculados para exibição
        return quantidade, valor_desconto, valor_com_desconto

    
    def verificar_alteracoes_produto(self, produto_original):
        # Obtém os valores atuais dos campos de texto
        try:
            valor_produto = float(self.txt_valor_produto_3.text().replace('R$', '').replace('.', '').replace(',', '.').strip())
        except ValueError:
            valor_produto = 0.0  # Valor padrão ou tratamento para erro

        try:
            desconto_str = self.txt_desconto_3.text().replace('%', '').replace(',', '.').strip()
            desconto = float(desconto_str) if desconto_str and desconto_str != 'Sem desconto' else 0.0
        except ValueError:
            desconto = 0.0  # Valor padrão ou tratamento para erro

        produto_atual = {
            "produto": self.txt_produto.text(),
            "quantidade": int(self.txt_quantidade.text()) if self.txt_quantidade.text().isdigit() else 0,
            "valor_produto": valor_produto,
            "desconto": desconto,
            "data_compra": self.dateEdit_3.date().toString("dd/MM/yyyy"),
            "codigo_item": self.txt_codigo_item.text(),
            "cliente": self.txt_cliente_3.text(),
            "descricao_produto": self.txt_descricao_produto_3.text()
        }

        # Compara o estado atual com o original
        return produto_atual != produto_original


    def exibir_tabela_produtos(self):
        dialog_atualizacao = AtualizarProduto(self)
        dialog_atualizacao.exec()
#*********************************************************************************************************************
    def adicionar_produto(self):
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
            
            self.atualizar_valores_frames(quantidade, valor_do_desconto, valor_com_desconto)

            # Limpar produto selecionado após a adição
            self.produto_selecionado = None
#*********************************************************************************************************************
    def confirmar_produtos(self):
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
        self.limpar_campos()
        
        # Limpar a imagem
        self.label_imagem_produto.clear()
        self.imagem_carregada_produto = None

        self.dateEdit_3.setDate(QDate.currentDate())  # Define a data atual
        self.dateEdit_3.clear()

        # Exibir mensagem de sucesso apenas se todos os campos estiverem preenchidos
        self.mostrar_mensagem_sucesso()
#*********************************************************************************************************************    
    def gerar_codigo_aleatorio(self, length=12):
        caracteres = string.ascii_uppercase + string.digits
        codigo_aleatorio = ''.join(random.choice(caracteres) for _ in range(length))
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
    def limpar_campos_após_atualizar(self):
        self.txt_produto.clear()
        self.txt_quantidade.clear()
        self.txt_valor_produto_3.clear()
        self.txt_desconto_3.clear()
        self.txt_codigo_item.clear()
        self.txt_cliente_3.clear()
        self.txt_descricao_produto_3.clear()
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
        # Verificar se algum produto foi selecionado na tabela
        if not hasattr(self, 'produto_id') or not self.produto_id:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setText("Não há produto selecionado para seguir.")
            msgBox.setWindowTitle("Aviso")
            
            # Adicionar botão "Detalhes"
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
        else:
            # Verificar se a imagem foi alterada
            produto_imagem = None
            if hasattr(self, 'nova_imagem') and self.nova_imagem:
                pixmap = QPixmap(self.nova_imagem)
                if not pixmap.isNull():
                    byte_array = QByteArray()
                    buffer = QBuffer(byte_array)
                    buffer.open(QIODevice.WriteOnly)
                    pixmap.save(buffer, "PNG")
                    produto_imagem = byte_array.toBase64().data().decode()

            # Obter os dados dos campos
            produto_nome = self.txt_produto.text()
            produto_quantidade = self.txt_quantidade.text()
            produto_valor_real = self.txt_valor_produto.text()
            produto_desconto = self.txt_desconto_3.text()
            produto_data_compra = self.dateEdit_3.date().toString("dd/MM/yyyy")
            produto_codigo_item = self.txt_codigo_item.text()
            produto_cliente = self.txt_cliente_3.text()
            produto_descricao = self.txt_descricao_produto_3.text()
            produto_id = self.produto_id

            # Conectar ao banco de dados
            db = DataBase()
            try:
                db.connecta()
                # Atualizar o produto no banco de dados
                db.atualizar_produto(produto_id, produto_nome, produto_quantidade, produto_valor_real,
                                    produto_desconto, produto_data_compra, 
                                    produto_codigo_item, produto_cliente, produto_descricao, produto_imagem)
                msgBox2 = QMessageBox(QMessageBox.Information, "Sucesso", "Produto atualizado com sucesso!")
                msgBox2.exec()
                self.limpar_imagem_produto_após_atualizar()
                self.limpar_campos()
            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Erro ao atualizar o produto: {str(e)}")
            finally:
                db.close_connection()

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
    def formatar_cep(self, text):
        if len(text) <= 9 and text.isdigit():
            if len(text) == 5:
                self.txt_cep.setText(text + "-")
            elif len(text) == 9:
                cep_formatado = "{}-{}".format(text[:5], text[5:])
                self.txt_cep.setText(cep_formatado)
        elif len(text) > 9:
            self.txt_cep.setText(text[:-1])
#*********************************************************************************************************************

    def formatar_cpf(self, text):
        # Remover caracteres não numéricos
        numero_cpf = ''.join(filter(str.isdigit, text))
        
        # Verificar se o CPF tem pelo menos 9 dígitos
        if len(numero_cpf) >= 9:
            # Formatar o CPF com pontos e hífen
            if len(numero_cpf) > 11:
                cpf_formatado = "{}.{}.{}-{}".format(numero_cpf[:3], numero_cpf[3:6], numero_cpf[6:9], numero_cpf[9:11])
            else:
                cpf_formatado = "{}.{}.{}-{}".format(numero_cpf[:3], numero_cpf[3:6], numero_cpf[6:9], numero_cpf[9:])
            self.txt_cpf.setText(cpf_formatado)
        else:
            # Se o CPF não tiver pelo menos 9 dígitos, manter o texto original
            self.txt_cpf.setText(text[:14])
#*********************************************************************************************************************
    def formatar_rg(self, text):
        # Remover caracteres não numéricos
        numero_rg = ''.join(filter(str.isdigit, text))
        
        # Verificar se o RG tem pelo menos 9 dígitos
        if len(numero_rg) >= 9:
            # Formatar o RG com pontos e hífen
            rg_formatado = "{}.{}.{}-{}".format(numero_rg[:2], numero_rg[2:5], numero_rg[5:8], numero_rg[8:9])
            self.txt_rg.setText(rg_formatado)
        else:
            # Se o RG não tiver pelo menos 9 dígitos, manter o texto original
            self.txt_rg.setText(text)
#*********************************************************************************************************************
    def formatar_data_nascimento(self, text):
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

        # Atualizar o texto do campo de data de nascimento
        self.txt_data_nascimento.setText(data_formatada)
#*********************************************************************************************************************

    def formatar_telefone(self, text):
        # Remover todos os caracteres que não são dígitos
        numero_limpo = ''.join(filter(str.isdigit, text))
        
        # Limitar o texto a 14 caracteres
        numero_limpo = numero_limpo[:14]
        
        # Verificar se o número tem pelo menos 2 dígitos
        if len(numero_limpo) >= 2:
            numero_formatado = "({}) ".format(numero_limpo[:2])
            
            # Adicionar o hífen se o número tiver mais de 8 dígitos
            if len(numero_limpo) >= 8:
                numero_formatado += "{}-{}".format(numero_limpo[2:7], numero_limpo[7:11])
                
                # Atualizar o texto do campo de texto
                self.txt_telefone.setText(numero_formatado)
            else:
                # Se o número não tiver mais de 7 dígitos, apenas atualizar o texto
                self.txt_telefone.setText(numero_formatado + numero_limpo[2:])
    
#*******************************************************************************************************
    def conectar_botao_adicionar_produto(self):
        self.btn_adicionar_produto.clicked.connect(self.adicionar_produto)
#*********************************************************************************************************************
    def selecionar_imagem_usuario(self, row):
    # Obter o ID do usuário selecionado
        id_usuario = self.tabela_usuario_dialogo.item(row, 0).text()
        self.produto_id = id_usuario
        
        # Atualizar os campos e a imagem com base no produto selecionado
        self.atualizar_campos()
        self.atualizar_imagem()

#*******************************************************************************************************
    def mostrar_erro_desconto(self):
        detalhes_msg_detalhes = QMessageBox()
        detalhes_msg_detalhes.setIcon(QMessageBox.Information)
        detalhes_msg_detalhes.setWindowTitle("Detalhes do Erro")
        detalhes_msg_detalhes.setText("Os campos obrigatórios precisam estar preenchidos.")
        detalhes_msg_detalhes.exec()
#*******************************************************************************************************
    def limpar_campos(self):
        self.txt_produto.clear()
        self.txt_quantidade.clear()
        self.txt_valor_produto_3.clear()
        self.txt_desconto_3.clear()
        self.dateEdit_3.clear()
        self.txt_codigo_item.clear()
        self.txt_cliente_3.clear()
        self.txt_descricao_produto_3.clear()
        
        # Limpar o texto dos QLabel nos frames
        self.frame_valor_total_produtos.setText("")
        self.frame_valor_desconto.setText("")
        self.frame_quantidade.setText("")
        self.frame_valor_do_desconto.setText("")
        
        # Limpar o campo dateEdit e configurar para a data atual
        self.dateEdit_3.setDate(QDate.currentDate())
#*******************************************************************************************************
    def apagar_campos(self):
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
            self.limpar_campos()

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
    def is_valid_email(self, email):
        email = email.strip()
        email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{3,}$')
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

    def cor_estado_produto(self):
        pass




# Função principal
if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = Login(login_window=None)
    main_window = MainWindow (user=None, tipo_usuario=None, login_window=login_window)
    
    login_window.show()
    sys.exit(app.exec())


    