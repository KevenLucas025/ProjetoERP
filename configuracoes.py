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
                self.usuario = config.get("usuario", None)
                self.mantem_conectado = config.get("mantem_conectado", False)
        except FileNotFoundError:
            pass

    def salvar(self, usuario, mantem_conectado):
        self.usuario = usuario
        self.mantem_conectado = mantem_conectado
        config = {
            "usuario": self.usuario,
            "mantem_conectado": self.mantem_conectado
        }
        with open("config.json", "w") as f:
            json.dump(config, f)

        self.main_window.carregar_configuracoes()

    def salvar_configuracoes(self, usuario, mantem_conectado):
        self.usuario = usuario
        self.mantem_conectado = mantem_conectado
        config = {
            "usuario": self.usuario,
            "mantem_conectado": self.mantem_conectado
        }
        with open("config.json", "w") as f:
            json.dump(config, f)

    def sair(self):
        # Implemente aqui a lógica para desconectar o usuário, limpar as configurações e fechar a aplicação
        self.main_window.btn_login.setEnabled(True)  # Ativar o botão de login
        self.main_window.lbl_status.setText("Desconectado")
        self.main_window.txt_usuario.setText("")  # Limpar o campo de usuário
        self.main_window.chk_mantenha_conectado.setChecked(False)  # Desmarcar a opção "mantenha-me conectado"

    def verificar_credenciais_salvas(self):
        return self.usuario and self.mantem_conectado

    def obter_senha_salva(self):
        try:
            with open("config.json", "r") as f:
                config = json.load(f)
                return config.get("senha", "")
        except FileNotFoundError:
            return ""
