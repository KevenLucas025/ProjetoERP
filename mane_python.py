# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'novamaine.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDateEdit,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QToolButton,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1445, 820)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 820))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 80, 121);")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setFocusPolicy(Qt.StrongFocus)
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_5 = QSpacerItem(1130, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_5, 0, 1, 1, 1)

        self.frame_botoes_navegacoes = QFrame(self.centralwidget)
        self.frame_botoes_navegacoes.setObjectName(u"frame_botoes_navegacoes")
        sizePolicy.setHeightForWidth(self.frame_botoes_navegacoes.sizePolicy().hasHeightForWidth())
        self.frame_botoes_navegacoes.setSizePolicy(sizePolicy)
        self.frame_botoes_navegacoes.setMaximumSize(QSize(162, 16777215))
        self.frame_botoes_navegacoes.setAutoFillBackground(False)
        self.frame_botoes_navegacoes.setFrameShape(QFrame.NoFrame)
        self.frame_botoes_navegacoes.setFrameShadow(QFrame.Plain)
        self.gridLayout = QGridLayout(self.frame_botoes_navegacoes)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_configuracoes = QPushButton(self.frame_botoes_navegacoes)
        self.btn_configuracoes.setObjectName(u"btn_configuracoes")
        sizePolicy.setHeightForWidth(self.btn_configuracoes.sizePolicy().hasHeightForWidth())
        self.btn_configuracoes.setSizePolicy(sizePolicy)
        self.btn_configuracoes.setMaximumSize(QSize(145, 27))
        self.btn_configuracoes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_configuracoes.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")

        self.gridLayout.addWidget(self.btn_configuracoes, 6, 0, 1, 1)

        self.btn_verificar_usuarios = QPushButton(self.frame_botoes_navegacoes)
        self.btn_verificar_usuarios.setObjectName(u"btn_verificar_usuarios")
        sizePolicy.setHeightForWidth(self.btn_verificar_usuarios.sizePolicy().hasHeightForWidth())
        self.btn_verificar_usuarios.setSizePolicy(sizePolicy)
        self.btn_verificar_usuarios.setMaximumSize(QSize(145, 27))
        self.btn_verificar_usuarios.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_verificar_usuarios.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")

        self.gridLayout.addWidget(self.btn_verificar_usuarios, 2, 0, 1, 1)

        self.btn_home = QPushButton(self.frame_botoes_navegacoes)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMaximumSize(QSize(145, 27))
        self.btn_home.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_home.setAutoFillBackground(False)
        self.btn_home.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")

        self.gridLayout.addWidget(self.btn_home, 0, 0, 1, 1)

        self.btn_verificar_estoque = QPushButton(self.frame_botoes_navegacoes)
        self.btn_verificar_estoque.setObjectName(u"btn_verificar_estoque")
        sizePolicy.setHeightForWidth(self.btn_verificar_estoque.sizePolicy().hasHeightForWidth())
        self.btn_verificar_estoque.setSizePolicy(sizePolicy)
        self.btn_verificar_estoque.setMaximumSize(QSize(145, 27))
        self.btn_verificar_estoque.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_verificar_estoque.setAutoFillBackground(False)
        self.btn_verificar_estoque.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")

        self.gridLayout.addWidget(self.btn_verificar_estoque, 1, 0, 1, 1)

        self.btn_clientes = QPushButton(self.frame_botoes_navegacoes)
        self.btn_clientes.setObjectName(u"btn_clientes")
        sizePolicy.setHeightForWidth(self.btn_clientes.sizePolicy().hasHeightForWidth())
        self.btn_clientes.setSizePolicy(sizePolicy)
        self.btn_clientes.setMaximumSize(QSize(145, 27))
        self.btn_clientes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_clientes.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")

        self.gridLayout.addWidget(self.btn_clientes, 5, 0, 1, 1)

        self.btn_cadastrar_usuarios = QPushButton(self.frame_botoes_navegacoes)
        self.btn_cadastrar_usuarios.setObjectName(u"btn_cadastrar_usuarios")
        sizePolicy.setHeightForWidth(self.btn_cadastrar_usuarios.sizePolicy().hasHeightForWidth())
        self.btn_cadastrar_usuarios.setSizePolicy(sizePolicy)
        self.btn_cadastrar_usuarios.setMaximumSize(QSize(145, 27))
        self.btn_cadastrar_usuarios.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cadastrar_usuarios.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")

        self.gridLayout.addWidget(self.btn_cadastrar_usuarios, 4, 0, 1, 1)

        self.btn_cadastrar_produto = QPushButton(self.frame_botoes_navegacoes)
        self.btn_cadastrar_produto.setObjectName(u"btn_cadastrar_produto")
        sizePolicy.setHeightForWidth(self.btn_cadastrar_produto.sizePolicy().hasHeightForWidth())
        self.btn_cadastrar_produto.setSizePolicy(sizePolicy)
        self.btn_cadastrar_produto.setMaximumSize(QSize(145, 27))
        self.btn_cadastrar_produto.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cadastrar_produto.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")

        self.gridLayout.addWidget(self.btn_cadastrar_produto, 3, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_botoes_navegacoes, 0, 0, 2, 1)

        self.btn_mais_opcoes = QToolButton(self.centralwidget)
        self.btn_mais_opcoes.setObjectName(u"btn_mais_opcoes")
        sizePolicy.setHeightForWidth(self.btn_mais_opcoes.sizePolicy().hasHeightForWidth())
        self.btn_mais_opcoes.setSizePolicy(sizePolicy)
        self.btn_mais_opcoes.setMaximumSize(QSize(120, 30))
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(11)
        self.btn_mais_opcoes.setFont(font)
        self.btn_mais_opcoes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_mais_opcoes.setStyleSheet(u"QToolButton {\n"
"                background-color: rgb(50, 150, 250);\n"
"                color: white;\n"
"                border-radius: 10px;\n"
"                border: 2px solid rgb(50, 150, 250);\n"
"                padding: 5px 10px;\n"
"            }\n"
"            QToolButton:hover {\n"
"                background-color: rgb(100, 180, 255);\n"
"                border: 2px solid rgb(100, 180, 255);\n"
"            }\n"
"            ")
        self.btn_mais_opcoes.setPopupMode(QToolButton.MenuButtonPopup)
        self.btn_mais_opcoes.setToolButtonStyle(Qt.ToolButtonTextOnly)

        self.gridLayout_2.addWidget(self.btn_mais_opcoes, 0, 2, 1, 1)

        self.paginas_sistemas = QStackedWidget(self.centralwidget)
        self.paginas_sistemas.setObjectName(u"paginas_sistemas")
        sizePolicy.setHeightForWidth(self.paginas_sistemas.sizePolicy().hasHeightForWidth())
        self.paginas_sistemas.setSizePolicy(sizePolicy)
        self.paginas_sistemas.setStyleSheet(u"")
        self.home_pag = QWidget()
        self.home_pag.setObjectName(u"home_pag")
        sizePolicy.setHeightForWidth(self.home_pag.sizePolicy().hasHeightForWidth())
        self.home_pag.setSizePolicy(sizePolicy)
        self.home_pag.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(self.home_pag)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame = QFrame(self.home_pag)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
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
        self.label_imagem_sistema.setFrameShape(QFrame.Box)
        self.label_imagem_sistema.setPixmap(QPixmap(u"../../../../Pictures/ProjetoERP/Projeto ERP/Projeto ERP/54206.cur"))
        self.label_imagem_sistema.setScaledContents(True)
        self.label_imagem_sistema.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_imagem_sistema.setWordWrap(False)
        self.label_imagem_sistema.setOpenExternalLinks(False)

        self.gridLayout_4.addWidget(self.label_imagem_sistema, 0, 0, 1, 1)

        self.label_bem_vindo = QLabel(self.frame)
        self.label_bem_vindo.setObjectName(u"label_bem_vindo")
        sizePolicy.setHeightForWidth(self.label_bem_vindo.sizePolicy().hasHeightForWidth())
        self.label_bem_vindo.setSizePolicy(sizePolicy)
        self.label_bem_vindo.setMaximumSize(QSize(502, 234))
        self.label_bem_vindo.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_bem_vindo, 2, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame, 1, 0, 1, 1)

        self.paginas_sistemas.addWidget(self.home_pag)
        self.pag_estoque = QWidget()
        self.pag_estoque.setObjectName(u"pag_estoque")
        sizePolicy.setHeightForWidth(self.pag_estoque.sizePolicy().hasHeightForWidth())
        self.pag_estoque.setSizePolicy(sizePolicy)
        self.gridLayout_5 = QGridLayout(self.pag_estoque)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame_pag_estoque = QFrame(self.pag_estoque)
        self.frame_pag_estoque.setObjectName(u"frame_pag_estoque")
        sizePolicy.setHeightForWidth(self.frame_pag_estoque.sizePolicy().hasHeightForWidth())
        self.frame_pag_estoque.setSizePolicy(sizePolicy)
        self.frame_pag_estoque.setMinimumSize(QSize(0, 0))
        self.frame_pag_estoque.setMaximumSize(QSize(16777215, 16777215))
        self.frame_pag_estoque.setStyleSheet(u"")
        self.frame_pag_estoque.setFrameShape(QFrame.NoFrame)
        self.frame_pag_estoque.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_pag_estoque)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tb_base = QTabWidget(self.frame_pag_estoque)
        self.tb_base.setObjectName(u"tb_base")
        self.tb_base.setMinimumSize(QSize(0, 0))
        self.tb_base.setMaximumSize(QSize(16777215, 16777215))
        self.tb_base.setStyleSheet(u"")
        self.tb_base.setUsesScrollButtons(False)
        self.tb_base.setMovable(False)
        self.tb_base.setTabBarAutoHide(False)
        self.tabela_base = QWidget()
        self.tabela_base.setObjectName(u"tabela_base")
        sizePolicy.setHeightForWidth(self.tabela_base.sizePolicy().hasHeightForWidth())
        self.tabela_base.setSizePolicy(sizePolicy)
        self.tabela_base.setStyleSheet(u"")
        self.gridLayout_7 = QGridLayout(self.tabela_base)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_abrir_planilha = QPushButton(self.tabela_base)
        self.btn_abrir_planilha.setObjectName(u"btn_abrir_planilha")
        self.btn_abrir_planilha.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_abrir_planilha.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")

        self.verticalLayout.addWidget(self.btn_abrir_planilha)

        self.line_excel = QLineEdit(self.tabela_base)
        self.line_excel.setObjectName(u"line_excel")
        self.line_excel.setStyleSheet(u"QLineEdit {\n"
"	color: black;\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150,250); /* Borda azul */\n"
"    border-radius: 12px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QLineEdit::placeholderText {\n"
"    color: black; /* Cor do texto do placeholder */\n"
"}\n"
"\n"
"")
        self.line_excel.setAlignment(Qt.AlignCenter)
        self.line_excel.setReadOnly(True)

        self.verticalLayout.addWidget(self.line_excel)

        self.progress_excel = QProgressBar(self.tabela_base)
        self.progress_excel.setObjectName(u"progress_excel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.progress_excel.sizePolicy().hasHeightForWidth())
        self.progress_excel.setSizePolicy(sizePolicy1)
        self.progress_excel.setStyleSheet(u"QProgressBar {\n"
"	color: black;\n"
"    border: 3px solid rgb(50,150,250);\n"
"    border-radius: 13px;  /* Aumentei o valor para deixar a borda mais redonda */\n"
"    background-color: #f0f0f0;  /* Cor cinza claro */\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #4682b4;  /* Cor do progresso preenchido (azul) */\n"
"    border-radius: 12px;  /* Faz com que o progresso tamb\u00e9m tenha bordas arredondadas */\n"
"}\n"
"")
        self.progress_excel.setValue(0)
        self.progress_excel.setAlignment(Qt.AlignCenter)
        self.progress_excel.setTextVisible(True)
        self.progress_excel.setInvertedAppearance(False)

        self.verticalLayout.addWidget(self.progress_excel)


        self.gridLayout_7.addLayout(self.verticalLayout, 0, 0, 1, 8)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 2, 0, 0)
        self.btn_novo_produto = QPushButton(self.tabela_base)
        self.btn_novo_produto.setObjectName(u"btn_novo_produto")
        sizePolicy.setHeightForWidth(self.btn_novo_produto.sizePolicy().hasHeightForWidth())
        self.btn_novo_produto.setSizePolicy(sizePolicy)
        self.btn_novo_produto.setMaximumSize(QSize(163, 30))
        self.btn_novo_produto.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_novo_produto.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_novo_produto)

        self.btn_atualizar_saida = QPushButton(self.tabela_base)
        self.btn_atualizar_saida.setObjectName(u"btn_atualizar_saida")
        sizePolicy.setHeightForWidth(self.btn_atualizar_saida.sizePolicy().hasHeightForWidth())
        self.btn_atualizar_saida.setSizePolicy(sizePolicy)
        self.btn_atualizar_saida.setMaximumSize(QSize(163, 30))
        self.btn_atualizar_saida.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_atualizar_saida.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_atualizar_saida)

        self.btn_atualizar_estoque = QPushButton(self.tabela_base)
        self.btn_atualizar_estoque.setObjectName(u"btn_atualizar_estoque")
        sizePolicy.setHeightForWidth(self.btn_atualizar_estoque.sizePolicy().hasHeightForWidth())
        self.btn_atualizar_estoque.setSizePolicy(sizePolicy)
        self.btn_atualizar_estoque.setMaximumSize(QSize(163, 30))
        self.btn_atualizar_estoque.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_atualizar_estoque.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_atualizar_estoque)

        self.btn_historico = QPushButton(self.tabela_base)
        self.btn_historico.setObjectName(u"btn_historico")
        sizePolicy.setHeightForWidth(self.btn_historico.sizePolicy().hasHeightForWidth())
        self.btn_historico.setSizePolicy(sizePolicy)
        self.btn_historico.setMaximumSize(QSize(163, 30))
        self.btn_historico.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_historico.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_historico)

        self.btn_gerar_pdf = QPushButton(self.tabela_base)
        self.btn_gerar_pdf.setObjectName(u"btn_gerar_pdf")
        sizePolicy.setHeightForWidth(self.btn_gerar_pdf.sizePolicy().hasHeightForWidth())
        self.btn_gerar_pdf.setSizePolicy(sizePolicy)
        self.btn_gerar_pdf.setMaximumSize(QSize(163, 30))
        self.btn_gerar_pdf.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_gerar_pdf.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_gerar_pdf)

        self.btn_limpar_tabelas = QPushButton(self.tabela_base)
        self.btn_limpar_tabelas.setObjectName(u"btn_limpar_tabelas")
        sizePolicy.setHeightForWidth(self.btn_limpar_tabelas.sizePolicy().hasHeightForWidth())
        self.btn_limpar_tabelas.setSizePolicy(sizePolicy)
        self.btn_limpar_tabelas.setMaximumSize(QSize(163, 30))
        self.btn_limpar_tabelas.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_limpar_tabelas.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_limpar_tabelas)

        self.btn_incluir_produto_sistema = QPushButton(self.tabela_base)
        self.btn_incluir_produto_sistema.setObjectName(u"btn_incluir_produto_sistema")
        sizePolicy.setHeightForWidth(self.btn_incluir_produto_sistema.sizePolicy().hasHeightForWidth())
        self.btn_incluir_produto_sistema.setSizePolicy(sizePolicy)
        self.btn_incluir_produto_sistema.setMaximumSize(QSize(163, 30))
        self.btn_incluir_produto_sistema.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_incluir_produto_sistema.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 13px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_incluir_produto_sistema)


        self.gridLayout_7.addLayout(self.verticalLayout_2, 0, 8, 5, 1)

        self.label_estoque = QLabel(self.tabela_base)
        self.label_estoque.setObjectName(u"label_estoque")
        sizePolicy.setHeightForWidth(self.label_estoque.sizePolicy().hasHeightForWidth())
        self.label_estoque.setSizePolicy(sizePolicy)
        self.label_estoque.setMaximumSize(QSize(135, 40))
        self.label_estoque.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"	border: 3px solid white;\n"
"}\n"
"")

        self.gridLayout_7.addWidget(self.label_estoque, 1, 0, 1, 6)

        self.table_base = QTableWidget(self.tabela_base)
        if (self.table_base.columnCount() < 11):
            self.table_base.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_base.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_base.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_base.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_base.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_base.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_base.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_base.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_base.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_base.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_base.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_base.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.table_base.setObjectName(u"table_base")
        self.table_base.setMinimumSize(QSize(0, 0))
        self.table_base.setMaximumSize(QSize(16777215, 16777215))
        self.table_base.setStyleSheet(u"/* Estiliza apenas o QTableView com objectName \"table_ativos\" */\n"
"QTableView {\n"
"    gridline-color: black;\n"
"    border: 2px solid white;\n"
"    color: black;\n"
"    selection-color: white;\n"
"}\n"
"\n"
"/* Estiliza a barra de rolagem horizontal */\n"
"QTableView QScrollBar:horizontal {\n"
"    border: none;\n"
"    background-color: rgb(255, 255, 255);\n"
"    height: 15px;\n"
"    margin: 0px 10px 0px 10px;\n"
"}\n"
"\n"
"/* Estiliza a barra de rolagem vertical */\n"
"QTableView QScrollBar:vertical {\n"
"    border: none;\n"
"    background-color: rgb(255, 255, 255); /* branco */\n"
"    width: 35px;\n"
"    margin: 0px 10px 0px 10px;\n"
"}\n"
"\n"
"/* Parte que voc\u00ea arrasta */\n"
"QTableView QScrollBar::handle:vertical {\n"
"    background-color: rgb(180, 180,150);  /* cinza */\n"
"    min-height: 30px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QTableView QScrollBar::handle:horizontal{\n"
"	background-color: rgb(180,180,150);\n"
"	min-height: 30px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"/* "
                        "Remove os bot\u00f5es */\n"
"QTableView QScrollBar::add-line:vertical,\n"
"QTableView QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"    width: 0px;\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"QTableView QScrollBar::groove:horizontal{\n"
"	background-color: rgb(100,240,240);\n"
"	border-radius: 2px;\n"
"	height: 15px;\n"
"	margin: 0px 10px 0px 10px;\n"
"}\n"
"\n"
"/* Estilo para item selecionado */\n"
"QTableWidget::item:selected {\n"
"    background-color: rgb(0, 120, 215);\n"
"    color: white;\n"
"}")
        self.table_base.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_base.setProperty(u"showDropIndicator", True)
        self.table_base.setDragDropOverwriteMode(True)
        self.table_base.setAlternatingRowColors(False)
        self.table_base.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_base.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_base.setShowGrid(True)
        self.table_base.setGridStyle(Qt.SolidLine)
        self.table_base.setCornerButtonEnabled(False)
        self.table_base.horizontalHeader().setCascadingSectionResizes(False)
        self.table_base.horizontalHeader().setMinimumSectionSize(39)
        self.table_base.horizontalHeader().setDefaultSectionSize(112)
        self.table_base.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.table_base.verticalHeader().setVisible(False)
        self.table_base.verticalHeader().setCascadingSectionResizes(False)
        self.table_base.verticalHeader().setHighlightSections(True)

        self.gridLayout_7.addWidget(self.table_base, 2, 0, 1, 6)

        self.label_saida = QLabel(self.tabela_base)
        self.label_saida.setObjectName(u"label_saida")
        sizePolicy.setHeightForWidth(self.label_saida.sizePolicy().hasHeightForWidth())
        self.label_saida.setSizePolicy(sizePolicy)
        self.label_saida.setMaximumSize(QSize(100, 40))
        self.label_saida.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"	border: 3px solid white;\n"
"}")

        self.gridLayout_7.addWidget(self.label_saida, 3, 0, 1, 1)

        self.table_saida = QTableWidget(self.tabela_base)
        if (self.table_saida.columnCount() < 12):
            self.table_saida.setColumnCount(12)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_saida.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table_saida.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table_saida.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table_saida.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table_saida.setHorizontalHeaderItem(4, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.table_saida.setHorizontalHeaderItem(5, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.table_saida.setHorizontalHeaderItem(6, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.table_saida.setHorizontalHeaderItem(7, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.table_saida.setHorizontalHeaderItem(8, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.table_saida.setHorizontalHeaderItem(9, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.table_saida.setHorizontalHeaderItem(10, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.table_saida.setHorizontalHeaderItem(11, __qtablewidgetitem22)
        self.table_saida.setObjectName(u"table_saida")
        self.table_saida.setStyleSheet(u"/* Estiliza apenas o QTableView com objectName \"table_ativos\" */\n"
"QTableView {\n"
"    gridline-color: black;\n"
"    border: 2px solid white;\n"
"    color: black;\n"
"    selection-color: white;\n"
"}\n"
"\n"
"/* Estiliza a barra de rolagem horizontal */\n"
"QTableView QScrollBar:horizontal {\n"
"    border: none;\n"
"    background-color: rgb(255, 255, 255);\n"
"    height: 15px;\n"
"    margin: 0px 10px 0px 10px;\n"
"}\n"
"\n"
"/* Estiliza a barra de rolagem vertical */\n"
"QTableView QScrollBar:vertical {\n"
"    border: none;\n"
"    background-color: rgb(255, 255, 255); /* branco */\n"
"    width: 35px;\n"
"    margin: 0px 10px 0px 10px;\n"
"}\n"
"\n"
"/* Parte que voc\u00ea arrasta */\n"
"QTableView QScrollBar::handle:vertical {\n"
"    background-color: rgb(180, 180,150);  /* cinza */\n"
"    min-height: 30px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QTableView QScrollBar::handle:horizontal{\n"
"	background-color: rgb(180,180,150);\n"
"	min-height: 30px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"/* "
                        "Remove os bot\u00f5es */\n"
"QTableView QScrollBar::add-line:vertical,\n"
"QTableView QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"    width: 0px;\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"QTableView QScrollBar::groove:horizontal{\n"
"	background-color: rgb(100,240,240);\n"
"	border-radius: 2px;\n"
"	height: 15px;\n"
"	margin: 0px 10px 0px 10px;\n"
"}\n"
"\n"
"/* Estilo para item selecionado */\n"
"QTableWidget::item:selected {\n"
"    background-color: rgb(0, 120, 215);\n"
"    color: white;\n"
"}")
        self.table_saida.setFrameShadow(QFrame.Sunken)
        self.table_saida.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_saida.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_saida.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_saida.setCornerButtonEnabled(False)
        self.table_saida.horizontalHeader().setCascadingSectionResizes(False)
        self.table_saida.horizontalHeader().setDefaultSectionSize(112)
        self.table_saida.verticalHeader().setCascadingSectionResizes(False)

        self.gridLayout_7.addWidget(self.table_saida, 4, 0, 1, 8)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer, 3, 2, 1, 1)

        self.btn_importar = QPushButton(self.tabela_base)
        self.btn_importar.setObjectName(u"btn_importar")
        sizePolicy.setHeightForWidth(self.btn_importar.sizePolicy().hasHeightForWidth())
        self.btn_importar.setSizePolicy(sizePolicy)
        self.btn_importar.setMaximumSize(QSize(148, 28))
        self.btn_importar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
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
"}")

        self.gridLayout_7.addWidget(self.btn_importar, 3, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_2, 3, 4, 1, 1)

        self.btn_gerar_saida = QPushButton(self.tabela_base)
        self.btn_gerar_saida.setObjectName(u"btn_gerar_saida")
        sizePolicy.setHeightForWidth(self.btn_gerar_saida.sizePolicy().hasHeightForWidth())
        self.btn_gerar_saida.setSizePolicy(sizePolicy)
        self.btn_gerar_saida.setMaximumSize(QSize(148, 28))
        self.btn_gerar_saida.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
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
"}")

        self.gridLayout_7.addWidget(self.btn_gerar_saida, 3, 5, 1, 1)

        self.btn_gerar_estorno = QPushButton(self.tabela_base)
        self.btn_gerar_estorno.setObjectName(u"btn_gerar_estorno")
        sizePolicy.setHeightForWidth(self.btn_gerar_estorno.sizePolicy().hasHeightForWidth())
        self.btn_gerar_estorno.setSizePolicy(sizePolicy)
        self.btn_gerar_estorno.setMaximumSize(QSize(148, 28))
        self.btn_gerar_estorno.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
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
"}")

        self.gridLayout_7.addWidget(self.btn_gerar_estorno, 3, 1, 1, 1)

        self.tb_base.addTab(self.tabela_base, "")

        self.gridLayout_6.addWidget(self.tb_base, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_pag_estoque, 0, 0, 1, 1)

        self.paginas_sistemas.addWidget(self.pag_estoque)
        self.page_verificar_usuarios = QWidget()
        self.page_verificar_usuarios.setObjectName(u"page_verificar_usuarios")
        sizePolicy.setHeightForWidth(self.page_verificar_usuarios.sizePolicy().hasHeightForWidth())
        self.page_verificar_usuarios.setSizePolicy(sizePolicy)
        self.gridLayout_8 = QGridLayout(self.page_verificar_usuarios)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.frame_page_verificar_usuarios = QFrame(self.page_verificar_usuarios)
        self.frame_page_verificar_usuarios.setObjectName(u"frame_page_verificar_usuarios")
        sizePolicy.setHeightForWidth(self.frame_page_verificar_usuarios.sizePolicy().hasHeightForWidth())
        self.frame_page_verificar_usuarios.setSizePolicy(sizePolicy)
        self.frame_page_verificar_usuarios.setMaximumSize(QSize(16777215, 910))
        self.frame_page_verificar_usuarios.setFrameShape(QFrame.NoFrame)
        self.frame_page_verificar_usuarios.setFrameShadow(QFrame.Raised)
        self.gridLayout_21 = QGridLayout(self.frame_page_verificar_usuarios)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.horizontalSpacer_12 = QSpacerItem(8, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_12, 3, 5, 1, 1)

        self.frame_5 = QFrame(self.frame_page_verificar_usuarios)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QSize(180, 0))
        self.frame_5.setMaximumSize(QSize(180, 16777215))
        self.frame_5.setFrameShape(QFrame.Box)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_5)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.btn_atualizar_ativos = QPushButton(self.frame_5)
        self.btn_atualizar_ativos.setObjectName(u"btn_atualizar_ativos")
        sizePolicy.setHeightForWidth(self.btn_atualizar_ativos.sizePolicy().hasHeightForWidth())
        self.btn_atualizar_ativos.setSizePolicy(sizePolicy)
        self.btn_atualizar_ativos.setMaximumSize(QSize(185, 30))
        self.btn_atualizar_ativos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_atualizar_ativos.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")

        self.gridLayout_9.addWidget(self.btn_atualizar_ativos, 1, 0, 1, 1)

        self.btn_cadastrar_novo_usuario = QPushButton(self.frame_5)
        self.btn_cadastrar_novo_usuario.setObjectName(u"btn_cadastrar_novo_usuario")
        sizePolicy.setHeightForWidth(self.btn_cadastrar_novo_usuario.sizePolicy().hasHeightForWidth())
        self.btn_cadastrar_novo_usuario.setSizePolicy(sizePolicy)
        self.btn_cadastrar_novo_usuario.setMinimumSize(QSize(0, 0))
        self.btn_cadastrar_novo_usuario.setMaximumSize(QSize(185, 30))
        self.btn_cadastrar_novo_usuario.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cadastrar_novo_usuario.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")

        self.gridLayout_9.addWidget(self.btn_cadastrar_novo_usuario, 0, 0, 1, 1)

        self.btn_limpar_tabelas_usuarios = QPushButton(self.frame_5)
        self.btn_limpar_tabelas_usuarios.setObjectName(u"btn_limpar_tabelas_usuarios")
        sizePolicy.setHeightForWidth(self.btn_limpar_tabelas_usuarios.sizePolicy().hasHeightForWidth())
        self.btn_limpar_tabelas_usuarios.setSizePolicy(sizePolicy)
        self.btn_limpar_tabelas_usuarios.setMaximumSize(QSize(185, 30))
        self.btn_limpar_tabelas_usuarios.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_limpar_tabelas_usuarios.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")

        self.gridLayout_9.addWidget(self.btn_limpar_tabelas_usuarios, 4, 0, 1, 1)

        self.btn_atualizar_inativos = QPushButton(self.frame_5)
        self.btn_atualizar_inativos.setObjectName(u"btn_atualizar_inativos")
        sizePolicy.setHeightForWidth(self.btn_atualizar_inativos.sizePolicy().hasHeightForWidth())
        self.btn_atualizar_inativos.setSizePolicy(sizePolicy)
        self.btn_atualizar_inativos.setMaximumSize(QSize(185, 30))
        self.btn_atualizar_inativos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_atualizar_inativos.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")

        self.gridLayout_9.addWidget(self.btn_atualizar_inativos, 3, 0, 1, 1)

        self.btn_historico_usuarios = QPushButton(self.frame_5)
        self.btn_historico_usuarios.setObjectName(u"btn_historico_usuarios")
        sizePolicy.setHeightForWidth(self.btn_historico_usuarios.sizePolicy().hasHeightForWidth())
        self.btn_historico_usuarios.setSizePolicy(sizePolicy)
        self.btn_historico_usuarios.setMaximumSize(QSize(185, 30))
        self.btn_historico_usuarios.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_historico_usuarios.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")

        self.gridLayout_9.addWidget(self.btn_historico_usuarios, 2, 0, 1, 1)


        self.gridLayout_21.addWidget(self.frame_5, 0, 6, 5, 1)

        self.frame_4 = QFrame(self.frame_page_verificar_usuarios)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMaximumSize(QSize(16777215, 60))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_inativos = QLabel(self.frame_4)
        self.label_inativos.setObjectName(u"label_inativos")
        sizePolicy.setHeightForWidth(self.label_inativos.sizePolicy().hasHeightForWidth())
        self.label_inativos.setSizePolicy(sizePolicy)
        self.label_inativos.setMinimumSize(QSize(0, 0))
        self.label_inativos.setMaximumSize(QSize(143, 40))
        self.label_inativos.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"	border: 3px solid white;\n"
"}\n"
"")
        self.label_inativos.setScaledContents(False)

        self.horizontalLayout_24.addWidget(self.label_inativos)


        self.gridLayout_21.addWidget(self.frame_4, 3, 0, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(128, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_10, 3, 1, 1, 1)

        self.btn_gerar_saida_usuarios = QPushButton(self.frame_page_verificar_usuarios)
        self.btn_gerar_saida_usuarios.setObjectName(u"btn_gerar_saida_usuarios")
        sizePolicy.setHeightForWidth(self.btn_gerar_saida_usuarios.sizePolicy().hasHeightForWidth())
        self.btn_gerar_saida_usuarios.setSizePolicy(sizePolicy)
        self.btn_gerar_saida_usuarios.setMinimumSize(QSize(140, 0))
        self.btn_gerar_saida_usuarios.setMaximumSize(QSize(16777215, 30))
        self.btn_gerar_saida_usuarios.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_gerar_saida_usuarios.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")

        self.gridLayout_21.addWidget(self.btn_gerar_saida_usuarios, 3, 4, 1, 1)

        self.btn_importar_usuarios = QPushButton(self.frame_page_verificar_usuarios)
        self.btn_importar_usuarios.setObjectName(u"btn_importar_usuarios")
        sizePolicy.setHeightForWidth(self.btn_importar_usuarios.sizePolicy().hasHeightForWidth())
        self.btn_importar_usuarios.setSizePolicy(sizePolicy)
        self.btn_importar_usuarios.setMinimumSize(QSize(140, 0))
        self.btn_importar_usuarios.setMaximumSize(QSize(16777215, 30))
        self.btn_importar_usuarios.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_importar_usuarios.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")

        self.gridLayout_21.addWidget(self.btn_importar_usuarios, 3, 2, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(155, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_11, 3, 3, 1, 1)

        self.label_ativos = QLabel(self.frame_page_verificar_usuarios)
        self.label_ativos.setObjectName(u"label_ativos")
        sizePolicy.setHeightForWidth(self.label_ativos.sizePolicy().hasHeightForWidth())
        self.label_ativos.setSizePolicy(sizePolicy)
        self.label_ativos.setMaximumSize(QSize(135, 40))
        self.label_ativos.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"	border: 3px solid white;\n"
"}\n"
"")

        self.gridLayout_21.addWidget(self.label_ativos, 1, 0, 1, 1)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.btn_abrir_planilha_usuarios = QPushButton(self.frame_page_verificar_usuarios)
        self.btn_abrir_planilha_usuarios.setObjectName(u"btn_abrir_planilha_usuarios")
        self.btn_abrir_planilha_usuarios.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_abrir_planilha_usuarios.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")

        self.verticalLayout_19.addWidget(self.btn_abrir_planilha_usuarios)

        self.line_excel_usuarios = QLineEdit(self.frame_page_verificar_usuarios)
        self.line_excel_usuarios.setObjectName(u"line_excel_usuarios")
        self.line_excel_usuarios.setStyleSheet(u"QLineEdit {\n"
"	color: black;\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150,250); /* Borda azul */\n"
"    border-radius: 12px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QLineEdit::placeholderText {\n"
"    color: black; /* Cor do texto do placeholder */\n"
"}\n"
"\n"
"")
        self.line_excel_usuarios.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.line_excel_usuarios)

        self.progress_excel_usuarios = QProgressBar(self.frame_page_verificar_usuarios)
        self.progress_excel_usuarios.setObjectName(u"progress_excel_usuarios")
        sizePolicy1.setHeightForWidth(self.progress_excel_usuarios.sizePolicy().hasHeightForWidth())
        self.progress_excel_usuarios.setSizePolicy(sizePolicy1)
        self.progress_excel_usuarios.setStyleSheet(u"QProgressBar {\n"
"	color: black;\n"
"    border: 3px solid rgb(50,150,250);\n"
"    border-radius: 13px;  /* Aumentei o valor para deixar a borda mais redonda */\n"
"    background-color: #f0f0f0;  /* Cor cinza claro */\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #4682b4;  /* Cor do progresso preenchido (azul) */\n"
"    border-radius: 12px;  /* Faz com que o progresso tamb\u00e9m tenha bordas arredondadas */\n"
"}\n"
"")
        self.progress_excel_usuarios.setValue(0)
        self.progress_excel_usuarios.setAlignment(Qt.AlignCenter)
        self.progress_excel_usuarios.setTextVisible(True)
        self.progress_excel_usuarios.setInvertedAppearance(False)

        self.verticalLayout_19.addWidget(self.progress_excel_usuarios)


        self.gridLayout_21.addLayout(self.verticalLayout_19, 0, 0, 1, 6)

        self.table_inativos = QTableWidget(self.frame_page_verificar_usuarios)
        if (self.table_inativos.columnCount() < 24):
            self.table_inativos.setColumnCount(24)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.table_inativos.setHorizontalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.table_inativos.setHorizontalHeaderItem(1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.table_inativos.setHorizontalHeaderItem(2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.table_inativos.setHorizontalHeaderItem(3, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.table_inativos.setHorizontalHeaderItem(4, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.table_inativos.setHorizontalHeaderItem(5, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.table_inativos.setHorizontalHeaderItem(6, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.table_inativos.setHorizontalHeaderItem(7, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.table_inativos.setHorizontalHeaderItem(8, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.table_inativos.setHorizontalHeaderItem(9, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.table_inativos.setHorizontalHeaderItem(10, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.table_inativos.setHorizontalHeaderItem(11, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.table_inativos.setHorizontalHeaderItem(12, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.table_inativos.setHorizontalHeaderItem(13, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.table_inativos.setHorizontalHeaderItem(14, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.table_inativos.setHorizontalHeaderItem(15, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.table_inativos.setHorizontalHeaderItem(16, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.table_inativos.setHorizontalHeaderItem(17, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.table_inativos.setHorizontalHeaderItem(18, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.table_inativos.setHorizontalHeaderItem(19, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.table_inativos.setHorizontalHeaderItem(20, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.table_inativos.setHorizontalHeaderItem(21, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.table_inativos.setHorizontalHeaderItem(22, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.table_inativos.setHorizontalHeaderItem(23, __qtablewidgetitem46)
        self.table_inativos.setObjectName(u"table_inativos")
        self.table_inativos.setStyleSheet(u"/* Estiliza apenas o QTableView com objectName \"table_ativos\" */\n"
"QTableView {\n"
"    gridline-color: black;\n"
"    border: 2px solid white;\n"
"    color: black;\n"
"    selection-color: white;\n"
"}\n"
"\n"
"/* Estiliza a barra de rolagem horizontal */\n"
"QTableView QScrollBar:horizontal {\n"
"    border: none;\n"
"    background-color: rgb(255, 255, 255);\n"
"    height: 15px;\n"
"    margin: 0px 10px 0px 10px;\n"
"}\n"
"\n"
"/* Estiliza a barra de rolagem vertical */\n"
"QTableView QScrollBar:vertical {\n"
"    border: none;\n"
"    background-color: rgb(255, 255, 255); /* branco */\n"
"    width: 35px;\n"
"    margin: 0px 10px 0px 10px;\n"
"}\n"
"\n"
"/* Parte que voc\u00ea arrasta */\n"
"QTableView QScrollBar::handle:vertical {\n"
"    background-color: rgb(180, 180,150);  /* cinza */\n"
"    min-height: 30px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QTableView QScrollBar::handle:horizontal{\n"
"	background-color: rgb(180,180,150);\n"
"	min-height: 30px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"/* "
                        "Remove os bot\u00f5es */\n"
"QTableView QScrollBar::add-line:vertical,\n"
"QTableView QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"    width: 0px;\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"QTableView QScrollBar::groove:horizontal{\n"
"	background-color: rgb(100,240,240);\n"
"	border-radius: 2px;\n"
"	height: 15px;\n"
"	margin: 0px 10px 0px 10px;\n"
"}\n"
"\n"
"/* Estilo para item selecionado */\n"
"QTableWidget::item:selected {\n"
"    background-color: rgb(0, 120, 215);\n"
"    color: white;\n"
"}")
        self.table_inativos.setFrameShape(QFrame.NoFrame)
        self.table_inativos.setFrameShadow(QFrame.Sunken)
        self.table_inativos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_inativos.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_inativos.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_inativos.setCornerButtonEnabled(False)
        self.table_inativos.verticalHeader().setCascadingSectionResizes(False)

        self.gridLayout_21.addWidget(self.table_inativos, 4, 0, 1, 6)

        self.table_ativos = QTableWidget(self.frame_page_verificar_usuarios)
        if (self.table_ativos.columnCount() < 23):
            self.table_ativos.setColumnCount(23)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.table_ativos.setHorizontalHeaderItem(0, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.table_ativos.setHorizontalHeaderItem(1, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.table_ativos.setHorizontalHeaderItem(2, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.table_ativos.setHorizontalHeaderItem(3, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.table_ativos.setHorizontalHeaderItem(4, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.table_ativos.setHorizontalHeaderItem(5, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.table_ativos.setHorizontalHeaderItem(6, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.table_ativos.setHorizontalHeaderItem(7, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.table_ativos.setHorizontalHeaderItem(8, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.table_ativos.setHorizontalHeaderItem(9, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.table_ativos.setHorizontalHeaderItem(10, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.table_ativos.setHorizontalHeaderItem(11, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.table_ativos.setHorizontalHeaderItem(12, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.table_ativos.setHorizontalHeaderItem(13, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.table_ativos.setHorizontalHeaderItem(14, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.table_ativos.setHorizontalHeaderItem(15, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.table_ativos.setHorizontalHeaderItem(16, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.table_ativos.setHorizontalHeaderItem(17, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.table_ativos.setHorizontalHeaderItem(18, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.table_ativos.setHorizontalHeaderItem(19, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.table_ativos.setHorizontalHeaderItem(20, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.table_ativos.setHorizontalHeaderItem(21, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.table_ativos.setHorizontalHeaderItem(22, __qtablewidgetitem69)
        self.table_ativos.setObjectName(u"table_ativos")
        self.table_ativos.setMinimumSize(QSize(0, 0))
        self.table_ativos.setMaximumSize(QSize(16777215, 16777215))
        self.table_ativos.setStyleSheet(u"/* Estiliza apenas o QTableView com objectName \"table_ativos\" */\n"
"QTableView {\n"
"    gridline-color: black;\n"
"    border: 2px solid white;\n"
"    color: black;\n"
"    selection-color: white;\n"
"}\n"
"\n"
"/* Estiliza a barra de rolagem horizontal */\n"
"QTableView QScrollBar:horizontal {\n"
"    border: none;\n"
"    background-color: rgb(255, 255, 255);\n"
"    height: 15px;\n"
"    margin: 0px 10px 0px 10px;\n"
"}\n"
"\n"
"/* Estiliza a barra de rolagem vertical */\n"
"QTableView QScrollBar:vertical {\n"
"    border: none;\n"
"    background-color: rgb(255, 255, 255); /* branco */\n"
"    width: 35px;\n"
"    margin: 0px 10px 0px 10px;\n"
"}\n"
"\n"
"/* Parte que voc\u00ea arrasta */\n"
"QTableView QScrollBar::handle:vertical {\n"
"    background-color: rgb(180, 180,150);  /* cinza */\n"
"    min-height: 30px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QTableView QScrollBar::handle:horizontal{\n"
"	background-color: rgb(180,180,150);\n"
"	min-height: 30px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"/* "
                        "Remove os bot\u00f5es */\n"
"QTableView QScrollBar::add-line:vertical,\n"
"QTableView QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"    width: 0px;\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"QTableView QScrollBar::groove:horizontal{\n"
"	background-color: rgb(100,240,240);\n"
"	border-radius: 2px;\n"
"	height: 15px;\n"
"	margin: 0px 10px 0px 10px;\n"
"}\n"
"\n"
"/* Estilo para item selecionado */\n"
"QTableWidget::item:selected {\n"
"    background-color: rgb(0, 120, 215);\n"
"    color: white;\n"
"}")
        self.table_ativos.setFrameShape(QFrame.NoFrame)
        self.table_ativos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_ativos.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_ativos.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_ativos.setSortingEnabled(False)
        self.table_ativos.setCornerButtonEnabled(False)
        self.table_ativos.horizontalHeader().setCascadingSectionResizes(False)
        self.table_ativos.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.table_ativos.horizontalHeader().setStretchLastSection(False)
        self.table_ativos.verticalHeader().setVisible(False)
        self.table_ativos.verticalHeader().setCascadingSectionResizes(False)
        self.table_ativos.verticalHeader().setStretchLastSection(False)

        self.gridLayout_21.addWidget(self.table_ativos, 2, 0, 1, 6)


        self.gridLayout_8.addWidget(self.frame_page_verificar_usuarios, 0, 0, 1, 1)

        self.paginas_sistemas.addWidget(self.page_verificar_usuarios)
        self.pg_cadastrar_produto = QWidget()
        self.pg_cadastrar_produto.setObjectName(u"pg_cadastrar_produto")
        sizePolicy.setHeightForWidth(self.pg_cadastrar_produto.sizePolicy().hasHeightForWidth())
        self.pg_cadastrar_produto.setSizePolicy(sizePolicy)
        self.pg_cadastrar_produto.setStyleSheet(u"background-color: rgb(0, 80, 121);")
        self.gridLayout_10 = QGridLayout(self.pg_cadastrar_produto)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.frame_cadastrar_produto = QFrame(self.pg_cadastrar_produto)
        self.frame_cadastrar_produto.setObjectName(u"frame_cadastrar_produto")
        sizePolicy.setHeightForWidth(self.frame_cadastrar_produto.sizePolicy().hasHeightForWidth())
        self.frame_cadastrar_produto.setSizePolicy(sizePolicy)
        self.frame_cadastrar_produto.setStyleSheet(u"background-color: rgb(0, 80, 121);")
        self.frame_cadastrar_produto.setFrameShape(QFrame.NoFrame)
        self.frame_cadastrar_produto.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_cadastrar_produto)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.frame_botoes_a_e_a_a = QFrame(self.frame_cadastrar_produto)
        self.frame_botoes_a_e_a_a.setObjectName(u"frame_botoes_a_e_a_a")
        sizePolicy.setHeightForWidth(self.frame_botoes_a_e_a_a.sizePolicy().hasHeightForWidth())
        self.frame_botoes_a_e_a_a.setSizePolicy(sizePolicy)
        self.frame_botoes_a_e_a_a.setMinimumSize(QSize(177, 0))
        self.frame_botoes_a_e_a_a.setMaximumSize(QSize(200, 190))
        self.frame_botoes_a_e_a_a.setFrameShape(QFrame.NoFrame)
        self.frame_botoes_a_e_a_a.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_botoes_a_e_a_a)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.btn_adicionar_produto = QPushButton(self.frame_botoes_a_e_a_a)
        self.btn_adicionar_produto.setObjectName(u"btn_adicionar_produto")
        sizePolicy.setHeightForWidth(self.btn_adicionar_produto.sizePolicy().hasHeightForWidth())
        self.btn_adicionar_produto.setSizePolicy(sizePolicy)
        self.btn_adicionar_produto.setMaximumSize(QSize(16777215, 30))
        self.btn_adicionar_produto.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_adicionar_produto.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")
        icon = QIcon()
        icon.addFile(u"../../../../.designer/backup/imagens/pngwing.com.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_adicionar_produto.setIcon(icon)

        self.verticalLayout_12.addWidget(self.btn_adicionar_produto)

        self.btn_editar = QPushButton(self.frame_botoes_a_e_a_a)
        self.btn_editar.setObjectName(u"btn_editar")
        sizePolicy.setHeightForWidth(self.btn_editar.sizePolicy().hasHeightForWidth())
        self.btn_editar.setSizePolicy(sizePolicy)
        self.btn_editar.setMaximumSize(QSize(16777215, 30))
        self.btn_editar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_editar.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../../../../.designer/backup/imagens/editar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_editar.setIcon(icon1)

        self.verticalLayout_12.addWidget(self.btn_editar)

        self.btn_sair_modo_edicao_produtos = QPushButton(self.frame_botoes_a_e_a_a)
        self.btn_sair_modo_edicao_produtos.setObjectName(u"btn_sair_modo_edicao_produtos")
        sizePolicy.setHeightForWidth(self.btn_sair_modo_edicao_produtos.sizePolicy().hasHeightForWidth())
        self.btn_sair_modo_edicao_produtos.setSizePolicy(sizePolicy)
        self.btn_sair_modo_edicao_produtos.setMaximumSize(QSize(16777215, 30))
        self.btn_sair_modo_edicao_produtos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_sair_modo_edicao_produtos.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 14px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"../../../../.designer/backup/imagens/sair.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_sair_modo_edicao_produtos.setIcon(icon2)

        self.verticalLayout_12.addWidget(self.btn_sair_modo_edicao_produtos)

        self.btn_atualizar_produto = QPushButton(self.frame_botoes_a_e_a_a)
        self.btn_atualizar_produto.setObjectName(u"btn_atualizar_produto")
        sizePolicy.setHeightForWidth(self.btn_atualizar_produto.sizePolicy().hasHeightForWidth())
        self.btn_atualizar_produto.setSizePolicy(sizePolicy)
        self.btn_atualizar_produto.setMaximumSize(QSize(16777215, 30))
        self.btn_atualizar_produto.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_atualizar_produto.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"../../../../.designer/backup/imagens/toppng.com-update-512x512.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_atualizar_produto.setIcon(icon3)

        self.verticalLayout_12.addWidget(self.btn_atualizar_produto)

        self.btn_limpar_campos = QPushButton(self.frame_botoes_a_e_a_a)
        self.btn_limpar_campos.setObjectName(u"btn_limpar_campos")
        sizePolicy.setHeightForWidth(self.btn_limpar_campos.sizePolicy().hasHeightForWidth())
        self.btn_limpar_campos.setSizePolicy(sizePolicy)
        self.btn_limpar_campos.setMaximumSize(QSize(16777215, 30))
        self.btn_limpar_campos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_limpar_campos.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"../../../../.designer/backup/imagens/Delete-Button-PNG-Download-Image.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_limpar_campos.setIcon(icon4)
        self.btn_limpar_campos.setIconSize(QSize(27, 29))
        self.btn_limpar_campos.setCheckable(False)

        self.verticalLayout_12.addWidget(self.btn_limpar_campos)


        self.gridLayout_11.addWidget(self.frame_botoes_a_e_a_a, 2, 1, 1, 1)

        self.frame_2 = QFrame(self.frame_cadastrar_produto)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(340, 0))
        self.frame_2.setMaximumSize(QSize(331, 16777215))
        self.frame_2.setStyleSheet(u"background-color: rgb(0, 80, 121);")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_produto = QFrame(self.frame_2)
        self.frame_produto.setObjectName(u"frame_produto")
        self.frame_produto.setMaximumSize(QSize(328, 50))
        self.frame_produto.setFrameShape(QFrame.NoFrame)
        self.frame_produto.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_produto)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_produto = QLabel(self.frame_produto)
        self.label_produto.setObjectName(u"label_produto")
        self.label_produto.setStyleSheet(u"QLabel {\n"
"    color: black;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.label_produto)

        self.txt_produto = QLineEdit(self.frame_produto)
        self.txt_produto.setObjectName(u"txt_produto")
        sizePolicy.setHeightForWidth(self.txt_produto.sizePolicy().hasHeightForWidth())
        self.txt_produto.setSizePolicy(sizePolicy)
        self.txt_produto.setMinimumSize(QSize(0, 0))
        self.txt_produto.setMaximumSize(QSize(150, 26))
        self.txt_produto.setStyleSheet(u"QLineEdit {\n"
"	color: black;\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150,250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QLineEdit::placeholderText {\n"
"    color: black; /* Cor do texto do placeholder */\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.txt_produto)

        self.frame_erro_produto = QFrame(self.frame_produto)
        self.frame_erro_produto.setObjectName(u"frame_erro_produto")
        self.frame_erro_produto.setMaximumSize(QSize(21, 21))
        self.frame_erro_produto.setFrameShape(QFrame.NoFrame)
        self.frame_erro_produto.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_erro_produto)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.verticalLayout_11.addWidget(self.frame_produto)

        self.frame_quantidade_2 = QFrame(self.frame_2)
        self.frame_quantidade_2.setObjectName(u"frame_quantidade_2")
        self.frame_quantidade_2.setMaximumSize(QSize(328, 50))
        self.frame_quantidade_2.setFrameShape(QFrame.NoFrame)
        self.frame_quantidade_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_quantidade_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_quantidade = QLabel(self.frame_quantidade_2)
        self.label_quantidade.setObjectName(u"label_quantidade")
        self.label_quantidade.setStyleSheet(u"QLabel {\n"
"    color: black;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.label_quantidade)

        self.txt_quantidade = QLineEdit(self.frame_quantidade_2)
        self.txt_quantidade.setObjectName(u"txt_quantidade")
        sizePolicy.setHeightForWidth(self.txt_quantidade.sizePolicy().hasHeightForWidth())
        self.txt_quantidade.setSizePolicy(sizePolicy)
        self.txt_quantidade.setMinimumSize(QSize(0, 0))
        self.txt_quantidade.setMaximumSize(QSize(150, 26))
        self.txt_quantidade.setStyleSheet(u"QLineEdit {\n"
"	color: black;\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150,250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QLineEdit::placeholderText {\n"
"    color: black; /* Cor do texto do placeholder */\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.txt_quantidade)

        self.frame_erro_quantidade = QFrame(self.frame_quantidade_2)
        self.frame_erro_quantidade.setObjectName(u"frame_erro_quantidade")
        self.frame_erro_quantidade.setMaximumSize(QSize(21, 21))
        self.frame_erro_quantidade.setFrameShape(QFrame.NoFrame)
        self.frame_erro_quantidade.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_erro_quantidade)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout_11.addWidget(self.frame_quantidade_2)

        self.frame_valor_produto = QFrame(self.frame_2)
        self.frame_valor_produto.setObjectName(u"frame_valor_produto")
        self.frame_valor_produto.setMaximumSize(QSize(328, 50))
        self.frame_valor_produto.setStyleSheet(u"background-color: rgb(0, 80, 121);")
        self.frame_valor_produto.setFrameShape(QFrame.NoFrame)
        self.frame_valor_produto.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_valor_produto)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_valor_produto_3 = QLabel(self.frame_valor_produto)
        self.label_valor_produto_3.setObjectName(u"label_valor_produto_3")
        self.label_valor_produto_3.setStyleSheet(u"QLabel {\n"
"    color: black;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.label_valor_produto_3)

        self.txt_valor_produto_3 = QLineEdit(self.frame_valor_produto)
        self.txt_valor_produto_3.setObjectName(u"txt_valor_produto_3")
        self.txt_valor_produto_3.setMinimumSize(QSize(0, 0))
        self.txt_valor_produto_3.setMaximumSize(QSize(150, 26))
        self.txt_valor_produto_3.setStyleSheet(u"QLineEdit {\n"
"	color: black;\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150,250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QLineEdit::placeholderText {\n"
"    color: black; /* Cor do texto do placeholder */\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.txt_valor_produto_3)

        self.frame_erro_valor_produto = QFrame(self.frame_valor_produto)
        self.frame_erro_valor_produto.setObjectName(u"frame_erro_valor_produto")
        self.frame_erro_valor_produto.setMaximumSize(QSize(21, 21))
        self.frame_erro_valor_produto.setFrameShape(QFrame.NoFrame)
        self.frame_erro_valor_produto.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_erro_valor_produto)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)


        self.verticalLayout_11.addWidget(self.frame_valor_produto)

        self.frame_desconto = QFrame(self.frame_2)
        self.frame_desconto.setObjectName(u"frame_desconto")
        self.frame_desconto.setMaximumSize(QSize(328, 50))
        self.frame_desconto.setStyleSheet(u"background-color: rgb(0, 80, 121);")
        self.frame_desconto.setFrameShape(QFrame.NoFrame)
        self.frame_desconto.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_desconto)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_desconto_3 = QLabel(self.frame_desconto)
        self.label_desconto_3.setObjectName(u"label_desconto_3")
        self.label_desconto_3.setStyleSheet(u"QLabel {\n"
"    color: black;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.label_desconto_3)

        self.txt_desconto_3 = QLineEdit(self.frame_desconto)
        self.txt_desconto_3.setObjectName(u"txt_desconto_3")
        self.txt_desconto_3.setMinimumSize(QSize(0, 0))
        self.txt_desconto_3.setMaximumSize(QSize(150, 26))
        self.txt_desconto_3.setStyleSheet(u"QLineEdit {\n"
"	color: black;\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150,250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QLineEdit::placeholderText {\n"
"    color: black; /* Cor do texto do placeholder */\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.txt_desconto_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)


        self.verticalLayout_11.addWidget(self.frame_desconto)

        self.frame_data_compra = QFrame(self.frame_2)
        self.frame_data_compra.setObjectName(u"frame_data_compra")
        self.frame_data_compra.setMaximumSize(QSize(328, 50))
        self.frame_data_compra.setStyleSheet(u"background-color: rgb(0, 80, 121);")
        self.frame_data_compra.setFrameShape(QFrame.NoFrame)
        self.frame_data_compra.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_data_compra)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_data_cadastro = QLabel(self.frame_data_compra)
        self.label_data_cadastro.setObjectName(u"label_data_cadastro")
        self.label_data_cadastro.setStyleSheet(u"QLabel {\n"
"    color: black;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.horizontalLayout_5.addWidget(self.label_data_cadastro)

        self.dateEdit_3 = QDateEdit(self.frame_data_compra)
        self.dateEdit_3.setObjectName(u"dateEdit_3")
        sizePolicy1.setHeightForWidth(self.dateEdit_3.sizePolicy().hasHeightForWidth())
        self.dateEdit_3.setSizePolicy(sizePolicy1)
        self.dateEdit_3.setMinimumSize(QSize(150, 0))
        self.dateEdit_3.setMaximumSize(QSize(150, 26))
        self.dateEdit_3.setStyleSheet(u"QDateEdit {\n"
"    color: black; /* Cor do texto */\n"
"    background-color: white; /* Cor de fundo */\n"
"}\n"
"")
        self.dateEdit_3.setTime(QTime(3, 0, 0))
        self.dateEdit_3.setCalendarPopup(True)

        self.horizontalLayout_5.addWidget(self.dateEdit_3)

        self.frame_erro_data_cadastro = QFrame(self.frame_data_compra)
        self.frame_erro_data_cadastro.setObjectName(u"frame_erro_data_cadastro")
        self.frame_erro_data_cadastro.setMaximumSize(QSize(21, 21))
        self.frame_erro_data_cadastro.setFrameShape(QFrame.NoFrame)
        self.frame_erro_data_cadastro.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_erro_data_cadastro)


        self.verticalLayout_10.addLayout(self.horizontalLayout_5)


        self.verticalLayout_11.addWidget(self.frame_data_compra)

        self.frame_codigo_item = QFrame(self.frame_2)
        self.frame_codigo_item.setObjectName(u"frame_codigo_item")
        self.frame_codigo_item.setMaximumSize(QSize(328, 50))
        self.frame_codigo_item.setFrameShape(QFrame.NoFrame)
        self.frame_codigo_item.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_codigo_item)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_codigo_item_3 = QLabel(self.frame_codigo_item)
        self.label_codigo_item_3.setObjectName(u"label_codigo_item_3")
        self.label_codigo_item_3.setStyleSheet(u"QLabel {\n"
"    color: black;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.label_codigo_item_3)

        self.txt_codigo_item = QLineEdit(self.frame_codigo_item)
        self.txt_codigo_item.setObjectName(u"txt_codigo_item")
        self.txt_codigo_item.setMaximumSize(QSize(150, 26))
        self.txt_codigo_item.setStyleSheet(u"QLineEdit {\n"
"	color: black;\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150,250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QLineEdit::placeholderText {\n"
"    color: black; /* Cor do texto do placeholder */\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.txt_codigo_item)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)


        self.verticalLayout_11.addWidget(self.frame_codigo_item)

        self.frame_cliente = QFrame(self.frame_2)
        self.frame_cliente.setObjectName(u"frame_cliente")
        self.frame_cliente.setMaximumSize(QSize(328, 50))
        self.frame_cliente.setFrameShape(QFrame.NoFrame)
        self.frame_cliente.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_cliente)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_cliente_4 = QLabel(self.frame_cliente)
        self.label_cliente_4.setObjectName(u"label_cliente_4")
        self.label_cliente_4.setStyleSheet(u"QLabel {\n"
"    color: black;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.horizontalLayout_7.addWidget(self.label_cliente_4)

        self.txt_cliente_3 = QLineEdit(self.frame_cliente)
        self.txt_cliente_3.setObjectName(u"txt_cliente_3")
        self.txt_cliente_3.setMaximumSize(QSize(150, 26))
        self.txt_cliente_3.setStyleSheet(u"QLineEdit {\n"
"	color: black;\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150,250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QLineEdit::placeholderText {\n"
"    color: black; /* Cor do texto do placeholder */\n"
"}\n"
"")

        self.horizontalLayout_7.addWidget(self.txt_cliente_3)

        self.frame_erro_cliente = QFrame(self.frame_cliente)
        self.frame_erro_cliente.setObjectName(u"frame_erro_cliente")
        self.frame_erro_cliente.setMaximumSize(QSize(21, 21))
        self.frame_erro_cliente.setFrameShape(QFrame.NoFrame)
        self.frame_erro_cliente.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.frame_erro_cliente)


        self.verticalLayout_8.addLayout(self.horizontalLayout_7)


        self.verticalLayout_11.addWidget(self.frame_cliente)

        self.frame_descricao_produto = QFrame(self.frame_2)
        self.frame_descricao_produto.setObjectName(u"frame_descricao_produto")
        self.frame_descricao_produto.setMaximumSize(QSize(328, 50))
        self.frame_descricao_produto.setFrameShape(QFrame.NoFrame)
        self.frame_descricao_produto.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_descricao_produto)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_descricao_produto_3 = QLabel(self.frame_descricao_produto)
        self.label_descricao_produto_3.setObjectName(u"label_descricao_produto_3")
        self.label_descricao_produto_3.setStyleSheet(u"QLabel {\n"
"    color: black;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.horizontalLayout_8.addWidget(self.label_descricao_produto_3)

        self.txt_descricao_produto_3 = QLineEdit(self.frame_descricao_produto)
        self.txt_descricao_produto_3.setObjectName(u"txt_descricao_produto_3")
        self.txt_descricao_produto_3.setMinimumSize(QSize(0, 0))
        self.txt_descricao_produto_3.setMaximumSize(QSize(150, 26))
        self.txt_descricao_produto_3.setStyleSheet(u"QLineEdit {\n"
"	color: black;\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150,250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QLineEdit::placeholderText {\n"
"    color: black; /* Cor do texto do placeholder */\n"
"}\n"
"")

        self.horizontalLayout_8.addWidget(self.txt_descricao_produto_3)

        self.frame_erro_descricao = QFrame(self.frame_descricao_produto)
        self.frame_erro_descricao.setObjectName(u"frame_erro_descricao")
        self.frame_erro_descricao.setMinimumSize(QSize(21, 21))
        self.frame_erro_descricao.setMaximumSize(QSize(21, 21))
        self.frame_erro_descricao.setFrameShape(QFrame.NoFrame)
        self.frame_erro_descricao.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.frame_erro_descricao)


        self.verticalLayout_9.addLayout(self.horizontalLayout_8)


        self.verticalLayout_11.addWidget(self.frame_descricao_produto)


        self.gridLayout_11.addWidget(self.frame_2, 2, 0, 3, 1)

        self.label_cadastramento_produtos = QLabel(self.frame_cadastrar_produto)
        self.label_cadastramento_produtos.setObjectName(u"label_cadastramento_produtos")
        self.label_cadastramento_produtos.setMaximumSize(QSize(16777215, 50))
        self.label_cadastramento_produtos.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"	border: 3px solid white;\n"
"}\n"
"")

        self.gridLayout_11.addWidget(self.label_cadastramento_produtos, 0, 1, 1, 2)

        self.frame_imagem_produto_3 = QFrame(self.frame_cadastrar_produto)
        self.frame_imagem_produto_3.setObjectName(u"frame_imagem_produto_3")
        self.frame_imagem_produto_3.setMinimumSize(QSize(331, 321))
        self.frame_imagem_produto_3.setMaximumSize(QSize(331, 321))
        self.frame_imagem_produto_3.setFrameShape(QFrame.NoFrame)
        self.frame_imagem_produto_3.setFrameShadow(QFrame.Raised)

        self.gridLayout_11.addWidget(self.frame_imagem_produto_3, 2, 3, 3, 1)

        self.frame_remover_e_carregar_imagem = QFrame(self.frame_cadastrar_produto)
        self.frame_remover_e_carregar_imagem.setObjectName(u"frame_remover_e_carregar_imagem")
        sizePolicy.setHeightForWidth(self.frame_remover_e_carregar_imagem.sizePolicy().hasHeightForWidth())
        self.frame_remover_e_carregar_imagem.setSizePolicy(sizePolicy)
        self.frame_remover_e_carregar_imagem.setMaximumSize(QSize(200, 89))
        self.frame_remover_e_carregar_imagem.setFrameShape(QFrame.NoFrame)
        self.frame_remover_e_carregar_imagem.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_remover_e_carregar_imagem)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.btn_remover_imagem = QPushButton(self.frame_remover_e_carregar_imagem)
        self.btn_remover_imagem.setObjectName(u"btn_remover_imagem")
        sizePolicy.setHeightForWidth(self.btn_remover_imagem.sizePolicy().hasHeightForWidth())
        self.btn_remover_imagem.setSizePolicy(sizePolicy)
        self.btn_remover_imagem.setMaximumSize(QSize(170, 30))
        self.btn_remover_imagem.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_remover_imagem.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"../../../../.designer/backup/imagens/icons8-remover-imagem-16.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_remover_imagem.setIcon(icon5)

        self.verticalLayout_13.addWidget(self.btn_remover_imagem)

        self.btn_carregar_imagem = QPushButton(self.frame_remover_e_carregar_imagem)
        self.btn_carregar_imagem.setObjectName(u"btn_carregar_imagem")
        sizePolicy.setHeightForWidth(self.btn_carregar_imagem.sizePolicy().hasHeightForWidth())
        self.btn_carregar_imagem.setSizePolicy(sizePolicy)
        self.btn_carregar_imagem.setMinimumSize(QSize(153, 0))
        self.btn_carregar_imagem.setMaximumSize(QSize(180, 30))
        self.btn_carregar_imagem.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_carregar_imagem.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"../../../../.designer/backup/imagens/014upload2_99941.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_carregar_imagem.setIcon(icon6)

        self.verticalLayout_13.addWidget(self.btn_carregar_imagem)


        self.gridLayout_11.addWidget(self.frame_remover_e_carregar_imagem, 3, 1, 1, 1)

        self.frame_6 = QFrame(self.frame_cadastrar_produto)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMaximumSize(QSize(350, 16777215))
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_6)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_valor_total_produtos = QFrame(self.frame_6)
        self.frame_valor_total_produtos.setObjectName(u"frame_valor_total_produtos")
        sizePolicy.setHeightForWidth(self.frame_valor_total_produtos.sizePolicy().hasHeightForWidth())
        self.frame_valor_total_produtos.setSizePolicy(sizePolicy)
        self.frame_valor_total_produtos.setMinimumSize(QSize(321, 102))
        self.frame_valor_total_produtos.setMaximumSize(QSize(321, 102))
        self.frame_valor_total_produtos.setStyleSheet(u"background-color: rgb(100, 200, 100); /* Verde claro */\n"
"")
        self.frame_valor_total_produtos.setFrameShape(QFrame.StyledPanel)
        self.frame_valor_total_produtos.setFrameShadow(QFrame.Raised)

        self.verticalLayout_15.addWidget(self.frame_valor_total_produtos)

        self.frame_valor_do_desconto = QFrame(self.frame_6)
        self.frame_valor_do_desconto.setObjectName(u"frame_valor_do_desconto")
        sizePolicy.setHeightForWidth(self.frame_valor_do_desconto.sizePolicy().hasHeightForWidth())
        self.frame_valor_do_desconto.setSizePolicy(sizePolicy)
        self.frame_valor_do_desconto.setMinimumSize(QSize(0, 102))
        self.frame_valor_do_desconto.setMaximumSize(QSize(321, 102))
        self.frame_valor_do_desconto.setStyleSheet(u"background-color: rgb(100, 200, 100); /* Verde claro */\n"
"")
        self.frame_valor_do_desconto.setFrameShape(QFrame.StyledPanel)
        self.frame_valor_do_desconto.setFrameShadow(QFrame.Raised)

        self.verticalLayout_15.addWidget(self.frame_valor_do_desconto)

        self.frame_valor_com_desconto1 = QFrame(self.frame_6)
        self.frame_valor_com_desconto1.setObjectName(u"frame_valor_com_desconto1")
        sizePolicy.setHeightForWidth(self.frame_valor_com_desconto1.sizePolicy().hasHeightForWidth())
        self.frame_valor_com_desconto1.setSizePolicy(sizePolicy)
        self.frame_valor_com_desconto1.setMinimumSize(QSize(0, 102))
        self.frame_valor_com_desconto1.setMaximumSize(QSize(321, 102))
        self.frame_valor_com_desconto1.setStyleSheet(u"background-color: rgb(100, 200, 100); /* Verde claro */\n"
"")
        self.frame_valor_com_desconto1.setFrameShape(QFrame.StyledPanel)
        self.frame_valor_com_desconto1.setFrameShadow(QFrame.Raised)

        self.verticalLayout_15.addWidget(self.frame_valor_com_desconto1)

        self.frame_quantidade = QFrame(self.frame_6)
        self.frame_quantidade.setObjectName(u"frame_quantidade")
        sizePolicy.setHeightForWidth(self.frame_quantidade.sizePolicy().hasHeightForWidth())
        self.frame_quantidade.setSizePolicy(sizePolicy)
        self.frame_quantidade.setMinimumSize(QSize(0, 102))
        self.frame_quantidade.setMaximumSize(QSize(321, 102))
        self.frame_quantidade.setStyleSheet(u"background-color: rgb(100, 200, 100); /* Verde claro */\n"
"")
        self.frame_quantidade.setFrameShape(QFrame.StyledPanel)
        self.frame_quantidade.setFrameShadow(QFrame.Raised)

        self.verticalLayout_15.addWidget(self.frame_quantidade)


        self.gridLayout_11.addWidget(self.frame_6, 2, 2, 3, 1)

        self.frame_confirmar_ver_produto = QFrame(self.frame_cadastrar_produto)
        self.frame_confirmar_ver_produto.setObjectName(u"frame_confirmar_ver_produto")
        sizePolicy.setHeightForWidth(self.frame_confirmar_ver_produto.sizePolicy().hasHeightForWidth())
        self.frame_confirmar_ver_produto.setSizePolicy(sizePolicy)
        self.frame_confirmar_ver_produto.setMaximumSize(QSize(200, 200))
        self.frame_confirmar_ver_produto.setFrameShape(QFrame.NoFrame)
        self.frame_confirmar_ver_produto.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_confirmar_ver_produto)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.btn_confirmar = QPushButton(self.frame_confirmar_ver_produto)
        self.btn_confirmar.setObjectName(u"btn_confirmar")
        sizePolicy.setHeightForWidth(self.btn_confirmar.sizePolicy().hasHeightForWidth())
        self.btn_confirmar.setSizePolicy(sizePolicy)
        self.btn_confirmar.setMinimumSize(QSize(0, 0))
        self.btn_confirmar.setMaximumSize(QSize(177, 30))
        self.btn_confirmar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_confirmar.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255); /* Cor do texto (branco) */\n"
"    border-radius: 10px;\n"
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
        icon7 = QIcon()
        icon7.addFile(u"../../../../.designer/backup/imagens/confirmacao.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_confirmar.setIcon(icon7)

        self.verticalLayout_20.addWidget(self.btn_confirmar)

        self.btn_ver_clientes_juridicos = QPushButton(self.frame_confirmar_ver_produto)
        self.btn_ver_clientes_juridicos.setObjectName(u"btn_ver_clientes_juridicos")
        sizePolicy.setHeightForWidth(self.btn_ver_clientes_juridicos.sizePolicy().hasHeightForWidth())
        self.btn_ver_clientes_juridicos.setSizePolicy(sizePolicy)
        self.btn_ver_clientes_juridicos.setMaximumSize(QSize(16777215, 30))
        self.btn_ver_clientes_juridicos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_ver_clientes_juridicos.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"../../../../.designer/backup/imagens/74472.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_ver_clientes_juridicos.setIcon(icon8)
        self.btn_ver_clientes_juridicos.setIconSize(QSize(21, 25))

        self.verticalLayout_20.addWidget(self.btn_ver_clientes_juridicos)

        self.btn_ver_item = QPushButton(self.frame_confirmar_ver_produto)
        self.btn_ver_item.setObjectName(u"btn_ver_item")
        sizePolicy.setHeightForWidth(self.btn_ver_item.sizePolicy().hasHeightForWidth())
        self.btn_ver_item.setSizePolicy(sizePolicy)
        self.btn_ver_item.setMinimumSize(QSize(0, 0))
        self.btn_ver_item.setMaximumSize(QSize(177, 30))
        self.btn_ver_item.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_ver_item.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u"../../../../.designer/backup/imagens/pasta.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_ver_item.setIcon(icon9)

        self.verticalLayout_20.addWidget(self.btn_ver_item)


        self.gridLayout_11.addWidget(self.frame_confirmar_ver_produto, 4, 1, 1, 1)


        self.gridLayout_10.addWidget(self.frame_cadastrar_produto, 0, 0, 1, 1)

        self.paginas_sistemas.addWidget(self.pg_cadastrar_produto)
        self.pg_cadastrar_usuario = QWidget()
        self.pg_cadastrar_usuario.setObjectName(u"pg_cadastrar_usuario")
        sizePolicy.setHeightForWidth(self.pg_cadastrar_usuario.sizePolicy().hasHeightForWidth())
        self.pg_cadastrar_usuario.setSizePolicy(sizePolicy)
        self.gridLayout_13 = QGridLayout(self.pg_cadastrar_usuario)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.frame_pag_cadastrar_usuario = QFrame(self.pg_cadastrar_usuario)
        self.frame_pag_cadastrar_usuario.setObjectName(u"frame_pag_cadastrar_usuario")
        sizePolicy.setHeightForWidth(self.frame_pag_cadastrar_usuario.sizePolicy().hasHeightForWidth())
        self.frame_pag_cadastrar_usuario.setSizePolicy(sizePolicy)
        self.frame_pag_cadastrar_usuario.setFrameShape(QFrame.NoFrame)
        self.frame_pag_cadastrar_usuario.setFrameShadow(QFrame.Raised)
        self.gridLayout_27 = QGridLayout(self.frame_pag_cadastrar_usuario)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.label_cadastramento = QLabel(self.frame_pag_cadastrar_usuario)
        self.label_cadastramento.setObjectName(u"label_cadastramento")
        sizePolicy.setHeightForWidth(self.label_cadastramento.sizePolicy().hasHeightForWidth())
        self.label_cadastramento.setSizePolicy(sizePolicy)
        self.label_cadastramento.setMaximumSize(QSize(338, 60))
        self.label_cadastramento.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"	border: 3px solid white;\n"
"}\n"
"")

        self.gridLayout_27.addWidget(self.label_cadastramento, 0, 1, 1, 1)

        self.frame_3 = QFrame(self.frame_pag_cadastrar_usuario)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMaximumSize(QSize(400, 16777215))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_3)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_confirmar_senha_3 = QLabel(self.frame_3)
        self.label_confirmar_senha_3.setObjectName(u"label_confirmar_senha_3")
        self.label_confirmar_senha_3.setStyleSheet(u"QLabel {\n"
"    color: black;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.horizontalLayout_27.addWidget(self.label_confirmar_senha_3)

        self.txt_bairro = QLineEdit(self.frame_3)
        self.txt_bairro.setObjectName(u"txt_bairro")
        sizePolicy.setHeightForWidth(self.txt_bairro.sizePolicy().hasHeightForWidth())
        self.txt_bairro.setSizePolicy(sizePolicy)
        self.txt_bairro.setMaximumSize(QSize(181, 30))
        self.txt_bairro.setStyleSheet(u"QLineEdit {\n"
"	color: black;\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150,250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QLineEdit::placeholderText {\n"
"    color: black; /* Cor do texto do placeholder */\n"
"}\n"
"")

        self.horizontalLayout_27.addWidget(self.txt_bairro)

        self.frame_erro_bairro = QFrame(self.frame_3)
        self.frame_erro_bairro.setObjectName(u"frame_erro_bairro")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_erro_bairro.sizePolicy().hasHeightForWidth())
        self.frame_erro_bairro.setSizePolicy(sizePolicy2)
        self.frame_erro_bairro.setMaximumSize(QSize(21, 21))
        self.frame_erro_bairro.setFrameShape(QFrame.StyledPanel)
        self.frame_erro_bairro.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_27.addWidget(self.frame_erro_bairro)


        self.gridLayout_14.addLayout(self.horizontalLayout_27, 8, 0, 1, 1)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_confirmar_senha_4 = QLabel(self.frame_3)
        self.label_confirmar_senha_4.setObjectName(u"label_confirmar_senha_4")
        self.label_confirmar_senha_4.setMaximumSize(QSize(16777215, 20))
        self.label_confirmar_senha_4.setStyleSheet(u"QLabel {\n"
"    color: black;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.horizontalLayout_28.addWidget(self.label_confirmar_senha_4)

        self.txt_cnpj = QLineEdit(self.frame_3)
        self.txt_cnpj.setObjectName(u"txt_cnpj")
        sizePolicy.setHeightForWidth(self.txt_cnpj.sizePolicy().hasHeightForWidth())
        self.txt_cnpj.setSizePolicy(sizePolicy)
        self.txt_cnpj.setMaximumSize(QSize(181, 30))
        self.txt_cnpj.setStyleSheet(u"QLineEdit {\n"
"	color: black;\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150,250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QLineEdit::placeholderText {\n"
"    color: black; /* Cor do texto do placeholder */\n"
"}\n"
"")

        self.horizontalLayout_28.addWidget(self.txt_cnpj)

        self.frame_erro_cnpj = QFrame(self.frame_3)
        self.frame_erro_cnpj.setObjectName(u"frame_erro_cnpj")
        sizePolicy.setHeightForWidth(self.frame_erro_cnpj.sizePolicy().hasHeightForWidth())
        self.frame_erro_cnpj.setSizePolicy(sizePolicy)
        self.frame_erro_cnpj.setMaximumSize(QSize(21, 21))
        self.frame_erro_cnpj.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_28.addWidget(self.frame_erro_cnpj)


        self.gridLayout_14.addLayout(self.horizontalLayout_28, 16, 0, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_complemento = QLabel(self.frame_3)
        self.label_complemento.setObjectName(u"label_complemento")
        self.label_complemento.setStyleSheet(u"QLabel {\n"
"    color: black;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.horizontalLayout_15.addWidget(self.label_complemento)

        self.txt_complemento = QLineEdit(self.frame_3)
        self.txt_complemento.setObjectName(u"txt_complemento")
        sizePolicy.setHeightForWidth(self.txt_complemento.sizePolicy().hasHeightForWidth())
        self.txt_complemento.setSizePolicy(sizePolicy)
        self.txt_complemento.setMaximumSize(QSize(181, 30))
        self.txt_complemento.setStyleSheet(u"QLineEdit {\n"
"	color: black;\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150,250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QLineEdit::placeholderText {\n"
"    color: black; /* Cor do texto do placeholder */\n"
"}\n"
"")

        self.horizontalLayout_15.addWidget(self.txt_complemento)

        self.frame_erro_complemento = QFrame(self.frame_3)
        self.frame_erro_complemento.setObjectName(u"frame_erro_complemento")
        sizePolicy2.setHeightForWidth(self.frame_erro_complemento.sizePolicy().hasHeightForWidth())
        self.frame_erro_complemento.setSizePolicy(sizePolicy2)
        self.frame_erro_complemento.setMaximumSize(QSize(21, 21))
        self.frame_erro_complemento.setFrameShape(QFrame.StyledPanel)
        self.frame_erro_complemento.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_15.addWidget(self.frame_erro_complemento)


        self.gridLayout_14.addLayout(self.horizontalLayout_15, 10, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_usuario = QLabel(self.frame_3)
        self.label_usuario.setObjectName(u"label_usuario")
        self.label_usuario.setStyleSheet(u"QLabel {\n"
"    color: black;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.horizontalLayout_10.addWidget(self.label_usuario)

        self.txt_usuario = QLineEdit(self.frame_3)
        self.txt_usuario.setObjectName(u"txt_usuario")
        sizePolicy.setHeightForWidth(self.txt_usuario.sizePolicy().hasHeightForWidth())
        self.txt_usuario.setSizePolicy(sizePolicy)
        self.txt_usuario.setMaximumSize(QSize(181, 30))
        self.txt_usuario.setStyleSheet(u"QLineEdit {\n"
"	color: black;\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150,250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QLineEdit::placeholderText {\n"
"    color: black; /* Cor do texto do placeholder */\n"
"}\n"
"")

        self.horizontalLayout_10.addWidget(self.txt_usuario)

        self.frame_erro_usuario = QFrame(self.frame_3)
        self.frame_erro_usuario.setObjectName(u"frame_erro_usuario")
        sizePolicy2.setHeightForWidth(self.frame_erro_usuario.sizePolicy().hasHeightForWidth())
        self.frame_erro_usuario.setSizePolicy(sizePolicy2)
        self.frame_erro_usuario.setMaximumSize(QSize(21, 21))
        self.frame_erro_usuario.setFrameShape(QFrame.StyledPanel)
        self.frame_erro_usuario.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_erro_usuario)


        self.gridLayout_14.addLayout(self.horizontalLayout_10, 1, 0, 1, 1)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, 0, -1, -1)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_20.addWidget(self.label_2)

        self.txt_rg = QLineEdit(self.frame_3)
        self.txt_rg.setObjectName(u"txt_rg")
        sizePolicy.setHeightForWidth(self.txt_rg.sizePolicy().hasHeightForWidth())
        self.txt_rg.setSizePolicy(sizePolicy)
        self.txt_rg.setMaximumSize(QSize(180, 30))
        self.txt_rg.setStyleSheet(u"QLineEdit {\n"
"	color: black;\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150,250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QLineEdit::placeholderText {\n"
"    color: black; /* Cor do texto do placeholder */\n"
"}\n"
"")

        self.horizontalLayout_20.addWidget(self.txt_rg)

        self.frame_erro_rg = QFrame(self.frame_3)
        self.frame_erro_rg.setObjectName(u"frame_erro_rg")
        sizePolicy2.setHeightForWidth(self.frame_erro_rg.sizePolicy().hasHeightForWidth())
        self.frame_erro_rg.setSizePolicy(sizePolicy2)
        self.frame_erro_rg.setMaximumSize(QSize(21, 21))
        self.frame_erro_rg.setFrameShape(QFrame.StyledPanel)
        self.frame_erro_rg.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_20.addWidget(self.frame_erro_rg)


        self.gridLayout_14.addLayout(self.horizontalLayout_20, 14, 0, 1, 1)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_cpf = QLabel(self.frame_3)
        self.label_cpf.setObjectName(u"label_cpf")
        self.label_cpf.setStyleSheet(u"QLabel {\n"
"    color: black;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.horizontalLayout_17.addWidget(self.label_cpf)

        self.txt_cpf = QLineEdit(self.frame_3)
        self.txt_cpf.setObjectName(u"txt_cpf")
        sizePolicy.setHeightForWidth(self.txt_cpf.sizePolicy().hasHeightForWidth())
        self.txt_cpf.setSizePolicy(sizePolicy)
        self.txt_cpf.setMaximumSize(QSize(181, 30))
        self.txt_cpf.setStyleSheet(u"QLineEdit {\n"
"	color: black;\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150,250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QLineEdit::placeholderText {\n"
"    color: black; /* Cor do texto do placeholder */\n"
"}\n"
"")

        self.horizontalLayout_17.addWidget(self.txt_cpf)

        self.frame_erro_cpf = QFrame(self.frame_3)
        self.frame_erro_cpf.setObjectName(u"frame_erro_cpf")
        sizePolicy2.setHeightForWidth(self.frame_erro_cpf.sizePolicy().hasHeightForWidth())
        self.frame_erro_cpf.setSizePolicy(sizePolicy2)
        self.frame_erro_cpf.setMaximumSize(QSize(21, 21))
        self.frame_erro_cpf.setFrameShape(QFrame.StyledPanel)
        self.frame_erro_cpf.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_17.addWidget(self.frame_erro_cpf)


        self.gridLayout_14.addLayout(self.horizontalLayout_17, 15, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_nome = QLabel(self.frame_3)
        self.label_nome.setObjectName(u"label_nome")
        self.label_nome.setStyleSheet(u"QLabel {\n"
"    color: black;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.horizontalLayout_9.addWidget(self.label_nome)

        self.txt_nome = QLineEdit(self.frame_3)
        self.txt_nome.setObjectName(u"txt_nome")
        sizePolicy.setHeightForWidth(self.txt_nome.sizePolicy().hasHeightForWidth())
        self.txt_nome.setSizePolicy(sizePolicy)
        self.txt_nome.setMaximumSize(QSize(181, 30))
        self.txt_nome.setStyleSheet(u"QLineEdit {\n"
"	color: black;\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150,250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QLineEdit::placeholderText {\n"
"    color: black; /* Cor do texto do placeholder */\n"
"}\n"
"")

        self.horizontalLayout_9.addWidget(self.txt_nome)

        self.frame_erro_nome = QFrame(self.frame_3)
        self.frame_erro_nome.setObjectName(u"frame_erro_nome")
        sizePolicy2.setHeightForWidth(self.frame_erro_nome.sizePolicy().hasHeightForWidth())
        self.frame_erro_nome.setSizePolicy(sizePolicy2)
        self.frame_erro_nome.setMaximumSize(QSize(21, 21))
        self.frame_erro_nome.setFrameShape(QFrame.StyledPanel)
        self.frame_erro_nome.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_9.addWidget(self.frame_erro_nome)


        self.gridLayout_14.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_data_nascimento = QLabel(self.frame_3)
        self.label_data_nascimento.setObjectName(u"label_data_nascimento")
        self.label_data_nascimento.setStyleSheet(u"QLabel {\n"
"    color: black;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.horizontalLayout_14.addWidget(self.label_data_nascimento)

        self.txt_data_nascimento = QLineEdit(self.frame_3)
        self.txt_data_nascimento.setObjectName(u"txt_data_nascimento")
        sizePolicy.setHeightForWidth(self.txt_data_nascimento.sizePolicy().hasHeightForWidth())
        self.txt_data_nascimento.setSizePolicy(sizePolicy)
        self.txt_data_nascimento.setMaximumSize(QSize(181, 30))
        self.txt_data_nascimento.setStyleSheet(u"QLineEdit {\n"
"	color: black;\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150,250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QLineEdit::placeholderText {\n"
"    color: black; /* Cor do texto do placeholder */\n"
"}\n"
"")

        self.horizontalLayout_14.addWidget(self.txt_data_nascimento)

        self.frame_data_nascimento = QFrame(self.frame_3)
        self.frame_data_nascimento.setObjectName(u"frame_data_nascimento")
        sizePolicy2.setHeightForWidth(self.frame_data_nascimento.sizePolicy().hasHeightForWidth())
        self.frame_data_nascimento.setSizePolicy(sizePolicy2)
        self.frame_data_nascimento.setMaximumSize(QSize(21, 21))
        self.frame_data_nascimento.setFrameShape(QFrame.StyledPanel)
        self.frame_data_nascimento.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_14.addWidget(self.frame_data_nascimento)


        self.gridLayout_14.addLayout(self.horizontalLayout_14, 13, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_perfil = QLabel(self.frame_3)
        self.label_perfil.setObjectName(u"label_perfil")
        self.label_perfil.setStyleSheet(u"QLabel {\n"
"    color: black;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.horizontalLayout_11.addWidget(self.label_perfil)

        self.perfil_usuarios = QComboBox(self.frame_3)
        self.perfil_usuarios.addItem("")
        self.perfil_usuarios.addItem("")
        self.perfil_usuarios.addItem("")
        self.perfil_usuarios.addItem("")
        self.perfil_usuarios.setObjectName(u"perfil_usuarios")
        sizePolicy.setHeightForWidth(self.perfil_usuarios.sizePolicy().hasHeightForWidth())
        self.perfil_usuarios.setSizePolicy(sizePolicy)
        self.perfil_usuarios.setMinimumSize(QSize(0, 0))
        self.perfil_usuarios.setMaximumSize(QSize(181, 30))
        self.perfil_usuarios.setStyleSheet(u"\n"
"    QComboBox { \n"
"        background-color: white; \n"
"        border: 3px solid rgb(50,150,250); \n"
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
" "
                        "   }\n"
"    QComboBox QAbstractItemView QScrollBar::add-page:vertical, \n"
"    QComboBox QAbstractItemView QScrollBar::sub-page:vertical {\n"
"        background: none;\n"
"    }\n"
"\n"
"")
        self.perfil_usuarios.setEditable(False)
        self.perfil_usuarios.setMaxCount(5)

        self.horizontalLayout_11.addWidget(self.perfil_usuarios)

        self.frame_erro_perfil = QFrame(self.frame_3)
        self.frame_erro_perfil.setObjectName(u"frame_erro_perfil")
        sizePolicy2.setHeightForWidth(self.frame_erro_perfil.sizePolicy().hasHeightForWidth())
        self.frame_erro_perfil.setSizePolicy(sizePolicy2)
        self.frame_erro_perfil.setMaximumSize(QSize(21, 21))
        self.frame_erro_perfil.setFrameShape(QFrame.StyledPanel)
        self.frame_erro_perfil.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_11.addWidget(self.frame_erro_perfil)


        self.gridLayout_14.addLayout(self.horizontalLayout_11, 21, 0, 1, 1)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_email = QLabel(self.frame_3)
        self.label_email.setObjectName(u"label_email")
        self.label_email.setStyleSheet(u"QLabel {\n"
"    color: black;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.horizontalLayout_16.addWidget(self.label_email)

        self.txt_email = QLineEdit(self.frame_3)
        self.txt_email.setObjectName(u"txt_email")
        sizePolicy.setHeightForWidth(self.txt_email.sizePolicy().hasHeightForWidth())
        self.txt_email.setSizePolicy(sizePolicy)
        self.txt_email.setMaximumSize(QSize(181, 30))
        self.txt_email.setStyleSheet(u"QLineEdit {\n"
"	color: black;\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150,250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QLineEdit::placeholderText {\n"
"    color: black; /* Cor do texto do placeholder */\n"
"}\n"
"")

        self.horizontalLayout_16.addWidget(self.txt_email)

        self.frame_erro_email = QFrame(self.frame_3)
        self.frame_erro_email.setObjectName(u"frame_erro_email")
        sizePolicy2.setHeightForWidth(self.frame_erro_email.sizePolicy().hasHeightForWidth())
        self.frame_erro_email.setSizePolicy(sizePolicy2)
        self.frame_erro_email.setMaximumSize(QSize(21, 21))
        self.frame_erro_email.setFrameShape(QFrame.StyledPanel)
        self.frame_erro_email.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_16.addWidget(self.frame_erro_email)


        self.gridLayout_14.addLayout(self.horizontalLayout_16, 12, 0, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_endereco = QLabel(self.frame_3)
        self.label_endereco.setObjectName(u"label_endereco")
        self.label_endereco.setStyleSheet(u"QLabel {\n"
"    color: black;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.horizontalLayout_13.addWidget(self.label_endereco)

        self.txt_endereco = QLineEdit(self.frame_3)
        self.txt_endereco.setObjectName(u"txt_endereco")
        sizePolicy.setHeightForWidth(self.txt_endereco.sizePolicy().hasHeightForWidth())
        self.txt_endereco.setSizePolicy(sizePolicy)
        self.txt_endereco.setMaximumSize(QSize(181, 30))
        self.txt_endereco.setStyleSheet(u"QLineEdit {\n"
"	color: black;\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150,250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QLineEdit::placeholderText {\n"
"    color: black; /* Cor do texto do placeholder */\n"
"}\n"
"")

        self.horizontalLayout_13.addWidget(self.txt_endereco)

        self.frame_erro_endereco = QFrame(self.frame_3)
        self.frame_erro_endereco.setObjectName(u"frame_erro_endereco")
        sizePolicy2.setHeightForWidth(self.frame_erro_endereco.sizePolicy().hasHeightForWidth())
        self.frame_erro_endereco.setSizePolicy(sizePolicy2)
        self.frame_erro_endereco.setMaximumSize(QSize(21, 21))
        self.frame_erro_endereco.setFrameShape(QFrame.StyledPanel)
        self.frame_erro_endereco.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_13.addWidget(self.frame_erro_endereco)


        self.gridLayout_14.addLayout(self.horizontalLayout_13, 5, 0, 1, 1)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_numero = QLabel(self.frame_3)
        self.label_numero.setObjectName(u"label_numero")
        self.label_numero.setStyleSheet(u"QLabel {\n"
"    color: black;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.horizontalLayout_19.addWidget(self.label_numero)

        self.txt_numero = QLineEdit(self.frame_3)
        self.txt_numero.setObjectName(u"txt_numero")
        sizePolicy.setHeightForWidth(self.txt_numero.sizePolicy().hasHeightForWidth())
        self.txt_numero.setSizePolicy(sizePolicy)
        self.txt_numero.setMaximumSize(QSize(181, 30))
        self.txt_numero.setStyleSheet(u"QLineEdit {\n"
"	color: black;\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150,250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QLineEdit::placeholderText {\n"
"    color: black; /* Cor do texto do placeholder */\n"
"}\n"
"")

        self.horizontalLayout_19.addWidget(self.txt_numero)

        self.frame_erro_numero = QFrame(self.frame_3)
        self.frame_erro_numero.setObjectName(u"frame_erro_numero")
        sizePolicy2.setHeightForWidth(self.frame_erro_numero.sizePolicy().hasHeightForWidth())
        self.frame_erro_numero.setSizePolicy(sizePolicy2)
        self.frame_erro_numero.setMaximumSize(QSize(21, 21))
        self.frame_erro_numero.setFrameShape(QFrame.StyledPanel)
        self.frame_erro_numero.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_19.addWidget(self.frame_erro_numero)


        self.gridLayout_14.addLayout(self.horizontalLayout_19, 6, 0, 1, 1)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_cep = QLabel(self.frame_3)
        self.label_cep.setObjectName(u"label_cep")
        self.label_cep.setStyleSheet(u"QLabel {\n"
"    color: black;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.horizontalLayout_22.addWidget(self.label_cep)

        self.txt_cep = QLineEdit(self.frame_3)
        self.txt_cep.setObjectName(u"txt_cep")
        sizePolicy.setHeightForWidth(self.txt_cep.sizePolicy().hasHeightForWidth())
        self.txt_cep.setSizePolicy(sizePolicy)
        self.txt_cep.setMaximumSize(QSize(181, 30))
        self.txt_cep.setStyleSheet(u"QLineEdit {\n"
"	color: black;\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150,250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QLineEdit::placeholderText {\n"
"    color: black; /* Cor do texto do placeholder */\n"
"}\n"
"")

        self.horizontalLayout_22.addWidget(self.txt_cep)

        self.frame_erro_cep = QFrame(self.frame_3)
        self.frame_erro_cep.setObjectName(u"frame_erro_cep")
        sizePolicy2.setHeightForWidth(self.frame_erro_cep.sizePolicy().hasHeightForWidth())
        self.frame_erro_cep.setSizePolicy(sizePolicy2)
        self.frame_erro_cep.setMaximumSize(QSize(21, 21))
        self.frame_erro_cep.setFrameShape(QFrame.StyledPanel)
        self.frame_erro_cep.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_22.addWidget(self.frame_erro_cep)


        self.gridLayout_14.addLayout(self.horizontalLayout_22, 4, 0, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_telefone = QLabel(self.frame_3)
        self.label_telefone.setObjectName(u"label_telefone")
        self.label_telefone.setStyleSheet(u"QLabel {\n"
"    color: black;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.horizontalLayout_12.addWidget(self.label_telefone)

        self.txt_telefone = QLineEdit(self.frame_3)
        self.txt_telefone.setObjectName(u"txt_telefone")
        sizePolicy.setHeightForWidth(self.txt_telefone.sizePolicy().hasHeightForWidth())
        self.txt_telefone.setSizePolicy(sizePolicy)
        self.txt_telefone.setMaximumSize(QSize(181, 30))
        self.txt_telefone.setStyleSheet(u"QLineEdit {\n"
"	color: black;\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150,250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QLineEdit::placeholderText {\n"
"    color: black; /* Cor do texto do placeholder */\n"
"}\n"
"")

        self.horizontalLayout_12.addWidget(self.txt_telefone)

        self.frame_erro_telefone = QFrame(self.frame_3)
        self.frame_erro_telefone.setObjectName(u"frame_erro_telefone")
        sizePolicy2.setHeightForWidth(self.frame_erro_telefone.sizePolicy().hasHeightForWidth())
        self.frame_erro_telefone.setSizePolicy(sizePolicy2)
        self.frame_erro_telefone.setMaximumSize(QSize(21, 21))
        self.frame_erro_telefone.setFrameShape(QFrame.StyledPanel)
        self.frame_erro_telefone.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_12.addWidget(self.frame_erro_telefone)


        self.gridLayout_14.addLayout(self.horizontalLayout_12, 11, 0, 1, 1)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_confirmar_senha_2 = QLabel(self.frame_3)
        self.label_confirmar_senha_2.setObjectName(u"label_confirmar_senha_2")
        self.label_confirmar_senha_2.setStyleSheet(u"QLabel {\n"
"    color: black;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.horizontalLayout_26.addWidget(self.label_confirmar_senha_2)

        self.txt_cidade = QLineEdit(self.frame_3)
        self.txt_cidade.setObjectName(u"txt_cidade")
        sizePolicy.setHeightForWidth(self.txt_cidade.sizePolicy().hasHeightForWidth())
        self.txt_cidade.setSizePolicy(sizePolicy)
        self.txt_cidade.setMaximumSize(QSize(181, 30))
        self.txt_cidade.setStyleSheet(u"QLineEdit {\n"
"	color: black;\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150,250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QLineEdit::placeholderText {\n"
"    color: black; /* Cor do texto do placeholder */\n"
"}\n"
"")

        self.horizontalLayout_26.addWidget(self.txt_cidade)

        self.frame_erro_cidade = QFrame(self.frame_3)
        self.frame_erro_cidade.setObjectName(u"frame_erro_cidade")
        sizePolicy2.setHeightForWidth(self.frame_erro_cidade.sizePolicy().hasHeightForWidth())
        self.frame_erro_cidade.setSizePolicy(sizePolicy2)
        self.frame_erro_cidade.setMaximumSize(QSize(21, 21))
        self.frame_erro_cidade.setFrameShape(QFrame.StyledPanel)
        self.frame_erro_cidade.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_26.addWidget(self.frame_erro_cidade)


        self.gridLayout_14.addLayout(self.horizontalLayout_26, 7, 0, 1, 1)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_senha = QLabel(self.frame_3)
        self.label_senha.setObjectName(u"label_senha")
        self.label_senha.setStyleSheet(u"QLabel {\n"
"    color: black;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.horizontalLayout_21.addWidget(self.label_senha)

        self.txt_senha = QLineEdit(self.frame_3)
        self.txt_senha.setObjectName(u"txt_senha")
        sizePolicy.setHeightForWidth(self.txt_senha.sizePolicy().hasHeightForWidth())
        self.txt_senha.setSizePolicy(sizePolicy)
        self.txt_senha.setMaximumSize(QSize(181, 30))
        self.txt_senha.setStyleSheet(u"QLineEdit {\n"
"	color: black;\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150,250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QLineEdit::placeholderText {\n"
"    color: black; /* Cor do texto do placeholder */\n"
"}\n"
"")
        self.txt_senha.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_21.addWidget(self.txt_senha)

        self.frame_senha = QFrame(self.frame_3)
        self.frame_senha.setObjectName(u"frame_senha")
        sizePolicy2.setHeightForWidth(self.frame_senha.sizePolicy().hasHeightForWidth())
        self.frame_senha.setSizePolicy(sizePolicy2)
        self.frame_senha.setMaximumSize(QSize(21, 21))
        self.frame_senha.setFrameShape(QFrame.StyledPanel)
        self.frame_senha.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_21.addWidget(self.frame_senha)


        self.gridLayout_14.addLayout(self.horizontalLayout_21, 2, 0, 1, 1)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_estado = QLabel(self.frame_3)
        self.label_estado.setObjectName(u"label_estado")
        self.label_estado.setStyleSheet(u"QLabel {\n"
"    color: black;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.horizontalLayout_23.addWidget(self.label_estado)

        self.perfil_estado = QComboBox(self.frame_3)
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
        self.perfil_estado.addItem("")
        self.perfil_estado.setObjectName(u"perfil_estado")
        sizePolicy.setHeightForWidth(self.perfil_estado.sizePolicy().hasHeightForWidth())
        self.perfil_estado.setSizePolicy(sizePolicy)
        self.perfil_estado.setMaximumSize(QSize(181, 30))
        self.perfil_estado.setStyleSheet(u"\n"
"    QComboBox { \n"
"        background-color: white; \n"
"        border:  2px solid rgb(50,150,250); \n"
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
""
                        "    }\n"
"    QComboBox QAbstractItemView QScrollBar::add-page:vertical, \n"
"    QComboBox QAbstractItemView QScrollBar::sub-page:vertical {\n"
"        background: none;\n"
"    }\n"
"\n"
"")
        self.perfil_estado.setEditable(False)
        self.perfil_estado.setMaxVisibleItems(27)

        self.horizontalLayout_23.addWidget(self.perfil_estado)

        self.frame_erro_estado = QFrame(self.frame_3)
        self.frame_erro_estado.setObjectName(u"frame_erro_estado")
        sizePolicy2.setHeightForWidth(self.frame_erro_estado.sizePolicy().hasHeightForWidth())
        self.frame_erro_estado.setSizePolicy(sizePolicy2)
        self.frame_erro_estado.setMaximumSize(QSize(21, 21))
        self.frame_erro_estado.setFrameShape(QFrame.StyledPanel)
        self.frame_erro_estado.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_23.addWidget(self.frame_erro_estado)


        self.gridLayout_14.addLayout(self.horizontalLayout_23, 9, 0, 1, 1)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_confirmar_senha = QLabel(self.frame_3)
        self.label_confirmar_senha.setObjectName(u"label_confirmar_senha")
        self.label_confirmar_senha.setStyleSheet(u"QLabel {\n"
"    color: black;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.horizontalLayout_18.addWidget(self.label_confirmar_senha)

        self.txt_confirmar_senha = QLineEdit(self.frame_3)
        self.txt_confirmar_senha.setObjectName(u"txt_confirmar_senha")
        sizePolicy.setHeightForWidth(self.txt_confirmar_senha.sizePolicy().hasHeightForWidth())
        self.txt_confirmar_senha.setSizePolicy(sizePolicy)
        self.txt_confirmar_senha.setMaximumSize(QSize(181, 30))
        self.txt_confirmar_senha.setStyleSheet(u"QLineEdit {\n"
"	color: black;\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150,250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QLineEdit::placeholderText {\n"
"    color: black; /* Cor do texto do placeholder */\n"
"}\n"
"")
        self.txt_confirmar_senha.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_18.addWidget(self.txt_confirmar_senha)

        self.frame_confirmar_senha = QFrame(self.frame_3)
        self.frame_confirmar_senha.setObjectName(u"frame_confirmar_senha")
        sizePolicy2.setHeightForWidth(self.frame_confirmar_senha.sizePolicy().hasHeightForWidth())
        self.frame_confirmar_senha.setSizePolicy(sizePolicy2)
        self.frame_confirmar_senha.setMaximumSize(QSize(21, 21))
        self.frame_confirmar_senha.setFrameShape(QFrame.StyledPanel)
        self.frame_confirmar_senha.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_18.addWidget(self.frame_confirmar_senha)


        self.gridLayout_14.addLayout(self.horizontalLayout_18, 3, 0, 1, 1)


        self.gridLayout_27.addWidget(self.frame_3, 1, 0, 1, 1)

        self.frame_20 = QFrame(self.frame_pag_cadastrar_usuario)
        self.frame_20.setObjectName(u"frame_20")
        sizePolicy.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy)
        self.frame_20.setMaximumSize(QSize(230, 320))
        self.frame_20.setFrameShape(QFrame.NoFrame)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_20)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.btn_editar_cadastro = QPushButton(self.frame_20)
        self.btn_editar_cadastro.setObjectName(u"btn_editar_cadastro")
        sizePolicy.setHeightForWidth(self.btn_editar_cadastro.sizePolicy().hasHeightForWidth())
        self.btn_editar_cadastro.setSizePolicy(sizePolicy)
        self.btn_editar_cadastro.setMinimumSize(QSize(0, 39))
        self.btn_editar_cadastro.setMaximumSize(QSize(16777215, 39))
        self.btn_editar_cadastro.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_editar_cadastro.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")
        self.btn_editar_cadastro.setIcon(icon1)
        self.btn_editar_cadastro.setIconSize(QSize(20, 20))

        self.verticalLayout_16.addWidget(self.btn_editar_cadastro)

        self.btn_sair_modo_edicao = QPushButton(self.frame_20)
        self.btn_sair_modo_edicao.setObjectName(u"btn_sair_modo_edicao")
        sizePolicy.setHeightForWidth(self.btn_sair_modo_edicao.sizePolicy().hasHeightForWidth())
        self.btn_sair_modo_edicao.setSizePolicy(sizePolicy)
        self.btn_sair_modo_edicao.setMinimumSize(QSize(0, 39))
        self.btn_sair_modo_edicao.setMaximumSize(QSize(16777215, 39))
        self.btn_sair_modo_edicao.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_sair_modo_edicao.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")
        self.btn_sair_modo_edicao.setIcon(icon2)
        self.btn_sair_modo_edicao.setIconSize(QSize(20, 20))

        self.verticalLayout_16.addWidget(self.btn_sair_modo_edicao)

        self.btn_atualizar_cadastro = QPushButton(self.frame_20)
        self.btn_atualizar_cadastro.setObjectName(u"btn_atualizar_cadastro")
        sizePolicy.setHeightForWidth(self.btn_atualizar_cadastro.sizePolicy().hasHeightForWidth())
        self.btn_atualizar_cadastro.setSizePolicy(sizePolicy)
        self.btn_atualizar_cadastro.setMinimumSize(QSize(0, 39))
        self.btn_atualizar_cadastro.setMaximumSize(QSize(16777215, 39))
        self.btn_atualizar_cadastro.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_atualizar_cadastro.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")
        self.btn_atualizar_cadastro.setIcon(icon3)
        self.btn_atualizar_cadastro.setIconSize(QSize(20, 20))

        self.verticalLayout_16.addWidget(self.btn_atualizar_cadastro)

        self.btn_apagar_cadastro = QPushButton(self.frame_20)
        self.btn_apagar_cadastro.setObjectName(u"btn_apagar_cadastro")
        sizePolicy.setHeightForWidth(self.btn_apagar_cadastro.sizePolicy().hasHeightForWidth())
        self.btn_apagar_cadastro.setSizePolicy(sizePolicy)
        self.btn_apagar_cadastro.setMinimumSize(QSize(0, 39))
        self.btn_apagar_cadastro.setMaximumSize(QSize(16777215, 39))
        self.btn_apagar_cadastro.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_apagar_cadastro.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")
        self.btn_apagar_cadastro.setIcon(icon4)
        self.btn_apagar_cadastro.setIconSize(QSize(20, 31))

        self.verticalLayout_16.addWidget(self.btn_apagar_cadastro)

        self.btn_carregar_imagem_4 = QPushButton(self.frame_20)
        self.btn_carregar_imagem_4.setObjectName(u"btn_carregar_imagem_4")
        sizePolicy.setHeightForWidth(self.btn_carregar_imagem_4.sizePolicy().hasHeightForWidth())
        self.btn_carregar_imagem_4.setSizePolicy(sizePolicy)
        self.btn_carregar_imagem_4.setMinimumSize(QSize(0, 39))
        self.btn_carregar_imagem_4.setMaximumSize(QSize(16777215, 39))
        self.btn_carregar_imagem_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_carregar_imagem_4.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")
        self.btn_carregar_imagem_4.setIcon(icon6)
        self.btn_carregar_imagem_4.setIconSize(QSize(20, 20))

        self.verticalLayout_16.addWidget(self.btn_carregar_imagem_4)

        self.btn_remover_imagem_usuario = QPushButton(self.frame_20)
        self.btn_remover_imagem_usuario.setObjectName(u"btn_remover_imagem_usuario")
        sizePolicy.setHeightForWidth(self.btn_remover_imagem_usuario.sizePolicy().hasHeightForWidth())
        self.btn_remover_imagem_usuario.setSizePolicy(sizePolicy)
        self.btn_remover_imagem_usuario.setMinimumSize(QSize(0, 39))
        self.btn_remover_imagem_usuario.setMaximumSize(QSize(16777215, 39))
        self.btn_remover_imagem_usuario.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_remover_imagem_usuario.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")
        self.btn_remover_imagem_usuario.setIcon(icon5)
        self.btn_remover_imagem_usuario.setIconSize(QSize(24, 31))

        self.verticalLayout_16.addWidget(self.btn_remover_imagem_usuario)

        self.btn_fazer_cadastro = QPushButton(self.frame_20)
        self.btn_fazer_cadastro.setObjectName(u"btn_fazer_cadastro")
        sizePolicy.setHeightForWidth(self.btn_fazer_cadastro.sizePolicy().hasHeightForWidth())
        self.btn_fazer_cadastro.setSizePolicy(sizePolicy)
        self.btn_fazer_cadastro.setMinimumSize(QSize(0, 39))
        self.btn_fazer_cadastro.setMaximumSize(QSize(16777215, 39))
        self.btn_fazer_cadastro.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_fazer_cadastro.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")
        self.btn_fazer_cadastro.setIcon(icon7)
        self.btn_fazer_cadastro.setIconSize(QSize(20, 20))

        self.verticalLayout_16.addWidget(self.btn_fazer_cadastro)

        self.btn_ver_usuario = QPushButton(self.frame_20)
        self.btn_ver_usuario.setObjectName(u"btn_ver_usuario")
        sizePolicy.setHeightForWidth(self.btn_ver_usuario.sizePolicy().hasHeightForWidth())
        self.btn_ver_usuario.setSizePolicy(sizePolicy)
        self.btn_ver_usuario.setMinimumSize(QSize(0, 39))
        self.btn_ver_usuario.setMaximumSize(QSize(16777215, 39))
        self.btn_ver_usuario.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_ver_usuario.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")
        self.btn_ver_usuario.setIcon(icon8)
        self.btn_ver_usuario.setIconSize(QSize(20, 28))

        self.verticalLayout_16.addWidget(self.btn_ver_usuario)


        self.gridLayout_27.addWidget(self.frame_20, 1, 1, 1, 1)

        self.frame_imagem_cadastro = QFrame(self.frame_pag_cadastrar_usuario)
        self.frame_imagem_cadastro.setObjectName(u"frame_imagem_cadastro")
        sizePolicy.setHeightForWidth(self.frame_imagem_cadastro.sizePolicy().hasHeightForWidth())
        self.frame_imagem_cadastro.setSizePolicy(sizePolicy)
        self.frame_imagem_cadastro.setMaximumSize(QSize(300, 300))
        self.frame_imagem_cadastro.setFrameShape(QFrame.NoFrame)
        self.frame_imagem_cadastro.setFrameShadow(QFrame.Raised)

        self.gridLayout_27.addWidget(self.frame_imagem_cadastro, 1, 2, 1, 1)


        self.gridLayout_13.addWidget(self.frame_pag_cadastrar_usuario, 0, 0, 1, 1)

        self.paginas_sistemas.addWidget(self.pg_cadastrar_usuario)
        self.pg_clientes = QWidget()
        self.pg_clientes.setObjectName(u"pg_clientes")
        sizePolicy.setHeightForWidth(self.pg_clientes.sizePolicy().hasHeightForWidth())
        self.pg_clientes.setSizePolicy(sizePolicy)
        self.gridLayout_15 = QGridLayout(self.pg_clientes)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.frame_pg_clientes = QFrame(self.pg_clientes)
        self.frame_pg_clientes.setObjectName(u"frame_pg_clientes")
        self.frame_pg_clientes.setFrameShape(QFrame.NoFrame)
        self.frame_pg_clientes.setFrameShadow(QFrame.Raised)
        self.gridLayout_18 = QGridLayout(self.frame_pg_clientes)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.tab_clientes_todos = QTabWidget(self.frame_pg_clientes)
        self.tab_clientes_todos.setObjectName(u"tab_clientes_todos")
        self.tab_clientes_todos.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.tab_clientes_todos.setStyleSheet(u"QTabBar::tab:selected {\n"
"    background-color: white;\n"
"    color: black;\n"
"}\n"
"")
        self.tab_clientes = QWidget()
        self.tab_clientes.setObjectName(u"tab_clientes")
        self.gridLayout_22 = QGridLayout(self.tab_clientes)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.frame_7 = QFrame(self.tab_clientes)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setMaximumSize(QSize(16777215, 50))
        self.frame_7.setFrameShape(QFrame.Box)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_7)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.btn_adicionar_cliente_juridico = QPushButton(self.frame_7)
        self.btn_adicionar_cliente_juridico.setObjectName(u"btn_adicionar_cliente_juridico")
        sizePolicy.setHeightForWidth(self.btn_adicionar_cliente_juridico.sizePolicy().hasHeightForWidth())
        self.btn_adicionar_cliente_juridico.setSizePolicy(sizePolicy)
        self.btn_adicionar_cliente_juridico.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_adicionar_cliente_juridico.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")

        self.horizontalLayout_25.addWidget(self.btn_adicionar_cliente_juridico)

        self.btn_editar_clientes = QPushButton(self.frame_7)
        self.btn_editar_clientes.setObjectName(u"btn_editar_clientes")
        sizePolicy.setHeightForWidth(self.btn_editar_clientes.sizePolicy().hasHeightForWidth())
        self.btn_editar_clientes.setSizePolicy(sizePolicy)
        self.btn_editar_clientes.setMaximumSize(QSize(145, 30))
        self.btn_editar_clientes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_editar_clientes.setAutoFillBackground(False)
        self.btn_editar_clientes.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")

        self.horizontalLayout_25.addWidget(self.btn_editar_clientes)

        self.btn_excluir_clientes = QPushButton(self.frame_7)
        self.btn_excluir_clientes.setObjectName(u"btn_excluir_clientes")
        sizePolicy.setHeightForWidth(self.btn_excluir_clientes.sizePolicy().hasHeightForWidth())
        self.btn_excluir_clientes.setSizePolicy(sizePolicy)
        self.btn_excluir_clientes.setMaximumSize(QSize(145, 30))
        self.btn_excluir_clientes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_excluir_clientes.setAutoFillBackground(False)
        self.btn_excluir_clientes.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")

        self.horizontalLayout_25.addWidget(self.btn_excluir_clientes)

        self.btn_gerar_relatorio_clientes = QPushButton(self.frame_7)
        self.btn_gerar_relatorio_clientes.setObjectName(u"btn_gerar_relatorio_clientes")
        sizePolicy.setHeightForWidth(self.btn_gerar_relatorio_clientes.sizePolicy().hasHeightForWidth())
        self.btn_gerar_relatorio_clientes.setSizePolicy(sizePolicy)
        self.btn_gerar_relatorio_clientes.setMaximumSize(QSize(145, 27))
        self.btn_gerar_relatorio_clientes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_gerar_relatorio_clientes.setAutoFillBackground(False)
        self.btn_gerar_relatorio_clientes.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")

        self.horizontalLayout_25.addWidget(self.btn_gerar_relatorio_clientes)

        self.btn_marcar_como_clientes = QPushButton(self.frame_7)
        self.btn_marcar_como_clientes.setObjectName(u"btn_marcar_como_clientes")
        sizePolicy.setHeightForWidth(self.btn_marcar_como_clientes.sizePolicy().hasHeightForWidth())
        self.btn_marcar_como_clientes.setSizePolicy(sizePolicy)
        self.btn_marcar_como_clientes.setMaximumSize(QSize(145, 27))
        self.btn_marcar_como_clientes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_marcar_como_clientes.setAutoFillBackground(False)
        self.btn_marcar_como_clientes.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")

        self.horizontalLayout_25.addWidget(self.btn_marcar_como_clientes)

        self.btn_historico_clientes = QPushButton(self.frame_7)
        self.btn_historico_clientes.setObjectName(u"btn_historico_clientes")
        sizePolicy.setHeightForWidth(self.btn_historico_clientes.sizePolicy().hasHeightForWidth())
        self.btn_historico_clientes.setSizePolicy(sizePolicy)
        self.btn_historico_clientes.setMaximumSize(QSize(145, 27))
        self.btn_historico_clientes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_historico_clientes.setAutoFillBackground(False)
        self.btn_historico_clientes.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")

        self.horizontalLayout_25.addWidget(self.btn_historico_clientes)


        self.verticalLayout_21.addLayout(self.horizontalLayout_25)


        self.gridLayout_22.addWidget(self.frame_7, 0, 1, 1, 1)

        self.line_clientes = QLineEdit(self.tab_clientes)
        self.line_clientes.setObjectName(u"line_clientes")
        sizePolicy.setHeightForWidth(self.line_clientes.sizePolicy().hasHeightForWidth())
        self.line_clientes.setSizePolicy(sizePolicy)
        self.line_clientes.setMaximumSize(QSize(260, 30))
        self.line_clientes.setStyleSheet(u"QLineEdit {\n"
"	color: black;\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150,250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QLineEdit::placeholderText {\n"
"    color: black; /* Cor do texto do placeholder */\n"
"}\n"
"")

        self.gridLayout_22.addWidget(self.line_clientes, 0, 0, 1, 1)

        self.table_clientes_juridicos = QTableWidget(self.tab_clientes)
        if (self.table_clientes_juridicos.columnCount() < 20):
            self.table_clientes_juridicos.setColumnCount(20)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.table_clientes_juridicos.setHorizontalHeaderItem(0, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.table_clientes_juridicos.setHorizontalHeaderItem(1, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.table_clientes_juridicos.setHorizontalHeaderItem(2, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.table_clientes_juridicos.setHorizontalHeaderItem(3, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.table_clientes_juridicos.setHorizontalHeaderItem(4, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.table_clientes_juridicos.setHorizontalHeaderItem(5, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.table_clientes_juridicos.setHorizontalHeaderItem(6, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.table_clientes_juridicos.setHorizontalHeaderItem(7, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.table_clientes_juridicos.setHorizontalHeaderItem(8, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.table_clientes_juridicos.setHorizontalHeaderItem(9, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.table_clientes_juridicos.setHorizontalHeaderItem(10, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.table_clientes_juridicos.setHorizontalHeaderItem(11, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.table_clientes_juridicos.setHorizontalHeaderItem(12, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.table_clientes_juridicos.setHorizontalHeaderItem(13, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.table_clientes_juridicos.setHorizontalHeaderItem(14, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        self.table_clientes_juridicos.setHorizontalHeaderItem(15, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.table_clientes_juridicos.setHorizontalHeaderItem(16, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.table_clientes_juridicos.setHorizontalHeaderItem(17, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        self.table_clientes_juridicos.setHorizontalHeaderItem(18, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        self.table_clientes_juridicos.setHorizontalHeaderItem(19, __qtablewidgetitem89)
        self.table_clientes_juridicos.setObjectName(u"table_clientes_juridicos")
        self.table_clientes_juridicos.setStyleSheet(u"/* Estiliza apenas o QTableView com objectName \"table_ativos\" */\n"
"QTableView {\n"
"    gridline-color: black;\n"
"    border: 2px solid white;\n"
"    color: black;\n"
"    selection-color: white;\n"
"}\n"
"\n"
"/* Estiliza a barra de rolagem horizontal */\n"
"QTableView QScrollBar:horizontal {\n"
"    border: none;\n"
"    background-color: rgb(255, 255, 255);\n"
"    height: 15px;\n"
"    margin: 0px 10px 0px 10px;\n"
"}\n"
"\n"
"/* Estiliza a barra de rolagem vertical */\n"
"QTableView QScrollBar:vertical {\n"
"    border: none;\n"
"    background-color: rgb(255, 255, 255); /* branco */\n"
"    width: 35px;\n"
"    margin: 0px 10px 0px 10px;\n"
"}\n"
"\n"
"/* Parte que voc\u00ea arrasta */\n"
"QTableView QScrollBar::handle:vertical {\n"
"    background-color: rgb(180, 180,150);  /* cinza */\n"
"    min-height: 30px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QTableView QScrollBar::handle:horizontal{\n"
"	background-color: rgb(180,180,150);\n"
"	min-height: 30px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"/* "
                        "Remove os bot\u00f5es */\n"
"QTableView QScrollBar::add-line:vertical,\n"
"QTableView QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"    width: 0px;\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"QTableView QScrollBar::groove:horizontal{\n"
"	background-color: rgb(100,240,240);\n"
"	border-radius: 2px;\n"
"	height: 15px;\n"
"	margin: 0px 10px 0px 10px;\n"
"}\n"
"\n"
"/* Estilo para item selecionado */\n"
"QTableWidget::item:selected {\n"
"    background-color: rgb(0, 120, 215);\n"
"    color: white;\n"
"}")
        self.table_clientes_juridicos.setFrameShape(QFrame.Box)
        self.table_clientes_juridicos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_clientes_juridicos.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_clientes_juridicos.setGridStyle(Qt.SolidLine)
        self.table_clientes_juridicos.setCornerButtonEnabled(False)
        self.table_clientes_juridicos.horizontalHeader().setDefaultSectionSize(118)
        self.table_clientes_juridicos.verticalHeader().setVisible(True)

        self.gridLayout_22.addWidget(self.table_clientes_juridicos, 1, 0, 1, 2)

        self.tab_clientes_todos.addTab(self.tab_clientes, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_28 = QGridLayout(self.tab_3)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.line_clientes_fisicos = QLineEdit(self.tab_3)
        self.line_clientes_fisicos.setObjectName(u"line_clientes_fisicos")
        sizePolicy.setHeightForWidth(self.line_clientes_fisicos.sizePolicy().hasHeightForWidth())
        self.line_clientes_fisicos.setSizePolicy(sizePolicy)
        self.line_clientes_fisicos.setMaximumSize(QSize(260, 30))
        self.line_clientes_fisicos.setStyleSheet(u"QLineEdit {\n"
"	color: black;\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150,250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QLineEdit::placeholderText {\n"
"    color: black; /* Cor do texto do placeholder */\n"
"}\n"
"")

        self.gridLayout_28.addWidget(self.line_clientes_fisicos, 0, 0, 1, 1)

        self.frame_12 = QFrame(self.tab_3)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setMaximumSize(QSize(16777215, 50))
        self.frame_12.setFrameShape(QFrame.Box)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_12)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.btn_adicionar_cliente_fisico = QPushButton(self.frame_12)
        self.btn_adicionar_cliente_fisico.setObjectName(u"btn_adicionar_cliente_fisico")
        sizePolicy.setHeightForWidth(self.btn_adicionar_cliente_fisico.sizePolicy().hasHeightForWidth())
        self.btn_adicionar_cliente_fisico.setSizePolicy(sizePolicy)
        self.btn_adicionar_cliente_fisico.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_adicionar_cliente_fisico.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")

        self.horizontalLayout_29.addWidget(self.btn_adicionar_cliente_fisico)

        self.btn_editar_clientes_fisicos = QPushButton(self.frame_12)
        self.btn_editar_clientes_fisicos.setObjectName(u"btn_editar_clientes_fisicos")
        sizePolicy.setHeightForWidth(self.btn_editar_clientes_fisicos.sizePolicy().hasHeightForWidth())
        self.btn_editar_clientes_fisicos.setSizePolicy(sizePolicy)
        self.btn_editar_clientes_fisicos.setMaximumSize(QSize(145, 30))
        self.btn_editar_clientes_fisicos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_editar_clientes_fisicos.setAutoFillBackground(False)
        self.btn_editar_clientes_fisicos.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")

        self.horizontalLayout_29.addWidget(self.btn_editar_clientes_fisicos)

        self.btn_excluir_clientes_fisicos = QPushButton(self.frame_12)
        self.btn_excluir_clientes_fisicos.setObjectName(u"btn_excluir_clientes_fisicos")
        sizePolicy.setHeightForWidth(self.btn_excluir_clientes_fisicos.sizePolicy().hasHeightForWidth())
        self.btn_excluir_clientes_fisicos.setSizePolicy(sizePolicy)
        self.btn_excluir_clientes_fisicos.setMaximumSize(QSize(145, 30))
        self.btn_excluir_clientes_fisicos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_excluir_clientes_fisicos.setAutoFillBackground(False)
        self.btn_excluir_clientes_fisicos.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")

        self.horizontalLayout_29.addWidget(self.btn_excluir_clientes_fisicos)

        self.btn_gerar_relatorio_clientes_fisicos = QPushButton(self.frame_12)
        self.btn_gerar_relatorio_clientes_fisicos.setObjectName(u"btn_gerar_relatorio_clientes_fisicos")
        sizePolicy.setHeightForWidth(self.btn_gerar_relatorio_clientes_fisicos.sizePolicy().hasHeightForWidth())
        self.btn_gerar_relatorio_clientes_fisicos.setSizePolicy(sizePolicy)
        self.btn_gerar_relatorio_clientes_fisicos.setMaximumSize(QSize(145, 27))
        self.btn_gerar_relatorio_clientes_fisicos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_gerar_relatorio_clientes_fisicos.setAutoFillBackground(False)
        self.btn_gerar_relatorio_clientes_fisicos.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")

        self.horizontalLayout_29.addWidget(self.btn_gerar_relatorio_clientes_fisicos)

        self.btn_marcar_como_clientes_fisicos = QPushButton(self.frame_12)
        self.btn_marcar_como_clientes_fisicos.setObjectName(u"btn_marcar_como_clientes_fisicos")
        sizePolicy.setHeightForWidth(self.btn_marcar_como_clientes_fisicos.sizePolicy().hasHeightForWidth())
        self.btn_marcar_como_clientes_fisicos.setSizePolicy(sizePolicy)
        self.btn_marcar_como_clientes_fisicos.setMaximumSize(QSize(145, 27))
        self.btn_marcar_como_clientes_fisicos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_marcar_como_clientes_fisicos.setAutoFillBackground(False)
        self.btn_marcar_como_clientes_fisicos.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")

        self.horizontalLayout_29.addWidget(self.btn_marcar_como_clientes_fisicos)

        self.btn_historico_clientes_fisicos = QPushButton(self.frame_12)
        self.btn_historico_clientes_fisicos.setObjectName(u"btn_historico_clientes_fisicos")
        sizePolicy.setHeightForWidth(self.btn_historico_clientes_fisicos.sizePolicy().hasHeightForWidth())
        self.btn_historico_clientes_fisicos.setSizePolicy(sizePolicy)
        self.btn_historico_clientes_fisicos.setMaximumSize(QSize(145, 27))
        self.btn_historico_clientes_fisicos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_historico_clientes_fisicos.setAutoFillBackground(False)
        self.btn_historico_clientes_fisicos.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}")

        self.horizontalLayout_29.addWidget(self.btn_historico_clientes_fisicos)


        self.verticalLayout_23.addLayout(self.horizontalLayout_29)


        self.gridLayout_28.addWidget(self.frame_12, 0, 1, 1, 1)

        self.table_clientes_fisicos = QTableWidget(self.tab_3)
        if (self.table_clientes_fisicos.columnCount() < 18):
            self.table_clientes_fisicos.setColumnCount(18)
        __qtablewidgetitem90 = QTableWidgetItem()
        self.table_clientes_fisicos.setHorizontalHeaderItem(0, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        self.table_clientes_fisicos.setHorizontalHeaderItem(1, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        self.table_clientes_fisicos.setHorizontalHeaderItem(2, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        self.table_clientes_fisicos.setHorizontalHeaderItem(3, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        self.table_clientes_fisicos.setHorizontalHeaderItem(4, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        self.table_clientes_fisicos.setHorizontalHeaderItem(5, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        self.table_clientes_fisicos.setHorizontalHeaderItem(6, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        self.table_clientes_fisicos.setHorizontalHeaderItem(7, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        self.table_clientes_fisicos.setHorizontalHeaderItem(8, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        self.table_clientes_fisicos.setHorizontalHeaderItem(9, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        self.table_clientes_fisicos.setHorizontalHeaderItem(10, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        self.table_clientes_fisicos.setHorizontalHeaderItem(11, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        self.table_clientes_fisicos.setHorizontalHeaderItem(12, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        self.table_clientes_fisicos.setHorizontalHeaderItem(13, __qtablewidgetitem103)
        __qtablewidgetitem104 = QTableWidgetItem()
        self.table_clientes_fisicos.setHorizontalHeaderItem(14, __qtablewidgetitem104)
        __qtablewidgetitem105 = QTableWidgetItem()
        self.table_clientes_fisicos.setHorizontalHeaderItem(15, __qtablewidgetitem105)
        __qtablewidgetitem106 = QTableWidgetItem()
        self.table_clientes_fisicos.setHorizontalHeaderItem(16, __qtablewidgetitem106)
        __qtablewidgetitem107 = QTableWidgetItem()
        self.table_clientes_fisicos.setHorizontalHeaderItem(17, __qtablewidgetitem107)
        self.table_clientes_fisicos.setObjectName(u"table_clientes_fisicos")
        self.table_clientes_fisicos.setStyleSheet(u"/* Estiliza apenas o QTableView com objectName \"table_ativos\" */\n"
"QTableView {\n"
"    gridline-color: black;\n"
"    border: 2px solid white;\n"
"    color: black;\n"
"    selection-color: white;\n"
"}\n"
"\n"
"/* Estiliza a barra de rolagem horizontal */\n"
"QTableView QScrollBar:horizontal {\n"
"    border: none;\n"
"    background-color: rgb(255, 255, 255);\n"
"    height: 15px;\n"
"    margin: 0px 10px 0px 10px;\n"
"}\n"
"\n"
"/* Estiliza a barra de rolagem vertical */\n"
"QTableView QScrollBar:vertical {\n"
"    border: none;\n"
"    background-color: rgb(255, 255, 255); /* branco */\n"
"    width: 35px;\n"
"    margin: 0px 10px 0px 10px;\n"
"}\n"
"\n"
"/* Parte que voc\u00ea arrasta */\n"
"QTableView QScrollBar::handle:vertical {\n"
"    background-color: rgb(180, 180,150);  /* cinza */\n"
"    min-height: 30px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QTableView QScrollBar::handle:horizontal{\n"
"	background-color: rgb(180,180,150);\n"
"	min-height: 30px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"/* "
                        "Remove os bot\u00f5es */\n"
"QTableView QScrollBar::add-line:vertical,\n"
"QTableView QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"    width: 0px;\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"QTableView QScrollBar::groove:horizontal{\n"
"	background-color: rgb(100,240,240);\n"
"	border-radius: 2px;\n"
"	height: 15px;\n"
"	margin: 0px 10px 0px 10px;\n"
"}\n"
"\n"
"/* Estilo para item selecionado */\n"
"QTableWidget::item:selected {\n"
"    background-color: rgb(0, 120, 215);\n"
"    color: white;\n"
"}")
        self.table_clientes_fisicos.setFrameShape(QFrame.Box)
        self.table_clientes_fisicos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_clientes_fisicos.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_clientes_fisicos.setGridStyle(Qt.SolidLine)
        self.table_clientes_fisicos.setCornerButtonEnabled(False)
        self.table_clientes_fisicos.horizontalHeader().setCascadingSectionResizes(False)
        self.table_clientes_fisicos.horizontalHeader().setDefaultSectionSize(118)
        self.table_clientes_fisicos.verticalHeader().setVisible(False)

        self.gridLayout_28.addWidget(self.table_clientes_fisicos, 1, 0, 1, 2)

        self.tab_clientes_todos.addTab(self.tab_3, "")

        self.gridLayout_18.addWidget(self.tab_clientes_todos, 0, 0, 1, 1)


        self.gridLayout_15.addWidget(self.frame_pg_clientes, 0, 0, 1, 1)

        self.paginas_sistemas.addWidget(self.pg_clientes)
        self.pg_configuracoes = QWidget()
        self.pg_configuracoes.setObjectName(u"pg_configuracoes")
        sizePolicy.setHeightForWidth(self.pg_configuracoes.sizePolicy().hasHeightForWidth())
        self.pg_configuracoes.setSizePolicy(sizePolicy)
        self.gridLayout_16 = QGridLayout(self.pg_configuracoes)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.frame_pg_configuracoes = QFrame(self.pg_configuracoes)
        self.frame_pg_configuracoes.setObjectName(u"frame_pg_configuracoes")
        sizePolicy.setHeightForWidth(self.frame_pg_configuracoes.sizePolicy().hasHeightForWidth())
        self.frame_pg_configuracoes.setSizePolicy(sizePolicy)
        self.frame_pg_configuracoes.setFrameShape(QFrame.NoFrame)
        self.frame_pg_configuracoes.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.frame_pg_configuracoes)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.horizontalSpacer_4 = QSpacerItem(398, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)

        self.label_configuracoes = QLabel(self.frame_pg_configuracoes)
        self.label_configuracoes.setObjectName(u"label_configuracoes")
        sizePolicy.setHeightForWidth(self.label_configuracoes.sizePolicy().hasHeightForWidth())
        self.label_configuracoes.setSizePolicy(sizePolicy)
        self.label_configuracoes.setMaximumSize(QSize(16777215, 50))
        self.label_configuracoes.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"	border: 3px solid white;\n"
"	border-radius: 8px;\n"
"}\n"
"")

        self.gridLayout_17.addWidget(self.label_configuracoes, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(438, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.frame_botoes_configuracoes = QFrame(self.frame_pg_configuracoes)
        self.frame_botoes_configuracoes.setObjectName(u"frame_botoes_configuracoes")
        sizePolicy.setHeightForWidth(self.frame_botoes_configuracoes.sizePolicy().hasHeightForWidth())
        self.frame_botoes_configuracoes.setSizePolicy(sizePolicy)
        self.frame_botoes_configuracoes.setMinimumSize(QSize(0, 703))
        self.frame_botoes_configuracoes.setMaximumSize(QSize(16777215, 691))
        self.frame_botoes_configuracoes.setStyleSheet(u"QFrame#frame_botoes_configuracoes {	\n"
"        border: 2px solid white;\n"
"		border-radius: 10px;\n"
"		padding: 5px;\n"
"}")
        self.frame_botoes_configuracoes.setFrameShape(QFrame.NoFrame)
        self.frame_botoes_configuracoes.setFrameShadow(QFrame.Raised)
        self.frame_botoes_config = QFrame(self.frame_botoes_configuracoes)
        self.frame_botoes_config.setObjectName(u"frame_botoes_config")
        self.frame_botoes_config.setGeometry(QRect(9, 19, 181, 660))
        sizePolicy.setHeightForWidth(self.frame_botoes_config.sizePolicy().hasHeightForWidth())
        self.frame_botoes_config.setSizePolicy(sizePolicy)
        self.frame_botoes_config.setMinimumSize(QSize(0, 660))
        self.frame_botoes_config.setMaximumSize(QSize(16777215, 612))
        self.frame_botoes_config.setFrameShape(QFrame.NoFrame)
        self.frame_botoes_config.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_botoes_config)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.tool_tema = QToolButton(self.frame_botoes_config)
        self.tool_tema.setObjectName(u"tool_tema")
        sizePolicy.setHeightForWidth(self.tool_tema.sizePolicy().hasHeightForWidth())
        self.tool_tema.setSizePolicy(sizePolicy)
        self.tool_tema.setMaximumSize(QSize(150, 30))
        self.tool_tema.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
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

        self.verticalLayout_17.addWidget(self.tool_tema)

        self.tool_atalhos = QToolButton(self.frame_botoes_config)
        self.tool_atalhos.setObjectName(u"tool_atalhos")
        sizePolicy.setHeightForWidth(self.tool_atalhos.sizePolicy().hasHeightForWidth())
        self.tool_atalhos.setSizePolicy(sizePolicy)
        self.tool_atalhos.setMaximumSize(QSize(150, 30))
        self.tool_atalhos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
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

        self.verticalLayout_17.addWidget(self.tool_atalhos)

        self.tool_hora = QToolButton(self.frame_botoes_config)
        self.tool_hora.setObjectName(u"tool_hora")
        sizePolicy.setHeightForWidth(self.tool_hora.sizePolicy().hasHeightForWidth())
        self.tool_hora.setSizePolicy(sizePolicy)
        self.tool_hora.setMaximumSize(QSize(150, 30))
        self.tool_hora.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
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
        self.tool_hora.setToolButtonStyle(Qt.ToolButtonTextOnly)

        self.verticalLayout_17.addWidget(self.tool_hora)

        self.tool_fonte = QToolButton(self.frame_botoes_config)
        self.tool_fonte.setObjectName(u"tool_fonte")
        sizePolicy.setHeightForWidth(self.tool_fonte.sizePolicy().hasHeightForWidth())
        self.tool_fonte.setSizePolicy(sizePolicy)
        self.tool_fonte.setMaximumSize(QSize(150, 30))
        self.tool_fonte.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
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
        self.tool_fonte.setToolButtonStyle(Qt.ToolButtonTextOnly)

        self.verticalLayout_17.addWidget(self.tool_fonte)

        self.tool_atualizacoes = QToolButton(self.frame_botoes_config)
        self.tool_atualizacoes.setObjectName(u"tool_atualizacoes")
        sizePolicy.setHeightForWidth(self.tool_atualizacoes.sizePolicy().hasHeightForWidth())
        self.tool_atualizacoes.setSizePolicy(sizePolicy)
        self.tool_atualizacoes.setMaximumSize(QSize(150, 30))
        self.tool_atualizacoes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
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

        self.verticalLayout_17.addWidget(self.tool_atualizacoes)

        self.tool_notificacoes = QToolButton(self.frame_botoes_config)
        self.tool_notificacoes.setObjectName(u"tool_notificacoes")
        sizePolicy.setHeightForWidth(self.tool_notificacoes.sizePolicy().hasHeightForWidth())
        self.tool_notificacoes.setSizePolicy(sizePolicy)
        self.tool_notificacoes.setMaximumSize(QSize(150, 30))
        self.tool_notificacoes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.tool_notificacoes.setStyleSheet(u"QToolButton {\n"
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
        self.tool_notificacoes.setPopupMode(QToolButton.MenuButtonPopup)
        self.tool_notificacoes.setToolButtonStyle(Qt.ToolButtonTextOnly)

        self.verticalLayout_17.addWidget(self.tool_notificacoes)


        self.gridLayout_17.addWidget(self.frame_botoes_configuracoes, 1, 0, 1, 3)


        self.gridLayout_16.addWidget(self.frame_pg_configuracoes, 0, 0, 1, 1)

        self.paginas_sistemas.addWidget(self.pg_configuracoes)
        self.pg_contato = QWidget()
        self.pg_contato.setObjectName(u"pg_contato")
        self.gridLayout_19 = QGridLayout(self.pg_contato)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.frame_pg_contato = QFrame(self.pg_contato)
        self.frame_pg_contato.setObjectName(u"frame_pg_contato")
        self.frame_pg_contato.setFrameShape(QFrame.NoFrame)
        self.frame_pg_contato.setFrameShadow(QFrame.Raised)
        self.gridLayout_20 = QGridLayout(self.frame_pg_contato)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.horizontalSpacer_7 = QSpacerItem(408, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_7, 0, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(388, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_8, 0, 2, 1, 1)

        self.frame_desenvolvido = QFrame(self.frame_pg_contato)
        self.frame_desenvolvido.setObjectName(u"frame_desenvolvido")
        sizePolicy.setHeightForWidth(self.frame_desenvolvido.sizePolicy().hasHeightForWidth())
        self.frame_desenvolvido.setSizePolicy(sizePolicy)
        self.frame_desenvolvido.setMaximumSize(QSize(16777215, 204))
        self.frame_desenvolvido.setFrameShape(QFrame.NoFrame)
        self.frame_desenvolvido.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_desenvolvido)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_desenvolvido = QLabel(self.frame_desenvolvido)
        self.label_desenvolvido.setObjectName(u"label_desenvolvido")
        self.label_desenvolvido.setStyleSheet(u"QLabel {\n"
"    color: black;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"\n"
"}\n"
"\n"
"")

        self.verticalLayout_18.addWidget(self.label_desenvolvido)


        self.gridLayout_20.addWidget(self.frame_desenvolvido, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_20.addItem(self.verticalSpacer, 1, 1, 1, 1)


        self.gridLayout_19.addWidget(self.frame_pg_contato, 0, 0, 1, 1)

        self.paginas_sistemas.addWidget(self.pg_contato)
        self.page_cadastrar_massa_produtos = QWidget()
        self.page_cadastrar_massa_produtos.setObjectName(u"page_cadastrar_massa_produtos")
        self.gridLayout_12 = QGridLayout(self.page_cadastrar_massa_produtos)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.frame_8 = QFrame(self.page_cadastrar_massa_produtos)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_23 = QGridLayout(self.frame_8)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setMinimumSize(QSize(0, 0))
        self.frame_9.setMaximumSize(QSize(16777214, 200))
        self.frame_9.setFrameShape(QFrame.Box)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_9)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(9, -1, 9, -1)
        self.btn_fazer_cadastro_massa_produtos = QPushButton(self.frame_9)
        self.btn_fazer_cadastro_massa_produtos.setObjectName(u"btn_fazer_cadastro_massa_produtos")
        sizePolicy.setHeightForWidth(self.btn_fazer_cadastro_massa_produtos.sizePolicy().hasHeightForWidth())
        self.btn_fazer_cadastro_massa_produtos.setSizePolicy(sizePolicy)
        self.btn_fazer_cadastro_massa_produtos.setMinimumSize(QSize(0, 0))
        self.btn_fazer_cadastro_massa_produtos.setMaximumSize(QSize(16777215, 31))
        self.btn_fazer_cadastro_massa_produtos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_fazer_cadastro_massa_produtos.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}\n"
"")

        self.verticalLayout_22.addWidget(self.btn_fazer_cadastro_massa_produtos)

        self.btn_abrir_planilha_massa_produtos = QPushButton(self.frame_9)
        self.btn_abrir_planilha_massa_produtos.setObjectName(u"btn_abrir_planilha_massa_produtos")
        sizePolicy.setHeightForWidth(self.btn_abrir_planilha_massa_produtos.sizePolicy().hasHeightForWidth())
        self.btn_abrir_planilha_massa_produtos.setSizePolicy(sizePolicy)
        self.btn_abrir_planilha_massa_produtos.setMaximumSize(QSize(16777215, 31))
        self.btn_abrir_planilha_massa_produtos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_abrir_planilha_massa_produtos.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}\n"
"")

        self.verticalLayout_22.addWidget(self.btn_abrir_planilha_massa_produtos)

        self.btn_editar_massa_produtos = QPushButton(self.frame_9)
        self.btn_editar_massa_produtos.setObjectName(u"btn_editar_massa_produtos")
        sizePolicy.setHeightForWidth(self.btn_editar_massa_produtos.sizePolicy().hasHeightForWidth())
        self.btn_editar_massa_produtos.setSizePolicy(sizePolicy)
        self.btn_editar_massa_produtos.setMaximumSize(QSize(16777215, 31))
        self.btn_editar_massa_produtos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_editar_massa_produtos.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}\n"
"")

        self.verticalLayout_22.addWidget(self.btn_editar_massa_produtos)

        self.progress_massa_produtos = QProgressBar(self.frame_9)
        self.progress_massa_produtos.setObjectName(u"progress_massa_produtos")
        sizePolicy.setHeightForWidth(self.progress_massa_produtos.sizePolicy().hasHeightForWidth())
        self.progress_massa_produtos.setSizePolicy(sizePolicy)
        self.progress_massa_produtos.setMaximumSize(QSize(16777215, 31))
        self.progress_massa_produtos.setStyleSheet(u"QProgressBar {\n"
"	color: black;\n"
"    border: 3px solid rgb(50,150,250);\n"
"    border-radius: 13px;  /* Aumentei o valor para deixar a borda mais redonda */\n"
"    background-color: #f0f0f0;  /* Cor cinza claro */\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #4682b4;  /* Cor do progresso preenchido (azul) */\n"
"    border-radius: 12px;  /* Faz com que o progresso tamb\u00e9m tenha bordas arredondadas */\n"
"}\n"
"")
        self.progress_massa_produtos.setValue(0)
        self.progress_massa_produtos.setAlignment(Qt.AlignCenter)
        self.progress_massa_produtos.setTextVisible(True)

        self.verticalLayout_22.addWidget(self.progress_massa_produtos)

        self.line_edit_massa_produtos = QLineEdit(self.frame_9)
        self.line_edit_massa_produtos.setObjectName(u"line_edit_massa_produtos")
        sizePolicy.setHeightForWidth(self.line_edit_massa_produtos.sizePolicy().hasHeightForWidth())
        self.line_edit_massa_produtos.setSizePolicy(sizePolicy)
        self.line_edit_massa_produtos.setMaximumSize(QSize(16777215, 31))
        self.line_edit_massa_produtos.setStyleSheet(u"QLineEdit {\n"
"	color: black;\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150,250); /* Borda azul */\n"
"    border-radius: 12px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QLineEdit::placeholderText {\n"
"    color: black; /* Cor do texto do placeholder */\n"
"}\n"
"\n"
"")
        self.line_edit_massa_produtos.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.line_edit_massa_produtos)


        self.gridLayout_23.addWidget(self.frame_9, 0, 0, 1, 1)

        self.table_massa_produtos = QTableWidget(self.frame_8)
        if (self.table_massa_produtos.columnCount() < 9):
            self.table_massa_produtos.setColumnCount(9)
        __qtablewidgetitem108 = QTableWidgetItem()
        self.table_massa_produtos.setHorizontalHeaderItem(0, __qtablewidgetitem108)
        __qtablewidgetitem109 = QTableWidgetItem()
        self.table_massa_produtos.setHorizontalHeaderItem(1, __qtablewidgetitem109)
        __qtablewidgetitem110 = QTableWidgetItem()
        self.table_massa_produtos.setHorizontalHeaderItem(2, __qtablewidgetitem110)
        __qtablewidgetitem111 = QTableWidgetItem()
        self.table_massa_produtos.setHorizontalHeaderItem(3, __qtablewidgetitem111)
        __qtablewidgetitem112 = QTableWidgetItem()
        self.table_massa_produtos.setHorizontalHeaderItem(4, __qtablewidgetitem112)
        __qtablewidgetitem113 = QTableWidgetItem()
        self.table_massa_produtos.setHorizontalHeaderItem(5, __qtablewidgetitem113)
        __qtablewidgetitem114 = QTableWidgetItem()
        self.table_massa_produtos.setHorizontalHeaderItem(6, __qtablewidgetitem114)
        __qtablewidgetitem115 = QTableWidgetItem()
        self.table_massa_produtos.setHorizontalHeaderItem(7, __qtablewidgetitem115)
        __qtablewidgetitem116 = QTableWidgetItem()
        self.table_massa_produtos.setHorizontalHeaderItem(8, __qtablewidgetitem116)
        self.table_massa_produtos.setObjectName(u"table_massa_produtos")
        self.table_massa_produtos.setMinimumSize(QSize(0, 0))
        self.table_massa_produtos.setMaximumSize(QSize(16777215, 16777215))
        self.table_massa_produtos.setStyleSheet(u"/* Estiliza apenas o QTableView com objectName \"table_ativos\" */\n"
"QTableView {\n"
"    gridline-color: black;\n"
"    border: 2px solid white;\n"
"    color: black;\n"
"    selection-color: white;\n"
"}\n"
"\n"
"/* Estiliza a barra de rolagem horizontal */\n"
"QTableView QScrollBar:horizontal {\n"
"    border: none;\n"
"    background-color: rgb(255, 255, 255);\n"
"    height: 15px;\n"
"    margin: 0px \n"
"}\n"
"\n"
"/* Estiliza a barra de rolagem vertical */\n"
"QTableView QScrollBar:vertical {\n"
"    border: none;\n"
"    background-color: rgb(255, 255, 255); /* branco */\n"
"    width: 20px;\n"
"    margin: 0px \n"
"}\n"
"\n"
"/* Parte que voc\u00ea arrasta */\n"
"QTableView QScrollBar::handle:vertical {\n"
"    background-color: rgb(180, 180,150);  /* cinza */\n"
"    min-height: 30px;\n"
"}\n"
"\n"
"QTableView QScrollBar::handle:horizontal{\n"
"	background-color: rgb(180,180,150);\n"
"	min-height: 30px;\n"
"}\n"
"\n"
"/* Remove os bot\u00f5es */\n"
"QTableView QScrollBar::add-line:vertical,\n"
"QTa"
                        "bleView QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"    width: 0px;\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"/* Estilo para item selecionado */\n"
"QTableWidget::item:selected {\n"
"    background-color: rgb(0, 120, 215);\n"
"    color: white;\n"
"}\n"
"")
        self.table_massa_produtos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_massa_produtos.setProperty(u"showDropIndicator", True)
        self.table_massa_produtos.setDragDropOverwriteMode(True)
        self.table_massa_produtos.setAlternatingRowColors(False)
        self.table_massa_produtos.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_massa_produtos.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_massa_produtos.setShowGrid(True)
        self.table_massa_produtos.setGridStyle(Qt.SolidLine)
        self.table_massa_produtos.setCornerButtonEnabled(False)
        self.table_massa_produtos.horizontalHeader().setCascadingSectionResizes(False)
        self.table_massa_produtos.horizontalHeader().setMinimumSectionSize(39)
        self.table_massa_produtos.horizontalHeader().setDefaultSectionSize(112)
        self.table_massa_produtos.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.table_massa_produtos.verticalHeader().setVisible(False)
        self.table_massa_produtos.verticalHeader().setCascadingSectionResizes(False)
        self.table_massa_produtos.verticalHeader().setHighlightSections(True)

        self.gridLayout_23.addWidget(self.table_massa_produtos, 1, 0, 1, 1)


        self.gridLayout_12.addWidget(self.frame_8, 0, 0, 1, 1)

        self.paginas_sistemas.addWidget(self.page_cadastrar_massa_produtos)
        self.page_cadastrar_massa_usuarios = QWidget()
        self.page_cadastrar_massa_usuarios.setObjectName(u"page_cadastrar_massa_usuarios")
        self.gridLayout_24 = QGridLayout(self.page_cadastrar_massa_usuarios)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.frame_10 = QFrame(self.page_cadastrar_massa_usuarios)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_25 = QGridLayout(self.frame_10)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy)
        self.frame_11.setMinimumSize(QSize(0, 0))
        self.frame_11.setMaximumSize(QSize(16777214, 200))
        self.frame_11.setFrameShape(QFrame.Box)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_26 = QGridLayout(self.frame_11)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setContentsMargins(9, -1, 9, -1)
        self.btn_abrir_planilha_massa_usuarios = QPushButton(self.frame_11)
        self.btn_abrir_planilha_massa_usuarios.setObjectName(u"btn_abrir_planilha_massa_usuarios")
        sizePolicy.setHeightForWidth(self.btn_abrir_planilha_massa_usuarios.sizePolicy().hasHeightForWidth())
        self.btn_abrir_planilha_massa_usuarios.setSizePolicy(sizePolicy)
        self.btn_abrir_planilha_massa_usuarios.setMinimumSize(QSize(0, 31))
        self.btn_abrir_planilha_massa_usuarios.setMaximumSize(QSize(16777215, 31))
        self.btn_abrir_planilha_massa_usuarios.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_abrir_planilha_massa_usuarios.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}\n"
"")

        self.gridLayout_26.addWidget(self.btn_abrir_planilha_massa_usuarios, 1, 0, 1, 1)

        self.btn_editar_massa_usuario = QPushButton(self.frame_11)
        self.btn_editar_massa_usuario.setObjectName(u"btn_editar_massa_usuario")
        sizePolicy.setHeightForWidth(self.btn_editar_massa_usuario.sizePolicy().hasHeightForWidth())
        self.btn_editar_massa_usuario.setSizePolicy(sizePolicy)
        self.btn_editar_massa_usuario.setMinimumSize(QSize(0, 31))
        self.btn_editar_massa_usuario.setMaximumSize(QSize(16777215, 31))
        self.btn_editar_massa_usuario.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_editar_massa_usuario.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}\n"
"")

        self.gridLayout_26.addWidget(self.btn_editar_massa_usuario, 2, 0, 1, 1)

        self.line_edit_massa_usuarios = QLineEdit(self.frame_11)
        self.line_edit_massa_usuarios.setObjectName(u"line_edit_massa_usuarios")
        sizePolicy.setHeightForWidth(self.line_edit_massa_usuarios.sizePolicy().hasHeightForWidth())
        self.line_edit_massa_usuarios.setSizePolicy(sizePolicy)
        self.line_edit_massa_usuarios.setMinimumSize(QSize(0, 31))
        self.line_edit_massa_usuarios.setMaximumSize(QSize(16777215, 31))
        self.line_edit_massa_usuarios.setStyleSheet(u"QLineEdit {\n"
"	color: black;\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150,250); /* Borda azul */\n"
"    border-radius: 12px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QLineEdit::placeholderText {\n"
"    color: black; /* Cor do texto do placeholder */\n"
"}\n"
"\n"
"")
        self.line_edit_massa_usuarios.setAlignment(Qt.AlignCenter)

        self.gridLayout_26.addWidget(self.line_edit_massa_usuarios, 4, 0, 1, 1)

        self.progress_massa_usuarios = QProgressBar(self.frame_11)
        self.progress_massa_usuarios.setObjectName(u"progress_massa_usuarios")
        sizePolicy.setHeightForWidth(self.progress_massa_usuarios.sizePolicy().hasHeightForWidth())
        self.progress_massa_usuarios.setSizePolicy(sizePolicy)
        self.progress_massa_usuarios.setMinimumSize(QSize(0, 31))
        self.progress_massa_usuarios.setMaximumSize(QSize(16777215, 31))
        self.progress_massa_usuarios.setStyleSheet(u"QProgressBar {\n"
"	color: black;\n"
"    border: 3px solid rgb(50,150,250);\n"
"    border-radius: 13px;  /* Aumentei o valor para deixar a borda mais redonda */\n"
"    background-color: #f0f0f0;  /* Cor cinza claro */\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #4682b4;  /* Cor do progresso preenchido (azul) */\n"
"    border-radius: 12px;  /* Faz com que o progresso tamb\u00e9m tenha bordas arredondadas */\n"
"}\n"
"")
        self.progress_massa_usuarios.setValue(0)
        self.progress_massa_usuarios.setAlignment(Qt.AlignCenter)
        self.progress_massa_usuarios.setTextVisible(True)

        self.gridLayout_26.addWidget(self.progress_massa_usuarios, 3, 0, 1, 1)

        self.btn_fazer_cadastro_massa_usuarios = QPushButton(self.frame_11)
        self.btn_fazer_cadastro_massa_usuarios.setObjectName(u"btn_fazer_cadastro_massa_usuarios")
        sizePolicy.setHeightForWidth(self.btn_fazer_cadastro_massa_usuarios.sizePolicy().hasHeightForWidth())
        self.btn_fazer_cadastro_massa_usuarios.setSizePolicy(sizePolicy)
        self.btn_fazer_cadastro_massa_usuarios.setMinimumSize(QSize(0, 31))
        self.btn_fazer_cadastro_massa_usuarios.setMaximumSize(QSize(16777215, 31))
        self.btn_fazer_cadastro_massa_usuarios.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_fazer_cadastro_massa_usuarios.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 4px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}\n"
"")

        self.gridLayout_26.addWidget(self.btn_fazer_cadastro_massa_usuarios, 0, 0, 1, 1)


        self.gridLayout_25.addWidget(self.frame_11, 0, 0, 1, 1)

        self.table_massa_usuarios = QTableWidget(self.frame_10)
        if (self.table_massa_usuarios.columnCount() < 18):
            self.table_massa_usuarios.setColumnCount(18)
        __qtablewidgetitem117 = QTableWidgetItem()
        self.table_massa_usuarios.setHorizontalHeaderItem(0, __qtablewidgetitem117)
        __qtablewidgetitem118 = QTableWidgetItem()
        self.table_massa_usuarios.setHorizontalHeaderItem(1, __qtablewidgetitem118)
        __qtablewidgetitem119 = QTableWidgetItem()
        self.table_massa_usuarios.setHorizontalHeaderItem(2, __qtablewidgetitem119)
        __qtablewidgetitem120 = QTableWidgetItem()
        self.table_massa_usuarios.setHorizontalHeaderItem(3, __qtablewidgetitem120)
        __qtablewidgetitem121 = QTableWidgetItem()
        self.table_massa_usuarios.setHorizontalHeaderItem(4, __qtablewidgetitem121)
        __qtablewidgetitem122 = QTableWidgetItem()
        self.table_massa_usuarios.setHorizontalHeaderItem(5, __qtablewidgetitem122)
        __qtablewidgetitem123 = QTableWidgetItem()
        self.table_massa_usuarios.setHorizontalHeaderItem(6, __qtablewidgetitem123)
        __qtablewidgetitem124 = QTableWidgetItem()
        self.table_massa_usuarios.setHorizontalHeaderItem(7, __qtablewidgetitem124)
        __qtablewidgetitem125 = QTableWidgetItem()
        self.table_massa_usuarios.setHorizontalHeaderItem(8, __qtablewidgetitem125)
        __qtablewidgetitem126 = QTableWidgetItem()
        self.table_massa_usuarios.setHorizontalHeaderItem(9, __qtablewidgetitem126)
        __qtablewidgetitem127 = QTableWidgetItem()
        self.table_massa_usuarios.setHorizontalHeaderItem(10, __qtablewidgetitem127)
        __qtablewidgetitem128 = QTableWidgetItem()
        self.table_massa_usuarios.setHorizontalHeaderItem(11, __qtablewidgetitem128)
        __qtablewidgetitem129 = QTableWidgetItem()
        self.table_massa_usuarios.setHorizontalHeaderItem(12, __qtablewidgetitem129)
        __qtablewidgetitem130 = QTableWidgetItem()
        self.table_massa_usuarios.setHorizontalHeaderItem(13, __qtablewidgetitem130)
        __qtablewidgetitem131 = QTableWidgetItem()
        self.table_massa_usuarios.setHorizontalHeaderItem(14, __qtablewidgetitem131)
        __qtablewidgetitem132 = QTableWidgetItem()
        self.table_massa_usuarios.setHorizontalHeaderItem(15, __qtablewidgetitem132)
        __qtablewidgetitem133 = QTableWidgetItem()
        self.table_massa_usuarios.setHorizontalHeaderItem(16, __qtablewidgetitem133)
        __qtablewidgetitem134 = QTableWidgetItem()
        self.table_massa_usuarios.setHorizontalHeaderItem(17, __qtablewidgetitem134)
        self.table_massa_usuarios.setObjectName(u"table_massa_usuarios")
        self.table_massa_usuarios.setMinimumSize(QSize(0, 0))
        self.table_massa_usuarios.setMaximumSize(QSize(16777215, 16777215))
        self.table_massa_usuarios.setStyleSheet(u"/* Estiliza apenas o QTableView com objectName \"table_ativos\" */\n"
"QTableView {\n"
"    gridline-color: black;\n"
"    border: 2px solid white;\n"
"    color: black;\n"
"    selection-color: white;\n"
"}\n"
"\n"
"/* Estiliza a barra de rolagem horizontal */\n"
"QTableView QScrollBar:horizontal {\n"
"    border: none;\n"
"    background-color: rgb(255, 255, 255);\n"
"    height: 15px;\n"
"    margin: 0px 10px 0px 10px;\n"
"}\n"
"\n"
"/* Estiliza a barra de rolagem vertical */\n"
"QTableView QScrollBar:vertical {\n"
"    border: none;\n"
"    background-color: rgb(255, 255, 255); /* branco */\n"
"    width: 35px;\n"
"    margin: 0px 10px 0px 10px;\n"
"}\n"
"\n"
"/* Parte que voc\u00ea arrasta */\n"
"QTableView QScrollBar::handle:vertical {\n"
"    background-color: rgb(180, 180,150);  /* cinza */\n"
"    min-height: 30px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QTableView QScrollBar::handle:horizontal{\n"
"	background-color: rgb(180,180,150);\n"
"	min-height: 30px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"/* "
                        "Remove os bot\u00f5es */\n"
"QTableView QScrollBar::add-line:vertical,\n"
"QTableView QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"    width: 0px;\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"QTableView QScrollBar::groove:horizontal{\n"
"	background-color: rgb(100,240,240);\n"
"	border-radius: 2px;\n"
"	height: 15px;\n"
"	margin: 0px 10px 0px 10px;\n"
"}\n"
"\n"
"/* Estilo para item selecionado */\n"
"QTableWidget::item:selected {\n"
"    background-color: rgb(0, 120, 215);\n"
"    color: white;\n"
"}")
        self.table_massa_usuarios.setFrameShape(QFrame.NoFrame)
        self.table_massa_usuarios.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_massa_usuarios.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_massa_usuarios.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_massa_usuarios.setSortingEnabled(False)
        self.table_massa_usuarios.setCornerButtonEnabled(False)
        self.table_massa_usuarios.horizontalHeader().setCascadingSectionResizes(False)
        self.table_massa_usuarios.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.table_massa_usuarios.horizontalHeader().setStretchLastSection(False)
        self.table_massa_usuarios.verticalHeader().setVisible(False)
        self.table_massa_usuarios.verticalHeader().setCascadingSectionResizes(False)
        self.table_massa_usuarios.verticalHeader().setStretchLastSection(False)

        self.gridLayout_25.addWidget(self.table_massa_usuarios, 1, 0, 1, 1)


        self.gridLayout_24.addWidget(self.frame_10, 0, 0, 1, 1)

        self.paginas_sistemas.addWidget(self.page_cadastrar_massa_usuarios)

        self.gridLayout_2.addWidget(self.paginas_sistemas, 1, 1, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tb_base.setCurrentIndex(0)
        self.tab_clientes_todos.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_configuracoes.setText(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es", None))
        self.btn_verificar_usuarios.setText(QCoreApplication.translate("MainWindow", u"Verificar Usu\u00e1rios", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_verificar_estoque.setText(QCoreApplication.translate("MainWindow", u"Verificar Estoque", None))
        self.btn_clientes.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.btn_cadastrar_usuarios.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Usu\u00e1rio", None))
        self.btn_cadastrar_produto.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Produto", None))
        self.btn_mais_opcoes.setText(QCoreApplication.translate("MainWindow", u"Mais op\u00e7\u00f5es", None))
        self.label_imagem_sistema.setText("")
        self.label_bem_vindo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; font-style:italic;\">Bem vindo(a) ao</span></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; font-style:italic;\">Sistema de Gerenciamento do </span></p><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; font-style:italic;\">controle de Estoque</span></p></body></html>", None))
        self.btn_abrir_planilha.setText(QCoreApplication.translate("MainWindow", u"Abrir Planilha", None))
        self.line_excel.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Arquivo em excel aparecer\u00e1 aqui", None))
        self.btn_novo_produto.setText(QCoreApplication.translate("MainWindow", u"Novo Produto", None))
        self.btn_atualizar_saida.setText(QCoreApplication.translate("MainWindow", u"Atualizar Sa\u00edda", None))
        self.btn_atualizar_estoque.setText(QCoreApplication.translate("MainWindow", u"Atualizar estoque", None))
        self.btn_historico.setText(QCoreApplication.translate("MainWindow", u"Hist\u00f3rico", None))
        self.btn_gerar_pdf.setText(QCoreApplication.translate("MainWindow", u"Gerar PDF", None))
        self.btn_limpar_tabelas.setText(QCoreApplication.translate("MainWindow", u"Limpar tabelas", None))
        self.btn_incluir_produto_sistema.setText(QCoreApplication.translate("MainWindow", u"Incluir produto no sistema", None))
#if QT_CONFIG(whatsthis)
        self.label_estoque.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">ESTOQUE</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_estoque.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">ESTOQUE</span></p></body></html>", None))
        ___qtablewidgetitem = self.table_base.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Produto", None));
        ___qtablewidgetitem1 = self.table_base.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtablewidgetitem2 = self.table_base.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Valor do Produto", None));
        ___qtablewidgetitem3 = self.table_base.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Desconto", None));
        ___qtablewidgetitem4 = self.table_base.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Valor Total", None));
        ___qtablewidgetitem5 = self.table_base.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Data do Cadastro", None));
        ___qtablewidgetitem6 = self.table_base.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo do Item", None));
        ___qtablewidgetitem7 = self.table_base.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Cliente", None));
        ___qtablewidgetitem8 = self.table_base.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o do Produto", None));
        ___qtablewidgetitem9 = self.table_base.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None));
        ___qtablewidgetitem10 = self.table_base.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Status da Sa\u00edda", None));
        self.label_saida.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; font-style:italic;\">SA\u00cdDA</span></p></body></html>", None))
        ___qtablewidgetitem11 = self.table_saida.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Produto", None));
        ___qtablewidgetitem12 = self.table_saida.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtablewidgetitem13 = self.table_saida.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Valor do Produto", None));
        ___qtablewidgetitem14 = self.table_saida.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Desconto", None));
        ___qtablewidgetitem15 = self.table_saida.horizontalHeaderItem(4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Valor Total", None));
        ___qtablewidgetitem16 = self.table_saida.horizontalHeaderItem(5)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Data da Sa\u00edda", None));
        ___qtablewidgetitem17 = self.table_saida.horizontalHeaderItem(6)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Data do Cadastro", None));
        ___qtablewidgetitem18 = self.table_saida.horizontalHeaderItem(7)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo do Produto", None));
        ___qtablewidgetitem19 = self.table_saida.horizontalHeaderItem(8)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Cliente", None));
        ___qtablewidgetitem20 = self.table_saida.horizontalHeaderItem(9)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o do Produto", None));
        ___qtablewidgetitem21 = self.table_saida.horizontalHeaderItem(10)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None));
        ___qtablewidgetitem22 = self.table_saida.horizontalHeaderItem(11)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Status da Sa\u00edda", None));
        self.btn_importar.setText(QCoreApplication.translate("MainWindow", u"Importar", None))
        self.btn_gerar_saida.setText(QCoreApplication.translate("MainWindow", u"Gerar S\u00e1ida", None))
        self.btn_gerar_estorno.setText(QCoreApplication.translate("MainWindow", u"Gerar Estorno", None))
        self.tb_base.setTabText(self.tb_base.indexOf(self.tabela_base), QCoreApplication.translate("MainWindow", u"Base", None))
        self.btn_atualizar_ativos.setText(QCoreApplication.translate("MainWindow", u"Atualizar Ativos", None))
        self.btn_cadastrar_novo_usuario.setText(QCoreApplication.translate("MainWindow", u"Nova Usu\u00e1rio", None))
        self.btn_limpar_tabelas_usuarios.setText(QCoreApplication.translate("MainWindow", u"Limpar Tabelas", None))
        self.btn_atualizar_inativos.setText(QCoreApplication.translate("MainWindow", u"Atualizar Inativos", None))
        self.btn_historico_usuarios.setText(QCoreApplication.translate("MainWindow", u"Hist\u00f3rico", None))
#if QT_CONFIG(whatsthis)
        self.label_inativos.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">ESTOQUE</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_inativos.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">INATIVOS</span></p></body></html>", None))
        self.btn_gerar_saida_usuarios.setText(QCoreApplication.translate("MainWindow", u"Gerar Sa\u00edda", None))
        self.btn_importar_usuarios.setText(QCoreApplication.translate("MainWindow", u"Importar", None))
#if QT_CONFIG(whatsthis)
        self.label_ativos.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">ESTOQUE</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_ativos.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">ATIVOS</span></p></body></html>", None))
        self.btn_abrir_planilha_usuarios.setText(QCoreApplication.translate("MainWindow", u"Abrir Planilha", None))
        self.line_excel_usuarios.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Arquivo em excel aparecer\u00e1 aqui", None))
        ___qtablewidgetitem23 = self.table_inativos.horizontalHeaderItem(0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem24 = self.table_inativos.horizontalHeaderItem(1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None));
        ___qtablewidgetitem25 = self.table_inativos.horizontalHeaderItem(2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Senha", None));
        ___qtablewidgetitem26 = self.table_inativos.horizontalHeaderItem(3)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Confirmar Senha", None));
        ___qtablewidgetitem27 = self.table_inativos.horizontalHeaderItem(4)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"CEP", None));
        ___qtablewidgetitem28 = self.table_inativos.horizontalHeaderItem(5)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None));
        ___qtablewidgetitem29 = self.table_inativos.horizontalHeaderItem(6)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"N\u00famero", None));
        ___qtablewidgetitem30 = self.table_inativos.horizontalHeaderItem(7)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Cidade", None));
        ___qtablewidgetitem31 = self.table_inativos.horizontalHeaderItem(8)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Bairro", None));
        ___qtablewidgetitem32 = self.table_inativos.horizontalHeaderItem(9)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Estado", None));
        ___qtablewidgetitem33 = self.table_inativos.horizontalHeaderItem(10)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Complemento", None));
        ___qtablewidgetitem34 = self.table_inativos.horizontalHeaderItem(11)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Telefone", None));
        ___qtablewidgetitem35 = self.table_inativos.horizontalHeaderItem(12)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"E-mail", None));
        ___qtablewidgetitem36 = self.table_inativos.horizontalHeaderItem(13)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Data de Nascimento", None));
        ___qtablewidgetitem37 = self.table_inativos.horizontalHeaderItem(14)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"RG", None));
        ___qtablewidgetitem38 = self.table_inativos.horizontalHeaderItem(15)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"CPF", None));
        ___qtablewidgetitem39 = self.table_inativos.horizontalHeaderItem(16)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"CNPJ", None));
        ___qtablewidgetitem40 = self.table_inativos.horizontalHeaderItem(17)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"\u00daltima Troca de Senha", None));
        ___qtablewidgetitem41 = self.table_inativos.horizontalHeaderItem(18)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Data da Senha Cadastrada", None));
        ___qtablewidgetitem42 = self.table_inativos.horizontalHeaderItem(19)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Data da Inclus\u00e3o do Usu\u00e1rio", None));
        ___qtablewidgetitem43 = self.table_inativos.horizontalHeaderItem(20)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Data da Inatividade do Usu\u00e1rio", None));
        ___qtablewidgetitem44 = self.table_inativos.horizontalHeaderItem(21)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Segredo", None));
        ___qtablewidgetitem45 = self.table_inativos.horizontalHeaderItem(22)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio Logado", None));
        ___qtablewidgetitem46 = self.table_inativos.horizontalHeaderItem(23)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Acesso", None));
        ___qtablewidgetitem47 = self.table_ativos.horizontalHeaderItem(0)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem48 = self.table_ativos.horizontalHeaderItem(1)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None));
        ___qtablewidgetitem49 = self.table_ativos.horizontalHeaderItem(2)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"Senha", None));
        ___qtablewidgetitem50 = self.table_ativos.horizontalHeaderItem(3)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"Confirmar Senha", None));
        ___qtablewidgetitem51 = self.table_ativos.horizontalHeaderItem(4)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"CEP", None));
        ___qtablewidgetitem52 = self.table_ativos.horizontalHeaderItem(5)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None));
        ___qtablewidgetitem53 = self.table_ativos.horizontalHeaderItem(6)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"N\u00famero", None));
        ___qtablewidgetitem54 = self.table_ativos.horizontalHeaderItem(7)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"Cidade", None));
        ___qtablewidgetitem55 = self.table_ativos.horizontalHeaderItem(8)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"Bairro", None));
        ___qtablewidgetitem56 = self.table_ativos.horizontalHeaderItem(9)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"Estado", None));
        ___qtablewidgetitem57 = self.table_ativos.horizontalHeaderItem(10)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"Complemento", None));
        ___qtablewidgetitem58 = self.table_ativos.horizontalHeaderItem(11)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"Telefone", None));
        ___qtablewidgetitem59 = self.table_ativos.horizontalHeaderItem(12)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"E-mail", None));
        ___qtablewidgetitem60 = self.table_ativos.horizontalHeaderItem(13)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"Data de Nascimento", None));
        ___qtablewidgetitem61 = self.table_ativos.horizontalHeaderItem(14)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"RG", None));
        ___qtablewidgetitem62 = self.table_ativos.horizontalHeaderItem(15)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"CPF", None));
        ___qtablewidgetitem63 = self.table_ativos.horizontalHeaderItem(16)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"CNPJ", None));
        ___qtablewidgetitem64 = self.table_ativos.horizontalHeaderItem(17)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"\u00daltima Troca de Senha", None));
        ___qtablewidgetitem65 = self.table_ativos.horizontalHeaderItem(18)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"Data da Senha Cadastrada ", None));
        ___qtablewidgetitem66 = self.table_ativos.horizontalHeaderItem(19)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"Data da Inclus\u00e3o do Usu\u00e1rio", None));
        ___qtablewidgetitem67 = self.table_ativos.horizontalHeaderItem(20)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"Segredo", None));
        ___qtablewidgetitem68 = self.table_ativos.horizontalHeaderItem(21)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio Logado", None));
        ___qtablewidgetitem69 = self.table_ativos.horizontalHeaderItem(22)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"Acesso", None));
        self.btn_adicionar_produto.setText(QCoreApplication.translate("MainWindow", u"ADICIONAR", None))
        self.btn_editar.setText(QCoreApplication.translate("MainWindow", u"EDITAR ", None))
        self.btn_sair_modo_edicao_produtos.setText(QCoreApplication.translate("MainWindow", u"SAIR DO MODO EDI\u00c7\u00c3O", None))
        self.btn_atualizar_produto.setText(QCoreApplication.translate("MainWindow", u"ATUALIZAR", None))
        self.btn_limpar_campos.setText(QCoreApplication.translate("MainWindow", u"APAGAR", None))
        self.label_produto.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Produto</span></p></body></html>", None))
        self.label_quantidade.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Quantidade</span></p></body></html>", None))
        self.label_valor_produto_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Valor do produto</span></p></body></html>", None))
        self.label_desconto_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Desconto</span></p></body></html>", None))
        self.txt_desconto_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Opcional", None))
        self.label_data_cadastro.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Data do Cadastro</span></p></body></html>", None))
        self.label_codigo_item_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">C\u00f3digo do Item</span></p></body></html>", None))
        self.label_cliente_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Cliente</span></p></body></html>", None))
        self.label_descricao_produto_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Descri\u00e7\u00e3o do Produto</span></p></body></html>", None))
        self.label_cadastramento_produtos.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">Cadastramento de Produtos</span></p></body></html>", None))
        self.btn_remover_imagem.setText(QCoreApplication.translate("MainWindow", u"REMOVER IMAGEM", None))
        self.btn_carregar_imagem.setText(QCoreApplication.translate("MainWindow", u"CARREGAR IMAGEM", None))
        self.btn_confirmar.setText(QCoreApplication.translate("MainWindow", u"CONFIRMAR", None))
        self.btn_ver_clientes_juridicos.setText(QCoreApplication.translate("MainWindow", u"VER CLIENTES", None))
        self.btn_ver_item.setText(QCoreApplication.translate("MainWindow", u"VER PRODUTOS", None))
        self.label_cadastramento.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; font-style:italic;\">CADASTRAMENTO DE USU\u00c1RIO</span></p></body></html>", None))
        self.label_confirmar_senha_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Bairro</span></p></body></html>", None))
        self.label_confirmar_senha_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">CNPJ</span></p></body></html>", None))
        self.label_complemento.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Complemento</span></p></body></html>", None))
        self.txt_complemento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Opcional", None))
        self.label_usuario.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Usu\u00e1rio</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">RG</span></p></body></html>", None))
        self.label_cpf.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">CPF</span></p></body></html>", None))
        self.label_nome.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Nome</span></p></body></html>", None))
        self.label_data_nascimento.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Data de Nascimento</span></p></body></html>", None))
        self.label_perfil.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Perfil</span></p></body></html>", None))
        self.perfil_usuarios.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.perfil_usuarios.setItemText(1, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.perfil_usuarios.setItemText(2, QCoreApplication.translate("MainWindow", u"Convidado", None))
        self.perfil_usuarios.setItemText(3, QCoreApplication.translate("MainWindow", u"Administrador", None))

        self.label_email.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">E-mail</span></p></body></html>", None))
        self.label_endereco.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Endere\u00e7o</span></p></body></html>", None))
        self.label_numero.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">N\u00famero</span></p></body></html>", None))
        self.label_cep.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">CEP</span></p></body></html>", None))
        self.label_telefone.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Telefone</span></p></body></html>", None))
        self.txt_telefone.setPlaceholderText("")
        self.label_confirmar_senha_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Cidade</span></p></body></html>", None))
        self.label_senha.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Senha</span></p></body></html>", None))
        self.label_estado.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Estado</span></p></body></html>", None))
        self.perfil_estado.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.perfil_estado.setItemText(1, QCoreApplication.translate("MainWindow", u"AC", None))
        self.perfil_estado.setItemText(2, QCoreApplication.translate("MainWindow", u"AL", None))
        self.perfil_estado.setItemText(3, QCoreApplication.translate("MainWindow", u"AP", None))
        self.perfil_estado.setItemText(4, QCoreApplication.translate("MainWindow", u"AM", None))
        self.perfil_estado.setItemText(5, QCoreApplication.translate("MainWindow", u"BA", None))
        self.perfil_estado.setItemText(6, QCoreApplication.translate("MainWindow", u"CE", None))
        self.perfil_estado.setItemText(7, QCoreApplication.translate("MainWindow", u"DF", None))
        self.perfil_estado.setItemText(8, QCoreApplication.translate("MainWindow", u"ES", None))
        self.perfil_estado.setItemText(9, QCoreApplication.translate("MainWindow", u"GO", None))
        self.perfil_estado.setItemText(10, QCoreApplication.translate("MainWindow", u"MA", None))
        self.perfil_estado.setItemText(11, QCoreApplication.translate("MainWindow", u"MT", None))
        self.perfil_estado.setItemText(12, QCoreApplication.translate("MainWindow", u"MS", None))
        self.perfil_estado.setItemText(13, QCoreApplication.translate("MainWindow", u"MG", None))
        self.perfil_estado.setItemText(14, QCoreApplication.translate("MainWindow", u"PA", None))
        self.perfil_estado.setItemText(15, QCoreApplication.translate("MainWindow", u"PB", None))
        self.perfil_estado.setItemText(16, QCoreApplication.translate("MainWindow", u"PR", None))
        self.perfil_estado.setItemText(17, QCoreApplication.translate("MainWindow", u"PE", None))
        self.perfil_estado.setItemText(18, QCoreApplication.translate("MainWindow", u"PI", None))
        self.perfil_estado.setItemText(19, QCoreApplication.translate("MainWindow", u"RJ", None))
        self.perfil_estado.setItemText(20, QCoreApplication.translate("MainWindow", u"RN", None))
        self.perfil_estado.setItemText(21, QCoreApplication.translate("MainWindow", u"RS", None))
        self.perfil_estado.setItemText(22, QCoreApplication.translate("MainWindow", u"RO", None))
        self.perfil_estado.setItemText(23, QCoreApplication.translate("MainWindow", u"RR", None))
        self.perfil_estado.setItemText(24, QCoreApplication.translate("MainWindow", u"SC", None))
        self.perfil_estado.setItemText(25, QCoreApplication.translate("MainWindow", u"SP", None))
        self.perfil_estado.setItemText(26, QCoreApplication.translate("MainWindow", u"SE", None))
        self.perfil_estado.setItemText(27, QCoreApplication.translate("MainWindow", u"TO", None))

        self.label_confirmar_senha.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Confirmar Senha</span></p></body></html>", None))
        self.btn_editar_cadastro.setText(QCoreApplication.translate("MainWindow", u"EDITAR", None))
        self.btn_sair_modo_edicao.setText(QCoreApplication.translate("MainWindow", u"SAIR DO MODO EDI\u00c7\u00c3O", None))
        self.btn_atualizar_cadastro.setText(QCoreApplication.translate("MainWindow", u"ATUALIZAR", None))
        self.btn_apagar_cadastro.setText(QCoreApplication.translate("MainWindow", u"APAGAR", None))
        self.btn_carregar_imagem_4.setText(QCoreApplication.translate("MainWindow", u"CARREGAR IMAGEM", None))
        self.btn_remover_imagem_usuario.setText(QCoreApplication.translate("MainWindow", u"REMOVER IMAGEM", None))
        self.btn_fazer_cadastro.setText(QCoreApplication.translate("MainWindow", u"FAZER CADASTRO", None))
        self.btn_ver_usuario.setText(QCoreApplication.translate("MainWindow", u"VER USU\u00c1RIO", None))
        self.btn_adicionar_cliente_juridico.setText(QCoreApplication.translate("MainWindow", u"Criar cliente", None))
        self.btn_editar_clientes.setText(QCoreApplication.translate("MainWindow", u"Editar cliente", None))
        self.btn_excluir_clientes.setText(QCoreApplication.translate("MainWindow", u"Excluir cliente", None))
        self.btn_gerar_relatorio_clientes.setText(QCoreApplication.translate("MainWindow", u"Gerar Relat\u00f3rio", None))
        self.btn_marcar_como_clientes.setText(QCoreApplication.translate("MainWindow", u"Marcar como", None))
        self.btn_historico_clientes.setText(QCoreApplication.translate("MainWindow", u"Hist\u00f3rico", None))
        self.line_clientes.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        ___qtablewidgetitem70 = self.table_clientes_juridicos.horizontalHeaderItem(0)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"Nome do Cliente", None));
        ___qtablewidgetitem71 = self.table_clientes_juridicos.horizontalHeaderItem(1)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"Raz\u00e3o Social", None));
        ___qtablewidgetitem72 = self.table_clientes_juridicos.horizontalHeaderItem(2)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"Data da Inclus\u00e3o", None));
        ___qtablewidgetitem73 = self.table_clientes_juridicos.horizontalHeaderItem(3)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"CNPJ", None));
        ___qtablewidgetitem74 = self.table_clientes_juridicos.horizontalHeaderItem(4)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"RG", None));
        ___qtablewidgetitem75 = self.table_clientes_juridicos.horizontalHeaderItem(5)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"CPF", None));
        ___qtablewidgetitem76 = self.table_clientes_juridicos.horizontalHeaderItem(6)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"Telefone", None));
        ___qtablewidgetitem77 = self.table_clientes_juridicos.horizontalHeaderItem(7)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"CEP", None));
        ___qtablewidgetitem78 = self.table_clientes_juridicos.horizontalHeaderItem(8)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None));
        ___qtablewidgetitem79 = self.table_clientes_juridicos.horizontalHeaderItem(9)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MainWindow", u"N\u00famero", None));
        ___qtablewidgetitem80 = self.table_clientes_juridicos.horizontalHeaderItem(10)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MainWindow", u"Complemento", None));
        ___qtablewidgetitem81 = self.table_clientes_juridicos.horizontalHeaderItem(11)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MainWindow", u"Cidade", None));
        ___qtablewidgetitem82 = self.table_clientes_juridicos.horizontalHeaderItem(12)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("MainWindow", u"Bairro", None));
        ___qtablewidgetitem83 = self.table_clientes_juridicos.horizontalHeaderItem(13)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("MainWindow", u"Estado", None));
        ___qtablewidgetitem84 = self.table_clientes_juridicos.horizontalHeaderItem(14)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("MainWindow", u"Status do Cliente", None));
        ___qtablewidgetitem85 = self.table_clientes_juridicos.horizontalHeaderItem(15)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("MainWindow", u"Categoria do Cliente", None));
        ___qtablewidgetitem86 = self.table_clientes_juridicos.horizontalHeaderItem(16)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("MainWindow", u"\u00daltima Atualiza\u00e7\u00e3o", None));
        ___qtablewidgetitem87 = self.table_clientes_juridicos.horizontalHeaderItem(17)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("MainWindow", u"Origem do Cliente", None));
        ___qtablewidgetitem88 = self.table_clientes_juridicos.horizontalHeaderItem(18)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("MainWindow", u"Valor Gasto Total", None));
        ___qtablewidgetitem89 = self.table_clientes_juridicos.horizontalHeaderItem(19)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("MainWindow", u"\u00daltima Compra", None));
        self.tab_clientes_todos.setTabText(self.tab_clientes_todos.indexOf(self.tab_clientes), QCoreApplication.translate("MainWindow", u"Base de Clientes Jurid\u00edcos", None))
        self.line_clientes_fisicos.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        self.btn_adicionar_cliente_fisico.setText(QCoreApplication.translate("MainWindow", u"Criar cliente", None))
        self.btn_editar_clientes_fisicos.setText(QCoreApplication.translate("MainWindow", u"Editar cliente", None))
        self.btn_excluir_clientes_fisicos.setText(QCoreApplication.translate("MainWindow", u"Excluir cliente", None))
        self.btn_gerar_relatorio_clientes_fisicos.setText(QCoreApplication.translate("MainWindow", u"Gerar Relat\u00f3rio", None))
        self.btn_marcar_como_clientes_fisicos.setText(QCoreApplication.translate("MainWindow", u"Marcar como", None))
        self.btn_historico_clientes_fisicos.setText(QCoreApplication.translate("MainWindow", u"Hist\u00f3rico", None))
        ___qtablewidgetitem90 = self.table_clientes_fisicos.horizontalHeaderItem(0)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("MainWindow", u"Nome do Cliente", None));
        ___qtablewidgetitem91 = self.table_clientes_fisicos.horizontalHeaderItem(1)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("MainWindow", u"Data da Inclus\u00e3o", None));
        ___qtablewidgetitem92 = self.table_clientes_fisicos.horizontalHeaderItem(2)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("MainWindow", u"CPF", None));
        ___qtablewidgetitem93 = self.table_clientes_fisicos.horizontalHeaderItem(3)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("MainWindow", u"RG", None));
        ___qtablewidgetitem94 = self.table_clientes_fisicos.horizontalHeaderItem(4)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("MainWindow", u"Telefone", None));
        ___qtablewidgetitem95 = self.table_clientes_fisicos.horizontalHeaderItem(5)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("MainWindow", u"CEP", None));
        ___qtablewidgetitem96 = self.table_clientes_fisicos.horizontalHeaderItem(6)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None));
        ___qtablewidgetitem97 = self.table_clientes_fisicos.horizontalHeaderItem(7)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("MainWindow", u"N\u00famero", None));
        ___qtablewidgetitem98 = self.table_clientes_fisicos.horizontalHeaderItem(8)
        ___qtablewidgetitem98.setText(QCoreApplication.translate("MainWindow", u"Complemento", None));
        ___qtablewidgetitem99 = self.table_clientes_fisicos.horizontalHeaderItem(9)
        ___qtablewidgetitem99.setText(QCoreApplication.translate("MainWindow", u"Cidade", None));
        ___qtablewidgetitem100 = self.table_clientes_fisicos.horizontalHeaderItem(10)
        ___qtablewidgetitem100.setText(QCoreApplication.translate("MainWindow", u"Bairro", None));
        ___qtablewidgetitem101 = self.table_clientes_fisicos.horizontalHeaderItem(11)
        ___qtablewidgetitem101.setText(QCoreApplication.translate("MainWindow", u"Estado", None));
        ___qtablewidgetitem102 = self.table_clientes_fisicos.horizontalHeaderItem(12)
        ___qtablewidgetitem102.setText(QCoreApplication.translate("MainWindow", u"Status do Cliente", None));
        ___qtablewidgetitem103 = self.table_clientes_fisicos.horizontalHeaderItem(13)
        ___qtablewidgetitem103.setText(QCoreApplication.translate("MainWindow", u"Categoria do Cliente", None));
        ___qtablewidgetitem104 = self.table_clientes_fisicos.horizontalHeaderItem(14)
        ___qtablewidgetitem104.setText(QCoreApplication.translate("MainWindow", u"\u00daltima Atualiza\u00e7\u00e3o", None));
        ___qtablewidgetitem105 = self.table_clientes_fisicos.horizontalHeaderItem(15)
        ___qtablewidgetitem105.setText(QCoreApplication.translate("MainWindow", u"Origem do Cliente", None));
        ___qtablewidgetitem106 = self.table_clientes_fisicos.horizontalHeaderItem(16)
        ___qtablewidgetitem106.setText(QCoreApplication.translate("MainWindow", u"Valor Gasto Total", None));
        ___qtablewidgetitem107 = self.table_clientes_fisicos.horizontalHeaderItem(17)
        ___qtablewidgetitem107.setText(QCoreApplication.translate("MainWindow", u"\u00daltima Compra", None));
        self.tab_clientes_todos.setTabText(self.tab_clientes_todos.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Base de Clientes F\u00edsicos", None))
        self.label_configuracoes.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; font-style:italic;\">CONFIGURA\u00c7\u00d5ES</span></p></body></html>", None))
        self.tool_tema.setText(QCoreApplication.translate("MainWindow", u"Tema do Sistema", None))
        self.tool_atalhos.setText(QCoreApplication.translate("MainWindow", u"Atalhos do teclado", None))
        self.tool_hora.setText(QCoreApplication.translate("MainWindow", u"Hora e idioma", None))
        self.tool_fonte.setText(QCoreApplication.translate("MainWindow", u"Tamanho da fonte", None))
        self.tool_atualizacoes.setText(QCoreApplication.translate("MainWindow", u"Atualiza\u00e7\u00f5es", None))
        self.tool_notificacoes.setText(QCoreApplication.translate("MainWindow", u"Notifica\u00e7\u00f5es", None))
        self.label_desenvolvido.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; font-style:italic;\">Desenvolvido e publicado por:</span></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; font-style:italic;\">Keven Lucas</span></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; font-style:italic;\">(19) 98201-8869</span></p></body></html>", None))
        self.btn_fazer_cadastro_massa_produtos.setText(QCoreApplication.translate("MainWindow", u"Fazer o cadastro em massa", None))
        self.btn_abrir_planilha_massa_produtos.setText(QCoreApplication.translate("MainWindow", u"Abrir planilha", None))
        self.btn_editar_massa_produtos.setText(QCoreApplication.translate("MainWindow", u"Editar produto", None))
        ___qtablewidgetitem108 = self.table_massa_produtos.horizontalHeaderItem(0)
        ___qtablewidgetitem108.setText(QCoreApplication.translate("MainWindow", u"Produto", None));
        ___qtablewidgetitem109 = self.table_massa_produtos.horizontalHeaderItem(1)
        ___qtablewidgetitem109.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtablewidgetitem110 = self.table_massa_produtos.horizontalHeaderItem(2)
        ___qtablewidgetitem110.setText(QCoreApplication.translate("MainWindow", u"Valor do Produto", None));
        ___qtablewidgetitem111 = self.table_massa_produtos.horizontalHeaderItem(3)
        ___qtablewidgetitem111.setText(QCoreApplication.translate("MainWindow", u"Desconto", None));
        ___qtablewidgetitem112 = self.table_massa_produtos.horizontalHeaderItem(4)
        ___qtablewidgetitem112.setText(QCoreApplication.translate("MainWindow", u"Valor Total", None));
        ___qtablewidgetitem113 = self.table_massa_produtos.horizontalHeaderItem(5)
        ___qtablewidgetitem113.setText(QCoreApplication.translate("MainWindow", u"Data do Cadastro", None));
        ___qtablewidgetitem114 = self.table_massa_produtos.horizontalHeaderItem(6)
        ___qtablewidgetitem114.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo do Item", None));
        ___qtablewidgetitem115 = self.table_massa_produtos.horizontalHeaderItem(7)
        ___qtablewidgetitem115.setText(QCoreApplication.translate("MainWindow", u"Cliente", None));
        ___qtablewidgetitem116 = self.table_massa_produtos.horizontalHeaderItem(8)
        ___qtablewidgetitem116.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o do Produto", None));
        self.btn_abrir_planilha_massa_usuarios.setText(QCoreApplication.translate("MainWindow", u"Abrir planilha", None))
        self.btn_editar_massa_usuario.setText(QCoreApplication.translate("MainWindow", u"Editar usu\u00e1rio", None))
        self.btn_fazer_cadastro_massa_usuarios.setText(QCoreApplication.translate("MainWindow", u"Fazer o cadastro em massa", None))
        ___qtablewidgetitem117 = self.table_massa_usuarios.horizontalHeaderItem(0)
        ___qtablewidgetitem117.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem118 = self.table_massa_usuarios.horizontalHeaderItem(1)
        ___qtablewidgetitem118.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None));
        ___qtablewidgetitem119 = self.table_massa_usuarios.horizontalHeaderItem(2)
        ___qtablewidgetitem119.setText(QCoreApplication.translate("MainWindow", u"Senha", None));
        ___qtablewidgetitem120 = self.table_massa_usuarios.horizontalHeaderItem(3)
        ___qtablewidgetitem120.setText(QCoreApplication.translate("MainWindow", u"Confirmar Senha", None));
        ___qtablewidgetitem121 = self.table_massa_usuarios.horizontalHeaderItem(4)
        ___qtablewidgetitem121.setText(QCoreApplication.translate("MainWindow", u"CEP", None));
        ___qtablewidgetitem122 = self.table_massa_usuarios.horizontalHeaderItem(5)
        ___qtablewidgetitem122.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None));
        ___qtablewidgetitem123 = self.table_massa_usuarios.horizontalHeaderItem(6)
        ___qtablewidgetitem123.setText(QCoreApplication.translate("MainWindow", u"N\u00famero", None));
        ___qtablewidgetitem124 = self.table_massa_usuarios.horizontalHeaderItem(7)
        ___qtablewidgetitem124.setText(QCoreApplication.translate("MainWindow", u"Cidade", None));
        ___qtablewidgetitem125 = self.table_massa_usuarios.horizontalHeaderItem(8)
        ___qtablewidgetitem125.setText(QCoreApplication.translate("MainWindow", u"Bairro", None));
        ___qtablewidgetitem126 = self.table_massa_usuarios.horizontalHeaderItem(9)
        ___qtablewidgetitem126.setText(QCoreApplication.translate("MainWindow", u"Estado", None));
        ___qtablewidgetitem127 = self.table_massa_usuarios.horizontalHeaderItem(10)
        ___qtablewidgetitem127.setText(QCoreApplication.translate("MainWindow", u"Complemento", None));
        ___qtablewidgetitem128 = self.table_massa_usuarios.horizontalHeaderItem(11)
        ___qtablewidgetitem128.setText(QCoreApplication.translate("MainWindow", u"Telefone", None));
        ___qtablewidgetitem129 = self.table_massa_usuarios.horizontalHeaderItem(12)
        ___qtablewidgetitem129.setText(QCoreApplication.translate("MainWindow", u"E-mail", None));
        ___qtablewidgetitem130 = self.table_massa_usuarios.horizontalHeaderItem(13)
        ___qtablewidgetitem130.setText(QCoreApplication.translate("MainWindow", u"Data de Nascimento", None));
        ___qtablewidgetitem131 = self.table_massa_usuarios.horizontalHeaderItem(14)
        ___qtablewidgetitem131.setText(QCoreApplication.translate("MainWindow", u"RG", None));
        ___qtablewidgetitem132 = self.table_massa_usuarios.horizontalHeaderItem(15)
        ___qtablewidgetitem132.setText(QCoreApplication.translate("MainWindow", u"CPF", None));
        ___qtablewidgetitem133 = self.table_massa_usuarios.horizontalHeaderItem(16)
        ___qtablewidgetitem133.setText(QCoreApplication.translate("MainWindow", u"CNPJ", None));
        ___qtablewidgetitem134 = self.table_massa_usuarios.horizontalHeaderItem(17)
        ___qtablewidgetitem134.setText(QCoreApplication.translate("MainWindow", u"Acesso", None));
    # retranslateUi

