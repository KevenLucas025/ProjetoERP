from PySide6.QtWidgets import QLineEdit, QToolButton
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt

class MostrarSenha:
    def __init__(self, txt_senha, txt_confirmar_senha):
        self.line_edit = line_edit
        self._show_password = False
        self.botao_exibir_senha()

    def botao_exibir_senha(self):
        # Criar botão dentro do QLineEdit
        self.btn_mostrar_senha = QToolButton(self.line_edit)
        self.btn_mostrar_senha.setCursor(Qt.PointingHandCursor)
        self.btn_mostrar_senha.setIcon(QIcon(QPixmap("imagens/829117.png")))  # Ícone olho fechado
        
        altura = self.line_edit.height() - 4
        self.btn_mostrar_senha.setFixedSize(altura, altura)
        self.btn_mostrar_senha.move(self.line_edit.width() - altura - 2, 2)
        
        # Ajustar padding do texto para não ficar atrás do botão
        self.line_edit.setStyleSheet("""
            QLineEdit {
                background: transparent;
            }
            """
            )

        # Conectar o clique para alternar mostrar/ocultar senha
        self.btn_mostrar_senha.clicked.connect(self.senha_visivel)

        # Definir modo password inicialmente
        self.line_edit.setEchoMode(QLineEdit.Password)

        # Ajustar o posicionamento caso o QLineEdit mude de tamanho (opcional)
        self.line_edit.resizeEvent = self._on_resize

    def _on_resize(self, event):
        altura = self.line_edit.height() - 4
        self.btn_mostrar_senha.setFixedSize(altura, altura)
        self.btn_mostrar_senha.move(self.line_edit.width() - altura - 2, 2)
        
        # Se tiver um método original de resizeEvent, você pode chamar aqui, se quiser

    def senha_visivel(self):
        if self._show_password:
            self.line_edit.setEchoMode(QLineEdit.Password)
            self.btn_mostrar_senha.setIcon(QIcon(QPixmap("imagens/829117.png")))
            self._show_password = False
        else:
            self.line_edit.setEchoMode(QLineEdit.Normal)
            self.btn_mostrar_senha.setIcon(QIcon(QPixmap("imagens/829117.png")))
            self._show_password = True
