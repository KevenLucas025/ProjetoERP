import msal
from msal import ConfidentialClientApplication,PublicClientApplication
from PySide6.QtWidgets import QWidget, QMessageBox, QInputDialog, QDialog, QVBoxLayout, QLabel, QPushButton,QMainWindow
from ui_login_3 import Ui_Mainwindow_Login
from database import DataBase
import sys
from PySide6.QtCore import Qt,QTimer
from configuracoes import Configuracoes_Login
from PySide6.QtCore import Signal
from PySide6 import QtCore  
from PySide6.QtGui import QPixmap
import pyotp
import qrcode
import urllib3
import ssl
import requests
import os
import webbrowser

class Login(QMainWindow, Ui_Mainwindow_Login):  # Altere QWidget para QMainWindow
    def __init__(self, login_window=None):
        super(Login, self).__init__()  # Mantenha a chamada ao super() com QMainWindow
        self.tentativas = 0
        self.config = Configuracoes_Login(self)
        self.config.carregar()
        login_sucesso = Signal()
        self.setupUi(self)
        
        self.users = DataBase()  # Defina self.users aqui

        
        

        
        # Desabilitar a verificação SSL
        '''ssl._create_default_https_context = ssl._create_unverified_context
        requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)'''
        
        self.setWindowTitle("Login do Sistema")
        self.btn_login.clicked.connect(self.checkLogin)
        
        if self.config.mantem_conectado:
            self.txt_usuario.setText(self.config.usuario)
            self.btn_manter_conectado.setChecked(True)


        self.login_window = login_window

        self.label_trocar_senha.linkActivated.connect(self.exibir_janela_trocar_senha)

    def exibir_janela_trocar_senha(self):
        from config_senha import TrocarSenha 
        trocar_senha_dialog = TrocarSenha()
        trocar_senha_dialog.exec()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.checkLogin()
            return
        else:
            super().keyPressEvent(event)

    def checkLogin(self):
        if hasattr(self, "autenticando") and self.autenticando:
            print("Autenticação já em andamento. Aguardando...")
            return
        
        self.autenticacao = True
        self.users = DataBase()
        self.users.connecta()

        usuario_ou_email = self.txt_usuario.text()
        senha = self.txt_senha.text()

        tipo_usuario = self.users.check_user(usuario_ou_email, senha)

        if tipo_usuario:
            manter_conectado = self.btn_manter_conectado.isChecked()
            self.config.salvar_configuracoes(usuario_ou_email, manter_conectado)
        else:
            self.mostrarMensagem("Erro", "Login ou senha incorretos", QMessageBox.Warning)
            self.users.close_connection()
            self.tentativas += 1
            if self.tentativas >= 3:
                self.mostrarMensagem("Erro", "Número máximo de tentativas excedido.", QMessageBox.Critical)
                sys.exit()
            return

        # Chamar autenticação via Azure AD com notificação push
        self.btn_login.setEnabled(False)  # Desativa o botão para evitar cliques duplos
        access_token = self.autenticar_com_azure()
        self.btn_login.setEnabled(True)   # Reativa o botão após a autenticação
        self.autenticacao = False


        if not access_token:
            self.mostrarMensagem("Erro", "Falha ao autenticar via Azure AD.", QMessageBox.Warning)
            self.tentativas += 1
            if self.tentativas >= 3:
                self.mostrarMensagem("Erro", "Número máximo de tentativas excedido.", QMessageBox.Critical)
                sys.exit()
            return

        # Se autenticado com sucesso, abre a tela principal
        print("Login bem-sucedido!")
        from main import MainWindow
        self.w = MainWindow(tipo_usuario.lower(), self)
        self.w.show()
        self.close()
        self.tentativas = 0




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
            print("Login automático desativado.")
            return
        
        usuario = self.config.usuario
        if not usuario:
            print("Nenhum usuário salvo para login automático.")
            return

        print(f"Tentando login automático para {usuario}...")

        # Autenticação via Azure AD (forçando autenticação interativa)
        access_token = self.autenticar_com_azure()

        if access_token:
            print("Login automático bem sucedido!")
            from main import MainWindow
            self.w = MainWindow("usuario", self)
            self.w.show()
            self.close()
        else:
            print("Falha no login automático.")
            self.mostrarMensagem("Erro", "Não foi possível autenticar automaticamente.", QMessageBox.Warning)


    def mostrarMensagem(self, titulo, mensagem, icone):
        msg = QMessageBox()
        msg.setIcon(icone)
        msg.setWindowTitle(titulo)
        msg.setText(mensagem)
        msg.exec()

    def setLoginWindow(self, login_window):
        self.login_window = login_window


    def closeEvent(self, event):
        print("Fechando janela de login...")

        # Garantir que o banco de dados seja fechado corretamente
        if hasattr(self, 'users'):
            self.users.close_connection()

        # Apagar configurações do usuário ao sair
        self.config.usuario = None
        self.config.salvar_configuracoes(None, False)  # Garantir que não está armazenando sessão

    def limpar_campos(self):
        # Limpar os campos de login e senha
        self.txt_usuario.clear()
        self.txt_senha.clear()

    def usuario_logado(self):
        return self.config.usuario if self.config.usuario else "Nenhum usuário logado"

    def carregar_configuracoes(self):
        # Carregar configurações do arquivo config.json
        self.config.carregar()
        # Atualizar os campos de login com as configurações carregadas
        self.txt_usuario.setText(self.config.usuario)
        self.btn_manter_conectado.setChecked(self.config.mantem_conectado)
        
            

    def autenticar_com_azure(self):
        CLIENT_ID = "a762a92a-1751-4c32-88db-43d5645cbb19"
        TENANT_ID = "2923a0b2-b49d-488a-a010-519f426261e5"
        SCOPES = ["https://graph.microsoft.com/User.Read"]

        app = PublicClientApplication(
            CLIENT_ID,
            authority=f"https://login.microsoftonline.com/{TENANT_ID}",
        )

        # REMOVER QUALQUER SESSÃO ARMAZENADA NO MSAL
        accounts = app.get_accounts()
        for account in accounts:
            print(f"Removendo sessão armazenada para {account['username']}")
            app.remove_account(account)

        try:
            # FORÇAR SEMPRE A AUTENTICAÇÃO INTERATIVA
            token_result = app.acquire_token_interactive(scopes=SCOPES, prompt="login",login_hint="keven.lucas00_hotmail.com#EXT#@KevenLucas.onmicrosoft.com")

            if "access_token" in token_result:
                print("Autenticação bem-sucedida!")
                return token_result["access_token"]
            else:
                print("Erro ao autenticar:", token_result.get("error_description"))
                return None

        except Exception as e:
            print("Erro durante a autenticação:", e)
            return None




    def mostrarMensagem(self, titulo, mensagem, icone):
        msg = QMessageBox()
        msg.setIcon(icone)
        msg.setWindowTitle(titulo)
        msg.setText(mensagem)
        msg.exec()




        
        

        
        
        