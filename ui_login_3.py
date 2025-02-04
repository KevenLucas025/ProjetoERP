# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_3.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_Mainwindow_Login(object):
    def setupUi(self, Mainwindow_Login):
        if not Mainwindow_Login.objectName():
            Mainwindow_Login.setObjectName(u"Mainwindow_Login")
        Mainwindow_Login.resize(683, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Mainwindow_Login.sizePolicy().hasHeightForWidth())
        Mainwindow_Login.setSizePolicy(sizePolicy)
        Mainwindow_Login.setStyleSheet(u"background-color: rgb(0,74, 112);")
        self.centralwidget = QWidget(Mainwindow_Login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.layout_login_tela = QGridLayout()
        self.layout_login_tela.setObjectName(u"layout_login_tela")
        self.layout_login_tela.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.layout_login_tela.setHorizontalSpacing(25)
        self.layout_login_tela.setVerticalSpacing(6)
        self.layout_login_tela.setContentsMargins(20, 19, 0, 3)
        self.frame_login_botao = QFrame(self.centralwidget)
        self.frame_login_botao.setObjectName(u"frame_login_botao")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_login_botao.sizePolicy().hasHeightForWidth())
        self.frame_login_botao.setSizePolicy(sizePolicy1)
        self.frame_login_botao.setMinimumSize(QSize(0, 250))
        self.frame_login_botao.setMaximumSize(QSize(300, 300))
        self.frame_login_botao.setFrameShape(QFrame.NoFrame)
        self.frame_login_botao.setFrameShadow(QFrame.Raised)
        self.label_primeiro_acesso = QLabel(self.frame_login_botao)
        self.label_primeiro_acesso.setObjectName(u"label_primeiro_acesso")
        self.label_primeiro_acesso.setGeometry(QRect(92, 105, 141, 51))
        sizePolicy1.setHeightForWidth(self.label_primeiro_acesso.sizePolicy().hasHeightForWidth())
        self.label_primeiro_acesso.setSizePolicy(sizePolicy1)
        self.label_primeiro_acesso.setMinimumSize(QSize(15, 51))
        self.label_primeiro_acesso.setMaximumSize(QSize(150, 24))
        self.label_primeiro_acesso.setSizeIncrement(QSize(0, 0))
        self.label_primeiro_acesso.setBaseSize(QSize(0, 0))
        self.label_primeiro_acesso.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_primeiro_acesso.setTextFormat(Qt.PlainText)
        self.label_primeiro_acesso.setScaledContents(False)
        self.label_primeiro_acesso.setMargin(17)
        self.label_primeiro_acesso.setIndent(-1)
        self.btn_manter_conectado = QCheckBox(self.frame_login_botao)
        self.btn_manter_conectado.setObjectName(u"btn_manter_conectado")
        self.btn_manter_conectado.setEnabled(True)
        self.btn_manter_conectado.setGeometry(QRect(79, 167, 158, 24))
        sizePolicy1.setHeightForWidth(self.btn_manter_conectado.sizePolicy().hasHeightForWidth())
        self.btn_manter_conectado.setSizePolicy(sizePolicy1)
        self.btn_manter_conectado.setMinimumSize(QSize(158, 18))
        self.btn_manter_conectado.setMaximumSize(QSize(152, 24))
        self.btn_manter_conectado.setSizeIncrement(QSize(0, 0))
        self.btn_manter_conectado.setBaseSize(QSize(0, 0))
        self.btn_manter_conectado.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_manter_conectado.setCheckable(True)
        self.btn_manter_conectado.setAutoRepeat(False)
        self.label_trocar_senha = QLabel(self.frame_login_botao)
        self.label_trocar_senha.setObjectName(u"label_trocar_senha")
        self.label_trocar_senha.setGeometry(QRect(92, 200, 130, 49))
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(37)
        sizePolicy2.setHeightForWidth(self.label_trocar_senha.sizePolicy().hasHeightForWidth())
        self.label_trocar_senha.setSizePolicy(sizePolicy2)
        self.label_trocar_senha.setMinimumSize(QSize(130, 49))
        self.label_trocar_senha.setMaximumSize(QSize(110, 56))
        self.label_trocar_senha.setSizeIncrement(QSize(0, 0))
        self.label_trocar_senha.setBaseSize(QSize(0, 0))
        self.label_trocar_senha.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_trocar_senha.setText(u"<a href=\"trocar_senha\" style=\"color: white;\">Esqueci a senha</a>")
        self.label_trocar_senha.setTextFormat(Qt.AutoText)
        self.label_trocar_senha.setScaledContents(False)
        self.label_trocar_senha.setWordWrap(False)
        self.label_trocar_senha.setMargin(17)
        self.label_trocar_senha.setIndent(-1)
        self.label_trocar_senha.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
        self.btn_login = QPushButton(self.frame_login_botao)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(101, 250, 90, 38))
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(27)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_login.sizePolicy().hasHeightForWidth())
        self.btn_login.setSizePolicy(sizePolicy3)
        self.btn_login.setMinimumSize(QSize(90, 28))
        self.btn_login.setMaximumSize(QSize(90, 38))
        self.btn_login.setBaseSize(QSize(0, 0))
        self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_login.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 3px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}\n"
"")
        self.btn_login.setAutoDefault(False)
        self.txt_senha = QLineEdit(self.frame_login_botao)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setGeometry(QRect(80, 70, 128, 32))
        sizePolicy1.setHeightForWidth(self.txt_senha.sizePolicy().hasHeightForWidth())
        self.txt_senha.setSizePolicy(sizePolicy1)
        self.txt_senha.setMinimumSize(QSize(0, 0))
        self.txt_senha.setMaximumSize(QSize(166675, 166675))
        self.txt_senha.setCursor(QCursor(Qt.IBeamCursor))
        self.txt_senha.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #0078d4;  /* Cor da borda */\n"
"    border-radius: 5px;          /* Bordas arredondadas */\n"
"    padding: 5px;                /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: white;  /* Cor do placeholder */\n"
"}\n"
"")
        self.txt_senha.setEchoMode(QLineEdit.Password)
        self.txt_senha.setAlignment(Qt.AlignCenter)
        self.txt_senha.setDragEnabled(False)
        self.txt_senha.setReadOnly(False)
        self.txt_senha.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.txt_senha.setClearButtonEnabled(False)
        self.txt_usuario = QLineEdit(self.frame_login_botao)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setGeometry(QRect(80, 20, 128, 32))
        sizePolicy1.setHeightForWidth(self.txt_usuario.sizePolicy().hasHeightForWidth())
        self.txt_usuario.setSizePolicy(sizePolicy1)
        self.txt_usuario.setMinimumSize(QSize(0, 0))
        self.txt_usuario.setMaximumSize(QSize(164578, 1646578))
        self.txt_usuario.setCursor(QCursor(Qt.IBeamCursor))
        self.txt_usuario.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #0078d4;  /* Cor da borda */\n"
"    border-radius: 5px;          /* Bordas arredondadas */\n"
"    padding: 5px;                /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: white;  /* Cor do placeholder */\n"
"}\n"
"")
        self.txt_usuario.setFrame(True)
        self.txt_usuario.setAlignment(Qt.AlignCenter)
        self.txt_usuario.setDragEnabled(False)
        self.txt_usuario.setReadOnly(False)
        self.txt_usuario.setClearButtonEnabled(False)

        self.layout_login_tela.addWidget(self.frame_login_botao, 10, 0, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMinimumSize(QSize(205, 190))
        self.frame.setMaximumSize(QSize(250, 250))
        self.frame.setSizeIncrement(QSize(0, 0))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_foto_sistema = QLabel(self.frame)
        self.label_foto_sistema.setObjectName(u"label_foto_sistema")
        self.label_foto_sistema.setGeometry(QRect(28, 10, 221, 221))
        sizePolicy1.setHeightForWidth(self.label_foto_sistema.sizePolicy().hasHeightForWidth())
        self.label_foto_sistema.setSizePolicy(sizePolicy1)
        self.label_foto_sistema.setMaximumSize(QSize(250, 300))
        self.label_foto_sistema.setPixmap(QPixmap(u"imagens/74472.png"))
        self.label_foto_sistema.setScaledContents(True)

        self.layout_login_tela.addWidget(self.frame, 1, 0, 1, 1)


        self.gridLayout_3.addLayout(self.layout_login_tela, 0, 0, 1, 1)

        Mainwindow_Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Mainwindow_Login)

        QMetaObject.connectSlotsByName(Mainwindow_Login)
    # setupUi

    def retranslateUi(self, Mainwindow_Login):
        Mainwindow_Login.setWindowTitle(QCoreApplication.translate("Mainwindow_Login", u"MainWindow", None))
        self.label_primeiro_acesso.setText(QCoreApplication.translate("Mainwindow_Login", u"Primeiro acesso?", None))
        self.btn_manter_conectado.setText(QCoreApplication.translate("Mainwindow_Login", u"Mantenha-me conectado", None))
#if QT_CONFIG(shortcut)
        self.btn_manter_conectado.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.btn_login.setText(QCoreApplication.translate("Mainwindow_Login", u"Login", None))
        self.txt_senha.setPlaceholderText(QCoreApplication.translate("Mainwindow_Login", u"Senha", None))
        self.txt_usuario.setPlaceholderText(QCoreApplication.translate("Mainwindow_Login", u"Usu\u00e1rio ou e-mail", None))
        self.label_foto_sistema.setText("")
    # retranslateUi

