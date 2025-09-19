# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_4.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_Mainwindow_Login(object):
    def setupUi(self, Mainwindow_Login):
        if not Mainwindow_Login.objectName():
            Mainwindow_Login.setObjectName(u"Mainwindow_Login")
        Mainwindow_Login.resize(683, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Mainwindow_Login.sizePolicy().hasHeightForWidth())
        Mainwindow_Login.setSizePolicy(sizePolicy)
        Mainwindow_Login.setMaximumSize(QSize(683, 600))
        Mainwindow_Login.setStyleSheet(u"background-color: rgb(0, 80, 121);")
        self.centralwidget = QWidget(Mainwindow_Login)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_opcoes_extras = QPushButton(self.centralwidget)
        self.btn_opcoes_extras.setObjectName(u"btn_opcoes_extras")
        sizePolicy.setHeightForWidth(self.btn_opcoes_extras.sizePolicy().hasHeightForWidth())
        self.btn_opcoes_extras.setSizePolicy(sizePolicy)
        self.btn_opcoes_extras.setMaximumSize(QSize(21, 21))
        self.btn_opcoes_extras.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_opcoes_extras.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    border:  transparent;\n"
"	background-color: rgb(100, 200, 255);\n"
"}\n"
"\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u"imagens/32339.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_opcoes_extras.setIcon(icon)
        self.btn_opcoes_extras.setIconSize(QSize(21, 21))

        self.gridLayout.addWidget(self.btn_opcoes_extras, 0, 4, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(218, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 3, 3, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(183, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(189, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 2, 0, 2, 2)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(217, 0))
        self.frame_2.setMaximumSize(QSize(290, 350))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.txt_usuario = QLineEdit(self.frame_2)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setGeometry(QRect(50, 28, 120, 30))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(100)
        sizePolicy1.setVerticalStretch(100)
        sizePolicy1.setHeightForWidth(self.txt_usuario.sizePolicy().hasHeightForWidth())
        self.txt_usuario.setSizePolicy(sizePolicy1)
        self.txt_usuario.setMaximumSize(QSize(121, 30))
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
        self.txt_usuario.setAlignment(Qt.AlignCenter)
        self.txt_senha = QLineEdit(self.frame_2)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setGeometry(QRect(50, 81, 120, 30))
        sizePolicy.setHeightForWidth(self.txt_senha.sizePolicy().hasHeightForWidth())
        self.txt_senha.setSizePolicy(sizePolicy)
        self.txt_senha.setMaximumSize(QSize(121, 30))
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
        self.label_primeiro_acesso = QLabel(self.frame_2)
        self.label_primeiro_acesso.setObjectName(u"label_primeiro_acesso")
        self.label_primeiro_acesso.setGeometry(QRect(70, 134, 90, 16))
        sizePolicy.setHeightForWidth(self.label_primeiro_acesso.sizePolicy().hasHeightForWidth())
        self.label_primeiro_acesso.setSizePolicy(sizePolicy)
        self.label_primeiro_acesso.setMaximumSize(QSize(90, 20))
        self.btn_manter_conectado = QCheckBox(self.frame_2)
        self.btn_manter_conectado.setObjectName(u"btn_manter_conectado")
        self.btn_manter_conectado.setGeometry(QRect(41, 177, 160, 17))
        sizePolicy.setHeightForWidth(self.btn_manter_conectado.sizePolicy().hasHeightForWidth())
        self.btn_manter_conectado.setSizePolicy(sizePolicy)
        self.btn_manter_conectado.setMaximumSize(QSize(16777215, 16777215))
        self.btn_manter_conectado.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_trocar_senha = QLabel(self.frame_2)
        self.label_trocar_senha.setObjectName(u"label_trocar_senha")
        self.label_trocar_senha.setGeometry(QRect(73, 220, 90, 16))
        sizePolicy.setHeightForWidth(self.label_trocar_senha.sizePolicy().hasHeightForWidth())
        self.label_trocar_senha.setSizePolicy(sizePolicy)
        self.label_trocar_senha.setMaximumSize(QSize(90, 20))
        self.btn_login = QPushButton(self.frame_2)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(50, 260, 120, 35))
        sizePolicy.setHeightForWidth(self.btn_login.sizePolicy().hasHeightForWidth())
        self.btn_login.setSizePolicy(sizePolicy)
        self.btn_login.setMaximumSize(QSize(16777215, 35))
        self.btn_login.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_login.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 14px;\n"
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

        self.gridLayout.addWidget(self.frame_2, 2, 2, 3, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QSize(217, 219))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_foto_sistema = QLabel(self.frame)
        self.label_foto_sistema.setObjectName(u"label_foto_sistema")
        sizePolicy.setHeightForWidth(self.label_foto_sistema.sizePolicy().hasHeightForWidth())
        self.label_foto_sistema.setSizePolicy(sizePolicy)
        self.label_foto_sistema.setMaximumSize(QSize(16777215, 16777215))
        self.label_foto_sistema.setPixmap(QPixmap(u"imagens/74472.png"))
        self.label_foto_sistema.setScaledContents(True)
        self.label_foto_sistema.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_foto_sistema, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 1, 2, 1, 2)

        Mainwindow_Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Mainwindow_Login)

        QMetaObject.connectSlotsByName(Mainwindow_Login)
    # setupUi

    def retranslateUi(self, Mainwindow_Login):
        Mainwindow_Login.setWindowTitle(QCoreApplication.translate("Mainwindow_Login", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.btn_opcoes_extras.setToolTip(QCoreApplication.translate("Mainwindow_Login", u"Reiniciar sistema", None))
#endif // QT_CONFIG(tooltip)
        self.btn_opcoes_extras.setText("")
        self.txt_usuario.setPlaceholderText(QCoreApplication.translate("Mainwindow_Login", u"Usu\u00e1rio,email ou CPF", None))
        self.txt_senha.setPlaceholderText(QCoreApplication.translate("Mainwindow_Login", u"Senha", None))
        self.label_primeiro_acesso.setText(QCoreApplication.translate("Mainwindow_Login", u"<a href=\"primeiro_acesso\">Primeiro acesso?</a>", None))
        self.btn_manter_conectado.setText(QCoreApplication.translate("Mainwindow_Login", u"Mantenha-me conectado", None))
        self.label_trocar_senha.setText(QCoreApplication.translate("Mainwindow_Login", u"<a href=\"trocar_senha\">Esqueci a senha</a>", None))
        self.btn_login.setText(QCoreApplication.translate("Mainwindow_Login", u"Login", None))
        self.label_foto_sistema.setText("")
    # retranslateUi

