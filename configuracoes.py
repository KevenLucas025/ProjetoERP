import json

class Configuracoes_Login:
    def __init__(self, main_window):
        self.main_window = main_window
        self.usuario = None
        self.senha = None
        self.mantem_conectado = False
        self.nao_mostrar_mensagem_boas_vindas = False
        self.nao_mostrar_aviso_irreversivel = False
        self.nao_mostrar_mensagem_arquivo_excel = False
        self.nao_mostrar_mensagem_arquivo_excel_fisicos = False
        self.historico_autocompletes = {}
        self.carregar()

    def carregar(self):
        try:
            with open("config.json", "r") as f:
                config = json.load(f)
                self.usuario = config.get("usuario", "")
                self.senha = config.get("senha","")
                self.mantem_conectado = config.get("mantem_conectado", False)
                self.nao_mostrar_mensagem_boas_vindas = config.get("nao_mostrar_mensagem_boas_vindas", False)
                self.nao_mostrar_aviso_irreversivel = config.get("nao_mostrar_aviso_irreversivel", False)
                self.nao_mostrar_mensagem_arquivo_excel = config.get("nao_mostrar_mensagem_arquivo_excel", False)
                self.nao_mostrar_mensagem_arquivo_excel_fisicos = config.get("nao_mostrar_mensagem_arquivo_excel_fisicos",False)
                self.historico_autocompletes = config.get("historico_autocompletes", {})
        except FileNotFoundError:
            print("Arquivo config.json não encontrado")
        except json.JSONDecodeError:
            print("Erro ao decodificar o JSON")

    def salvar(self, usuario, senha, mantem_conectado):
        config = {
            "usuario": usuario or "",
            "senha": senha or "",
            "mantem_conectado": mantem_conectado,
            "nao_mostrar_mensagem_boas_vindas": self.nao_mostrar_mensagem_boas_vindas,
            "nao_mostrar_aviso_irreversivel": self.nao_mostrar_aviso_irreversivel,
            "nao_mostrar_mensagem_arquivo_excel": self.nao_mostrar_mensagem_arquivo_excel,
            "nao_mostrar_mensagem_arquivo_excel_fisicos":self.nao_mostrar_mensagem_arquivo_excel_fisicos,
            "historico_autocompletes": self.historico_autocompletes
        }
        with open("config.json", "w") as f:
            json.dump(config, f,indent=4,ensure_ascii=False)


    def salvar_configuracoes(self, usuario, senha, mantem_conectado):
        """Atualiza as variáveis e salva no JSON."""
        self.usuario = usuario
        self.senha = senha
        self.mantem_conectado = mantem_conectado
        print(f"Salvando configurações: {usuario}, {mantem_conectado}")
        self.salvar(usuario, senha, mantem_conectado)

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