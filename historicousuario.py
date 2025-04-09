from PySide6.QtWidgets import QWidget,QTableWidget,QMessageBox,QTableWidgetItem
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
                  btn_incluir_usuarios_sistema,btn_salvar_tables_usuarios,btn_gerar_saida_usuarios,parent=None):
        super().__init__(parent)

        self.db = DataBase("banco_de_dados.db")
        self.alteracoes_salvas = False

        self.tabela_historico_usuarios = QTableWidget()  # A tabela que você está usando
        self.checkboxes = []  # Lista para armazenar os checkboxes
        self.coluna_checkboxes_adicionada = False
        self.todos_selecionados = False

        

        self.main_window = main_window
        self.table_ativos_usuarios = self.main_window.table_ativos  # Referência para a tabela no main window
        self.table_inativos_usuarios = self.main_window.table_inativos
        self.btn_abrir_planilha_usuarios = btn_abrir_planilha_usuarios
        self.btn_cadastrar_novo_usuario = btn_cadastrar_novo_usuario
        self.btn_gerar_pdf_usuario = btn_gerar_pdf_usuario
        self.btn_historico_usuarios = btn_historico_usuarios
        self.btn_atualizar_ativos = btn_atualizar_ativos
        self.btn_atualizar_inativos = btn_atualizar_inativos
        self.btn_limpar_tabelas_usuarios = btn_limpar_tabelas_usuarios
        self.btn_incluir_usuarios_sistema = btn_incluir_usuarios_sistema
        self.btn_salvar_tables_usuarios = btn_salvar_tables_usuarios
        self.btn_gerar_saida_usuarios = btn_gerar_saida_usuarios

        self.tabela_ativos()
        
        #self.btn_gerar_pdf_usuario.clicked.connect(self.exibir_pdf_usuarios)
        #self.btn_gerar_estorno_usuarios.clicked.connect(self.criar_estorno_usuarios)
        self.btn_gerar_saida_usuarios.clicked.connect(self.confirmar_saida_usuarios)
        #self.btn_limpar_tabelas_usuarios.clicked.connect(self.limpar_tabela_usuarios)
        #self.btn_salvar_tables_usuarios.clicked.connect(self.salvar_tabelas_usuarios)
        #self.btn_atualizar_ativos.clicked.connect(self.atualizar_ativos)
        #self.btn_atualizar_inativos.clicked.connect(self.atualizar_inativos)
        #self.btn_historico_usuarios.clicked.connect(self.exibir_historico_usuarios)    
        #self.btn_incluir_usuarios_sistema.clicked.connect(self.incluir_usuario_no_sistema)
        #self.btn_abrir_planilha_usuarios.clicked.connect(self.abrir_planilha_usuarios)

    # Função auxiliar para criar um QTableWidgetItem com texto centralizado
    def formatar_texto(self, text):
        item = QTableWidgetItem(text)
        item.setTextAlignment(Qt.AlignCenter)  # Centraliza o texto
        item.setForeground(QBrush(QColor("white"))) 
        return item

    def tabela_ativos(self):
        cn = sqlite3.connect("banco_de_dados.db")

        query = """
        SELECT Nome,Usuário,Senha,"Confirmar Senha",Acesso,Endereço,CEP,CPF,Número,Estado,Email,RG,Complemento,
        Telefone,Data_Nascimento,"Última Troca de Senha","Data da Senha Cadastrada","Data da Inclusão do Usuário",Secret,"Usuário Logado"
        FROM users
        """
        df = pd.read_sql_query(query, cn)
        cn.close()

        if df.empty:
            QMessageBox.warning(self, "ERRO", "Nenhum dado encontrado no banco de dados 'users'")
            return

        numero_colunas = len(df.columns)
        self.table_ativos_usuarios.setRowCount(len(df))
        self.table_ativos_usuarios.setColumnCount(numero_colunas)

        coluna_ativos = [
            "Nome", "Usuário", "Senha", "Confirmar Senha","Acesso", "Endereço", "CEP", "CPF", "Número",
            "Estado", "Email", "RG", "Complemento", "Telefone", "Data de Nascimento",
            "Última Troca de Senha", "Data da Senha Cadastrada", "Data da Inclusão do Usuário", "Segredo","Usuário Logado"
        ]
        self.table_ativos_usuarios.setHorizontalHeaderLabels(coluna_ativos)
        self.table_ativos_usuarios.setRowCount(0)   

        for row_index, row_data in df.iterrows():
            self.table_ativos_usuarios.insertRow(row_index)
            for col_index, data in enumerate(row_data):
                item = self.formatar_texto(str(data))
                self.table_ativos_usuarios.setItem(row_index,col_index,item)

        for col in range(numero_colunas):
            self.table_ativos_usuarios.resizeColumnToContents(col)


    def tabela_inativos(self, usuarios_selecionados):
        linha_inicial = self.table_inativos_usuarios.rowCount()

        coluna_inativos = [
            "Nome", "Usuário", "Senha", "Confirmar Senha", "Acesso", "Endereço", "CEP", "CPF", "Número",
            "Estado", "Email", "RG", "Complemento", "Telefone", "Data de Nascimento",
            "Última Troca de Senha", "Data da Senha Cadastrada", "Data da Inclusão do Usuário",
            "Data da Inatividade do Usuário", "Segredo", "Usuário Logado"
        ]

        self.table_inativos_usuarios.setColumnCount(len(coluna_inativos))
        self.table_inativos_usuarios.setHorizontalHeaderLabels(coluna_inativos)

        if not usuarios_selecionados:
            QMessageBox.critical(self, "Aviso", "Nenhum usuário selecionado para gerar saída!")
            return False

        for i, row_index in enumerate(usuarios_selecionados):
            nova_linha = linha_inicial + i
            self.table_inativos_usuarios.insertRow(nova_linha)

            # Coleta cada campo, tratando caso esteja vazio
            for col_index in range(len(coluna_inativos)):
                item = self.table_ativos_usuarios.item(row_index, col_index)
                texto = item.text() if item and item.text().strip() else "Não Cadastrado"
                self.table_inativos_usuarios.setItem(nova_linha, col_index, self.formatar_texto(texto))

            # Define a data de inatividade do usuário
            data_hoje = datetime.today().strftime("%d/%m/%Y")
            self.table_inativos_usuarios.setItem(nova_linha, 18, self.formatar_texto(data_hoje))  # Data da Inatividade

            col_segredo = 19
            segredo_usuario = self.table_ativos_usuarios.item(row_index,col_segredo)
            usuario_texto = segredo_usuario.text() if segredo_usuario and segredo_usuario.text().strip() else "Não Cadastrado"
            self.table_inativos_usuarios.setItem(nova_linha, col_segredo, self.formatar_texto(usuario_texto))

            col_usuario_logado = 20
            item_logado = self.table_ativos_usuarios.item(row_index,col_usuario_logado)
            texto_logado = item_logado.text() if item_logado and item_logado.text().strip() else "Não Cadastrado"
            self.table_inativos_usuarios.setItem(nova_linha, col_usuario_logado, self.formatar_texto(texto_logado))

            

        # Ajusta o tamanho das colunas
        for col in range(len(coluna_inativos)):
            self.table_inativos_usuarios.resizeColumnToContents(col)

        return True





    def confirmar_saida_usuarios(self):
        selecionar_linhas = self.table_ativos_usuarios.selectionModel().selectedRows()
        usuarios_selecionados = [row.row() for row in selecionar_linhas]

        if not usuarios_selecionados:
            QMessageBox.information(self, "Aviso", "Nenhum usuário selecionado para tornar inativo")
            return
        
        # Define a mensagem com base na quantidade de usuários
        if len(usuarios_selecionados) == 1:
            mensagem = "Tem certeza de que deseja tornar o usuário inativo?"
        else:
            mensagem = "Tem certeza de que deseja tornar os usuários inativos?"

        # Cria uma caixa de diálogo personalizada
        caixa_dialogo = QMessageBox(self)
        caixa_dialogo.setIcon(QMessageBox.Question)
        caixa_dialogo.setWindowTitle("Confirmar Inatividade")
        caixa_dialogo.setText(mensagem)
        caixa_dialogo.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        # Personaliza os botões
        botao_sim = caixa_dialogo.button(QMessageBox.Yes)
        botao_sim.setText("Sim")
        botao_nao = caixa_dialogo.button(QMessageBox.No)
        botao_nao.setText("Não")

        # Mostra a caixa de diálogo
        resposta = caixa_dialogo.exec()

        if resposta == QMessageBox.Yes:
            self.tabela_inativos(usuarios_selecionados)
