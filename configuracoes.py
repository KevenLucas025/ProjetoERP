import json

class Configuracoes_Login:
    def __init__(self, main_window):
        self.main_window = main_window
        self.usuario = ""
        self.mantem_conectado = False
        self.carregar()

    def carregar(self):
        try:
            with open("config.json", "r") as f:
                config = json.load(f)
                self.usuario = config.get("usuario", "")
                self.mantem_conectado = config.get("mantem_conectado", False)
        except FileNotFoundError:
            pass

    def salvar(self, usuario, mantem_conectado):
        config = {
            "usuario": usuario,
            "mantem_conectado": mantem_conectado
        }
        with open("config.json", "w") as f:
            json.dump(config, f)

    def salvar_configuracoes(self, usuario, mantem_conectado):
        self.usuario = usuario
        self.mantem_conectado = mantem_conectado
        self.salvar(usuario, mantem_conectado)

    def sair(self):
        # Lógica para desconectar o usuário e limpar as configurações
        self.usuario = ""
        self.mantem_conectado = False
        self.salvar(self.usuario, self.mantem_conectado)

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
        # Ajustado para pegar o usuário diretamente do JSON e não de um método get
        return self.usuario if self.usuario else "Nenhum usuário logado"
