from PySide6.QtWidgets import QLineEdit, QPushButton,QVBoxLayout,QLabel,QFrame
from PySide6.QtGui import QIcon, QPixmap, QTransform
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve


class MostrarSenha:
    def __init__(self, main_window, line_edit: QLineEdit):
        self.line_edit = line_edit
        self._show_password = False
        self.botao_exibir_senha()
        self.main_window = main_window  

    def botao_exibir_senha(self):
        # Criar botão dentro do QLineEdit
        self.btn_mostrar_senha = QPushButton(self.line_edit)
        self.btn_mostrar_senha.setCursor(Qt.PointingHandCursor)
        self.btn_mostrar_senha.setContentsMargins(0,0,0,0)
        self.btn_mostrar_senha.setObjectName("btn_mostrar_senha")
        
        altura = self.line_edit.height() - 4
        self.btn_mostrar_senha.setFixedSize(altura, altura)
        self.btn_mostrar_senha.move(self.line_edit.width() - altura - 2, 2)


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
        
    def animar_botao(self):
        rect = self.btn_mostrar_senha.geometry()
        # botão “afunda” 2 pixels para baixo e direita
        self.anim = QPropertyAnimation(self.btn_mostrar_senha, b"geometry")
        self.anim.setDuration(100)
        self.anim.setStartValue(rect)
        self.anim.setKeyValueAt(0.5, rect.adjusted(2, 2, 2, 2))
        self.anim.setEndValue(rect)
        self.anim.start()


    def senha_visivel(self):
        self.animar_botao()
        
        if self._show_password:
            self.line_edit.setEchoMode(QLineEdit.Password)
            self._show_password = False
        else:
            self.line_edit.setEchoMode(QLineEdit.Normal)
            self._show_password = True



def configurar_frame_valores(frame: QFrame, titulo: str, valor_monetario: bool = True) -> QLabel:
    layout = QVBoxLayout(frame)
    layout.setAlignment(Qt.AlignCenter)

    label_titulo = QLabel(titulo)
    label_titulo.setAlignment(Qt.AlignCenter)
    label_titulo.setObjectName("label_titulo")

    label_valor = QLabel("R$ 0,00" if valor_monetario else "")
    label_valor.setAlignment(Qt.AlignCenter)
    label_valor.setObjectName("label_valor")

    layout.addWidget(label_titulo)
    layout.addWidget(label_valor)

    return label_valor  # você salva essa referência depois para atualizar o texto
