from PySide6.QtGui import QColor, QBrush,QGuiApplication
from PySide6.QtWidgets import (QWidget, QTableWidget, QTableWidgetItem, 
                               QMessageBox,QCheckBox,QVBoxLayout,QDialog,QPushButton,QMainWindow,QHBoxLayout,
                               QLineEdit,QLabel,QInputDialog,QGroupBox,QRadioButton,QFileDialog,QHeaderView)
from PySide6.QtCore import Qt,QTimer,QEvent
import sqlite3
import pandas as pd
from datetime import datetime
from database import DataBase
import csv
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter,landscape,A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.pdfgen import canvas
from configuracoes import Configuracoes_Login


class EstoqueProduto(QWidget):
    def __init__(self, main_window, btn_gerar_pdf, btn_gerar_estorno, 
                 btn_gerar_saida,btn_importar, btn_limpar_tabela, 
                 btn_atualizar_saida, btn_atualizar_estoque, btn_historico,
                 btn_abrir_planilha, line_excel, progress_excel, btn_incluir_produto_sistema,
                 btn_fazer_cadastro_massa_produtos,btn_abrir_planilha_massa_produtos,progress_massa_produtos,
                 line_edit_massa_produtos,parent=None):
        super().__init__(parent)

        self.db = DataBase("banco_de_dados.db")
        self.alteracoes_salvas = False
        self.config = Configuracoes_Login(self)

        self.checkboxes = []  # Lista para armazenar os checkboxes
        self.coluna_checkboxes_adicionada = False


        self.main_window = main_window
        self.table_base = self.main_window.table_base  # Referência para a tabela no main window
        self.table_saida = self.main_window.table_saida
        self.table_massa_produtos = self.main_window.table_massa_produtos
        self.btn_gerar_pdf = btn_gerar_pdf
        self.btn_gerar_estorno = btn_gerar_estorno
        self.btn_gerar_saida = btn_gerar_saida
        self.btn_importar = btn_importar
        self.btn_limpar_tabela = btn_limpar_tabela
        self.btn_atualizar_saida = btn_atualizar_saida
        self.btn_atualizar_estoque = btn_atualizar_estoque
        self.btn_historico = btn_historico
        self.btn_abrir_planilha = btn_abrir_planilha
        self.line_excel = line_excel
        self.progress_excel = progress_excel
        self.btn_incluir_produto_sistema = btn_incluir_produto_sistema
        self.btn_fazer_cadastro_massa_produtos = btn_fazer_cadastro_massa_produtos
        self.btn_abrir_planilha_massa_produtos = btn_abrir_planilha_massa_produtos
        self.progress_massa_produtos = progress_massa_produtos
        self.line_edit_massa_produtos = line_edit_massa_produtos
        


        self.btn_gerar_pdf.clicked.connect(self.exibir_pdf)
        self.btn_gerar_estorno.clicked.connect(self.criar_estorno)
        self.btn_gerar_saida.clicked.connect(self.confirmar_saida)
        self.btn_importar.clicked.connect(self.importar_produto)
        self.btn_limpar_tabela.clicked.connect(self.limpar_tabela)
        self.btn_atualizar_saida.clicked.connect(self.atualizar_saida)
        self.btn_atualizar_estoque.clicked.connect(self.atualizar_estoque)
        self.btn_historico.clicked.connect(self.exibir_historico)    
        self.btn_abrir_planilha.clicked.connect(self.abrir_planilha)
        self.btn_incluir_produto_sistema.clicked.connect(self.incluir_produto_no_sistema)
        self.btn_fazer_cadastro_massa_produtos.clicked.connect(self.cadastrar_produtos_em_massa)
        self.btn_abrir_planilha_massa_produtos.clicked.connect(self.abrir_planilha_em_massa_produtos)
        self.main_window.table_base.viewport().installEventFilter(self)
        self.main_window.table_saida.viewport().installEventFilter(self)

        


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
        SELECT Produto, Quantidade, Valor_Real, IFNULL(Desconto, 'Sem Desconto') AS Desconto,"Valor Total", "Data do Cadastro", 
        Código_Item, Cliente, Descrição_Produto, Usuário, "Status da Saída"
        FROM products
        """
        df = pd.read_sql_query(query, cn)

        # Verificando se há dados na consulta
        if df.empty:
            print("Nenhum dado encontrado no banco de dados.")
            return

        # Configurando cabeçalhos das colunas
        num_columns = len(df.columns)
        self.table_base.setRowCount(len(df))
        self.table_base.setColumnCount(num_columns)
        
        
        # Limpando o QTableWidget antes de popular com novos dados
        self.table_base.clearContents()
        self.table_base.setRowCount(0)  # Certifique-se de que as linhas estão limpas

        # Iterando sobre os dados do DataFrame e adicionando-os ao QTableWidget
        for row_index, row_data in df.iterrows():
            self.table_base.insertRow(row_index)  # Inserir nova linha
            for col_index, data in enumerate(row_data):
                item = self.criar_item(str(data))  # Usando a função auxiliar
                
                # Adicionando o item à QTableWidget
                self.table_base.setItem(row_index, col_index, item)



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
        produtos_saida = []
        historico_logs = []
        atualizacoes_produtos = []

        for row in produtos_selecionados:
            produto = self.main_window.table_base.item(row, 0).text() or ""
            quantidade_str = self.main_window.table_base.item(row, 1).text() or "0"
            quantidade = int(quantidade_str)
            valor_produto = self.main_window.table_base.item(row, 2).text() or ""
            desconto = self.main_window.table_base.item(row, 3).text() or ""
            valor_total = self.main_window.table_base.item(row, 4).text() or ""
            data_cadastro = self.main_window.table_base.item(row, 5).text() or ""
            codigo_produto = self.main_window.table_base.item(row, 6).text() or ""
            cliente = self.main_window.table_base.item(row, 7).text() or ""
            descricao = self.main_window.table_base.item(row, 8).text() or ""
            usuario = self.main_window.table_base.item(row, 9).text() or ""
            status_saida = 1
            data_saida = datetime.now().strftime("%d/%m/%Y %H:%M")

            if quantidade > 1:
                quantidade_saida, ok = QInputDialog.getInt(
                    None,
                    "Saída de Produto",
                    f"O produto '{produto}' tem {quantidade} unidades.\nQuantas deseja dar saída?",
                    value=1,
                    minValue=1,
                    maxValue=quantidade
                )
                if not ok:
                    return
            else:
                quantidade_saida = 1

            nova_quantidade = quantidade - quantidade_saida
            atualizacoes_produtos.append((nova_quantidade, codigo_produto))

            # Atualiza visualmente na table_base
            if nova_quantidade > 0:
                self.main_window.table_base.item(row, 1).setText(str(nova_quantidade))
                self.main_window.table_base.setItem(row, 1, self.criar_item("1"))  
            else:
                self.main_window.table_base.removeRow(row)

            # Verifica se já está na lista e soma
            produto_existente = None
            for i, p in enumerate(produtos_saida):
                if p[7] == codigo_produto: # Índice 7 = Código do Produto
                    produto_existente = i
                    break

            if produto_existente is not None:
                quantidade_existente = int(produtos_saida[produto_existente][1])
                nova_quantidade_saida = quantidade_existente + quantidade_saida
                produtos_saida[produto_existente] = (
                    produto,
                    str(nova_quantidade_saida),
                    valor_produto,
                    desconto,
                    valor_total,
                    data_saida,
                    data_cadastro,
                    codigo_produto,
                    cliente,
                    descricao,
                    usuario,
                    status_saida # 12º item (sem imagem)
                )
            else:
                produtos_saida.append((
                    produto,
                    str(quantidade_saida),
                    valor_produto,
                    desconto,
                    valor_total,
                    data_saida,
                    data_cadastro,
                    codigo_produto,
                    cliente,
                    descricao,
                    usuario,
                    status_saida
                ))

            historico_logs.append(f"Produto {produto} foi gerado saída de {quantidade_saida} unidade(s).")

        try:
            cursor = self.db.connection.cursor()

            for (nova_quantidade, codigo_produto) in atualizacoes_produtos:
                if nova_quantidade > 0:
                    cursor.execute("""
                        UPDATE products
                        SET Quantidade = ?, 'Status da Saída' = 1
                        WHERE Código_Item = ?
                    """, (nova_quantidade, codigo_produto))
                else:
                    cursor.execute("""
                        UPDATE products
                        SET 'Status da Saída' = 1
                        WHERE Código_Item = ?
                    """, (codigo_produto,))
                    cursor.execute("""
                        DELETE FROM products
                        WHERE Código_Item = ?
                    """, (codigo_produto,))

            for produto_info in produtos_saida:
                # Recupera imagem separadamente e adiciona à tupla
                imagem = self.recuperar_imagem_produto_bd_products(produto_info[7]) # Código do Produto
                produto_info_com_imagem = produto_info[:11] + (imagem,produto_info[11]) # insere imagem no índice 11
                self.db.salvar_saida_produto(produto_info_com_imagem)

            self.db.connection.commit()

        except Exception as e:
            print(f"Erro ao salvar saída: {e}")

        for texto in historico_logs:
            self.main_window.registrar_historico("Gerado Saída", texto)

        if produtos_saida:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle("Aviso")
            msg_box.setText("Saída do(s) produto(s) gerada com sucesso!")
            msg_box.exec()
            self.tabela_saida_preencher(produtos_saida)

        self.reindex_table_base()



    def tabela_saida_preencher(self, dados_saida):
        for item in dados_saida:
            codigo_produto_novo = item[7]  # 'Código do Produto'
            quantidade_nova = int(item[1])

            linha_existente = None
            for row in range(self.main_window.table_saida.rowCount()):
                codigo_existente = self.main_window.table_saida.item(row, 6)
                if codigo_existente and codigo_existente.text() == codigo_produto_novo:
                    linha_existente = row
                    break

            if linha_existente is not None:
                # Produto já existe: somar as quantidades
                quantidade_existente = int(self.main_window.table_saida.item(linha_existente, 1).text())
                nova_quantidade = quantidade_existente + quantidade_nova
                self.main_window.table_saida.item(linha_existente, 1).setText(str(nova_quantidade))
            else:
                # Produto não existe ainda: adicionar nova linha
                row_position = self.main_window.table_saida.rowCount()
                self.main_window.table_saida.insertRow(row_position)

                self.main_window.table_saida.setItem(row_position, 0, self.criar_item(item[0]))   # Produto
                self.main_window.table_saida.setItem(row_position, 1, self.criar_item(item[1]))   # Quantidade
                self.main_window.table_saida.setItem(row_position, 2, self.criar_item(item[2]))   # Valor do Produto
                self.main_window.table_saida.setItem(row_position, 3, self.criar_item(item[3]))   # Desconto
                self.main_window.table_saida.setItem(row_position, 4, self.criar_item(item[4]))   # Valor Total
                self.main_window.table_saida.setItem(row_position, 5, self.criar_item(item[5]))   # Data de Saída
                self.main_window.table_saida.setItem(row_position, 6, self.criar_item(item[6]))   # Data da Criação
                self.main_window.table_saida.setItem(row_position, 7, self.criar_item(item[7]))   # Código do Produto
                self.main_window.table_saida.setItem(row_position, 8, self.criar_item(item[8]))   # Cliente
                self.main_window.table_saida.setItem(row_position, 9, self.criar_item(item[9]))   # Descrição
                self.main_window.table_saida.setItem(row_position, 10, self.criar_item(item[10])) # Usuário
                self.main_window.table_saida.setItem(row_position, 11, self.criar_item(str(item[11]))) # Status da Saída

                self.table_saida.resizeColumnsToContents()
                self.table_saida.resizeRowsToContents()




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
        
        row_count = self.main_window.table_saida.rowCount()

        if row_count == 0:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("ERRO")
            msg_box.setText("Não há nenhum dado disponível na tabela para gerar estorno!")
            msg_box.exec()
            return

        for row in range(row_count):
            produto_item = self.main_window.table_saida.item(row, 0)
            quantidade_item = self.main_window.table_saida.item(row, 1)
            valor_real_item = self.main_window.table_saida.item(row, 2)
            desconto_item = self.main_window.table_saida.item(row, 3)
            valor_total_item = self.main_window.table_saida.item(row, 4)         # Valor Total
            data_cadastro_item = self.main_window.table_saida.item(row, 6)       # Data do Cadastro
            codigo_item = self.main_window.table_saida.item(row, 7)              # Código do Produto
            cliente_item = self.main_window.table_saida.item(row, 8)             # Cliente
            descricao_item = self.main_window.table_saida.item(row, 9)           # Descrição
            usuario_item = self.main_window.table_saida.item(row, 10)            # Usuário
            status_saida_item = self.main_window.table_saida.item(row, 11)       # Status da Saída

            produto = produto_item.text() if produto_item else ""
            quantidade = int(quantidade_item.text()) if quantidade_item else "0"
            valor_real = valor_real_item.text() if valor_real_item else ""
            desconto = desconto_item.text() if desconto_item else ""
            valor_total = valor_total_item.text() if valor_total_item else ""
            data_cadastro = data_cadastro_item.text() if data_cadastro_item else ""
            codigo_produto = codigo_item.text() if codigo_item else ""
            cliente = cliente_item.text() if cliente_item else ""
            descricao = descricao_item.text() if descricao_item else ""
            usuario = usuario_item.text() if usuario_item else "Não Cadastrado"
            status_saida = status_saida_item.text() if status_saida_item else "Não Cadastrado"


            #  Verifica se a quantidade é válida
            if int(quantidade) <= 0:
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Warning)
                msg_box.setWindowTitle("Estorno inválido")
                msg_box.setText(f"O produto '{produto}' tem quantidade 0 e não pode ser estornado.")
                msg_box.exec()
                continue

            if int(quantidade) > 1:
                quantidade_estorno, ok = QInputDialog.getInt(
                    self.main_window,
                    "Quantidade de Estorno",
                    f"O produto {produto} possui {quantidade} unidades. Quanto deseja estornar? ",
                    minValue=1,
                    maxValue=quantidade,
                    value=1
                )
                if not ok:
                    return
            else:
                quantidade_estorno = 1

            # Recupera imagem do banco
            imagem = self.recuperar_imagem_produto_bd_products_saida(codigo_produto)

            # Atualiza ou insere no banco
            with sqlite3.connect("banco_de_dados.db") as cn:
                cursor = cn.cursor()

                # Verifica se o produto já existe
                cursor.execute("SELECT Quantidade FROM products WHERE Código_Item = ?", (codigo_produto,))
                resultado = cursor.fetchone()

                if resultado:
                    # Atualiza a quantidade somando a estornada
                    nova_quantidade = int(resultado[0]) + quantidade_estorno
                    cursor.execute("""
                        UPDATE products
                        SET Quantidade = ?
                        WHERE Código_Item = ?
                    """, (nova_quantidade, codigo_produto))
                else:
                    # Insere como novo produto
                    cursor.execute("""
                        INSERT INTO products 
                        (Produto, Quantidade, Valor_Real, Desconto, "Valor Total","Data do Cadastro", Código_Item, Cliente, Descrição_Produto, Imagem, Usuário,'Status da Saída')
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?,?)
                    """, (produto, str(quantidade_estorno), valor_real, desconto,valor_total, data_cadastro, 
                          codigo_produto, cliente, descricao, imagem, usuario, 1))
                cn.commit()

                if quantidade_estorno >= quantidade:
                    cursor.execute("""
                        DELETE FROM products_saida WHERE "Código do Produto" = ?
                    """, (codigo_produto,))

                # Deleta da tabela de saída
                else:
                    nova_quantidade_saida = quantidade - quantidade_estorno
                    cursor.execute("""
                        UPDATE products_saida
                        SET Quantidade = ?
                        WHERE "Código do Produto" = ?
                    """, (nova_quantidade_saida, codigo_produto))
                    cn.commit()
                    

            # Verifica se o item já está na table_base visualmente
            linha_existente = None
            for linha in range(self.main_window.table_base.rowCount()):
                codigo_existente = self.main_window.table_base.item(linha,5)
                if codigo_existente and codigo_existente.text() == codigo_produto:
                    linha_existente = linha
                    break
            if linha_existente is not None:
                # Soma a quantidade diretamente na linha existente
                item_quantidade = self.main_window.table_base.item(linha_existente,1)
                quantidade_atual = int(item_quantidade.text()) if item_quantidade else 0
                nova_quantidade_visual = quantidade_atual + int(quantidade)
                self.main_window.table_base.setItem(linha_existente, 1,self.criar_item(str(nova_quantidade_visual)))
            else:
                # Recupera o nome do usuário do código original
                usuario = self.config.obter_usuario_logado()

                # Atualiza a tabela base visualmente
                row_base = self.main_window.table_base.rowCount()
                self.main_window.table_base.insertRow(row_base)
                self.main_window.table_base.setItem(row_base, 0, self.criar_item(produto))
                self.main_window.table_base.setItem(row_base, 1, self.criar_item(str(quantidade_estorno)))
                self.main_window.table_base.setItem(row_base, 2, self.criar_item(valor_real))
                self.main_window.table_base.setItem(row_base, 3, self.criar_item(desconto))
                self.main_window.table_base.setItem(row_base, 4, self.criar_item(valor_total))
                self.main_window.table_base.setItem(row_base, 5, self.criar_item(data_cadastro))
                self.main_window.table_base.setItem(row_base, 6, self.criar_item(codigo_produto))
                self.main_window.table_base.setItem(row_base, 7, self.criar_item(cliente))
                self.main_window.table_base.setItem(row_base, 8, self.criar_item(descricao))
                self.main_window.table_base.setItem(row_base, 9, self.criar_item(usuario))
                self.main_window.table_base.setItem(row_base,10,self.criar_item("1"))

            # Registrar histórico
            historico_texto = f"Produto '{produto}' foi estornado."
            self.main_window.registrar_historico("Estorno do Produto", historico_texto)

        # Limpar a tabela de saída
        self.main_window.table_saida.clearContents()
        self.main_window.table_saida.setRowCount(0)

        # Mensagem de sucesso
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("Sucesso")
        msg_box.setText("Estorno realizado com sucesso.")
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


    def atualizar_estoque(self):
        try:
            # Limpar a tabela antes de atualizar
            self.table_base.setRowCount(0)  # Remove todas as linhas da tabela

            # Consultar todos os produtos
            query = """
            SELECT Produto, Quantidade, Valor_Real, Desconto, "Valor Total","Data do Cadastro", Código_Item, Cliente, Descrição_Produto, Usuário, "Status da Saída"
            FROM products
            """
            produtos = self.db.executar_query(query)

            if produtos:
                for produto in produtos:
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
            msg_box.setWindowTitle("Erro")
            msg_box.setText("Erro ao atualizar a tabela de estoque")       
            msg_box.exec()


        except Exception as e:
            print(f"Erro ao atualizar a tabela de estoque: {e}")


    def atualizar_saida(self):
        try:
            # Limpa a tabela antes de carregar os novos dados
            self.table_saida.setRowCount(0)
            
            # Consulta os dados da tabela de saída no banco de dados (agrupando os produtos iguais)
            query = """
            SELECT 
                Produto, 
                SUM(Quantidade) as Quantidade, 
                "Valor do Produto", 
                Desconto,
                "Valor Total", 
                "Data de Saída", 
                "Data da Criação", 
                "Código do Produto", 
                Cliente, 
                "Descrição do Produto", 
                Usuário,  
                "Status da Saída"
            FROM products_saida
            WHERE "Status da Saída" = 1
            GROUP BY 
                Produto, 
                "Valor do Produto", 
                Desconto,
                "Valor Total", 
                "Data de Saída", 
                "Data da Criação", 
                "Código do Produto", 
                Cliente, 
                "Descrição do Produto", 
                Usuário, 
                "Status da Saída"
            """

            saidas = self.db.executar_query(query)  # Método que executa a consulta e retorna os resultados

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
        caminho, _ = QFileDialog.getSaveFileName(
            None,
            "Salvar PDF",
            "relatorio.pdf",
            "PDF files (*.pdf)"
        )
        if not caminho:
            return
        try:
            c = canvas.Canvas(caminho, pagesize=A4)
            width, height = A4

            #Título
            c.setFont("Helvetica-Bold", 16)
            c.drawString(50, height - 50, "Relatório de Produtos")

            # Cabeçalhos
            c.setFont("Helvetica-Bold", 10)
            headers = ["Produto", "Quantidade", "Valor", "Desconto", 
                       "Data", "Código", "Cliente", "Descrição", "Usuário"]
            y = height - 80
            for i, header in enumerate(headers):
                c.drawString(50 + i * 60, y, header)

            # Dados da tabela
            c.setFont("Helvetica", 9)
            for row in range(self.main_window.table_base.rowCount()):
                y -= 20
                if y < 50:
                    c.showPage()
                    y = height - 50
                    c.setFont("Helvetica-Bold", 10)
                    for i, header in enumerate(headers):
                        c.drawString(50 + i * 60, y, header)
                    y -= 20
                    c.setFont("Helvetica", 9)

                for col in range(9):  # Assume 9 colunas
                    item = self.main_window.table_base.item(row, col)
                    texto = item.text() if item else ""
                    texto = item.text() if item else ""
                    c.drawString(50 + col * 60, y, str(texto)[:15])  # Garante que é string


            c.save()

            # Mensagem de sucesso
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("PDF Gerado")
            msg.setText("O PDF foi gerado com sucesso!")
            msg.exec()

        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erro")
            msg.setText(f"Erro ao gerar PDF: {str(e)}")
            msg.exec()



    def exibir_historico(self):
        # Criação da nova janela de histórico como QMainWindow
        self.janela_historico = QMainWindow()
        self.janela_historico.setWindowTitle("Histórico de Ações")
        self.janela_historico.resize(800, 650)

        def fechar_janela_historico(evento):
            self.coluna_checkboxes_adicionada = False
            evento.accept()

        self.janela_historico.closeEvent = fechar_janela_historico # Liga a função fechar janela do histórico

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

        # Botão Exportar CSV
        botao_exportar_csv = QPushButton("Exportar para CSV")
        botao_exportar_csv.clicked.connect(self.exportar_csv)

        
        # Botão Exportar Excel
        botao_exportar_excel = QPushButton("Exportar para Excel")
        botao_exportar_excel.clicked.connect(self.exportar_excel)

        # Botão PDF
        botao_exportar_pdf = QPushButton("Exportar PDF")
        botao_exportar_pdf.clicked.connect(self.exportar_pdf)

        botao_pausar_historico = QPushButton("Pausar Histórico")
        botao_pausar_historico.clicked.connect(self.pausar_historico)


        botao_filtrar_historico = QPushButton("Filtrar Histórico")
        botao_filtrar_historico.clicked.connect(self.filtrar_historico)

        botao_ordenar_historico = QPushButton("Ordenar Histórico")
        botao_ordenar_historico.clicked.connect(self.ordenar_historico)


        # Criar checkbox "Selecionar Individualmente" toda vez que a janela for aberta
        self.checkbox_selecionar = QCheckBox("Selecionar")
        self.checkbox_selecionar.stateChanged.connect(self.selecionar_individual)

        # Adicionar outros botões ao layout
        layout.addWidget(botao_atualizar)
        layout.addWidget(botao_apagar)
        layout.addWidget(botao_exportar_csv)
        layout.addWidget(botao_exportar_excel)
        layout.addWidget(botao_exportar_pdf)
        layout.addWidget(botao_pausar_historico)
        layout.addWidget(botao_ordenar_historico)
        layout.addWidget(botao_filtrar_historico)
        layout.addWidget(self.checkbox_selecionar)
        layout.addWidget(self.tabela_historico)
        


        # Configurar o widget central e exibir a janela
        self.janela_historico.setCentralWidget(central_widget)
        self.janela_historico.show()

        # Preencher tabela pela primeira vez
        self.carregar_historico()
        self.tabela_historico.resizeColumnsToContents()
    

    def carregar_historico(self):
        with sqlite3.connect('banco_de_dados.db') as cn:
            cursor = cn.cursor()
            cursor.execute('SELECT * FROM historico ORDER BY "Data e Hora" DESC')
            registros = cursor.fetchall()

        self.tabela_historico.clearContents()
        self.tabela_historico.setRowCount(len(registros))

        deslocamento = 1 if self.coluna_checkboxes_adicionada else 0
        self.checkboxes = []  # Zerar e recriar lista de checkboxes

        for i, (data, usuario, acao, descricao) in enumerate(registros):
            if self.coluna_checkboxes_adicionada:
                checkbox = QCheckBox()
                checkbox.setStyleSheet("margin-left:9px; margin-right:9px;")
                self.tabela_historico.setCellWidget(i,0,checkbox)
                self.checkboxes.append(checkbox)
            self.tabela_historico.setItem(i, 0 + deslocamento, QTableWidgetItem(data))
            self.tabela_historico.setItem(i, 1 + deslocamento, QTableWidgetItem(usuario))
            self.tabela_historico.setItem(i, 2 + deslocamento, QTableWidgetItem(acao))
            self.tabela_historico.setItem(i, 3 + deslocamento, QTableWidgetItem(descricao))



    def atualizar_historico(self):
        QMessageBox.information(self.janela_historico, "Sucesso", "Dados carregados com sucesso!")
        self.carregar_historico()

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

    def apagar_historico(self):
        # Caso checkboxes estejam ativados
        if self.coluna_checkboxes_adicionada and self.checkboxes:
            linhas_para_remover = []
            ids_para_remover = []

            # Identificar as linhas com checkboxes selecionados
            for row, checkbox in enumerate(self.checkboxes):
                if checkbox and checkbox.isChecked():
                    linhas_para_remover.append(row)
                    coluna_data_hora = 1 if not self.coluna_checkboxes_adicionada else 2
                    item_data_widget = self.tabela_historico.item(row, coluna_data_hora)  # Coluna de Data/Hora
                    if item_data_widget:
                        item_data_text = item_data_widget.text().strip()
                        # Excluir com base na data e hora
                        if item_data_text:
                            ids_para_remover.append(item_data_text)
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
                    for data_hora in ids_para_remover:
                        cursor.execute("DELETE FROM historico WHERE 'Data e Hora' = ?", (data_hora,))
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
            coluna_data_hora = 0 if not self.coluna_checkboxes_adicionada else 1
            item_data_widget = self.tabela_historico.item(linha_selecionada, coluna_data_hora)  # Coluna de Data/Hora
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

                    if item_data_text:
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
                    cursor.execute("DELETE FROM historico WHERE 'Data e Hora' = ?", (item_id,))
                    print(f"Item removido do banco de dados: ID {item_id}")
                    cn.commit()
                except Exception as e:
                    QMessageBox.critical(self, "Erro", f"Erro ao excluir do banco de dados: {e}")
                    return

            # Remover a linha da interface
            self.tabela_historico.removeRow(linha_selecionada)

            QMessageBox.information(self, "Sucesso", "Item removido com sucesso!")
    
    # Função para desmarcar todos os checkboxes
    def desmarcar_checkboxes(self):
        for checkbox in self.checkboxes:
            if checkbox:
                checkbox.setChecked(False)
    
    def selecionar_todos(self):
        if not self.coluna_checkboxes_adicionada:
            QMessageBox.warning(self, "Aviso", "Ative a opção 'Selecionar Individualmente' antes.")
            if hasattr(self, "checkbox_header"):
                self.checkbox_header.setChecked(False)
            return

        estado = self.checkbox_header.checkState() == Qt.Checked
        self.checkboxes.clear()  # Reinicia a lista para manter consistência
        
        for row in range(self.tabela_historico.rowCount()):
            widget = self.tabela_historico.cellWidget(row, 0)
            if widget is not None:
                checkbox = widget.findChild(QCheckBox)
                if checkbox:
                    checkbox.blockSignals(True)
                    checkbox.setChecked(estado)
                    checkbox.blockSignals(False)



     # Função para adicionar checkboxes selecionar_individual na tabela de histórico
    def selecionar_individual(self):
        if self.tabela_historico.rowCount() == 0:
            QMessageBox.warning(self, "Aviso", "Nenhum histórico para selecionar.")
            self.checkbox_selecionar_individual.setChecked(False)
            return

        if self.coluna_checkboxes_adicionada:
            self.tabela_historico.removeColumn(0)
            self.tabela_historico.verticalHeader().setVisible(True)
            self.coluna_checkboxes_adicionada = False

            if hasattr(self, "checkbox_header"):
                self.checkbox_header.deleteLater()
                del self.checkbox_header

            self.checkboxes.clear()
            return

        self.tabela_historico.insertColumn(0)
        self.tabela_historico.setHorizontalHeaderItem(0, QTableWidgetItem(""))
        self.tabela_historico.setColumnWidth(0, 30)
        self.tabela_historico.horizontalHeader().setMinimumSectionSize(30)
        self.tabela_historico.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)

        # Checkbox do cabeçalho
        self.checkbox_header = QCheckBox(self.tabela_historico)
        self.checkbox_header.setToolTip("Selecionar todos")
        self.checkbox_header.setChecked(False)
        self.checkbox_header.stateChanged.connect(self.selecionar_todos)
        self.checkbox_header.setFixedSize(20, 20)
        self.checkbox_header.show()

        header = self.tabela_historico.horizontalHeader()
        self.atualizar_posicao_checkbox_header()
        header.sectionResized.connect(self.atualizar_posicao_checkbox_header)

        self.checkboxes.clear()

        QTimer.singleShot(0,self.atualizar_posicao_checkbox_header)

        for row in range(self.tabela_historico.rowCount()):
            checkbox = QCheckBox()
            checkbox.stateChanged.connect(self.atualizar_selecao_todos)

            container = QWidget()
            layout = QHBoxLayout(container)
            layout.addWidget(checkbox)
            layout.setAlignment(Qt.AlignCenter)
            layout.setContentsMargins(0, 0, 0, 0)

            self.tabela_historico.setCellWidget(row, 0, container)
            self.checkboxes.append(checkbox)

        self.tabela_historico.verticalHeader().setVisible(False)
        self.coluna_checkboxes_adicionada = True

    def atualizar_selecao_todos(self):
        self.checkbox_header.blockSignals(True)

        all_checked = all(checkbox.isChecked() for checkbox in self.checkboxes if checkbox)
        any_checked = any(checkbox.isChecked() for checkbox in self.checkboxes if checkbox)

        if all_checked:
            self.checkbox_header.setCheckState(Qt.Checked)
        elif any_checked:
            self.checkbox_header.setCheckState(Qt.PartiallyChecked)
        else:
            self.checkbox_header.setCheckState(Qt.Unchecked)

        self.checkbox_header.blockSignals(False)

        
    def atualizar_posicao_checkbox_header(self):
        if hasattr(self, "checkbox_header") and self.coluna_checkboxes_adicionada:
            header = self.tabela_historico.horizontalHeader()

            x = header.sectionViewportPosition(0) + (header.sectionSize(0) - self.checkbox_header.width()) // 2 + 4
            y = (header.height() - self.checkbox_header.height()) // 2

            self.checkbox_header.move(x, y)


    def ordenar_historico(self):
        if hasattr(self, "checkbox_header"):
            QMessageBox.warning(
                None,
                "Aviso",
                "Desmarque o checkbox antes de ordenar o histórico."
            )
            return
        # Obter a coluna pela qual o usuário deseja ordenar
        coluna = self.obter_coluna_para_ordenar()  # Função fictícia para capturar escolha
        if coluna is None:
            return  # Cancela o processo todo
        
        # Determinar a direção de ordenação (ascendente ou descendente)
        direcao = self.obter_direcao_ordenacao()  # Função fictícia para capturar escolha
        if direcao is None:
            return  # Cancela o processo todo
        
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
        if hasattr(self,"checkbox_header"):
            QMessageBox.warning(
                None,
                "Aviso",
                "Desmarque o checkbox antes de filtrar o histórico."
            )
            return
        
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
        self.remover_coluna_selecao() # Remove os checkboxes se estiverem ativos
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
            self.tabela_historico.setItem(i, 0, QTableWidgetItem(row[0]))  # Data/Hora
            self.tabela_historico.setItem(i, 1, QTableWidgetItem(row[1]))  # Usuário
            self.tabela_historico.setItem(i, 2, QTableWidgetItem(row[2]))  # Ação
            self.tabela_historico.setItem(i, 3, QTableWidgetItem(row[3]))  # Descrição

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

        
        # Alterar o texto da line_excel para "Carregando arquivo Excel..."
        self.line_excel.setText("Carregando arquivo Excel...")
        self.nome_arquivo_excel = nome_arquivo  # Salva para usar depois

        # Inicializar a barra de progresso
        self.progress_excel.setValue(0)
        self.progresso = 0
        

        # Começar o timer para simular carregamento visual
        self.timer_excel = QTimer()
        self.timer_excel.timeout.connect(self.atualizar_progress_excel)
        self.timer_excel.start(20)

    def atualizar_progress_excel(self):
        if self.progresso < 100:
            self.progresso += 1
            self.progress_excel.setValue(self.progresso)
        else:
            self.timer_excel.stop()

            try:
                df = pd.read_excel(self.nome_arquivo_excel, engine="openpyxl", header=0)
                df = df.fillna("Não informado")

                colunas_table_base = ["Produto", "Quantidade", "Valor do Produto", "Desconto", "Data da Compra",
                                    "Código do Item", "Cliente", "Descrição do Produto", "Usuário"]

                if df.shape[1] != len(colunas_table_base):
                    QMessageBox.warning(self, "Erro", "O número de colunas no arquivo Excel não corresponde ao número esperado.")
                    self.line_excel.clear()
                    # Zerando a barra de progresso
                    self.progress_excel.setValue(0)
                    self.progresso = 0  # Resetando a variável de progresso
                    return

                if df.shape[0] == 0:
                    QMessageBox.warning(self, "Erro", "O arquivo Excel está vazio.")
                    self.line_excel.clear()
                    # Zerando a barra de progresso
                    self.progress_excel.setValue(0)
                    self.progresso = 0  # Resetando a variável de progresso
                    return
                

                self.table_base.setRowCount(0)

                df["Valor do Produto"] = pd.to_numeric(df.iloc[:, 2], errors="coerce").fillna(0)
                df["Valor do Produto"] = df["Valor do Produto"].apply(
                    lambda x: f"R$ {x:,.2f}".replace(",", "_").replace(".", ",").replace("_", ".")
                )

                df["Desconto"] = pd.to_numeric(df.iloc[:, 3], errors="coerce").fillna(0)
                df["Desconto"] = df["Desconto"].apply(
                    lambda x: f"{x:.2f}%" if x < 1 else f"{x * 100:.2f}%"
                )

                if "Data da Compra" in df.columns:
                    df["Data da Compra"] = pd.to_datetime(df["Data da Compra"], errors="coerce").dt.strftime('%d/%m/%Y')
                else:
                    df["Data da Compra"] = ""

                for row in df.itertuples(index=False):
                    row_position = self.table_base.rowCount()
                    self.table_base.insertRow(row_position)
                    for column, value in enumerate(row):
                        item = self.criar_item(str(value))
                        self.table_base.setItem(row_position, column, item)

                QMessageBox.information(self, "Sucesso", "Arquivo Excel importado com sucesso!")

            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Erro ao importar o arquivo Excel: {e}")

            # Quando o arquivo for carregado, atualizar o texto da line_excel com o caminho do arquivo
            self.line_excel.setText(self.nome_arquivo_excel)

            # Zerando a barra de progresso
            self.progress_excel.setValue(0)
            self.progresso = 0  # Resetando a variável de progresso

    def importar_produto(self):
        # Verificar se a tabela está vazia
        if self.table_base.rowCount() == 0 and self.table_saida.rowCount() == 0:
            QMessageBox.warning(self, "Aviso", "Nenhum dado encontrado para gerar arquivo Excel.")
            return  # Se a tabela estiver vazia, encerra a função sem prosseguir
        
        nome_arquivo, _ = QFileDialog.getSaveFileName(
            self,
            "Salvar Arquivo Excel",
            "relatório.xlsx",
            "Arquivos Excel (*.xlsx)"

        )

        if not nome_arquivo:
            return
        
        # Garantir que o arquivo tenha extensão .xlsx
        if not nome_arquivo.endswith(".xlsx"):
            nome_arquivo += ".xlsx"

        try:
            with pd.ExcelWriter(nome_arquivo, engine="openpyxl") as writer:
                def tabela_para_dataframe(tabela):
                    dados = []
                    cabecalhos = [tabela.horizontalHeaderItem(col).text() for col in range(tabela.columnCount())]
                    for linha in range(tabela.rowCount()):
                        linha_dados = []
                        for coluna in range(tabela.columnCount()):
                            item = tabela.item(linha, coluna)
                            linha_dados.append(item.text() if item else "")
                        dados.append(linha_dados)
                    return pd.DataFrame(dados, columns=cabecalhos)
                
                # Converter e salvar a tabela de estoque
                if self.table_base.rowCount() > 0:
                    df_saida = tabela_para_dataframe(self.table_base)
                    df_saida.to_excel(writer, sheet_name="Estoque", index=False)
                
                # Converter e salvar a tabela de saída
                if self.table_saida.rowCount() > 0:
                    df_estoque = tabela_para_dataframe(self.table_saida)
                    df_estoque.to_excel(writer, sheet_name="Saída", index=False)
        
            QMessageBox.information(self, "Sucesso", f"Arquivo Excel gerado com sucesso em:\n{nome_arquivo}")
        
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao salvar arquivo Excel: {str(e)}")


    
    def incluir_produto_no_sistema(self):
        selected_rows = self.main_window.table_base.selectionModel().selectedRows()

        if not hasattr(self, 'nome_arquivo_excel') or not self.nome_arquivo_excel:
            QMessageBox.warning(self, "Aviso", "Você precisa carregar uma planilha antes de cadastrar os produtos no sistema.")
            return

        if not selected_rows:
            QMessageBox.critical(self, "Aviso", "Nenhum produto selecionado para gerar saída!")
            return False

        try:
            conn = sqlite3.connect("banco_de_dados.db")
            cursor = conn.cursor()

            for model_index in selected_rows:
                row_index = model_index.row()
                row_data = []
                for col in range(self.main_window.table_base.columnCount()):
                    item = self.main_window.table_base.item(row_index, col)
                    row_data.append(item.text() if item else "")

                # Desempacotar os dados corretamente
                produto = row_data[0]
                quantidade = row_data[1]
                valor_real = row_data[2]
                desconto = row_data[3]
                data_cadastro = row_data[4]
                codigo_item = row_data[5]
                cliente = row_data[6]
                descricao = row_data[7]
                usuario = row_data[8]

                cursor.execute("""
                    INSERT INTO products (Produto, Quantidade, Valor_Real, Desconto, "Data do Cadastro", Código_Item, 
                            Cliente, Descrição_Produto, Usuário) 
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (produto, quantidade, valor_real, desconto, data_cadastro, codigo_item, 
                    cliente, descricao, usuario))

            conn.commit()
            conn.close()
            QMessageBox.information(self, "Sucesso", "Produto(s) incluído(s) com sucesso no sistema.")

            # Registrar histórico
            descricao = f"Produto '{produto}' foi incluído no sistema."
            self.main_window.registrar_historico( "Inclusão de produto",descricao)


        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao incluir o produto no sistema:\n{e}")



    # Limpa a coluna selecionada clicando em qualquer lugar da tabela
    def eventFilter(self, source, event):
        if event.type() == QEvent.MouseButtonPress:
            if source == self.main_window.table_base.viewport():
                index = self.main_window.table_base.indexAt(event.pos())
                if not index.isValid():
                    self.main_window.table_base.clearSelection()
                    self.main_window.table_base.clearFocus()

            elif source == self.main_window.table_saida.viewport():
                index = self.main_window.table_saida.indexAt(event.pos())
                if not index.isValid():
                    self.main_window.table_saida.clearSelection()
                    self.main_window.table_saida.clearFocus()

        return super().eventFilter(source, event)

    def abrir_planilha_em_massa_produtos(self):
        # Abrir o diálogo para selecionar o arquivo Excel
        nome_arquivo, _ = QFileDialog.getOpenFileName(self, "Abrir Arquivo Excel", "", "Arquivos Excel (*.xlsx)")

        # Se o usuário cancelar a seleção do arquivo
        if not nome_arquivo:
            return
        
        # Alterar o texto da line_excel para "Carregando arquivo Excel..."
        self.line_edit_massa_produtos.setText("Carregando arquivo Excel...")
        self.nome_arquivo_excel_massa = nome_arquivo

        # Inicializar a barra de progresso
        self.progress_massa_produtos.setValue(0)
        self.progresso_massa = 0

        # Começar o timer para simular carregamento visual
        self.timer_excel_massa = QTimer()
        self.timer_excel_massa.timeout.connect(self.atualizar_progress_excel_massa)
        self.timer_excel_massa.start(20)

    def atualizar_progress_excel_massa(self):
        if self.progresso_massa < 100:
            self.progresso_massa += 1
            self.progress_massa_produtos.setValue(self.progresso_massa)
        else:
            self.timer_excel_massa.stop()
            try:
                df = pd.read_excel(self.nome_arquivo_excel_massa, engine="openpyxl", header=0)
                df = df.fillna("Não informado")

                coluna_table_massa_produtos = ["Produto", "Quantidade", "Valor do Produto", "Desconto", "Data da Compra",
                                            "Código do Item", "Cliente", "Descrição do Produto"]
                if df.shape[1] != len(coluna_table_massa_produtos):
                    QMessageBox.warning(self, "Erro", "O número de colunas no arquivo Excel não corresponde ao número esperado.")
                    self.line_edit_massa_produtos.clear()
                    # Zerando a barra de progresso
                    self.progress_massa_produtos.setValue(0)
                    self.progresso_massa = 0
                    return
                if df.shape[0] == 0:
                    QMessageBox.warning(self, "Erro", "O arquivo Excel está vazio.")
                    self.line_edit_massa_produtos.clear()
                    # Zerando a barra de progresso
                    self.progress_massa_produtos.setValue(0)
                    self.progresso_massa = 0
                    return
                self.table_massa_produtos.setRowCount(0)

                if df["Valor do Produto"].dtype != object or not df["Valor do Produto"].iloc[0].startswith("R$"):
                    df["Valor do Produto"] = pd.to_numeric(df["Valor do Produto"], errors="coerce").fillna(0)
                    df["Valor do Produto"] = df["Valor do Produto"].apply(
                        lambda x: f"R$ {x:,.2f}".replace(",", "_").replace(".", ",").replace("_", ".")
                    )


                df["Desconto"] = pd.to_numeric(df.iloc[:, 3], errors="coerce").fillna(0)
                df["Desconto"] = df["Desconto"].apply(
                    lambda x: "Sem desconto" if x == 0  else f"{x:.2f}%" if x < 1 else f"{x / 100:.2f}%"
                )

                if "Data da Compra" in df.columns:
                    df["Data da Compra"] = pd.to_datetime(df["Data da Compra"], errors="coerce").dt.strftime('%d/%m/%Y')
                else:
                    df["Data da Compra"] = ""
                for _, row in df.iterrows():
                    row_position = self.table_massa_produtos.rowCount()
                    self.table_massa_produtos.insertRow(row_position)
                    for column, value in enumerate(row):
                        item = self.formatar_texto_produtos_em_massa(str(value))
                        self.table_massa_produtos.setItem(row_position, column, item)
                QMessageBox.information(self, "Sucesso", "Arquivo Excel importado com sucesso!")
            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Erro ao importar o arquivo Excel: {e}")
            # Quando o arquivo for carregado, atualizar o texto da line_excel com o caminho do arquivo
            self.line_edit_massa_produtos.setText(self.nome_arquivo_excel_massa)

            # Zerando a barra de progresso
            self.progress_massa_produtos.setValue(0)
            self.progresso_massa = 0
            self.table_massa_produtos.resizeColumnsToContents()  # Ajusta a largura das colunas para o conteúdo
            self.table_massa_produtos.resizeRowsToContents()

    def formatar_texto_produtos_em_massa(self, texto):
        item = QTableWidgetItem(texto)
        item.setTextAlignment(Qt.AlignCenter)  # Centraliza o texto
        item.setForeground(QBrush(QColor("white"))) 
        return item
    
    def cadastrar_produtos_em_massa(self):
        try:
            total_linhas = self.table_massa_produtos.rowCount()
            if total_linhas == 0:
                QMessageBox.warning(self, "Aviso", "Nenhum produto encontrado para cadastrar.")
                return
            for linha in range(total_linhas):
                produto = self.table_massa_produtos.item(linha, 0).text()
                quantidade = self.table_massa_produtos.item(linha, 1).text()

              

                # Tratamento do valor (remover R$ e converter para float)
                valor_str = self.table_massa_produtos.item(linha, 2).text().replace("R$", "").replace(".", "").replace(",", ".").strip()
                valor_float = float(valor_str) if valor_str else 0.0
                valor_produto = f"R$ {valor_float:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

                # Desconto: tratar "Sem desconto" como 0
                desconto_str = self.table_massa_produtos.item(linha, 3).text().replace("%", "").replace(",", ".").strip()
                desconto = 0.0 if desconto_str.lower() == "sem desconto" else float(desconto_str)

                data_cadastro = self.table_massa_produtos.item(linha, 4).text()
                cliente = self.table_massa_produtos.item(linha, 6).text()
                descricao_produto = self.table_massa_produtos.item(linha, 7).text()
                
                 # Valor total vindo da coluna 5 (ajuste se estiver em outra)
                valor_total_str = self.table_massa_produtos.item(linha, 5).text().replace("R$", "").replace(".", "").replace(",", ".").strip()
                valor_total_float = float(valor_total_str) if valor_total_str else 0.0
                valor_total = f"R$ {valor_total_float:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

                # Gerar código aleatório para cada produto
                codigo_aleatorio = self.main_window.gerar_codigo_aleatorio()

                produto_info = {
                    "produto": produto,
                    "quantidade": quantidade,
                    "valor_produto": valor_produto,
                    "desconto": desconto,
                    "valor_total":valor_total,
                    "data_cadastro": data_cadastro,
                    "codigo_item": codigo_aleatorio,
                    "cliente": cliente,
                    "descricao_produto": descricao_produto
                }
                self.main_window.inserir_produto_no_bd(produto_info,registrar_historico=False)

                # Registrar no histórico para o cadastro em massa
                descricao = f"Produto {produto} foi cadastrado com quantidade {quantidade} e valor {valor_produto}!"
                self.main_window.registrar_historico("Cadastro em Massa", descricao)

            QMessageBox.information(self, "Sucesso", "Produtos cadastrados com sucesso!")
            self.line_edit_massa_produtos.clear()

            # Limpar a tabela após a inserção
            self.table_massa_produtos.setRowCount(0)

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao cadastrar produtos em massa:\n{e}")

    
    





