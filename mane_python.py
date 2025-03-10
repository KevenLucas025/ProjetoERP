# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maine6.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QAbstractSpinBox, QApplication,
    QComboBox, QDateEdit, QDateTimeEdit, QFormLayout,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QTableWidget, QTableWidgetItem,
    QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1713, 949)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(400, 200))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"background-color: rgb(0,80,121)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.frame_principal = QFrame(self.centralwidget)
        self.frame_principal.setObjectName(u"frame_principal")
        sizePolicy.setHeightForWidth(self.frame_principal.sizePolicy().hasHeightForWidth())
        self.frame_principal.setSizePolicy(sizePolicy)
        self.frame_principal.setFrameShape(QFrame.NoFrame)
        self.frame_principal.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_principal)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_botoes_navegacoes = QFrame(self.frame_principal)
        self.frame_botoes_navegacoes.setObjectName(u"frame_botoes_navegacoes")
        sizePolicy.setHeightForWidth(self.frame_botoes_navegacoes.sizePolicy().hasHeightForWidth())
        self.frame_botoes_navegacoes.setSizePolicy(sizePolicy)
        self.frame_botoes_navegacoes.setMaximumSize(QSize(162, 16777215))
        self.frame_botoes_navegacoes.setFrameShape(QFrame.NoFrame)
        self.frame_botoes_navegacoes.setFrameShadow(QFrame.Plain)
        self.verticalLayout_11 = QVBoxLayout(self.frame_botoes_navegacoes)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.btn_home = QPushButton(self.frame_botoes_navegacoes)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMaximumSize(QSize(145, 25))
        self.btn_home.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_home.setStyleSheet(u"QPushButton {\n"
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
"}")

        self.verticalLayout_11.addWidget(self.btn_home)

        self.btn_verificar_estoque = QPushButton(self.frame_botoes_navegacoes)
        self.btn_verificar_estoque.setObjectName(u"btn_verificar_estoque")
        sizePolicy.setHeightForWidth(self.btn_verificar_estoque.sizePolicy().hasHeightForWidth())
        self.btn_verificar_estoque.setSizePolicy(sizePolicy)
        self.btn_verificar_estoque.setMaximumSize(QSize(145, 25))
        self.btn_verificar_estoque.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_verificar_estoque.setStyleSheet(u"QPushButton {\n"
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
"}")

        self.verticalLayout_11.addWidget(self.btn_verificar_estoque)

        self.btn_verificar_usuarios = QPushButton(self.frame_botoes_navegacoes)
        self.btn_verificar_usuarios.setObjectName(u"btn_verificar_usuarios")
        sizePolicy.setHeightForWidth(self.btn_verificar_usuarios.sizePolicy().hasHeightForWidth())
        self.btn_verificar_usuarios.setSizePolicy(sizePolicy)
        self.btn_verificar_usuarios.setMaximumSize(QSize(145, 25))
        self.btn_verificar_usuarios.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_verificar_usuarios.setStyleSheet(u"QPushButton {\n"
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
"}")

        self.verticalLayout_11.addWidget(self.btn_verificar_usuarios)

        self.btn_cadastrar_produto = QPushButton(self.frame_botoes_navegacoes)
        self.btn_cadastrar_produto.setObjectName(u"btn_cadastrar_produto")
        sizePolicy.setHeightForWidth(self.btn_cadastrar_produto.sizePolicy().hasHeightForWidth())
        self.btn_cadastrar_produto.setSizePolicy(sizePolicy)
        self.btn_cadastrar_produto.setMaximumSize(QSize(145, 25))
        self.btn_cadastrar_produto.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cadastrar_produto.setStyleSheet(u"QPushButton {\n"
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
"}")

        self.verticalLayout_11.addWidget(self.btn_cadastrar_produto)

        self.btn_cadastrar_usuarios = QPushButton(self.frame_botoes_navegacoes)
        self.btn_cadastrar_usuarios.setObjectName(u"btn_cadastrar_usuarios")
        sizePolicy.setHeightForWidth(self.btn_cadastrar_usuarios.sizePolicy().hasHeightForWidth())
        self.btn_cadastrar_usuarios.setSizePolicy(sizePolicy)
        self.btn_cadastrar_usuarios.setMaximumSize(QSize(145, 25))
        self.btn_cadastrar_usuarios.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cadastrar_usuarios.setStyleSheet(u"QPushButton {\n"
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
"}")

        self.verticalLayout_11.addWidget(self.btn_cadastrar_usuarios)

        self.btn_clientes = QPushButton(self.frame_botoes_navegacoes)
        self.btn_clientes.setObjectName(u"btn_clientes")
        sizePolicy.setHeightForWidth(self.btn_clientes.sizePolicy().hasHeightForWidth())
        self.btn_clientes.setSizePolicy(sizePolicy)
        self.btn_clientes.setMaximumSize(QSize(145, 25))
        self.btn_clientes.setStyleSheet(u"QPushButton {\n"
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
"}")

        self.verticalLayout_11.addWidget(self.btn_clientes)

        self.btn_configuracoes = QPushButton(self.frame_botoes_navegacoes)
        self.btn_configuracoes.setObjectName(u"btn_configuracoes")
        sizePolicy.setHeightForWidth(self.btn_configuracoes.sizePolicy().hasHeightForWidth())
        self.btn_configuracoes.setSizePolicy(sizePolicy)
        self.btn_configuracoes.setMaximumSize(QSize(145, 25))
        self.btn_configuracoes.setStyleSheet(u"QPushButton {\n"
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
"}")

        self.verticalLayout_11.addWidget(self.btn_configuracoes)


        self.gridLayout_2.addWidget(self.frame_botoes_navegacoes, 0, 0, 1, 1)

        self.paginas_sistemas = QStackedWidget(self.frame_principal)
        self.paginas_sistemas.setObjectName(u"paginas_sistemas")
        sizePolicy.setHeightForWidth(self.paginas_sistemas.sizePolicy().hasHeightForWidth())
        self.paginas_sistemas.setSizePolicy(sizePolicy)
        self.paginas_sistemas.setFrameShape(QFrame.NoFrame)
        self.paginas_sistemas.setFrameShadow(QFrame.Plain)
        self.home_pag = QWidget()
        self.home_pag.setObjectName(u"home_pag")
        sizePolicy.setHeightForWidth(self.home_pag.sizePolicy().hasHeightForWidth())
        self.home_pag.setSizePolicy(sizePolicy)
        self.gridLayout_3 = QGridLayout(self.home_pag)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame = QFrame(self.home_pag)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_imagem_sistema = QLabel(self.frame)
        self.label_imagem_sistema.setObjectName(u"label_imagem_sistema")
        sizePolicy.setHeightForWidth(self.label_imagem_sistema.sizePolicy().hasHeightForWidth())
        self.label_imagem_sistema.setSizePolicy(sizePolicy)
        self.label_imagem_sistema.setMaximumSize(QSize(251, 161))
        self.label_imagem_sistema.setBaseSize(QSize(0, 0))
        self.label_imagem_sistema.setFocusPolicy(Qt.NoFocus)
        self.label_imagem_sistema.setPixmap(QPixmap(u"Projeto ERP/54206.cur"))
        self.label_imagem_sistema.setScaledContents(True)
        self.label_imagem_sistema.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_imagem_sistema.setWordWrap(False)
        self.label_imagem_sistema.setMargin(1)
        self.label_imagem_sistema.setIndent(-2)
        self.label_imagem_sistema.setOpenExternalLinks(False)

        self.gridLayout_4.addWidget(self.label_imagem_sistema, 0, 0, 1, 1)

        self.label_bem_vindo = QLabel(self.frame)
        self.label_bem_vindo.setObjectName(u"label_bem_vindo")
        sizePolicy.setHeightForWidth(self.label_bem_vindo.sizePolicy().hasHeightForWidth())
        self.label_bem_vindo.setSizePolicy(sizePolicy)
        self.label_bem_vindo.setMaximumSize(QSize(502, 234))
        self.label_bem_vindo.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_bem_vindo, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)

        self.paginas_sistemas.addWidget(self.home_pag)
        self.pag_estoque = QWidget()
        self.pag_estoque.setObjectName(u"pag_estoque")
        sizePolicy.setHeightForWidth(self.pag_estoque.sizePolicy().hasHeightForWidth())
        self.pag_estoque.setSizePolicy(sizePolicy)
        self.gridLayout_6 = QGridLayout(self.pag_estoque)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.frame_pag_estoque = QFrame(self.pag_estoque)
        self.frame_pag_estoque.setObjectName(u"frame_pag_estoque")
        sizePolicy.setHeightForWidth(self.frame_pag_estoque.sizePolicy().hasHeightForWidth())
        self.frame_pag_estoque.setSizePolicy(sizePolicy)
        self.frame_pag_estoque.setFrameShape(QFrame.NoFrame)
        self.frame_pag_estoque.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_pag_estoque)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.tb_base = QTabWidget(self.frame_pag_estoque)
        self.tb_base.setObjectName(u"tb_base")
        self.tb_base.setMaximumSize(QSize(16777215, 880))
        font = QFont()
        font.setBold(False)
        self.tb_base.setFont(font)
        self.tb_base.setFocusPolicy(Qt.NoFocus)
        self.tb_base.setStyleSheet(u"QTabWidget{\n"
"	border: 2px solid white;\n"
"}")
        self.tb_base.setLocale(QLocale(QLocale.Portuguese, QLocale.Brazil))
        self.tb_base.setTabShape(QTabWidget.Rounded)
        self.tb_base.setIconSize(QSize(0, 0))
        self.tb_base.setUsesScrollButtons(False)
        self.tb_base.setTabsClosable(False)
        self.tb_base.setMovable(False)
        self.tb_base.setTabBarAutoHide(True)
        self.tabela_base = QWidget()
        self.tabela_base.setObjectName(u"tabela_base")
        sizePolicy.setHeightForWidth(self.tabela_base.sizePolicy().hasHeightForWidth())
        self.tabela_base.setSizePolicy(sizePolicy)
        self.tabela_base.setMaximumSize(QSize(16777215, 880))
        self.gridLayout_13 = QGridLayout(self.tabela_base)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.frame_saida = QFrame(self.tabela_base)
        self.frame_saida.setObjectName(u"frame_saida")
        sizePolicy.setHeightForWidth(self.frame_saida.sizePolicy().hasHeightForWidth())
        self.frame_saida.setSizePolicy(sizePolicy)
        self.frame_saida.setMaximumSize(QSize(118, 54))
        self.frame_saida.setFrameShape(QFrame.NoFrame)
        self.frame_saida.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_saida)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_saida = QLabel(self.frame_saida)
        self.label_saida.setObjectName(u"label_saida")
        sizePolicy.setHeightForWidth(self.label_saida.sizePolicy().hasHeightForWidth())
        self.label_saida.setSizePolicy(sizePolicy)
        self.label_saida.setMinimumSize(QSize(97, 43))
        self.label_saida.setMaximumSize(QSize(134, 82))
        self.label_saida.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"	border: 3px solid white;\n"
"}\n"
"\n"
"")
        self.label_saida.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.label_saida, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.frame_saida, 3, 0, 1, 1)

        self.frame_btns_estorno_saida_importar = QFrame(self.tabela_base)
        self.frame_btns_estorno_saida_importar.setObjectName(u"frame_btns_estorno_saida_importar")
        sizePolicy.setHeightForWidth(self.frame_btns_estorno_saida_importar.sizePolicy().hasHeightForWidth())
        self.frame_btns_estorno_saida_importar.setSizePolicy(sizePolicy)
        self.frame_btns_estorno_saida_importar.setFrameShape(QFrame.NoFrame)
        self.frame_btns_estorno_saida_importar.setFrameShadow(QFrame.Raised)
        self.gridLayout_58 = QGridLayout(self.frame_btns_estorno_saida_importar)
        self.gridLayout_58.setObjectName(u"gridLayout_58")
        self.layout_btns_importar_saida_estorno = QHBoxLayout()
        self.layout_btns_importar_saida_estorno.setObjectName(u"layout_btns_importar_saida_estorno")
        self.horizontalSpacer_7 = QSpacerItem(56, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout_btns_importar_saida_estorno.addItem(self.horizontalSpacer_7)

        self.btn_gerar_estorno = QPushButton(self.frame_btns_estorno_saida_importar)
        self.btn_gerar_estorno.setObjectName(u"btn_gerar_estorno")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_gerar_estorno.sizePolicy().hasHeightForWidth())
        self.btn_gerar_estorno.setSizePolicy(sizePolicy1)
        self.btn_gerar_estorno.setMaximumSize(QSize(161, 28))
        self.btn_gerar_estorno.setStyleSheet(u"QPushButton {\n"
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

        self.layout_btns_importar_saida_estorno.addWidget(self.btn_gerar_estorno)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout_btns_importar_saida_estorno.addItem(self.horizontalSpacer_10)

        self.btn_importar = QPushButton(self.frame_btns_estorno_saida_importar)
        self.btn_importar.setObjectName(u"btn_importar")
        sizePolicy.setHeightForWidth(self.btn_importar.sizePolicy().hasHeightForWidth())
        self.btn_importar.setSizePolicy(sizePolicy)
        self.btn_importar.setMaximumSize(QSize(168, 28))
        self.btn_importar.setStyleSheet(u"QPushButton {\n"
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

        self.layout_btns_importar_saida_estorno.addWidget(self.btn_importar)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout_btns_importar_saida_estorno.addItem(self.horizontalSpacer_9)

        self.btn_gerar_saida = QPushButton(self.frame_btns_estorno_saida_importar)
        self.btn_gerar_saida.setObjectName(u"btn_gerar_saida")
        sizePolicy.setHeightForWidth(self.btn_gerar_saida.sizePolicy().hasHeightForWidth())
        self.btn_gerar_saida.setSizePolicy(sizePolicy)
        self.btn_gerar_saida.setMaximumSize(QSize(168, 28))
        self.btn_gerar_saida.setStyleSheet(u"QPushButton {\n"
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

        self.layout_btns_importar_saida_estorno.addWidget(self.btn_gerar_saida)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout_btns_importar_saida_estorno.addItem(self.horizontalSpacer_8)


        self.gridLayout_58.addLayout(self.layout_btns_importar_saida_estorno, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.frame_btns_estorno_saida_importar, 3, 2, 1, 2)

        self.frame_botoes_tabelas = QFrame(self.tabela_base)
        self.frame_botoes_tabelas.setObjectName(u"frame_botoes_tabelas")
        sizePolicy.setHeightForWidth(self.frame_botoes_tabelas.sizePolicy().hasHeightForWidth())
        self.frame_botoes_tabelas.setSizePolicy(sizePolicy)
        self.frame_botoes_tabelas.setMinimumSize(QSize(0, 831))
        self.frame_botoes_tabelas.setMaximumSize(QSize(183, 831))
        self.frame_botoes_tabelas.setFrameShape(QFrame.NoFrame)
        self.frame_botoes_tabelas.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_botoes_tabelas)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.layout_botoes_tabelas = QVBoxLayout()
        self.layout_botoes_tabelas.setSpacing(9)
        self.layout_botoes_tabelas.setObjectName(u"layout_botoes_tabelas")
        self.layout_botoes_tabelas.setContentsMargins(0, 1, 1, 0)
        self.btn_novo_produto = QPushButton(self.frame_botoes_tabelas)
        self.btn_novo_produto.setObjectName(u"btn_novo_produto")
        sizePolicy.setHeightForWidth(self.btn_novo_produto.sizePolicy().hasHeightForWidth())
        self.btn_novo_produto.setSizePolicy(sizePolicy)
        self.btn_novo_produto.setMaximumSize(QSize(197, 30))
        font1 = QFont()
        self.btn_novo_produto.setFont(font1)
        self.btn_novo_produto.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_novo_produto.setStyleSheet(u"QPushButton {\n"
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

        self.layout_botoes_tabelas.addWidget(self.btn_novo_produto)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layout_botoes_tabelas.addItem(self.verticalSpacer)

        self.btn_atualizar_saida = QPushButton(self.frame_botoes_tabelas)
        self.btn_atualizar_saida.setObjectName(u"btn_atualizar_saida")
        sizePolicy.setHeightForWidth(self.btn_atualizar_saida.sizePolicy().hasHeightForWidth())
        self.btn_atualizar_saida.setSizePolicy(sizePolicy)
        self.btn_atualizar_saida.setMaximumSize(QSize(197, 30))
        self.btn_atualizar_saida.setFont(font1)
        self.btn_atualizar_saida.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_atualizar_saida.setStyleSheet(u"QPushButton {\n"
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

        self.layout_botoes_tabelas.addWidget(self.btn_atualizar_saida)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layout_botoes_tabelas.addItem(self.verticalSpacer_2)

        self.btn_historico = QPushButton(self.frame_botoes_tabelas)
        self.btn_historico.setObjectName(u"btn_historico")
        sizePolicy.setHeightForWidth(self.btn_historico.sizePolicy().hasHeightForWidth())
        self.btn_historico.setSizePolicy(sizePolicy)
        self.btn_historico.setMaximumSize(QSize(197, 30))
        self.btn_historico.setFont(font1)
        self.btn_historico.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_historico.setStyleSheet(u"QPushButton {\n"
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

        self.layout_botoes_tabelas.addWidget(self.btn_historico)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layout_botoes_tabelas.addItem(self.verticalSpacer_3)

        self.btn_gerar_pdf = QPushButton(self.frame_botoes_tabelas)
        self.btn_gerar_pdf.setObjectName(u"btn_gerar_pdf")
        sizePolicy.setHeightForWidth(self.btn_gerar_pdf.sizePolicy().hasHeightForWidth())
        self.btn_gerar_pdf.setSizePolicy(sizePolicy)
        self.btn_gerar_pdf.setMaximumSize(QSize(197, 30))
        self.btn_gerar_pdf.setFont(font1)
        self.btn_gerar_pdf.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_gerar_pdf.setStyleSheet(u"QPushButton {\n"
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

        self.layout_botoes_tabelas.addWidget(self.btn_gerar_pdf)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layout_botoes_tabelas.addItem(self.verticalSpacer_4)

        self.btn_atualizar_estoque = QPushButton(self.frame_botoes_tabelas)
        self.btn_atualizar_estoque.setObjectName(u"btn_atualizar_estoque")
        sizePolicy.setHeightForWidth(self.btn_atualizar_estoque.sizePolicy().hasHeightForWidth())
        self.btn_atualizar_estoque.setSizePolicy(sizePolicy)
        self.btn_atualizar_estoque.setMaximumSize(QSize(197, 30))
        self.btn_atualizar_estoque.setFont(font1)
        self.btn_atualizar_estoque.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_atualizar_estoque.setStyleSheet(u"QPushButton {\n"
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

        self.layout_botoes_tabelas.addWidget(self.btn_atualizar_estoque)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layout_botoes_tabelas.addItem(self.verticalSpacer_5)

        self.btn_limpar_tabelas = QPushButton(self.frame_botoes_tabelas)
        self.btn_limpar_tabelas.setObjectName(u"btn_limpar_tabelas")
        sizePolicy.setHeightForWidth(self.btn_limpar_tabelas.sizePolicy().hasHeightForWidth())
        self.btn_limpar_tabelas.setSizePolicy(sizePolicy)
        self.btn_limpar_tabelas.setMaximumSize(QSize(197, 30))
        self.btn_limpar_tabelas.setFont(font1)
        self.btn_limpar_tabelas.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_limpar_tabelas.setStyleSheet(u"QPushButton {\n"
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

        self.layout_botoes_tabelas.addWidget(self.btn_limpar_tabelas)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layout_botoes_tabelas.addItem(self.verticalSpacer_6)

        self.btn_incluir_no_sistema = QPushButton(self.frame_botoes_tabelas)
        self.btn_incluir_no_sistema.setObjectName(u"btn_incluir_no_sistema")
        sizePolicy.setHeightForWidth(self.btn_incluir_no_sistema.sizePolicy().hasHeightForWidth())
        self.btn_incluir_no_sistema.setSizePolicy(sizePolicy)
        self.btn_incluir_no_sistema.setMaximumSize(QSize(197, 30))
        self.btn_incluir_no_sistema.setFont(font1)
        self.btn_incluir_no_sistema.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_incluir_no_sistema.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    font-size: 13px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 3px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}\n"
"")

        self.layout_botoes_tabelas.addWidget(self.btn_incluir_no_sistema)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layout_botoes_tabelas.addItem(self.verticalSpacer_7)


        self.gridLayout_14.addLayout(self.layout_botoes_tabelas, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.frame_botoes_tabelas, 0, 4, 5, 1)

        self.frame_tb_saida = QFrame(self.tabela_base)
        self.frame_tb_saida.setObjectName(u"frame_tb_saida")
        sizePolicy.setHeightForWidth(self.frame_tb_saida.sizePolicy().hasHeightForWidth())
        self.frame_tb_saida.setSizePolicy(sizePolicy)
        self.frame_tb_saida.setMaximumSize(QSize(1300, 302))
        self.frame_tb_saida.setFrameShape(QFrame.NoFrame)
        self.frame_tb_saida.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_tb_saida)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.table_saida = QTableWidget(self.frame_tb_saida)
        if (self.table_saida.columnCount() < 10):
            self.table_saida.setColumnCount(10)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        font2 = QFont()
        font2.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2);
        __qtablewidgetitem.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem.setForeground(brush);
        self.table_saida.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font2);
        __qtablewidgetitem1.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem1.setForeground(brush);
        self.table_saida.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font2);
        __qtablewidgetitem2.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem2.setForeground(brush);
        self.table_saida.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font2);
        __qtablewidgetitem3.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem3.setForeground(brush);
        self.table_saida.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font2);
        __qtablewidgetitem4.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem4.setForeground(brush);
        self.table_saida.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font2);
        __qtablewidgetitem5.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem5.setForeground(brush);
        self.table_saida.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font2);
        __qtablewidgetitem6.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem6.setForeground(brush);
        self.table_saida.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font2);
        __qtablewidgetitem7.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem7.setForeground(brush);
        self.table_saida.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font2);
        __qtablewidgetitem8.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem8.setForeground(brush);
        self.table_saida.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font2);
        __qtablewidgetitem9.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem9.setForeground(brush);
        self.table_saida.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.table_saida.setObjectName(u"table_saida")
        self.table_saida.setMinimumSize(QSize(0, 284))
        self.table_saida.setMaximumSize(QSize(1300, 300))
        self.table_saida.setContextMenuPolicy(Qt.NoContextMenu)
        self.table_saida.setLayoutDirection(Qt.LeftToRight)
        self.table_saida.setStyleSheet(u"QTableWidget{\n"
"	border: 2px solid white;\n"
"}")
        self.table_saida.setLocale(QLocale(QLocale.Portuguese, QLocale.Brazil))
        self.table_saida.setFrameShape(QFrame.StyledPanel)
        self.table_saida.setFrameShadow(QFrame.Plain)
        self.table_saida.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.table_saida.setAutoScroll(True)
        self.table_saida.setDragEnabled(False)
        self.table_saida.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.table_saida.setAlternatingRowColors(False)
        self.table_saida.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_saida.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.table_saida.setTextElideMode(Qt.ElideRight)
        self.table_saida.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.table_saida.setGridStyle(Qt.SolidLine)
        self.table_saida.setSortingEnabled(False)
        self.table_saida.setColumnCount(10)
        self.table_saida.horizontalHeader().setVisible(True)
        self.table_saida.horizontalHeader().setCascadingSectionResizes(False)
        self.table_saida.horizontalHeader().setMinimumSectionSize(38)
        self.table_saida.horizontalHeader().setDefaultSectionSize(110)
        self.table_saida.horizontalHeader().setHighlightSections(True)
        self.table_saida.horizontalHeader().setProperty(u"showSortIndicator", True)
        self.table_saida.horizontalHeader().setStretchLastSection(False)
        self.table_saida.verticalHeader().setVisible(True)
        self.table_saida.verticalHeader().setCascadingSectionResizes(False)
        self.table_saida.verticalHeader().setHighlightSections(True)
        self.table_saida.verticalHeader().setProperty(u"showSortIndicator", False)
        self.table_saida.verticalHeader().setStretchLastSection(False)

        self.gridLayout_11.addWidget(self.table_saida, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.frame_tb_saida, 4, 0, 1, 4)

        self.frame_botao_salvar = QFrame(self.tabela_base)
        self.frame_botao_salvar.setObjectName(u"frame_botao_salvar")
        sizePolicy.setHeightForWidth(self.frame_botao_salvar.sizePolicy().hasHeightForWidth())
        self.frame_botao_salvar.setSizePolicy(sizePolicy)
        self.frame_botao_salvar.setMinimumSize(QSize(0, 0))
        self.frame_botao_salvar.setMaximumSize(QSize(44, 49))
        self.frame_botao_salvar.setLayoutDirection(Qt.LeftToRight)
        self.frame_botao_salvar.setFrameShape(QFrame.NoFrame)
        self.frame_botao_salvar.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_botao_salvar)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(10, -1, 9, 14)
        self.btn_salvar_tables = QPushButton(self.frame_botao_salvar)
        self.btn_salvar_tables.setObjectName(u"btn_salvar_tables")
        sizePolicy.setHeightForWidth(self.btn_salvar_tables.sizePolicy().hasHeightForWidth())
        self.btn_salvar_tables.setSizePolicy(sizePolicy)
        self.btn_salvar_tables.setMinimumSize(QSize(33, 40))
        self.btn_salvar_tables.setMaximumSize(QSize(52, 50))
        self.btn_salvar_tables.setStyleSheet(u"QPushButton {\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"Projeto ERP/imagens/Delete-Button-PNG-Download-Image.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_salvar_tables.setIcon(icon)
        self.btn_salvar_tables.setIconSize(QSize(46, 53))

        self.gridLayout_10.addWidget(self.btn_salvar_tables, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.frame_botao_salvar, 3, 1, 1, 1)

        self.frame_estoque = QFrame(self.tabela_base)
        self.frame_estoque.setObjectName(u"frame_estoque")
        sizePolicy.setHeightForWidth(self.frame_estoque.sizePolicy().hasHeightForWidth())
        self.frame_estoque.setSizePolicy(sizePolicy)
        self.frame_estoque.setMaximumSize(QSize(152, 63))
        self.frame_estoque.setFrameShape(QFrame.NoFrame)
        self.frame_estoque.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_estoque)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_estoque = QLabel(self.frame_estoque)
        self.label_estoque.setObjectName(u"label_estoque")
        sizePolicy.setHeightForWidth(self.label_estoque.sizePolicy().hasHeightForWidth())
        self.label_estoque.setSizePolicy(sizePolicy)
        self.label_estoque.setMaximumSize(QSize(134, 41))
        self.label_estoque.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"	border: 3px solid white;\n"
"}\n"
"\n"
"")

        self.gridLayout_9.addWidget(self.label_estoque, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.frame_estoque, 1, 0, 1, 4)

        self.frame_botoes_planilha = QFrame(self.tabela_base)
        self.frame_botoes_planilha.setObjectName(u"frame_botoes_planilha")
        sizePolicy.setHeightForWidth(self.frame_botoes_planilha.sizePolicy().hasHeightForWidth())
        self.frame_botoes_planilha.setSizePolicy(sizePolicy)
        self.frame_botoes_planilha.setMaximumSize(QSize(1300, 400))
        self.frame_botoes_planilha.setFrameShape(QFrame.NoFrame)
        self.frame_botoes_planilha.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_botoes_planilha)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.line_excel = QLineEdit(self.frame_botoes_planilha)
        self.line_excel.setObjectName(u"line_excel")
        sizePolicy.setHeightForWidth(self.line_excel.sizePolicy().hasHeightForWidth())
        self.line_excel.setSizePolicy(sizePolicy)
        self.line_excel.setMaximumSize(QSize(1300, 26))
        self.line_excel.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QLineEdit::placeholderText {\n"
"    color: black; /* Cor do texto do placeholder */\n"
"}\n"
"")
        self.line_excel.setAlignment(Qt.AlignCenter)
        self.line_excel.setReadOnly(False)
        self.line_excel.setPlaceholderText(u"Arquivo em excel aparecer\u00e1 aqui")

        self.verticalLayout_2.addWidget(self.line_excel)

        self.btn_abrir_planilha = QPushButton(self.frame_botoes_planilha)
        self.btn_abrir_planilha.setObjectName(u"btn_abrir_planilha")
        sizePolicy.setHeightForWidth(self.btn_abrir_planilha.sizePolicy().hasHeightForWidth())
        self.btn_abrir_planilha.setSizePolicy(sizePolicy)
        self.btn_abrir_planilha.setMaximumSize(QSize(1300, 26))
        self.btn_abrir_planilha.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_abrir_planilha.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_2.addWidget(self.btn_abrir_planilha)

        self.progress_excel = QProgressBar(self.frame_botoes_planilha)
        self.progress_excel.setObjectName(u"progress_excel")
        sizePolicy.setHeightForWidth(self.progress_excel.sizePolicy().hasHeightForWidth())
        self.progress_excel.setSizePolicy(sizePolicy)
        self.progress_excel.setMaximumSize(QSize(1300, 26))
        self.progress_excel.setStyleSheet(u"QProgressBar {\n"
"    border: 1px solid gray;\n"
"    border-radius: 4px;\n"
"    background-color: white;  /* Define o fundo como branco */\n"
"}\n"
"")
        self.progress_excel.setValue(0)
        self.progress_excel.setAlignment(Qt.AlignCenter)
        self.progress_excel.setTextVisible(True)
        self.progress_excel.setOrientation(Qt.Horizontal)
        self.progress_excel.setTextDirection(QProgressBar.TopToBottom)
        self.progress_excel.setFormat(u"%p%")

        self.verticalLayout_2.addWidget(self.progress_excel)


        self.gridLayout_13.addWidget(self.frame_botoes_planilha, 0, 0, 1, 4)

        self.frame_tb_estoque = QFrame(self.tabela_base)
        self.frame_tb_estoque.setObjectName(u"frame_tb_estoque")
        sizePolicy.setHeightForWidth(self.frame_tb_estoque.sizePolicy().hasHeightForWidth())
        self.frame_tb_estoque.setSizePolicy(sizePolicy)
        self.frame_tb_estoque.setMinimumSize(QSize(0, 281))
        self.frame_tb_estoque.setMaximumSize(QSize(1300, 280))
        self.frame_tb_estoque.setLayoutDirection(Qt.LeftToRight)
        self.frame_tb_estoque.setFrameShape(QFrame.NoFrame)
        self.frame_tb_estoque.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_tb_estoque)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.table_base = QTableWidget(self.frame_tb_estoque)
        if (self.table_base.columnCount() < 9):
            self.table_base.setColumnCount(9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font2);
        __qtablewidgetitem10.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem10.setForeground(brush);
        self.table_base.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font2);
        __qtablewidgetitem11.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem11.setForeground(brush);
        self.table_base.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font2);
        __qtablewidgetitem12.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem12.setForeground(brush);
        self.table_base.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font2);
        __qtablewidgetitem13.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem13.setForeground(brush);
        self.table_base.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font2);
        __qtablewidgetitem14.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem14.setForeground(brush);
        self.table_base.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font2);
        __qtablewidgetitem15.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem15.setForeground(brush);
        self.table_base.setHorizontalHeaderItem(5, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font2);
        __qtablewidgetitem16.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem16.setForeground(brush);
        self.table_base.setHorizontalHeaderItem(6, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font2);
        __qtablewidgetitem17.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem17.setForeground(brush);
        self.table_base.setHorizontalHeaderItem(7, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font2);
        __qtablewidgetitem18.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem18.setForeground(brush);
        self.table_base.setHorizontalHeaderItem(8, __qtablewidgetitem18)
        if (self.table_base.rowCount() < 8):
            self.table_base.setRowCount(8)
        self.table_base.setObjectName(u"table_base")
        self.table_base.setStyleSheet(u"QTableWidget{\n"
"	border: 2px solid white;\n"
"}")
        self.table_base.setFrameShape(QFrame.StyledPanel)
        self.table_base.setFrameShadow(QFrame.Plain)
        self.table_base.setGridStyle(Qt.SolidLine)
        self.table_base.setSortingEnabled(True)
        self.table_base.setWordWrap(True)
        self.table_base.setCornerButtonEnabled(False)
        self.table_base.setRowCount(8)
        self.table_base.horizontalHeader().setDefaultSectionSize(127)
        self.table_base.horizontalHeader().setProperty(u"showSortIndicator", True)

        self.verticalLayout_3.addWidget(self.table_base)


        self.gridLayout_13.addWidget(self.frame_tb_estoque, 2, 0, 1, 4)

        self.tb_base.addTab(self.tabela_base, "")

        self.gridLayout_7.addWidget(self.tb_base, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame_pag_estoque, 0, 0, 1, 1)

        self.paginas_sistemas.addWidget(self.pag_estoque)
        self.page_verificar_usuarios = QWidget()
        self.page_verificar_usuarios.setObjectName(u"page_verificar_usuarios")
        sizePolicy.setHeightForWidth(self.page_verificar_usuarios.sizePolicy().hasHeightForWidth())
        self.page_verificar_usuarios.setSizePolicy(sizePolicy)
        self.gridLayout_15 = QGridLayout(self.page_verificar_usuarios)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.frame_page_verificar_usuarios = QFrame(self.page_verificar_usuarios)
        self.frame_page_verificar_usuarios.setObjectName(u"frame_page_verificar_usuarios")
        self.frame_page_verificar_usuarios.setFrameShape(QFrame.StyledPanel)
        self.frame_page_verificar_usuarios.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.frame_page_verificar_usuarios)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.label_em_desenvolvimento = QLabel(self.frame_page_verificar_usuarios)
        self.label_em_desenvolvimento.setObjectName(u"label_em_desenvolvimento")
        sizePolicy.setHeightForWidth(self.label_em_desenvolvimento.sizePolicy().hasHeightForWidth())
        self.label_em_desenvolvimento.setSizePolicy(sizePolicy)
        self.label_em_desenvolvimento.setMaximumSize(QSize(380, 69))
        self.label_em_desenvolvimento.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"	border: 3px solid white;\n"
"}\n"
"\n"
"")

        self.gridLayout_17.addWidget(self.label_em_desenvolvimento, 0, 0, 1, 1)


        self.gridLayout_15.addWidget(self.frame_page_verificar_usuarios, 0, 0, 1, 1)

        self.paginas_sistemas.addWidget(self.page_verificar_usuarios)
        self.pg_cadastrar_produto = QWidget()
        self.pg_cadastrar_produto.setObjectName(u"pg_cadastrar_produto")
        self.gridLayout_5 = QGridLayout(self.pg_cadastrar_produto)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame_cadastrar_produto = QFrame(self.pg_cadastrar_produto)
        self.frame_cadastrar_produto.setObjectName(u"frame_cadastrar_produto")
        sizePolicy.setHeightForWidth(self.frame_cadastrar_produto.sizePolicy().hasHeightForWidth())
        self.frame_cadastrar_produto.setSizePolicy(sizePolicy)
        self.frame_cadastrar_produto.setLayoutDirection(Qt.LeftToRight)
        self.frame_cadastrar_produto.setFrameShape(QFrame.NoFrame)
        self.frame_cadastrar_produto.setFrameShadow(QFrame.Raised)
        self.gridLayout_26 = QGridLayout(self.frame_cadastrar_produto)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.frame_quantidade = QFrame(self.frame_cadastrar_produto)
        self.frame_quantidade.setObjectName(u"frame_quantidade")
        sizePolicy.setHeightForWidth(self.frame_quantidade.sizePolicy().hasHeightForWidth())
        self.frame_quantidade.setSizePolicy(sizePolicy)
        self.frame_quantidade.setMaximumSize(QSize(321, 101))
        self.frame_quantidade.setStyleSheet(u"background-color: rgb(100, 200, 100); /* Verde claro */\n"
"")
        self.frame_quantidade.setFrameShape(QFrame.NoFrame)
        self.frame_quantidade.setFrameShadow(QFrame.Raised)
        self.label_quantidade_2 = QLabel(self.frame_quantidade)
        self.label_quantidade_2.setObjectName(u"label_quantidade_2")
        self.label_quantidade_2.setGeometry(QRect(40, 10, 240, 19))
        sizePolicy.setHeightForWidth(self.label_quantidade_2.sizePolicy().hasHeightForWidth())
        self.label_quantidade_2.setSizePolicy(sizePolicy)
        self.label_quantidade_2.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.label_quantidade_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_26.addWidget(self.frame_quantidade, 5, 2, 1, 1)

        self.frame_botoes_a_e_a_a = QFrame(self.frame_cadastrar_produto)
        self.frame_botoes_a_e_a_a.setObjectName(u"frame_botoes_a_e_a_a")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_botoes_a_e_a_a.sizePolicy().hasHeightForWidth())
        self.frame_botoes_a_e_a_a.setSizePolicy(sizePolicy2)
        self.frame_botoes_a_e_a_a.setMaximumSize(QSize(150, 16777215))
        self.frame_botoes_a_e_a_a.setFrameShape(QFrame.NoFrame)
        self.frame_botoes_a_e_a_a.setFrameShadow(QFrame.Raised)
        self.frame_botoes_a_e_a_a.setLineWidth(0)
        self.gridLayout_21 = QGridLayout(self.frame_botoes_a_e_a_a)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.layou_botoes_a_e_a_a = QVBoxLayout()
        self.layou_botoes_a_e_a_a.setSpacing(9)
        self.layou_botoes_a_e_a_a.setObjectName(u"layou_botoes_a_e_a_a")
        self.layou_botoes_a_e_a_a.setContentsMargins(1, 1, 1, 0)
        self.btn_adicionar_produto = QPushButton(self.frame_botoes_a_e_a_a)
        self.btn_adicionar_produto.setObjectName(u"btn_adicionar_produto")
        sizePolicy.setHeightForWidth(self.btn_adicionar_produto.sizePolicy().hasHeightForWidth())
        self.btn_adicionar_produto.setSizePolicy(sizePolicy)
        self.btn_adicionar_produto.setMaximumSize(QSize(16777215, 23))
        self.btn_adicionar_produto.setStyleSheet(u"QPushButton {\n"
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
        icon1 = QIcon()
        icon1.addFile(u"OneDrive/\u00c1rea de Trabalho/Python Work/Projeto ERP/Projeto ERP/Projeto ERP/Projeto ERP/Downloads/pngwing.com.png", QSize(), QIcon.Mode.Active, QIcon.State.On)
        self.btn_adicionar_produto.setIcon(icon1)

        self.layou_botoes_a_e_a_a.addWidget(self.btn_adicionar_produto)

        self.btn_editar = QPushButton(self.frame_botoes_a_e_a_a)
        self.btn_editar.setObjectName(u"btn_editar")
        sizePolicy.setHeightForWidth(self.btn_editar.sizePolicy().hasHeightForWidth())
        self.btn_editar.setSizePolicy(sizePolicy)
        self.btn_editar.setMaximumSize(QSize(16777215, 23))
        self.btn_editar.setStyleSheet(u"QPushButton {\n"
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

        self.layou_botoes_a_e_a_a.addWidget(self.btn_editar)

        self.btn_atualizar_produto = QPushButton(self.frame_botoes_a_e_a_a)
        self.btn_atualizar_produto.setObjectName(u"btn_atualizar_produto")
        sizePolicy.setHeightForWidth(self.btn_atualizar_produto.sizePolicy().hasHeightForWidth())
        self.btn_atualizar_produto.setSizePolicy(sizePolicy)
        self.btn_atualizar_produto.setMaximumSize(QSize(16777215, 23))
        self.btn_atualizar_produto.setStyleSheet(u"QPushButton {\n"
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
        icon2 = QIcon()
        icon2.addFile(u"OneDrive/\u00c1rea de Trabalho/Python Work/Projeto ERP/Projeto ERP/Projeto ERP/Projeto ERP/Downloads/toppng.com-update-512x512.png", QSize(), QIcon.Mode.Active, QIcon.State.On)
        self.btn_atualizar_produto.setIcon(icon2)

        self.layou_botoes_a_e_a_a.addWidget(self.btn_atualizar_produto)

        self.btn_limpar_campos = QPushButton(self.frame_botoes_a_e_a_a)
        self.btn_limpar_campos.setObjectName(u"btn_limpar_campos")
        sizePolicy.setHeightForWidth(self.btn_limpar_campos.sizePolicy().hasHeightForWidth())
        self.btn_limpar_campos.setSizePolicy(sizePolicy)
        self.btn_limpar_campos.setMaximumSize(QSize(16777215, 23))
        self.btn_limpar_campos.setMouseTracking(False)
        self.btn_limpar_campos.setAcceptDrops(False)
        self.btn_limpar_campos.setAutoFillBackground(False)
        self.btn_limpar_campos.setStyleSheet(u"QPushButton {\n"
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
        icon3 = QIcon()
        icon3.addFile(u"OneDrive/\u00c1rea de Trabalho/Python Work/Projeto ERP/Projeto ERP/Projeto ERP/Projeto ERP/Downloads/1486564399-close_81512.png", QSize(), QIcon.Mode.Active, QIcon.State.On)
        self.btn_limpar_campos.setIcon(icon3)

        self.layou_botoes_a_e_a_a.addWidget(self.btn_limpar_campos)


        self.gridLayout_21.addLayout(self.layou_botoes_a_e_a_a, 0, 0, 1, 1)


        self.gridLayout_26.addWidget(self.frame_botoes_a_e_a_a, 3, 1, 1, 1)

        self.frame_remover_e_carregar_imagem = QFrame(self.frame_cadastrar_produto)
        self.frame_remover_e_carregar_imagem.setObjectName(u"frame_remover_e_carregar_imagem")
        sizePolicy2.setHeightForWidth(self.frame_remover_e_carregar_imagem.sizePolicy().hasHeightForWidth())
        self.frame_remover_e_carregar_imagem.setSizePolicy(sizePolicy2)
        self.frame_remover_e_carregar_imagem.setMaximumSize(QSize(204, 16777215))
        self.frame_remover_e_carregar_imagem.setFrameShape(QFrame.NoFrame)
        self.frame_remover_e_carregar_imagem.setFrameShadow(QFrame.Raised)
        self.gridLayout_20 = QGridLayout(self.frame_remover_e_carregar_imagem)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.layout_remover_carregar_imagem = QVBoxLayout()
        self.layout_remover_carregar_imagem.setObjectName(u"layout_remover_carregar_imagem")
        self.btn_remover_imagem = QPushButton(self.frame_remover_e_carregar_imagem)
        self.btn_remover_imagem.setObjectName(u"btn_remover_imagem")
        sizePolicy.setHeightForWidth(self.btn_remover_imagem.sizePolicy().hasHeightForWidth())
        self.btn_remover_imagem.setSizePolicy(sizePolicy)
        self.btn_remover_imagem.setMaximumSize(QSize(16777215, 23))
        self.btn_remover_imagem.setMouseTracking(False)
        self.btn_remover_imagem.setAcceptDrops(False)
        self.btn_remover_imagem.setAutoFillBackground(False)
        self.btn_remover_imagem.setStyleSheet(u"QPushButton {\n"
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
        self.btn_remover_imagem.setIcon(icon3)

        self.layout_remover_carregar_imagem.addWidget(self.btn_remover_imagem)

        self.btn_carregar_imagem = QPushButton(self.frame_remover_e_carregar_imagem)
        self.btn_carregar_imagem.setObjectName(u"btn_carregar_imagem")
        sizePolicy.setHeightForWidth(self.btn_carregar_imagem.sizePolicy().hasHeightForWidth())
        self.btn_carregar_imagem.setSizePolicy(sizePolicy)
        self.btn_carregar_imagem.setMaximumSize(QSize(16777215, 23))
        self.btn_carregar_imagem.setStyleSheet(u"QPushButton {\n"
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

        self.layout_remover_carregar_imagem.addWidget(self.btn_carregar_imagem)


        self.gridLayout_20.addLayout(self.layout_remover_carregar_imagem, 0, 0, 1, 1)


        self.gridLayout_26.addWidget(self.frame_remover_e_carregar_imagem, 4, 1, 1, 1)

        self.frame_valor_do_desconto = QFrame(self.frame_cadastrar_produto)
        self.frame_valor_do_desconto.setObjectName(u"frame_valor_do_desconto")
        sizePolicy.setHeightForWidth(self.frame_valor_do_desconto.sizePolicy().hasHeightForWidth())
        self.frame_valor_do_desconto.setSizePolicy(sizePolicy)
        self.frame_valor_do_desconto.setMinimumSize(QSize(0, 101))
        self.frame_valor_do_desconto.setMaximumSize(QSize(321, 101))
        self.frame_valor_do_desconto.setStyleSheet(u"\n"
"background-color: rgb(100, 200, 100); /* Verde claro */\n"
"")
        self.frame_valor_do_desconto.setFrameShape(QFrame.NoFrame)
        self.frame_valor_do_desconto.setFrameShadow(QFrame.Raised)
        self.label_valor_do_desconto = QLabel(self.frame_valor_do_desconto)
        self.label_valor_do_desconto.setObjectName(u"label_valor_do_desconto")
        self.label_valor_do_desconto.setGeometry(QRect(80, 10, 161, 21))
        sizePolicy.setHeightForWidth(self.label_valor_do_desconto.sizePolicy().hasHeightForWidth())
        self.label_valor_do_desconto.setSizePolicy(sizePolicy)
        self.label_valor_do_desconto.setMinimumSize(QSize(34, 0))
        self.label_valor_do_desconto.setMaximumSize(QSize(16777215, 33))
        self.label_valor_do_desconto.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.label_valor_do_desconto.setAlignment(Qt.AlignCenter)

        self.gridLayout_26.addWidget(self.frame_valor_do_desconto, 3, 2, 1, 1)

        self.frame_confirmar_ver_produto = QFrame(self.frame_cadastrar_produto)
        self.frame_confirmar_ver_produto.setObjectName(u"frame_confirmar_ver_produto")
        sizePolicy2.setHeightForWidth(self.frame_confirmar_ver_produto.sizePolicy().hasHeightForWidth())
        self.frame_confirmar_ver_produto.setSizePolicy(sizePolicy2)
        self.frame_confirmar_ver_produto.setMaximumSize(QSize(183, 16777215))
        self.frame_confirmar_ver_produto.setFrameShape(QFrame.NoFrame)
        self.frame_confirmar_ver_produto.setFrameShadow(QFrame.Raised)
        self.gridLayout_19 = QGridLayout(self.frame_confirmar_ver_produto)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.layout_confirmar_ver_produto = QVBoxLayout()
        self.layout_confirmar_ver_produto.setSpacing(5)
        self.layout_confirmar_ver_produto.setObjectName(u"layout_confirmar_ver_produto")
        self.layout_confirmar_ver_produto.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.layout_confirmar_ver_produto.setContentsMargins(0, 0, 2, 0)
        self.btn_confirmar = QPushButton(self.frame_confirmar_ver_produto)
        self.btn_confirmar.setObjectName(u"btn_confirmar")
        sizePolicy.setHeightForWidth(self.btn_confirmar.sizePolicy().hasHeightForWidth())
        self.btn_confirmar.setSizePolicy(sizePolicy)
        self.btn_confirmar.setMaximumSize(QSize(16777215, 23))
        self.btn_confirmar.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255); /* Cor do texto (branco) */\n"
"    border-radius: 3px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 200, 100), stop:1 rgb(150, 255, 150)); /* Gradiente de verde claro para verde mais claro */\n"
"    border: 3px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(150, 255, 150), stop:1 rgb(200, 255, 200)); /* Gradiente de verde mais claro para verde ainda mais claro */\n"
"    color: rgb(0, 0, 0); /* Cor do texto (preto) */\n"
"}\n"
"")

        self.layout_confirmar_ver_produto.addWidget(self.btn_confirmar)

        self.btn_ver_item = QPushButton(self.frame_confirmar_ver_produto)
        self.btn_ver_item.setObjectName(u"btn_ver_item")
        sizePolicy.setHeightForWidth(self.btn_ver_item.sizePolicy().hasHeightForWidth())
        self.btn_ver_item.setSizePolicy(sizePolicy)
        self.btn_ver_item.setMinimumSize(QSize(141, 0))
        self.btn_ver_item.setMaximumSize(QSize(16777215, 23))
        self.btn_ver_item.setStyleSheet(u"QPushButton {\n"
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
        icon4 = QIcon()
        icon4.addFile(u"OneDrive/\u00c1rea de Trabalho/Python Work/Projeto ERP/Projeto ERP/Projeto ERP/Projeto ERP/Downloads/pasta.png", QSize(), QIcon.Mode.Active, QIcon.State.On)
        self.btn_ver_item.setIcon(icon4)

        self.layout_confirmar_ver_produto.addWidget(self.btn_ver_item)


        self.gridLayout_19.addLayout(self.layout_confirmar_ver_produto, 0, 0, 1, 1)


        self.gridLayout_26.addWidget(self.frame_confirmar_ver_produto, 5, 1, 1, 1)

        self.frame_cadastramento_produtos = QFrame(self.frame_cadastrar_produto)
        self.frame_cadastramento_produtos.setObjectName(u"frame_cadastramento_produtos")
        sizePolicy.setHeightForWidth(self.frame_cadastramento_produtos.sizePolicy().hasHeightForWidth())
        self.frame_cadastramento_produtos.setSizePolicy(sizePolicy)
        self.frame_cadastramento_produtos.setMaximumSize(QSize(16777215, 73))
        self.frame_cadastramento_produtos.setFrameShape(QFrame.NoFrame)
        self.frame_cadastramento_produtos.setFrameShadow(QFrame.Raised)
        self.gridLayout_25 = QGridLayout(self.frame_cadastramento_produtos)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.label_cadastramento_produtos = QLabel(self.frame_cadastramento_produtos)
        self.label_cadastramento_produtos.setObjectName(u"label_cadastramento_produtos")
        sizePolicy.setHeightForWidth(self.label_cadastramento_produtos.sizePolicy().hasHeightForWidth())
        self.label_cadastramento_produtos.setSizePolicy(sizePolicy)
        self.label_cadastramento_produtos.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"	border: 5px solid white;\n"
"}\n"
"\n"
"")

        self.gridLayout_25.addWidget(self.label_cadastramento_produtos, 0, 0, 1, 1)


        self.gridLayout_26.addWidget(self.frame_cadastramento_produtos, 0, 0, 1, 4)

        self.frame_valor_com_desconto1 = QFrame(self.frame_cadastrar_produto)
        self.frame_valor_com_desconto1.setObjectName(u"frame_valor_com_desconto1")
        sizePolicy.setHeightForWidth(self.frame_valor_com_desconto1.sizePolicy().hasHeightForWidth())
        self.frame_valor_com_desconto1.setSizePolicy(sizePolicy)
        self.frame_valor_com_desconto1.setMinimumSize(QSize(0, 101))
        self.frame_valor_com_desconto1.setMaximumSize(QSize(321, 101))
        self.frame_valor_com_desconto1.setStyleSheet(u"background-color: rgb(100, 200, 100); /* Verde claro */\n"
"")
        self.frame_valor_com_desconto1.setFrameShape(QFrame.NoFrame)
        self.frame_valor_com_desconto1.setFrameShadow(QFrame.Raised)
        self.label_valor_com_desconto = QLabel(self.frame_valor_com_desconto1)
        self.label_valor_com_desconto.setObjectName(u"label_valor_com_desconto")
        self.label_valor_com_desconto.setGeometry(QRect(31, 14, 261, 19))
        sizePolicy.setHeightForWidth(self.label_valor_com_desconto.sizePolicy().hasHeightForWidth())
        self.label_valor_com_desconto.setSizePolicy(sizePolicy)
        self.label_valor_com_desconto.setMaximumSize(QSize(16777215, 36))
        self.label_valor_com_desconto.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.label_valor_com_desconto.setAlignment(Qt.AlignCenter)

        self.gridLayout_26.addWidget(self.frame_valor_com_desconto1, 4, 2, 1, 1)

        self.frame_valor_total_produtos = QFrame(self.frame_cadastrar_produto)
        self.frame_valor_total_produtos.setObjectName(u"frame_valor_total_produtos")
        sizePolicy.setHeightForWidth(self.frame_valor_total_produtos.sizePolicy().hasHeightForWidth())
        self.frame_valor_total_produtos.setSizePolicy(sizePolicy)
        self.frame_valor_total_produtos.setMaximumSize(QSize(321, 102))
        self.frame_valor_total_produtos.setStyleSheet(u"background-color: rgb(100, 200, 100); /* Verde claro */\n"
"")
        self.frame_valor_total_produtos.setFrameShape(QFrame.NoFrame)
        self.frame_valor_total_produtos.setFrameShadow(QFrame.Raised)
        self.label_valor_total_produtos_2 = QLabel(self.frame_valor_total_produtos)
        self.label_valor_total_produtos_2.setObjectName(u"label_valor_total_produtos_2")
        self.label_valor_total_produtos_2.setGeometry(QRect(18, 9, 285, 18))
        sizePolicy.setHeightForWidth(self.label_valor_total_produtos_2.sizePolicy().hasHeightForWidth())
        self.label_valor_total_produtos_2.setSizePolicy(sizePolicy)
        self.label_valor_total_produtos_2.setMinimumSize(QSize(285, 0))
        self.label_valor_total_produtos_2.setMaximumSize(QSize(284, 30))
        self.label_valor_total_produtos_2.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.label_valor_total_produtos_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_26.addWidget(self.frame_valor_total_produtos, 2, 2, 1, 1)

        self.frame_imagem_produto_3 = QFrame(self.frame_cadastrar_produto)
        self.frame_imagem_produto_3.setObjectName(u"frame_imagem_produto_3")
        sizePolicy.setHeightForWidth(self.frame_imagem_produto_3.sizePolicy().hasHeightForWidth())
        self.frame_imagem_produto_3.setSizePolicy(sizePolicy)
        self.frame_imagem_produto_3.setMaximumSize(QSize(321, 331))
        self.frame_imagem_produto_3.setLayoutDirection(Qt.RightToLeft)
        self.frame_imagem_produto_3.setFrameShape(QFrame.NoFrame)
        self.frame_imagem_produto_3.setFrameShadow(QFrame.Raised)

        self.gridLayout_26.addWidget(self.frame_imagem_produto_3, 1, 4, 8, 1)

        self.frame_txts_labels = QFrame(self.frame_cadastrar_produto)
        self.frame_txts_labels.setObjectName(u"frame_txts_labels")
        sizePolicy.setHeightForWidth(self.frame_txts_labels.sizePolicy().hasHeightForWidth())
        self.frame_txts_labels.setSizePolicy(sizePolicy)
        self.frame_txts_labels.setMinimumSize(QSize(380, 0))
        self.frame_txts_labels.setMaximumSize(QSize(421, 16777215))
        self.frame_txts_labels.setFrameShape(QFrame.NoFrame)
        self.frame_txts_labels.setFrameShadow(QFrame.Raised)
        self.gridLayout_18 = QGridLayout(self.frame_txts_labels)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.frame_produto = QFrame(self.frame_txts_labels)
        self.frame_produto.setObjectName(u"frame_produto")
        sizePolicy.setHeightForWidth(self.frame_produto.sizePolicy().hasHeightForWidth())
        self.frame_produto.setSizePolicy(sizePolicy)
        self.frame_produto.setFrameShape(QFrame.NoFrame)
        self.frame_produto.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_produto)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.layout_produto = QHBoxLayout()
        self.layout_produto.setObjectName(u"layout_produto")
        self.label_produto = QLabel(self.frame_produto)
        self.label_produto.setObjectName(u"label_produto")
        sizePolicy.setHeightForWidth(self.label_produto.sizePolicy().hasHeightForWidth())
        self.label_produto.setSizePolicy(sizePolicy)
        self.label_produto.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.layout_produto.addWidget(self.label_produto)

        self.txt_produto = QLineEdit(self.frame_produto)
        self.txt_produto.setObjectName(u"txt_produto")
        sizePolicy.setHeightForWidth(self.txt_produto.sizePolicy().hasHeightForWidth())
        self.txt_produto.setSizePolicy(sizePolicy)
        self.txt_produto.setMaximumSize(QSize(16777215, 30))
        self.txt_produto.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")

        self.layout_produto.addWidget(self.txt_produto)

        self.frame_erro_produto = QFrame(self.frame_produto)
        self.frame_erro_produto.setObjectName(u"frame_erro_produto")
        sizePolicy.setHeightForWidth(self.frame_erro_produto.sizePolicy().hasHeightForWidth())
        self.frame_erro_produto.setSizePolicy(sizePolicy)
        self.frame_erro_produto.setMaximumSize(QSize(21, 21))
        self.frame_erro_produto.setFrameShape(QFrame.NoFrame)
        self.frame_erro_produto.setFrameShadow(QFrame.Raised)

        self.layout_produto.addWidget(self.frame_erro_produto)


        self.horizontalLayout_5.addLayout(self.layout_produto)


        self.gridLayout_18.addWidget(self.frame_produto, 0, 0, 1, 1)

        self.frame_quantidade_2 = QFrame(self.frame_txts_labels)
        self.frame_quantidade_2.setObjectName(u"frame_quantidade_2")
        sizePolicy.setHeightForWidth(self.frame_quantidade_2.sizePolicy().hasHeightForWidth())
        self.frame_quantidade_2.setSizePolicy(sizePolicy)
        self.frame_quantidade_2.setFrameShape(QFrame.NoFrame)
        self.frame_quantidade_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_quantidade_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.layout_quantidade = QHBoxLayout()
        self.layout_quantidade.setObjectName(u"layout_quantidade")
        self.label_quantidade = QLabel(self.frame_quantidade_2)
        self.label_quantidade.setObjectName(u"label_quantidade")
        sizePolicy.setHeightForWidth(self.label_quantidade.sizePolicy().hasHeightForWidth())
        self.label_quantidade.setSizePolicy(sizePolicy)
        self.label_quantidade.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.layout_quantidade.addWidget(self.label_quantidade)

        self.txt_quantidade = QLineEdit(self.frame_quantidade_2)
        self.txt_quantidade.setObjectName(u"txt_quantidade")
        sizePolicy.setHeightForWidth(self.txt_quantidade.sizePolicy().hasHeightForWidth())
        self.txt_quantidade.setSizePolicy(sizePolicy)
        self.txt_quantidade.setMaximumSize(QSize(16777215, 30))
        self.txt_quantidade.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")

        self.layout_quantidade.addWidget(self.txt_quantidade)

        self.frame_erro_quantidade = QFrame(self.frame_quantidade_2)
        self.frame_erro_quantidade.setObjectName(u"frame_erro_quantidade")
        sizePolicy.setHeightForWidth(self.frame_erro_quantidade.sizePolicy().hasHeightForWidth())
        self.frame_erro_quantidade.setSizePolicy(sizePolicy)
        self.frame_erro_quantidade.setMaximumSize(QSize(21, 21))
        self.frame_erro_quantidade.setFrameShape(QFrame.NoFrame)
        self.frame_erro_quantidade.setFrameShadow(QFrame.Raised)

        self.layout_quantidade.addWidget(self.frame_erro_quantidade)


        self.horizontalLayout_4.addLayout(self.layout_quantidade)


        self.gridLayout_18.addWidget(self.frame_quantidade_2, 1, 0, 1, 1)

        self.frame_valor_produto = QFrame(self.frame_txts_labels)
        self.frame_valor_produto.setObjectName(u"frame_valor_produto")
        sizePolicy.setHeightForWidth(self.frame_valor_produto.sizePolicy().hasHeightForWidth())
        self.frame_valor_produto.setSizePolicy(sizePolicy)
        self.frame_valor_produto.setFrameShape(QFrame.NoFrame)
        self.frame_valor_produto.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_valor_produto)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.layout_valor_produto = QHBoxLayout()
        self.layout_valor_produto.setObjectName(u"layout_valor_produto")
        self.label_valor_produto_3 = QLabel(self.frame_valor_produto)
        self.label_valor_produto_3.setObjectName(u"label_valor_produto_3")
        sizePolicy.setHeightForWidth(self.label_valor_produto_3.sizePolicy().hasHeightForWidth())
        self.label_valor_produto_3.setSizePolicy(sizePolicy)
        self.label_valor_produto_3.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.layout_valor_produto.addWidget(self.label_valor_produto_3)

        self.txt_valor_produto_3 = QLineEdit(self.frame_valor_produto)
        self.txt_valor_produto_3.setObjectName(u"txt_valor_produto_3")
        sizePolicy.setHeightForWidth(self.txt_valor_produto_3.sizePolicy().hasHeightForWidth())
        self.txt_valor_produto_3.setSizePolicy(sizePolicy)
        self.txt_valor_produto_3.setMaximumSize(QSize(16777215, 30))
        self.txt_valor_produto_3.setContextMenuPolicy(Qt.NoContextMenu)
        self.txt_valor_produto_3.setAutoFillBackground(False)
        self.txt_valor_produto_3.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")
        self.txt_valor_produto_3.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.txt_valor_produto_3.setClearButtonEnabled(False)

        self.layout_valor_produto.addWidget(self.txt_valor_produto_3)

        self.frame_erro_valor_produto = QFrame(self.frame_valor_produto)
        self.frame_erro_valor_produto.setObjectName(u"frame_erro_valor_produto")
        sizePolicy.setHeightForWidth(self.frame_erro_valor_produto.sizePolicy().hasHeightForWidth())
        self.frame_erro_valor_produto.setSizePolicy(sizePolicy)
        self.frame_erro_valor_produto.setMaximumSize(QSize(21, 21))
        self.frame_erro_valor_produto.setFrameShape(QFrame.NoFrame)
        self.frame_erro_valor_produto.setFrameShadow(QFrame.Raised)

        self.layout_valor_produto.addWidget(self.frame_erro_valor_produto)


        self.horizontalLayout_3.addLayout(self.layout_valor_produto)


        self.gridLayout_18.addWidget(self.frame_valor_produto, 2, 0, 1, 1)

        self.frame_desconto = QFrame(self.frame_txts_labels)
        self.frame_desconto.setObjectName(u"frame_desconto")
        sizePolicy.setHeightForWidth(self.frame_desconto.sizePolicy().hasHeightForWidth())
        self.frame_desconto.setSizePolicy(sizePolicy)
        self.frame_desconto.setFrameShape(QFrame.NoFrame)
        self.frame_desconto.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_desconto)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.layout_desconto = QHBoxLayout()
        self.layout_desconto.setObjectName(u"layout_desconto")
        self.layout_desconto.setContentsMargins(0, 0, -1, 0)
        self.label_desconto_3 = QLabel(self.frame_desconto)
        self.label_desconto_3.setObjectName(u"label_desconto_3")
        sizePolicy.setHeightForWidth(self.label_desconto_3.sizePolicy().hasHeightForWidth())
        self.label_desconto_3.setSizePolicy(sizePolicy)
        self.label_desconto_3.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.layout_desconto.addWidget(self.label_desconto_3)

        self.txt_desconto_3 = QLineEdit(self.frame_desconto)
        self.txt_desconto_3.setObjectName(u"txt_desconto_3")
        sizePolicy.setHeightForWidth(self.txt_desconto_3.sizePolicy().hasHeightForWidth())
        self.txt_desconto_3.setSizePolicy(sizePolicy)
        self.txt_desconto_3.setMaximumSize(QSize(16777215, 30))
        self.txt_desconto_3.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")

        self.layout_desconto.addWidget(self.txt_desconto_3)


        self.horizontalLayout_2.addLayout(self.layout_desconto)


        self.gridLayout_18.addWidget(self.frame_desconto, 3, 0, 1, 1)

        self.frame_data_compra = QFrame(self.frame_txts_labels)
        self.frame_data_compra.setObjectName(u"frame_data_compra")
        sizePolicy.setHeightForWidth(self.frame_data_compra.sizePolicy().hasHeightForWidth())
        self.frame_data_compra.setSizePolicy(sizePolicy)
        self.frame_data_compra.setFrameShape(QFrame.NoFrame)
        self.frame_data_compra.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_data_compra)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.layout_data_compra = QHBoxLayout()
        self.layout_data_compra.setObjectName(u"layout_data_compra")
        self.label_data_compra_3 = QLabel(self.frame_data_compra)
        self.label_data_compra_3.setObjectName(u"label_data_compra_3")
        sizePolicy.setHeightForWidth(self.label_data_compra_3.sizePolicy().hasHeightForWidth())
        self.label_data_compra_3.setSizePolicy(sizePolicy)
        self.label_data_compra_3.setMaximumSize(QSize(16777215, 16))
        self.label_data_compra_3.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.layout_data_compra.addWidget(self.label_data_compra_3)

        self.dateEdit_3 = QDateEdit(self.frame_data_compra)
        self.dateEdit_3.setObjectName(u"dateEdit_3")
        sizePolicy.setHeightForWidth(self.dateEdit_3.sizePolicy().hasHeightForWidth())
        self.dateEdit_3.setSizePolicy(sizePolicy)
        self.dateEdit_3.setMaximumSize(QSize(16777215, 30))
        self.dateEdit_3.setStyleSheet(u"QDateEdit {\n"
"    color: #333; /* Cor do texto */\n"
"    background-color: white; /* Cor de fundo */\n"
"}\n"
"")
        self.dateEdit_3.setInputMethodHints(Qt.ImhPreferNumbers)
        self.dateEdit_3.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.dateEdit_3.setAccelerated(False)
        self.dateEdit_3.setProperty(u"showGroupSeparator", False)
        self.dateEdit_3.setMinimumDate(QDate(1900, 9, 14))
        self.dateEdit_3.setCurrentSection(QDateTimeEdit.DaySection)
        self.dateEdit_3.setCalendarPopup(True)
        self.dateEdit_3.setCurrentSectionIndex(0)
        self.dateEdit_3.setTimeSpec(Qt.UTC)

        self.layout_data_compra.addWidget(self.dateEdit_3)

        self.frame_erro_data_compra = QFrame(self.frame_data_compra)
        self.frame_erro_data_compra.setObjectName(u"frame_erro_data_compra")
        sizePolicy.setHeightForWidth(self.frame_erro_data_compra.sizePolicy().hasHeightForWidth())
        self.frame_erro_data_compra.setSizePolicy(sizePolicy)
        self.frame_erro_data_compra.setMaximumSize(QSize(21, 21))
        self.frame_erro_data_compra.setFrameShape(QFrame.NoFrame)
        self.frame_erro_data_compra.setFrameShadow(QFrame.Raised)

        self.layout_data_compra.addWidget(self.frame_erro_data_compra)


        self.horizontalLayout.addLayout(self.layout_data_compra)


        self.gridLayout_18.addWidget(self.frame_data_compra, 4, 0, 1, 1)

        self.frame_codigo_item = QFrame(self.frame_txts_labels)
        self.frame_codigo_item.setObjectName(u"frame_codigo_item")
        sizePolicy.setHeightForWidth(self.frame_codigo_item.sizePolicy().hasHeightForWidth())
        self.frame_codigo_item.setSizePolicy(sizePolicy)
        self.frame_codigo_item.setFrameShape(QFrame.NoFrame)
        self.frame_codigo_item.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_codigo_item)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_codigo_item_3 = QLabel(self.frame_codigo_item)
        self.label_codigo_item_3.setObjectName(u"label_codigo_item_3")
        sizePolicy.setHeightForWidth(self.label_codigo_item_3.sizePolicy().hasHeightForWidth())
        self.label_codigo_item_3.setSizePolicy(sizePolicy)
        self.label_codigo_item_3.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.horizontalLayout_9.addWidget(self.label_codigo_item_3)

        self.txt_codigo_item = QLineEdit(self.frame_codigo_item)
        self.txt_codigo_item.setObjectName(u"txt_codigo_item")
        sizePolicy.setHeightForWidth(self.txt_codigo_item.sizePolicy().hasHeightForWidth())
        self.txt_codigo_item.setSizePolicy(sizePolicy)
        self.txt_codigo_item.setMaximumSize(QSize(16777215, 30))
        self.txt_codigo_item.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")

        self.horizontalLayout_9.addWidget(self.txt_codigo_item)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_9)


        self.gridLayout_18.addWidget(self.frame_codigo_item, 5, 0, 1, 1)

        self.frame_cliente = QFrame(self.frame_txts_labels)
        self.frame_cliente.setObjectName(u"frame_cliente")
        sizePolicy.setHeightForWidth(self.frame_cliente.sizePolicy().hasHeightForWidth())
        self.frame_cliente.setSizePolicy(sizePolicy)
        self.frame_cliente.setFrameShape(QFrame.NoFrame)
        self.frame_cliente.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_cliente)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.layout_cliente = QHBoxLayout()
        self.layout_cliente.setObjectName(u"layout_cliente")
        self.label_cliente_4 = QLabel(self.frame_cliente)
        self.label_cliente_4.setObjectName(u"label_cliente_4")
        sizePolicy.setHeightForWidth(self.label_cliente_4.sizePolicy().hasHeightForWidth())
        self.label_cliente_4.setSizePolicy(sizePolicy)
        self.label_cliente_4.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.layout_cliente.addWidget(self.label_cliente_4)

        self.txt_cliente_3 = QLineEdit(self.frame_cliente)
        self.txt_cliente_3.setObjectName(u"txt_cliente_3")
        sizePolicy.setHeightForWidth(self.txt_cliente_3.sizePolicy().hasHeightForWidth())
        self.txt_cliente_3.setSizePolicy(sizePolicy)
        self.txt_cliente_3.setMaximumSize(QSize(16777215, 30))
        self.txt_cliente_3.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")

        self.layout_cliente.addWidget(self.txt_cliente_3)

        self.frame_erro_cliente = QFrame(self.frame_cliente)
        self.frame_erro_cliente.setObjectName(u"frame_erro_cliente")
        sizePolicy.setHeightForWidth(self.frame_erro_cliente.sizePolicy().hasHeightForWidth())
        self.frame_erro_cliente.setSizePolicy(sizePolicy)
        self.frame_erro_cliente.setMaximumSize(QSize(21, 21))
        self.frame_erro_cliente.setFrameShape(QFrame.NoFrame)
        self.frame_erro_cliente.setFrameShadow(QFrame.Raised)

        self.layout_cliente.addWidget(self.frame_erro_cliente)


        self.horizontalLayout_7.addLayout(self.layout_cliente)


        self.gridLayout_18.addWidget(self.frame_cliente, 6, 0, 1, 1)

        self.frame_descricao_produto = QFrame(self.frame_txts_labels)
        self.frame_descricao_produto.setObjectName(u"frame_descricao_produto")
        sizePolicy.setHeightForWidth(self.frame_descricao_produto.sizePolicy().hasHeightForWidth())
        self.frame_descricao_produto.setSizePolicy(sizePolicy)
        self.frame_descricao_produto.setMaximumSize(QSize(16777212, 16777215))
        self.frame_descricao_produto.setFrameShape(QFrame.NoFrame)
        self.frame_descricao_produto.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_descricao_produto)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.layout_descricao_produto = QHBoxLayout()
        self.layout_descricao_produto.setObjectName(u"layout_descricao_produto")
        self.label_descricao_produto_3 = QLabel(self.frame_descricao_produto)
        self.label_descricao_produto_3.setObjectName(u"label_descricao_produto_3")
        sizePolicy.setHeightForWidth(self.label_descricao_produto_3.sizePolicy().hasHeightForWidth())
        self.label_descricao_produto_3.setSizePolicy(sizePolicy)
        self.label_descricao_produto_3.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.layout_descricao_produto.addWidget(self.label_descricao_produto_3)

        self.txt_descricao_produto_3 = QLineEdit(self.frame_descricao_produto)
        self.txt_descricao_produto_3.setObjectName(u"txt_descricao_produto_3")
        sizePolicy.setHeightForWidth(self.txt_descricao_produto_3.sizePolicy().hasHeightForWidth())
        self.txt_descricao_produto_3.setSizePolicy(sizePolicy)
        self.txt_descricao_produto_3.setMaximumSize(QSize(16777215, 30))
        self.txt_descricao_produto_3.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")

        self.layout_descricao_produto.addWidget(self.txt_descricao_produto_3)

        self.frame_erro_descricao = QFrame(self.frame_descricao_produto)
        self.frame_erro_descricao.setObjectName(u"frame_erro_descricao")
        sizePolicy.setHeightForWidth(self.frame_erro_descricao.sizePolicy().hasHeightForWidth())
        self.frame_erro_descricao.setSizePolicy(sizePolicy)
        self.frame_erro_descricao.setMaximumSize(QSize(21, 21))
        self.frame_erro_descricao.setFrameShape(QFrame.NoFrame)
        self.frame_erro_descricao.setFrameShadow(QFrame.Raised)

        self.layout_descricao_produto.addWidget(self.frame_erro_descricao)


        self.horizontalLayout_6.addLayout(self.layout_descricao_produto)


        self.gridLayout_18.addWidget(self.frame_descricao_produto, 7, 0, 1, 1)


        self.gridLayout_26.addWidget(self.frame_txts_labels, 1, 0, 8, 1)


        self.gridLayout_5.addWidget(self.frame_cadastrar_produto, 0, 0, 1, 1)

        self.paginas_sistemas.addWidget(self.pg_cadastrar_produto)
        self.pg_cadastrar_usuario = QWidget()
        self.pg_cadastrar_usuario.setObjectName(u"pg_cadastrar_usuario")
        self.gridLayout_34 = QGridLayout(self.pg_cadastrar_usuario)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.frame_pag_cadastrar_usuario = QFrame(self.pg_cadastrar_usuario)
        self.frame_pag_cadastrar_usuario.setObjectName(u"frame_pag_cadastrar_usuario")
        sizePolicy.setHeightForWidth(self.frame_pag_cadastrar_usuario.sizePolicy().hasHeightForWidth())
        self.frame_pag_cadastrar_usuario.setSizePolicy(sizePolicy)
        self.frame_pag_cadastrar_usuario.setFrameShape(QFrame.StyledPanel)
        self.frame_pag_cadastrar_usuario.setFrameShadow(QFrame.Raised)
        self.gridLayout_37 = QGridLayout(self.frame_pag_cadastrar_usuario)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.frame_cadastramento_usuario = QFrame(self.frame_pag_cadastrar_usuario)
        self.frame_cadastramento_usuario.setObjectName(u"frame_cadastramento_usuario")
        sizePolicy.setHeightForWidth(self.frame_cadastramento_usuario.sizePolicy().hasHeightForWidth())
        self.frame_cadastramento_usuario.setSizePolicy(sizePolicy)
        self.frame_cadastramento_usuario.setMinimumSize(QSize(0, 0))
        self.frame_cadastramento_usuario.setMaximumSize(QSize(1200, 70))
        self.frame_cadastramento_usuario.setLayoutDirection(Qt.LeftToRight)
        self.frame_cadastramento_usuario.setFrameShape(QFrame.NoFrame)
        self.frame_cadastramento_usuario.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_cadastramento_usuario)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_cadastramento = QLabel(self.frame_cadastramento_usuario)
        self.label_cadastramento.setObjectName(u"label_cadastramento")
        sizePolicy.setHeightForWidth(self.label_cadastramento.sizePolicy().hasHeightForWidth())
        self.label_cadastramento.setSizePolicy(sizePolicy)
        self.label_cadastramento.setMinimumSize(QSize(0, 42))
        self.label_cadastramento.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"	border: 5px solid white;\n"
"}\n"
"\n"
"")

        self.verticalLayout_6.addWidget(self.label_cadastramento)


        self.gridLayout_37.addWidget(self.frame_cadastramento_usuario, 0, 1, 1, 1)

        self.frames_txts_labels_usuarios = QFrame(self.frame_pag_cadastrar_usuario)
        self.frames_txts_labels_usuarios.setObjectName(u"frames_txts_labels_usuarios")
        sizePolicy.setHeightForWidth(self.frames_txts_labels_usuarios.sizePolicy().hasHeightForWidth())
        self.frames_txts_labels_usuarios.setSizePolicy(sizePolicy)
        self.frames_txts_labels_usuarios.setMinimumSize(QSize(0, 0))
        self.frames_txts_labels_usuarios.setMaximumSize(QSize(16777215, 16777215))
        self.frames_txts_labels_usuarios.setFrameShape(QFrame.NoFrame)
        self.frames_txts_labels_usuarios.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frames_txts_labels_usuarios)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_nome = QFrame(self.frames_txts_labels_usuarios)
        self.frame_nome.setObjectName(u"frame_nome")
        sizePolicy.setHeightForWidth(self.frame_nome.sizePolicy().hasHeightForWidth())
        self.frame_nome.setSizePolicy(sizePolicy)
        self.frame_nome.setMinimumSize(QSize(0, 60))
        self.frame_nome.setMaximumSize(QSize(16777215, 16777215))
        self.frame_nome.setFrameShape(QFrame.NoFrame)
        self.frame_nome.setFrameShadow(QFrame.Raised)
        self.gridLayout_50 = QGridLayout(self.frame_nome)
        self.gridLayout_50.setObjectName(u"gridLayout_50")
        self.layout_nome = QHBoxLayout()
        self.layout_nome.setObjectName(u"layout_nome")
        self.layout_nome.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.layout_nome.setContentsMargins(1, 0, 2, 1)
        self.label_nome = QLabel(self.frame_nome)
        self.label_nome.setObjectName(u"label_nome")
        sizePolicy.setHeightForWidth(self.label_nome.sizePolicy().hasHeightForWidth())
        self.label_nome.setSizePolicy(sizePolicy)
        self.label_nome.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.layout_nome.addWidget(self.label_nome)

        self.txt_nome = QLineEdit(self.frame_nome)
        self.txt_nome.setObjectName(u"txt_nome")
        sizePolicy.setHeightForWidth(self.txt_nome.sizePolicy().hasHeightForWidth())
        self.txt_nome.setSizePolicy(sizePolicy)
        self.txt_nome.setMinimumSize(QSize(0, 24))
        self.txt_nome.setMaximumSize(QSize(16777215, 28))
        self.txt_nome.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")

        self.layout_nome.addWidget(self.txt_nome)


        self.gridLayout_50.addLayout(self.layout_nome, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_nome)

        self.frame_usuario = QFrame(self.frames_txts_labels_usuarios)
        self.frame_usuario.setObjectName(u"frame_usuario")
        sizePolicy.setHeightForWidth(self.frame_usuario.sizePolicy().hasHeightForWidth())
        self.frame_usuario.setSizePolicy(sizePolicy)
        self.frame_usuario.setMinimumSize(QSize(0, 60))
        self.frame_usuario.setMaximumSize(QSize(16777215, 16777215))
        self.frame_usuario.setFrameShape(QFrame.NoFrame)
        self.frame_usuario.setFrameShadow(QFrame.Raised)
        self.gridLayout_49 = QGridLayout(self.frame_usuario)
        self.gridLayout_49.setObjectName(u"gridLayout_49")
        self.layout_usuario = QHBoxLayout()
        self.layout_usuario.setObjectName(u"layout_usuario")
        self.label_usuario = QLabel(self.frame_usuario)
        self.label_usuario.setObjectName(u"label_usuario")
        sizePolicy.setHeightForWidth(self.label_usuario.sizePolicy().hasHeightForWidth())
        self.label_usuario.setSizePolicy(sizePolicy)
        self.label_usuario.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.layout_usuario.addWidget(self.label_usuario)

        self.txt_usuario = QLineEdit(self.frame_usuario)
        self.txt_usuario.setObjectName(u"txt_usuario")
        sizePolicy.setHeightForWidth(self.txt_usuario.sizePolicy().hasHeightForWidth())
        self.txt_usuario.setSizePolicy(sizePolicy)
        self.txt_usuario.setMinimumSize(QSize(0, 24))
        self.txt_usuario.setMaximumSize(QSize(16777215, 28))
        self.txt_usuario.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")

        self.layout_usuario.addWidget(self.txt_usuario)


        self.gridLayout_49.addLayout(self.layout_usuario, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_usuario)

        self.frame_telefone = QFrame(self.frames_txts_labels_usuarios)
        self.frame_telefone.setObjectName(u"frame_telefone")
        sizePolicy.setHeightForWidth(self.frame_telefone.sizePolicy().hasHeightForWidth())
        self.frame_telefone.setSizePolicy(sizePolicy)
        self.frame_telefone.setMinimumSize(QSize(0, 60))
        self.frame_telefone.setMaximumSize(QSize(16777215, 16777215))
        self.frame_telefone.setFrameShape(QFrame.NoFrame)
        self.frame_telefone.setFrameShadow(QFrame.Raised)
        self.gridLayout_48 = QGridLayout(self.frame_telefone)
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.layout_telefone = QHBoxLayout()
        self.layout_telefone.setObjectName(u"layout_telefone")
        self.layout_telefone.setContentsMargins(-1, 0, 0, -1)
        self.label_telefone = QLabel(self.frame_telefone)
        self.label_telefone.setObjectName(u"label_telefone")
        sizePolicy.setHeightForWidth(self.label_telefone.sizePolicy().hasHeightForWidth())
        self.label_telefone.setSizePolicy(sizePolicy)
        self.label_telefone.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.layout_telefone.addWidget(self.label_telefone)

        self.txt_telefone = QLineEdit(self.frame_telefone)
        self.txt_telefone.setObjectName(u"txt_telefone")
        sizePolicy.setHeightForWidth(self.txt_telefone.sizePolicy().hasHeightForWidth())
        self.txt_telefone.setSizePolicy(sizePolicy)
        self.txt_telefone.setMinimumSize(QSize(0, 24))
        self.txt_telefone.setMaximumSize(QSize(16777215, 28))
        self.txt_telefone.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")

        self.layout_telefone.addWidget(self.txt_telefone)


        self.gridLayout_48.addLayout(self.layout_telefone, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_telefone)

        self.frame_endereco = QFrame(self.frames_txts_labels_usuarios)
        self.frame_endereco.setObjectName(u"frame_endereco")
        sizePolicy.setHeightForWidth(self.frame_endereco.sizePolicy().hasHeightForWidth())
        self.frame_endereco.setSizePolicy(sizePolicy)
        self.frame_endereco.setMinimumSize(QSize(0, 60))
        self.frame_endereco.setMaximumSize(QSize(16777215, 16777215))
        self.frame_endereco.setFrameShape(QFrame.NoFrame)
        self.frame_endereco.setFrameShadow(QFrame.Raised)
        self.gridLayout_47 = QGridLayout(self.frame_endereco)
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.layout_endereco = QHBoxLayout()
        self.layout_endereco.setObjectName(u"layout_endereco")
        self.label_endereco = QLabel(self.frame_endereco)
        self.label_endereco.setObjectName(u"label_endereco")
        sizePolicy.setHeightForWidth(self.label_endereco.sizePolicy().hasHeightForWidth())
        self.label_endereco.setSizePolicy(sizePolicy)
        self.label_endereco.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.layout_endereco.addWidget(self.label_endereco)

        self.txt_endereco = QLineEdit(self.frame_endereco)
        self.txt_endereco.setObjectName(u"txt_endereco")
        sizePolicy.setHeightForWidth(self.txt_endereco.sizePolicy().hasHeightForWidth())
        self.txt_endereco.setSizePolicy(sizePolicy)
        self.txt_endereco.setMinimumSize(QSize(0, 24))
        self.txt_endereco.setMaximumSize(QSize(16777215, 28))
        self.txt_endereco.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")

        self.layout_endereco.addWidget(self.txt_endereco)


        self.gridLayout_47.addLayout(self.layout_endereco, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_endereco)

        self.frame_numero = QFrame(self.frames_txts_labels_usuarios)
        self.frame_numero.setObjectName(u"frame_numero")
        sizePolicy.setHeightForWidth(self.frame_numero.sizePolicy().hasHeightForWidth())
        self.frame_numero.setSizePolicy(sizePolicy)
        self.frame_numero.setMinimumSize(QSize(0, 60))
        self.frame_numero.setMaximumSize(QSize(16777215, 16777215))
        self.frame_numero.setFrameShape(QFrame.NoFrame)
        self.frame_numero.setFrameShadow(QFrame.Raised)
        self.gridLayout_46 = QGridLayout(self.frame_numero)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.layout_numero = QHBoxLayout()
        self.layout_numero.setSpacing(2)
        self.layout_numero.setObjectName(u"layout_numero")
        self.layout_numero.setContentsMargins(0, -1, 0, 1)
        self.label_numero = QLabel(self.frame_numero)
        self.label_numero.setObjectName(u"label_numero")
        sizePolicy.setHeightForWidth(self.label_numero.sizePolicy().hasHeightForWidth())
        self.label_numero.setSizePolicy(sizePolicy)
        self.label_numero.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.layout_numero.addWidget(self.label_numero)

        self.txt_numero = QLineEdit(self.frame_numero)
        self.txt_numero.setObjectName(u"txt_numero")
        sizePolicy.setHeightForWidth(self.txt_numero.sizePolicy().hasHeightForWidth())
        self.txt_numero.setSizePolicy(sizePolicy)
        self.txt_numero.setMinimumSize(QSize(0, 24))
        self.txt_numero.setMaximumSize(QSize(16777215, 28))
        self.txt_numero.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")

        self.layout_numero.addWidget(self.txt_numero)


        self.gridLayout_46.addLayout(self.layout_numero, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_numero)

        self.frame_complemento = QFrame(self.frames_txts_labels_usuarios)
        self.frame_complemento.setObjectName(u"frame_complemento")
        sizePolicy.setHeightForWidth(self.frame_complemento.sizePolicy().hasHeightForWidth())
        self.frame_complemento.setSizePolicy(sizePolicy)
        self.frame_complemento.setMinimumSize(QSize(0, 60))
        self.frame_complemento.setMaximumSize(QSize(16777215, 16777215))
        self.frame_complemento.setFrameShape(QFrame.NoFrame)
        self.frame_complemento.setFrameShadow(QFrame.Raised)
        self.gridLayout_45 = QGridLayout(self.frame_complemento)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.layout_complemento = QHBoxLayout()
        self.layout_complemento.setObjectName(u"layout_complemento")
        self.label_complemento = QLabel(self.frame_complemento)
        self.label_complemento.setObjectName(u"label_complemento")
        sizePolicy.setHeightForWidth(self.label_complemento.sizePolicy().hasHeightForWidth())
        self.label_complemento.setSizePolicy(sizePolicy)
        self.label_complemento.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.layout_complemento.addWidget(self.label_complemento)

        self.txt_complemento = QLineEdit(self.frame_complemento)
        self.txt_complemento.setObjectName(u"txt_complemento")
        sizePolicy.setHeightForWidth(self.txt_complemento.sizePolicy().hasHeightForWidth())
        self.txt_complemento.setSizePolicy(sizePolicy)
        self.txt_complemento.setMinimumSize(QSize(0, 24))
        self.txt_complemento.setMaximumSize(QSize(16777215, 28))
        self.txt_complemento.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")

        self.layout_complemento.addWidget(self.txt_complemento)


        self.gridLayout_45.addLayout(self.layout_complemento, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_complemento)

        self.frame_email = QFrame(self.frames_txts_labels_usuarios)
        self.frame_email.setObjectName(u"frame_email")
        sizePolicy.setHeightForWidth(self.frame_email.sizePolicy().hasHeightForWidth())
        self.frame_email.setSizePolicy(sizePolicy)
        self.frame_email.setMinimumSize(QSize(0, 60))
        self.frame_email.setMaximumSize(QSize(16777215, 16777215))
        self.frame_email.setFrameShape(QFrame.NoFrame)
        self.frame_email.setFrameShadow(QFrame.Raised)
        self.gridLayout_44 = QGridLayout(self.frame_email)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.layout_email = QHBoxLayout()
        self.layout_email.setObjectName(u"layout_email")
        self.label_email = QLabel(self.frame_email)
        self.label_email.setObjectName(u"label_email")
        sizePolicy.setHeightForWidth(self.label_email.sizePolicy().hasHeightForWidth())
        self.label_email.setSizePolicy(sizePolicy)
        self.label_email.setMinimumSize(QSize(0, 0))
        self.label_email.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.layout_email.addWidget(self.label_email)

        self.txt_email = QLineEdit(self.frame_email)
        self.txt_email.setObjectName(u"txt_email")
        sizePolicy.setHeightForWidth(self.txt_email.sizePolicy().hasHeightForWidth())
        self.txt_email.setSizePolicy(sizePolicy)
        self.txt_email.setMinimumSize(QSize(0, 24))
        self.txt_email.setMaximumSize(QSize(16777215, 28))
        self.txt_email.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")

        self.layout_email.addWidget(self.txt_email)


        self.gridLayout_44.addLayout(self.layout_email, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_email)

        self.frame_data_nascimento = QFrame(self.frames_txts_labels_usuarios)
        self.frame_data_nascimento.setObjectName(u"frame_data_nascimento")
        sizePolicy.setHeightForWidth(self.frame_data_nascimento.sizePolicy().hasHeightForWidth())
        self.frame_data_nascimento.setSizePolicy(sizePolicy)
        self.frame_data_nascimento.setMinimumSize(QSize(0, 60))
        self.frame_data_nascimento.setMaximumSize(QSize(16777215, 16777215))
        self.frame_data_nascimento.setFrameShape(QFrame.NoFrame)
        self.frame_data_nascimento.setFrameShadow(QFrame.Raised)
        self.gridLayout_43 = QGridLayout(self.frame_data_nascimento)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.layout_data_nascimento = QHBoxLayout()
        self.layout_data_nascimento.setObjectName(u"layout_data_nascimento")
        self.label_data_nascimento = QLabel(self.frame_data_nascimento)
        self.label_data_nascimento.setObjectName(u"label_data_nascimento")
        sizePolicy.setHeightForWidth(self.label_data_nascimento.sizePolicy().hasHeightForWidth())
        self.label_data_nascimento.setSizePolicy(sizePolicy)
        self.label_data_nascimento.setMinimumSize(QSize(0, 0))
        self.label_data_nascimento.setMaximumSize(QSize(16777215, 29))
        self.label_data_nascimento.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.layout_data_nascimento.addWidget(self.label_data_nascimento)

        self.txt_data_nascimento = QLineEdit(self.frame_data_nascimento)
        self.txt_data_nascimento.setObjectName(u"txt_data_nascimento")
        sizePolicy.setHeightForWidth(self.txt_data_nascimento.sizePolicy().hasHeightForWidth())
        self.txt_data_nascimento.setSizePolicy(sizePolicy)
        self.txt_data_nascimento.setMaximumSize(QSize(16777215, 29))
        self.txt_data_nascimento.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")

        self.layout_data_nascimento.addWidget(self.txt_data_nascimento)


        self.gridLayout_43.addLayout(self.layout_data_nascimento, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_data_nascimento)

        self.frame_rg = QFrame(self.frames_txts_labels_usuarios)
        self.frame_rg.setObjectName(u"frame_rg")
        sizePolicy.setHeightForWidth(self.frame_rg.sizePolicy().hasHeightForWidth())
        self.frame_rg.setSizePolicy(sizePolicy)
        self.frame_rg.setMinimumSize(QSize(0, 60))
        self.frame_rg.setMaximumSize(QSize(16777215, 16777215))
        self.frame_rg.setFrameShape(QFrame.NoFrame)
        self.frame_rg.setFrameShadow(QFrame.Raised)
        self.gridLayout_42 = QGridLayout(self.frame_rg)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.layout_rg = QHBoxLayout()
        self.layout_rg.setObjectName(u"layout_rg")
        self.label_rg = QLabel(self.frame_rg)
        self.label_rg.setObjectName(u"label_rg")
        sizePolicy.setHeightForWidth(self.label_rg.sizePolicy().hasHeightForWidth())
        self.label_rg.setSizePolicy(sizePolicy)
        self.label_rg.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.layout_rg.addWidget(self.label_rg)

        self.txt_rg = QLineEdit(self.frame_rg)
        self.txt_rg.setObjectName(u"txt_rg")
        sizePolicy.setHeightForWidth(self.txt_rg.sizePolicy().hasHeightForWidth())
        self.txt_rg.setSizePolicy(sizePolicy)
        self.txt_rg.setMinimumSize(QSize(0, 24))
        self.txt_rg.setMaximumSize(QSize(16777215, 28))
        self.txt_rg.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")

        self.layout_rg.addWidget(self.txt_rg)


        self.gridLayout_42.addLayout(self.layout_rg, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_rg)

        self.frame_cpf = QFrame(self.frames_txts_labels_usuarios)
        self.frame_cpf.setObjectName(u"frame_cpf")
        sizePolicy.setHeightForWidth(self.frame_cpf.sizePolicy().hasHeightForWidth())
        self.frame_cpf.setSizePolicy(sizePolicy)
        self.frame_cpf.setMinimumSize(QSize(0, 60))
        self.frame_cpf.setMaximumSize(QSize(16777215, 16777215))
        self.frame_cpf.setFrameShape(QFrame.NoFrame)
        self.frame_cpf.setFrameShadow(QFrame.Raised)
        self.gridLayout_41 = QGridLayout(self.frame_cpf)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.layout_cpf = QHBoxLayout()
        self.layout_cpf.setObjectName(u"layout_cpf")
        self.label_cpf = QLabel(self.frame_cpf)
        self.label_cpf.setObjectName(u"label_cpf")
        sizePolicy.setHeightForWidth(self.label_cpf.sizePolicy().hasHeightForWidth())
        self.label_cpf.setSizePolicy(sizePolicy)
        self.label_cpf.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.layout_cpf.addWidget(self.label_cpf)

        self.txt_cpf = QLineEdit(self.frame_cpf)
        self.txt_cpf.setObjectName(u"txt_cpf")
        sizePolicy.setHeightForWidth(self.txt_cpf.sizePolicy().hasHeightForWidth())
        self.txt_cpf.setSizePolicy(sizePolicy)
        self.txt_cpf.setMinimumSize(QSize(0, 24))
        self.txt_cpf.setMaximumSize(QSize(16777215, 28))
        self.txt_cpf.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")

        self.layout_cpf.addWidget(self.txt_cpf)


        self.gridLayout_41.addLayout(self.layout_cpf, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_cpf)

        self.frame_cep = QFrame(self.frames_txts_labels_usuarios)
        self.frame_cep.setObjectName(u"frame_cep")
        sizePolicy.setHeightForWidth(self.frame_cep.sizePolicy().hasHeightForWidth())
        self.frame_cep.setSizePolicy(sizePolicy)
        self.frame_cep.setMinimumSize(QSize(0, 60))
        self.frame_cep.setMaximumSize(QSize(16777215, 16777215))
        self.frame_cep.setFrameShape(QFrame.NoFrame)
        self.frame_cep.setFrameShadow(QFrame.Raised)
        self.gridLayout_39 = QGridLayout(self.frame_cep)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.layout_cep = QHBoxLayout()
        self.layout_cep.setObjectName(u"layout_cep")
        self.label_cep = QLabel(self.frame_cep)
        self.label_cep.setObjectName(u"label_cep")
        sizePolicy.setHeightForWidth(self.label_cep.sizePolicy().hasHeightForWidth())
        self.label_cep.setSizePolicy(sizePolicy)
        self.label_cep.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.layout_cep.addWidget(self.label_cep)

        self.txt_cep = QLineEdit(self.frame_cep)
        self.txt_cep.setObjectName(u"txt_cep")
        sizePolicy.setHeightForWidth(self.txt_cep.sizePolicy().hasHeightForWidth())
        self.txt_cep.setSizePolicy(sizePolicy)
        self.txt_cep.setMinimumSize(QSize(0, 24))
        self.txt_cep.setMaximumSize(QSize(16777215, 28))
        self.txt_cep.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")

        self.layout_cep.addWidget(self.txt_cep)


        self.gridLayout_39.addLayout(self.layout_cep, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_cep)

        self.frame_estado = QFrame(self.frames_txts_labels_usuarios)
        self.frame_estado.setObjectName(u"frame_estado")
        sizePolicy.setHeightForWidth(self.frame_estado.sizePolicy().hasHeightForWidth())
        self.frame_estado.setSizePolicy(sizePolicy)
        self.frame_estado.setMinimumSize(QSize(0, 60))
        self.frame_estado.setMaximumSize(QSize(16777215, 16777215))
        self.frame_estado.setFrameShape(QFrame.NoFrame)
        self.frame_estado.setFrameShadow(QFrame.Raised)
        self.gridLayout_51 = QGridLayout(self.frame_estado)
        self.gridLayout_51.setObjectName(u"gridLayout_51")
        self.layout_estado = QHBoxLayout()
        self.layout_estado.setObjectName(u"layout_estado")
        self.label_estado = QLabel(self.frame_estado)
        self.label_estado.setObjectName(u"label_estado")
        sizePolicy.setHeightForWidth(self.label_estado.sizePolicy().hasHeightForWidth())
        self.label_estado.setSizePolicy(sizePolicy)
        self.label_estado.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.layout_estado.addWidget(self.label_estado)

        self.perfil_estado = QComboBox(self.frame_estado)
        self.perfil_estado.addItem("")
        self.perfil_estado.addItem("")
        self.perfil_estado.addItem("")
        self.perfil_estado.addItem("")
        self.perfil_estado.addItem("")
        self.perfil_estado.addItem("")
        self.perfil_estado.addItem("")
        self.perfil_estado.addItem("")
        self.perfil_estado.addItem("")
        self.perfil_estado.addItem("")
        self.perfil_estado.addItem("")
        self.perfil_estado.addItem("")
        self.perfil_estado.addItem("")
        self.perfil_estado.addItem("")
        self.perfil_estado.addItem("")
        self.perfil_estado.addItem("")
        self.perfil_estado.addItem("")
        self.perfil_estado.addItem("")
        self.perfil_estado.addItem("")
        self.perfil_estado.addItem("")
        self.perfil_estado.addItem("")
        self.perfil_estado.addItem("")
        self.perfil_estado.addItem("")
        self.perfil_estado.addItem("")
        self.perfil_estado.addItem("")
        self.perfil_estado.addItem("")
        self.perfil_estado.addItem("")
        self.perfil_estado.setObjectName(u"perfil_estado")
        sizePolicy.setHeightForWidth(self.perfil_estado.sizePolicy().hasHeightForWidth())
        self.perfil_estado.setSizePolicy(sizePolicy)
        self.perfil_estado.setMinimumSize(QSize(0, 24))
        self.perfil_estado.setMaximumSize(QSize(16777215, 28))
        self.perfil_estado.setStyleSheet(u"   QComboBox { \n"
"        background-color: white; \n"
"        border: 1px solid #ccc; \n"
"        border-radius: 5px; \n"
"        color: black; \n"
"        padding: 5px;\n"
"    }\n"
"    QComboBox QAbstractItemView {\n"
"        background-color: white; \n"
"        color: black; \n"
"        border: 1px solid #ccc; \n"
"        selection-background-color: #e5e5e5; \n"
"        selection-color: black;\n"
"    }\n"
"    QComboBox QAbstractItemView QScrollBar:vertical {\n"
"        background: #f5f5f5; \n"
"        width: 12px; \n"
"        border: none;\n"
"    }\n"
"    QComboBox QAbstractItemView QScrollBar::handle:vertical {\n"
"        background: #cccccc; \n"
"        min-height: 20px; \n"
"        border-radius: 5px;\n"
"    }\n"
"    QComboBox QAbstractItemView QScrollBar::add-line:vertical, \n"
"    QComboBox QAbstractItemView QScrollBar::sub-line:vertical {\n"
"        background: none;\n"
"        height: 0px;  /* Remove os bot\u00f5es de linha (setas de cima e baixo) */\n"
"    }\n"
"    QCom"
                        "boBox QAbstractItemView QScrollBar::add-page:vertical, \n"
"    QComboBox QAbstractItemView QScrollBar::sub-page:vertical {\n"
"        background: none;\n"
"    }\n"
"\n"
"")

        self.layout_estado.addWidget(self.perfil_estado)


        self.gridLayout_51.addLayout(self.layout_estado, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_estado)

        self.frame_senha = QFrame(self.frames_txts_labels_usuarios)
        self.frame_senha.setObjectName(u"frame_senha")
        sizePolicy.setHeightForWidth(self.frame_senha.sizePolicy().hasHeightForWidth())
        self.frame_senha.setSizePolicy(sizePolicy)
        self.frame_senha.setMinimumSize(QSize(0, 60))
        self.frame_senha.setMaximumSize(QSize(16777215, 16777215))
        self.frame_senha.setFrameShape(QFrame.NoFrame)
        self.frame_senha.setFrameShadow(QFrame.Raised)
        self.gridLayout_52 = QGridLayout(self.frame_senha)
        self.gridLayout_52.setObjectName(u"gridLayout_52")
        self.layout_senha = QHBoxLayout()
        self.layout_senha.setObjectName(u"layout_senha")
        self.label_senha = QLabel(self.frame_senha)
        self.label_senha.setObjectName(u"label_senha")
        sizePolicy.setHeightForWidth(self.label_senha.sizePolicy().hasHeightForWidth())
        self.label_senha.setSizePolicy(sizePolicy)
        self.label_senha.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.layout_senha.addWidget(self.label_senha)

        self.txt_senha = QLineEdit(self.frame_senha)
        self.txt_senha.setObjectName(u"txt_senha")
        sizePolicy.setHeightForWidth(self.txt_senha.sizePolicy().hasHeightForWidth())
        self.txt_senha.setSizePolicy(sizePolicy)
        self.txt_senha.setMinimumSize(QSize(0, 24))
        self.txt_senha.setMaximumSize(QSize(16777215, 28))
        self.txt_senha.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")
        self.txt_senha.setEchoMode(QLineEdit.Password)

        self.layout_senha.addWidget(self.txt_senha)


        self.gridLayout_52.addLayout(self.layout_senha, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_senha)

        self.frame_confirmar_senha = QFrame(self.frames_txts_labels_usuarios)
        self.frame_confirmar_senha.setObjectName(u"frame_confirmar_senha")
        sizePolicy.setHeightForWidth(self.frame_confirmar_senha.sizePolicy().hasHeightForWidth())
        self.frame_confirmar_senha.setSizePolicy(sizePolicy)
        self.frame_confirmar_senha.setMinimumSize(QSize(0, 60))
        self.frame_confirmar_senha.setMaximumSize(QSize(16777215, 16777215))
        self.frame_confirmar_senha.setFrameShape(QFrame.NoFrame)
        self.frame_confirmar_senha.setFrameShadow(QFrame.Raised)
        self.gridLayout_40 = QGridLayout(self.frame_confirmar_senha)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.layout_cpnfirmar_senha = QHBoxLayout()
        self.layout_cpnfirmar_senha.setObjectName(u"layout_cpnfirmar_senha")
        self.label_confirmar_senha = QLabel(self.frame_confirmar_senha)
        self.label_confirmar_senha.setObjectName(u"label_confirmar_senha")
        sizePolicy.setHeightForWidth(self.label_confirmar_senha.sizePolicy().hasHeightForWidth())
        self.label_confirmar_senha.setSizePolicy(sizePolicy)
        self.label_confirmar_senha.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.layout_cpnfirmar_senha.addWidget(self.label_confirmar_senha)

        self.txt_confirmar_senha = QLineEdit(self.frame_confirmar_senha)
        self.txt_confirmar_senha.setObjectName(u"txt_confirmar_senha")
        sizePolicy.setHeightForWidth(self.txt_confirmar_senha.sizePolicy().hasHeightForWidth())
        self.txt_confirmar_senha.setSizePolicy(sizePolicy)
        self.txt_confirmar_senha.setMinimumSize(QSize(0, 24))
        self.txt_confirmar_senha.setMaximumSize(QSize(16777215, 28))
        self.txt_confirmar_senha.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")
        self.txt_confirmar_senha.setEchoMode(QLineEdit.Password)

        self.layout_cpnfirmar_senha.addWidget(self.txt_confirmar_senha)


        self.gridLayout_40.addLayout(self.layout_cpnfirmar_senha, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_confirmar_senha)

        self.frame_usuarios = QFrame(self.frames_txts_labels_usuarios)
        self.frame_usuarios.setObjectName(u"frame_usuarios")
        sizePolicy.setHeightForWidth(self.frame_usuarios.sizePolicy().hasHeightForWidth())
        self.frame_usuarios.setSizePolicy(sizePolicy)
        self.frame_usuarios.setMinimumSize(QSize(0, 60))
        self.frame_usuarios.setFrameShape(QFrame.NoFrame)
        self.frame_usuarios.setFrameShadow(QFrame.Raised)
        self.gridLayout_53 = QGridLayout(self.frame_usuarios)
        self.gridLayout_53.setObjectName(u"gridLayout_53")
        self.layout_usuarios = QHBoxLayout()
        self.layout_usuarios.setObjectName(u"layout_usuarios")
        self.label_perfil = QLabel(self.frame_usuarios)
        self.label_perfil.setObjectName(u"label_perfil")
        sizePolicy.setHeightForWidth(self.label_perfil.sizePolicy().hasHeightForWidth())
        self.label_perfil.setSizePolicy(sizePolicy)
        self.label_perfil.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.layout_usuarios.addWidget(self.label_perfil)

        self.perfil_usuarios = QComboBox(self.frame_usuarios)
        self.perfil_usuarios.addItem("")
        self.perfil_usuarios.addItem("")
        self.perfil_usuarios.addItem("")
        self.perfil_usuarios.setObjectName(u"perfil_usuarios")
        sizePolicy.setHeightForWidth(self.perfil_usuarios.sizePolicy().hasHeightForWidth())
        self.perfil_usuarios.setSizePolicy(sizePolicy)
        self.perfil_usuarios.setMinimumSize(QSize(0, 24))
        self.perfil_usuarios.setMaximumSize(QSize(16777215, 28))
        self.perfil_usuarios.setStyleSheet(u"\n"
"    QComboBox { \n"
"        background-color: white; \n"
"        border: 1px solid #ccc; \n"
"        border-radius: 5px; \n"
"        color: black; \n"
"        padding: 5px;\n"
"    }\n"
"    QComboBox QAbstractItemView {\n"
"        background-color: white; \n"
"        color: black; \n"
"        border: 1px solid #ccc; \n"
"        selection-background-color: #e5e5e5; \n"
"        selection-color: black;\n"
"    }\n"
"    QComboBox QAbstractItemView QScrollBar:vertical {\n"
"        background: #f5f5f5; \n"
"        width: 12px; \n"
"        border: none;\n"
"    }\n"
"    QComboBox QAbstractItemView QScrollBar::handle:vertical {\n"
"        background: #cccccc; \n"
"        min-height: 20px; \n"
"        border-radius: 5px;\n"
"    }\n"
"    QComboBox QAbstractItemView QScrollBar::add-line:vertical, \n"
"    QComboBox QAbstractItemView QScrollBar::sub-line:vertical {\n"
"        background: none;\n"
"        height: 0px;  /* Remove os bot\u00f5es de linha (setas de cima e baixo) */\n"
"    }\n"
"  "
                        "  QComboBox QAbstractItemView QScrollBar::add-page:vertical, \n"
"    QComboBox QAbstractItemView QScrollBar::sub-page:vertical {\n"
"        background: none;\n"
"    }\n"
"\n"
"")

        self.layout_usuarios.addWidget(self.perfil_usuarios)


        self.gridLayout_53.addLayout(self.layout_usuarios, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_usuarios)


        self.gridLayout_37.addWidget(self.frames_txts_labels_usuarios, 1, 0, 1, 1)

        self.frame_20 = QFrame(self.frame_pag_cadastrar_usuario)
        self.frame_20.setObjectName(u"frame_20")
        sizePolicy.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy)
        self.frame_20.setMaximumSize(QSize(189, 219))
        self.frame_20.setFrameShape(QFrame.NoFrame)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.gridLayout_38 = QGridLayout(self.frame_20)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_editar_cadastro = QPushButton(self.frame_20)
        self.btn_editar_cadastro.setObjectName(u"btn_editar_cadastro")
        sizePolicy.setHeightForWidth(self.btn_editar_cadastro.sizePolicy().hasHeightForWidth())
        self.btn_editar_cadastro.setSizePolicy(sizePolicy)
        self.btn_editar_cadastro.setMaximumSize(QSize(16777215, 30))
        self.btn_editar_cadastro.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_4.addWidget(self.btn_editar_cadastro)

        self.btn_atualizar_cadastro = QPushButton(self.frame_20)
        self.btn_atualizar_cadastro.setObjectName(u"btn_atualizar_cadastro")
        sizePolicy.setHeightForWidth(self.btn_atualizar_cadastro.sizePolicy().hasHeightForWidth())
        self.btn_atualizar_cadastro.setSizePolicy(sizePolicy)
        self.btn_atualizar_cadastro.setMaximumSize(QSize(16777215, 30))
        self.btn_atualizar_cadastro.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_4.addWidget(self.btn_atualizar_cadastro)

        self.btn_apagar_cadastro = QPushButton(self.frame_20)
        self.btn_apagar_cadastro.setObjectName(u"btn_apagar_cadastro")
        sizePolicy.setHeightForWidth(self.btn_apagar_cadastro.sizePolicy().hasHeightForWidth())
        self.btn_apagar_cadastro.setSizePolicy(sizePolicy)
        self.btn_apagar_cadastro.setMaximumSize(QSize(16777215, 30))
        self.btn_apagar_cadastro.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_4.addWidget(self.btn_apagar_cadastro)

        self.btn_carregar_imagem_4 = QPushButton(self.frame_20)
        self.btn_carregar_imagem_4.setObjectName(u"btn_carregar_imagem_4")
        sizePolicy.setHeightForWidth(self.btn_carregar_imagem_4.sizePolicy().hasHeightForWidth())
        self.btn_carregar_imagem_4.setSizePolicy(sizePolicy)
        self.btn_carregar_imagem_4.setMaximumSize(QSize(16777215, 30))
        self.btn_carregar_imagem_4.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_4.addWidget(self.btn_carregar_imagem_4)

        self.btn_fazer_cadastro = QPushButton(self.frame_20)
        self.btn_fazer_cadastro.setObjectName(u"btn_fazer_cadastro")
        sizePolicy.setHeightForWidth(self.btn_fazer_cadastro.sizePolicy().hasHeightForWidth())
        self.btn_fazer_cadastro.setSizePolicy(sizePolicy)
        self.btn_fazer_cadastro.setMaximumSize(QSize(16777215, 30))
        self.btn_fazer_cadastro.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_4.addWidget(self.btn_fazer_cadastro)


        self.gridLayout_38.addLayout(self.verticalLayout_4, 0, 0, 1, 1)


        self.gridLayout_37.addWidget(self.frame_20, 1, 1, 1, 1)

        self.frame_imagem_cadastro = QFrame(self.frame_pag_cadastrar_usuario)
        self.frame_imagem_cadastro.setObjectName(u"frame_imagem_cadastro")
        sizePolicy.setHeightForWidth(self.frame_imagem_cadastro.sizePolicy().hasHeightForWidth())
        self.frame_imagem_cadastro.setSizePolicy(sizePolicy)
        self.frame_imagem_cadastro.setMaximumSize(QSize(300, 300))
        self.frame_imagem_cadastro.setFrameShape(QFrame.NoFrame)
        self.frame_imagem_cadastro.setFrameShadow(QFrame.Raised)

        self.gridLayout_37.addWidget(self.frame_imagem_cadastro, 1, 2, 1, 1)


        self.gridLayout_34.addWidget(self.frame_pag_cadastrar_usuario, 0, 0, 1, 1)

        self.paginas_sistemas.addWidget(self.pg_cadastrar_usuario)
        self.pg_clientes = QWidget()
        self.pg_clientes.setObjectName(u"pg_clientes")
        self.gridLayout_35 = QGridLayout(self.pg_clientes)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.frame_pg_clientes = QFrame(self.pg_clientes)
        self.frame_pg_clientes.setObjectName(u"frame_pg_clientes")
        self.frame_pg_clientes.setFrameShape(QFrame.NoFrame)
        self.frame_pg_clientes.setFrameShadow(QFrame.Raised)
        self.label_pagina_clientes = QLabel(self.frame_pg_clientes)
        self.label_pagina_clientes.setObjectName(u"label_pagina_clientes")
        self.label_pagina_clientes.setGeometry(QRect(590, 340, 361, 41))
        self.label_pagina_clientes.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.gridLayout_35.addWidget(self.frame_pg_clientes, 0, 0, 1, 1)

        self.paginas_sistemas.addWidget(self.pg_clientes)
        self.pg_configuracoes = QWidget()
        self.pg_configuracoes.setObjectName(u"pg_configuracoes")
        self.gridLayout_36 = QGridLayout(self.pg_configuracoes)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.frame_pg_configuracoes = QFrame(self.pg_configuracoes)
        self.frame_pg_configuracoes.setObjectName(u"frame_pg_configuracoes")
        sizePolicy.setHeightForWidth(self.frame_pg_configuracoes.sizePolicy().hasHeightForWidth())
        self.frame_pg_configuracoes.setSizePolicy(sizePolicy)
        self.frame_pg_configuracoes.setFrameShape(QFrame.NoFrame)
        self.frame_pg_configuracoes.setFrameShadow(QFrame.Raised)
        self.gridLayout_54 = QGridLayout(self.frame_pg_configuracoes)
        self.gridLayout_54.setObjectName(u"gridLayout_54")
        self.horizontalSpacer_2 = QSpacerItem(545, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_54.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.frame_configuracoes = QFrame(self.frame_pg_configuracoes)
        self.frame_configuracoes.setObjectName(u"frame_configuracoes")
        sizePolicy.setHeightForWidth(self.frame_configuracoes.sizePolicy().hasHeightForWidth())
        self.frame_configuracoes.setSizePolicy(sizePolicy)
        self.frame_configuracoes.setMinimumSize(QSize(500, 0))
        self.frame_configuracoes.setMaximumSize(QSize(0, 80))
        self.frame_configuracoes.setFrameShape(QFrame.NoFrame)
        self.frame_configuracoes.setFrameShadow(QFrame.Raised)
        self.gridLayout_55 = QGridLayout(self.frame_configuracoes)
        self.gridLayout_55.setObjectName(u"gridLayout_55")
        self.label_configuracoes = QLabel(self.frame_configuracoes)
        self.label_configuracoes.setObjectName(u"label_configuracoes")
        sizePolicy.setHeightForWidth(self.label_configuracoes.sizePolicy().hasHeightForWidth())
        self.label_configuracoes.setSizePolicy(sizePolicy)
        self.label_configuracoes.setMinimumSize(QSize(0, 42))
        self.label_configuracoes.setMaximumSize(QSize(16777215, 106))
        self.label_configuracoes.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"	border: 5px solid white;\n"
"}\n"
"\n"
"")

        self.gridLayout_55.addWidget(self.label_configuracoes, 0, 0, 1, 1)


        self.gridLayout_54.addWidget(self.frame_configuracoes, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(416, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_54.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.frame_botoes_configuracoes = QFrame(self.frame_pg_configuracoes)
        self.frame_botoes_configuracoes.setObjectName(u"frame_botoes_configuracoes")
        sizePolicy.setHeightForWidth(self.frame_botoes_configuracoes.sizePolicy().hasHeightForWidth())
        self.frame_botoes_configuracoes.setSizePolicy(sizePolicy)
        self.frame_botoes_configuracoes.setMinimumSize(QSize(0, 698))
        self.frame_botoes_configuracoes.setMaximumSize(QSize(16777215, 686))
        self.frame_botoes_configuracoes.setStyleSheet(u"QFrame {\n"
"    border: 2px solid white;\n"
"}\n"
"")
        self.frame_botoes_configuracoes.setFrameShape(QFrame.StyledPanel)
        self.frame_botoes_configuracoes.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_botoes_configuracoes)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tool_tema = QToolButton(self.frame_botoes_configuracoes)
        self.tool_tema.setObjectName(u"tool_tema")
        sizePolicy.setHeightForWidth(self.tool_tema.sizePolicy().hasHeightForWidth())
        self.tool_tema.setSizePolicy(sizePolicy)
        self.tool_tema.setMaximumSize(QSize(151, 31))
        self.tool_tema.setStyleSheet(u"QToolButton {\n"
"                background-color: rgb(50, 150, 250);\n"
"                color: white;\n"
"                border-radius: 5px;\n"
"                border: 2px solid rgb(50, 150, 250);\n"
"                padding: 5px 10px;\n"
"            }\n"
"            QToolButton:hover {\n"
"                background-color: rgb(100, 180, 255);\n"
"                border: 2px solid rgb(100, 180, 255);\n"
"            }\n"
"            ")
        self.tool_tema.setPopupMode(QToolButton.MenuButtonPopup)
        self.tool_tema.setToolButtonStyle(Qt.ToolButtonTextOnly)

        self.verticalLayout_7.addWidget(self.tool_tema)

        self.tool_atalhos = QToolButton(self.frame_botoes_configuracoes)
        self.tool_atalhos.setObjectName(u"tool_atalhos")
        sizePolicy.setHeightForWidth(self.tool_atalhos.sizePolicy().hasHeightForWidth())
        self.tool_atalhos.setSizePolicy(sizePolicy)
        self.tool_atalhos.setMaximumSize(QSize(151, 31))
        self.tool_atalhos.setStyleSheet(u"QToolButton {\n"
"                background-color: rgb(50, 150, 250);\n"
"                color: white;\n"
"                border-radius: 5px;\n"
"                border: 2px solid rgb(50, 150, 250);\n"
"                padding: 5px 10px;\n"
"            }\n"
"            QToolButton:hover {\n"
"                background-color: rgb(100, 180, 255);\n"
"                border: 2px solid rgb(100, 180, 255);\n"
"            }\n"
"            ")
        self.tool_atalhos.setPopupMode(QToolButton.MenuButtonPopup)
        self.tool_atalhos.setToolButtonStyle(Qt.ToolButtonTextOnly)

        self.verticalLayout_7.addWidget(self.tool_atalhos)

        self.tool_hora = QToolButton(self.frame_botoes_configuracoes)
        self.tool_hora.setObjectName(u"tool_hora")
        self.tool_hora.setMaximumSize(QSize(151, 31))
        self.tool_hora.setStyleSheet(u"QToolButton {\n"
"                background-color: rgb(50, 150, 250);\n"
"                color: white;\n"
"                border-radius: 5px;\n"
"                border: 2px solid rgb(50, 150, 250);\n"
"                padding: 5px 10px;\n"
"            }\n"
"            QToolButton:hover {\n"
"                background-color: rgb(100, 180, 255);\n"
"                border: 2px solid rgb(100, 180, 255);\n"
"            }\n"
"            ")
        self.tool_hora.setPopupMode(QToolButton.MenuButtonPopup)

        self.verticalLayout_7.addWidget(self.tool_hora)

        self.tool_fonte = QToolButton(self.frame_botoes_configuracoes)
        self.tool_fonte.setObjectName(u"tool_fonte")
        self.tool_fonte.setMaximumSize(QSize(151, 31))
        self.tool_fonte.setStyleSheet(u"QToolButton {\n"
"                background-color: rgb(50, 150, 250);\n"
"                color: white;\n"
"                border-radius: 5px;\n"
"                border: 2px solid rgb(50, 150, 250);\n"
"                padding: 5px 10px;\n"
"            }\n"
"            QToolButton:hover {\n"
"                background-color: rgb(100, 180, 255);\n"
"                border: 2px solid rgb(100, 180, 255);\n"
"            }\n"
"            ")
        self.tool_fonte.setPopupMode(QToolButton.MenuButtonPopup)

        self.verticalLayout_7.addWidget(self.tool_fonte)

        self.tool_atualizacoes = QToolButton(self.frame_botoes_configuracoes)
        self.tool_atualizacoes.setObjectName(u"tool_atualizacoes")
        self.tool_atualizacoes.setMaximumSize(QSize(151, 31))
        self.tool_atualizacoes.setStyleSheet(u"QToolButton {\n"
"                background-color: rgb(50, 150, 250);\n"
"                color: white;\n"
"                border-radius: 5px;\n"
"                border: 2px solid rgb(50, 150, 250);\n"
"                padding: 5px 10px;\n"
"            }\n"
"            QToolButton:hover {\n"
"                background-color: rgb(100, 180, 255);\n"
"                border: 2px solid rgb(100, 180, 255);\n"
"            }\n"
"            ")
        self.tool_atualizacoes.setPopupMode(QToolButton.MenuButtonPopup)
        self.tool_atualizacoes.setToolButtonStyle(Qt.ToolButtonTextOnly)

        self.verticalLayout_7.addWidget(self.tool_atualizacoes)


        self.gridLayout_54.addWidget(self.frame_botoes_configuracoes, 1, 0, 1, 3)


        self.gridLayout_36.addWidget(self.frame_pg_configuracoes, 0, 0, 1, 1)

        self.paginas_sistemas.addWidget(self.pg_configuracoes)
        self.pg_contato = QWidget()
        self.pg_contato.setObjectName(u"pg_contato")
        self.gridLayout_56 = QGridLayout(self.pg_contato)
        self.gridLayout_56.setObjectName(u"gridLayout_56")
        self.frame_2 = QFrame(self.pg_contato)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_57 = QGridLayout(self.frame_2)
        self.gridLayout_57.setObjectName(u"gridLayout_57")
        self.horizontalSpacer_5 = QSpacerItem(558, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_57.addItem(self.horizontalSpacer_5, 1, 3, 1, 2)

        self.horizontalSpacer_4 = QSpacerItem(552, 24, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_57.addItem(self.horizontalSpacer_4, 0, 4, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(482, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_57.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(488, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_57.addItem(self.horizontalSpacer_6, 1, 0, 1, 2)

        self.frame_desenvolvido = QFrame(self.frame_2)
        self.frame_desenvolvido.setObjectName(u"frame_desenvolvido")
        sizePolicy.setHeightForWidth(self.frame_desenvolvido.sizePolicy().hasHeightForWidth())
        self.frame_desenvolvido.setSizePolicy(sizePolicy)
        self.frame_desenvolvido.setMaximumSize(QSize(450, 170))
        self.frame_desenvolvido.setFrameShape(QFrame.NoFrame)
        self.frame_desenvolvido.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_desenvolvido)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_desenvolvido = QLabel(self.frame_desenvolvido)
        self.label_desenvolvido.setObjectName(u"label_desenvolvido")
        sizePolicy.setHeightForWidth(self.label_desenvolvido.sizePolicy().hasHeightForWidth())
        self.label_desenvolvido.setSizePolicy(sizePolicy)
        self.label_desenvolvido.setMinimumSize(QSize(0, 0))
        self.label_desenvolvido.setMaximumSize(QSize(401, 16777215))
        self.label_desenvolvido.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"\n"
"}\n"
"\n"
"")
        self.label_desenvolvido.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_8.addWidget(self.label_desenvolvido)


        self.gridLayout_57.addWidget(self.frame_desenvolvido, 0, 1, 1, 3)

        self.frame_contato_keven = QFrame(self.frame_2)
        self.frame_contato_keven.setObjectName(u"frame_contato_keven")
        sizePolicy.setHeightForWidth(self.frame_contato_keven.sizePolicy().hasHeightForWidth())
        self.frame_contato_keven.setSizePolicy(sizePolicy)
        self.frame_contato_keven.setMaximumSize(QSize(16777215, 56))
        self.frame_contato_keven.setFrameShape(QFrame.NoFrame)
        self.frame_contato_keven.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_contato_keven)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_contato_keven = QLabel(self.frame_contato_keven)
        self.label_contato_keven.setObjectName(u"label_contato_keven")
        self.label_contato_keven.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"\n"
"}\n"
"\n"
"")

        self.verticalLayout.addWidget(self.label_contato_keven)


        self.gridLayout_57.addWidget(self.frame_contato_keven, 1, 2, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_57.addItem(self.verticalSpacer_12, 2, 2, 1, 1)


        self.gridLayout_56.addWidget(self.frame_2, 0, 0, 1, 1)

        self.paginas_sistemas.addWidget(self.pg_contato)

        self.gridLayout_2.addWidget(self.paginas_sistemas, 0, 1, 1, 1)


        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.frame_principal)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.paginas_sistemas.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_verificar_estoque.setText(QCoreApplication.translate("MainWindow", u"Verificar Estoque", None))
        self.btn_verificar_usuarios.setText(QCoreApplication.translate("MainWindow", u"Verificar Usu\u00e1rios", None))
        self.btn_cadastrar_produto.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Produto", None))
        self.btn_cadastrar_usuarios.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Usu\u00e1rio", None))
        self.btn_clientes.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.btn_configuracoes.setText(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es", None))
        self.label_imagem_sistema.setText("")
        self.label_bem_vindo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; font-style:italic;\">Bem vindo(a) ao</span></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; font-style:italic;\">Sistema de Gerenciamento do </span></p><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; font-style:italic;\">controle de Estoque</span></p></body></html>", None))
        self.label_saida.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">SA\u00cdDA</span></p></body></html>", None))
        self.btn_gerar_estorno.setText(QCoreApplication.translate("MainWindow", u"Gerar Estorno", None))
        self.btn_importar.setText(QCoreApplication.translate("MainWindow", u"Importar", None))
        self.btn_gerar_saida.setText(QCoreApplication.translate("MainWindow", u"Gerar Sa\u00edda", None))
        self.btn_novo_produto.setText(QCoreApplication.translate("MainWindow", u"Novo produto", None))
        self.btn_atualizar_saida.setText(QCoreApplication.translate("MainWindow", u"Atualizar sa\u00edda", None))
        self.btn_historico.setText(QCoreApplication.translate("MainWindow", u"Hist\u00f3rico", None))
        self.btn_gerar_pdf.setText(QCoreApplication.translate("MainWindow", u"Gerar PDF", None))
        self.btn_atualizar_estoque.setText(QCoreApplication.translate("MainWindow", u"Atualizar estoque", None))
        self.btn_limpar_tabelas.setText(QCoreApplication.translate("MainWindow", u"Limpar tabelas", None))
        self.btn_incluir_no_sistema.setText(QCoreApplication.translate("MainWindow", u"Incluir produto no sistema", None))
        ___qtablewidgetitem = self.table_saida.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Produto", None));
        ___qtablewidgetitem1 = self.table_saida.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtablewidgetitem2 = self.table_saida.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Valor do Produto", None));
        ___qtablewidgetitem3 = self.table_saida.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Desconto", None));
        ___qtablewidgetitem4 = self.table_saida.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Data de Sa\u00edda", None));
        ___qtablewidgetitem5 = self.table_saida.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Data da Cria\u00e7\u00e3o ", None));
        ___qtablewidgetitem6 = self.table_saida.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo do Produto", None));
        ___qtablewidgetitem7 = self.table_saida.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Cliente", None));
        ___qtablewidgetitem8 = self.table_saida.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o do Produto", None));
        ___qtablewidgetitem9 = self.table_saida.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None));
        self.btn_salvar_tables.setText("")
        self.label_estoque.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">ESTOQUE</span></p></body></html>", None))
        self.btn_abrir_planilha.setText(QCoreApplication.translate("MainWindow", u"Abrir Planilha", None))
        ___qtablewidgetitem10 = self.table_base.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Produto", None));
        ___qtablewidgetitem11 = self.table_base.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtablewidgetitem12 = self.table_base.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Valor do Produto", None));
        ___qtablewidgetitem13 = self.table_base.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Desconto", None));
        ___qtablewidgetitem14 = self.table_base.horizontalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Data da Compra", None));
        ___qtablewidgetitem15 = self.table_base.horizontalHeaderItem(5)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo do Item", None));
        ___qtablewidgetitem16 = self.table_base.horizontalHeaderItem(6)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Cliente", None));
        ___qtablewidgetitem17 = self.table_base.horizontalHeaderItem(7)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o do Produto", None));
        ___qtablewidgetitem18 = self.table_base.horizontalHeaderItem(8)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None));
#if QT_CONFIG(whatsthis)
        self.table_base.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.tb_base.setTabText(self.tb_base.indexOf(self.tabela_base), "")
        self.label_em_desenvolvimento.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; font-style:italic;\">P\u00c1GINA EM DESENVOLVIMENTO</span></p></body></html>", None))
        self.label_quantidade_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Quantidade total de produtos</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.btn_adicionar_produto.setToolTip(QCoreApplication.translate("MainWindow", u"Realiza e exibe o c\u00e1lculo do produto", None))
#endif // QT_CONFIG(tooltip)
        self.btn_adicionar_produto.setText(QCoreApplication.translate("MainWindow", u"ADICIONAR", None))
#if QT_CONFIG(tooltip)
        self.btn_editar.setToolTip(QCoreApplication.translate("MainWindow", u"Exibe a tabela de produtos para atualiza\u00e7\u00e3o", None))
#endif // QT_CONFIG(tooltip)
        self.btn_editar.setText(QCoreApplication.translate("MainWindow", u"EDITAR ", None))
#if QT_CONFIG(tooltip)
        self.btn_atualizar_produto.setToolTip(QCoreApplication.translate("MainWindow", u"Atualiza o produto no banco de dados", None))
#endif // QT_CONFIG(tooltip)
        self.btn_atualizar_produto.setText(QCoreApplication.translate("MainWindow", u"ATUALIZAR", None))
#if QT_CONFIG(tooltip)
        self.btn_limpar_campos.setToolTip(QCoreApplication.translate("MainWindow", u"Apaga as informa\u00e7\u00f5es preenchidas", None))
#endif // QT_CONFIG(tooltip)
        self.btn_limpar_campos.setText(QCoreApplication.translate("MainWindow", u"APAGAR", None))
#if QT_CONFIG(tooltip)
        self.btn_remover_imagem.setToolTip(QCoreApplication.translate("MainWindow", u"Remove a imagem do produto selecionado", None))
#endif // QT_CONFIG(tooltip)
        self.btn_remover_imagem.setText(QCoreApplication.translate("MainWindow", u"REMOVER IMAGEM", None))
#if QT_CONFIG(tooltip)
        self.btn_carregar_imagem.setToolTip(QCoreApplication.translate("MainWindow", u"Carrega a imagem para cadastro do produto", None))
#endif // QT_CONFIG(tooltip)
        self.btn_carregar_imagem.setText(QCoreApplication.translate("MainWindow", u"CARREGAR IMAGEM", None))
        self.label_valor_do_desconto.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Valor do desconto</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.btn_confirmar.setToolTip(QCoreApplication.translate("MainWindow", u"Cadastra o produto", None))
#endif // QT_CONFIG(tooltip)
        self.btn_confirmar.setText(QCoreApplication.translate("MainWindow", u"CONFIRMAR", None))
#if QT_CONFIG(tooltip)
        self.btn_ver_item.setToolTip(QCoreApplication.translate("MainWindow", u"Redireciona at\u00e9 o estoque dos produtos", None))
#endif // QT_CONFIG(tooltip)
        self.btn_ver_item.setText(QCoreApplication.translate("MainWindow", u"VER PRODUTO", None))
        self.label_cadastramento_produtos.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">Cadastramento de Produtos</span></p></body></html>", None))
        self.label_valor_com_desconto.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Valor do produto com desconto</span></p></body></html>", None))
        self.label_valor_total_produtos_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Valor total de produtos sem desconto</span></p></body></html>", None))
        self.label_produto.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Produto</span></p></body></html>", None))
        self.label_quantidade.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Quantidade</span></p></body></html>", None))
        self.label_valor_produto_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Valor  do produto</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.txt_valor_produto_3.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.txt_valor_produto_3.setText("")
        self.txt_valor_produto_3.setPlaceholderText("")
        self.label_desconto_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Desconto</span></p></body></html>", None))
        self.txt_desconto_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Opcional", None))
        self.label_data_compra_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Data da Compra</span></p><p><br/></p></body></html>", None))
        self.label_codigo_item_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">C\u00f3digo do Item</span></p></body></html>", None))
        self.label_cliente_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Cliente</span></p></body></html>", None))
        self.label_descricao_produto_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Descri\u00e7\u00e3o do produto</span></p></body></html>", None))
        self.label_cadastramento.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; font-style:italic;\">CADASTRAMENTO DE USU\u00c1RIO</span></p></body></html>", None))
        self.label_nome.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Nome</span></p></body></html>", None))
        self.txt_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome completo", None))
        self.label_usuario.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Usu\u00e1rio</span></p></body></html>", None))
        self.txt_usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Gerado automaticamente", None))
        self.label_telefone.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Telefone</span></p></body></html>", None))
        self.txt_telefone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ex.. (00) 00000-0000", None))
        self.label_endereco.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Endere\u00e7o</span></p></body></html>", None))
        self.label_numero.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">N\u00famero</span></p></body></html>", None))
        self.label_complemento.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Complemento</span></p></body></html>", None))
        self.txt_complemento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Opcional", None))
        self.label_email.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">E-mail</span></p></body></html>", None))
        self.txt_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ex.. usuario@gmail.com", None))
        self.label_data_nascimento.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Data de nascimento</span></p><p><br/></p></body></html>", None))
        self.txt_data_nascimento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ex.. 00/00/0000", None))
        self.label_rg.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">RG</span></p></body></html>", None))
        self.txt_rg.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ex.. 00.000.000-00", None))
        self.label_cpf.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">CPF</span></p></body></html>", None))
        self.txt_cpf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ex.. 000.000.000-00", None))
        self.label_cep.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">CEP</span></p></body></html>", None))
        self.txt_cep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ex.. 00000-000", None))
        self.label_estado.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Estado</span></p></body></html>", None))
        self.perfil_estado.setItemText(0, QCoreApplication.translate("MainWindow", u"AC", None))
        self.perfil_estado.setItemText(1, QCoreApplication.translate("MainWindow", u"AL", None))
        self.perfil_estado.setItemText(2, QCoreApplication.translate("MainWindow", u"AP", None))
        self.perfil_estado.setItemText(3, QCoreApplication.translate("MainWindow", u"AM", None))
        self.perfil_estado.setItemText(4, QCoreApplication.translate("MainWindow", u"BA", None))
        self.perfil_estado.setItemText(5, QCoreApplication.translate("MainWindow", u"CE", None))
        self.perfil_estado.setItemText(6, QCoreApplication.translate("MainWindow", u"DF", None))
        self.perfil_estado.setItemText(7, QCoreApplication.translate("MainWindow", u"ES", None))
        self.perfil_estado.setItemText(8, QCoreApplication.translate("MainWindow", u"GO", None))
        self.perfil_estado.setItemText(9, QCoreApplication.translate("MainWindow", u"MA", None))
        self.perfil_estado.setItemText(10, QCoreApplication.translate("MainWindow", u"MT", None))
        self.perfil_estado.setItemText(11, QCoreApplication.translate("MainWindow", u"MS", None))
        self.perfil_estado.setItemText(12, QCoreApplication.translate("MainWindow", u"MG", None))
        self.perfil_estado.setItemText(13, QCoreApplication.translate("MainWindow", u"PA", None))
        self.perfil_estado.setItemText(14, QCoreApplication.translate("MainWindow", u"PB", None))
        self.perfil_estado.setItemText(15, QCoreApplication.translate("MainWindow", u"PR", None))
        self.perfil_estado.setItemText(16, QCoreApplication.translate("MainWindow", u"PE", None))
        self.perfil_estado.setItemText(17, QCoreApplication.translate("MainWindow", u"PI", None))
        self.perfil_estado.setItemText(18, QCoreApplication.translate("MainWindow", u"RJ", None))
        self.perfil_estado.setItemText(19, QCoreApplication.translate("MainWindow", u"RN", None))
        self.perfil_estado.setItemText(20, QCoreApplication.translate("MainWindow", u"RS", None))
        self.perfil_estado.setItemText(21, QCoreApplication.translate("MainWindow", u"RO", None))
        self.perfil_estado.setItemText(22, QCoreApplication.translate("MainWindow", u"RR", None))
        self.perfil_estado.setItemText(23, QCoreApplication.translate("MainWindow", u"SC", None))
        self.perfil_estado.setItemText(24, QCoreApplication.translate("MainWindow", u"SP", None))
        self.perfil_estado.setItemText(25, QCoreApplication.translate("MainWindow", u"SE", None))
        self.perfil_estado.setItemText(26, QCoreApplication.translate("MainWindow", u"TO", None))

        self.label_senha.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Senha</span></p></body></html>", None))
        self.label_confirmar_senha.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Confirmar senha</span></p></body></html>", None))
        self.label_perfil.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Perfil</span></p></body></html>", None))
        self.perfil_usuarios.setItemText(0, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.perfil_usuarios.setItemText(1, QCoreApplication.translate("MainWindow", u"Administrador", None))
        self.perfil_usuarios.setItemText(2, QCoreApplication.translate("MainWindow", u"Convidado", None))

        self.btn_editar_cadastro.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_atualizar_cadastro.setText(QCoreApplication.translate("MainWindow", u"Atualizar", None))
        self.btn_apagar_cadastro.setText(QCoreApplication.translate("MainWindow", u"Apagar", None))
        self.btn_carregar_imagem_4.setText(QCoreApplication.translate("MainWindow", u"Carregar imagem", None))
        self.btn_fazer_cadastro.setText(QCoreApplication.translate("MainWindow", u"Fazer cadastro", None))
        self.label_pagina_clientes.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; font-style:italic;\">P\u00c1GINA EM DESENVOLVIMENTO</span></p></body></html>", None))
        self.label_configuracoes.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; font-style:italic;\">CONFIGURA\u00c7\u00d5ES</span></p></body></html>", None))
        self.tool_tema.setText(QCoreApplication.translate("MainWindow", u"Tema do sistema", None))
        self.tool_atalhos.setText(QCoreApplication.translate("MainWindow", u"Atalhos do teclado", None))
        self.tool_hora.setText(QCoreApplication.translate("MainWindow", u"Hora e idioma", None))
        self.tool_fonte.setText(QCoreApplication.translate("MainWindow", u"Tamanho da fonte", None))
        self.tool_atualizacoes.setText(QCoreApplication.translate("MainWindow", u"Atualiza\u00e7\u00f5es", None))
        self.label_desenvolvido.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">Desenvolvido e publicado por:</span></p><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">Keven Lucas</span></p></body></html>", None))
        self.label_contato_keven.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">(19) 98201-8869</span></p></body></html>", None))
    # retranslateUi

