import os
import time
import shutil
import psutil
import sys
import subprocess
import zipfile
import tempfile


NOME_EXE_PRINCIPAL = "Sistema de Gerenciamento.exe"
NOME_ATUALIZADOR = "Atualizador.exe"
NOME_ZIP_ATUALIZACAO = "Sistema-de-Gerenciamento.zip"


def esperar_processo_morrer(caminho_exe):
    caminho_exe = os.path.abspath(caminho_exe).lower()

    while True:
        ativo = False

        for proc in psutil.process_iter(["exe"]):
            try:
                exe = proc.info.get("exe")
                if exe and os.path.abspath(exe).lower() == caminho_exe:
                    ativo = True
                    break
            except Exception:
                pass

        if not ativo:
            break

        time.sleep(0.5)


def remover_com_tentativas(caminho, tentativas=10, intervalo=0.5):
    for _ in range(tentativas):
        try:
            if os.path.isdir(caminho):
                shutil.rmtree(caminho)
            elif os.path.exists(caminho):
                os.remove(caminho)
            return True
        except Exception:
            time.sleep(intervalo)
    return not os.path.exists(caminho)


def copiar_arquivo_com_tentativas(origem, destino, tentativas=10, intervalo=0.5):
    os.makedirs(os.path.dirname(destino), exist_ok=True)

    for _ in range(tentativas):
        try:
            shutil.copy2(origem, destino)
            return True
        except Exception:
            time.sleep(intervalo)
    return False


def copiar_pasta_atualizacao(origem, destino):
    """
    Copia todos os arquivos da nova versão para a pasta do sistema,
    preservando o Atualizador.exe atual.
    """
    for raiz, dirs, files in os.walk(origem):
        rel = os.path.relpath(raiz, origem)
        pasta_destino = destino if rel == "." else os.path.join(destino, rel)
        os.makedirs(pasta_destino, exist_ok=True)

        for arquivo in files:
            origem_arquivo = os.path.join(raiz, arquivo)
            destino_arquivo = os.path.join(pasta_destino, arquivo)

            # Não sobrescreve o atualizador que está rodando
            if arquivo.lower() == NOME_ATUALIZADOR.lower():
                continue

            # Remove o arquivo antigo, se existir
            if os.path.exists(destino_arquivo):
                try:
                    os.remove(destino_arquivo)
                except Exception:
                    pass

            ok = copiar_arquivo_com_tentativas(origem_arquivo, destino_arquivo)
            if not ok:
                raise RuntimeError(f"Falha ao copiar arquivo: {arquivo}")


def encontrar_pasta_raiz_extraida(pasta_extracao):
    """
    Procura a pasta que contém o executável principal.
    Pode ser a própria pasta de extração ou uma subpasta.
    """
    exe_esperado = NOME_EXE_PRINCIPAL.lower()

    for raiz, dirs, files in os.walk(pasta_extracao):
        for arquivo in files:
            if arquivo.lower() == exe_esperado:
                return raiz

    return None


def main():
    pasta_sistema = os.path.dirname(sys.executable)

    exe_final = os.path.join(pasta_sistema, NOME_EXE_PRINCIPAL)
    zip_atualizacao = os.path.join(pasta_sistema, NOME_ZIP_ATUALIZACAO)

    # Aguarda o sistema principal fechar
    if os.path.exists(exe_final):
        esperar_processo_morrer(exe_final)

    # Se não existe ZIP, não há o que atualizar
    if not os.path.exists(zip_atualizacao):
        sys.exit(0)

    pasta_temp_base = tempfile.mkdtemp(prefix="sg_update_")
    pasta_extracao = os.path.join(pasta_temp_base, "extraido")

    try:
        os.makedirs(pasta_extracao, exist_ok=True)

        # Extrai o ZIP
        with zipfile.ZipFile(zip_atualizacao, "r") as zip_ref:
            zip_ref.extractall(pasta_extracao)

        # Encontra a pasta real da nova versão
        pasta_nova_versao = encontrar_pasta_raiz_extraida(pasta_extracao)
        if not pasta_nova_versao:
            raise RuntimeError("Não foi possível localizar os arquivos da nova versão no ZIP.")

        # Copia tudo por cima da instalação atual
        copiar_pasta_atualizacao(pasta_nova_versao, pasta_sistema)

        # Remove o ZIP depois da atualização bem-sucedida
        try:
            os.remove(zip_atualizacao)
        except Exception:
            pass

        # Reinicia o sistema
        if os.path.exists(exe_final):
            subprocess.Popen(
                [exe_final],
                cwd=pasta_sistema,
                creationflags=subprocess.DETACHED_PROCESS
            )

    except Exception as e:
        erro_path = os.path.join(pasta_sistema, "erro_atualizador.log")
        try:
            with open(erro_path, "a", encoding="utf-8") as f:
                f.write(f"{time.strftime('%d/%m/%Y %H:%M:%S')} - {str(e)}\n")
        except Exception:
            pass

    finally:
        remover_com_tentativas(pasta_temp_base, tentativas=10, intervalo=0.5)

    sys.exit(0)


if __name__ == "__main__":
    main()