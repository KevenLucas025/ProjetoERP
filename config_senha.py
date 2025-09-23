from PySide6.QtWidgets import (
    QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
)
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from database import DataBase
from datetime import datetime
from utils import Temas
import re


class BotaoAjuda(QHBoxLayout):
    def __init__(self, main_window,label_text="", help_text="", parent=None):
        super().__init__(parent)
        self.main_window = main_window
        self.tema = Temas()



        self.label = QLabel(label_text)
        self.line_edit = QLineEdit()
        self.help_button = QPushButton("?")
        self.help_button.setStyleSheet("border: none; padding: 0px; background: transparent;")
        self.help_button.setCursor(Qt.PointingHandCursor)
        self.help_button.setToolTip(help_text)
        self.help_button.clicked.connect(lambda: self.mostrar_ajuda(help_text))

        self.addWidget(self.label)
        self.addWidget(self.line_edit)
        self.addWidget(self.help_button)

        # Conectar o sinal textChanged ao método formatar_telefone
        self.line_edit.textChanged.connect(self.formatar_telefone)

    def mostrar_ajuda(self, help_text):
        QMessageBox.information(None, "Ajuda", help_text)

        
    
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
                self.line_edit.setText(numero_formatado)
            else:
                # Se o número não tiver mais de 7 dígitos, apenas atualizar o texto
                self.line_edit.setText(numero_formatado + numero_limpo[2:])

class TrocarSenha(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Alterar Senha")
        self.tema = Temas()

        self.db = DataBase()
        self.db.connecta()

        self.usuario_line_edit = BotaoAjuda(
            "Informe seu nome de usuário:", "O usuário informado deve ser o\n mesmo cadastrado no sistema"
        )
        self.email_line_edit = BotaoAjuda(
            "Informe seu e-mail:", "O e-mail informado deve ser o \n mesmo cadastrado no sistema"
        )
        self.telefone_line_edit = BotaoAjuda(
            "Informe seu número de telefone:", "O número de telefone deve ser o \n mesmo cadastrado no sistema"
        )

        config = self.tema.carregar_config_arquivo()
        tema  = config.get("tema","claro")


        if tema == "escuro":
            bg_cor = "#202124"
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
            QPushButton#nova_senha_show_button,
            QPushButton#confirmar_senha_show_button{
                qproperty-icon: url("imagens/olho_branco.png");
                qproperty-iconSize: 16px 16px;
                background: transparent;
                border: none;  
            }
            QPushButton#nova_senha_show_button:hover,
            QPushButton#confirmar_senha_show_button:hover{
                background-color: #444444; 
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
            label_style = """
                QLabel{
                    color: white;
                }
            
            """
        elif tema == "claro":
            bg_cor = "white"
            button_style =  """
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
            QPushButton#nova_senha_show_button,
            QPushButton#confirmar_senha_show_button{
                qproperty-icon: url("imagens/olho_preto.png");
                qproperty-iconSize: 16px 16px;
                background: transparent;
                border: none;  
            }
            QPushButton#nova_senha_show_button:hover,
            QPushButton#confirmar_senha_show_button:hover{
                background-color: #e0e0e0; 
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
            label_style = """
                QLabel{
                    color: black;
                }
            
            """
            
        else: # clássico
            bg_cor = "rgb(0,80,121)"

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
            QPushButton#nova_senha_show_button,
            QPushButton#confirmar_senha_show_button{
                qproperty-icon: url("imagens/olho_preto.png");
                qproperty-iconSize: 16px 16px;
                background: transparent;
                border: none;  
            }
            QPushButton#nova_senha_show_button:hover,
            QPushButton#confirmar_senha_show_button:hover{
                background: qlineargradient(
                x1:0, y1:0, x2:0, y2:1, 
                stop:0 rgb(100, 180, 255), 
                stop:1 rgb(150, 220, 255)
            );
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
            label_style = """
                QLabel{
                    color: white;
                }
            
                """

        estilo_completo = f"""
        QWidget {{
            background-color: {bg_cor};
        }}
        {button_style}
        {lineedit_style}
        {label_style}
        """
        self.setStyleSheet(estilo_completo)


        self.nova_senha_label = QLabel("Nova Senha:")
        self.nova_senha_line_edit = QLineEdit()
        self.nova_senha_line_edit.setEchoMode(QLineEdit.Password)
        self.nova_senha_show_button = QPushButton()
        self.nova_senha_show_button.setObjectName("nova_senha_show_button")

        self.nova_senha_show_button.setCheckable(True)
        self.nova_senha_show_button.setStyleSheet(button_style)
        self.nova_senha_show_button.toggled.connect(
            lambda checked: self.nova_senha_line_edit.setEchoMode(
                QLineEdit.Normal if checked else QLineEdit.Password
            )
        )

        self.confirmar_senha_label = QLabel("Confirmar Nova Senha:")
        self.confirmar_senha_line_edit = QLineEdit()
        self.confirmar_senha_line_edit.setEchoMode(QLineEdit.Password)
        self.confirmar_senha_show_button = QPushButton()
        self.confirmar_senha_show_button.setObjectName("confirmar_senha_show_button")
        self.confirmar_senha_show_button.setCheckable(True)
        
        
        self.confirmar_senha_show_button.toggled.connect(
            lambda checked: self.confirmar_senha_line_edit.setEchoMode(
                QLineEdit.Normal if checked else QLineEdit.Password
            )
        )

        self.atualizar_senha_button = QPushButton("Atualizar Senha")
        self.atualizar_senha_button.clicked.connect(self.trocar_senha)

        layout = QVBoxLayout()
        layout.addLayout(self.usuario_line_edit)
        layout.addLayout(self.email_line_edit)
        layout.addLayout(self.telefone_line_edit)

        nova_senha_layout = QHBoxLayout()
        nova_senha_layout.addWidget(self.nova_senha_label)
        nova_senha_layout.addWidget(self.nova_senha_line_edit)
        nova_senha_layout.addWidget(self.nova_senha_show_button)
        layout.addLayout(nova_senha_layout)

        confirmar_senha_layout = QHBoxLayout()
        confirmar_senha_layout.addWidget(self.confirmar_senha_label)
        confirmar_senha_layout.addWidget(self.confirmar_senha_line_edit)
        confirmar_senha_layout.addWidget(self.confirmar_senha_show_button)
        layout.addLayout(confirmar_senha_layout)

        layout.addWidget(self.atualizar_senha_button)

        self.setLayout(layout)

        


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

    
    def trocar_senha(self):
        usuario = self.usuario_line_edit.line_edit.text()
        email = self.email_line_edit.line_edit.text()
        telefone = self.telefone_line_edit.line_edit.text()
        nova_senha = self.nova_senha_line_edit.text()
        confirmar_nova_senha = self.confirmar_senha_line_edit.text()
        data_atual = datetime.now().strftime("%d/%m/%Y")

        # Verificar se todos os campos estão preenchidos
        if not usuario or not email or not telefone or not nova_senha or not confirmar_nova_senha:
            QMessageBox.warning(self, "Erro", "Por favor, preencha todos os campos.")
            return

        if self.verificar_usuario(usuario):
            dias_passados = self.verificar_tempo_ultima_troca(usuario)
            if not self.verificar_email(email):
                QMessageBox.warning(self, "Erro", "E-mail incorreto, \nPor favor digite o mesmo e-mail cadastrado no sistema.")
                return

            if not self.verificar_telefone(telefone):
                QMessageBox.warning(self, "Erro", "Telefone incorreto. \nPor favor digite o mesmo telefone cadastrado no sistema.")
                return
            if dias_passados is None or dias_passados >= 15:
                if self.atualizar_senha_usuario(usuario, nova_senha, confirmar_nova_senha, data_atual):
                    QMessageBox.information(self, "Sucesso", "Senha atualizada com sucesso.")
                    self.close()
                else:
                    QMessageBox.warning(self, "Erro", "Erro ao atualizar a senha.")
            else:
                QMessageBox.warning(self, "Erro", f"Você só pode trocar a senha a cada 15 dias. \n\t Dias passados: {dias_passados}")
        else:
            QMessageBox.warning(self, "Erro", "Usuário não encontrado.")
        
        


    def atualizar_senha_usuario(self, usuario, nova_senha, confirmar_senha, data_atual):
        if nova_senha != confirmar_senha:
            QMessageBox.warning(self, "Erro", "As senhas não coincidem.")
            return False

        if not self.validar_senha(nova_senha):
            QMessageBox.warning(self, "Erro", "A nova senha deve conter pelo menos um caractere especial e uma letra maiúscula.")
            return False

        senha_atual = self.obter_senha_atual(usuario)
        if nova_senha == senha_atual:
            QMessageBox.warning(self, "Erro", "A nova senha não pode ser a mesma que a senha atual.")
            return False

        query = "UPDATE users SET Senha = ?, 'Confirmar Senha' = ?, 'Última Troca de Senha' = ? WHERE Usuário = ?"
        try:
            cursor = self.db.connection.cursor()
            cursor.execute(query, (nova_senha, confirmar_senha, data_atual, usuario))
            self.db.connection.commit()
            return True
        except Exception as e:
            QMessageBox.warning(self, "Erro", f"Erro ao atualizar a senha: {e}")
            return False


    def verificar_usuario(self, usuario):
        query = "SELECT 1 FROM users WHERE Usuário = ?"
        cursor = self.db.connection.cursor()
        cursor.execute(query, (usuario,))
        return cursor.fetchone() is not None

    

    def registrar_data_ultima_troca(self, usuario):
        try:
            # Obtém a data atual
            data_atual = datetime.now().strftime("%d/%m/%Y")
            
            # Atualiza o banco de dados com a data da última troca de senha
            cursor = self.db.connection.cursor()
            query = "UPDATE users SET 'Última Troca de Senha' = ? WHERE Usuário = ?"
            cursor.execute(query, (data_atual, usuario))
            self.db.connection.commit()
        except Exception as e:
            print(f"Erro ao registrar data da última troca de senha: {e}")



    def verificar_tempo_ultima_troca(self, usuario):
        cursor = self.db.connection.cursor()
        cursor.execute("SELECT \"Última Troca de Senha\" FROM users WHERE Usuário = ?", (usuario,))
        result = cursor.fetchone()
        if result and result[0] and result[0] != "Não Cadastrado":
            ultima_troca = datetime.strptime(result[0], "%d/%m/%Y")
            dias_passados = (datetime.now() - ultima_troca).days
            return dias_passados
        return None



    def obter_data_ultima_troca(self, usuario):
        try:
            cursor = self.db.connection.cursor()
            query = "SELECT [Última Troca de Senha] FROM users WHERE Usuário = ?"
            cursor.execute(query, (usuario,))
            result = cursor.fetchone()

            if result and result[0] and result[0].strip() and result[0].strip() != 'Última Troca de Senha':
                return result[0].strip()
            else:
                return None

        except Exception as e:
            print(f"Erro ao obter a data da última troca de senha: {e}")
            return None

    def obter_senha_atual(self, usuario):
        try:
            cursor = self.db.connection.cursor()
            query = "SELECT Senha FROM users WHERE Usuário = ?"
            cursor.execute(query, (usuario,))
            result = cursor.fetchone()
            return result[0] if result else None
        except Exception as e:
            print(f"Erro ao obter a senha atual: {e}")
            return None
        
    
    def validar_senha(self, senha, confirmar_senha):
        """
        Valida se a senha tem pelo menos 8 caracteres, letras, números
        e se a confirmação de senha é igual à senha.
        """
        if senha != confirmar_senha:
            return False  # As senhas não coincidem

        if (
            len(senha) >= 8 and
            re.search(r'[A-Za-z]', senha) and
            re.search(r'[0-9]', senha)
        ):
            return True  # Senha válida e confirmação correta

        return False  # Senha fraca
    
    def verificar_email(self, email):
        query = "SELECT 1 FROM users WHERE Email = ?"
        cursor = self.db.connection.cursor()
        cursor.execute(query, (email,))
        return cursor.fetchone() is not None

    def verificar_telefone(self, telefone):
        query = "SELECT 1 FROM users WHERE Telefone = ?"
        cursor = self.db.connection.cursor()
        cursor.execute(query, (telefone,))
        return cursor.fetchone() is not None


    def closeEvent(self, event):
        self.db.close_connection()
        event.accept()

    