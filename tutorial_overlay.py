from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPainter, QColor
from PySide6.QtWidgets import QWidget, QMessageBox, QCheckBox


class TutorialOverlay(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WA_TransparentForMouseEvents, False)  # bloqueia clique no fundo
        self.setWindowFlags(Qt.Widget)

        self._msg: QMessageBox | None = None
        self._on_close_callback = None

        self.hide()

    def show_tutorial(self, title: str, text: str, on_close=None):
        # evita abrir 2x (flash / duplicação)
        if self._msg is not None:
            return

        self._on_close_callback = on_close

        # ⏳ espera, mas NÃO escurece ainda
        QTimer.singleShot(2000, lambda: self.abrir_msgbox(title, text))

    def abrir_msgbox(self, title, text):
        self.setGeometry(self.parentWidget().rect())
        self.raise_()
        self.show()
        self.update()
        
        
        msg = QMessageBox(self.window())
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle(title)
        msg.setText(title)
        msg.setInformativeText(text)

        chk = QCheckBox("Não mostrar essa mensagem novamente")
        msg.setCheckBox(chk)

        msg.setStandardButtons(QMessageBox.Ok)
        msg.button(QMessageBox.Ok).setText("Entendi")

        def finished(_):
            self.hide()
            if callable(self._on_close_callback):
                self._on_close_callback(bool(chk.isChecked()))
            self._msg = None

        msg.finished.connect(finished)

        self._msg = msg
        msg.adjustSize()
        self._position_msgbox_using_size(msg.size())
        msg.show()
        
    def _position_msgbox_using_size(self, msg_size):
        margin = 16
        host = self.window()
        host_rect = host.geometry()

        x = host_rect.x() + host_rect.width() - msg_size.width() - margin
        y = host_rect.y() + margin
        self._msg.move(x, y)

    def _position_msgbox(self):
        if not self._msg:
            return

        margin = 16
        host = self.window()
        host_rect = host.geometry()

        size = self._msg.sizeHint()
        x = host_rect.x() + host_rect.width() - size.width() - margin
        y = host_rect.y() + margin
        self._msg.move(x, y)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.setGeometry(self.parentWidget().rect())
        self._position_msgbox()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # ✅ mais visível: 170 (teste entre 140 e 200)
        painter.fillRect(self.rect(), QColor(0, 0, 0, 170))