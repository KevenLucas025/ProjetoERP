from PySide6.QtCore import QThread, Signal
import requests
import os
import time

class DownloadThread(QThread):
    concluido = Signal(str)     # Emite o caminho quando termina
    erro = Signal(str)          # Emite uma mensagem de erro
    progresso = Signal(int)     # Emite o progresso (0–100)

    def __init__(self, url, destino):
        super().__init__()
        self.url = url
        self.destino = destino
        self.cancelado = False

    def run(self):
        try:
            response = requests.get(self.url, stream=True)
            response.raise_for_status()

            total = int(response.headers.get("content-length", 0))
            if total == 0:
                raise Exception("Não foi possível obter o tamanho do arquivo.")

            baixado = 0

            with open(self.destino, "wb") as f:
                for chunk in response.iter_content(32768):  # 32 KB → barra suave
                    if self.cancelado:
                        f.close()
                        if os.path.exists(self.destino):
                            os.remove(self.destino)
                        return

                    if chunk:
                        f.write(chunk)
                        baixado += len(chunk)

                        percentual = int((baixado / total) * 100)
                        self.progresso.emit(percentual)

                        time.sleep(0.01)  # deixa suave sem travar

            self.progresso.emit(100)
            self.concluido.emit(self.destino)

        except Exception as e:
            self.erro.emit(str(e))

    def cancelar(self):
        self.cancelado = True
