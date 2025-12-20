import os
import time
import shutil
import psutil
import sys

def esperar_processar_morrer(caminho_exe):
    caminho_exe = caminho_exe.lower()

    while True:
        ativo = False
        for proc in psutil.process_iter(['exe']):
            try:
                if proc.info['exe'] and proc.info['exe'].lower() == caminho_exe:
                    ativo = True
            except:
                pass

        if not ativo:
            break

        time.sleep(0.5)


def main():
    # Pasta onde o atualizador está sendo executado
    pasta_sistema = os.path.dirname(sys.executable)

    origem_temp = os.path.join(pasta_sistema, "SistemadeGerenciamento_tmp.exe")
    destino_final = os.path.join(pasta_sistema, "SistemadeGerenciamento.exe")

    # Espera o EXE principal fechar
    esperar_processar_morrer(destino_final)

    # Apaga o antigo
    if os.path.exists(destino_final):
        os.remove(destino_final)

    # Move/renomeia o novo
    if os.path.exists(origem_temp):
        shutil.move(origem_temp, destino_final)

    # Executa o EXE atualizado
    os.startfile(destino_final)


if __name__ == "__main__":
    main()
