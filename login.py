from PySide6.QtWidgets import (
    QWidget, QMessageBox,QApplication, QDialog, 
    QVBoxLayout, QLabel, QPushButton,QMainWindow,QLabel,QLineEdit,QComboBox,
    QHBoxLayout,QMenu,QToolButton)
from ui_login_4 import Ui_Mainwindow_Login
from database import DataBase
import sys
from PySide6.QtCore import Qt,QTimer
from configuracoes import Configuracoes_Login
from utils import Temas
from PySide6.QtCore import Signal
from PySide6 import QtCore
from PySide6.QtGui import QPixmap,QAction
import pyotp
import qrcode
import os
import sqlite3
from datetime import datetime
import subprocess



class Login(QMainWindow, Ui_Mainwindow_Login):  
    def __init__(self, login_window=None):
        super(Login, self).__init__() 
        self.tentativas = 0
        self.config = Configuracoes_Login(self)
        self.config.carregar()   
        self.setupUi(self)
        self.login_window = login_window
        self.users = DataBase()  # Defina self.users aqui
        self.users.connecta()    # <-- Conecta ao banco de dados
        self.setWindowTitle("Login do Sistema")
        self.tema = Temas()

        self.menu_btn_opcoes_extras = QMenu(self.btn_opcoes_extras)
        self.btn_opcoes_extras.setMenu(self.menu_btn_opcoes_extras)
        self.btn_opcoes_extras.setPopupMode(QToolButton.InstantPopup)
        self.btn_opcoes_extras.setToolButtonStyle(Qt.ToolButtonIconOnly)
        
        
        self.acao_reiniciar_sistema = QAction("Reiniciar sistema",self)
        self.acao_primeiro_acesso = QAction("Primeiro acesso",self)
        
        self.menu_btn_opcoes_extras.addAction(self.acao_reiniciar_sistema)
        self.menu_btn_opcoes_extras.addAction(self.acao_primeiro_acesso)

        self.acao_reiniciar_sistema.triggered.connect(self.reiniciar_sistema_tela_login)
        self.acao_primeiro_acesso.triggered.connect(self.abrir_janela_primeiro_acesso)
        
        self.btn_login.clicked.connect(self.checkLogin)

        
        if self.config.mantem_conectado:
            self.txt_usuario.setText(self.config.usuario)
            self.btn_manter_conectado.setChecked(True)

        

        self.label_trocar_senha.linkActivated.connect(self.exibir_janela_trocar_senha)
    
    def abrir_janela_primeiro_acesso(self):
        # Criar e abrir a janela de cadastro
        cadastro_dialog = PrimeiroAcesso(self)
        cadastro_dialog.show()

    def exibir_janela_trocar_senha(self):
        from config_senha import TrocarSenha 
        trocar_senha_dialog = TrocarSenha()
        trocar_senha_dialog.exec()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            # Desativa o botão para evitar múltiplos cliques ou pressionamentos rápidos
            if not self.btn_login.isEnabled():
                return
            # Desativa o botão de login para evitar múltiplos cliques rápidos
            self.btn_login.setEnabled(False)
            
            # Chama o método de login
            self.checkLogin()
            
            # Reativa o botão depois de 2 segundo (ou o tempo necessário)
            QTimer.singleShot(2000, lambda: self.btn_login.setEnabled(True))
            
            return
        else:
            super().keyPressEvent(event)


    def checkLogin(self):
        if hasattr(self, "autenticando") and self.autenticando:
            return
        
        self.autenticacao = True
        self.users = DataBase()
        self.users.connecta()

        usuario_ou_email = self.txt_usuario.text()
        senha = self.txt_senha.text()

        tipo_usuario = self.users.check_user(usuario_ou_email, senha)

        if tipo_usuario:
            manter_conectado = self.btn_manter_conectado.isChecked()
            self.config.salvar_configuracoes(usuario_ou_email,senha, manter_conectado)
            print(f"Usuário salvo: {self.config.usuario}")  # DEBUG
            print(f"Senha salva: {self.config.senha}") # DEBUG

            self.config.carregar()
            self.hide()

        else:
            self.mostrarMensagem(f"Erro", f"Login ou senha incorretos.\nTentativa {self.tentativas + 1} de 3", QMessageBox.Warning)
            self.users.close_connection()
            self.tentativas += 1
            if self.tentativas >= 3:
                self.mostrarMensagem("Erro", "Número máximo de tentativas excedido.\n O sistema será encerrado, se o erro persistir entre em contato com seu administrador", QMessageBox.Critical)
                #self.abrir_janela_primeiro_acesso()
                sys.exit()
            return


        self.btn_login.setEnabled(True)   # Reativa o botão após o processo

        # Se autenticado com sucesso, abre a tela principal
        print("Login bem-sucedido!")
        from main import MainWindow
        self.w = MainWindow(tipo_usuario.lower(), self)
        self.w.show()
        self.tentativas = 0
        QTimer.singleShot(2000,self.w.boas_vindas)
        QTimer.singleShot(3000, self.w.verificar_atualizacao_automatica)



    def verificar_codigo_totp(self, secret, codigo):
        totp = pyotp.TOTP(secret)
        print("Código gerado pelo TOTP:", totp.now())  # Exibe o código gerado para depuração
        return totp.verify(codigo)

    def abrir_janela_configuracao_2fa(self, usuario):

        # Criando uma janela de configuração de 2FA
        dialog = QDialog(self)
        dialog.setWindowTitle("Configurar Autenticação de Dois Fatores (2FA)")

        layout = QVBoxLayout(dialog)

        # Gerar o Secret para o usuário
        secret = pyotp.random_base32()  # Gerar uma chave secreta Base32
        totp = pyotp.TOTP(secret)
        email = self.users.get_user_email(usuario)  # Pegar o email cadastrado no banco de dados
        otpauth_url = totp.provisioning_uri(name=email, issuer_name="Sistema de Gerenciamento")


        # Gerar o QR code para o usuário escanear
        qr = qrcode.make(otpauth_url)
        qr_image_path = f"{usuario}_qrcode.png"
        qr.save(qr_image_path)

        # Exibir QR Code para o usuário
        qr_label = QLabel(dialog)
        pixmap = QPixmap(qr_image_path)
        qr_label.setPixmap(pixmap)
        layout.addWidget(qr_label)

        # Botão para confirmar
        confirmar_button = QPushButton("Confirmar", dialog)
        confirmar_button.clicked.connect(lambda: self.confirmar_2fa_config(usuario, secret, dialog))
        layout.addWidget(confirmar_button)

        dialog.setLayout(layout)
        dialog.exec()

    def confirmar_2fa_config(self, usuario, secret, dialog):
        # Salvar o Secret no banco de dados
        self.users = DataBase()
        self.users.connecta()
        try:
            query = "UPDATE users SET Secret = ? WHERE Usuário = ?"
            cursor = self.users.connection.cursor()
            cursor.execute(query, (secret, usuario))
            self.users.connection.commit()
            print("2FA configurado com sucesso para o usuário:", usuario)
        except Exception as e:
            print("Erro ao configurar 2FA:", e)

        # Fechar a janela
        dialog.accept()
        self.mostrarMensagem("Sucesso", "Autenticação de dois fatores (2FA) configurada com sucesso!", QMessageBox.Information)

    def update_user_secret(self, usuario, secret):
        try:
            self.users.connecta()  # Certifique-se de que o banco está conectado
            query = "UPDATE users SET Secret = ? WHERE Usuário = ?"
            cursor = self.users.connection.cursor()
            cursor.execute(query, (secret, usuario))
            self.users.connection.commit()
            print("Chave secreta atualizada com sucesso!")
        except Exception as e:
            print("Erro ao atualizar o segredo do usuário:", e)
        finally:
            self.users.close_connection()  # Fechar a conexão após o uso

    def fazerLoginAutomatico(self):
        if not self.config.mantem_conectado:
            return

        usuario = self.config.usuario
        senha = self.config.senha  # Se você optar por continuar salvando a senha

        if not (usuario and senha):
            return

        tipo_usuario = self.users.check_user(usuario, senha)
        if tipo_usuario:
            print("Login automático bem-sucedido!")
            from main import MainWindow
            self.w = MainWindow(tipo_usuario.lower(), self)
            self.w.show()
            self.close()
        else:
            print("Falha no login automático.")
            self.mostrarMensagem("Erro", "Não foi possível autenticar automaticamente.", QMessageBox.Warning)


    def closeEvent(self, event):
        # Garantir que o banco de dados seja fechado corretamente
        if hasattr(self, 'users'):
            self.users.close_connection()

        # Apagar configurações do usuário ao sair
        self.config.usuario = None
        self.config.salvar_configuracoes(None,"", False)  # Garantir que não está armazenando sessão

    def limpar_campos(self):
        # Limpar os campos de login e senha
        self.txt_usuario.clear()
        self.txt_senha.clear()

    def usuario_logado(self):
        print(f"Função usuario_logado(): {self.config.usuario}")
        return self.config.usuario if self.config.usuario else None

    def carregar_configuracoes(self):
        # Carregar configurações do arquivo config.json
        self.config.carregar()
        print(f"Usuário carregado: {self.config.usuario}")
        # Atualizar os campos de login com as configurações carregadas
        self.txt_usuario.setText(self.config.usuario)
        self.btn_manter_conectado.setChecked(self.config.mantem_conectado)
        

    def mostrarMensagem(self, titulo, mensagem, icone):
        msg = QMessageBox(self)
        msg.setIcon(icone)
        msg.setWindowTitle(titulo)
        msg.setText(mensagem)
        msg.exec()

    def reiniciar_sistema_tela_login(self):
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Reiniciar Sistema")
            msg_box.setText("Tem certeza que deseja reiniciar o sistema? ")
            msg_box.setIcon(QMessageBox.Question)

            botao_sim = msg_box.addButton("Sim",QMessageBox.YesRole)
            botao_nao = msg_box.addButton("Não",QMessageBox.NoRole)
            msg_box.setDefaultButton(botao_nao) # Define "Não" como o botão padrão

            msg_box.exec()

            if msg_box.clickedButton() == botao_sim:
                python = sys.executable
                script = os.path.abspath(sys.argv[0])
                # Fecha o app atual
                QApplication.quit()
                # Reinicia com subprocess (mais robusto para caminhos com espaço)
                subprocess.Popen([python, script] + sys.argv[1:])
                sys.exit()

class PrimeiroAcesso(QMainWindow):  
    def __init__(self, parent=None):
        super(PrimeiroAcesso, self).__init__(parent)
        self.setWindowTitle("Primeiro Acesso")
        self.tema = Temas()
        self.users = DataBase()  # Defina self.users aqui
        self.users.connecta()    # <-- Conecta ao banco de dados
        
        self.setMinimumWidth(400)
        self.setMinimumHeight(400)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout(self.central_widget)

        # Carregar tema
        config = self.tema.carregar_config_arquivo()
        tema = config.get("tema", "claro")

        if tema == "escuro":
            bg_cor = "#202124"
            text_cor = "white"
            lineedit_bg = "#303030"

            button_style = """
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
            """

            lineedit_style = """
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
        elif tema == "claro":
            bg_cor = "white"
            text_cor = "black"
            lineedit_bg = "white"

            button_style = """
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
            
            """

            lineedit_style = """
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
        else: #clássico
            bg_cor = "rgb(0,80,121)"
            text_cor = "white"
            lineedit_bg = "white"

            button_style = """
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
            
            """

            lineedit_style = """
                QLineEdit {
                color: black;
                background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */
                border: 3px solid rgb(50, 150,250); /* Borda azul */
                border-radius: 12px; /* Cantos arredondados */
                padding: 3px; /* Espaçamento interno */
            }

            QLineEdit::placeholderText {
                color: black; /* Cor do texto do placeholder */
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
            
         # Nome
        hbox_nome = QHBoxLayout()
        self.label_nome = QLabel("Nome: ")
        self.txt_nome = QLineEdit()
        self.txt_nome.setStyleSheet(lineedit_style)
        hbox_nome.addWidget(self.label_nome)
        hbox_nome.addWidget(self.txt_nome)
        self.layout.addLayout(hbox_nome)

        # Usuário
        hbox_usuario = QHBoxLayout()
        self.label_usuario = QLabel("Usuário: ")
        self.txt_usuario = QLineEdit()
        self.txt_usuario.setStyleSheet(lineedit_style)
        hbox_usuario.addWidget(self.label_usuario)
        hbox_usuario.addWidget(self.txt_usuario)
        self.layout.addLayout(hbox_usuario)

        # Senha
        hbox_senha = QHBoxLayout()
        self.label_senha = QLabel("Senha: ")
        self.txt_senha = QLineEdit()
        self.txt_senha.setStyleSheet(lineedit_style)
        self.txt_senha.setEchoMode(QLineEdit.Password)  # Ocultar senha
        hbox_senha.addWidget(self.label_senha)
        hbox_senha.addWidget(self.txt_senha)
        self.layout.addLayout(hbox_senha)


         # Confirmar Senha
        hbox_confirmar_senha = QHBoxLayout()
        self.label_confirmar_senha = QLabel("Confirmar senha: ")
        self.txt_confirmar_senha = QLineEdit()
        self.txt_confirmar_senha.setEchoMode(QLineEdit.Password)
        self.txt_confirmar_senha.setStyleSheet(lineedit_style)
        hbox_confirmar_senha.addWidget(self.label_confirmar_senha)
        hbox_confirmar_senha.addWidget(self.txt_confirmar_senha)
        self.layout.addLayout(hbox_confirmar_senha)
        
        # ComboBox de Acesso
        hbox_acesso = QHBoxLayout()
        self.label_acesso = QLabel("Tipo de acesso: ")
        hbox_acesso.addWidget(self.label_acesso)
        self.combobox_acesso = QComboBox()
        self.combobox_acesso.addItem("Convidado")
        self.combobox_acesso.addItem("Administrador")
        self.combobox_acesso.addItem("Usuário")
        self.combobox_acesso.setStyleSheet(combobox_style)
        hbox_acesso.addWidget(self.combobox_acesso)
        self.layout.addLayout(hbox_acesso)


        self.btn_cadastrar = QPushButton("Realizar cadastro")
        self.btn_cadastrar.setStyleSheet(button_style)
        self.btn_cadastrar.clicked.connect(self.inserir_usuario_no_banco_de_dados)
        self.layout.addWidget(self.btn_cadastrar)

        # Exibir a mensagem assim que a janela de primeiro acesso for exibida
        QMessageBox.information(self,
            "Informação",
            "O usuário será cadastrado com  informações temporárias\n"
            "assim que logado no sistema, ir em Cadastrar Usuário e incluir/alterar todas as informações necessárias. ",
        )
        
    def inserir_usuario_no_banco_de_dados(self):   
        # Realizar as verificações de campos
        nome = self.txt_nome.text()
        usuario = self.txt_usuario.text()
        senha = self.txt_senha.text()
        confirmar_senha = self.txt_confirmar_senha.text()
        acesso = self.combobox_acesso.currentText()
        data_atual = datetime.now().strftime("%d/%m/%Y %H:%M")
        segredo = "Não Cadastrado"
        usuario_logado = "Primeiro Acesso"
        data_ultima_troca = "Não Cadastrado"

        # Verificar se os campos obrigatórios estão preenchidos
        if not (nome and usuario and senha and confirmar_senha):
            QMessageBox.warning(self,"Erro", "Por favor, preencha todos os campos.")
            return

        # Verificar se as senhas coincidem
        if senha != confirmar_senha:
            QMessageBox.warning(self,"Erro", "As senhas não coincidem.")
            return

        if self.combobox_acesso.currentText() == "Administrador":
            QMessageBox.warning(self,
                "Erro",
                "Para primeiro acesso o usuário pode ser cadastrado somente como Convidado ou Usuário comum.\n" 
                "O tipo de acesso para usuário administrador só pode ser realizado por outro administrador.\n"
                "Por favor, entre em contato com seu administrador para revogar seu privilégio.\n"
                "Se o erro persistir, entre em contato com o desenvolvedor do sistema.",        
            )
            return

        # Conectar ao banco de dados e inserir os dados
        try:
            with self.users.connection as cn:
                cursor = cn.cursor()

                # Verificar se o usuário já existe
                cursor.execute("SELECT * FROM users WHERE Usuário = ?", (usuario,))
                existing_user = cursor.fetchone()
                if existing_user:
                    QMessageBox.warning(self,"Erro", "Já existe um usuário cadastrado no sistema! ")
                    return

                # Inserir o novo usuário no banco de dados
                cursor.execute("""
                        INSERT INTO users(
                            Nome, Usuário, Senha, "Confirmar Senha",Acesso,
                            "Última Troca de Senha","Data da Senha Cadastrada",
                            "Data da Inclusão do Usuário",Segredo, "Usuário Logado"
                        )
                        VALUES (?,?,?,?,?,?,?,?,?,?)
                """,(nome, usuario,senha,confirmar_senha,acesso,data_ultima_troca,
                    data_atual,data_atual,segredo,usuario_logado))
                cn.commit()
                

                # Mensagem de sucesso
                QMessageBox.information(self,"Sucesso", "Usuário cadastrado com sucesso!")
                self.close()  # Fecha a janela de cadastro

        except sqlite3.Error as e:
            print(f"Erro ao salvar o usuário: {e}")
   
        
    def esconder_label_acesso(self):
        pass

    