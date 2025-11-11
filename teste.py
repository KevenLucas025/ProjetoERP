'''from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Teste")


        
        QMessageBox.warning(self, "Teste", "Apenas um teste para ver a cor do aviso")





if __name__ == "__main__":
    app = QApplication(sys.argv)

    app.setStyle("WindowsVista")
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())'''


'''import os
import re

# Caminho da pasta do seu projeto
pasta_projeto = r"C:\Users\keven\OneDrive\Área de Trabalho\Python Work\ProjetoERP"

# Regex para encontrar sqlite3.connect com banco "banco_de_dados.db"
pattern = re.compile(r'sqlite3\.connect\(["\']banco_de_dados\.db["\']\)')

# Função para percorrer arquivos
def atualizar_arquivos(pasta):
    for root, dirs, files in os.walk(pasta):
        for file in files:
            if file.endswith(".py"):
                caminho_arquivo = os.path.join(root, file)
                with open(caminho_arquivo, "r", encoding="utf-8") as f:
                    conteudo = f.read()

                # Substitui todas as ocorrências
                novo_conteudo = pattern.sub("self.db.connection", conteudo)

                if novo_conteudo != conteudo:
                    with open(caminho_arquivo, "w", encoding="utf-8") as f:
                        f.write(novo_conteudo)
                    print(f"[OK] Atualizado: {caminho_arquivo}")

# Executa
atualizar_arquivos(pasta_projeto)
print("Atualização concluída!")'''


