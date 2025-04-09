import json

class Configuracoes_Login:
    def __init__(self, main_window):
        self.main_window = main_window
        self.usuario = None
        self.senha = None
        self.mantem_conectado = False
        self.carregar()

    def carregar(self):
        try:
            with open("config.json", "r") as f:
                config = json.load(f)
                self.usuario = config.get("usuario", "")
                self.senha = config.get("senha","")
                self.mantem_conectado = config.get("mantem_conectado", False)
        except FileNotFoundError:
            print("Arquivo config.json não encontrado")

    def salvar(self, usuario,senha, mantem_conectado):
        config = {
            "usuario": usuario,
            "senha": senha,
            "mantem_conectado": mantem_conectado
        }
        with open("config.json", "w") as f:
            json.dump(config, f)

    def salvar_configuracoes(self, usuario, senha, mantem_conectado):
        """Atualiza as variáveis e salva no JSON."""
        self.usuario = usuario
        self.senha = senha
        self.mantem_conectado = mantem_conectado
        print(f"Salvando configurações: {usuario}, {mantem_conectado}")
        self.salvar(usuario, senha, mantem_conectado)

    def sair(self):
        # Lógica para desconectar o usuário e limpar as configurações
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
