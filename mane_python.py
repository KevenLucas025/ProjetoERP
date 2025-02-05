# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maine4.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QDateTimeEdit, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QToolButton,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1686, 963)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 80, 121);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_botoes_navegacoes = QFrame(self.centralwidget)
        self.frame_botoes_navegacoes.setObjectName(u"frame_botoes_navegacoes")
        self.frame_botoes_navegacoes.setStyleSheet(u"background-color: rgb(0, 80, 121);")
        self.frame_botoes_navegacoes.setFrameShape(QFrame.StyledPanel)
        self.frame_botoes_navegacoes.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_botoes_navegacoes)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_home = QPushButton(self.frame_botoes_navegacoes)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy1)
#if QT_CONFIG(tooltip)
        self.btn_home.setToolTip(u"P\u00e1gina principal")
#endif // QT_CONFIG(tooltip)
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
"}\n"
"")

        self.verticalLayout.addWidget(self.btn_home)

        self.btn_verificar_estoque = QPushButton(self.frame_botoes_navegacoes)
        self.btn_verificar_estoque.setObjectName(u"btn_verificar_estoque")
#if QT_CONFIG(tooltip)
        self.btn_verificar_estoque.setToolTip(u"Verifica o estoque dos produtos")
#endif // QT_CONFIG(tooltip)
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
"}\n"
"")

        self.verticalLayout.addWidget(self.btn_verificar_estoque)

        self.btn_verificar_usuarios = QPushButton(self.frame_botoes_navegacoes)
        self.btn_verificar_usuarios.setObjectName(u"btn_verificar_usuarios")
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
"}\n"
"")

        self.verticalLayout.addWidget(self.btn_verificar_usuarios)

        self.btn_cadastrar_produto = QPushButton(self.frame_botoes_navegacoes)
        self.btn_cadastrar_produto.setObjectName(u"btn_cadastrar_produto")
#if QT_CONFIG(tooltip)
        self.btn_cadastrar_produto.setToolTip(u"Cadastra produtos")
#endif // QT_CONFIG(tooltip)
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
"}\n"
"")

        self.verticalLayout.addWidget(self.btn_cadastrar_produto)

        self.btn_cadastro_usuario = QPushButton(self.frame_botoes_navegacoes)
        self.btn_cadastro_usuario.setObjectName(u"btn_cadastro_usuario")
#if QT_CONFIG(tooltip)
        self.btn_cadastro_usuario.setToolTip(u"<html><head/><body><p>Cadastra um usu\u00e1rio</p></body></html>")
#endif // QT_CONFIG(tooltip)
        self.btn_cadastro_usuario.setToolTipDuration(-1)
        self.btn_cadastro_usuario.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout.addWidget(self.btn_cadastro_usuario)

        self.btn_clientes = QPushButton(self.frame_botoes_navegacoes)
        self.btn_clientes.setObjectName(u"btn_clientes")
#if QT_CONFIG(tooltip)
        self.btn_clientes.setToolTip(u"Exibe os clientes")
#endif // QT_CONFIG(tooltip)
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
"}\n"
"")

        self.verticalLayout.addWidget(self.btn_clientes)

        self.btn_configuracoes = QPushButton(self.frame_botoes_navegacoes)
        self.btn_configuracoes.setObjectName(u"btn_configuracoes")
#if QT_CONFIG(tooltip)
        self.btn_configuracoes.setToolTip(u"Exibe as configura\u00e7\u00f5es do sistema")
#endif // QT_CONFIG(tooltip)
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
"}\n"
"")

        self.verticalLayout.addWidget(self.btn_configuracoes)


        self.gridLayout.addWidget(self.frame_botoes_navegacoes, 0, 0, 1, 1)

        self.paginas_sistemas = QStackedWidget(self.centralwidget)
        self.paginas_sistemas.setObjectName(u"paginas_sistemas")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.paginas_sistemas.sizePolicy().hasHeightForWidth())
        self.paginas_sistemas.setSizePolicy(sizePolicy2)
        self.paginas_sistemas.setStyleSheet(u"background-color: rgb(0, 80, 121);")
        self.home_pag = QWidget()
        self.home_pag.setObjectName(u"home_pag")
        sizePolicy2.setHeightForWidth(self.home_pag.sizePolicy().hasHeightForWidth())
        self.home_pag.setSizePolicy(sizePolicy2)
        self.verticalLayout_5 = QVBoxLayout(self.home_pag)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_5 = QFrame(self.home_pag)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy2.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy2)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(450, 360, 651, 391))
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.label_imagem_sistema = QLabel(self.frame_5)
        self.label_imagem_sistema.setObjectName(u"label_imagem_sistema")
        self.label_imagem_sistema.setGeometry(QRect(570, 20, 351, 321))
        sizePolicy2.setHeightForWidth(self.label_imagem_sistema.sizePolicy().hasHeightForWidth())
        self.label_imagem_sistema.setSizePolicy(sizePolicy2)
        self.label_imagem_sistema.setPixmap(QPixmap(u"Projeto ERP/Projeto ERP/Downloads/sistema-de-gerenciamento-de-conteudo.png"))
        self.label_imagem_sistema.setScaledContents(True)
        self.label_bem_vindo = QLabel(self.frame_5)
        self.label_bem_vindo.setObjectName(u"label_bem_vindo")
        self.label_bem_vindo.setGeometry(QRect(610, 400, 331, 71))
        sizePolicy2.setHeightForWidth(self.label_bem_vindo.sizePolicy().hasHeightForWidth())
        self.label_bem_vindo.setSizePolicy(sizePolicy2)
        self.label_bem_vindo.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.frame_5)

        self.paginas_sistemas.addWidget(self.home_pag)
        self.page_estoque = QWidget()
        self.page_estoque.setObjectName(u"page_estoque")
        sizePolicy2.setHeightForWidth(self.page_estoque.sizePolicy().hasHeightForWidth())
        self.page_estoque.setSizePolicy(sizePolicy2)
        self.horizontalLayout_7 = QHBoxLayout(self.page_estoque)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_page_estoque = QFrame(self.page_estoque)
        self.frame_page_estoque.setObjectName(u"frame_page_estoque")
        sizePolicy2.setHeightForWidth(self.frame_page_estoque.sizePolicy().hasHeightForWidth())
        self.frame_page_estoque.setSizePolicy(sizePolicy2)
        self.frame_page_estoque.setFrameShape(QFrame.StyledPanel)
        self.frame_page_estoque.setFrameShadow(QFrame.Raised)
        self.tb_base = QTabWidget(self.frame_page_estoque)
        self.tb_base.setObjectName(u"tb_base")
        self.tb_base.setGeometry(QRect(0, 5, 1321, 911))
        sizePolicy2.setHeightForWidth(self.tb_base.sizePolicy().hasHeightForWidth())
        self.tb_base.setSizePolicy(sizePolicy2)
        self.tb_base.setTabShape(QTabWidget.Triangular)
        self.tabela_base = QWidget()
        self.tabela_base.setObjectName(u"tabela_base")
        sizePolicy2.setHeightForWidth(self.tabela_base.sizePolicy().hasHeightForWidth())
        self.tabela_base.setSizePolicy(sizePolicy2)
        self.frame_table_estoque = QFrame(self.tabela_base)
        self.frame_table_estoque.setObjectName(u"frame_table_estoque")
        self.frame_table_estoque.setGeometry(QRect(9, 139, 1471, 311))
        self.frame_table_estoque.setFrameShape(QFrame.StyledPanel)
        self.frame_table_estoque.setFrameShadow(QFrame.Raised)
        self.table_base = QTableWidget(self.frame_table_estoque)
        if (self.table_base.columnCount() < 9):
            self.table_base.setColumnCount(9)
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
        self.table_base.setObjectName(u"table_base")
        self.table_base.setGeometry(QRect(0, 20, 1301, 291))
        self.frame_table_saida = QFrame(self.tabela_base)
        self.frame_table_saida.setObjectName(u"frame_table_saida")
        self.frame_table_saida.setGeometry(QRect(10, 550, 1451, 331))
        self.frame_table_saida.setFrameShape(QFrame.StyledPanel)
        self.frame_table_saida.setFrameShadow(QFrame.Raised)
        self.table_saida = QTableWidget(self.frame_table_saida)
        if (self.table_saida.columnCount() < 10):
            self.table_saida.setColumnCount(10)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_saida.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_saida.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_saida.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table_saida.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table_saida.setHorizontalHeaderItem(4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table_saida.setHorizontalHeaderItem(5, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table_saida.setHorizontalHeaderItem(6, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.table_saida.setHorizontalHeaderItem(7, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.table_saida.setHorizontalHeaderItem(8, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.table_saida.setHorizontalHeaderItem(9, __qtablewidgetitem18)
        self.table_saida.setObjectName(u"table_saida")
        self.table_saida.setGeometry(QRect(0, 50, 1301, 281))
        self.btn_salvar_tables = QPushButton(self.frame_table_saida)
        self.btn_salvar_tables.setObjectName(u"btn_salvar_tables")
        self.btn_salvar_tables.setGeometry(QRect(110, 10, 21, 23))
        icon = QIcon()
        icon.addFile(u"../../Downloads/disquete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_salvar_tables.setIcon(icon)
        self.btn_salvar_tables.setIconSize(QSize(16, 16))
        self.label_saida = QLabel(self.tabela_base)
        self.label_saida.setObjectName(u"label_saida")
        self.label_saida.setGeometry(QRect(10, 540, 101, 51))
        self.label_saida.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"	border: 3px solid white;\n"
"}\n"
"\n"
"")
        self.frame_do_meio = QFrame(self.tabela_base)
        self.frame_do_meio.setObjectName(u"frame_do_meio")
        self.frame_do_meio.setGeometry(QRect(10, 450, 1381, 91))
        self.frame_do_meio.setFrameShape(QFrame.StyledPanel)
        self.frame_do_meio.setFrameShadow(QFrame.Raised)
        self.btn_gerar_estorno = QPushButton(self.frame_do_meio)
        self.btn_gerar_estorno.setObjectName(u"btn_gerar_estorno")
        self.btn_gerar_estorno.setGeometry(QRect(30, 40, 161, 28))
        font = QFont()
        self.btn_gerar_estorno.setFont(font)
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
        self.btn_importar = QPushButton(self.frame_do_meio)
        self.btn_importar.setObjectName(u"btn_importar")
        self.btn_importar.setGeometry(QRect(500, 40, 161, 28))
        self.btn_importar.setFont(font)
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
        self.btn_gerar_saida = QPushButton(self.frame_do_meio)
        self.btn_gerar_saida.setObjectName(u"btn_gerar_saida")
        self.btn_gerar_saida.setGeometry(QRect(1020, 40, 161, 28))
        self.btn_gerar_saida.setFont(font)
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
        self.frame_botoes = QFrame(self.tabela_base)
        self.frame_botoes.setObjectName(u"frame_botoes")
        self.frame_botoes.setGeometry(QRect(-1, 10, 1321, 141))
        self.frame_botoes.setFrameShape(QFrame.StyledPanel)
        self.frame_botoes.setFrameShadow(QFrame.Raised)
        self.label_estoque = QLabel(self.frame_botoes)
        self.label_estoque.setObjectName(u"label_estoque")
        self.label_estoque.setGeometry(QRect(10, 100, 141, 41))
        self.label_estoque.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"	border: 3px solid white;\n"
"}\n"
"\n"
"")
        self.line_excel = QLineEdit(self.frame_botoes)
        self.line_excel.setObjectName(u"line_excel")
        self.line_excel.setGeometry(QRect(9, 0, 1304, 26))
        sizePolicy2.setHeightForWidth(self.line_excel.sizePolicy().hasHeightForWidth())
        self.line_excel.setSizePolicy(sizePolicy2)
        self.line_excel.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")
        self.line_excel.setAlignment(Qt.AlignCenter)
        self.line_excel.setReadOnly(False)
        self.line_excel.setPlaceholderText(u"Arquivo em excel aparecer\u00e1 aqui")
        self.progress_excel = QProgressBar(self.frame_botoes)
        self.progress_excel.setObjectName(u"progress_excel")
        self.progress_excel.setGeometry(QRect(10, 60, 1301, 23))
        sizePolicy2.setHeightForWidth(self.progress_excel.sizePolicy().hasHeightForWidth())
        self.progress_excel.setSizePolicy(sizePolicy2)
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
        self.btn_abrir_planilha = QPushButton(self.frame_botoes)
        self.btn_abrir_planilha.setObjectName(u"btn_abrir_planilha")
        self.btn_abrir_planilha.setGeometry(QRect(10, 30, 1301, 25))
        sizePolicy2.setHeightForWidth(self.btn_abrir_planilha.sizePolicy().hasHeightForWidth())
        self.btn_abrir_planilha.setSizePolicy(sizePolicy2)
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
        self.tb_base.addTab(self.tabela_base, "")
        self.btn_atualizar_estoque = QPushButton(self.frame_page_estoque)
        self.btn_atualizar_estoque.setObjectName(u"btn_atualizar_estoque")
        self.btn_atualizar_estoque.setGeometry(QRect(1327, 130, 161, 28))
        self.btn_atualizar_estoque.setFont(font)
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
        self.btn_historico = QPushButton(self.frame_page_estoque)
        self.btn_historico.setObjectName(u"btn_historico")
        self.btn_historico.setGeometry(QRect(1327, 170, 161, 28))
        self.btn_historico.setFont(font)
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
        self.btn_atualizar_saida = QPushButton(self.frame_page_estoque)
        self.btn_atualizar_saida.setObjectName(u"btn_atualizar_saida")
        self.btn_atualizar_saida.setGeometry(QRect(1327, 210, 161, 28))
        self.btn_atualizar_saida.setFont(font)
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
        self.btn_novo_produto = QPushButton(self.frame_page_estoque)
        self.btn_novo_produto.setObjectName(u"btn_novo_produto")
        self.btn_novo_produto.setGeometry(QRect(1327, 250, 161, 28))
        self.btn_novo_produto.setFont(font)
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
        self.btn_gerar_pdf = QPushButton(self.frame_page_estoque)
        self.btn_gerar_pdf.setObjectName(u"btn_gerar_pdf")
        self.btn_gerar_pdf.setGeometry(QRect(1328, 290, 161, 28))
        self.btn_gerar_pdf.setFont(font)
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
        self.btn_limpar_tabelas = QPushButton(self.frame_page_estoque)
        self.btn_limpar_tabelas.setObjectName(u"btn_limpar_tabelas")
        self.btn_limpar_tabelas.setGeometry(QRect(1330, 330, 161, 28))
        self.btn_limpar_tabelas.setFont(font)
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
        self.btn_incluir_no_sistema = QPushButton(self.frame_page_estoque)
        self.btn_incluir_no_sistema.setObjectName(u"btn_incluir_no_sistema")
        self.btn_incluir_no_sistema.setGeometry(QRect(1330, 370, 161, 28))
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_incluir_no_sistema.sizePolicy().hasHeightForWidth())
        self.btn_incluir_no_sistema.setSizePolicy(sizePolicy3)
        self.btn_incluir_no_sistema.setFont(font)
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

        self.horizontalLayout_7.addWidget(self.frame_page_estoque)

        self.paginas_sistemas.addWidget(self.page_estoque)
        self.page_verificar_usuarios = QWidget()
        self.page_verificar_usuarios.setObjectName(u"page_verificar_usuarios")
        self.frame = QFrame(self.page_verificar_usuarios)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-1, -1, 1521, 951))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(310, 460, 771, 71))
        self.label_9.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"	border: 3px solid white;\n"
"}\n"
"\n"
"")
        self.paginas_sistemas.addWidget(self.page_verificar_usuarios)
        self.pg_cadastrar_produto = QWidget()
        self.pg_cadastrar_produto.setObjectName(u"pg_cadastrar_produto")
        sizePolicy2.setHeightForWidth(self.pg_cadastrar_produto.sizePolicy().hasHeightForWidth())
        self.pg_cadastrar_produto.setSizePolicy(sizePolicy2)
        self.frame_2 = QFrame(self.pg_cadastrar_produto)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(-10, -110, 1631, 1081))
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setInputMethodHints(Qt.ImhNone)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_cadastramento_produtos = QLabel(self.frame_2)
        self.label_cadastramento_produtos.setObjectName(u"label_cadastramento_produtos")
        self.label_cadastramento_produtos.setGeometry(QRect(55, 160, 991, 61))
        sizePolicy2.setHeightForWidth(self.label_cadastramento_produtos.sizePolicy().hasHeightForWidth())
        self.label_cadastramento_produtos.setSizePolicy(sizePolicy2)
        self.label_cadastramento_produtos.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"	border: 5px solid white;\n"
"}\n"
"\n"
"")
        self.label_produto = QLabel(self.frame_2)
        self.label_produto.setObjectName(u"label_produto")
        self.label_produto.setGeometry(QRect(40, 271, 51, 16))
        sizePolicy2.setHeightForWidth(self.label_produto.sizePolicy().hasHeightForWidth())
        self.label_produto.setSizePolicy(sizePolicy2)
        self.label_produto.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.label_quantidade = QLabel(self.frame_2)
        self.label_quantidade.setObjectName(u"label_quantidade")
        self.label_quantidade.setGeometry(QRect(30, 340, 71, 16))
        sizePolicy2.setHeightForWidth(self.label_quantidade.sizePolicy().hasHeightForWidth())
        self.label_quantidade.setSizePolicy(sizePolicy2)
        self.label_quantidade.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.label_valor_produto = QLabel(self.frame_2)
        self.label_valor_produto.setObjectName(u"label_valor_produto")
        self.label_valor_produto.setGeometry(QRect(22, 406, 101, 20))
        sizePolicy2.setHeightForWidth(self.label_valor_produto.sizePolicy().hasHeightForWidth())
        self.label_valor_produto.setSizePolicy(sizePolicy2)
        self.label_valor_produto.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.label_desconto = QLabel(self.frame_2)
        self.label_desconto.setObjectName(u"label_desconto")
        self.label_desconto.setGeometry(QRect(35, 475, 61, 16))
        sizePolicy2.setHeightForWidth(self.label_desconto.sizePolicy().hasHeightForWidth())
        self.label_desconto.setSizePolicy(sizePolicy2)
        self.label_desconto.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.label_data_compra = QLabel(self.frame_2)
        self.label_data_compra.setObjectName(u"label_data_compra")
        self.label_data_compra.setGeometry(QRect(18, 536, 91, 20))
        sizePolicy2.setHeightForWidth(self.label_data_compra.sizePolicy().hasHeightForWidth())
        self.label_data_compra.setSizePolicy(sizePolicy2)
        self.label_data_compra.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.label_codigo_item = QLabel(self.frame_2)
        self.label_codigo_item.setObjectName(u"label_codigo_item")
        self.label_codigo_item.setGeometry(QRect(19, 585, 91, 20))
        sizePolicy2.setHeightForWidth(self.label_codigo_item.sizePolicy().hasHeightForWidth())
        self.label_codigo_item.setSizePolicy(sizePolicy2)
        self.label_codigo_item.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.label_cliente_2 = QLabel(self.frame_2)
        self.label_cliente_2.setObjectName(u"label_cliente_2")
        self.label_cliente_2.setGeometry(QRect(42, 643, 51, 16))
        sizePolicy2.setHeightForWidth(self.label_cliente_2.sizePolicy().hasHeightForWidth())
        self.label_cliente_2.setSizePolicy(sizePolicy2)
        self.label_cliente_2.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.label_descricao_produto = QLabel(self.frame_2)
        self.label_descricao_produto.setObjectName(u"label_descricao_produto")
        self.label_descricao_produto.setGeometry(QRect(10, 700, 131, 20))
        sizePolicy2.setHeightForWidth(self.label_descricao_produto.sizePolicy().hasHeightForWidth())
        self.label_descricao_produto.setSizePolicy(sizePolicy2)
        self.label_descricao_produto.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.txt_produto = QLineEdit(self.frame_2)
        self.txt_produto.setObjectName(u"txt_produto")
        self.txt_produto.setGeometry(QRect(140, 265, 171, 25))
        sizePolicy2.setHeightForWidth(self.txt_produto.sizePolicy().hasHeightForWidth())
        self.txt_produto.setSizePolicy(sizePolicy2)
        self.txt_produto.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")
        self.txt_quantidade = QLineEdit(self.frame_2)
        self.txt_quantidade.setObjectName(u"txt_quantidade")
        self.txt_quantidade.setGeometry(QRect(140, 335, 171, 25))
        sizePolicy2.setHeightForWidth(self.txt_quantidade.sizePolicy().hasHeightForWidth())
        self.txt_quantidade.setSizePolicy(sizePolicy2)
        self.txt_quantidade.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")
        self.txt_valor_produto = QLineEdit(self.frame_2)
        self.txt_valor_produto.setObjectName(u"txt_valor_produto")
        self.txt_valor_produto.setGeometry(QRect(140, 405, 171, 25))
        sizePolicy2.setHeightForWidth(self.txt_valor_produto.sizePolicy().hasHeightForWidth())
        self.txt_valor_produto.setSizePolicy(sizePolicy2)
        self.txt_valor_produto.setContextMenuPolicy(Qt.NoContextMenu)
        self.txt_valor_produto.setAutoFillBackground(False)
        self.txt_valor_produto.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")
        self.txt_valor_produto.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.txt_valor_produto.setClearButtonEnabled(False)
        self.txt_desconto = QLineEdit(self.frame_2)
        self.txt_desconto.setObjectName(u"txt_desconto")
        self.txt_desconto.setGeometry(QRect(140, 469, 171, 25))
        sizePolicy2.setHeightForWidth(self.txt_desconto.sizePolicy().hasHeightForWidth())
        self.txt_desconto.setSizePolicy(sizePolicy2)
        self.txt_desconto.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")
        self.txt_codigo_item = QLineEdit(self.frame_2)
        self.txt_codigo_item.setObjectName(u"txt_codigo_item")
        self.txt_codigo_item.setGeometry(QRect(140, 580, 171, 25))
        sizePolicy2.setHeightForWidth(self.txt_codigo_item.sizePolicy().hasHeightForWidth())
        self.txt_codigo_item.setSizePolicy(sizePolicy2)
        self.txt_codigo_item.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")
        self.txt_cliente = QLineEdit(self.frame_2)
        self.txt_cliente.setObjectName(u"txt_cliente")
        self.txt_cliente.setGeometry(QRect(140, 636, 171, 25))
        sizePolicy2.setHeightForWidth(self.txt_cliente.sizePolicy().hasHeightForWidth())
        self.txt_cliente.setSizePolicy(sizePolicy2)
        self.txt_cliente.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")
        self.txt_descricao_produto = QLineEdit(self.frame_2)
        self.txt_descricao_produto.setObjectName(u"txt_descricao_produto")
        self.txt_descricao_produto.setGeometry(QRect(140, 699, 171, 25))
        sizePolicy2.setHeightForWidth(self.txt_descricao_produto.sizePolicy().hasHeightForWidth())
        self.txt_descricao_produto.setSizePolicy(sizePolicy2)
        self.txt_descricao_produto.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")
        self.btn_adicionar_produto = QPushButton(self.frame_2)
        self.btn_adicionar_produto.setObjectName(u"btn_adicionar_produto")
        self.btn_adicionar_produto.setGeometry(QRect(400, 270, 141, 23))
        sizePolicy2.setHeightForWidth(self.btn_adicionar_produto.sizePolicy().hasHeightForWidth())
        self.btn_adicionar_produto.setSizePolicy(sizePolicy2)
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
        icon1.addFile(u"Projeto ERP/Projeto ERP/Downloads/pngwing.com.png", QSize(), QIcon.Active, QIcon.On)
        self.btn_adicionar_produto.setIcon(icon1)
        self.btn_atualizar_produto = QPushButton(self.frame_2)
        self.btn_atualizar_produto.setObjectName(u"btn_atualizar_produto")
        self.btn_atualizar_produto.setGeometry(QRect(400, 316, 141, 23))
        sizePolicy2.setHeightForWidth(self.btn_atualizar_produto.sizePolicy().hasHeightForWidth())
        self.btn_atualizar_produto.setSizePolicy(sizePolicy2)
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
        icon2.addFile(u"Projeto ERP/Projeto ERP/Downloads/toppng.com-update-512x512.png", QSize(), QIcon.Active, QIcon.On)
        self.btn_atualizar_produto.setIcon(icon2)
        self.btn_limpar_campos = QPushButton(self.frame_2)
        self.btn_limpar_campos.setObjectName(u"btn_limpar_campos")
        self.btn_limpar_campos.setGeometry(QRect(400, 409, 141, 23))
        sizePolicy2.setHeightForWidth(self.btn_limpar_campos.sizePolicy().hasHeightForWidth())
        self.btn_limpar_campos.setSizePolicy(sizePolicy2)
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
        icon3.addFile(u"Projeto ERP/Projeto ERP/Downloads/1486564399-close_81512.png", QSize(), QIcon.Active, QIcon.On)
        self.btn_limpar_campos.setIcon(icon3)
        self.btn_confirmar = QPushButton(self.frame_2)
        self.btn_confirmar.setObjectName(u"btn_confirmar")
        self.btn_confirmar.setGeometry(QRect(400, 600, 141, 23))
        sizePolicy2.setHeightForWidth(self.btn_confirmar.sizePolicy().hasHeightForWidth())
        self.btn_confirmar.setSizePolicy(sizePolicy2)
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
        self.btn_ver_item = QPushButton(self.frame_2)
        self.btn_ver_item.setObjectName(u"btn_ver_item")
        self.btn_ver_item.setGeometry(QRect(400, 660, 141, 31))
        sizePolicy2.setHeightForWidth(self.btn_ver_item.sizePolicy().hasHeightForWidth())
        self.btn_ver_item.setSizePolicy(sizePolicy2)
        self.btn_ver_item.setMinimumSize(QSize(141, 0))
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
        icon4.addFile(u"Projeto ERP/Projeto ERP/Downloads/pasta.png", QSize(), QIcon.Active, QIcon.On)
        self.btn_ver_item.setIcon(icon4)
        self.frame_valor_total_produtos = QFrame(self.frame_2)
        self.frame_valor_total_produtos.setObjectName(u"frame_valor_total_produtos")
        self.frame_valor_total_produtos.setGeometry(QRect(724, 260, 321, 101))
        sizePolicy2.setHeightForWidth(self.frame_valor_total_produtos.sizePolicy().hasHeightForWidth())
        self.frame_valor_total_produtos.setSizePolicy(sizePolicy2)
        self.frame_valor_total_produtos.setStyleSheet(u"background-color: rgb(100, 200, 100); /* Verde claro */\n"
"")
        self.frame_valor_total_produtos.setFrameShape(QFrame.StyledPanel)
        self.frame_valor_total_produtos.setFrameShadow(QFrame.Raised)
        self.label_valor_total_produtos = QLabel(self.frame_valor_total_produtos)
        self.label_valor_total_produtos.setObjectName(u"label_valor_total_produtos")
        self.label_valor_total_produtos.setGeometry(QRect(19, 10, 281, 31))
        sizePolicy2.setHeightForWidth(self.label_valor_total_produtos.sizePolicy().hasHeightForWidth())
        self.label_valor_total_produtos.setSizePolicy(sizePolicy2)
        self.label_valor_total_produtos.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.frame_quantidade = QFrame(self.frame_2)
        self.frame_quantidade.setObjectName(u"frame_quantidade")
        self.frame_quantidade.setGeometry(QRect(724, 685, 321, 101))
        sizePolicy2.setHeightForWidth(self.frame_quantidade.sizePolicy().hasHeightForWidth())
        self.frame_quantidade.setSizePolicy(sizePolicy2)
        self.frame_quantidade.setStyleSheet(u"background-color: rgb(100, 200, 100); /* Verde claro */\n"
"")
        self.frame_quantidade.setFrameShape(QFrame.StyledPanel)
        self.frame_quantidade.setFrameShadow(QFrame.Raised)
        self.label_quantidade_2 = QLabel(self.frame_quantidade)
        self.label_quantidade_2.setObjectName(u"label_quantidade_2")
        self.label_quantidade_2.setGeometry(QRect(42, 10, 251, 31))
        sizePolicy2.setHeightForWidth(self.label_quantidade_2.sizePolicy().hasHeightForWidth())
        self.label_quantidade_2.setSizePolicy(sizePolicy2)
        self.label_quantidade_2.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.dateEdit = QDateEdit(self.frame_2)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(140, 528, 171, 25))
        sizePolicy2.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy2)
        self.dateEdit.setStyleSheet(u"QDateEdit {\n"
"    color: #333; /* Cor do texto */\n"
"    background-color: white; /* Cor de fundo */\n"
"}\n"
"")
        self.dateEdit.setInputMethodHints(Qt.ImhPreferNumbers)
        self.dateEdit.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.dateEdit.setAccelerated(False)
        self.dateEdit.setProperty("showGroupSeparator", False)
        self.dateEdit.setMinimumDate(QDate(1900, 9, 14))
        self.dateEdit.setCurrentSection(QDateTimeEdit.DaySection)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setCurrentSectionIndex(0)
        self.dateEdit.setTimeSpec(Qt.UTC)
        self.frame_valor_com_desconto1 = QFrame(self.frame_2)
        self.frame_valor_com_desconto1.setObjectName(u"frame_valor_com_desconto1")
        self.frame_valor_com_desconto1.setGeometry(QRect(724, 543, 321, 101))
        sizePolicy2.setHeightForWidth(self.frame_valor_com_desconto1.sizePolicy().hasHeightForWidth())
        self.frame_valor_com_desconto1.setSizePolicy(sizePolicy2)
        self.frame_valor_com_desconto1.setStyleSheet(u"background-color: rgb(100, 200, 100); /* Verde claro */\n"
"")
        self.frame_valor_com_desconto1.setFrameShape(QFrame.StyledPanel)
        self.frame_valor_com_desconto1.setFrameShadow(QFrame.Raised)
        self.label_valor_com_desconto1 = QLabel(self.frame_valor_com_desconto1)
        self.label_valor_com_desconto1.setObjectName(u"label_valor_com_desconto1")
        self.label_valor_com_desconto1.setGeometry(QRect(20, 10, 281, 32))
        sizePolicy2.setHeightForWidth(self.label_valor_com_desconto1.sizePolicy().hasHeightForWidth())
        self.label_valor_com_desconto1.setSizePolicy(sizePolicy2)
        self.label_valor_com_desconto1.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.btn_carregar_imagem = QPushButton(self.frame_2)
        self.btn_carregar_imagem.setObjectName(u"btn_carregar_imagem")
        self.btn_carregar_imagem.setGeometry(QRect(390, 550, 161, 23))
        sizePolicy2.setHeightForWidth(self.btn_carregar_imagem.sizePolicy().hasHeightForWidth())
        self.btn_carregar_imagem.setSizePolicy(sizePolicy2)
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
        self.frame_imagem_produto = QFrame(self.frame_2)
        self.frame_imagem_produto.setObjectName(u"frame_imagem_produto")
        self.frame_imagem_produto.setGeometry(QRect(1159, 270, 321, 331))
        sizePolicy2.setHeightForWidth(self.frame_imagem_produto.sizePolicy().hasHeightForWidth())
        self.frame_imagem_produto.setSizePolicy(sizePolicy2)
        self.frame_imagem_produto.setFrameShape(QFrame.StyledPanel)
        self.frame_imagem_produto.setFrameShadow(QFrame.Raised)
        self.frame_valor_do_desconto = QFrame(self.frame_2)
        self.frame_valor_do_desconto.setObjectName(u"frame_valor_do_desconto")
        self.frame_valor_do_desconto.setGeometry(QRect(724, 400, 321, 101))
        sizePolicy2.setHeightForWidth(self.frame_valor_do_desconto.sizePolicy().hasHeightForWidth())
        self.frame_valor_do_desconto.setSizePolicy(sizePolicy2)
        self.frame_valor_do_desconto.setStyleSheet(u"\n"
"background-color: rgb(100, 200, 100); /* Verde claro */\n"
"")
        self.frame_valor_do_desconto.setFrameShape(QFrame.StyledPanel)
        self.frame_valor_do_desconto.setFrameShadow(QFrame.Raised)
        self.label_valor_do_desconto = QLabel(self.frame_valor_do_desconto)
        self.label_valor_do_desconto.setObjectName(u"label_valor_do_desconto")
        self.label_valor_do_desconto.setGeometry(QRect(80, 8, 171, 41))
        sizePolicy2.setHeightForWidth(self.label_valor_do_desconto.sizePolicy().hasHeightForWidth())
        self.label_valor_do_desconto.setSizePolicy(sizePolicy2)
        self.label_valor_do_desconto.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.btn_editar = QPushButton(self.frame_2)
        self.btn_editar.setObjectName(u"btn_editar")
        self.btn_editar.setGeometry(QRect(400, 361, 141, 23))
        sizePolicy2.setHeightForWidth(self.btn_editar.sizePolicy().hasHeightForWidth())
        self.btn_editar.setSizePolicy(sizePolicy2)
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
        self.btn_remover_imagem = QPushButton(self.frame_2)
        self.btn_remover_imagem.setObjectName(u"btn_remover_imagem")
        self.btn_remover_imagem.setGeometry(QRect(390, 520, 161, 23))
        sizePolicy2.setHeightForWidth(self.btn_remover_imagem.sizePolicy().hasHeightForWidth())
        self.btn_remover_imagem.setSizePolicy(sizePolicy2)
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
        self.frame_erro_produto = QFrame(self.frame_2)
        self.frame_erro_produto.setObjectName(u"frame_erro_produto")
        self.frame_erro_produto.setGeometry(QRect(320, 267, 21, 21))
        self.frame_erro_produto.setFrameShape(QFrame.StyledPanel)
        self.frame_erro_produto.setFrameShadow(QFrame.Raised)
        self.frame_erro_quantidade = QFrame(self.frame_2)
        self.frame_erro_quantidade.setObjectName(u"frame_erro_quantidade")
        self.frame_erro_quantidade.setGeometry(QRect(320, 337, 21, 21))
        self.frame_erro_quantidade.setFrameShape(QFrame.StyledPanel)
        self.frame_erro_quantidade.setFrameShadow(QFrame.Raised)
        self.frame_erro_valor_produto = QFrame(self.frame_2)
        self.frame_erro_valor_produto.setObjectName(u"frame_erro_valor_produto")
        self.frame_erro_valor_produto.setGeometry(QRect(320, 407, 21, 21))
        self.frame_erro_valor_produto.setFrameShape(QFrame.StyledPanel)
        self.frame_erro_valor_produto.setFrameShadow(QFrame.Raised)
        self.frame_erro_cliente = QFrame(self.frame_2)
        self.frame_erro_cliente.setObjectName(u"frame_erro_cliente")
        self.frame_erro_cliente.setGeometry(QRect(320, 639, 21, 21))
        self.frame_erro_cliente.setFrameShape(QFrame.StyledPanel)
        self.frame_erro_cliente.setFrameShadow(QFrame.Raised)
        self.frame_erro_descricao = QFrame(self.frame_2)
        self.frame_erro_descricao.setObjectName(u"frame_erro_descricao")
        self.frame_erro_descricao.setGeometry(QRect(320, 703, 21, 21))
        self.frame_erro_descricao.setFrameShape(QFrame.StyledPanel)
        self.frame_erro_descricao.setFrameShadow(QFrame.Raised)
        self.frame_erro_data_compra = QFrame(self.frame_2)
        self.frame_erro_data_compra.setObjectName(u"frame_erro_data_compra")
        self.frame_erro_data_compra.setGeometry(QRect(320, 530, 21, 21))
        self.frame_erro_data_compra.setFrameShape(QFrame.StyledPanel)
        self.frame_erro_data_compra.setFrameShadow(QFrame.Raised)
        self.paginas_sistemas.addWidget(self.pg_cadastrar_produto)
        self.pg_cliente = QWidget()
        self.pg_cliente.setObjectName(u"pg_cliente")
        sizePolicy2.setHeightForWidth(self.pg_cliente.sizePolicy().hasHeightForWidth())
        self.pg_cliente.setSizePolicy(sizePolicy2)
        self.frame_6 = QFrame(self.pg_cliente)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(-1, -1, 1651, 991))
        sizePolicy2.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy2)
        self.frame_6.setToolTipDuration(0)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(360, 110, 71, 41))
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
        self.label_7.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"	border: 5px solid white;\n"
"}\n"
"\n"
"")
        self.paginas_sistemas.addWidget(self.pg_cliente)
        self.pg_cadastro_usuario = QWidget()
        self.pg_cadastro_usuario.setObjectName(u"pg_cadastro_usuario")
        sizePolicy2.setHeightForWidth(self.pg_cadastro_usuario.sizePolicy().hasHeightForWidth())
        self.pg_cadastro_usuario.setSizePolicy(sizePolicy2)
        self.pg_cadastro_usuario.setStyleSheet(u"background-color: rgb(0, 80, 121);")
        self.verticalLayout_6 = QVBoxLayout(self.pg_cadastro_usuario)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_cadastro_usuario = QFrame(self.pg_cadastro_usuario)
        self.frame_cadastro_usuario.setObjectName(u"frame_cadastro_usuario")
        sizePolicy2.setHeightForWidth(self.frame_cadastro_usuario.sizePolicy().hasHeightForWidth())
        self.frame_cadastro_usuario.setSizePolicy(sizePolicy2)
        self.frame_cadastro_usuario.setFrameShape(QFrame.StyledPanel)
        self.frame_cadastro_usuario.setFrameShadow(QFrame.Raised)
        self.label_cadastramento = QLabel(self.frame_cadastro_usuario)
        self.label_cadastramento.setObjectName(u"label_cadastramento")
        self.label_cadastramento.setGeometry(QRect(530, 30, 391, 61))
        sizePolicy2.setHeightForWidth(self.label_cadastramento.sizePolicy().hasHeightForWidth())
        self.label_cadastramento.setSizePolicy(sizePolicy2)
        self.label_cadastramento.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"	border: 5px solid white;\n"
"}\n"
"\n"
"")
        self.label_nome = QLabel(self.frame_cadastro_usuario)
        self.label_nome.setObjectName(u"label_nome")
        self.label_nome.setGeometry(QRect(38, 194, 71, 21))
        sizePolicy2.setHeightForWidth(self.label_nome.sizePolicy().hasHeightForWidth())
        self.label_nome.setSizePolicy(sizePolicy2)
        self.label_nome.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.label_cpf = QLabel(self.frame_cadastro_usuario)
        self.label_cpf.setObjectName(u"label_cpf")
        self.label_cpf.setGeometry(QRect(45, 570, 41, 21))
        sizePolicy2.setHeightForWidth(self.label_cpf.sizePolicy().hasHeightForWidth())
        self.label_cpf.setSizePolicy(sizePolicy2)
        self.label_cpf.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.label_cep = QLabel(self.frame_cadastro_usuario)
        self.label_cep.setObjectName(u"label_cep")
        self.label_cep.setGeometry(QRect(45, 613, 41, 21))
        sizePolicy2.setHeightForWidth(self.label_cep.sizePolicy().hasHeightForWidth())
        self.label_cep.setSizePolicy(sizePolicy2)
        self.label_cep.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.label_estado = QLabel(self.frame_cadastro_usuario)
        self.label_estado.setObjectName(u"label_estado")
        self.label_estado.setGeometry(QRect(34, 652, 81, 31))
        sizePolicy2.setHeightForWidth(self.label_estado.sizePolicy().hasHeightForWidth())
        self.label_estado.setSizePolicy(sizePolicy2)
        self.label_estado.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.label_endereco = QLabel(self.frame_cadastro_usuario)
        self.label_endereco.setObjectName(u"label_endereco")
        self.label_endereco.setGeometry(QRect(36, 310, 111, 21))
        sizePolicy2.setHeightForWidth(self.label_endereco.sizePolicy().hasHeightForWidth())
        self.label_endereco.setSizePolicy(sizePolicy2)
        self.label_endereco.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.label_usuario = QLabel(self.frame_cadastro_usuario)
        self.label_usuario.setObjectName(u"label_usuario")
        self.label_usuario.setGeometry(QRect(35, 220, 91, 41))
        sizePolicy2.setHeightForWidth(self.label_usuario.sizePolicy().hasHeightForWidth())
        self.label_usuario.setSizePolicy(sizePolicy2)
        self.label_usuario.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.label_confirma_senha = QLabel(self.frame_cadastro_usuario)
        self.label_confirma_senha.setObjectName(u"label_confirma_senha")
        self.label_confirma_senha.setGeometry(QRect(10, 749, 161, 31))
        sizePolicy2.setHeightForWidth(self.label_confirma_senha.sizePolicy().hasHeightForWidth())
        self.label_confirma_senha.setSizePolicy(sizePolicy2)
        self.label_confirma_senha.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.label_senha = QLabel(self.frame_cadastro_usuario)
        self.label_senha.setObjectName(u"label_senha")
        self.label_senha.setGeometry(QRect(34, 699, 61, 31))
        sizePolicy2.setHeightForWidth(self.label_senha.sizePolicy().hasHeightForWidth())
        self.label_senha.setSizePolicy(sizePolicy2)
        self.label_senha.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.label_numero = QLabel(self.frame_cadastro_usuario)
        self.label_numero.setObjectName(u"label_numero")
        self.label_numero.setGeometry(QRect(38, 350, 91, 21))
        sizePolicy2.setHeightForWidth(self.label_numero.sizePolicy().hasHeightForWidth())
        self.label_numero.setSizePolicy(sizePolicy2)
        self.label_numero.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.label_email = QLabel(self.frame_cadastro_usuario)
        self.label_email.setObjectName(u"label_email")
        self.label_email.setGeometry(QRect(38, 440, 71, 31))
        sizePolicy2.setHeightForWidth(self.label_email.sizePolicy().hasHeightForWidth())
        self.label_email.setSizePolicy(sizePolicy2)
        self.label_email.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.label_perfil = QLabel(self.frame_cadastro_usuario)
        self.label_perfil.setObjectName(u"label_perfil")
        self.label_perfil.setGeometry(QRect(60, 810, 61, 21))
        sizePolicy2.setHeightForWidth(self.label_perfil.sizePolicy().hasHeightForWidth())
        self.label_perfil.setSizePolicy(sizePolicy2)
        self.label_perfil.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.label_telefone = QLabel(self.frame_cadastro_usuario)
        self.label_telefone.setObjectName(u"label_telefone")
        self.label_telefone.setGeometry(QRect(35, 270, 101, 20))
        sizePolicy2.setHeightForWidth(self.label_telefone.sizePolicy().hasHeightForWidth())
        self.label_telefone.setSizePolicy(sizePolicy2)
        self.label_telefone.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.label_rg = QLabel(self.frame_cadastro_usuario)
        self.label_rg.setObjectName(u"label_rg")
        self.label_rg.setGeometry(QRect(50, 526, 51, 31))
        sizePolicy2.setHeightForWidth(self.label_rg.sizePolicy().hasHeightForWidth())
        self.label_rg.setSizePolicy(sizePolicy2)
        self.label_rg.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.txt_nome = QLineEdit(self.frame_cadastro_usuario)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setGeometry(QRect(189, 190, 491, 29))
        sizePolicy2.setHeightForWidth(self.txt_nome.sizePolicy().hasHeightForWidth())
        self.txt_nome.setSizePolicy(sizePolicy2)
        self.txt_nome.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")
        self.txt_telefone = QLineEdit(self.frame_cadastro_usuario)
        self.txt_telefone.setObjectName(u"txt_telefone")
        self.txt_telefone.setGeometry(QRect(189, 270, 491, 29))
        sizePolicy2.setHeightForWidth(self.txt_telefone.sizePolicy().hasHeightForWidth())
        self.txt_telefone.setSizePolicy(sizePolicy2)
        self.txt_telefone.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")
        self.txt_usuario = QLineEdit(self.frame_cadastro_usuario)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setGeometry(QRect(189, 230, 491, 29))
        sizePolicy2.setHeightForWidth(self.txt_usuario.sizePolicy().hasHeightForWidth())
        self.txt_usuario.setSizePolicy(sizePolicy2)
        self.txt_usuario.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")
        self.txt_endereco = QLineEdit(self.frame_cadastro_usuario)
        self.txt_endereco.setObjectName(u"txt_endereco")
        self.txt_endereco.setGeometry(QRect(189, 310, 491, 29))
        sizePolicy2.setHeightForWidth(self.txt_endereco.sizePolicy().hasHeightForWidth())
        self.txt_endereco.setSizePolicy(sizePolicy2)
        self.txt_endereco.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")
        self.txt_numero = QLineEdit(self.frame_cadastro_usuario)
        self.txt_numero.setObjectName(u"txt_numero")
        self.txt_numero.setGeometry(QRect(189, 350, 491, 29))
        sizePolicy2.setHeightForWidth(self.txt_numero.sizePolicy().hasHeightForWidth())
        self.txt_numero.setSizePolicy(sizePolicy2)
        self.txt_numero.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")
        self.txt_rg = QLineEdit(self.frame_cadastro_usuario)
        self.txt_rg.setObjectName(u"txt_rg")
        self.txt_rg.setGeometry(QRect(189, 529, 491, 29))
        sizePolicy2.setHeightForWidth(self.txt_rg.sizePolicy().hasHeightForWidth())
        self.txt_rg.setSizePolicy(sizePolicy2)
        self.txt_rg.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")
        self.txt_email = QLineEdit(self.frame_cadastro_usuario)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setGeometry(QRect(189, 440, 491, 29))
        sizePolicy2.setHeightForWidth(self.txt_email.sizePolicy().hasHeightForWidth())
        self.txt_email.setSizePolicy(sizePolicy2)
        self.txt_email.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")
        self.txt_cpf = QLineEdit(self.frame_cadastro_usuario)
        self.txt_cpf.setObjectName(u"txt_cpf")
        self.txt_cpf.setGeometry(QRect(189, 566, 491, 29))
        sizePolicy2.setHeightForWidth(self.txt_cpf.sizePolicy().hasHeightForWidth())
        self.txt_cpf.setSizePolicy(sizePolicy2)
        self.txt_cpf.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")
        self.txt_cep = QLineEdit(self.frame_cadastro_usuario)
        self.txt_cep.setObjectName(u"txt_cep")
        self.txt_cep.setGeometry(QRect(189, 609, 491, 29))
        sizePolicy2.setHeightForWidth(self.txt_cep.sizePolicy().hasHeightForWidth())
        self.txt_cep.setSizePolicy(sizePolicy2)
        self.txt_cep.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")
        self.txt_confirmar_senha = QLineEdit(self.frame_cadastro_usuario)
        self.txt_confirmar_senha.setObjectName(u"txt_confirmar_senha")
        self.txt_confirmar_senha.setGeometry(QRect(190, 749, 491, 29))
        sizePolicy2.setHeightForWidth(self.txt_confirmar_senha.sizePolicy().hasHeightForWidth())
        self.txt_confirmar_senha.setSizePolicy(sizePolicy2)
        self.txt_confirmar_senha.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")
        self.txt_confirmar_senha.setEchoMode(QLineEdit.Password)
        self.txt_complemento = QLineEdit(self.frame_cadastro_usuario)
        self.txt_complemento.setObjectName(u"txt_complemento")
        self.txt_complemento.setGeometry(QRect(189, 395, 491, 29))
        sizePolicy2.setHeightForWidth(self.txt_complemento.sizePolicy().hasHeightForWidth())
        self.txt_complemento.setSizePolicy(sizePolicy2)
        self.txt_complemento.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")
        self.label_complemento = QLabel(self.frame_cadastro_usuario)
        self.label_complemento.setObjectName(u"label_complemento")
        self.label_complemento.setGeometry(QRect(10, 390, 141, 31))
        sizePolicy2.setHeightForWidth(self.label_complemento.sizePolicy().hasHeightForWidth())
        self.label_complemento.setSizePolicy(sizePolicy2)
        self.label_complemento.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.txt_senha = QLineEdit(self.frame_cadastro_usuario)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setGeometry(QRect(189, 700, 491, 29))
        sizePolicy2.setHeightForWidth(self.txt_senha.sizePolicy().hasHeightForWidth())
        self.txt_senha.setSizePolicy(sizePolicy2)
        self.txt_senha.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")
        self.txt_senha.setEchoMode(QLineEdit.Password)
        self.btn_fazer_cadastro = QPushButton(self.frame_cadastro_usuario)
        self.btn_fazer_cadastro.setObjectName(u"btn_fazer_cadastro")
        self.btn_fazer_cadastro.setGeometry(QRect(130, 840, 131, 25))
        sizePolicy2.setHeightForWidth(self.btn_fazer_cadastro.sizePolicy().hasHeightForWidth())
        self.btn_fazer_cadastro.setSizePolicy(sizePolicy2)
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
        self.perfil_usuarios = QComboBox(self.frame_cadastro_usuario)
        self.perfil_usuarios.addItem("")
        self.perfil_usuarios.addItem("")
        self.perfil_usuarios.addItem("")
        self.perfil_usuarios.setObjectName(u"perfil_usuarios")
        self.perfil_usuarios.setGeometry(QRect(190, 804, 491, 25))
        sizePolicy2.setHeightForWidth(self.perfil_usuarios.sizePolicy().hasHeightForWidth())
        self.perfil_usuarios.setSizePolicy(sizePolicy2)
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
        self.btn_carregar_imagem_2 = QPushButton(self.frame_cadastro_usuario)
        self.btn_carregar_imagem_2.setObjectName(u"btn_carregar_imagem_2")
        self.btn_carregar_imagem_2.setGeometry(QRect(550, 870, 151, 25))
        sizePolicy2.setHeightForWidth(self.btn_carregar_imagem_2.sizePolicy().hasHeightForWidth())
        self.btn_carregar_imagem_2.setSizePolicy(sizePolicy2)
        self.btn_carregar_imagem_2.setStyleSheet(u"QPushButton {\n"
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
        self.btn_atualizar_cadastro = QPushButton(self.frame_cadastro_usuario)
        self.btn_atualizar_cadastro.setObjectName(u"btn_atualizar_cadastro")
        self.btn_atualizar_cadastro.setGeometry(QRect(410, 840, 131, 25))
        sizePolicy2.setHeightForWidth(self.btn_atualizar_cadastro.sizePolicy().hasHeightForWidth())
        self.btn_atualizar_cadastro.setSizePolicy(sizePolicy2)
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
        self.btn_editar_cadastro = QPushButton(self.frame_cadastro_usuario)
        self.btn_editar_cadastro.setObjectName(u"btn_editar_cadastro")
        self.btn_editar_cadastro.setGeometry(QRect(270, 840, 131, 25))
        sizePolicy2.setHeightForWidth(self.btn_editar_cadastro.sizePolicy().hasHeightForWidth())
        self.btn_editar_cadastro.setSizePolicy(sizePolicy2)
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
        self.btn_apagar_cadastro = QPushButton(self.frame_cadastro_usuario)
        self.btn_apagar_cadastro.setObjectName(u"btn_apagar_cadastro")
        self.btn_apagar_cadastro.setGeometry(QRect(550, 840, 131, 25))
        sizePolicy2.setHeightForWidth(self.btn_apagar_cadastro.sizePolicy().hasHeightForWidth())
        self.btn_apagar_cadastro.setSizePolicy(sizePolicy2)
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
        self.txt_data_nascimento = QLineEdit(self.frame_cadastro_usuario)
        self.txt_data_nascimento.setObjectName(u"txt_data_nascimento")
        self.txt_data_nascimento.setGeometry(QRect(189, 490, 491, 29))
        sizePolicy2.setHeightForWidth(self.txt_data_nascimento.sizePolicy().hasHeightForWidth())
        self.txt_data_nascimento.setSizePolicy(sizePolicy2)
        self.txt_data_nascimento.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")
        self.label_data_nascimento = QLabel(self.frame_cadastro_usuario)
        self.label_data_nascimento.setObjectName(u"label_data_nascimento")
        self.label_data_nascimento.setGeometry(QRect(0, 492, 170, 31))
        sizePolicy2.setHeightForWidth(self.label_data_nascimento.sizePolicy().hasHeightForWidth())
        self.label_data_nascimento.setSizePolicy(sizePolicy2)
        self.label_data_nascimento.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.frame_imagem_cadastro = QFrame(self.frame_cadastro_usuario)
        self.frame_imagem_cadastro.setObjectName(u"frame_imagem_cadastro")
        self.frame_imagem_cadastro.setGeometry(QRect(793, 207, 611, 601))
        sizePolicy2.setHeightForWidth(self.frame_imagem_cadastro.sizePolicy().hasHeightForWidth())
        self.frame_imagem_cadastro.setSizePolicy(sizePolicy2)
        self.frame_imagem_cadastro.setFrameShape(QFrame.StyledPanel)
        self.frame_imagem_cadastro.setFrameShadow(QFrame.Raised)
        self.perfil_estado = QComboBox(self.frame_cadastro_usuario)
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
        self.perfil_estado.setGeometry(QRect(190, 660, 491, 25))
        sizePolicy2.setHeightForWidth(self.perfil_estado.sizePolicy().hasHeightForWidth())
        self.perfil_estado.setSizePolicy(sizePolicy2)
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

        self.verticalLayout_6.addWidget(self.frame_cadastro_usuario)

        self.paginas_sistemas.addWidget(self.pg_cadastro_usuario)
        self.pg_configuracoes = QWidget()
        self.pg_configuracoes.setObjectName(u"pg_configuracoes")
        sizePolicy2.setHeightForWidth(self.pg_configuracoes.sizePolicy().hasHeightForWidth())
        self.pg_configuracoes.setSizePolicy(sizePolicy2)
        self.frame_pg_configuracoes1 = QFrame(self.pg_configuracoes)
        self.frame_pg_configuracoes1.setObjectName(u"frame_pg_configuracoes1")
        self.frame_pg_configuracoes1.setGeometry(QRect(-1, -1, 1511, 981))
        sizePolicy2.setHeightForWidth(self.frame_pg_configuracoes1.sizePolicy().hasHeightForWidth())
        self.frame_pg_configuracoes1.setSizePolicy(sizePolicy2)
        self.frame_pg_configuracoes1.setInputMethodHints(Qt.ImhNone)
        self.frame_pg_configuracoes1.setFrameShape(QFrame.StyledPanel)
        self.frame_pg_configuracoes1.setFrameShadow(QFrame.Raised)
        self.label_8 = QLabel(self.frame_pg_configuracoes1)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(640, 70, 331, 81))
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)
        self.label_8.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"	border: 5px solid white;\n"
"}\n"
"\n"
"")
        self.frame_pg_configuracoes = QFrame(self.frame_pg_configuracoes1)
        self.frame_pg_configuracoes.setObjectName(u"frame_pg_configuracoes")
        self.frame_pg_configuracoes.setGeometry(QRect(0, 210, 1501, 711))
        sizePolicy2.setHeightForWidth(self.frame_pg_configuracoes.sizePolicy().hasHeightForWidth())
        self.frame_pg_configuracoes.setSizePolicy(sizePolicy2)
        self.frame_pg_configuracoes.setStyleSheet(u"QFrame {\n"
"    border: 2px solid white;\n"
"}\n"
"")
        self.frame_pg_configuracoes.setFrameShape(QFrame.StyledPanel)
        self.frame_pg_configuracoes.setFrameShadow(QFrame.Raised)
        self.tool_atualizacoes = QToolButton(self.frame_pg_configuracoes)
        self.tool_atualizacoes.setObjectName(u"tool_atualizacoes")
        self.tool_atualizacoes.setGeometry(QRect(40, 240, 151, 31))
        sizePolicy2.setHeightForWidth(self.tool_atualizacoes.sizePolicy().hasHeightForWidth())
        self.tool_atualizacoes.setSizePolicy(sizePolicy2)
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
"")
        self.tool_atualizacoes.setAutoRepeat(False)
        self.tool_atualizacoes.setPopupMode(QToolButton.MenuButtonPopup)
        self.tool_atualizacoes.setToolButtonStyle(Qt.ToolButtonTextOnly)
        self.tool_atualizacoes.setAutoRaise(False)
        self.tool_atualizacoes.setArrowType(Qt.DownArrow)
        self.tool_fonte = QToolButton(self.frame_pg_configuracoes)
        self.tool_fonte.setObjectName(u"tool_fonte")
        self.tool_fonte.setGeometry(QRect(40, 190, 151, 31))
        sizePolicy2.setHeightForWidth(self.tool_fonte.sizePolicy().hasHeightForWidth())
        self.tool_fonte.setSizePolicy(sizePolicy2)
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
"")
        self.tool_fonte.setAutoRepeat(False)
        self.tool_fonte.setPopupMode(QToolButton.MenuButtonPopup)
        self.tool_fonte.setToolButtonStyle(Qt.ToolButtonTextOnly)
        self.tool_fonte.setAutoRaise(False)
        self.tool_fonte.setArrowType(Qt.DownArrow)
        self.tool_hora = QToolButton(self.frame_pg_configuracoes)
        self.tool_hora.setObjectName(u"tool_hora")
        self.tool_hora.setGeometry(QRect(40, 140, 151, 31))
        sizePolicy2.setHeightForWidth(self.tool_hora.sizePolicy().hasHeightForWidth())
        self.tool_hora.setSizePolicy(sizePolicy2)
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
"")
        self.tool_hora.setAutoRepeat(False)
        self.tool_hora.setPopupMode(QToolButton.MenuButtonPopup)
        self.tool_hora.setToolButtonStyle(Qt.ToolButtonTextOnly)
        self.tool_hora.setAutoRaise(False)
        self.tool_hora.setArrowType(Qt.DownArrow)
        self.tool_atalhos = QToolButton(self.frame_pg_configuracoes)
        self.tool_atalhos.setObjectName(u"tool_atalhos")
        self.tool_atalhos.setGeometry(QRect(40, 90, 151, 31))
        sizePolicy2.setHeightForWidth(self.tool_atalhos.sizePolicy().hasHeightForWidth())
        self.tool_atalhos.setSizePolicy(sizePolicy2)
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
"")
        self.tool_atalhos.setAutoRepeat(False)
        self.tool_atalhos.setPopupMode(QToolButton.MenuButtonPopup)
        self.tool_atalhos.setToolButtonStyle(Qt.ToolButtonTextOnly)
        self.tool_atalhos.setAutoRaise(False)
        self.tool_atalhos.setArrowType(Qt.DownArrow)
        self.tool_tema = QToolButton(self.frame_pg_configuracoes)
        self.tool_tema.setObjectName(u"tool_tema")
        self.tool_tema.setGeometry(QRect(40, 40, 151, 31))
        sizePolicy2.setHeightForWidth(self.tool_tema.sizePolicy().hasHeightForWidth())
        self.tool_tema.setSizePolicy(sizePolicy2)
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
        self.tool_tema.setAutoRepeat(False)
        self.tool_tema.setPopupMode(QToolButton.MenuButtonPopup)
        self.tool_tema.setToolButtonStyle(Qt.ToolButtonTextOnly)
        self.tool_tema.setAutoRaise(False)
        self.tool_tema.setArrowType(Qt.DownArrow)
        self.paginas_sistemas.addWidget(self.pg_configuracoes)
        self.pg_contato = QWidget()
        self.pg_contato.setObjectName(u"pg_contato")
        sizePolicy2.setHeightForWidth(self.pg_contato.sizePolicy().hasHeightForWidth())
        self.pg_contato.setSizePolicy(sizePolicy2)
        self.frame_4 = QFrame(self.pg_contato)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(-240, -260, 1751, 1201))
        sizePolicy2.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy2)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(600, 360, 411, 101))
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"\n"
"}\n"
"\n"
"")
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(660, 480, 41, 31))
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setPixmap(QPixmap(u"Projeto ERP/Projeto ERP/Downloads/Whatsapp_37229.png"))
        self.label_3.setScaledContents(True)
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(710, 490, 151, 31))
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"\n"
"}\n"
"\n"
"")
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(660, 530, 41, 31))
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setPixmap(QPixmap(u"Projeto ERP/Projeto ERP/Downloads/linkedin_icon-icons.com_65929.png"))
        self.label_5.setScaledContents(True)
        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(710, 535, 251, 20))
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"\n"
"}\n"
"\n"
"")
        self.paginas_sistemas.addWidget(self.pg_contato)

        self.gridLayout.addWidget(self.paginas_sistemas, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.paginas_sistemas.setCurrentIndex(5)
        self.tb_base.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_verificar_estoque.setText(QCoreApplication.translate("MainWindow", u"Verificar Estoque", None))
#if QT_CONFIG(tooltip)
        self.btn_verificar_usuarios.setToolTip(QCoreApplication.translate("MainWindow", u"Verifica os usu\u00e1rios cadastrados", None))
#endif // QT_CONFIG(tooltip)
        self.btn_verificar_usuarios.setText(QCoreApplication.translate("MainWindow", u"Verificar Usu\u00e1rios", None))
        self.btn_cadastrar_produto.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Produto", None))
        self.btn_cadastro_usuario.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Usu\u00e1rio", None))
        self.btn_clientes.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.btn_configuracoes.setText(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; font-style:italic;\">Sistema de gerenciamento </span></p><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; font-style:italic;\">do controle de estoque</span></p></body></html>", None))
        self.label_imagem_sistema.setText("")
        self.label_bem_vindo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; font-style:italic; color:#ffffff;\">Bem vindo(a) ao</span></p></body></html>", None))
        ___qtablewidgetitem = self.table_base.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Produto", None));
        ___qtablewidgetitem1 = self.table_base.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtablewidgetitem2 = self.table_base.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Valor do Produto", None));
        ___qtablewidgetitem3 = self.table_base.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Desconto", None));
        ___qtablewidgetitem4 = self.table_base.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Data da Compra", None));
        ___qtablewidgetitem5 = self.table_base.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo do Item", None));
        ___qtablewidgetitem6 = self.table_base.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Cliente", None));
        ___qtablewidgetitem7 = self.table_base.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o do Produto", None));
        ___qtablewidgetitem8 = self.table_base.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None));
        ___qtablewidgetitem9 = self.table_saida.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Produto", None));
        ___qtablewidgetitem10 = self.table_saida.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtablewidgetitem11 = self.table_saida.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Valor do Produto", None));
        ___qtablewidgetitem12 = self.table_saida.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Desconto", None));
        ___qtablewidgetitem13 = self.table_saida.horizontalHeaderItem(4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Data de Sa\u00edda", None));
        ___qtablewidgetitem14 = self.table_saida.horizontalHeaderItem(5)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Data da Cria\u00e7\u00e3o ", None));
        ___qtablewidgetitem15 = self.table_saida.horizontalHeaderItem(6)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo do Produto", None));
        ___qtablewidgetitem16 = self.table_saida.horizontalHeaderItem(7)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Cliente", None));
        ___qtablewidgetitem17 = self.table_saida.horizontalHeaderItem(8)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o do Produto", None));
        ___qtablewidgetitem18 = self.table_saida.horizontalHeaderItem(9)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None));
        self.btn_salvar_tables.setText("")
        self.label_saida.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">SA\u00cdDA</span></p></body></html>", None))
        self.btn_gerar_estorno.setText(QCoreApplication.translate("MainWindow", u"Gerar Estorno", None))
        self.btn_importar.setText(QCoreApplication.translate("MainWindow", u"Importar", None))
        self.btn_gerar_saida.setText(QCoreApplication.translate("MainWindow", u"Gerar Sa\u00edda", None))
        self.label_estoque.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">ESTOQUE</span></p></body></html>", None))
        self.btn_abrir_planilha.setText(QCoreApplication.translate("MainWindow", u"Abrir Planilha", None))
        self.tb_base.setTabText(self.tb_base.indexOf(self.tabela_base), QCoreApplication.translate("MainWindow", u"Base", None))
        self.btn_atualizar_estoque.setText(QCoreApplication.translate("MainWindow", u"Atualizar estoque", None))
        self.btn_historico.setText(QCoreApplication.translate("MainWindow", u"Hist\u00f3rico", None))
        self.btn_atualizar_saida.setText(QCoreApplication.translate("MainWindow", u"Atualizar sa\u00edda", None))
        self.btn_novo_produto.setText(QCoreApplication.translate("MainWindow", u"Novo produto", None))
        self.btn_gerar_pdf.setText(QCoreApplication.translate("MainWindow", u"Gerar PDF", None))
        self.btn_limpar_tabelas.setText(QCoreApplication.translate("MainWindow", u"Limpar tabelas", None))
        self.btn_incluir_no_sistema.setText(QCoreApplication.translate("MainWindow", u"Incluir produto no sistema", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">ESSA P\u00c1GINA AINDA CONSTA EM PROCESSO DE DESENVOLVIMENTO</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.frame_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_cadastramento_produtos.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">Cadastramento de Produtos</span></p></body></html>", None))
        self.label_produto.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Produto</span></p></body></html>", None))
        self.label_quantidade.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Quantidade</span></p></body></html>", None))
        self.label_valor_produto.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Valor  do produto</span></p></body></html>", None))
        self.label_desconto.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Desconto</span></p></body></html>", None))
        self.label_data_compra.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Data da Compra</span></p><p><br/></p></body></html>", None))
        self.label_codigo_item.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">C\u00f3digo do Item</span></p></body></html>", None))
        self.label_cliente_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Cliente</span></p></body></html>", None))
        self.label_descricao_produto.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Descri\u00e7\u00e3o do produto</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.txt_valor_produto.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.txt_valor_produto.setText("")
        self.txt_valor_produto.setPlaceholderText("")
        self.txt_desconto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Opcional", None))
        self.txt_codigo_item.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Gerado automaticamente", None))
#if QT_CONFIG(tooltip)
        self.btn_adicionar_produto.setToolTip(QCoreApplication.translate("MainWindow", u"Realiza e exibe o c\u00e1lculo do produto", None))
#endif // QT_CONFIG(tooltip)
        self.btn_adicionar_produto.setText(QCoreApplication.translate("MainWindow", u"ADICIONAR", None))
#if QT_CONFIG(tooltip)
        self.btn_atualizar_produto.setToolTip(QCoreApplication.translate("MainWindow", u"Atualiza o produto no banco de dados", None))
#endif // QT_CONFIG(tooltip)
        self.btn_atualizar_produto.setText(QCoreApplication.translate("MainWindow", u"ATUALIZAR", None))
#if QT_CONFIG(tooltip)
        self.btn_limpar_campos.setToolTip(QCoreApplication.translate("MainWindow", u"Apaga as informa\u00e7\u00f5es preenchidas", None))
#endif // QT_CONFIG(tooltip)
        self.btn_limpar_campos.setText(QCoreApplication.translate("MainWindow", u"APAGAR", None))
#if QT_CONFIG(tooltip)
        self.btn_confirmar.setToolTip(QCoreApplication.translate("MainWindow", u"Cadastra o produto", None))
#endif // QT_CONFIG(tooltip)
        self.btn_confirmar.setText(QCoreApplication.translate("MainWindow", u"CONFIRMAR", None))
#if QT_CONFIG(tooltip)
        self.btn_ver_item.setToolTip(QCoreApplication.translate("MainWindow", u"Redireciona at\u00e9 o estoque dos produtos", None))
#endif // QT_CONFIG(tooltip)
        self.btn_ver_item.setText(QCoreApplication.translate("MainWindow", u"VER ITEM", None))
        self.label_valor_total_produtos.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Valor total de produtos sem desconto</span></p></body></html>", None))
        self.label_quantidade_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Quantidade total de produtos</span></p></body></html>", None))
        self.label_valor_com_desconto1.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Valor do produto com desconto</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.btn_carregar_imagem.setToolTip(QCoreApplication.translate("MainWindow", u"Carrega a imagem para cadastro do produto", None))
#endif // QT_CONFIG(tooltip)
        self.btn_carregar_imagem.setText(QCoreApplication.translate("MainWindow", u"CARREGAR IMAGEM", None))
        self.label_valor_do_desconto.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Valor do desconto</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.btn_editar.setToolTip(QCoreApplication.translate("MainWindow", u"Exibe a tabela de produtos para atualiza\u00e7\u00e3o", None))
#endif // QT_CONFIG(tooltip)
        self.btn_editar.setText(QCoreApplication.translate("MainWindow", u"EDITAR ", None))
#if QT_CONFIG(tooltip)
        self.btn_remover_imagem.setToolTip(QCoreApplication.translate("MainWindow", u"Remove a imagem do produto selecionado", None))
#endif // QT_CONFIG(tooltip)
        self.btn_remover_imagem.setText(QCoreApplication.translate("MainWindow", u"REMOVER IMAGEM", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"CLIENTE", None))
        self.label_cadastramento.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; font-style:italic;\">CADASTRAMENTO DE USU\u00c1RIO</span></p></body></html>", None))
        self.label_nome.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Nome</span></p></body></html>", None))
        self.label_cpf.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">CPF</span></p></body></html>", None))
        self.label_cep.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">CEP</span></p></body></html>", None))
        self.label_estado.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Estado</span></p></body></html>", None))
        self.label_endereco.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Endere\u00e7o</span></p></body></html>", None))
        self.label_usuario.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Usu\u00e1rio</span></p></body></html>", None))
        self.label_confirma_senha.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Confirmar senha</span></p></body></html>", None))
        self.label_senha.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Senha</span></p></body></html>", None))
        self.label_numero.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">N\u00famero</span></p></body></html>", None))
        self.label_email.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">E-mail</span></p></body></html>", None))
        self.label_perfil.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Perfil</span></p></body></html>", None))
        self.label_telefone.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Telefone</span></p></body></html>", None))
        self.label_rg.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">RG</span></p></body></html>", None))
        self.txt_complemento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Opcional", None))
        self.label_complemento.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Complemento</span></p></body></html>", None))
        self.btn_fazer_cadastro.setText(QCoreApplication.translate("MainWindow", u"Fazer cadastro", None))
        self.perfil_usuarios.setItemText(0, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.perfil_usuarios.setItemText(1, QCoreApplication.translate("MainWindow", u"Administrador", None))
        self.perfil_usuarios.setItemText(2, QCoreApplication.translate("MainWindow", u"Convidado", None))

        self.btn_carregar_imagem_2.setText(QCoreApplication.translate("MainWindow", u"Carregar imagem", None))
        self.btn_atualizar_cadastro.setText(QCoreApplication.translate("MainWindow", u"Atualizar", None))
        self.btn_editar_cadastro.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_apagar_cadastro.setText(QCoreApplication.translate("MainWindow", u"Apagar", None))
        self.label_data_nascimento.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Data de nascimento</span></p><p><br/></p></body></html>", None))
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

        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; font-style:italic;\">CONFIGURA\u00c7\u00d5ES</span></p></body></html>", None))
        self.tool_atualizacoes.setText(QCoreApplication.translate("MainWindow", u"Atualiza\u00e7\u00f5es autom\u00e1ticas", None))
        self.tool_fonte.setText(QCoreApplication.translate("MainWindow", u"Tamanho da fonte", None))
        self.tool_hora.setText(QCoreApplication.translate("MainWindow", u" Hora e idioma", None))
        self.tool_atalhos.setText(QCoreApplication.translate("MainWindow", u"Atalhos do teclado", None))
        self.tool_tema.setText(QCoreApplication.translate("MainWindow", u" Tema do sistema", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">Desenvolvido e publicado por:</span></p><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">Keven Lucas</span></p></body></html>", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">(19) 98201-8869</span></p></body></html>", None))
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; font-style:italic; text-decoration: underline;\">Clique aqui para visitar o site</span></p></body></html>", None))
    # retranslateUi

