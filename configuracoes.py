import json

class Configuracoes_Login:
    def __init__(self, main_window):
        self.main_window = main_window
        self.tamanho_fonte_percentual = 100  # valor padrão
        self.usuario = None
        self.senha = None
        self.mantem_conectado = False
        self.nao_mostrar_mensagem_boas_vindas = False
        self.nao_mostrar_aviso_irreversivel = False
        self.nao_mostrar_mensagem_arquivo_excel = False
        self.nao_mostrar_mensagem_arquivo_excel_fisicos = False
        self.historico_autocompletes = {}
        self.tema = "classico"
        self.atalhos = {}
        self.carregar()

    def carregar(self):
        try:
            with open("config.json", "r", encoding="utf-8") as f:
                conteudo = f.read().strip()

                # Arquivo existe mas está vazio
                if not conteudo:
                    print("config.json está vazio, aplicando tema padrão.")
                    self.tema = "classico"  # ou "escuro", se quiser
                    self.tamanho_fonte_percentual = 100
                    return

                config = json.loads(conteudo)

                self.usuario = config.get("usuario", "")
                self.senha = config.get("senha", "")
                self.mantem_conectado = config.get("mantem_conectado", False)
                self.nao_mostrar_mensagem_boas_vindas = config.get("nao_mostrar_mensagem_boas_vindas", False)
                self.nao_mostrar_aviso_irreversivel = config.get("nao_mostrar_aviso_irreversivel", False)
                self.nao_mostrar_mensagem_arquivo_excel = config.get("nao_mostrar_mensagem_arquivo_excel", False)
                self.nao_mostrar_mensagem_arquivo_excel_fisicos = config.get("nao_mostrar_mensagem_arquivo_excel_fisicos", False)
                self.historico_autocompletes = config.get("historico_autocompletes", {})
                self.atalhos = config.get("atalhos", {})

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


    def salvar(self, usuario=None, senha=None, mantem_conectado=None, tamanho_fonte_percentual=None):
        # Atualiza atributos da instância
        if usuario is not None:
            self.usuario = usuario
        if senha is not None:
            self.senha = senha
        if mantem_conectado is not None:
            self.mantem_conectado = mantem_conectado
        if tamanho_fonte_percentual is not None:
            self.tamanho_fonte_percentual = tamanho_fonte_percentual

        config = {
            "usuario": self.usuario or "",
            "senha": self.senha or "",
            "mantem_conectado": self.mantem_conectado,
            "nao_mostrar_mensagem_boas_vindas": self.nao_mostrar_mensagem_boas_vindas,
            "nao_mostrar_aviso_irreversivel": self.nao_mostrar_aviso_irreversivel,
            "nao_mostrar_mensagem_arquivo_excel": self.nao_mostrar_mensagem_arquivo_excel,
            "nao_mostrar_mensagem_arquivo_excel_fisicos": self.nao_mostrar_mensagem_arquivo_excel_fisicos,
            "historico_autocompletes": self.historico_autocompletes,
            "tema": self.tema,
            "tamanho_fonte_percentual": self.tamanho_fonte_percentual,
            "atalhos": self.atalhos,
        }

        with open("config.json", "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4, ensure_ascii=False)
            
    def salvar_atalho(self, acao, tecla):
        """Salva/atualiza um atalho específico e persiste no JSON"""
        self.atalhos[acao] = tecla
        self.salvar(self.usuario, self.senha, self.mantem_conectado)

    def obter_atalho(self, acao):
        """Retorna o atalho de uma ação, ou None"""
        return self.atalhos.get(acao)

    def obter_todos_atalhos(self):
        """Retorna todos os atalhos"""
        return self.atalhos


    def salvar_configuracoes(self, usuario, senha, mantem_conectado):
        """Atualiza as variáveis e salva no JSON."""
        self.usuario = usuario
        self.senha = senha
        self.mantem_conectado = mantem_conectado
        print(f"Salvando configurações: {usuario}, {mantem_conectado}")
        self.salvar(usuario, senha, mantem_conectado)

    def salvar_percentual_fonte(self, percentual):
        """Salva apenas o percentual de fonte no JSON"""
        self.salvar(tamanho_fonte_percentual=percentual)

    def sair(self):
        # Lógica para desconectar o usuário e limpar as configurações
        self.nao_mostrar_mensagem_boas_vindas = False
        self.nao_mostrar_aviso_irreversivel = False
        self.nao_mostrar_mensagem_arquivo_excel = False
        self.nao_mostrar_mensagem_arquivo_excel_fisicos = False
        self.salvar(None, None, False)
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
            with open("config.json", "r") as f:
                config = json.load(f)
                return config.get("senha", "")
        except FileNotFoundError:
            return ""

    def obter_usuario_logado(self):
        self.carregar()
        # Ajustado para pegar o usuário diretamente do JSON e não de um método get
        return self.usuario if self.usuario else None

    def carregar_historico_autocompletar(self,nome_campo):
        return self.historico_autocompletes.get(nome_campo, [])
    
    def adicionar_ao_historico(self,nome_campo,texto):
        if not texto.strip():
            return
        if nome_campo not in self.historico_autocompletes:
            self.historico_autocompletes[nome_campo] = []
        if texto not in self.historico_autocompletes[nome_campo]:
            self.historico_autocompletes[nome_campo].append(texto)
            self.salvar(self.usuario,self.senha,self.mantem_conectado)