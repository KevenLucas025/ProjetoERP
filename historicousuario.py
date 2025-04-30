from PySide6.QtWidgets import QWidget,QTableWidget,QMessageBox,QTableWidgetItem,QInputDialog,QLineEdit,QAbstractItemView
from PySide6.QtGui import QBrush,QColor
from PySide6.QtCore import Qt
from database import DataBase
import sqlite3
import pandas as pd
import csv
from datetime import datetime



class Pagina_Usuarios(QWidget):
    def __init__(self,main_window,btn_abrir_planilha_usuarios,btn_cadastrar_novo_usuario,btn_gerar_pdf_usuario,
                  btn_historico_usuarios,btn_atualizar_ativos,btn_atualizar_inativos,btn_limpar_tabelas_usuarios,
                  btn_gerar_saida_usuarios,btn_cadastrar_todos,parent=None):
        super().__init__(parent)

        self.db = DataBase("banco_de_dados.db")
        self.alteracoes_salvas = False

        self.tabela_historico_usuarios = QTableWidget()  # A tabela que você está usando
        self.checkboxes = []  # Lista para armazenar os checkboxes
        self.coluna_checkboxes_adicionada = False
        self.todos_selecionados = False
        
        

        self.main_window = main_window
        self.table_ativos = self.main_window.table_ativos  # Referência para a tabela no main window
        self.table_inativos = self.main_window.table_inativos
        self.btn_abrir_planilha_usuarios = btn_abrir_planilha_usuarios
        self.btn_cadastrar_novo_usuario = btn_cadastrar_novo_usuario
        self.btn_gerar_pdf_usuario = btn_gerar_pdf_usuario
        self.btn_historico_usuarios = btn_historico_usuarios
        self.btn_atualizar_ativos = btn_atualizar_ativos
        self.btn_atualizar_inativos = btn_atualizar_inativos
        self.btn_limpar_tabelas_usuarios = btn_limpar_tabelas_usuarios
        self.btn_gerar_saida_usuarios = btn_gerar_saida_usuarios
        self.btn_cadastrar_todos = btn_cadastrar_todos
        

        self.btn_gerar_saida_usuarios.clicked.connect(self.confirmar_saida_usuarios)
        self.btn_limpar_tabelas_usuarios.clicked.connect(self.limpar_tabelas)
        self.btn_atualizar_ativos.clicked.connect(self.atualizar_ativos)
        self.btn_atualizar_inativos.clicked.connect(self.atualizar_inativos)
        self.btn_cadastrar_todos.clicked.connect(self.cadastrar_em_massa)


    # Função auxiliar para criar um QTableWidgetItem com texto centralizado
    def formatar_texto(self, text):
        item = QTableWidgetItem(text)
        item.setTextAlignment(Qt.AlignCenter)  # Centraliza o texto
        item.setForeground(QBrush(QColor("white"))) 
        return item

    def tabela_ativos(self):
        cn = sqlite3.connect("banco_de_dados.db")

        # Carregar dados da tabela users usando pandas
        query = """
        SELECT Nome,Usuário,Senha,"Confirmar Senha",Acesso,Endereço,CEP,CPF,Número,Estado,Email,RG,Complemento,
        Telefone,Data_Nascimento,"Última Troca de Senha","Data da Senha Cadastrada","Data da Inclusão do Usuário",Secret
        FROM users
        """
        df = pd.read_sql_query(query, cn)

        # Verificando se há dados na consulta
        if df.empty:
            print("Nenhum dado encontrado no banco de dados 'users'")
            return
        
        # Configurando cabeçalhos das colunas
        numero_colunas = len(df.columns)
        self.table_ativos.setRowCount(len(df))
        self.table_ativos.setColumnCount(numero_colunas)

    
       # Limpando o QTableWidget antes de popular com novos dados
        self.table_ativos.clearContents()
        self.table_ativos.setRowCount(0)  # Certificando  que as linhas estão limpas 

        for row_index, row_data in df.iterrows():
            self.table_ativos.insertRow(row_index)
            for col_index, data in enumerate(row_data):
                item = self.formatar_texto(str(data))
                self.table_ativos.setItem(row_index,col_index,item)


    def tabela_inativos(self, usuarios_selecionados):
        # Limpa a tabela de saída antes de preencher com novos dados
        self.main_window.table_ativos.clearContents()
        self.main_window.table_ativos.setRowCount(0)

        if not usuarios_selecionados:
            QMessageBox.critical(self.main_window, "Aviso", "Nenhum usuário selecionado para gerar saída!")
            return False

        # Preenche a table_inativos com os dados dos usuários selecionados
        for row_index, row in enumerate(usuarios_selecionados):
            self.main_window.table_ativos.insertRow(row_index)

            # Nome
            nome = self.main_window.table_ativos.item(row, 0)
            if nome:
                self.main_window.table_ativos.setItem(row_index, 0, self.formatar_texto(nome.text()))

            # Usuário
            usuario = self.main_window.table_ativos.item(row, 1)
            if usuario:
                self.main_window.table_ativos.setItem(row_index, 1, self.formatar_texto(usuario.text()))

            # Senha
            senha = self.main_window.table_ativos.item(row, 2)
            if senha:
                self.main_window.table_ativos.setItem(row_index, 2, self.formatar_texto(senha.text()))

            # Confirmar Senha
            confirmar_senha = self.main_window.table_ativos.item(row, 3)
            if confirmar_senha:
                self.main_window.table_ativos.setItem(row_index, 3, self.formatar_texto(confirmar_senha.text()))

            # Acesso
            acesso = self.main_window.table_ativos.item(row, 4)
            if acesso:
                self.main_window.table_ativos.setItem(row_index, 4, self.formatar_texto(acesso.text()))

            # Endereço
            endereco = self.main_window.table_ativos.item(row, 5)
            if endereco:
                self.main_window.table_ativos.setItem(row_index, 5, self.formatar_texto(endereco.text()))

            # CEP
            cep = self.main_window.table_ativos.item(row, 6)
            if cep:
                self.main_window.table_ativos.setItem(row_index, 6, self.formatar_texto(cep.text()))

            # CPF
            cpf = self.main_window.table_ativos.item(row, 7)
            if cpf:
                self.main_window.table_ativos.setItem(row_index, 7, self.formatar_texto(cpf.text()))

            # Número
            numero = self.main_window.table_ativos.item(row, 8)
            if numero:
                self.main_window.table_ativos.setItem(row_index, 8, self.formatar_texto(numero.text()))

            # Estado
            estado = self.main_window.table_ativos.item(row, 9)
            if estado:
                self.main_window.table_ativos.setItem(row_index, 9, self.formatar_texto(estado.text()))

            # E-mail
            email = self.main_window.table_ativos.item(row, 10)
            if email:
                self.main_window.table_ativos.setItem(row_index, 10, self.formatar_texto(email.text()))

            # Complemento
            complemento = self.main_window.table_ativos.item(row, 11)
            if complemento:
                self.main_window.table_ativos.setItem(row_index, 11, self.formatar_texto(complemento.text()))

            # Telefone
            telefone = self.main_window.table_ativos.item(row, 12)
            if telefone:
                self.main_window.table_ativos.setItem(row_index, 12, self.formatar_texto(telefone.text()))

            # Data de Nascimento
            data_nascimento = self.main_window.table_ativos.item(row, 13)
            if data_nascimento:
                self.main_window.table_ativos.setItem(row_index, 13, self.formatar_texto(data_nascimento.text()))

            # RG
            rg = self.main_window.table_ativos.item(row, 14)
            if rg:
                self.main_window.table_ativos.setItem(row_index, 14, self.formatar_texto(rg.text()))

            # Última Troca de Senha
            ultima_troca_senha = self.main_window.table_ativos.item(row, 15)
            if ultima_troca_senha:
                self.main_window.table_ativos.setItem(row_index, 15, self.formatar_texto(ultima_troca_senha.text()))

            # Data da Senha Cadastrada
            data_senha_cadastrada = self.main_window.table_ativos.item(row, 16)
            if data_senha_cadastrada:
                self.main_window.table_ativos.setItem(row_index, 16, self.formatar_texto(data_senha_cadastrada.text()))

            # Data da Inclusão do Usuário
            data_inclusao_usuario = self.main_window.table_ativos.item(row, 17)
            if data_inclusao_usuario:
                self.main_window.table_ativos.setItem(row_index, 17, self.formatar_texto(data_inclusao_usuario.text()))

            # Data da Inatividade do Usuário
            data_inatividade_usuario = self.main_window.table_ativos.item(row, 18)
            if data_inatividade_usuario:
                self.main_window.table_ativos.setItem(row_index, 18, self.formatar_texto(data_inatividade_usuario.text()))

            # Segredo
            segredo = self.main_window.table_ativos.item(row, 19)
            if segredo:
                self.main_window.table_ativos.setItem(row_index, 19, self.formatar_texto(segredo.text()))

            # Usuário Logado
            usuario_logado = self.main_window.table_ativos.item(row, 20)
            if usuario_logado:
                self.main_window.table_ativos.setItem(row_index, 20, self.formatar_texto(usuario_logado.text()))

        return True
    
    def gerar_saida_usuarios(self, usuarios_selecionados):
        saida_usuarios = []
        historico_logs = []

        numero_usuarios = len(usuarios_selecionados)

        confirmar_saida, ok = QInputDialog.getText(
            self.main_window,
            "Confirmação de Saída",
            f"Você selecionou {numero_usuarios} usuários, tem certeza que deseja gerar a saída de todos eles?",
            QLineEdit.Normal,
            "Sim"
        )

        if not ok or confirmar_saida != "Sim":
            return

        for row in usuarios_selecionados:
            dados_usuario = []
            for coluna in range(21):
                item = self.main_window.table_ativos.item(row, coluna)
                dados_usuario.append(item.text() if item else "")
                print(f"Coluna {coluna}: {item}")

        
            dados_usuario[18] = datetime.now().strftime("%d/%m/%Y %H:%M")
            dados_usuario[19] = dados_usuario[19]
            dados_usuario[20] = dados_usuario[20]

            #print(f"Colunas do usuário: {len(dados_usuario)} → {dados_usuario}")

            saida_usuarios.append(tuple(dados_usuario))
            historico_logs.append(f"Usuário {dados_usuario[0]} gerado para saída.")

        for texto in historico_logs:
            self.main_window.registrar_historico("Gerado Saída de Usuário", texto)

        if saida_usuarios:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle("Aviso")
            msg_box.setText("Saída do(s) usuário(s) gerada com sucesso!")
            msg_box.exec()
            self.tabela_inativos_preencher(saida_usuarios)


    def tabela_inativos_preencher(self, dados_saida):
        for item in dados_saida:
            row_position = self.main_window.table_inativos.rowCount()
            self.main_window.table_inativos.insertRow(row_position)

            for col in range(21):
                if col < len(item):
                    self.main_window.table_inativos.setItem(row_position, col, self.formatar_texto(item[col]))

    def confirmar_saida_usuarios(self):
        # Verifica a linha diretamente selecionada pelo usuário
        selecionar_linhas = self.main_window.table_ativos.selectionModel().selectedRows()
        usuarios_selecionados = [row.row() for row in selecionar_linhas]

        # Verifica se existe uma linha selecionada diretamente pelo clique
        if usuarios_selecionados:
            mensagem = "Tem certeza de que deseja gerar a saída do usuário selecionado?"

            caixa_dialogo = QMessageBox()
            caixa_dialogo.setWindowTitle("Confirmar Saída")
            caixa_dialogo.setText(mensagem)
            caixa_dialogo.setIcon(QMessageBox.Question)
            caixa_dialogo.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            caixa_dialogo.setDefaultButton(QMessageBox.Yes)

            # Personalizando o texto dos botões
            botao_nao = caixa_dialogo.button(QMessageBox.No)
            botao_nao.setText("Não")
            botao_sim = caixa_dialogo.button(QMessageBox.Yes)
            botao_sim.setText("Sim")

            resposta = caixa_dialogo.exec()
            if resposta == QMessageBox.Yes:
                self.gerar_saida_usuarios(usuarios_selecionados)

        else:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle("Aviso")
            msg_box.setText("Nenhum usuário selecionado para gerar saída")
            msg_box.exec()

    




    def atualizar_ativos(self):
        try:
            # Limpar a tabela antes de atualizar
            self.table_ativos.setRowCount(0)  # Remove todas as linhas da tabela

            # Consultar todos os usuarios
            query = """
            SELECT Nome,Usuário,Senha,"Confirmar Senha",Acesso,Endereço,CEP,CPF,Número,Estado,Email,RG,Complemento,
            Telefone,Data_Nascimento,"Última Troca de Senha","Data da Senha Cadastrada","Data da Inclusão do Usuário",Secret,"Usuário Logado"
            FROM users
            """
            usuarios = self.db.executar_query(query)

            for linha_index, linha_data in enumerate(usuarios):
                self.table_ativos.insertRow(linha_index)
                for col, value in enumerate(linha_data):
                    item = self.formatar_texto(str(value))
                    self.table_ativos.setItem(linha_index, col, item)

            # Exibir uma mensagem de sucesso
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle("Informação")
            msg_box.setText("Tabela ativos atualizada com sucesso!")       
            msg_box.exec()

        except Exception as e:
            print(f"Erro ao atualizar a tabela de ativos: {e}")

            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle("Informação")
            msg_box.setText("Tabela ativos atualizada com sucesso!")       
            msg_box.exec()


        except Exception as e:
            print(f"Erro ao atualizar a tabela de ativos: {e}")


    def atualizar_inativos(self):
        try:
            # Limpa a tabela antes de carregar os novos dados
            self.table_inativos_usuarios.setRowCount(0)
            
            # Consulta os dados da tabela de saída no banco de dados (somente usuarios que já tiveram saída gerada)
            query = """
            SELECT Nome,Usuário,Senha,"Confirmar Senha",Acesso,Endereço,CEP,CPF,Número,Estado,Email,RG,Complemento,
            Telefone,Data_Nascimento,"Última Troca de Senha","Data da Senha Cadastrada","Data da Inclusão do Usuário",Secret,"Usuário Logado"
            FROM users
            """
            saidas = self.db.executar_query(query)  # Método que executa a consulta e retorna os resultados

            # Preenche a tabela com os dados obtidos
            if saidas:
                for saida in saidas:
                    row_position = self.table_inativos_usuarios.rowCount()
                    self.table_inativos_usuarios.insertRow(row_position)
                    for column, value in enumerate(saida):
                        item = self.reaplicar_formatacao_tabela(str(value))
                        self.table_inativos_usuarios.setItem(row_position, column, item)
                        
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle("Informação")
            msg_box.setText("Tabela inativos atualizada com sucesso!")       
            msg_box.exec()

        except Exception as e:
            print(f"Erro ao atualizar a tabela de inativos: {e}")


    def importar(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("ERRO")
        msg.setText("Ação ainda não está disponível!")
        msg.exec()

    def reaplicar_formatacao_tabela(self, tabela):
        # Define o número de colunas
        colunas = tabela.columnCount()
        
        # Para cada linha e coluna da tabela, aplique o estilo desejado
        for row in range(tabela.rowCount()):
            for col in range(colunas):
                # Centraliza e define o texto branco para cada célula
                item = self.criar_item('')
                tabela.setItem(row, col, item)


    def limpar_tabelas(self):
        # Verifica se as tabelas estão vazias
        if self.table_inativos_usuarios.rowCount() == 0 and self.table_ativos_usuarios.rowCount() == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Aviso")
            msg.setText("As tabelas já estão vazias.")
            msg.exec()
            return

        # Limpa a tabela de ativos (table_ativos_usuarios)
        self.table_ativos_usuarios.setRowCount(0)
        self.reaplicar_formatacao_tabela(self.table_ativos_usuarios)

        # Limpa a tabela de saída (table_inativos_usuarios)
        self.table_inativos_usuarios.setRowCount(0)
        self.reaplicar_formatacao_tabela(self.table_inativos_usuarios)

        # Mensagem de confirmação após a limpeza
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Limpeza Concluída")
        msg.setText("As tabelas foram limpas com sucesso.")
        msg.exec()

    
    def cadastrar_em_massa(self):
        pass