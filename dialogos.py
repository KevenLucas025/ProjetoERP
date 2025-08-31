# dialogos.py
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QComboBox, QDialogButtonBox
import json

# -----------------------------
# Classe base de dialog estilizado
# -----------------------------
class DialogoEstilizado(QDialog):
    def __init__(self, tema=None, parent=None):
        super().__init__(parent)

        # Carrega tema do config se não for passado
        if tema is None:
            config = self.carregar_config()
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
        else:  # claro
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

        # Aplica o estilo apenas ao dialog e widgets internos
        self.setStyleSheet(f"""
            QDialog {{
                background-color: {bg_cor};
                color: {text_cor};
                font-size: 12px;
            }}
            {button_style}
            {combo_style}
            QLabel {{
                color: {text_cor};
                font-size: 12px;
            }}
        """)

    def carregar_config(self):
        try:
            with open("config.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return {"tema": "claro"}  # fallback padrão

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