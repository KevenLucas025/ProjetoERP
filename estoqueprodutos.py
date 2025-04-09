from PySide6.QtGui import QColor, QBrush,QGuiApplication
from PySide6.QtWidgets import (QWidget, QTableWidget, QTableWidgetItem, 
                               QMessageBox,QCheckBox,QVBoxLayout,QDialog,QPushButton,QMainWindow,QHBoxLayout,
                               QLineEdit,QLabel,QInputDialog,QGroupBox,QRadioButton,QFileDialog)
from PySide6.QtCore import Qt,QRegularExpression
import sqlite3
import pandas as pd
from datetime import datetime
from database import DataBase
import csv
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter,landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle


class EstoqueProduto(QWidget):
    def __init__(self, main_window, btn_gerar_pdf, btn_gerar_estorno, 
                 btn_gerar_saida, btn_limpar_tabela, btn_salvar_tables, btn_atualizar_saida, btn_atualizar_estoque, btn_historico,
                  btn_incluir_no_sistema,btn_abrir_planilha,parent=None):
        super().__init__(parent)

        self.db = DataBase("banco_de_dados.db")
        self.alteracoes_salvas = False

        self.tabela_historico = QTableWidget()  # A tabela que você está usando
        self.checkboxes = []  # Lista para armazenar os checkboxes
        self.coluna_checkboxes_adicionada = False
        self.todos_selecionados = False


        self.main_window = main_window
        self.table_base = self.main_window.table_base  # Referência para a tabela no main window
        self.table_saida = self.main_window.table_saida
        self.btn_gerar_pdf = btn_gerar_pdf
        self.btn_gerar_estorno = btn_gerar_estorno
        self.btn_gerar_saida = btn_gerar_saida
        self.btn_limpar_tabela = btn_limpar_tabela
        self.btn_salvar_tables = btn_salvar_tables
        self.btn_atualizar_saida = btn_atualizar_saida
        self.btn_atualizar_estoque = btn_atualizar_estoque
        self.btn_historico = btn_historico
        self.btn_incluir_no_sistema = btn_incluir_no_sistema
        self.btn_abrir_planilha = btn_abrir_planilha

        self.btn_gerar_pdf.clicked.connect(self.exibir_pdf)
        self.btn_gerar_estorno.clicked.connect(self.criar_estorno)
        self.btn_gerar_saida.clicked.connect(self.confirmar_saida)
        self.btn_limpar_tabela.clicked.connect(self.limpar_tabela)
        self.btn_salvar_tables.clicked.connect(self.salvar_tabelas)
        self.btn_atualizar_saida.clicked.connect(self.atualizar_saida)
        self.btn_atualizar_estoque.clicked.connect(self.atualizar_estoque)
        self.btn_historico.clicked.connect(self.exibir_historico)    
        self.btn_incluir_no_sistema.clicked.connect(self.incluir_sistema)
        self.btn_abrir_planilha.clicked.connect(self.abrir_planilha)


    # Função auxiliar para criar um QTableWidgetItem com texto centralizado
    def criar_item(self, text):
        item = QTableWidgetItem(text)
        item.setTextAlignment(Qt.AlignCenter)  # Centraliza o texto
        item.setForeground(QBrush(QColor("white"))) 
        return item

    def tabela_estoque(self):
        # Conectando ao banco de dados SQLite
        cn = sqlite3.connect("banco_de_dados.db")
        
        # Carregar dados da tabela "products" usando pandas
        query = """
        SELECT Produto, Quantidade, Valor_Real, IFNULL(Desconto, 'Sem Desconto') AS Desconto, Data_Compra, Código_Item, Cliente, Descrição_Produto, Usuário
        FROM products
        """
        df = pd.read_sql_query(query, cn)
        cn.close()

        # Verificando se há dados na consulta
        if df.empty:
            print("Nenhum dado encontrado no banco de dados.")
            return

        # Configurando cabeçalhos das colunas
        num_columns = len(df.columns)
        self.table_base.setRowCount(len(df))
        self.table_base.setColumnCount(num_columns)
        
        # Definindo cabeçalhos das colunas na ordem desejada
        coluna_estoque = [
            "Produto", 
            "Quantidade", 
            "Valor do Produto", 
            "Desconto", 
            "Data da Compra", 
            "Código do Produto", 
            "Cliente", 
            "Descrição do Produto",
            "Usuário"  # Coluna Usuário na ordem correta
        ]
        self.table_base.setHorizontalHeaderLabels(coluna_estoque)

        # Limpando o QTableWidget antes de popular com novos dados
        #self.table_base.clearContents()
        self.table_base.setRowCount(0)  # Certifique-se de que as linhas estão limpas

        # Iterando sobre os dados do DataFrame e adicionando-os ao QTableWidget
        for row_index, row_data in df.iterrows():
            self.table_base.insertRow(row_index)  # Inserir nova linha
            for col_index, data in enumerate(row_data):
                item = self.criar_item(str(data))  # Usando a função auxiliar
                
                # Adicionando o item à QTableWidget
                self.table_base.setItem(row_index, col_index, item)

        # Ajustar o tamanho das colunas para se ajustar ao conteúdo
        for col in range(num_columns):
            self.table_base.resizeColumnToContents(col)

    def tabela_saida(self, produtos_selecionados):
        # Limpa a tabela de saída antes de preencher com novos dados
        self.main_window.table_saida.clearContents()
        self.main_window.table_saida.setRowCount(0)

        # Define as colunas para a table_saida
        colunas_saida = [
            "Produto", 
            "Quantidade",
            "Valor do Produto",
            "Desconto", 
            "Data de Saída", 
            "Data da Criação", 
            "Código do Produto", 
            "Cliente", 
            "Descrição do Produto", 
            "Usuário"
        ]
        self.main_window.table_saida.setColumnCount(len(colunas_saida))
        self.main_window.table_saida.setHorizontalHeaderLabels(colunas_saida)

        # Verifica se há produtos selecionados para a saída
        if not produtos_selecionados:
            QMessageBox.critical(self.main_window, "Aviso", "Nenhum produto selecionado para gerar saída!")
            return False

        # Preenche a table_saida com os dados dos produtos selecionados
        for row_index, row in enumerate(produtos_selecionados):
            self.main_window.table_saida.insertRow(row_index)
            
            # Produto
            produto_item = self.main_window.table_base.item(row, 0)
            if produto_item:
                self.main_window.table_saida.setItem(row_index, 0, self.criar_item(produto_item.text()))
            
            # Quantidade
            quantidade_item = self.main_window.table_base.item(row, 1)
            if quantidade_item:
                self.main_window.table_saida.setItem(row_index, 1, self.criar_item(quantidade_item.text()))

            # Valor do Produto
            valor_produto_item = self.main_window.table_base.item(row, 2)
            if valor_produto_item:
                self.main_window.table_saida.setItem(row_index, 2, self.criar_item(valor_produto_item.text()))

            # Desconto
            desconto_item = self.main_window.table_base.item(row, 3)
            if desconto_item:
                self.main_window.table_saida.setItem(row_index, 3, self.criar_item(desconto_item.text()))

            # Data de Saída (data atual)
            data_saida = datetime.now().strftime("%d/%m/%Y %H:%M")
            self.main_window.table_saida.setItem(row_index, 4, self.criar_item(data_saida))

            # Data da Criação (Data da Compra)
            data_criacao_item = self.main_window.table_base.item(row, 4)
            if data_criacao_item:
                self.main_window.table_saida.setItem(row_index, 5, self.criar_item(data_criacao_item.text()))

            # Código do Produto
            codigo_item = self.main_window.table_base.item(row, 5)
            if codigo_item:
                self.main_window.table_saida.setItem(row_index, 6, self.criar_item(codigo_item.text()))

            # Cliente
            cliente_item = self.main_window.table_base.item(row, 6)
            if cliente_item:
                self.main_window.table_saida.setItem(row_index, 7, self.criar_item(cliente_item.text()))

            # Descrição do Produto
            descricao_item = self.main_window.table_base.item(row, 7)
            if descricao_item:
                self.main_window.table_saida.setItem(row_index, 8, self.criar_item(descricao_item.text()))

            # Usuário
            usuario_item = self.main_window.table_base.item(row, 8)
            if usuario_item:
                self.main_window.table_saida.setItem(row_index, 9, self.criar_item(usuario_item.text()))

        # Ajusta o tamanho das colunas para o conteúdo
        for col in range(len(colunas_saida)):
            self.main_window.table_saida.resizeColumnToContents(col)

        return True



    def confirmar_saida(self):
        # Verifica a linha diretamente selecionada pelo usuário
        selected_rows = self.main_window.table_base.selectionModel().selectedRows()
        produtos_selecionados = [row.row() for row in selected_rows]

        # Verifica se existe uma linha selecionada diretamente pelo clique
        if produtos_selecionados:
            mensagem = "Tem certeza de que deseja gerar a saída do produto selecionado?"

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
                self.gerar_saida(produtos_selecionados)

        else:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle("Aviso")
            msg_box.setText("Nenhum produto selecionado para gerar saída")
            msg_box.exec()

    def gerar_saida(self, produtos_selecionados):
        if not self.tabela_saida(produtos_selecionados):
            return  # Não prossegue se não houver dados

        produtos_saida = []

        for row in produtos_selecionados:
            produto = self.main_window.table_base.item(row, 0).text() if self.main_window.table_base.item(row, 0) else ""
            quantidade = self.main_window.table_base.item(row, 1).text() if self.main_window.table_base.item(row, 1) else ""
            valor_produto = self.main_window.table_base.item(row, 2).text() if self.main_window.table_base.item(row, 2) else ""
            desconto = self.main_window.table_base.item(row, 3).text() if self.main_window.table_base.item(row, 3) else ""
            data_criacao = self.main_window.table_base.item(row, 4).text() if self.main_window.table_base.item(row, 4) else ""
            codigo_produto = self.main_window.table_base.item(row, 5).text() if self.main_window.table_base.item(row, 5) else ""
            cliente = self.main_window.table_base.item(row, 6).text() if self.main_window.table_base.item(row, 6) else ""
            descricao = self.main_window.table_base.item(row, 7).text() if self.main_window.table_base.item(row, 7) else ""
            usuario = self.main_window.table_base.item(row, 8).text() if self.main_window.table_base.item(row, 8) else ""
            imagem = self.recuperar_imagem_produto_bd_products(codigo_produto)

            status_item = self.main_window.table_base.item(row, 9)
            status = status_item.text() if status_item else "Inativo"
            status_saida = "1"

            data_saida = datetime.now().strftime("%d/%m/%Y %H:%M")

            produtos_saida.append((produto, quantidade, valor_produto, desconto, data_saida, data_criacao, codigo_produto, cliente, descricao, usuario, imagem, status, status_saida))

        with sqlite3.connect("banco_de_dados.db") as cn:
            cursor = cn.cursor()

            cursor.executemany("""
                INSERT INTO products_saida (Produto, Quantidade, 'Valor do Produto', Desconto, 'Data de Saída', 'Data da Criação', 'Código do Produto', Cliente, 'Descrição do Produto', Usuário, Imagem, Status, 'Status da Saída')
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, produtos_saida)

            for produto in produtos_saida:
                codigo_produto = produto[6]
                cursor.execute("DELETE FROM products WHERE Código_Item = ?", (codigo_produto,))

            cn.commit()

        # Remove a linha da tabela `table_base` na interface
        for row in sorted(produtos_selecionados, reverse=True):
            self.main_window.table_base.removeRow(row)

            # Registrar no histórico após a inserção do produto
            descricao = f"Produto {produto[0]} foi gerado saída."
            self.main_window.registrar_historico("Gerado Saída", descricao)

        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("Aviso")
        msg_box.setText("Saída do produto gerada com sucesso!")
        msg_box.exec()

        # Reindexar as linhas da `table_base` para manter ordem crescente
        self.reindex_table_base()

    def reindex_table_base(self):
        row_count = self.main_window.table_base.rowCount()
        for row in range(row_count):
            item = QTableWidgetItem(str(row + 1))
            self.main_window.table_base.setVerticalHeaderItem(row, item)


    # Função para recuperar imagem de um produto com base no código do produto
    def recuperar_imagem_produto_bd_products(self, codigo_produto):
        conexao = sqlite3.connect('banco_de_dados.db')
        cursor = conexao.cursor()
        cursor.execute("SELECT Imagem FROM products WHERE Código_Item = ?", (codigo_produto,))
        
        resultado = cursor.fetchone()  # Tenta buscar uma linha
        
        if resultado is not None:
            imagem_blob = resultado[0]  # Recupera a imagem se o resultado não for None
        else:
            imagem_blob = None  # Define como None se a imagem não for encontrada
        
        conexao.close()
        return imagem_blob



    def criar_estorno(self):
        selected_rows = self.main_window.table_base.selectionModel().selectedRows()
        produtos_selecionados = [row.row() for row in selected_rows]
        # Obtém o número de linhas na table_saida
        row_count = self.main_window.table_saida.rowCount()

        # Exibe uma mensagem de erro se não houver dados
        if row_count == 0:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("ERRO")
            msg_box.setText("Não há nenhum dado disponível na tabela para gerar estorno!")
            msg_box.exec()
            return  # Evitar continuar o estorno se não houver dados

        # Se há dados, continue com o estorno
        for row in range(row_count):
            self.main_window.table_base.insertRow(self.main_window.table_base.rowCount())
            row_base = self.main_window.table_base.rowCount() - 1

            # Produto (coluna 0)
            produto_item = self.main_window.table_saida.item(row, 0)
            produto = produto_item.text() if produto_item else ""
            self.main_window.table_base.setItem(row_base, 0, self.criar_item(produto))

            # Quantidade (coluna 1)
            quantidade_item = self.main_window.table_saida.item(row, 1)
            quantidade = quantidade_item.text() if quantidade_item else ""
            self.main_window.table_base.setItem(row_base, 1, self.criar_item(quantidade))

            # Valor Real (coluna 2)
            valor_real_item = self.main_window.table_saida.item(row, 2)
            valor_real = valor_real_item.text() if valor_real_item else ""
            self.main_window.table_base.setItem(row_base, 2, self.criar_item(valor_real))

            # Desconto (coluna 3)
            desconto_item = self.main_window.table_saida.item(row, 3)
            desconto = desconto_item.text() if desconto_item else ""
            self.main_window.table_base.setItem(row_base, 3, self.criar_item(desconto))

            # Data da Compra (coluna 4)
            data_compra_item = self.main_window.table_saida.item(row, 5)  # Corrigido para pegar a data correta
            data_compra = data_compra_item.text() if data_compra_item else ""
            self.main_window.table_base.setItem(row_base, 4, self.criar_item(data_compra))

            # Código do Produto (coluna 5)
            codigo_item = self.main_window.table_saida.item(row, 6)
            codigo_produto = codigo_item.text() if codigo_item else ""
            self.main_window.table_base.setItem(row_base, 5, self.criar_item(codigo_produto))

            # Cliente (coluna 6)
            cliente_item = self.main_window.table_saida.item(row, 7)
            cliente = cliente_item.text() if cliente_item else ""
            self.main_window.table_base.setItem(row_base, 6, self.criar_item(cliente))

            # Descrição do Produto (coluna 7)
            descricao_item = self.main_window.table_saida.item(row, 8)
            descricao = descricao_item.text() if descricao_item else ""
            self.main_window.table_base.setItem(row_base, 7, self.criar_item(descricao))

            # Usuário (coluna 8)
            # Ajusta o valor do usuário para o que fez o estorno (administrador, por exemplo)
            usuario = "admin"  # Aqui você pode alterar para pegar o usuário logado, se houver
            self.main_window.table_base.setItem(row_base, 8, self.criar_item(usuario))

            # Imagem do produto (recuperar do banco de dados)
            imagem = self.recuperar_imagem_produto_bd_products_saida(codigo_produto)

            # Status da Saída (coluna 9)
            status_da_saida = "1"

            # Inserir o produto de volta na tabela `products` com o status "Ativo"
            with sqlite3.connect("banco_de_dados.db") as cn:
                cursor = cn.cursor()

                # Inserir o produto de volta na tabela products
                cursor.execute("""
                    INSERT INTO products (Produto, Quantidade, Valor_Real, Desconto, Data_Compra, Código_Item, Cliente, Descrição_Produto, Imagem, Usuário, Status, 'Status da Saída')
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'Ativo', ?)
                """, (produto, quantidade, valor_real, desconto, data_compra, codigo_produto, cliente, descricao, imagem, usuario, status_da_saida))

                cn.commit()

                try:
                    cursor.execute("""
                        DELETE FROM products_saida WHERE "Código do Produto" = ?
                    """, (codigo_produto,))
                    cn.commit()
                except sqlite3.Error as e:
                    print(f"Erro ao excluir o produto: {e}")
                    cn.rollback()

                # Registrar no histórico após a inserção do produto
                descricao = f"Produto {produto} foi estornado."
                self.main_window.registrar_historico("Estorno do Produto", descricao)

        # Limpa a tabela de saída
        self.main_window.table_saida.clearContents()
        self.main_window.table_saida.setRowCount(0)

        # Mensagem de sucesso
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("Sucesso")
        msg_box.setText("Estorno realizado com sucesso")
        msg_box.exec()

    # Função para recuperar a imagem do produto pelo código (recupera a imagem do banco de dados)
    def recuperar_imagem_produto_bd_products_saida(self, codigo_produto):
        try:
            with sqlite3.connect('banco_de_dados.db') as conexao:
                cursor = conexao.cursor()
                # Corrigir se necessário o nome da coluna
                cursor.execute("SELECT Imagem FROM products_saida WHERE `Código do Produto` = ?", (codigo_produto,))
                resultado = cursor.fetchone()

                # Verifica se a imagem foi encontrada, caso contrário retorna uma string vazia
                if resultado:
                    return resultado[0]  # Retorna a imagem (blob ou caminho da imagem)
                else:   
                    return ""  # Retorna uma string vazia se não encontrar a imagem

        except sqlite3.Error as e:
            print(f"Erro ao recuperar imagem do banco de dados: {e}")
            return ""  # Em caso de erro, retorna uma string vazia


    def limpar_valor(self, valor):
        # Remove o símbolo 'R$' e espaços e converte para float
        return float(valor.replace('R$', '').replace('.', '').replace(',', '.').strip())
    
    def marcar_alteracao(self):
        # Método para marcar quando ocorre uma alteração
        self.alteracoes_salvas = False

    def salvar_tabelas(self):
        if self.alteracoes_salvas:
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setWindowTitle("Informação ")
                msg_box.setText("Alterações já foram salvas ")
                msg_box.exec()
                return 
        try:
            # Criar conexão e cursor
            conexao = sqlite3.connect('banco_de_dados.db')
            cursor = conexao.cursor()

            # Salvando as alterações na table_base (estoque)
            for row in range(self.main_window.table_base.rowCount()):
                if all(self.main_window.table_base.item(row, col) is not None for col in range(10)):  # Verificar se todos os itens da linha existem
                    produto = self.main_window.table_base.item(row, 0).text() if self.main_window.table_base.item(row, 0) else ""
                    quantidade = int(self.main_window.table_base.item(row, 1).text()) if self.main_window.table_base.item(row, 1) else 0
                    valor_produto = self.limpar_valor(self.main_window.table_base.item(row, 2).text()) if self.main_window.table_base.item(row, 2) else 0.0
                    desconto = self.main_window.table_base.item(row, 3).text() if self.main_window.table_base.item(row, 3) else ""
                    data_compra = self.main_window.table_base.item(row, 4).text() if self.main_window.table_base.item(row, 4) else ""
                    codigo_produto = self.main_window.table_base.item(row, 5).text() if self.main_window.table_base.item(row, 5) else ""
                    cliente = self.main_window.table_base.item(row, 6).text() if self.main_window.table_base.item(row, 6) else ""
                    descricao = self.main_window.table_base.item(row, 7).text() if self.main_window.table_base.item(row, 7) else ""
                    usuario = self.main_window.table_base.item(row, 8).text() if self.main_window.table_base.item(row, 8) else ""
                    status = self.main_window.table_base.item(row, 9).text() if self.main_window.table_base.item(row, 9) else ""
                    status_da_saida = self.main_window.table_base.item(row, 10).text() if self.main_window.table_base.item(row, 10) else ""

                    # Usar UPDATE para modificar dados existentes
                    cursor.execute("""
                        UPDATE products SET
                            Produto = ?, 
                            Quantidade = ?, 
                            Valor_Real = ?,
                            Desconto = ?,
                            Data_Compra = ?,
                            Código_Item = ?, 
                            Cliente = ?, 
                            Descrição_Produto = ?,
                            Usuário = ?, 
                            Status = ?,
                            'Status da Saída' = ?
                        WHERE Código_Item = ?
                    """, (produto, quantidade, valor_produto, desconto, data_compra, codigo_produto, cliente, descricao, usuario, status, status_da_saida, codigo_produto))

            # Salvando as alterações na table_saida (saída de produtos)
            for row in range(self.main_window.table_saida.rowCount()):
                if all(self.main_window.table_saida.item(row, col) is not None for col in range(12)):  # Verificar se todos os itens da linha existem
                    produto = self.main_window.table_saida.item(row, 0).text() if self.main_window.table_saida.item(row, 0) else ""
                    quantidade = int(self.main_window.table_saida.item(row, 1).text()) if self.main_window.table_saida.item(row, 1) else 0
                    valor_produto = self.main_window.table_saida.item(row, 2).text() if self.main_window.table_saida.item(row, 2) else ""
                    desconto = self.main_window.table_saida.item(row, 3).text() if self.main_window.table_saida.item(row, 3) else ""
                    data_saida = self.main_window.table_saida.item(row, 4).text() if self.main_window.table_saida.item(row, 4) else ""
                    data_criacao = self.main_window.table_saida.item(row, 5).text() if self.main_window.table_saida.item(row, 5) else ""
                    codigo_produto = self.main_window.table_saida.item(row, 6).text() if self.main_window.table_saida.item(row, 6) else ""
                    cliente = self.main_window.table_saida.item(row, 7).text() if self.main_window.table_saida.item(row, 7) else ""
                    descricao_produto = self.main_window.table_saida.item(row, 8).text() if self.main_window.table_saida.item(row, 8) else ""
                    usuario = self.main_window.table_saida.item(row, 9).text() if self.main_window.table_saida.item(row, 9) else ""
                    imagem = self.main_window.table_saida.item(row, 10).text() if self.main_window.table_saida.item(row, 10) else ""
                    status = self.main_window.table_saida.item(row, 11).text() if self.main_window.table_saida.item(row, 11) else ""
                    status_da_saida = self.main_window.table_saida.item(row, 12).text() if self.main_window.table_saida.item(row, 12) else ""

                    # Usar INSERT para novos registros ou UPDATE para registros existentes
                    cursor.execute("""
                        INSERT INTO products_saida (Produto, Quantidade, 'Valor do Produto', Desconto, 'Data de Saída', 'Data da Criação', 'Código do Produto', Cliente, 'Descrição do Produto', Usuário, Imagem, Status, 'Status da Saída')
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        ON CONFLICT(Código_do_Produto) DO UPDATE SET 
                            Quantidade = excluded.Quantidade,
                            'Data de Saída' = excluded.'Data de Saída',
                            Cliente = excluded.Cliente,
                            Descrição_Produto = excluded.Descrição_Produto,
                            Usuário = excluded.Usuário
                    """, (produto, quantidade, valor_produto, desconto, data_saida, data_criacao, codigo_produto, cliente, descricao_produto, usuario, imagem, status, status_da_saida))

            # Confirmar as alterações no banco de dados
            conexao.commit()
            conexao.close()

            # Marcar que as alterações foram salvas
            self.alteracoes_salvas = True    

            # Exibir uma mensagem de sucesso
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle("Sucesso ")
            msg_box.setText("Alterações salvas com sucesso ")
            msg_box.exec()
            return

        except Exception as e:
            print(f"Erro ao salvar tabelas: {e}")
            QMessageBox.critical(self.main_window, "Erro", f"Erro ao salvar tabelas: {e}")


    def atualizar_estoque(self):
        try:
            # Limpar a tabela antes de atualizar
            self.table_base.setRowCount(0)  # Remove todas as linhas da tabela

            # Consultar todos os produtos
            query = """
            SELECT Produto, Quantidade, Valor_Real, Desconto, Data_Compra, Código_Item, Cliente, Descrição_Produto, Usuário, "Status da Saída"
            FROM products
            """
            produtos = self.db.executar_query(query)

            # Consultar produtos com condições específicas
            query_condicional = """
            SELECT Produto, Quantidade, Valor_Real, Desconto, Data_Compra, Código_Item, Cliente, Descrição_Produto, Usuário 
            FROM products
            WHERE "Status da Saída" IS NULL OR "Status da Saída" = 0 OR "Status da Saída" = ''
            """
            produtos_condicional = self.db.executar_query(query_condicional)

            if produtos_condicional:
                for produto in produtos_condicional:
                    row_position = self.table_base.rowCount()
                    self.table_base.insertRow(row_position)  # Insere uma nova linha na tabela
                    for column, value in enumerate(produto):
                        item = self.criar_item(str(value))  # Cria o item com os dados
                        self.table_base.setItem(row_position, column, item)  # Define o item na posição correspondente
            else:
                print("Nenhum produto para adicionar.")

            # Exibir uma mensagem de sucesso
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle("Informação")
            msg_box.setText("Tabela estoque atualizada com sucesso!")       
            msg_box.exec()

        except Exception as e:
            print(f"Erro ao atualizar a tabela de estoque: {e}")

            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle("Informação")
            msg_box.setText("Tabela estoque atualizada com sucesso!")       
            msg_box.exec()


        except Exception as e:
            print(f"Erro ao atualizar a tabela de estoque: {e}")


    def atualizar_saida(self):
        try:
            # Limpa a tabela antes de carregar os novos dados
            self.table_saida.setRowCount(0)
            
            # Consulta os dados da tabela de saída no banco de dados (somente produtos que já tiveram saída gerada)
            query = """
            SELECT Produto, Quantidade, "Valor do Produto", Desconto, "Data de Saída", "Data da Criação", "Código do Produto", Cliente, "Descrição do Produto", Usuário, Imagem, Status, "Status da Saída"
            FROM products_saida
            WHERE "Status da Saída" = 1
            """
            saidas = self.db.executar_query(query)  # Método que executa a consulta e retorna os resultados

            # Preenche a tabela com os dados obtidos
            if saidas:
                for saida in saidas:
                    row_position = self.table_saida.rowCount()
                    self.table_saida.insertRow(row_position)
                    for column, value in enumerate(saida):
                        item = self.criar_item(str(value))
                        self.table_saida.setItem(row_position, column, item)
                        
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle("Informação")
            msg_box.setText("Tabela saída atualizada com sucesso!")       
            msg_box.exec()

        except Exception as e:
            print(f"Erro ao atualizar a tabela de saída: {e}")


    def importar(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("ERRO")
        msg.setText("1ção ainda não está disponível!")
        msg.exec()


    def limpar_tabela(self):
        # Verifica se as tabelas estão vazias
        if self.table_base.rowCount() == 0 and self.table_saida.rowCount() == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Aviso")
            msg.setText("As tabelas já estão vazias.")
            msg.exec()
            return

        # Limpa a tabela de estoque (table_base)
        self.table_base.setRowCount(0)
        self.reaplicar_formatacao_tabela(self.table_base)

        # Limpa a tabela de saída (table_saida)
        self.table_saida.setRowCount(0)
        self.reaplicar_formatacao_tabela(self.table_saida)

        # Mensagem de confirmação após a limpeza
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Limpeza Concluída")
        msg.setText("As tabelas foram limpas com sucesso.")
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

    def exibir_pdf(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("ERRO")
        msg.setText("Essa função ainda não está disponível!")
        msg.exec()


    def exibir_historico(self):
        # Criação da nova janela de histórico como QMainWindow
        self.janela_historico = QMainWindow()
        self.janela_historico.setWindowTitle("Histórico de Ações")
        self.janela_historico.resize(800, 650)

        # Centralizar a janela na tela
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_geometry = self.janela_historico.frameGeometry()
        window_geometry.moveCenter(screen_geometry.center())
        self.janela_historico.move(window_geometry.topLeft())

        # Criação do layout e tabela para exibir o histórico
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # Tabela do histórico
        self.tabela_historico = QTableWidget()
        self.tabela_historico.setColumnCount(4)
        self.tabela_historico.setHorizontalHeaderLabels(["Data/Hora", "Usuário", "Ação", "Descrição"])

        # Botão Atualizar
        botao_atualizar = QPushButton("Atualizar Histórico")
        botao_atualizar.clicked.connect(self.atualizar_historico)

        # Botão Apagar
        botao_apagar = QPushButton("Apagar Histórico")
        botao_apagar.clicked.connect(self.apagar_historico)

        botao_exportar_csv = QPushButton("Exportar CSV")
        botao_exportar_csv.clicked.connect(self.exportar_csv)

        botao_exportar_excel = QPushButton("Exportar Excel")
        botao_exportar_excel.clicked.connect(self.exportar_excel)

        botao_exportar_pdf = QPushButton("Exportar PDF")
        botao_exportar_pdf.clicked.connect(self.exportar_pdf)

        botao_pausar_historico = QPushButton("Pausar Histórico")
        botao_pausar_historico.clicked.connect(self.pausar_historico)


        botao_filtrar_historico = QPushButton("Filtrar Histórico")
        botao_filtrar_historico.clicked.connect(self.filtrar_historico)

        botao_ordenar_historico = QPushButton("Ordenar Histórico")
        botao_ordenar_historico.clicked.connect(self.ordenar_historico)

        # Criar checkbox "Selecionar Todos" toda vez que a janela for aberta
        self.checkbox_selecionar_todos = QCheckBox("Selecionar todo o histórico")
        self.checkbox_selecionar_todos.stateChanged.connect(self.selecionar_todos)

        # Criar checkbox "Selecionar Individualmente" toda vez que a janela for aberta
        self.checkbox_selecionar_individual = QCheckBox("Selecionar Individualmente")
        self.checkbox_selecionar_individual.stateChanged.connect(self.selecionar_individual)

        # Adicionar os checkboxes ao layout
        layout.addWidget(self.checkbox_selecionar_todos)
        layout.addWidget(self.checkbox_selecionar_individual)
    

        # Adicionar outros botões ao layout
        layout.addWidget(botao_atualizar)
        layout.addWidget(botao_apagar)
        layout.addWidget(botao_exportar_csv)
        layout.addWidget(botao_exportar_excel)
        layout.addWidget(botao_exportar_pdf)
        layout.addWidget(botao_pausar_historico)
        layout.addWidget(botao_ordenar_historico)
        layout.addWidget(botao_filtrar_historico)
        layout.addWidget(self.tabela_historico)


        # Configurar o widget central e exibir a janela
        self.janela_historico.setCentralWidget(central_widget)
        self.janela_historico.show()

        # Preencher tabela pela primeira vez
        self.carregar_historico()


    def selecionar_todos(self):
        if not self.coluna_checkboxes_adicionada:
            QMessageBox.warning(self, "Aviso", "Ative a opção 'Selecionar Individualmente' antes.")
            self.checkbox_selecionar_todos.setChecked(False)
            return

        estado = self.checkbox_selecionar_todos.isChecked()
        for checkbox in self.checkboxes:
            if checkbox:
                # Bloquear sinais para evitar loops
                checkbox.blockSignals(True)
                checkbox.setChecked(estado)
                checkbox.blockSignals(False)

    # Função para desmarcar todos os checkboxes
    def desmarcar_checkboxes(self):
        for checkbox in self.checkboxes:
            if checkbox:
                checkbox.setChecked(False)

    def carregar_historico(self):
        with sqlite3.connect('banco_de_dados.db') as cn:
            cursor = cn.cursor()
            cursor.execute("SELECT * FROM historico ORDER BY 'Data e Hora' DESC")
            registros = cursor.fetchall()

        self.tabela_historico.clearContents()
        self.tabela_historico.setRowCount(len(registros))

        for i, row in enumerate(registros):
            self.tabela_historico.setItem(i, 0, QTableWidgetItem(row[1]))  # Data/Hora
            self.tabela_historico.setItem(i, 1, QTableWidgetItem(row[2]))  # Usuário
            self.tabela_historico.setItem(i, 2, QTableWidgetItem(row[3]))  # Ação
            self.tabela_historico.setItem(i, 3, QTableWidgetItem(row[4]))  # Descrição


    def atualizar_historico(self):
        QMessageBox.information(self.janela_historico, "Sucesso", "Dados carregados com sucesso!")
        self.carregar_historico()


    def apagar_historico(self):
        """
        Função principal para apagar histórico. Trata tanto exclusão por checkboxes 
        quanto exclusão por seleção direta, dependendo do estado da tabela.
        """
        # Caso checkboxes estejam ativados
        if self.coluna_checkboxes_adicionada and self.checkboxes:
            linhas_para_remover = []
            ids_para_remover = []

            # Identificar as linhas com checkboxes selecionados
            for row, checkbox in enumerate(self.checkboxes):
                if checkbox and checkbox.isChecked():
                    linhas_para_remover.append(row)
                    item_data_widget = self.tabela_historico.item(row, 1)  # Coluna de Data/Hora
                    if item_data_widget:
                        item_data_text = item_data_widget.text().strip()
                        # Excluir com base na data e hora
                        item_id = self.get_id_by_data_hora(item_data_text)
                        if item_id:
                            ids_para_remover.append(item_id)
                        else:
                            print(f"Erro ao capturar ID para a data/hora: '{item_data_text}'")
                    else:
                        print(f"Erro ao capturar Data/Hora na linha {row}")

            if not ids_para_remover:
                QMessageBox.warning(self, "Erro", "Nenhum item válido foi selecionado para apagar!")
                return

            # Confirmar exclusão
            mensagem = (
                f"Você tem certeza que deseja apagar os {len(ids_para_remover)} itens selecionados?"
                if len(ids_para_remover) > 1
                else "Você tem certeza que deseja apagar o item selecionado?"
            )

            if not self.confirmar_historico_apagado(mensagem):
                return

            # Excluir do banco de dados
            with sqlite3.connect('banco_de_dados.db') as cn:
                cursor = cn.cursor()
                try:
                    for item_id in ids_para_remover:
                        cursor.execute("DELETE FROM historico WHERE id = ?", (item_id,))
                        print(f"Item removido do banco: ID {item_id}")
                    cn.commit()
                except Exception as e:
                    QMessageBox.critical(self, "Erro", f"Erro ao excluir do banco de dados: {e}")
                    return

            # Remover as linhas na interface
            for row in sorted(linhas_para_remover, reverse=True):
                self.tabela_historico.removeRow(row)

            QMessageBox.information(self, "Sucesso", "Itens removidos com sucesso!")

        # Caso sem checkboxes (seleção manual)
        else:
            linha_selecionada = self.tabela_historico.currentRow()

            if linha_selecionada < 0:
                QMessageBox.warning(self, "Erro", "Nenhum item foi selecionado para apagar!")
                return

            # Capturar a Data/Hora da célula correspondente (coluna 0)
            item_data_widget = self.tabela_historico.item(linha_selecionada, 0)  # Coluna de Data/Hora
            if not item_data_widget:
                QMessageBox.warning(self, "Erro", "Não foi possível identificar a Data/Hora do item a ser apagado!")
                return

            item_data_text = item_data_widget.text().strip()

            # Conectar ao banco de dados para buscar o ID relacionado à Data/Hora
            with sqlite3.connect('banco_de_dados.db') as cn:
                cursor = cn.cursor()
                try:
                    # Buscar o ID com base na Data/Hora, removendo espaços ou caracteres extras
                    cursor.execute('SELECT id FROM historico WHERE "Data e Hora" = ?', (item_data_text,))
                    resultado = cursor.fetchone()

                    if resultado:
                        item_id = resultado[0]  # Pegamos o ID encontrado
                    else:
                        QMessageBox.warning(self, "Erro", f"Não foi encontrado um item para a Data/Hora: {item_data_text}")
                        return

                except Exception as e:
                    QMessageBox.critical(self, "Erro", f"Erro ao buscar ID: {e}")
                    return

            # Confirmar exclusão
            mensagem = "Você tem certeza que deseja apagar o item selecionado?"

            if not self.confirmar_historico_apagado(mensagem):
                return

            # Excluir do banco de dados
            with sqlite3.connect('banco_de_dados.db') as cn:
                cursor = cn.cursor()
                try:
                    cursor.execute("DELETE FROM historico WHERE id = ?", (item_id,))
                    print(f"Item removido do banco de dados: ID {item_id}")
                    cn.commit()
                except Exception as e:
                    QMessageBox.critical(self, "Erro", f"Erro ao excluir do banco de dados: {e}")
                    return

            # Remover a linha da interface
            self.tabela_historico.removeRow(linha_selecionada)

            QMessageBox.information(self, "Sucesso", "Item removido com sucesso!")


    def get_id_by_data_hora(self, data_hora):
        """
        Função que busca o ID correspondente à Data/Hora no banco de dados.
        """
        with sqlite3.connect('banco_de_dados.db') as cn:
            cursor = cn.cursor()
            try:
                # Converter a Data/Hora para um formato compatível com o banco de dados
                cursor.execute('SELECT id FROM historico WHERE "Data e Hora" = ?', (data_hora,))
                resultado = cursor.fetchone()
                if resultado:
                    return resultado[0]  # Retorna o ID encontrado
                else:
                    return None  # Não encontrou nenhum ID correspondente
            except Exception as e:
                print(f"Erro ao buscar ID: {e}")
                return None






    def confirmar_historico_apagado(self, mensagem):
        """
        Exibe uma caixa de diálogo para confirmar a exclusão.
        """
        msgbox = QMessageBox(self)
        msgbox.setWindowTitle("Confirmação")
        msgbox.setText(mensagem)

        btn_sim = QPushButton("Sim")
        btn_nao = QPushButton("Não")
        msgbox.addButton(btn_sim, QMessageBox.ButtonRole.YesRole)
        msgbox.addButton(btn_nao, QMessageBox.ButtonRole.NoRole)

        msgbox.setDefaultButton(btn_nao)
        resposta = msgbox.exec()

        return msgbox.clickedButton() == btn_sim


     # Função para adicionar checkboxes na tabela de histórico
    def selecionar_individual(self):
        if self.tabela_historico.rowCount() == 0:
            QMessageBox.warning(self, "Aviso", "Nenhum histórico para selecionar.")
            return

        if self.coluna_checkboxes_adicionada:
            self.desmarcar_checkboxes()
            self.tabela_historico.removeColumn(0)
            self.coluna_checkboxes_adicionada = False
            return

        self.tabela_historico.insertColumn(0)
        self.tabela_historico.setHorizontalHeaderItem(0, QTableWidgetItem("Selecionar"))
        self.checkboxes = []

        for row in range(self.tabela_historico.rowCount()):
            checkbox = QCheckBox()
            checkbox.stateChanged.connect(self.atualizar_selecao_todos)
            checkbox_widget = QWidget()
            layout = QHBoxLayout(checkbox_widget)
            layout.addWidget(checkbox)
            layout.setAlignment(Qt.AlignCenter)
            layout.setContentsMargins(0, 0, 0, 0)
            checkbox_widget.setLayout(layout)
            self.tabela_historico.setCellWidget(row, 0, checkbox)
            self.checkboxes.append(checkbox)

        self.tabela_historico.setColumnWidth(0, 30)
        self.coluna_checkboxes_adicionada = True

    
    def atualizar_selecao_todos(self):
        self.checkbox_selecionar_todos.blockSignals(True)

        # Atualizar o estado do "Selecionar Todos"
        all_checked = all(checkbox.isChecked() for checkbox in self.checkboxes if checkbox)
        any_checked = any(checkbox.isChecked() for checkbox in self.checkboxes if checkbox)

        self.checkbox_selecionar_todos.setChecked(all_checked)

        self.checkbox_selecionar_todos.blockSignals(False)


    def ordenar_historico(self):
        # Obter a coluna pela qual o usuário deseja ordenar
        coluna = self.obter_coluna_para_ordenar()  # Função fictícia para capturar escolha
        
        # Determinar a direção de ordenação (ascendente ou descendente)
        direcao = self.obter_direcao_ordenacao()  # Função fictícia para capturar escolha
        
        # Mapeamento de colunas para índices (ajustar conforme sua tabela)
        colunas_para_indices = {
            "Data/Hora": 0,
            "Usuário": 1,
            "Ação": 2,
            "Descrição": 3
        }
        
        # Verificar se a coluna escolhida é válida
        if coluna not in colunas_para_indices:
            QMessageBox.warning(self, "Erro", "Coluna inválida para ordenação!")
            return
        
        # Obter o índice da coluna escolhida
        indice_coluna = colunas_para_indices[coluna]
        
        # Obter os dados atuais da tabela
        dados = []
        for row in range(self.tabela_historico.rowCount()):
            linha = [
                self.tabela_historico.item(row, col).text() if self.tabela_historico.item(row, col) else ""
                for col in range(self.tabela_historico.columnCount())
            ]
            dados.append(linha)
        
        # Ordenar os dados com base na coluna escolhida e direção
        dados.sort(key=lambda x: x[indice_coluna], reverse=(direcao == "Decrescente"))
        
        # Atualizar a tabela com os dados ordenados
        self.tabela_historico.setRowCount(0)  # Limpar tabela
        for row_data in dados:
            row = self.tabela_historico.rowCount()
            self.tabela_historico.insertRow(row)
            for col, value in enumerate(row_data):
                self.tabela_historico.setItem(row, col, QTableWidgetItem(value))


    def obter_coluna_para_ordenar(self):
        colunas = ["Data/Hora", "Usuário", "Ação", "Descrição"]
        coluna, ok = QInputDialog.getItem(self, "Ordenar por", "Escolha a coluna:", colunas, 0, False)
        return coluna if ok else None

    def obter_direcao_ordenacao(self):
        direcoes = ["Crescente", "Decrescente"]
        direcao, ok = QInputDialog.getItem(self, "Direção da Ordenação", "Escolha a direção:", direcoes, 0, False)
        return direcao if ok else None



    def filtrar_historico(self):
        # Criar a janela de filtro
        janela_filtro = QDialog(self)
        janela_filtro.setWindowTitle("Filtrar Histórico")
        layout = QVBoxLayout(janela_filtro)

        # Campo para inserir a data
        campo_data = QLineEdit()
        campo_data.setPlaceholderText("Digite a data no formato DD/MM/AAAA")
        
        # Conectar ao método de formatação, passando o texto
        campo_data.textChanged.connect(lambda: self.formatar_data(campo_data))


        # Campo para selecionar se quer o mais recente ou mais antigo (filtro por hora)
        grupo_hora = QGroupBox("Filtrar por Hora")
        layout_hora = QVBoxLayout(grupo_hora)

        radio_mais_novo = QRadioButton("Mais Recente")
        radio_mais_velho = QRadioButton("Mais Antigo")

        layout_hora.addWidget(radio_mais_novo)
        layout_hora.addWidget(radio_mais_velho)
        grupo_hora.setLayout(layout_hora)

        # Botão para aplicar o filtro
        botao_filtrar = QPushButton("Aplicar Filtro")
        botao_filtrar.clicked.connect(
            lambda: self.aplicar_filtro(
                campo_data.text(),
                radio_mais_novo.isChecked(),
                radio_mais_velho.isChecked()
            )
        )

        # Adicionar widgets ao layout
        layout.addWidget(QLabel("Filtros Disponíveis"))
        layout.addWidget(campo_data)
        layout.addWidget(grupo_hora)
        layout.addWidget(botao_filtrar)

        # Exibir a janela de filtro
        janela_filtro.setLayout(layout)
        janela_filtro.exec()

    def formatar_data(self, campo_data):
        # Obter o texto do campo de data
        texto_data = campo_data.text().replace("/", "")  # Remover as barras existentes
        texto_data = ''.join(filter(str.isdigit, texto_data))  # Permite apenas números

        # Verificar se há caracteres alfabéticos (letras)
        if any(char.isalpha() for char in texto_data):
            # Mostrar mensagem de erro caso haja letras
            QMessageBox.warning(self, "Erro", "Somente números são permitidos.")
            campo_data.clear()
            return  # Não aplica a formatação se houver letras

        # Limitar a entrada para no máximo 8 dígitos
        if len(texto_data) > 8:
            texto_data = texto_data[:8]

         # Formatar a data no formato DD/MM/AAAA
        if len(texto_data) >= 8:
            data_formatada = "{}/{}/{}".format(texto_data[:2], texto_data[2:4], texto_data[4:])  # DD/MM/AAAA
        elif len(texto_data) > 6:
            data_formatada = "{}/{}".format(texto_data[:2], texto_data[2:8])  # DD/MM
        else:
            data_formatada = texto_data[:8]  # Apenas o DD

        # Atualizar o texto do campo de data se houver mudança
        if campo_data.text() != data_formatada:
            campo_data.setText(data_formatada)  # Atualiza o texto do campo de data
            campo_data.setCursorPosition(len(data_formatada))  # Move o cursor para o final do texto


    def aplicar_filtro(self, data, filtrar_novo, filtrar_velho):
        with sqlite3.connect('banco_de_dados.db') as cn:
            cursor = cn.cursor()

            query = "SELECT * FROM historico"
            params = []

            # Filtrar pela data, se fornecida
            if data:
                try:
                    # Garantir que a data seja no formato correto (DD/MM/AAAA)
                    data_formatada = datetime.strptime(data, "%d/%m/%Y").strftime("%d/%m/%Y")  # Formato DD/MM/YYYY
                    query += " WHERE SUBSTR([Data e Hora], 1, 10) = ?"
                    params.append(data_formatada)
                except ValueError:
                    QMessageBox.warning(self, "Erro", "Data inválida. Use o formato DD/MM/AAAA.")
                    return

            # Ordenar por hora, se aplicável
            if filtrar_novo:
                query += " ORDER BY [Data e Hora] DESC LIMIT 1"
            elif filtrar_velho:
                query += " ORDER BY [Data e Hora] ASC LIMIT 1"

            # Executar a consulta
            cursor.execute(query, params)
            registros = cursor.fetchall()

        # Atualizar a tabela com os registros filtrados
        self.tabela_historico.clearContents()
        self.tabela_historico.setRowCount(len(registros))

        for i, row in enumerate(registros):
            self.tabela_historico.setItem(i, 0, QTableWidgetItem(row[1]))  # Data/Hora
            self.tabela_historico.setItem(i, 1, QTableWidgetItem(row[2]))  # Usuário
            self.tabela_historico.setItem(i, 2, QTableWidgetItem(row[3]))  # Ação
            self.tabela_historico.setItem(i, 3, QTableWidgetItem(row[4]))  # Descrição

        QMessageBox.information(self, "Filtro Aplicado", f"{len(registros)} registro(s) encontrado(s)!")





    def exportar_csv(self):
        num_linhas = self.tabela_historico.rowCount()
        num_colunas = self.tabela_historico.columnCount()

        # Verificar se a tabela está vazia
        if self.tabela_historico.rowCount() == 0:
            QMessageBox.warning(self, "Aviso", "Nenhum histórico encontrado para gerar arquivo CSV.")
            return  # Se a tabela estiver vazia, encerra a função sem prosseguir

        nome_arquivo, _ = QFileDialog.getSaveFileName(
            self,
            "Salvar Arquivo CSV",
            "historico.csv",
            "Arquivos CSV (*.csv)"

        )

        if not nome_arquivo:
            return
        
        #Criar o arquivo CSV
        try:
            with open(nome_arquivo, mode="w",newline="",encoding="utf-8-sig") as arquivo_csv:
                escritor = csv.writer(arquivo_csv, delimiter=";")

                 # Adicionar cabeçalhos ao CSV
                cabecalhos = [self.tabela_historico.horizontalHeaderItem(col).text() for col in range (num_colunas)]
                escritor.writerow(cabecalhos)

                # Adicionar os dados da tabela ao CSV
                for linha in range(num_linhas):
                    dados_linhas = [
                        self.tabela_historico.item(linha, col).text() if self.tabela_historico.item(linha, col) else ""
                        for col in range(num_colunas)

                    ]
                    escritor.writerow(dados_linhas)

                    QMessageBox.information(self, "Sucesso", f"Arquivo CSV salvo com sucesso em:\n{nome_arquivo}")

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Falha ao salvar o arquivo CSV:\n{str(e)}")


    def exportar_excel(self):
        num_linhas = self.tabela_historico.rowCount()
        num_colunas = self.tabela_historico.columnCount()

        # Verificar se a tabela está vazia
        if self.tabela_historico.rowCount() == 0:
            QMessageBox.warning(self, "Aviso", "Nenhum histórico encontrado para gerar arquivo Excel.")
            return  # Se a tabela estiver vazia, encerra a função sem prosseguir
        
        nome_arquivo, _ = QFileDialog.getSaveFileName(
            self,
            "Salvar Arquivo Excel",
            "historico.xlsx",
            "Arquivos Excel (*.xlsx)"

        )

        if not nome_arquivo:
            return
        
        # Garantir que o arquivo tenha extensão .xlsx
        if not nome_arquivo.endswith(".xlsx"):
            nome_arquivo += ".xlsx"

        # Criar uma lista para armazenar os dados da tabela
        dados = []


        for linha in range(num_linhas):
            linha_dados = []
            for coluna in range(num_colunas):
                item = self.tabela_historico.item(linha, coluna)
                linha_dados.append(item.text() if item else "") # Adicionar o texto ou vazio se o item for None
            dados.append(linha_dados)

        # Obter os cabeçalhos da tabela        
        cabecalhos = [self.tabela_historico.horizontalHeaderItem(coluna).text() for coluna in range (num_colunas)]

        

        try:
            # Criar um DataFrame do pandas com os dados e cabeçalhos
            df = pd.DataFrame(dados, columns=cabecalhos)

            # Exportar para Excel
            df.to_excel(nome_arquivo, index=False,engine="openpyxl")
            QMessageBox.information(self, "Sucesso",f"Arquivo Excel gerado com sucesso em: \n{nome_arquivo}")
        except Exception as e:
            QMessageBox.critical(self, "Erro",f"Erro ao salvar arquivo Excel: {str(e)}")



    def exportar_pdf(self):
        num_linhas = self.tabela_historico.rowCount()
        num_colunas = self.tabela_historico.columnCount()

        # Verificar se a tabela está vazia
        if self.tabela_historico.rowCount() == 0:
            QMessageBox.warning(self, "Aviso", "Nenhum histórico encontrado para gerar arquivo PDF.")
            return  # Se a tabela estiver vazia, encerra a função sem prosseguir

        nome_arquivo, _ = QFileDialog.getSaveFileName(
            self,
            "Salvar Arquivo PDF",
            "historico.pdf",
            "Arquivos PDF (*.pdf)"
        )

        if not nome_arquivo:
            return

        # Garantir que o arquivo tenha extensão .pdf
        if not nome_arquivo.endswith(".pdf"):
            nome_arquivo += ".pdf"

        # Criar uma lista para armazenar os dados da tabela
        dados = []

        # Obter os cabeçalhos da tabela
        cabecalhos = [self.tabela_historico.horizontalHeaderItem(coluna).text() for coluna in range(num_colunas)]
        dados.append(cabecalhos)  # Adicionar os cabeçalhos como a primeira linha do PDF

        # Adicionar os dados da tabela
        for linha in range(num_linhas):
            linha_dados = []
            for coluna in range(num_colunas):
                item = self.tabela_historico.item(linha, coluna)
                linha_dados.append(item.text() if item else "")  # Adicionar o texto ou vazio se o item for None
            dados.append(linha_dados)

        try:
            # Criar o PDF
            pdf = SimpleDocTemplate(nome_arquivo, pagesize=landscape(letter))
            tabela = Table(dados)

            # Adicionar estilo à tabela
            estilo = TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Cabeçalho com fundo cinza
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Texto do cabeçalho branco
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Centralizar texto
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Fonte do cabeçalho
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Espaçamento inferior no cabeçalho
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  # Fundo das linhas de dados
                ('GRID', (0, 0), (-1, -1), 1, colors.black)  # Bordas da tabela
            ])
            tabela.setStyle(estilo)

            # Gerar o PDF
            pdf.build([tabela])
            QMessageBox.information(self, "Sucesso", f"Arquivo PDF gerado com sucesso em: \n{nome_arquivo}")

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao salvar arquivo PDF: {str(e)}")

    def pausar_historico(self):
        # Criação da nova janela de histórico como QMainWindow
        self.janela_escolha = QMainWindow()
        self.janela_escolha.setWindowTitle("Pausar Histórico")
        self.janela_escolha.resize(255, 150)


        # Botão "Sim"
        botao_sim = QPushButton("Sim")
        botao_sim.clicked.connect(self.historico_ativo)

        # Botão "Não"
        botao_nao = QPushButton("Não")
        botao_nao.clicked.connect(self.historico_inativo)


        # Criação do layout e tabela para exibir o histórico
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # Texto centralizado
        label = QLabel("Deseja pausar o histórico?")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Alinha o texto ao centro

        layout.addWidget(label)  # Adiciona o texto centralizado
        layout.addWidget(botao_sim)
        layout.addWidget(botao_nao)

        self.janela_escolha.setCentralWidget(central_widget)
        self.janela_escolha.show()


    def historico_ativo(self):
        # Atualiza o estado do histórico para ativo
        self.main_window.historico_pausado = True  # Atualiza a variável no MainWindow
        QMessageBox.information(self, "Histórico", "O registro do histórico foi pausado.")
        self.janela_escolha.close()

    def historico_inativo(self):
        # Atualiza o estado do histórico para inativo (continua registrando)
        self.main_window.historico_pausado = False  # Atualiza a variável no MainWindow
        QMessageBox.information(self, "Histórico", "O registro do histórico continua ativo.")
        self.janela_escolha.close()


    def abrir_planilha(self):
        # Abrir o diálogo para selecionar o arquivo Excel
        nome_arquivo, _ = QFileDialog.getOpenFileName(self, "Abrir Arquivo Excel", "", "Arquivos Excel (*.xlsx)")

        if not nome_arquivo:
            return  # Se o usuário cancelar a seleção do arquivo

        try:
            # Usando pandas para ler o arquivo Excel
            df = pd.read_excel(nome_arquivo, engine="openpyxl", header=0)

            # Definir os títulos das colunas da table_base manualmente, de acordo com a ordem desejada
            colunas_table_base = ["Produto", "Quantidade", "Valor do Produto", "Desconto", "Data da Compra", 
                                "Código do Item", "Cliente", "Descrição do Produto", "Usuário"]

            # Limpar a tabela antes de adicionar os dados
            self.table_base.setRowCount(0)

            # Verificar se o arquivo tem a quantidade certa de colunas
            if df.shape[1] != len(colunas_table_base):
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Icon.Warning)
                msg_box.setWindowTitle("Erro na Estrutura do Arquivo")
                msg_box.setText("O número de colunas no arquivo Excel não corresponde ao número esperado. Deseja continuar mesmo assim?")
                msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

                sim_button = msg_box.button(QMessageBox.StandardButton.Yes)
                sim_button.setText("Sim")
                nao_button = msg_box.button(QMessageBox.StandardButton.No)
                nao_button.setText("Não")

                resposta = msg_box.exec()

                if resposta == QMessageBox.StandardButton.No:
                    return  # Se o usuário escolher não continuar, encerra a função

                num_colunas_faltando = len(colunas_table_base) - df.shape[1]
                if num_colunas_faltando > 0:
                    df = pd.concat([df, pd.DataFrame([[""] * num_colunas_faltando] * df.shape[0])], axis=1)

            # Garantir que o valor do produto esteja em tipo float para cálculos
            df["Valor do Produto"] = pd.to_numeric(df.iloc[:, 2], errors="coerce").fillna(0)
            df["Valor do Produto"] = df["Valor do Produto"].apply(
                lambda x: f"R$ {x:,.2f}".replace(",", "_").replace(".", ",").replace("_", ".")
            )

            # Corrigir a coluna "Desconto" para ser uma fração em vez de porcentagem
            df["Desconto"] = pd.to_numeric(df.iloc[:, 3], errors="coerce").fillna(0)
            df["Desconto"] = df["Desconto"].apply(
                lambda x: f"{x:.2f}%" if x < 1 else f"{x * 100:.2f}%"
            )   

            # Criar a coluna "Data da Compra" com formatação sem a parte da hora
            if "Data da Compra" in df.columns:
                # Garantir que os valores da coluna de data estão no formato correto (sem a hora)
                df["Data da Compra"] = pd.to_datetime(df["Data da Compra"], errors="coerce").dt.strftime('%d/%m/%Y')
            else:
                # Se a coluna "Data da Compra" não existir, criar uma coluna com dados vazios
                df["Data da Compra"] = ""

            # Inserir os dados na table_base
            for row in df.itertuples(index=False):
                row_position = self.table_base.rowCount()
                self.table_base.insertRow(row_position)

                # Preencher cada célula da tabela com os dados do arquivo Excel, na ordem definida
                for column, value in enumerate(row):
                    item = self.criar_item(str(value))  # Usando o método que você já deve ter para criar os itens
                    self.table_base.setItem(row_position, column, item)

            QMessageBox.information(self, "Sucesso", "Arquivo Excel importado com sucesso!")

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao importar o arquivo Excel: {e}")




    def incluir_sistema(self):
        pass