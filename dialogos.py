# dialogos.py
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QComboBox, QDialogButtonBox,QLineEdit
import json
from utils import Temas

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
            bg_cor = "#202124"
            text_cor = "white"
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
        # claro
            bg_cor = "white"
            text_cor = "black"
            button_style = """
                QPushButton {
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                                stop:0 rgb(50,150,250),
                                                stop:1 rgb(100,200,255));
                    color: black;
                    border-radius: 8px;
                    font-size: 12px;
                    border: 2px solid rgb(50,150,250);
                    padding: 5px;
                }
                QPushButton:hover {
                    background-color: #e5f3ff;
                }
                QPushButton:pressed {
                    background-color: #cce7ff;
                    border: 2px solid #3399ff;
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
            bg_cor = """qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.2 #f5f5f5, stop: 1 #c0c0c0)"""
            text_cor = "black"
            lineedit_bg = "white"

            button_style = """
                QPushButton {
                    color: rgb(255, 255, 255);
                    border-radius: 8px;
                    font-size: 16px;
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */
                    border: 4px solid transparent;
            }

            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */
                color: black;
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
            QDialog {{
                background-color: {bg_cor};
                color: {text_cor};
                font-size: 12px;
            }}
            {button_style}
            {combo_style}
            {scroll_style}
            {lineedit_style}
            QLabel {{
                color: {text_cor};
                font-size: 12px;
                background: transparent;
            }}
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