import json
import sys
import os
from PySide6.QtWidgets import QMessageBox

class Configuracoes_Login:
    def __init__(self, main_window):
        self.main_window = main_window
        self.tamanho_fonte_percentual = 100  # valor padrão
        self.nome_usuario = None
        self.usuario = None
        self.senha = None
        self.email = None
        self.mantem_conectado = False
        self.nao_mostrar_mensagem_boas_vindas = False
        self.nao_mostrar_aviso_irreversivel = False
        self.nao_mostrar_mensagem_arquivo_excel = False
        self.nao_mostrar_mensagem_arquivo_excel_fisicos = False
        self.nao_mostrar_aviso_atualizacoes = False
        self.atualizacoes_automaticas = False
        self.historico_autocompletes = {}
        self.tema = "classico" # padrão
        self.atalhos = {}
        self.carregar()
        self.migrar_config_se_necessario()
        
    def rodando_como_exe(self):
        return getattr(sys, "frozen", False)


    def pasta_configuracao(self):
        if self.rodando_como_exe():
            return os.path.join(os.getenv("APPDATA"), "SistemaGerenciamento")
        else:
            return os.getcwd()


    def caminho_config_json(self):
        pasta = self.pasta_configuracao()
        os.makedirs(pasta, exist_ok=True)
        return os.path.join(pasta, "config.json")
    
    def migrar_config_se_necessario(self):
        if not self.rodando_como_exe():
            return
        
        config_antigo = os.path.join(os.getcwd(),"config.json")
        config_novo = self.caminho_config_json()
        
        if os.path.exists(config_antigo) and not os.path.exists(config_novo):
            try:
                os.replace(config_antigo,config_novo)
            except Exception as e:
                QMessageBox.information(self,"Erro", "Não foi possível migrar o arquivo de configurações.")
        

    def carregar(self):
        try:
            with open(self.caminho_config_json(), "r", encoding="utf-8") as f:
                conteudo = f.read().strip()

                # Arquivo existe mas está vazio
                if not conteudo:
                    print("config.json está vazio, aplicando tema padrão.")
                    self.tema = "classico"  # ou "escuro", se quiser
                    self.tamanho_fonte_percentual = 100
                    return

                config = json.loads(conteudo)

                self.nome_usuario = config.get("nome_usuario","")
                self.usuario = config.get("usuario", "")
                self.senha = config.get("senha", "")
                self.email = config.get("email", "")
                self.mantem_conectado = bool(config.get("mantem_conectado", False))
                self.nao_mostrar_mensagem_boas_vindas = config.get("nao_mostrar_mensagem_boas_vindas", False)
                self.nao_mostrar_aviso_irreversivel = config.get("nao_mostrar_aviso_irreversivel", False)
                self.nao_mostrar_mensagem_arquivo_excel = config.get("nao_mostrar_mensagem_arquivo_excel", False)
                self.nao_mostrar_mensagem_arquivo_excel_fisicos = config.get("nao_mostrar_mensagem_arquivo_excel_fisicos", False)
                self.nao_mostrar_aviso_atualizacoes = config.get("nao_mostrar_aviso_atualizacoes", False)
                self.historico_autocompletes = config.get("historico_autocompletes", {})
                self.atalhos = config.get("atalhos", {})
                self.atualizacoes_automaticas = config.get("atualizacoes_automaticas",False)
                

                # Tema
                self.tema = config.get("tema", "classico")
                # Percentual de fonte
                self.tamanho_fonte_percentual = config.get("tamanho_fonte_percentual", 100)

        except FileNotFoundError:
            print("Arquivo config.json não encontrado, aplicando tema padrão.")
            self.tema = "classico"  # ou "escuro"
            self.tamanho_fonte_percentual = 100
        except json.JSONDecodeError:
            print("Erro ao decodificar o JSON, aplicando tema padrão.")
            self.tema = "classico"  # ou "escuro"
            self.tamanho_fonte_percentual = 100 


    def salvar(self, nome_usuario=None, usuario=None, senha=None, email=None,
           mantem_conectado=None, tamanho_fonte_percentual=None):
        # Atualiza atributos da instância
        if nome_usuario is not None:
            self.nome_usuario = nome_usuario
        if usuario is not None:
            self.usuario = usuario
        if senha is not None:
            self.senha = senha
        if email is not None:
            self.email = email
        if mantem_conectado is not None:
            self.mantem_conectado = mantem_conectado
        if tamanho_fonte_percentual is not None:
            self.tamanho_fonte_percentual = tamanho_fonte_percentual

        path = self.caminho_config_json()

        # 1) Carrega config existente (pra não perder chaves de outros módulos)
        config_existente = {}
        try:
            if os.path.exists(path):
                with open(path, "r", encoding="utf-8") as f:
                    txt = f.read().strip()
                    config_existente = json.loads(txt) if txt else {}
        except json.JSONDecodeError:
            config_existente = {}

        # 2) Atualiza apenas as chaves do login
        config_existente.update({
            "nome_usuario": self.nome_usuario or "",
            "usuario": self.usuario or "",
            "senha": self.senha or "",
            "email": self.email or "",
            "mantem_conectado": self.mantem_conectado,
            "nao_mostrar_mensagem_boas_vindas": self.nao_mostrar_mensagem_boas_vindas,
            "nao_mostrar_aviso_irreversivel": self.nao_mostrar_aviso_irreversivel,
            "nao_mostrar_mensagem_arquivo_excel": self.nao_mostrar_mensagem_arquivo_excel,
            "nao_mostrar_mensagem_arquivo_excel_fisicos": self.nao_mostrar_mensagem_arquivo_excel_fisicos,
            "nao_mostrar_aviso_atualizacoes": self.nao_mostrar_aviso_atualizacoes,
            "historico_autocompletes": self.historico_autocompletes,
            "tema": self.tema,
            "tamanho_fonte_percentual": self.tamanho_fonte_percentual,
            "atalhos": self.atalhos,
            "atualizacoes_automaticas": self.atualizacoes_automaticas
        })

        # 3) Salva mantendo o resto (ex: ultimos_diretorios)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(config_existente, f, indent=4, ensure_ascii=False)


            
    def salvar_atalho(self, acao, tecla):
        """Salva/atualiza um atalho específico e persiste no JSON"""
        self.atalhos[acao] = tecla
        self.salvar(
            nome_usuario=self.nome_usuario,
            usuario=self.usuario,
            senha=self.senha,
            mantem_conectado=self.mantem_conectado)


    def obter_atalho(self, acao):
        """Retorna o atalho de uma ação, ou None"""
        return self.atalhos.get(acao)

    def obter_todos_atalhos(self):
        """Retorna todos os atalhos"""
        return self.atalhos


    def salvar_configuracoes(
        self,
        nome_usuario=None,
        usuario=None,
        senha=None,
        email=None,
        mantem_conectado=False
    ):
        """Atualiza as variáveis e salva no JSON."""

        if nome_usuario is not None:
            self.nome_usuario = nome_usuario

        if usuario is not None:
            self.usuario = usuario

        if senha is not None:
            self.senha = senha

        # 👇 NÃO sobrescreve o e-mail se vier None
        if email:
            self.email = email

        self.mantem_conectado = mantem_conectado

        print(f"Salvando configurações: Usuário - {self.usuario}")
        print(f"E-mail salvo: {self.email}")

        self.salvar(
            nome_usuario=self.nome_usuario,
            usuario=self.usuario,
            senha=self.senha,
            email=self.email,
            mantem_conectado=self.mantem_conectado
        )


    def salvar_percentual_fonte(self, percentual):
        """Salva apenas o percentual de fonte no JSON"""
        self.salvar(tamanho_fonte_percentual=percentual)

    def sair(self):
        # Lógica para desconectar o usuário e limpar as configurações
        self.nao_mostrar_mensagem_boas_vindas = False
        self.nao_mostrar_aviso_irreversivel = False
        self.nao_mostrar_mensagem_arquivo_excel = False
        self.nao_mostrar_mensagem_arquivo_excel_fisicos = False
        self.nao_mostrar_aviso_atualizacoes = False
        self.salvar(None, None, False)
        self.nome_usuario = ""
        self.usuario = ""
        self.senha = None
        self.mantem_conectado = False

        # Atualiza a interface do usuário se necessário
        self.main_window.btn_login.setEnabled(True)
        self.main_window.lbl_status.setText("Desconectado")
        self.main_window.txt_usuario.setText("")
        self.main_window.chk_mantenha_conectado.setChecked(False)

    def verificar_credenciais_salvas(self):
        return self.usuario and self.mantem_conectado

    def obter_senha_salva(self):
        try:
            with open(self.caminho_config_json(), "r",encoding="utf-8") as f:
                config = json.load(f)
                return config.get("senha", "")
        except FileNotFoundError:
            return ""

    def obter_usuario_logado(self):
        self.carregar()
        # Ajustado para pegar o usuário diretamente do JSON e não de um método get
        return self.usuario if self.usuario else None
    
    def obter_nome_completo_usuario(self):
        self.carregar()
        # Ajustado para pegar o nome completo do usuário diretamente do JSON e não de um método get
        return self.nome_usuario if self.nome_usuario else None

    def carregar_historico_autocompletar(self,nome_campo):
        return self.historico_autocompletes.get(nome_campo, [])
    
    def adicionar_ao_historico(self,nome_campo,texto):
        if not texto.strip():
            return
        if nome_campo not in self.historico_autocompletes:
            self.historico_autocompletes[nome_campo] = []
        if texto not in self.historico_autocompletes[nome_campo]:
            self.historico_autocompletes[nome_campo].append(texto)
            self.salvar(
            nome_usuario=self.nome_usuario,
            usuario=self.usuario,
            senha=self.senha,
            email=self.email,
            mantem_conectado=self.mantem_conectado
        )

            
    def obter_email_usuario(self):
        self.carregar()
        return self.email if self.email else None
