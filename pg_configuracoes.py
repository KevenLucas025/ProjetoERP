from PySide6.QtWidgets import (QWidget,QMenu, QVBoxLayout, 
                               QProgressBar,QApplication,QDialog,QMessageBox,
                               QToolButton,QMainWindow,QPushButton,QLabel,
                               QLineEdit,QTableWidget,QTextEdit,QAbstractItemView,
                               QStyledItemDelegate,QStyleOptionViewItem,QTableWidgetItem,
                               QAbstractScrollArea,QScrollArea,QHBoxLayout,QFrame,QSizePolicy,QComboBox)
from PySide6.QtCore import Qt, QTimer,QRect
from PySide6.QtGui import (QIcon,QKeySequence,QColor,
                           QTextDocument,QPainter,QFontMetrics,QTextCursor,QTextCharFormat,QPalette,QPixmap)
import os
import sys
from configuracoes import Configuracoes_Login
from dialogos import ComboDialog,DialogoEstilizado
from ui_login_4 import Ui_Mainwindow_Login
from utils import caminho_recurso
from mane_python import Ui_MainWindow
from pagamentos import MercadoPagoService
from packaging import version
import subprocess
from utils import Temas
import re
import string
import requests
from database import DataBase
import base64




class Pagina_Configuracoes(QWidget):
    def __init__(self,
                main_window, paginas_sistemas, frame_botoes_navegacoes, centralwidget, 
                 frame_2, frame_page_estoque, frame_5, frame_cadastro_usuario,
                 pg_cadastro_usuario, btn_avancar, btn_retroceder, btn_opcoes, btn_home, btn_verificar_estoque,
                 btn_cadastrar_produto, btn_cadastro_usuario, btn_clientes,
                 btn_importar, btn_gerar_saida, btn_estorno,
                 label_cadastramento, label_cadastramento_produtos,frame_valor_total_produtos,
                 frame_valor_do_desconto, frame_valor_desconto,frame_quantidade,login_window,parent=None):
        super().__init__(parent)
        self.atalhos = {}  # dicionário para guardar atalhos
        self.resultados_encontrados = []
        self.ultimo_texto_pesquisado = ""
        self.indice_atual = -1
        self.main_window_login = Ui_Mainwindow_Login()
        self.tema_obj = Temas()
        self.tema = self.tema_obj.config.get("tema", "claro")
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
        self.btn_importar = btn_importar
        self.btn_gerar_saida = btn_gerar_saida
        self.btn_estorno = btn_estorno
        self.label_cadastramento = label_cadastramento
        self.label_cadastramento_produtos = label_cadastramento_produtos
        self.frame_valor_total_produtos = frame_valor_total_produtos
        self.frame_valor_do_desconto = frame_valor_do_desconto
        self.frame_valor_desconto = frame_valor_desconto
        self.frame_quantidade = frame_quantidade
        self.historico_erros = {}
        self.login_window = login_window
        self.db = DataBase()
        self.mp_service = MercadoPagoService()
        
        self.login_window.label_foto_sistema.setPixmap(QPixmap(caminho_recurso("imagens/Imagem2.png")))

        # Criar a janela de configurações
        self.main_window.janela_config = QMainWindow()
        self.janela_config = self.main_window.janela_config
        self.janela_config.setWindowTitle("Configurações")
        self.janela_config.setMinimumSize(600, 500)
        
        # Aplica o style_sheet atual do sistema à janela de configurações
        self.janela_config.setStyleSheet(self.styleSheet())

        self.central = QWidget()
        self.layout = QVBoxLayout(self.central)
        self.janela_config.setCentralWidget(self.central)
       
        self.estilo_original_classico = Ui_MainWindow()
        self.config = Configuracoes_Login(main_window=main_window)
        

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
        
        self.aplicar_tema_inicial()

        
    def aplicar_tema_inicial(self):
        tema = self.config.tema
        if tema == "escuro":
            self.aplicar_modo_escuro_sem_progress()
        elif tema == "claro":
            self.aplicar_modo_claro_sem_progress()
        else:
            self.aplicar_modo_classico_sem_progress()


    def aplicar_tema_escuro(self):
        self.tema_obj.aplicar_tema_global(QApplication.instance())

        self.btn_opcoes.setIcon(QIcon(caminho_recurso("imagens/imagens_modo_escuro/seta_esquerda_preta.png"))) #Esse botão é o botão de retroceder, nomenclatura errada
        self.btn_retroceder.setIcon(QIcon(caminho_recurso("imagens/imagens_modo_escuro/seta_direita_preta.png"))) # Esse botão é o botão avançar, nomenclatura errada
        

        self.btn_retroceder.setGeometry(35, 5, 30, 30)  # Define a geometria do botão 'btn_retroceder'


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

    # --- Modos na inicialização (sem progress) ---
    def aplicar_modo_escuro_sem_progress(self):
        self.aplicar_tema_escuro()

    def aplicar_modo_claro_sem_progress(self):
        self.aplicar_tema_claro()

    def aplicar_modo_classico_sem_progress(self):
        self.aplicar_tema_classico()


    def aplicar_tema_claro(self):
        # Iterar sobre todos os widgets da aplicação e aplicar o estilo
        self.tema_obj.aplicar_tema_global(QApplication.instance())
        
        self.btn_opcoes.setIcon(QIcon(caminho_recurso("imagens/imagens_modo_escuro/seta_esquerda_preta.png")))  # Adicione o caminho do ícone de avançar
        self.btn_retroceder.setIcon(QIcon(caminho_recurso("imagens/imagens_modo_escuro/seta_direita_preta.png")))  # Adicione o caminho do ícone de retroceder
        
        self.btn_retroceder.setGeometry(35, 5, 30, 30)  # Define a geometria do botão 'btn_retroceder'


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
        # Iterar sobre todos os widgets da aplicação e aplicar o estilo
        self.tema_obj.aplicar_tema_global(QApplication.instance())
        
        self.btn_opcoes.setIcon(QIcon(caminho_recurso("imagens/seta esquerda 2.png")))  # Adicione o caminho do ícone de avançar
        self.btn_retroceder.setIcon(QIcon(caminho_recurso("imagens/seta_direita-removebg-preview.png")))  # Adicione o caminho do ícone de retroceder
        


    def configurar_menu_opcoes(self, parent_button):
        # Limpa o layout antes de adicionar novos botões
        self.limpar_layout(self.layout)
        # ------------------- MENU TEMA -------------------
        btn_tema = QToolButton(self.janela_config)
        btn_tema.setText("Sistema")
        btn_tema.setPopupMode(QToolButton.InstantPopup)
        btn_tema.setToolButtonStyle(Qt.ToolButtonTextOnly)
        btn_tema.setCursor(Qt.PointingHandCursor)
        btn_tema.setObjectName("btn_classe_tema") 
        btn_tema.setFixedHeight(38)
        menu_tema = QMenu(self.janela_config)
        menu_tema.addAction("Alterar para o modo escuro", self.aplicar_modo_escuro)
        menu_tema.addAction("Alterar para o modo claro", self.aplicar_modo_claro)
        menu_tema.addAction("Alterar para o modo clássico", self.aplicar_modo_classico)
        menu_tema.addAction("Feedback",self.main_window.mostrar_sugestao)
        menu_tema.addAction("Assinatura",self.aplicar_assinatura)
        btn_tema.setMenu(menu_tema)
        self.layout.addWidget(btn_tema)

        # ------------------- BOTÃO ATUALIZAÇÕES -------------------
        btn_atualizacoes = QToolButton(self.janela_config)
        btn_atualizacoes.setText("Atualizações")
        btn_atualizacoes.setPopupMode(QToolButton.InstantPopup)
        btn_atualizacoes.setToolButtonStyle(Qt.ToolButtonTextOnly)
        btn_atualizacoes.setCursor(Qt.PointingHandCursor)
        btn_atualizacoes.setObjectName("btn_classe_atualizacoes")
        btn_atualizacoes.setFixedHeight(38)
        menu_atualizacoes = QMenu(self.janela_config)
        menu_atualizacoes.addAction("Definir atualizações automaticamente",self.definir_atualizacoes_automaticamente)
        menu_atualizacoes.addAction("Não definir atualizações automáticas",self.nao_definir_autualizacoes_automaticamente)
        menu_atualizacoes.addAction("Verificar se há atualizações",lambda: self.verificar_atualizacoes())
        menu_atualizacoes.addAction("Exibir histórico de atualizações",self.exibir_historico_atualizacoes)
        btn_atualizacoes.setMenu(menu_atualizacoes)
        self.layout.addWidget(btn_atualizacoes)


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
        self.layout.addWidget(btn_fonte)

        # ------------------- MENU NOTIFICAÇÕES -------------------
        btn_notificacoes = QToolButton(self.janela_config)
        btn_notificacoes.setText("Notificações")
        btn_notificacoes.setPopupMode(QToolButton.InstantPopup)
        btn_notificacoes.setToolButtonStyle(Qt.ToolButtonTextOnly)
        btn_notificacoes.setCursor(Qt.PointingHandCursor)
        btn_notificacoes.setObjectName("btn_classe_notificacoes")
        btn_notificacoes.setFixedHeight(38)
        menu_notificacoes = QMenu(self.janela_config)
        menu_notificacoes.addAction("Definir todas as notificações",self.definir_todas_as_notificacoes)
        menu_notificacoes.addAction("Configurar notificação de boas-vindas",self.definir_notificacao_boas_vindas)
        menu_notificacoes.addAction("Configurar notificação de aviso irreversível",self.definir_aviso_irreversilvel)
        menu_notificacoes.addAction("Configurar notificação de aviso Excel para clientes jurídicos",self.definir_nao_mostrar_mensagem_arquivo_excel)
        menu_notificacoes.addAction("Configurar notificação de aviso Excel para clientes físicos",self.definir_nao_mostrar_mensagem_arquivo_excel_fisicos)
        menu_notificacoes.addAction("Configurar notificação de aviso sobre atualizações",self.definir_notificacao_atualizacoes)
        btn_notificacoes.setMenu(menu_notificacoes)
        self.layout.addWidget(btn_notificacoes)

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
        menu_atalhos.addAction("Abrir painel de atalhos",self.abrir_painel_atalhos)
        btn_atalhos.setMenu(menu_atalhos)
        self.layout.addWidget(btn_atalhos)

        # Mostrar janela
        self.janela_config.show()
        
    def criar_card_plano(self, titulo, preco, beneficios, callback, destaque=False):
        card = QFrame()
        card.setFixedSize(311, 300)
        card.setObjectName("cardPlano")

        layout = QVBoxLayout(card)
        layout.setSpacing(6)
        layout.setContentsMargins(12, 12, 12, 12)

        # TÍTULO
        lbl_titulo = QLabel(titulo)
        lbl_titulo.setStyleSheet("font-size: 18px; font-weight: bold;")
        lbl_titulo.setWordWrap(True)

        # PREÇO
        lbl_preco = QLabel(preco)
        lbl_preco.setStyleSheet("font-size: 14px; color: gray;")
        lbl_preco.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)

        layout.addWidget(lbl_titulo)
        layout.addWidget(lbl_preco)

        # 🔹 INCLUSÃO DE MODALIDADES (sempre logo abaixo do preço)
        lbl_modalidades = QLabel("Inclusão de modalidades")
        lbl_modalidades.setStyleSheet("font-size: 16px; font-weight: bold;")
        lbl_modalidades.setWordWrap(True)
        lbl_modalidades.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)

        layout.addWidget(lbl_modalidades)


        # 🔹 DEMAIS BENEFÍCIOS
        for b in beneficios:
            texto = b.strip()

            if "inclusão de modalidades" in texto.lower():
                continue  # já exibido acima

            label = QLabel(f"• {texto}")
            label.setStyleSheet("font-size: 14px;")
            label.setWordWrap(True)
            label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)

            layout.addWidget(label)

        layout.addStretch()

        # BOTÃO
        btn = QPushButton("Selecionar plano")
        btn.clicked.connect(callback)
        btn.setCursor(Qt.PointingHandCursor)
        layout.addWidget(btn)

        # BORDA DO CARD
        if destaque:
            card.setStyleSheet("""
                QFrame#cardPlano {
                    border: 2px solid #4f46e5;
                    border-radius: 10px;
                }
            """)
        else:
            card.setStyleSheet("""
                QFrame#cardPlano {
                    border: 1px solid #ccc;
                    border-radius: 10px;
                }
            """)

        return card


        
    def aplicar_assinatura(self):
        self.janela_assinatura = QMainWindow(self)
        self.janela_assinatura.setWindowTitle("Escolha seu plano")
        self.janela_assinatura.resize(760, 560)

        central = QWidget()
        self.janela_assinatura.setCentralWidget(central)

        layout = QHBoxLayout(central)
        layout.setSpacing(20)

        plano_basico = self.criar_card_plano(
            titulo="Plano Básico / Gratuito",
            preco="R$ 0,00",
            beneficios=[
                "Inclusão de modalidades",
                "Assistência a correções de erros"
            ],
            callback=self.realizar_cobranca_plano_basico
            
        )

        plano_pro = self.criar_card_plano(
            titulo="Plano Pro",
            preco="R$ 0,50",
            beneficios=[
                "Inclusão de modalidades",
                "Acesso ao cadastramento em massa de usuários",
                "Acesso ao cadastramento em massa de produtos",
                "Acesso a planilha de exemplos",
                "Assistência a correções de erros"
            ],
            callback=self.realizar_cobranca_plano_pro,
            destaque=True
        )

        layout.addStretch()
        layout.addWidget(plano_basico)
        layout.addWidget(plano_pro)
        layout.addStretch()

        self.janela_assinatura.show()
        
    def realizar_cobranca_plano_pro(self):
        email = self.config.obter_email_usuario()

        if not email:
            QMessageBox.warning(
                self,
                "E-mail necessário",
                "Cadastre um e-mail válido para continuar com o pagamento."
            )
            return

        # Cria o pagamento
        pagamento = self.mp_service.criar_pagamento_pix(
            valor=0.50,
            descricao="Plano Pro",
            email_cliente=email
        )

        # Pega só o ID do pagamento
        pagamento_id = pagamento.get("id")
        if not pagamento_id:
            QMessageBox.critical(
                self,
                "Erro no pagamento",
                "Não foi possível criar o pagamento.\nVerifique as credenciais ou o e-mail."
            )
            return

        # Abre a janela de pagamento com o ID
        self.abrir_janela_pagamento(pagamento_id)


        
    def realizar_cobranca_plano_basico(self):
        self.config.definir_plano("basico")
        QMessageBox.information(self, "Plano ativado", "Plano Básico ativado com sucesso.")
        
    def abrir_janela_pagamento(self, pagamento_id):
        dialog = QDialog(self)
        dialog.setWindowTitle("Pagamento - Plano Pro")
        dialog.setFixedSize(320, 400)

        layout = QVBoxLayout(dialog)

        lbl = QLabel("Selecione a forma de pagamento:")
        lbl.setStyleSheet("font-size: 14px; font-weight: bold;")
        layout.addWidget(lbl)

        combo = QComboBox(self)
        combo.addItems(["Débito", "Crédito", "PIX"])
        layout.addWidget(combo)

        qr_label = QLabel()
        layout.addWidget(qr_label)

        progress = QProgressBar()
        progress.setRange(0, 0)  # Indeterminado
        progress.hide()
        layout.addWidget(progress)

        btn_confirmar = QPushButton("Confirmar pagamento")
        layout.addWidget(btn_confirmar)

        def gerar_pix():
            if combo.currentText() != "PIX":
                QMessageBox.information(self, "Info", "Pagamento via PIX não selecionado.")
                return

            # Obter pagamento atualizado
            pagamento = self.mp_service.obter_pagamento(pagamento_id)

            # ⚡ Checa se point_of_interaction existe
            try:
                qr_code_base64 = pagamento["point_of_interaction"]["transaction_data"]["qr_code_base64"]
            except KeyError:
                QMessageBox.critical(self, "Erro", "QR Code não disponível para este pagamento.")
                return

            pixmap = QPixmap()
            pixmap.loadFromData(base64.b64decode(qr_code_base64))
            qr_label.setPixmap(pixmap.scaled(250, 250, Qt.KeepAspectRatio))

            progress.show()
            btn_confirmar.setEnabled(False)

            # Timer para verificar pagamento
            timer = QTimer()
            timer.setInterval(3000)
            def checar_pagamento():
                status = self.mp_service.obter_pagamento(pagamento_id).get("status")
                if status == "approved":
                    timer.stop()
                    progress.hide()
                    self.db.atualizar_plano_usuario(self.main_window.get_usuario_logado(), "Pro")
                    QMessageBox.information(self, "Pagamento aprovado", "Plano Pro ativado com sucesso!")
                    dialog.accept()
                elif status in ["cancelled", "rejected"]:
                    timer.stop()
                    progress.hide()
                    QMessageBox.warning(self, "Pagamento", "Pagamento não aprovado ou cancelado.")
                    btn_confirmar.setEnabled(True)

            timer.timeout.connect(checar_pagamento)
            timer.start()


        btn_confirmar.clicked.connect(gerar_pix)
        dialog.exec()



    def verificar_atualizacoes(self):
        try:
            url = "https://github.com/KevenLucas025/Sistema-Atualizador/raw/refs/heads/main/versao.json"

            response = requests.get(url, timeout=5)
            if response.status_code != 200:
                QMessageBox.warning(self.janela_config, "Erro", "Não foi possível verificar atualizações.")
                return

            dados = response.json()
            versao_remota = dados.get("versao")
            link_download = dados.get("url_download")

            versao_local = self.main_window.versao_instalada_local()

            # Há nova versão?
            if version.parse(versao_remota) > version.parse(versao_local):

                caixa = QMessageBox(self)
                caixa.setWindowTitle("Atualização disponível")
                caixa.setText(f"Uma nova versão ({versao_remota}) está disponível!\n\nDeseja baixar agora?")
                
                botao_sim = caixa.addButton("Sim",QMessageBox.YesRole)
                botao_nao = caixa.addButton("Não",QMessageBox.NoRole)
                
                caixa.exec()
                
                if caixa.clickedButton() == botao_sim:
                    self.main_window.baixar_atualizacao(versao_remota,link_download)
            else:
                QMessageBox.information(
                    self.janela_config,
                    "Atualizações",
                    "Você já está na versão mais recente."
                )

        except Exception as e:
            QMessageBox.warning(
                self.janela_config,
                "Erro",
                f"Falha ao verificar atualizações:\n{e}"
            )
            
    def exibir_historico_atualizacoes(self):
        if hasattr(self, "janela_historico"):
            try:
                if self.janela_historico.isVisible():
                    self.janela_historico.raise_()
                    self.janela_historico.activateWindow()
                    return
            except RuntimeError:
                del self.janela_historico

    
        config = self.tema_obj.carregar_config_arquivo()
        self.tema  = config.get("tema","claro")
        
        if getattr(sys, "frozen",False):
            # EXE → histórico no APPDATA
            caminho = os.path.join(
                self.main_window.pasta_estado(),
                "historico_atualizacoes.log"
            )
        else:
            # Python / VSCode → histórico no projeto
            caminho = os.path.join(
                self.main_window.pasta_do_sistema(),
                "historico_atualizacoes.log"
            )
            
        if getattr(sys, "frozen", False):
            os.makedirs(os.path.dirname(caminho), exist_ok=True)
            if not os.path.exists(caminho):
                open(caminho, "a", encoding="utf-8").close()

        
        if not os.path.exists(caminho):
            QMessageBox.information(
                self.janela_config,
                "Histórico de Atualizações",
                "Nenhuma atualização foi registrada até o momento"
            )
            return

        try:
            with open(caminho, "r", encoding="utf-8") as f:
                linhas = [l.strip() for l in f if l.strip()]

        except Exception as e:
            linhas = []
            QMessageBox.critical(
                self.janela_config,
                "Erro ao abrir histórico",
                "Não foi possível abrir o histórico de atualizações.\n\n"
                f"Motivo:\n{str(e)}"
            )
            return

        if not linhas:
            QMessageBox.information(
                self.janela_config,
                "Histórico de Atualizações",
                "Nenhuma atualização disponível no histórico"
            )
            return

        padrao = re.compile(
            r"\[(\d{2}/\d{2}/\d{4}) (\d{2}:\d{2}:\d{2})\]\s*"
            r"(.*?)(?:\s*\|\s*STATUS=(\w+))"
            r"(?:\s*\|\s*(.*))?$",
            re.IGNORECASE
        )

        registros = []

        for linha in linhas:
            match = padrao.search(linha)
            if match:
                data, hora, descricao, status, erro = match.groups()
                
                chave = f"{data} {hora}"

                if status.upper() == "ERRO":
                    descricao = "Falha ao aplicar atualização"
                    status = "Falha na atualização"
                    self.historico_erros[chave] = erro or "Motivo não informado"
                else:
                    status = "Sucesso"

                registros.append((data, hora, descricao, status))


        if not registros:
            QMessageBox.information(
                self.janela_config,
                "Histórico de Atualizações",
                "Nenhuma atualização válida encontrada no histórico"
            )
            return

        # =========================
        # QMainWindow
        # =========================
        self.janela_historico = QMainWindow(self.janela_config)
        self.janela_historico.setWindowTitle("Histórico de Atualizações")
        self.janela_historico.resize(700, 350)
        
        self.janela_historico.destroyed.connect(
            lambda: hasattr(self, "janela_historico") and delattr(self, "janela_historico")
        )

        #  CENTRAL WIDGET
        central = QWidget()
        self.janela_historico.setCentralWidget(central)

        layout = QVBoxLayout(central)
        
        if self.tema == "escuro":
            bg_color = "#2b2b2b"
            text_color = "white"
            
            table_view_style = """
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
        elif self.tema == "claro":
            bg_color = "white"
            text_color = "black"
            
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
                QHeaderView:vertical {
                    background-color: white; 
                    border: none;              
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
                """
        else: # clássico
            bg_color = "rgb(0,80,121)"
            text_color = "white"
            
             #  Scroll geral (scroll_style)
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
            #  Estilo específico para QTableView (table_view_style)
            table_view_style = """
                QTableView {
                    background-color: rgb(0,80,121);
                    color: white;
                    gridline-color: black;
                    border: 1px solid white;
                    selection-background-color: #007acc;
                    selection-color: white;
                }

                QHeaderView::section {
                    background-color: white;
                    color: black;
                    border: 1px solid #eeeeee;  /* Borda branco-acinzentada */
                    padding: 1px;
                }

                QTabWidget::pane {
                    border: 1px solid #004466;
                    background-color: #003355;
                }

                /* Scrollbars da QTableView - vertical */
                QTableView QScrollBar:vertical{
                    border: none;
                    background-color: rgb(255, 255, 255); /* fundo do track */
                    border-radius: 5px;
                    width: 10px; /* largura da barra vertical */
                    margin: 0px;
                
                }
                /* Scrollbars da QTableView - horizontal */
                QTableView QScrollBar:horizontal {
                    height: 11px;
                    background-color: rgb(255, 255, 255);
                    margin: 0px;
                }

                /* Handle dos scrolls (a parte que você arrasta) */
                QTableView QScrollBar::handle:vertical {
                    background-color: rgb(180, 180, 150);  /* cor do handle */
                    min-height: 10px;
                    min-width: 10px;
                    border-radius: 5px;
                
                }
                /* Handle dos scrolls (a parte que você arrasta) */
                QTableView QScrollBar::handle:horizontal {
                    background-color: rgb(180, 180, 150);
                    min-width: 20px;
                    border-radius: 5px;
                }

                /* Groove vertical */
                QTableView QScrollBar::groove:vertical {
                    background-color: rgb(100, 240, 240);  /* faixa visível no vertical */
                    border-radius: 2px;
                    width: 10px;
                    margin: 0px 10px 0px 10px;
                }

                /* Groove horizontal (faixa por onde o handle desliza) */
                QTableView QScrollBar::groove:horizontal {
                    background-color: rgb(220, 220, 220);
                    border-radius: 5px;
                    height: 10px;
                }

                QTableWidget::item:selected {
                    background-color: rgb(0, 120, 215);
                    color: white;
                }

                QTableCornerButton::section {
                    background-color: white;
                }
            """
        estilo_completo = f"""
        QMainWindow {{
            background-color: {bg_color};
        }}
        {table_view_style}
        {scroll_style}
        """

        # =========================
        # Tabela
        # =========================
        tabela = QTableWidget()
        tabela.setColumnCount(4)
        tabela.setHorizontalHeaderLabels([
            "Data", "Hora", "Versão da Atualização", "Status"
        ])
        
        

        tabela.setRowCount(len(registros))
        tabela.setEditTriggers(QTableWidget.NoEditTriggers)
        tabela.setSelectionBehavior(QTableWidget.SelectRows)
        tabela.horizontalHeader().setStretchLastSection(True)
        
        tabela.setContextMenuPolicy(Qt.CustomContextMenu)
        tabela.customContextMenuRequested.connect(
            lambda pos: self.abrir_menu_contexto_historico(pos, tabela)
        )


        for row, (data, hora, descricao, status) in enumerate(registros):
            tabela.setItem(row, 0, QTableWidgetItem(data))
            tabela.setItem(row, 1, QTableWidgetItem(hora))
            tabela.setItem(row, 2, QTableWidgetItem(descricao))
            tabela.setItem(row, 3, QTableWidgetItem(status.capitalize()))

            for col in range(4):
                tabela.item(row, col).setTextAlignment(Qt.AlignCenter)


        tabela.resizeColumnsToContents()
        tabela.resizeRowsToContents()

        layout.addWidget(tabela)

        # =========================
        # Botão Fechar
        # =========================
        btn_fechar = QPushButton("Fechar")
        def fechar_janela():
            self.janela_historico.close()
            self.janela_historico.deleteLater()
            del self.janela_historico

        btn_fechar.clicked.connect(fechar_janela)


        layout.addWidget(btn_fechar, alignment=Qt.AlignRight)
        self.janela_historico.setStyleSheet(estilo_completo)
        self.janela_historico.show()

    def abrir_menu_contexto_historico(self, pos,tabela: QTableWidget):
        index = tabela.indexAt(pos)
        if not index.isValid():
            return
        
        linha = index.row()
        
        data = tabela.item(linha, 0).text()
        hora = tabela.item(linha, 1).text()
        status = tabela.item(linha, 3).text()
        
        chave = f"{data} {hora}"
        
        menu = QMenu(tabela)
        
        detalhes_action = menu.addAction("Detalhes")
        
        
        action = menu.exec(tabela.viewport().mapToGlobal(pos))

        if action == detalhes_action:
            self.mostrar_detalhes_erro(chave)
        
        
        
    def mostrar_detalhes_erro(self, chave):
        if chave in self.historico_erros:
            erro = self.historico_erros.get(chave, "Motivo não informado")
            
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Falha na Atualização")
            msg.setText("Não foi possível aplicar a atualização")
            msg.setInformativeText(f"{erro}")
            msg.setStandardButtons(QMessageBox.Ok)
            
            copiar_btn = msg.addButton("Copiar erro",QMessageBox.ActionRole)
            msg.exec()
            
            
            if msg.clickedButton() == copiar_btn:
                QApplication.clipboard().setText(erro)
        else:
            msg = QMessageBox(self.janela_config)
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Atualização concluída")
            msg.setText("A atualização foi aplicada com sucesso.")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()

        
        
    def definir_atualizacoes_automaticamente(self):
        self.config.atualizacoes_automaticas = True
        self.config.salvar()
        
        QMessageBox.information(
            self.janela_config,
            "Atualizações automáticas",
            "As atualizações automáticas foram ativadas.\n\n"
            "O sistema irá baixar e aplicar atualizações automaticamente\n"
            "sempre que uma nova versão estiver disponível."
        )
    
    def nao_definir_autualizacoes_automaticamente(self):
        self.config.atualizacoes_automaticas = False
        self.config.salvar()

        QMessageBox.information(
            self.janela_config,
            "Atualizações automáticas",
            "As atualizações automáticas foram desativadas.\n\n"
            "O sistema ainda avisará quando houver nova versão,\n"
            "mas não irá baixar automaticamente."
        )
    def configurar_notificacao(self, nome_notificacao, attr_config):
        desativada = getattr(self.config, attr_config)
        
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setWindowTitle("Configurar Notificação")
        
        if desativada:
            msg_box.setText(
                f"A notificação {nome_notificacao} está ATIVADA.\n\n"
                "Deseja DESATIVAR essa notificação?"
            )
            
            
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_box.button(QMessageBox.Yes).setText("Sim")
        msg_box.button(QMessageBox.No).setText("Não")

        resposta = msg_box.exec()

        if resposta == QMessageBox.Yes:
            setattr(self.config, attr_config, not desativada)
            self.config.salvar()

            mensagem = (
                f"Notificação {nome_notificacao} ATIVADA com sucesso!"
                if desativada
                else
                f"Notificação {nome_notificacao} DESATIVADA com sucesso!"
            )

            QMessageBox.information(self, "Configuração Salva", mensagem)
  
    def definir_todas_as_notificacoes(self):
        estados = [
            self.config.nao_mostrar_mensagem_boas_vindas,
            self.config.nao_mostrar_aviso_irreversivel,
            self.config.nao_mostrar_mensagem_arquivo_excel,
            self.config.nao_mostrar_mensagem_arquivo_excel_fisicos,
            self.config.nao_mostrar_aviso_atualizacoes
        ]

        todas_desativadas = all(estados)
        todas_ativadas = not any(estados)
        estado_misto = not todas_desativadas and not todas_ativadas

        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setWindowTitle("Configurar Notificações")

        if estado_misto:
            msg_box.setText(
                "Algumas notificações estão ATIVADAS e outras DESATIVADAS.\n\n"
                "O que você deseja fazer com TODAS as notificações?"
            )
        elif todas_desativadas:
            msg_box.setText(
                "Todas as notificações estão DESATIVADAS.\n\n"
                "Deseja ATIVAR TODAS as notificações?"
            )
        else:
            msg_box.setText(
                "Todas as notificações estão ATIVADAS.\n\n"
                "Deseja DESATIVAR TODAS as notificações?"
            )

        # Botões conforme estado
        botao_ativar = None
        botao_desativar = None

        if estado_misto:
            botao_ativar = msg_box.addButton("Ativar todas", QMessageBox.AcceptRole)
            botao_desativar = msg_box.addButton("Desativar todas", QMessageBox.DestructiveRole)
        elif todas_desativadas:
            botao_ativar = msg_box.addButton("Ativar todas", QMessageBox.AcceptRole)
        else:
            botao_desativar = msg_box.addButton("Desativar todas", QMessageBox.DestructiveRole)

        msg_box.addButton("Cancelar", QMessageBox.RejectRole)

        msg_box.exec()
        botao_clicado = msg_box.clickedButton()

        if botao_clicado == botao_ativar:
            novo_estado = False
            mensagem = "Todas as notificações foram ATIVADAS com sucesso!"
        elif botao_clicado == botao_desativar:
            novo_estado = True
            mensagem = "Todas as notificações foram DESATIVADAS com sucesso!"
        else:
            return  # Cancelado

        self.config.nao_mostrar_mensagem_boas_vindas = novo_estado
        self.config.nao_mostrar_aviso_irreversivel = novo_estado
        self.config.nao_mostrar_mensagem_arquivo_excel = novo_estado
        self.config.nao_mostrar_mensagem_arquivo_excel_fisicos = novo_estado
        self.config.nao_mostrar_aviso_atualizacoes = novo_estado

        self.config.salvar()

        QMessageBox.information(self, "Configuração Salva", mensagem)

    def definir_nao_mostrar_mensagem_arquivo_excel(self):
        self.configurar_notificacao(
        "de aviso Excel para clientes jurídicos",
        "nao_mostrar_mensagem_arquivo_excel"
        )

    def definir_nao_mostrar_mensagem_arquivo_excel_fisicos(self):
        self.configurar_notificacao(
            "de aviso Excel para clientes físicos",
            "nao_mostrar_mensagem_arquivo_excel_fisicos"
        )


    def definir_aviso_irreversilvel(self):
        self.configurar_notificacao(
            "de aviso irreversível",
            "nao_mostrar_aviso_irreversivel"
        )


    def definir_notificacao_boas_vindas(self):
        self.configurar_notificacao(
            "de boas-vindas",
            "nao_mostrar_mensagem_boas_vindas"
        )

    def definir_notificacao_atualizacoes(self):
        self.configurar_notificacao(
            "de aviso atualização disponível",
            "nao_mostrar_aviso_atualizacoes"
        )


    def limpar_layout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        
    def mapear_teclas_atalhos(self):
        # 1. Perguntar qual ação o usuário quer mapear 
        opcoes = ["Pesquisar", "Abrir Mais Opções","Abrir Configurações","Abrir Página Inicial"] 
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
            if not tecla:
                return
            conflito = self.verificar_atalhos(tecla)
            atalhos_atuais = self.config.obter_todos_atalhos()

            # Se há conflito com outra ação
            if conflito and conflito != acao:
                resposta = QMessageBox.question(
                    self.janela_config,
                    "Atalho duplicado",
                    f"A tecla '{tecla}' já está sendo usada para {conflito};\n"
                    "Deseja trocar os atalhos entre as duas funções?",
                    QMessageBox.Yes | QMessageBox.No
                )
                if resposta == QMessageBox.No:
                    return
                # Troca as teclas entre as ações
                tecla_conflito = atalhos_atuais.get(acao, None)  # tecla atual da ação escolhida
                # conflito → ação que usava a tecla nova
                # acao → ação que o usuário está mapeando

                # Atualiza as duas no dicionário
                self.config.atalhos[conflito] = tecla_conflito or ""
                self.config.atalhos[acao] = tecla

                # Persiste no JSON
                self.config.salvar_atalho(conflito, self.config.atalhos[conflito])
                self.config.salvar_atalho(acao, tecla)

                # Atualiza no sistema (main)
                if tecla_conflito:
                    self.main_window.registrar_atalhos(conflito, tecla_conflito)
                self.main_window.registrar_atalhos(acao, tecla)

                QMessageBox.information(
                    self.janela_config,
                    "Troca realizada",
                    f"Atalhos trocados com sucesso:\n"
                    f"• {acao} → {tecla}\n"
                    f"• {conflito} → {tecla_conflito or 'nenhum atalho definido antes'}"
                )

                return

        # Se não há conflito, só salva normalmente
        self.config.salvar_atalho(acao, tecla)
        self.main_window.registrar_atalhos(acao, tecla)
        QMessageBox.information(self.janela_config, "Atalho salvo", f"Atalho '{tecla}' definido para '{acao}' com sucesso.")

    def verificar_atalhos(self, tecla):
        """Retorna a ação que já usa a tecla (se houver)"""
        atalhos_existentes = self.config.obter_todos_atalhos()
        for acao_existente, tecla_existente in atalhos_existentes.items():
            if tecla_existente and tecla_existente.lower() == tecla.lower():
                return acao_existente
        return None
    
    

    def abrir_painel_atalhos(self):
        """Exibe uma janela estilizada com a lista de atalhos registrados e suas funções."""
        atalhos_registrados = getattr(self.main_window, "atalhos", {})

        if not atalhos_registrados:
            QMessageBox.information(self, "Atalhos", "Nenhum atalho foi definido ainda.")
            return

        # --- CRIA A JANELA ---
        dialog = QDialog(self)
        dialog.setWindowTitle("Painel de Atalhos")
        dialog.resize(600, 500)
        


        layout = QVBoxLayout(dialog)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        


        # --- DEFINE CORES BASEADAS NO TEMA ATUAL ---
        config = self.tema_obj.carregar_config_arquivo()
        tema  = config.get("tema","claro")

        if tema == "escuro":
            text_cor = "white"
            bg_cor = "#202124"
            button_style = """
                QPushButton {
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                                stop:0 rgb(60,60,60),
                                                stop:1 rgb(100,100,100));
                    color: white;
                    border-radius: 8px;
                    font-size: 16px;
                    border: 2px solid #666666;
                    padding: 6px;
                }
                QPushButton:hover {
                    background-color: #444444;
                }
                QPushButton:pressed {
                    background-color: #555555;
                    border: 2px solid #888888;
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
                alternate-background-color: #202124;
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
            }"""
        elif tema == "claro":
            bg_cor = "white"
            text_cor = "black"
            button_style = """
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
            """
            scroll_style = """
                QScrollBar:vertical {
                    background: #ffffff;
                    width: 12px;
                    border-radius: 6px;
                }
                QScrollBar::handle:vertical {
                    background: #cccccc;
                    min-height: 20px;
                    border-radius: 5px;
                }
            """
            table_view_style = """
                /* QTableView com seleção diferenciada */
                QTableView {
                    background-color: white;
                    alternate-background-color: #f8f8f8;
                    color: black;
                    gridline-color: #cccccc;
                    selection-background-color: #d0e7ff;  /* azul claro */
                    selection-color: black;
                }
                QHeaderView:vertical {
                    background-color: white; 
                    border: none;              
                }


                /* Cabeçalhos da tabela */
                QHeaderView::section {
                    background-color: #eaeaea;
                    color: black;
                    border: 1px solid #cccccc;
                    padding: 2px;
                }"""
        else:  # clássico
            bg_cor = "rgb(0,80,121)"
            text_cor = "white"
            button_style = """
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
            QPushButton:pressed {
                background-color: #006bb3;
                border: 2px solid #005c99;
            }
            """
            scroll_style = """
                QScrollBar:vertical {
                    background: #ffffff;
                    width: 12px;
                    border-radius: 6px;
                }
                QScrollBar::handle:vertical {
                    background: #b4b4b4;
                    min-height: 20px;
                    border-radius: 5px;
                }
            """
            table_view_style = """
                QTableView {
                    background-color: rgb(0,80,121);
                    alternate-background-color: rgb(0, 80, 121);
                    color: white;
                    gridline-color: black;
                    border: 1px solid white;
                    selection-background-color: #007acc;
                    selection-color: white;
                }

                QHeaderView::section {
                    background-color: white;
                    color: black;
                    border: 1px solid #eeeeee;  /* Borda branco-acinzentada */
                    padding: 1px;
                }"""

        dialog.setStyleSheet(f"background-color: {bg_cor}; color: {text_cor};")

        # --- TÍTULO ---
        titulo = QLabel("🧭 <b>Lista de Atalhos</b>")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo.setStyleSheet(f"""
            color: {text_cor};
            font-size: 18px;
            margin-bottom: 10px;
        """)
        layout.addWidget(titulo)

        # --- TABELA ---
        tabela = QTableWidget()
        tabela.setColumnCount(2)
        tabela.setHorizontalHeaderLabels(["Ação", "Tecla"])
        tabela.horizontalHeader().setStretchLastSection(True)
        tabela.verticalHeader().setVisible(False)
        tabela.setEditTriggers(QTableWidget.NoEditTriggers)
        tabela.setSelectionMode(QTableWidget.NoSelection)
        tabela.setAlternatingRowColors(True)
        tabela.setStyleSheet(table_view_style)
        

        # --- POPULA A TABELA ---
        tabela.setRowCount(0)
        for i, (acao, shortcut) in enumerate(atalhos_registrados.items()):
            tabela.insertRow(i)
            item_acao = QTableWidgetItem(acao)
            item_tecla = QTableWidgetItem(shortcut.key().toString())
            item_acao.setTextAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)
            item_tecla.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            tabela.setItem(i, 0, item_acao)
            tabela.setItem(i, 1, item_tecla)

        # --- SCROLL AUTOMÁTICO ---
        tabela.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        layout.addWidget(tabela)

        tabela.resizeColumnsToContents()
        tabela.resizeRowsToContents()

        # --- BOTÃO FECHAR ---
        btn_fechar = QPushButton("Fechar")
        btn_fechar.setFixedWidth(100)
        btn_fechar.setStyleSheet(button_style)
        btn_fechar.clicked.connect(dialog.close)
        layout.addWidget(btn_fechar, alignment=Qt.AlignmentFlag.AlignRight)

        dialog.exec()
        
    def configurar_pesquisa(self):
        self.main_window.caixa_pesquisa.returnPressed.connect(self.acao_enter)
        self.main_window.btn_proximo.clicked.connect(self.proximo_resultado)
        self.main_window.btn_anterior.clicked.connect(self.anterior_resultado)


    def acao_enter(self):
        """ENTER faz a pesquisa se o texto mudou, ou vai para o próximo se for o mesmo texto."""
        texto = self.main_window.caixa_pesquisa.text().strip()
        if not texto:
            return

        # Se o texto é diferente → nova pesquisa
        if texto != self.ultimo_texto_pesquisado:
            self.ultimo_texto_pesquisado = texto
            self.executar_pesquisa()
        else:
            # Se já tem resultados → vai pro próximo
            if self.resultados_encontrados:
                self.proximo_resultado()
            else:
                # caso não tenha (ex: limpou resultados antes), pesquisa de novo
                self.executar_pesquisa()

    def cor_destaque_html(self):
        if self.tema == "escuro":
            return "rgba(80, 150, 255, 0.4)"
        elif self.tema == "clássico":
            return "rgba(50, 150, 250, 0.4)"
        else:  # claro
            return "rgba(50, 100, 200, 0.4)"

    def executar_pesquisa(self):
        texto = self.main_window.caixa_pesquisa.text().strip()
        diferenciar_maiusculas = self.main_window.checkbox_maiusculas.isChecked()

        self.main_window.label_contagem.setText("")
        self.main_window.btn_proximo.setEnabled(False)
        self.main_window.btn_anterior.setEnabled(False)

        # limpa os resultados anteriores
        self.resultados_encontrados = []
        self.indice_atual = -1
        self.resetar_destaques(self.main_window.centralWidget())

        if not texto:
            return

        pagina_atual = self.main_window.paginas_sistemas.currentWidget()
        self.buscar_todos_resultados(pagina_atual, texto, diferenciar_maiusculas)

        if self.resultados_encontrados:
            self.main_window.btn_proximo.setEnabled(True)
            self.main_window.btn_anterior.setEnabled(True)
            self.indice_atual = 0
            self.main_window.label_contagem.setText(f"1 de {len(self.resultados_encontrados)}")
            self.navegar_para_resultado(0)
        else:
            QMessageBox.warning(self, "Pesquisa", f"Nenhum resultado encontrado para: {texto}")

    
    def buscar_todos_resultados(self, widget, texto, case_sensitive):
        """Percorre todos os widgets e armazena TODAS as ocorrências (inclusive múltiplas por item)."""

        if not widget.isVisible() or isinstance(widget, (QPushButton, QLineEdit)):
            return

        # --- Caso 1: Tabelas ---
        if isinstance(widget, QTableWidget):
            for row in range(widget.rowCount()):
                for col in range(widget.columnCount()):
                    item = widget.item(row, col)
                    if not item:
                        continue

                    item_text = item.text().strip()

                    # Ignorar células vazias ou com caracteres invisíveis
                    if not item_text or all(c not in string.printable for c in item_text):
                        continue

                    texto_base = item_text if case_sensitive else item_text.lower()
                    texto_cmp = texto if case_sensitive else texto.lower()

                    start = 0
                    while True:
                        idx = texto_base.find(texto_cmp, start)
                        if idx == -1:
                            break

                        self.resultados_encontrados.append({
                            "tipo": "tabela",
                            "widget": item,
                            "row": row,
                            "col": col,
                            "pos": idx,
                            "len": len(texto)
                        })
                        start = idx + len(texto)
            return

        # --- Caso 2: QLabel ---
        elif isinstance(widget, QLabel):
            conteudo = widget.text()
            if not conteudo:
                return
            doc = QTextDocument()
            doc.setHtml(conteudo)
            texto_visivel = doc.toPlainText()

            texto_base = texto_visivel if case_sensitive else texto_visivel.lower()
            texto_cmp = texto if case_sensitive else texto.lower()

            start = 0
            while True:
                idx = texto_base.find(texto_cmp, start)
                if idx == -1:
                    break
                self.resultados_encontrados.append({
                    "tipo": "label",
                    "widget": widget,
                    "pos": idx,
                    "len": len(texto)
                })
                start = idx + len(texto)

        # --- Caso 3: QTextEdit (somente leitura) ---
        elif isinstance(widget, QTextEdit) and widget.isReadOnly():
            texto_edit = widget.toPlainText()
            texto_base = texto_edit if case_sensitive else texto_edit.lower()
            texto_cmp = texto if case_sensitive else texto.lower()

            start = 0
            while True:
                idx = texto_base.find(texto_cmp, start)
                if idx == -1:
                    break
                self.resultados_encontrados.append({
                    "tipo": "textedit",
                    "widget": widget,
                    "pos": idx,
                    "len": len(texto)
                })
                start = idx + len(texto)

        # --- Recursão ---
        for child in widget.findChildren(QWidget, options=Qt.FindDirectChildrenOnly):
            self.buscar_todos_resultados(child, texto, case_sensitive)



        
    def destacar_resultado_atual(self, resultado):
        """Destaca uma ocorrência específica (única posição) em QLabel, tabela ou QTextEdit."""
        self.resetar_destaques_tabelas()
        texto_procura = self.main_window.caixa_pesquisa.text()
        case_sensitive = self.main_window.checkbox_maiusculas.isChecked()
        cor = self.cor_destaque_html()

        tipo = resultado["tipo"]

        # Limpa destaque anterior de QLabel
        if hasattr(self, "ultimo_label_destacado") and self.ultimo_label_destacado is not None:
            texto_original = self.ultimo_label_destacado.property("texto_original")
            if texto_original:
                self.ultimo_label_destacado.setText(texto_original)
            self.ultimo_label_destacado = None

        # --- TABELA ---
        if tipo == "tabela":
            item = resultado["widget"] # O item da célula
            tabela = item.tableWidget()
            if tabela:
                delegate = CustomTableDelegate(
                    texto_procura=texto_procura,
                    case_sensitive=case_sensitive,
                    # MUDANÇA AQUI: Passe o dicionário de resultado completo
                    resultado_para_destaque=resultado, # <--- NOVO PARÂMETRO
                    tema=self.tema,
                    parent=tabela
                )
                tabela.setItemDelegate(delegate)
                tabela.viewport().update()
                tabela.scrollToItem(item, QAbstractItemView.EnsureVisible)
            return


        # --- QLabel ---
        elif tipo == "label":
            widget = resultado["widget"]
            pos = resultado["pos"] # Posição de início no texto PÚRO
            length = resultado["len"]
            cor = self.cor_destaque_html()

            # 1. Recupera o conteúdo original (PODE CONTER TAGS DE ESTILO DO QT)
            conteudo_original = widget.property("texto_original")
            if conteudo_original is None:
                conteudo_original = widget.text()
                widget.setProperty("texto_original", conteudo_original)
            
            if not conteudo_original:
                return

            # 2. Obter o texto PURO para usar as posições (Ex: "ESTOQUE")
            doc = QTextDocument()
            doc.setHtml(conteudo_original)
            texto_visivel = doc.toPlainText()

            if pos + length > len(texto_visivel):
                return

            # 3. Localizar o trecho (o texto em si, Ex: o 'E' na posição 0 ou 6)
            trecho = texto_visivel[pos:pos+length]
        

            # Cria um novo documento (ou reusa o doc anterior)
            doc_destaque = QTextDocument()
            doc_destaque.setHtml(conteudo_original)

            font = widget.font()
            color = widget.palette().color(QPalette.WindowText) # Pega a cor do texto
            color_name = color.name(QColor.HexRgb) # Converte para ex: "#ffffff"

            # 2. Define a fonte padrão para o documento
            doc_destaque.setDefaultFont(font)
            
            #    FORÇA a cor do texto que lemos da paleta.
            #    Isso preserva a cor do QSS.
            styled_html = f"<div style='color: {color_name};'>{conteudo_original}</div>"
            
            # 4. Define o HTML no documento
            doc_destaque.setHtml(styled_html)
            
            cursor = QTextCursor(doc_destaque)
            
            # Move o cursor para a posição de início do texto plano
            # O QTCursor trabalha com o texto plano, o que é perfeito para as posições `pos` e `length`
            cursor.movePosition(QTextCursor.Start)
            cursor.movePosition(QTextCursor.Right, QTextCursor.MoveAnchor, pos)
            cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor, length)

            # 4. Define o formato de caractere para o destaque
            char_format = QTextCharFormat(cursor.charFormat())
            char_format.setBackground(QColor(cor)) # A cor já vem como string rgba, mas aqui precisamos de QColor

            # Converte a string rgba (ex: "rgba(80, 150, 255, 0.4)") para QColor
            m = re.match(r'rgba\((\d+),\s*(\d+),\s*(\d+),\s*(\d+(\.\d+)?)\)', cor)
            if m:
                r, g, b, a_str = m.groups()[0:4]
                a = int(float(a_str) * 255) # Converte 0.4 para 100
                highlight_color = QColor(int(r), int(g), int(b), a)
                char_format.setBackground(highlight_color)
            else:
                # Fallback caso a regex falhe, para garantir que algo funcione
                char_format.setBackground(QColor(80, 150, 255, 100)) # Exemplo de cor com transparência (0-255)

            # Aplica o formato SÓ na seleção
            cursor.mergeCharFormat(char_format)
            
            # 5. Aplicar o novo HTML gerado (que contém o estilo original + o destaque)
            widget.setTextFormat(Qt.RichText)
            widget.setText(doc_destaque.toHtml()) # <--- Usa toHtml() do documento com destaque

            # 6. Salvar e rolar
            self.ultimo_label_destacado = widget
            self.rolar_para_widget(widget)
            return


        # --- QTextEdit ---
        elif tipo == "textedit":
            edit = resultado["widget"]
            cursor = edit.textCursor()
            cursor.setPosition(resultado["pos"])
            cursor.movePosition(cursor.Right, cursor.KeepAnchor, resultado["len"])
            edit.setTextCursor(cursor)
            self.rolar_para_widget(edit)
            return


        
    def proximo_resultado(self):
        if not self.resultados_encontrados:
            return

        self.indice_atual = (self.indice_atual + 1) % len(self.resultados_encontrados)
        self.navegar_para_resultado(self.indice_atual)
            
    def anterior_resultado(self):
        if not self.resultados_encontrados:
            return
        
        self.indice_atual = (self.indice_atual - 1) % len(self.resultados_encontrados)
        self.navegar_para_resultado(self.indice_atual)
        
    def rolar_para_widget(self, widget):
        """Tenta rolar a página até o widget visível."""
        # Pega o widget pai com barra de rolagem (QScrollArea, QAbstractScrollArea, etc)
        area = widget.parent()
        while area and not isinstance(area, (QAbstractScrollArea, QScrollArea)):
            area = area.parent()

        if area and hasattr(area, "ensureWidgetVisible"):
            area.ensureWidgetVisible(widget)
        elif area and hasattr(area, "verticalScrollBar"):
            # fallback genérico: rola o máximo possível até o widget
            y = widget.mapTo(area.viewport(), widget.rect().topLeft()).y()
            area.verticalScrollBar().setValue(y)
            
    def resetar_destaques_tabelas(self):
        pagina_atual = self.main_window.paginas_sistemas.currentWidget()
        if pagina_atual:
            tabelas = pagina_atual.findChildren(QTableWidget)
            for tabela in tabelas:
                # Reseta o delegate da tabela para o padrão
                tabela.setItemDelegate(QStyledItemDelegate(tabela))
                tabela.viewport().update() # Força a repintura

                # Limpa estilos de cabeçalho
                tabela.horizontalHeader().setStyleSheet("")
                tabela.verticalHeader().setStyleSheet("")
        
    def navegar_para_resultado(self, indice):
        """Vai até o resultado encontrado e aplica o destaque apropriado."""
        pagina_atual = self.main_window.paginas_sistemas.currentWidget()

        # ✅ Limpa os destaques anteriores antes de aplicar o novo
        #self.resetar_destaques(pagina_atual)

        item = self.resultados_encontrados[indice]
        self.main_window.label_contagem.setText(f"{self.indice_atual + 1} de {len(self.resultados_encontrados)}")

        # Habilita botões de navegação
        self.main_window.btn_proximo.setEnabled(True)
        self.main_window.btn_anterior.setEnabled(True)

        # Destaca o resultado
        self.destacar_resultado_atual(item)


    def procurar_widget(self, widget, texto, case_sensitive=False):
        """Percorre todos os widgets dentro da página atual e procura o texto"""
        encontrado = False  # Reinicia o status de 'encontrado' para esta tabela

        self.resetar_destaques(widget)  # Limpa destaques anteriores

        # === QLabel ===
        if isinstance(widget, QLabel):
            conteudo = widget.text()

            if widget.pixmap() is not None and not conteudo:
                return False  # Ignora QLabel que exibe imagem

            # Armazena o HTML original (com formatação)
            if widget.property("texto_original") is None:
                widget.setProperty("texto_original", conteudo)
            else:
                conteudo = widget.property("texto_original")

            doc = QTextDocument()
            doc.setHtml(conteudo)
            texto_visivel = doc.toPlainText()

            if not case_sensitive:
                texto_base = texto_visivel.lower()
                texto_procura = texto.lower()
            else:
                texto_base = texto_visivel
                texto_procura = texto

            pos = texto_base.find(texto_procura)
            if pos != -1:
                # Aplica destaque com QTextCursor
                doc_destaque = QTextDocument()
                doc_destaque.setHtml(conteudo)

                cursor = QTextCursor(doc_destaque)
                cursor.movePosition(QTextCursor.Start)
                cursor.movePosition(QTextCursor.Right, QTextCursor.MoveAnchor, pos)
                cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor, len(texto_procura))

                # Formato do destaque
                cor = self.cor_destaque_html()
                char_format = QTextCharFormat(cursor.charFormat())

                # Converte rgba → QColor
                m = re.match(r'rgba\((\d+),\s*(\d+),\s*(\d+),\s*(\d+(\.\d+)?)\)', cor)
                if m:
                    r, g, b, a_str = m.groups()[0:4]
                    a = int(float(a_str) * 255)
                    highlight_color = QColor(int(r), int(g), int(b), a)
                    char_format.setBackground(highlight_color)
                else:
                    char_format.setBackground(QColor(80, 150, 255, 100))

                cursor.mergeCharFormat(char_format)

                # Aplica o texto com destaque mantendo o HTML original
                widget.setTextFormat(Qt.RichText)
                widget.setText(doc_destaque.toHtml())
                encontrado = True
            else:
                texto_original = widget.property("texto_original")
                if texto_original:
                    widget.setText(texto_original)

        # === QTableWidget ===
        elif isinstance(widget, QTableWidget):
            delegate = CustomTableDelegate(texto_procura=texto, case_sensitive=case_sensitive, parent=widget)
            widget.setItemDelegate(delegate)

            for row in range(widget.rowCount()):
                for col in range(widget.columnCount()):
                    item = widget.item(row, col)
                    if item:
                        item_texto = item.text()
                        item_texto_cmp = item_texto if case_sensitive else item_texto.lower()
                        texto_cmp = texto if case_sensitive else texto.lower()

                        if texto_cmp in item_texto_cmp:
                            encontrado = True
                            widget.scrollToItem(item, QAbstractItemView.EnsureVisible)
                            widget.clearSelection()
                            break
                if encontrado:
                    break

        # === Recursão ===
        for tipo in (QLabel, QTextEdit, QTableWidget):
            for child in widget.findChildren(tipo):
                if self.procurar_widget(child, texto, case_sensitive):
                    encontrado = True

        return encontrado

    
    def resetar_destaques(self, widget):
        """Limpa todos os destaques de todos os widgets recursivamente."""
        
        # Se o widget for uma tabela, reseta o delegate
        if isinstance(widget, QTableWidget):
            widget.setItemDelegate(QStyledItemDelegate(widget))
            widget.viewport().update() # Força a repintura para remover o destaque
            
        # Se for uma Label, restaura o texto original
        elif isinstance(widget, QLabel):
            texto_original = widget.property("texto_original")
            if texto_original is not None:
                widget.setText(texto_original)
                widget.setProperty("texto_original", None)
                
        # Remove estilos de widgets que os tenham
        elif isinstance(widget, (QTextEdit, QPushButton)):
            widget.setStyleSheet("")

        # Recursivamente percorre os filhos para fazer a mesma limpeza
        for child in widget.findChildren(QWidget):
            self.resetar_destaques(child)

    def fechar_pesquisa(self):
        """Fecha a barra de pesquisa e limpa todos os destaques"""
        # Zera estado da pesquisa
        self.resultados_encontrados = []
        self.indice_atual = -1
        self.main_window.label_contagem.setText("")
        self.main_window.btn_proximo.setEnabled(False)
        self.main_window.btn_anterior.setEnabled(False)
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

class CustomTableDelegate(QStyledItemDelegate):
    # 1. MUDANÇA: Substituímos 'item_para_destaque' por 'resultado_para_destaque'
    def __init__(self, texto_procura="", case_sensitive=False, resultado_para_destaque=None, tema="claro", parent=None):
        super().__init__(parent)
        self.texto_procura = texto_procura
        self.case_sensitive = case_sensitive
        # Armazena o dicionário de resultado completo (com 'widget', 'pos', 'len')
        self.resultado_para_destaque = resultado_para_destaque 
        self.tema = tema

    def paint(self, painter: QPainter, option: QStyleOptionViewItem, index):
        item_text = index.data(Qt.DisplayRole) or ""

        # Desenha o fundo e a borda da célula normalmente
        super().paint(painter, option, index)

        # 1. Verifica se esta célula deve ser destacada (e se temos dados de posição)
        item = option.widget.item(index.row(), index.column())
        
        # Obtemos o item (widget) que armazena a ocorrência e verificamos se corresponde ao item atual
        item_para_destaque = self.resultado_para_destaque.get("widget") if self.resultado_para_destaque else None
        
        if item != item_para_destaque:
            return

        # 2. Obtemos a posição EXATA do destaque a partir dos dados armazenados
        # O código original usava match.start(), que sempre encontrava a primeira ocorrência.
        # Agora usamos a posição armazenada na lista self.resultados_encontrados.
        start_pos = self.resultado_para_destaque.get("pos", -1)
        length = self.resultado_para_destaque.get("len", 0)

        if start_pos == -1 or length == 0:
            return

        # Define a cor do destaque baseada no tema
        if self.tema == "escuro":
            # Usamos QColor com componente alpha (0-255)
            highlight_color = QColor(80, 150, 255, 100)
        elif self.tema == "clássico":
            highlight_color = QColor(50, 150, 250, 100)
        else:  # claro
            highlight_color = QColor(50, 100, 200, 100)

        painter.save()
        painter.setPen(Qt.NoPen)
        painter.setBrush(highlight_color)

        # 3. Calcula as dimensões do texto usando a posição exata (start_pos)
        font_metrics = QFontMetrics(option.font)
        
        # Utilizamos start_pos e length diretamente
        matched_text = item_text[start_pos : start_pos + length]
        
        # Use o alinhamento da célula para calcular a posição correta
        alignment = index.data(Qt.TextAlignmentRole) or Qt.AlignLeft | Qt.AlignVCenter

        # Cálculo da largura do texto antes do destaque
        text_width_before = font_metrics.horizontalAdvance(item_text[:start_pos])
        matched_width = font_metrics.horizontalAdvance(matched_text)
        full_text_width = font_metrics.horizontalAdvance(item_text)

        # A base do alinhamento é a posição do retangulo da célula
        text_rect = option.rect
        base_x = text_rect.x()

        if alignment & Qt.AlignHCenter:
            base_x += (text_rect.width() - full_text_width) / 2
        elif alignment & Qt.AlignRight:
            base_x += text_rect.width() - full_text_width
            
        # Corrigindo para garantir que os valores sejam inteiros ao construir o QRect
        highlight_rect = QRect(
            int(base_x + text_width_before),
            text_rect.y(),
            int(matched_width),
            text_rect.height()
        )

        # Desenha o retângulo de destaque
        painter.drawRect(highlight_rect)
        painter.restore()


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






            

        