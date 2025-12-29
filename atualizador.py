import os
import time
import shutil
import psutil
import sys

def esperar_processo_morrer(caminho_exe):
    caminho_exe = caminho_exe.lower()

    while True:
        ativo = False
        for proc in psutil.process_iter(['exe']):
            try:
                exe = proc.info.get('exe')
                if exe and exe.lower() == caminho_exe:
                    ativo = True
                    break
            except:
                pass

        if not ativo:
            break

        time.sleep(0.5)


def main():
    # =====================================
    # ATUALIZADOR SEMPRE RODA COMO EXE
    # =====================================
    pasta_sistema = os.path.dirname(sys.executable)

    exe_final = os.path.join(pasta_sistema, "SistemadeGerenciamento.exe")
    exe_tmp = os.path.join(pasta_sistema, "SistemadeGerenciamento_tmp.exe")

    # =====================================
    # AGUARDA O SISTEMA FECHAR
    # =====================================
    if os.path.exists(exe_final):
        esperar_processo_morrer(exe_final)

    # =====================================
    # SUBSTITUI O EXECUTÁVEL
    # =====================================
    if os.path.exists(exe_tmp):
        if os.path.exists(exe_final):
            for _ in range(5):  # tolerância ao Windows
                try:
                    os.remove(exe_final)
                    break
                except:
                    time.sleep(0.5)

        shutil.move(exe_tmp, exe_final)

    # =====================================
    # REINICIA O SISTEMA
    # =====================================
    if os.path.exists(exe_final):
        os.startfile(exe_final)

    sys.exit(0)


if __name__ == "__main__":
    main()
