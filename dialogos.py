from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QComboBox, QDialogButtonBox,QLineEdit
import json
from utils import Temas
from PySide6.QtCore import Qt

# -----------------------------
# Classe base de dialog estilizado
# -----------------------------
class DialogoEstilizado(QDialog):
    def __init__(self, tema=None, parent=None):
        super().__init__(parent)
        self.temas = Temas()

        # Carrega tema do config se não for passado
        if tema is None:
            config = self.temas.carregar_config_arquivo()
            tema = config.get("tema", "claro")
        self.tema = tema

        # Botões padrão OK / Cancelar
        self.botoes = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.botoes.button(QDialogButtonBox.Ok).setText("OK")
        self.botoes.button(QDialogButtonBox.Cancel).setText("Cancelar")
        self.botoes.accepted.connect(self.accept)
        self.botoes.rejected.connect(self.reject)

        # Aplica o estilo
        self.aplicar_estilo()
        

    def aplicar_estilo(self):
        # Estilos por tema
        if self.tema == "escuro":
            bg_cor = "#2b2b2b"
            text_cor = "white"
            lineedit_bg = "#2b2b2b"  
            button_style = """
                QPushButton {
                    border-radius: 8px;
                    background: qlineargradient(
                        x1:0, y1:0, x2:0, y2:1,
                        stop:0 rgb(60, 60, 60),
                        stop:1 rgb(100, 100, 100)
                    );
                    font-size: 12px;
                    padding: 5px;
                    color: white;
                }
                QPushButton:hover {
                    background-color: #444444;
                }
                QPushButton:pressed {
                    background-color: #555555;
                    border: 2px solid #888888;
                }
            """
            combo_style = """
                QComboBox {
                    color: white;
                    border: 2px solid #ffffff;
                    border-radius: 6px;
                    padding: 4px 10px;
                    background-color: #2b2b2b;
                }
                QComboBox QAbstractItemView::item:hover {
                    background-color: #444444;
                    color: white;
                }
                QComboBox QAbstractItemView::item:selected {
                    background-color: #696969;
                    color: white;
                }
            """
            scroll_style = """
            /* Scrollbar vertical */
            QScrollBar:vertical {
                background: #ffffff;   /* fundo do track */
                width: 12px;
                margin: 0px;
                border-radius: 6px;
            }

            QScrollBar::handle:vertical {
                background: #555555;   /* cor do handle */
                border-radius: 6px;
                min-height: 20px;
            }

            QScrollBar::handle:vertical:hover {
                background: #777777;   /* hover no handle */
            }

            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical {
                background: none;
                height: 0px;
            }

            QScrollBar::add-page:vertical,
            QScrollBar::sub-page:vertical {
                background: none;
            }
            """
            dialog_style = """
            QDialog {
                background-color: #2b2b2b;
                color: white;
                font-size: 12px;
            }
            """
            lineedit_style = f"""
                QLineEdit {{
                    background-color: {lineedit_bg};
                    color: {text_cor};
                    border: 2px solid white;
                    border-radius: 6px;
                    padding: 3px;
                }}
            """

        elif self.tema == "claro":
            bg_cor = "white"
            text_cor = "black"
            lineedit_bg = "black"
            button_style = """
                QPushButton {
                    border-radius: 8px;
                    background: qlineargradient(
                        x1:0, y1:0, x2:0, y2:1,
                        stop:0 rgb(220, 220, 220),  /* topo */
                        stop:1 rgb(245, 245, 245)   /* base */
                    );
                    font-size: 12px;
                    padding: 5px;
                    color: #000000; /* texto escuro */
                }

                QPushButton:hover {
                    background-color: #e0e0e0;
                }

                QPushButton:pressed {
                    background-color: #d0d0d0;
                    border: 2px solid #aaaaaa;
                }
            """
            combo_style = """
                QComboBox {
                    background-color: white;
                    border: 2px solid rgb(50,150,250);
                    border-radius: 5px;
                    color: black;
                    padding: 4px 10px;
                }
                QComboBox QAbstractItemView::item:hover {
                    background-color: #e5f3ff;
                    color: black;
                }
                QComboBox QAbstractItemView::item:selected {
                    background-color: #a0d1ff;
                    color: black;
                }
            """
            dialog_style = """
                QDialog {
                    background: qlineargradient(
                    x1: 0, y1: 0,
                    x2: 0, y2: 1,
                    stop: 0 #ffffff,       /* branco puro no topo */
                    stop: 0.2 #f5f5f5,     /* branco acinzentado na faixa */
                    stop: 1 #c0c0c0       /* branco acinzentado no resto */
                );
                color: black;
                }
                QDialog QPushButton{
                    background-color: #ffffff;
                    color: black;
                    border: 1px solid #0078d7;
                    padding: 2px 10px;
                    border-radius: 6px;
                    min-width: 40px;
                    min-height: 10px; 
                
                }
                QDialog QPushButton:hover{
                    background-color: #e6f0fa;
                }
                QDialog QPushButton:pressed{
                    background-color: #c7d7f9;
                }
            """
            scroll_style = """
                QScrollBar:vertical {
                    border: none;
                    background-color: #f0f0f0;
                    width: 12px;
                    margin: 0px;
                    border-radius: 5px;
                }
                QScrollBar::handle:vertical {
                    background-color: #b0b0b0;  /* cinza claro */
                    min-height: 22px;
                    border-radius: 5px;
                }
                /* Groove vertical */
                QScrollBar::groove:vertical {
                    background-color: #e0e0e0;
                    border-radius: 5px;
                    width: 15px;
                    margin: 10px 0px 10px 0px;
                }
            """
            lineedit_style = """
                QLineEdit {
                    background-color: white;
                    color: black;
                    border: 2px solid rgb(50,150,250);
                    border-radius: 6px;
                    padding: 3px;
                }
            """
        else: #classico
            bg_cor = "white"
            text_cor = "black"
            lineedit_bg = "black"

            button_style = """
                QPushButton {
                    background-color: #ffffff;
                    color: black;
                    border: 1px solid #0078d7;
                    padding: 2px 10px;
                    border-radius: 6px;
                    min-width: 40px;
                    min-height: 10px; 
                    font-size: 12px; 
                }
                QPushButton:hover {
                    background-color: #e6f0fa;
                }
                PushButton:pressed {
                    background-color: #c7d7f9;
                }
            """
            combo_style = """
                QComboBox {
                    background-color: white;
                    border: 3px solid rgb(50,150,250);
                    border-radius: 5px;
                    color: black;
                    padding: 5px;
                }
                QComboBox QAbstractItemView {
                    background-color: white;
                    color: black;
                    border: 1px solid #ccc;
                    selection-background-color: #e5e5e5;
                    selection-color: black;
                }
                QComboBox QScrollBar:vertical {
                    background: #f5f5f5;
                    width: 12px;
                    border: none;
                }
                QComboBox QScrollBar::handle:vertical {
                    background: #cccccc;
                    min-height: 20px;
                    border-radius: 5px;
                }
            """
            dialog_style = """
                QDialog {
                    background: qlineargradient(
                        x1: 0, y1: 0,
                        x2: 0, y2: 1,
                        stop: 0 #ffffff,
                        stop: 0.2 #f5f5f5,
                        stop: 1 #c0c0c0
                    );
                    color: black;
                    font-size: 12px;
                }
            """
            scroll_style = """
                QScrollBar:vertical {
                    border: none;
                    background-color: rgb(255, 255, 255); /* branco */
                    width: 30px;
                    margin: 0px 10px 0px 10px;
                }
                QScrollBar::handle:vertical {
                    background-color: rgb(180, 180,180);  /* cinza */
                    min-height: 30px;
                    border-radius: 5px;
                }
            """
            lineedit_style = """
                QLineEdit {
                    background-color: white;
                    color: black;
                    border: 2px solid rgb(50,150,250);
                    border-radius: 6px;
                    padding: 3px;
                }
            """

        # Aplica o estilo apenas ao dialog e widgets internos
        self.setStyleSheet(f"""
            {button_style}
            {combo_style}
            {scroll_style}
            {lineedit_style}

            QLabel {{
                color: {text_cor};
                font-weight: 500;
                font-size: 12px;
                background: transparent;
            }}

            {dialog_style}
        """)




        


# -----------------------------
# Dialog específico: Escolher planilha
# -----------------------------
class EscolherPlanilhaDialog(DialogoEstilizado):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.setWindowTitle("Escolher Planilha de Exemplo")
        layout = QVBoxLayout(self)
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)

        # Label
        label = QLabel("Selecione uma planilha de exemplo:")
        layout.addWidget(label)

        # ComboBox com as opções
        self.combo = QComboBox()
        self.combo.addItems([
            "Planilha de Exemplo 1 - Produtos",
            "Planilha de Exemplo 2 - Usuários"
        ])
        layout.addWidget(self.combo)

        # Adiciona os botões OK / Cancelar da classe base
        layout.addWidget(self.botoes)

    def escolha(self):
        return self.combo.currentText()

class ComboDialog(DialogoEstilizado):
    def __init__(self, titulo, mensagem, opcoes, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle(titulo)

        layout = QVBoxLayout(self)
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)

        # Label
        label = QLabel(mensagem)
        layout.addWidget(label)

        # ComboBox com as opções
        self.combo = QComboBox()
        self.combo.addItems(opcoes)
        layout.addWidget(self.combo)

        # Botões OK / Cancelar da classe base
        layout.addWidget(self.botoes)

    def escolha(self):
        return self.combo.currentText()
    

class DialogoSenha(DialogoEstilizado):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("Confirmação de Segurança")

        layout = QVBoxLayout(self)
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)

        # Label
        label = QLabel("Digite a senha do sistema:")
        layout.addWidget(label)

        # Campo de senha
        self.input_senha = QLineEdit()
        self.input_senha.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.input_senha)

        # Botões da classe base
        layout.addWidget(self.botoes)

    def get_senha(self):
        return self.input_senha.text()
    

class ConfirmacaoDialog(DialogoEstilizado):
    def __init__(self, titulo, mensagem, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle(titulo)

        layout = QVBoxLayout(self)
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)

        # Label da mensagem
        label = QLabel(mensagem)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        # Botões personalizados: Sim / Não
        self.botoes.button(QDialogButtonBox.Ok).setText("Sim")
        self.botoes.button(QDialogButtonBox.Cancel).setText("Não")

        layout.addWidget(self.botoes)

# -----------------------------
# Dialog específico: Filtro de Usuários
# -----------------------------
class FiltroUsuarioDialog(DialogoEstilizado):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("Filtrar Usuário")

        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(15)
        self.layout.setContentsMargins(20, 20, 20, 20)

        # Label e ComboBox com as opções
        self.layout.addWidget(QLabel("Escolha o tipo de filtro:"))
        self.combo = QComboBox()
        self.filtros = [
            "Filtrar por Nome", "Filtrar Por Usuário", "Filtrar Por Acesso",
            "Filtrar Por Telefone", "Filtrar Por Email", "Filtrar Por RG",
            "Filtrar Por CPF", "Filtrar Por CNPJ"
        ]
        self.combo.addItems(self.filtros)
        self.layout.addWidget(self.combo)

        # Label + QLineEdit
        self.label_criterio = QLabel("Nome do Usuário:")
        self.txt_entrada = QLineEdit()
        self.layout.addWidget(self.label_criterio)
        self.layout.addWidget(self.txt_entrada)

        # Botões da classe base
        self.botoes.button(QDialogButtonBox.Ok).setText("Filtrar")
        self.layout.addWidget(self.botoes)

        # Conecta eventos
        self.combo.currentIndexChanged.connect(self.atualizar_label)
        self.txt_entrada.textEdited.connect(self.formatar_texto)

    def atualizar_label(self):
        texto = self.combo.currentText()
        mapeamento = {
            "Filtrar por Nome": "Nome do Usuário:",
            "Filtrar Por Usuário": "Usuário:",
            "Filtrar Por Acesso": "Acesso do Usuário:",
            "Filtrar Por Telefone": "Telefone do Usuário:",
            "Filtrar Por Email": "Email do Usuário:",
            "Filtrar Por RG": "RG do Usuário:",
            "Filtrar Por CPF": "CPF do Usuário:",
            "Filtrar Por CNPJ": "CNPJ do Usuário:"
        }
        self.label_criterio.setText(mapeamento.get(texto, "Digite o valor: "))

    def formatar_texto(self, text):
        criterio = self.combo.currentText()
        numero = ''.join(filter(str.isdigit, text))
        formatado = text
        cursor_pos = self.txt_entrada.cursorPosition()

        if criterio == "Filtrar Por CPF":
            numero = numero[:11]
            if len(numero) <= 3:
                formatado = numero
            elif len(numero) <= 6:
                formatado = "{}.{}".format(numero[:3], numero[3:])
            elif len(numero) <= 9:
                formatado = "{}.{}.{}".format(numero[:3], numero[3:6], numero[6:])
            else:
                formatado = "{}.{}.{}-{}".format(numero[:3], numero[3:6], numero[6:9], numero[9:])

        elif criterio == "Filtrar Por CNPJ":
            numero = numero[:14]
            if len(numero) <= 2:
                formatado = numero
            elif len(numero) <= 5:
                formatado = "{}.{}".format(numero[:2], numero[2:])
            elif len(numero) <= 8:
                formatado = "{}.{}.{}".format(numero[:2], numero[2:5], numero[5:])
            elif len(numero) <= 12:
                formatado = "{}.{}.{}/{}".format(numero[:2], numero[2:5], numero[5:8], numero[8:])
            else:
                formatado = "{}.{}.{}/{}-{}".format(numero[:2], numero[2:5], numero[5:8], numero[8:12], numero[12:14])

        elif criterio == "Filtrar Por RG":
            numero = numero[:9]
            if len(numero) <= 2:
                formatado = numero
            elif len(numero) <= 5:
                formatado = "{}.{}".format(numero[:2], numero[2:])
            elif len(numero) <= 8:
                formatado = "{}.{}.{}".format(numero[:2], numero[2:5], numero[5:])
            else:
                formatado = "{}.{}.{}-{}".format(numero[:2], numero[2:5], numero[5:8], numero[8:])

        elif criterio == "Filtrar Por Telefone":
            numero = numero[:11]
            if len(numero) <= 2:
                formatado = "({})".format(numero)
            elif len(numero) <= 6:
                formatado = "({}) {}".format(numero[:2], numero[2:])
            elif len(numero) <= 10:
                formatado = "({}) {}-{}".format(numero[:2], numero[2:6], numero[6:])
            else:
                formatado = "({}) {}-{}".format(numero[:2], numero[2:7], numero[7:])

        if self.txt_entrada.text() != formatado:
            self.txt_entrada.blockSignals(True)
            self.txt_entrada.setText(formatado)
            self.txt_entrada.setCursorPosition(min(cursor_pos + 1, len(formatado)))
            self.txt_entrada.blockSignals(False)

    def get_valores(self):
        return self.combo.currentText(), self.txt_entrada.text()
    


class FiltroProdutoDialog(DialogoEstilizado):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("Filtrar Produtos")

        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(15)
        self.layout.setContentsMargins(20, 20, 20, 20)

        # Label e ComboBox com as opções
        self.layout.addWidget(QLabel("Escolha o tipo de filtro:"))
        self.combo = QComboBox()
        self.filtros = [
            "Filtrar por Produto", "Filtrar Por Data do Cadastro", "Filtrar Por Usuário",
            "Filtrar Por Cliente", "Filtrar Por Código do Produto",
        ]
        self.combo.addItems(self.filtros)
        self.layout.addWidget(self.combo)

        # Label + QLineEdit
        self.label_criterio = QLabel("Nome do Produto:")
        self.txt_entrada = QLineEdit()
        self.layout.addWidget(self.label_criterio)
        self.layout.addWidget(self.txt_entrada)

        # Botões da classe base
        self.botoes.button(QDialogButtonBox.Ok).setText("Filtrar")
        self.layout.addWidget(self.botoes)

        # Conecta eventos
        self.combo.currentIndexChanged.connect(self.atualizar_label_produto)

    def atualizar_label_produto(self):
        texto = self.combo.currentText()
        mapeamento = {
            "Filtrar por Produto": "Nome do Produto:",
            "Filtrar Por Data do Cadastro": "Data do Cadastro",
            "Filtrar Por Usuário": "Usuário",
            "Filtrar Por Cliente": "Cliente",
		    "Filtrar Por Código do Produto": "Código do Produto"
        }
        self.label_criterio.setText(mapeamento.get(texto, "Digite o valor: "))

    def get_valores(self):
        criterio = self.combo.currentText()
        valor = self.txt_entrada.text().strip()
        return criterio, valor