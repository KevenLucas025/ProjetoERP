from PySide6.QtWidgets import QWidget, QMessageBox
from ui_login_2 import Ui_Login
from database import DataBase
import sys
from PySide6.QtCore import Qt
from configuracoes import Configuracoes_Login
from PySide6.QtCore import Signal




class Login(QWidget, Ui_Login):
    def __init__(self,login_window=None):
        super(Login, self).__init__()
        self.tentativas = 0
        self.config = Configuracoes_Login(self)
        self.config.carregar()
        login_sucesso = Signal()
        self.setupUi(self)
        
        self.users = DataBase()  # Defina self.users aqui
        
        self.setWindowTitle("Login do Sistema")
        self.btn_login.clicked.connect(self.checkLogin)
        
        if self.config.mantem_conectado:
            self.txt_usuario.setText(self.config.usuario)
            self.btn_manter_conectado.setChecked(True)

        self.login_window = login_window

        self.label_trocar_senha.linkActivated.connect(self.exibir_janela_trocar_senha)
#*********************************************************************************************************************
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
#*********************************************************************************************************************
    def checkLogin(self):
        if not self.txt_usuario.text() or not self.txt_senha.text():
            self.mostrarMensagem("ERRO", "Por favor, insira o nome de usuário e senha", QMessageBox.Warning)
            return
        
        self.users = DataBase()
        self.users.connecta()
        
        usuario = self.txt_usuario.text()
        senha = self.txt_senha.text()
        
        tipo_usuario = self.users.check_user(usuario, senha)
        print("Tipo de usuário:", tipo_usuario)
        
        self.users.close_connection()
        
        if tipo_usuario:
            if self.btn_manter_conectado.isChecked():
                self.config.salvar_configuracoes(usuario, True)
            else:
                self.config.salvar_configuracoes("", False)

            print("Login bem sucedido!")
            from main import MainWindowNormal
            self.w = MainWindowNormal(tipo_usuario.lower(), self)
            self.w.show()  # Mostrar a janela principal
            
            # Fechar a janela de login
            self.close()
        else:
            self.tentativas += 1
            if self.tentativas < 3:
                self.mostrarMensagem("Erro ao acessar", f"Login ou senha incorretos \n\nTentativa: {self.tentativas} de 3", QMessageBox.Warning)
            elif self.tentativas == 3:
                self.mostrarMensagem("Erro ao acessar", "Número máximo de tentativas excedido. O aplicativo será encerrado.", QMessageBox.Critical)
                sys.exit()
#*********************************************************************************************************************
    def fazerLoginAutomatico(self):
        # Método para fazer login automaticamente
        usuario = self.config.usuario
        senha = ""  # Você pode armazenar a senha criptografada nas configurações e recuperá-la aqui
        tipo_usuario = self.users.check_user(usuario, senha)
        if tipo_usuario:
            print("Login automático bem sucedido!")
            from main import MainWindow
            self.w = MainWindow(tipo_usuario.lower(), self)
            self.w.show()
            
            # Fechar a janela de login
            self.close()
        else:
            print("Falha no login automático. As credenciais podem ter sido alteradas.")
            self.mostrarMensagem("Erro", "Falha no login automático. As credenciais podem ter sido alteradas.", QMessageBox.Warning)
#*********************************************************************************************************************
    def mostrarMensagem(self, titulo, mensagem, icone):
        msg = QMessageBox()
        msg.setIcon(icone)
        msg.setWindowTitle(titulo)
        msg.setText(mensagem)
        msg.exec_()
#*********************************************************************************************************************   
    def setLoginWindow(self, login_window):
        self.login_window = login_window
#*********************************************************************************************************************
    def check_user(self, usuario, senha, connection):
        try: 
            print("Usuário fornecido:", usuario)
            print("Senha fornecida:", senha)   
            query = "SELECT Senha FROM users WHERE Usuário = ? AND Senha = ? COLLATE NOCASE"
            cursor = connection.cursor()
            cursor.execute(query, (usuario, senha))
            result = cursor.fetchone()
            print("Resultado da consulta:", result)
            if result:
                print("Usuário autenticado com sucesso")
                return result[0]
            else:
                return ""
        except Exception as e:
            print("Erro ao verificar usuário:", e)
            return ""
#*********************************************************************************************************************    
    def closeEvent(self, event):
        print("Fechando janela de login...")
        if hasattr(self, 'users'):
            self.users.close_connection()
#*********************************************************************************************************************
    def limpar_campos(self):
        # Limpar os campos de login e senha
        self.txt_usuario.clear()
        self.txt_senha.clear()

