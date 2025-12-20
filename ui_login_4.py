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
    QSizePolicy, QSpacerItem, QToolButton, QVBoxLayout,
    QWidget)

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
        self.btn_opcoes_extras = QToolButton(self.centralwidget)
        self.btn_opcoes_extras.setObjectName(u"btn_opcoes_extras")
        self.btn_opcoes_extras.setGeometry(QRect(653, 10, 21, 21))
        sizePolicy.setHeightForWidth(self.btn_opcoes_extras.sizePolicy().hasHeightForWidth())
        self.btn_opcoes_extras.setSizePolicy(sizePolicy)
        self.btn_opcoes_extras.setMaximumSize(QSize(21, 21))
        self.btn_opcoes_extras.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_opcoes_extras.setStyleSheet(u"QToolButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    border:  transparent;\n"
"	background-color: rgb(100, 200, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u"imagens/32339.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_opcoes_extras.setIcon(icon)
        self.btn_opcoes_extras.setIconSize(QSize(21, 21))
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(141, 130, 398, 345))
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_2.setStyleSheet(u"QFrame#frame_2 {\n"
"    border-radius: 12px;\n"
"    border: 2px solid qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #1de9b6, stop:1 #0d47a1\n"
"    );\n"
"}\n"
"")
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(16)
        self.gridLayout.setContentsMargins(21, -1, 10, -1)
        self.btn_login = QPushButton(self.frame_2)
        self.btn_login.setObjectName(u"btn_login")
        sizePolicy.setHeightForWidth(self.btn_login.sizePolicy().hasHeightForWidth())
        self.btn_login.setSizePolicy(sizePolicy)
        self.btn_login.setMinimumSize(QSize(0, 31))
        self.btn_login.setMaximumSize(QSize(16777215, 40))
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

        self.gridLayout.addWidget(self.btn_login, 6, 1, 1, 6)

        self.horizontalSpacer_10 = QSpacerItem(98, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_10, 4, 6, 1, 3)

        self.horizontalSpacer_9 = QSpacerItem(57, 36, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_9, 4, 0, 1, 2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 6, 1, 1)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_manter_conectado = QCheckBox(self.frame_4)
        self.btn_manter_conectado.setObjectName(u"btn_manter_conectado")
        sizePolicy.setHeightForWidth(self.btn_manter_conectado.sizePolicy().hasHeightForWidth())
        self.btn_manter_conectado.setSizePolicy(sizePolicy)
        self.btn_manter_conectado.setMaximumSize(QSize(16777215, 16777215))
        self.btn_manter_conectado.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.btn_manter_conectado)


        self.gridLayout.addWidget(self.frame_4, 4, 3, 1, 3)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_trocar_senha = QLabel(self.frame_3)
        self.label_trocar_senha.setObjectName(u"label_trocar_senha")
        sizePolicy.setHeightForWidth(self.label_trocar_senha.sizePolicy().hasHeightForWidth())
        self.label_trocar_senha.setSizePolicy(sizePolicy)
        self.label_trocar_senha.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.label_trocar_senha)


        self.gridLayout.addWidget(self.frame_3, 3, 4, 1, 1)

        self.txt_senha = QLineEdit(self.frame_2)
        self.txt_senha.setObjectName(u"txt_senha")
        sizePolicy.setHeightForWidth(self.txt_senha.sizePolicy().hasHeightForWidth())
        self.txt_senha.setSizePolicy(sizePolicy)
        self.txt_senha.setMinimumSize(QSize(0, 40))
        self.txt_senha.setMaximumSize(QSize(16777215, 30))
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

        self.gridLayout.addWidget(self.txt_senha, 2, 0, 1, 8)

        self.txt_usuario = QLineEdit(self.frame_2)
        self.txt_usuario.setObjectName(u"txt_usuario")
        sizePolicy.setHeightForWidth(self.txt_usuario.sizePolicy().hasHeightForWidth())
        self.txt_usuario.setSizePolicy(sizePolicy)
        self.txt_usuario.setMinimumSize(QSize(0, 40))
        self.txt_usuario.setMaximumSize(QSize(16777215, 40))
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

        self.gridLayout.addWidget(self.txt_usuario, 1, 0, 1, 8)

        self.verticalSpacer_2 = QSpacerItem(20, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 5, 4, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 61, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(19, 18, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 6, 7, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(326, 38, 18, 18))
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QSize(217, 219))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_foto_sistema = QLabel(self.centralwidget)
        self.label_foto_sistema.setObjectName(u"label_foto_sistema")
        self.label_foto_sistema.setGeometry(QRect(270, 57, 141, 141))
        sizePolicy.setHeightForWidth(self.label_foto_sistema.sizePolicy().hasHeightForWidth())
        self.label_foto_sistema.setSizePolicy(sizePolicy)
        self.label_foto_sistema.setStyleSheet(u"border-radius: 45px;\n"
"background: transparent;")
        self.label_foto_sistema.setFrameShape(QFrame.Box)
        self.label_foto_sistema.setPixmap(QPixmap(u"imagens/Imagem2.png"))
        self.label_foto_sistema.setScaledContents(True)
        self.label_foto_sistema.setAlignment(Qt.AlignCenter)
        self.label_foto_sistema.setWordWrap(False)
        self.label_foto_sistema.setTextInteractionFlags(Qt.NoTextInteraction)
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
        self.btn_login.setText(QCoreApplication.translate("Mainwindow_Login", u"LOGIN", None))
        self.btn_manter_conectado.setText(QCoreApplication.translate("Mainwindow_Login", u"Mantenha-me conectado", None))
        self.label_trocar_senha.setText(QCoreApplication.translate("Mainwindow_Login", u"<html><head/><body><p align=\"center\"><a href=\"trocar_senha\"><span style=\" text-decoration: underline; color:#0000ff;\">Esqueci a senha</span></a></p></body></html>", None))
        self.txt_senha.setPlaceholderText(QCoreApplication.translate("Mainwindow_Login", u"Senha", None))
        self.txt_usuario.setPlaceholderText(QCoreApplication.translate("Mainwindow_Login", u"Usu\u00e1rio,email ou CPF", None))
        self.label_foto_sistema.setText("")
    # retranslateUi

