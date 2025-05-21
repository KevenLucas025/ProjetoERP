from PySide6.QtWidgets import (QWidget,QTableWidget,QMessageBox,
                               QTableWidgetItem,QInputDialog,QLineEdit,QCheckBox,
                               QFileDialog,QMainWindow,QVBoxLayout,QPushButton,QHBoxLayout,
                               QLabel,QRadioButton,QGroupBox,QDialog)
from PySide6.QtGui import QBrush,QColor,QGuiApplication
from PySide6.QtCore import Qt,QEvent,QTimer
from database import DataBase
import sqlite3
import pandas as pd
import csv
from datetime import datetime
from configuracoes import Configuracoes_Login
from reportlab.lib.pagesizes import letter,landscape,A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle,Spacer,Paragraph
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from openpyxl.utils import get_column_letter
from openpyxl.styles import Alignment, Font


class Pagina_Usuarios(QWidget):
    def __init__(self,main_window,btn_abrir_planilha_usuarios,btn_cadastrar_novo_usuario,btn_gerar_pdf_usuario,
                  btn_historico_usuarios,btn_atualizar_ativos,btn_atualizar_inativos,btn_limpar_tabelas_usuarios,
                  btn_gerar_saida_usuarios,line_excel_usuarios,progress_excel_usuarios,
                  btn_importar_usuarios,btn_abrir_planilha_massa_usuarios,btn_fazer_cadastro_massa_usuarios,
                  progress_massa_usuarios,line_edit_massa_usuarios,parent=None):
        super().__init__(parent)

        self.db = DataBase("banco_de_dados.db")
        self.alteracoes_salvas = False


        self.checkboxes = []  # Lista para armazenar os checkboxes
        self.coluna_checkboxes_usuarios_adicionada = False
        self.todos_selecionados = False
      
        

        self.main_window = main_window
        self.table_ativos = self.main_window.table_ativos  # Referência para a tabela no main window
        self.table_inativos = self.main_window.table_inativos
        self.table_massa_usuarios = self.main_window.table_massa_usuarios
        self.btn_abrir_planilha_usuarios = btn_abrir_planilha_usuarios
        self.btn_cadastrar_novo_usuario = btn_cadastrar_novo_usuario
        self.btn_gerar_pdf_usuario = btn_gerar_pdf_usuario
        self.btn_historico_usuarios = btn_historico_usuarios
        self.btn_atualizar_ativos = btn_atualizar_ativos
        self.btn_atualizar_inativos = btn_atualizar_inativos
        self.btn_limpar_tabelas_usuarios = btn_limpar_tabelas_usuarios
        self.btn_gerar_saida_usuarios = btn_gerar_saida_usuarios
        self.line_excel_usuarios = line_excel_usuarios
        self.progress_excel_usuarios = progress_excel_usuarios
        self.btn_importar_usuarios = btn_importar_usuarios
        self.btn_abrir_planilha_massa_usuarios = btn_abrir_planilha_massa_usuarios
        self.btn_fazer_cadastro_massa_usuarios = btn_fazer_cadastro_massa_usuarios
        self.progress_massa_usuarios = progress_massa_usuarios
        self.line_edit_massa_usuarios = line_edit_massa_usuarios
        
        

        self.btn_gerar_saida_usuarios.clicked.connect(self.confirmar_saida_usuarios)
        self.btn_limpar_tabelas_usuarios.clicked.connect(self.limpar_tabelas)
        self.btn_atualizar_ativos.clicked.connect(self.atualizar_ativos)
        self.btn_atualizar_inativos.clicked.connect(self.atualizar_inativos)
        self.btn_gerar_pdf_usuario.clicked.connect(self.exibir_pdf_usuarios)
        self.btn_historico_usuarios.clicked.connect(self.exibir_tabela_historico_usuario)
        self.btn_abrir_planilha_usuarios.clicked.connect(self.abrir_planilha_usuarios)
        self.btn_importar_usuarios.clicked.connect(self.importar_usuario)
        self.btn_abrir_planilha_massa_usuarios.clicked.connect(self.abrir_panilha_usuarios_em_massa)
        self.btn_fazer_cadastro_massa_usuarios.clicked.connect(self.cadastrar_usuarios_em_massa)
        self.main_window.table_ativos.viewport().installEventFilter(self)
        self.main_window.table_inativos.viewport().installEventFilter(self)



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
        Telefone,"Data de Nascimento","Última Troca de Senha","Data da Senha Cadastrada","Data da Inclusão do Usuário",Segredo
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
            nome = self.main_window.table_ativos.item(row, 1)
            if nome:
                self.main_window.table_ativos.setItem(row_index, 1, self.formatar_texto(nome.text()))

            # Usuário
            usuario = self.main_window.table_ativos.item(row, 2)
            if usuario:
                self.main_window.table_ativos.setItem(row_index, 2, self.formatar_texto(usuario.text()))

            # Senha
            senha = self.main_window.table_ativos.item(row, 3)
            if senha:
                self.main_window.table_ativos.setItem(row_index, 3, self.formatar_texto(senha.text()))

            # Confirmar Senha
            confirmar_senha = self.main_window.table_ativos.item(row, 4)
            if confirmar_senha:
                self.main_window.table_ativos.setItem(row_index, 4, self.formatar_texto(confirmar_senha.text()))

            # Acesso
            acesso = self.main_window.table_ativos.item(row, 5)
            if acesso:
                self.main_window.table_ativos.setItem(row_index, 5, self.formatar_texto(acesso.text()))

            # Endereço
            endereco = self.main_window.table_ativos.item(row, 6)
            if endereco:
                self.main_window.table_ativos.setItem(row_index, 6, self.formatar_texto(endereco.text()))

            # CEP
            cep = self.main_window.table_ativos.item(row, 7)
            if cep:
                self.main_window.table_ativos.setItem(row_index, 7, self.formatar_texto(cep.text()))

            # CPF
            cpf = self.main_window.table_ativos.item(row, 8)
            if cpf:
                self.main_window.table_ativos.setItem(row_index, 8, self.formatar_texto(cpf.text()))

            # Número
            numero = self.main_window.table_ativos.item(row, 9)
            if numero:
                self.main_window.table_ativos.setItem(row_index, 9, self.formatar_texto(numero.text()))

            # Estado
            estado = self.main_window.table_ativos.item(row, 10)
            if estado:
                self.main_window.table_ativos.setItem(row_index, 10, self.formatar_texto(estado.text()))

            # E-mail
            email = self.main_window.table_ativos.item(row, 11)
            if email:
                self.main_window.table_ativos.setItem(row_index, 11, self.formatar_texto(email.text()))

            # Complemento
            complemento = self.main_window.table_ativos.item(row, 12)
            if complemento:
                self.main_window.table_ativos.setItem(row_index, 12, self.formatar_texto(complemento.text()))

            # Telefone
            telefone = self.main_window.table_ativos.item(row, 13)
            if telefone:
                self.main_window.table_ativos.setItem(row_index, 13, self.formatar_texto(telefone.text()))

            # Data de Nascimento
            data_nascimento = self.main_window.table_ativos.item(row, 14)
            if data_nascimento:
                self.main_window.table_ativos.setItem(row_index, 14, self.formatar_texto(data_nascimento.text()))

            # RG
            rg = self.main_window.table_ativos.item(row, 15)
            if rg:
                self.main_window.table_ativos.setItem(row_index, 15, self.formatar_texto(rg.text()))

            # Última Troca de Senha
            ultima_troca_senha = self.main_window.table_ativos.item(row, 16)
            if ultima_troca_senha:
                self.main_window.table_ativos.setItem(row_index, 16, self.formatar_texto(ultima_troca_senha.text()))

            # Data da Senha Cadastrada
            data_senha_cadastrada = self.main_window.table_ativos.item(row, 17)
            if data_senha_cadastrada:
                self.main_window.table_ativos.setItem(row_index, 17, self.formatar_texto(data_senha_cadastrada.text()))

            # Data da Inclusão do Usuário
            data_inclusao_usuario = self.main_window.table_ativos.item(row, 18)
            if data_inclusao_usuario:
                self.main_window.table_ativos.setItem(row_index, 18, self.formatar_texto(data_inclusao_usuario.text()))

            # Data da Inatividade do Usuário
            data_inatividade_usuario = self.main_window.table_ativos.item(row, 19)
            if data_inatividade_usuario:
                self.main_window.table_ativos.setItem(row_index, 19, self.formatar_texto(data_inatividade_usuario.text()))

            # Segredo
            segredo = self.main_window.table_ativos.item(row, 20)
            if segredo:
                self.main_window.table_ativos.setItem(row_index, 20, self.formatar_texto(segredo.text()))

            # Usuário Logado
            usuario_logado = self.main_window.table_ativos.item(row, 21)
            if usuario_logado:
                self.main_window.table_ativos.setItem(row_index, 21, self.formatar_texto(usuario_logado.text()))

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

        # Abre a conexão com o banco de dados
        conexao = self.db.connecta()
        cursor = conexao.cursor()

        for row in usuarios_selecionados:
            dados_usuario = []
            for coluna in range(21):
                item = self.main_window.table_ativos.item(row, coluna)
                dados_usuario.append(item.text() if item else "")

            # Atualiza a coluna 18 com a data/hora da saída
            dados_usuario[18] = datetime.now().strftime("%d/%m/%Y %H:%M")

            # Coluna 19: Segredo
            item_segredo = self.main_window.table_ativos.item(row, 18)
            dados_usuario[19] = item_segredo.text() if item_segredo else ""

            # Coluna 20: Usuário logado
            item_usuario_logado = self.main_window.table_ativos.item(row, 19)
            dados_usuario[20] = item_usuario_logado.text() if item_usuario_logado else "Desconhecido"

            id_usuario = dados_usuario[1]
            imagem = self.recuperar_imagem_usuario_bd_users(id_usuario)

            dados_com_imagem = dados_usuario[:15] + [imagem] + dados_usuario[15:]


            # Inserção no banco de dados users_inativos
            cursor.execute("""
                INSERT INTO users_inativos (
                    Nome, Usuário, Senha, "Confirmar Senha",CEP,  Endereço,Número,Cidade,Bairro,Estado,Complemento,Telefone, 
                    Email,"Data de Nascimento",RG, CPF,CNPJ, Imagem, "Última Troca de Senha","Data da Senha Cadastrada", 
                    "Data da Inclusão do Usuário", "Data da Inatividade do Usuário",Segredo, "Usuário Logado",Acesso
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?,?,?)
            """, dados_com_imagem)

            # Exclui o usuário da tabela users usando o CPF
            cpf = dados_usuario[7]
            cursor.execute("DELETE FROM users WHERE CPF = ?", (cpf,))

            saida_usuarios.append(tuple(dados_usuario))
            historico_logs.append(f"Usuário {dados_usuario[0]} gerado para saída.")

        conexao.commit()

        for texto in historico_logs:
            self.main_window.registrar_historico("Gerado Saída de Usuário", texto)

        if saida_usuarios:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle("Aviso")
            msg_box.setText("Saída do(s) usuário(s) gerada com sucesso!")
            msg_box.exec()
            self.tabela_inativos_preencher(saida_usuarios)
            # Ajusta colunas e linhas automaticamente após preencher
            self.main_window.table_inativos.resizeColumnsToContents()
            self.main_window.table_inativos.resizeRowsToContents()



    def tabela_inativos_preencher(self, dados_saida):
        for item in dados_saida:
            row_position = self.main_window.table_inativos.rowCount()
            self.main_window.table_inativos.insertRow(row_position)

            for col in range(21):
                if col < len(item):
                    self.main_window.table_inativos.setItem(row_position, col, self.formatar_texto(item[col]))
        # Ajusta colunas e linhas automaticamente após preencher
        self.main_window.table_inativos.resizeColumnsToContents()
        self.main_window.table_inativos.resizeRowsToContents()


    def confirmar_saida_usuarios(self):
        configuracoes = Configuracoes_Login(self.main_window)
        if configuracoes.nao_mostrar_aviso_irreversivel:
            pass
        else:
            # Cria a mensagem de aviso com o checkbox
            msg_aviso = QMessageBox(self)
            msg_aviso.setIcon(QMessageBox.Warning)  # Ícone de aviso
            msg_aviso.setWindowTitle("Aviso de Saída Irreversível")  # Título da janela
            msg_aviso.setText("A função de saída de usuário é irreversível.\n\nUsuários removidos não poderão ser restaurados.")  # Texto do aviso
            msg_aviso.setStandardButtons(QMessageBox.Ok)  # Botão Ok

            # Adiciona o checkbox à caixa de mensagem
            checkbox = QCheckBox("Não mostrar esta mensagem novamente")
            msg_aviso.setCheckBox(checkbox)

            # Estilos personalizados
            msg_aviso.setStyleSheet("""
                QMessageBox {
                    background-color: #FFF3CD;
                    color: #856404;
                    border: 1px solid #ffeeba;
                    border-radius: 10px;
                    padding: 10px;
                }
                QMessageBox QPushButton {
                    background-color: #f0d88b;
                    color: #856404;  /* Cor do texto do botão igual ao checkbox */
                    border: 1px solid #d6a937;
                    border-radius: 4px;
                    padding: 5px 10px;
                    min-width: 100px;
                }
                QMessageBox QPushButton:hover {
                    background-color: #e0a800;
                    color: #856404;  /* Mantém a mesma cor no hover */
                }
                QMessageBox QCheckBox {
                    color: black;
                }
            """)


            # Exibe a mensagem de aviso
            msg_aviso.exec()

            # Verifica se o usuário marcou a opção para não mostrar novamente
            if checkbox.isChecked():
                configuracoes.nao_mostrar_aviso_irreversivel = True  # Define que o usuário não quer mais ver este aviso
                configuracoes.salvar(configuracoes.usuario, configuracoes.senha,configuracoes.mantem_conectado)

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




    # Função para recuperar imagem de um produto com base no código do produto
    def recuperar_imagem_usuario_bd_users(self, id_usuario):
        conexao = sqlite3.connect('banco_de_dados.db')
        cursor = conexao.cursor()
        cursor.execute("SELECT Imagem FROM users WHERE Usuário = ?", (id_usuario,))
        
        resultado = cursor.fetchone()  # Tenta buscar uma linha
        
        if resultado is not None:
            imagem_blob = resultado[0]  # Recupera a imagem se o resultado não for None
        else:
            imagem_blob = None  # Define como None se a imagem não for encontrada
        
        conexao.close()
        return imagem_blob

    def atualizar_ativos(self):
        try:
            # Limpar a tabela antes de atualizar
            self.table_ativos.setRowCount(0)  # Remove todas as linhas da tabela

            # Consultar todos os usuarios
            query = """
            SELECT Nome,Usuário,Senha,"Confirmar Senha",CEP,Endereço,Número,Cidade,Bairro,Estado,Complemento,Telefone,Email,"Data de Nascimento",
            RG,CPF,CNPJ,"Última Troca de Senha","Data da Senha Cadastrada","Data da Inclusão do Usuário",Segredo,"Usuário Logado",Acesso
            FROM users
            """
            usuarios = self.db.executar_query(query)

            for linha_index, linha_data in enumerate(usuarios):
                self.table_ativos.insertRow(linha_index)
                for col, value in enumerate(linha_data):
                    item = self.formatar_texto(str(value))
                    self.table_ativos.setItem(linha_index, col, item)
                    
            self.table_ativos.resizeColumnsToContents()  # Ajusta as colunas automaticamente
            self.table_ativos.resizeRowsToContents()  # Ajusta as linhas automaticamente

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
            self.table_inativos.setRowCount(0)
            
            # Consulta os dados da tabela de saída no banco de dados (somente usuarios que já tiveram saída gerada)
            query = """
            SELECT Nome,Usuário,Senha,"Confirmar Senha",CEP,Endereço,CPF,Número,Estado,Email,RG,Complemento,
            Telefone,"Data de Nascimento","Última Troca de Senha","Data da Senha Cadastrada","Data da Inclusão do Usuário",
            "Data da Inatividade do Usuário",Segredo,"Usuário Logado",Acesso
            FROM users_inativos
            """
            saidas = self.db.executar_query(query)  # Método que executa a consulta e retorna os resultados

            # Preenche a tabela com os dados obtidos
            if saidas:
                for saida in saidas:
                    row_position = self.table_inativos.rowCount()
                    self.table_inativos.insertRow(row_position)
                    for column, value in enumerate(saida):
                        item = self.formatar_texto(str(value))
                        self.table_inativos.setItem(row_position, column, item)
                        
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

    # Função auxiliar para criar um QTableWidgetItem com texto centralizado e branco
    def formatar_texto(self, text):
        item = QTableWidgetItem(text)
        item.setTextAlignment(Qt.AlignCenter)
        item.setForeground(QBrush(QColor("white")))
        return item



    def limpar_tabelas(self):
        # Verifica se as tabelas estão vazias
        if self.table_inativos.rowCount() == 0 and self.table_ativos.rowCount() == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Aviso")
            msg.setText("As tabelas já estão vazias.")
            msg.exec()
            return

        # Limpa a tabela de ativos
        self.table_ativos.setRowCount(0)

        # Limpa a tabela de inativos
        self.table_inativos.setRowCount(0)

        # Mensagem de confirmação após a limpeza
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Limpeza Concluída")
        msg.setText("As tabelas foram limpas com sucesso.")
        msg.exec()


    # Limpa a coluna selecionada clicando em qualquer lugar da tabela
    def eventFilter(self, source, event):
        if event.type() == QEvent.MouseButtonPress:
            if source == self.main_window.table_ativos.viewport():
                index = self.main_window.table_ativos.indexAt(event.pos())
                if not index.isValid():
                    self.main_window.table_ativos.clearSelection()

            elif source == self.main_window.table_inativos.viewport():
                index = self.main_window.table_inativos.indexAt(event.pos())
                if not index.isValid():
                    self.main_window.table_inativos.clearSelection()

        return super().eventFilter(source, event)


    def exibir_pdf_usuarios(self):
        caminho, _ = QFileDialog.getSaveFileName(
            None,
            "Salvar PDF",
            "relatorio_usuarios.pdf",
            "PDF Files (*.pdf)"
        )
        if not caminho:
            return

        try:
            doc = SimpleDocTemplate(
                caminho,
                pagesize=landscape(A4),
                rightMargin=15,
                leftMargin=15,
                topMargin=20,
                bottomMargin=20
            )
            elementos = []
            estilo = getSampleStyleSheet()

            def extrair_dados_da_tabela(table_widget):
                headers = [table_widget.horizontalHeaderItem(col).text() for col in range(table_widget.columnCount())]
                dados = [headers]
                for row in range(table_widget.rowCount()):
                    linha = []
                    for col in range(table_widget.columnCount()):
                        item = table_widget.item(row, col)
                        texto = item.text() if item else ""
                        linha.append(texto)
                    dados.append(linha)
                return dados

            def criar_tabela(dados):
                estilos = getSampleStyleSheet()
                estilo_celula = estilos['Normal']
                estilo_celula.fontSize = 4.5
                estilo_celula.leading = 5

                dados_formatados = []
                for linha in dados:
                    nova_linha = []
                    for celula in linha:
                        texto = str(celula or "").replace('\n', '<br/>')
                        nova_linha.append(Paragraph(texto, estilo_celula))
                    dados_formatados.append(nova_linha)

                colWidths = [
                    40,
                ]


                tabela = Table(dados_formatados,  colWidths=colWidths)
                tabela.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('GRID', (0, 0), (-1, -1), 0.25, colors.black),
                    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
                    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ]))

                return tabela

            def criar_tabela_inativos(dados):
                estilos = getSampleStyleSheet()
                estilo_celula = estilos['Normal']
                estilo_celula.fontSize = 4.5
                estilo_celula.leading = 6

                dados_formatados = []
                for linha in dados:
                    nova_linha = []
                    for celula in linha:
                        texto = str(celula or "").replace('\n', '<br/>')
                        nova_linha.append(Paragraph(texto, estilo_celula))
                    dados_formatados.append(nova_linha)


                colWidths = [
                    40
                ]

                tabela = Table(dados_formatados, repeatRows=1, colWidths=colWidths)
                tabela.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('GRID', (0, 0), (-1, -1), 0.25, colors.black),
                    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
                    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ]))

                return tabela

            # Ativos
            dados_ativos = extrair_dados_da_tabela(self.main_window.table_ativos)
            elementos.append(Paragraph("Relatório de Usuários Ativos", estilo["Heading2"]))
            elementos.append(Spacer(1, 6))
            elementos.append(criar_tabela(dados_ativos))

            # Inativos
            if self.main_window.table_inativos.rowCount() > 0:
                elementos.append(Spacer(1, 10))
                elementos.append(Paragraph("Relatório de Usuários Inativos", estilo["Heading2"]))
                elementos.append(Spacer(1, 3))
                dados_inativos = extrair_dados_da_tabela(self.main_window.table_inativos)
                elementos.append(criar_tabela_inativos(dados_inativos))

            doc.build(elementos)
            QMessageBox.information(None, "PDF Gerado", "O PDF foi gerado com sucesso!")

        except Exception as e:
            QMessageBox.critical(None, "Erro ao gerar PDF", f"Erro: {str(e)}")

    def exibir_tabela_historico_usuario(self):
        self.janela_historico = QMainWindow()
        self.janela_historico.setWindowTitle("Histórico de Ações")
        self.janela_historico.resize(800,650)

        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_geometry = self.janela_historico.frameGeometry()
        window_geometry.moveCenter(screen_geometry.center())
        self.janela_historico.move(window_geometry.topLeft())
        
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # Tabela do histórico
        self.tabela_historico_usuarios = QTableWidget()
        self.tabela_historico_usuarios.setColumnCount(4)
        self.tabela_historico_usuarios.setHorizontalHeaderLabels(["Data/Hora", "Usuário", "Ação", "Descrição"])

        #Botão Atualizar
        botao_atualizar = QPushButton("Atualizar Histórico")
        botao_atualizar.clicked.connect(self.atualizar_historico_usuario)

        # Botão Apagar
        botao_apagar = QPushButton("Apagar Histórico")
        botao_apagar.clicked.connect(self.apagar_historico_usuario)

        botao_exportar_csv = QPushButton("Exportar para CSV")
        botao_exportar_csv.clicked.connect(self.exportar_csv_usuarios)

        botao_exportar_excel = QPushButton("Exportar para Excel")
        botao_exportar_excel.clicked.connect(self.exportar_excel_usuarios)

        botao_exportar_pdf = QPushButton("Exportar PDF")
        botao_exportar_pdf.clicked.connect(self.exportar_pdf_usuarios)

        botao_pausar_historico = QPushButton("Pausar Histórico")
        botao_pausar_historico.clicked.connect(self.pausar_historico_usuario)


        botao_filtrar_historico = QPushButton("Filtrar Histórico")
        botao_filtrar_historico.clicked.connect(self.filtrar_historico_usuarios)

        botao_ordenar_historico = QPushButton("Ordenar Histórico")
        botao_ordenar_historico.clicked.connect(self.ordenar_historico_usuario)

        # Criar checkbox "Selecionar Todos" toda vez que a janela for aberta
        self.todos_selecionados = QCheckBox("Selecionar todo o histórico")
        self.todos_selecionados.stateChanged.connect(self.selecionar_todos_usuarios)

        # Criar checkbox "Selecionar Individualmente" toda vez que a janela for aberta
        self.checkbox_selecionar_individual = QCheckBox("Selecionar Individualmente")
        self.checkbox_selecionar_individual.stateChanged.connect(self.selecionar_usuarios_individual)

        # Adicionar os checkboxes ao layout
        layout.addWidget(self.todos_selecionados)
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
        layout.addWidget(self.tabela_historico_usuarios)

        # Configurar o widget central e exibir a janela
        self.janela_historico.setCentralWidget(central_widget)
        self.janela_historico.show()

        # Preencher tabela pela primeira vez
        self.carregar_historico_usuario()
        self.tabela_historico_usuarios.resizeColumnsToContents()


    def carregar_historico_usuario(self):
        with sqlite3.connect('banco_de_dados.db') as cn:
            cursor = cn.cursor()
            cursor.execute('SELECT * FROM historico_usuarios ORDER BY "Data e Hora" DESC')
            registros = cursor.fetchall()

        self.tabela_historico_usuarios.clearContents()
        self.tabela_historico_usuarios.setRowCount(len(registros))

        for i, (data, usuario, acao, descricao) in enumerate(registros):
            self.tabela_historico_usuarios.setItem(i, 0, QTableWidgetItem(data))
            self.tabela_historico_usuarios.setItem(i, 1, QTableWidgetItem(usuario))
            self.tabela_historico_usuarios.setItem(i, 2, QTableWidgetItem(acao))
            self.tabela_historico_usuarios.setItem(i, 3, QTableWidgetItem(descricao))



    def atualizar_historico_usuario(self):
        QMessageBox.information(self.janela_historico, "Sucesso", "Dados carregados com sucesso!")
        self.carregar_historico_usuario()

    def apagar_historico_usuario(self):
        """
        Função principal para apagar histórico. Trata tanto exclusão por checkboxes 
        quanto exclusão por seleção direta, dependendo do estado da tabela.
        """
        # Caso checkboxes estejam ativados
        if self.coluna_checkboxes_usuarios_adicionada and self.checkboxes:
            linhas_para_remover = []
            ids_para_remover = []

            # Identificar as linhas com checkboxes selecionados
            for row, checkbox in enumerate(self.checkboxes):
                if checkbox and checkbox.isChecked():
                    linhas_para_remover.append(row)
                    item_data_widget = self.tabela_historico_usuarios.item(row, 1)  # Coluna de Data/Hora
                    if item_data_widget:
                        item_data_text = item_data_widget.text().strip()
                        # Excluir com base na data e hora
                        item_id = self.get_id_by_data_hora_usuarios(item_data_text)
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

            if not self.confirmar_historico_usuarios_apagado(mensagem):
                return

            # Excluir do banco de dados
            with sqlite3.connect('banco_de_dados.db') as cn:
                cursor = cn.cursor()
                try:
                    for item_id in ids_para_remover:
                        cursor.execute("DELETE FROM historico_usuarios WHERE id = ?", (item_id,))
                        print(f"Item removido do banco: ID {item_id}")
                    cn.commit()
                except Exception as e:
                    QMessageBox.critical(self, "Erro", f"Erro ao excluir do banco de dados: {e}")
                    return

            # Remover as linhas na interface
            for row in sorted(linhas_para_remover, reverse=True):
                self.tabela_historico_usuarios.removeRow(row)

            QMessageBox.information(self, "Sucesso", "Itens removidos com sucesso!")

        # Caso sem checkboxes (seleção manual)
        else:
            linha_selecionada = self.tabela_historico_usuarios.currentRow()

            if linha_selecionada < 0:
                QMessageBox.warning(self, "Erro", "Nenhum item foi selecionado para apagar!")
                return

            # Capturar a Data/Hora da célula correspondente (coluna 0)
            item_data_widget = self.tabela_historico_usuarios.item(linha_selecionada, 0)  # Coluna de Data/Hora
            if not item_data_widget:
                QMessageBox.warning(self, "Erro", "Não foi possível identificar a Data/Hora do item a ser apagado!")
                return

            item_data_text = item_data_widget.text().strip()

            # Conectar ao banco de dados para buscar o ID relacionado à Data/Hora
            with sqlite3.connect('banco_de_dados.db') as cn:
                cursor = cn.cursor()
                try:
                    # Buscar o ID com base na Data/Hora, removendo espaços ou caracteres extras
                    cursor.execute('SELECT id FROM historico_usuarios WHERE "Data e Hora" = ?', (item_data_text,))
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

            if not self.confirmar_historico_usuarios_apagado(mensagem):
                return

            # Excluir do banco de dados
            with sqlite3.connect('banco_de_dados.db') as cn:
                cursor = cn.cursor()
                try:
                    cursor.execute("DELETE FROM historico_usuarios WHERE id = ?", (item_id,))
                    print(f"Item removido do banco de dados: ID {item_id}")
                    cn.commit()
                except Exception as e:
                    QMessageBox.critical(self, "Erro", f"Erro ao excluir do banco de dados: {e}")
                    return

            # Remover a linha da interface
            self.tabela_historico_usuarios.removeRow(linha_selecionada)

            QMessageBox.information(self, "Sucesso", "Item removido com sucesso!")

    def get_id_by_data_hora_usuarios(self, data_hora):
        """
        Função que busca o ID correspondente à Data/Hora no banco de dados.
        """
        with sqlite3.connect('banco_de_dados.db') as cn:
            cursor = cn.cursor()
            try:
                # Converter a Data/Hora para um formato compatível com o banco de dados
                cursor.execute('SELECT id FROM historico_usuarios WHERE "Data e Hora" = ?', (data_hora,))
                resultado = cursor.fetchone()
                if resultado:
                    return resultado[0]  # Retorna o ID encontrado
                else:
                    return None  # Não encontrou nenhum ID correspondente
            except Exception as e:
                print(f"Erro ao buscar ID: {e}")
                return None
            
    def confirmar_historico_usuarios_apagado(self, mensagem):
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
    
    # Função para desmarcar todos os checkboxes
    def desmarcar_checkboxes_usuarios(self):
        for checkbox in self.checkboxes:
            if checkbox:
                checkbox.setChecked(False)

    def selecionar_todos_usuarios(self):
        if not self.coluna_checkboxes_usuarios_adicionada:
            QMessageBox.warning(self, "Aviso", "Ative a opção 'Selecionar Individualmente' antes.")
            self.todos_selecionados.setChecked(False)
            return

        estado = self.todos_selecionados.isChecked()
        for checkbox in self.checkboxes:
            if checkbox:
                # Bloquear sinais para evitar loops
                checkbox.blockSignals(True)
                checkbox.setChecked(estado)
                checkbox.blockSignals(False)
                
    # Função para adicionar checkboxes selecionar_individual na tabela de histórico
    def selecionar_usuarios_individual(self):
        if self.tabela_historico_usuarios.rowCount() == 0:
            QMessageBox.warning(self, "Aviso", "Nenhum histórico para selecionar.")
            self.checkbox_selecionar_individual.setChecked(False)
            return

        if self.coluna_checkboxes_usuarios_adicionada:
            self.desmarcar_checkboxes()
            self.tabela_historico_usuarios.removeColumn(0)
            self.coluna_checkboxes_usuarios_adicionada = False
            return

        self.tabela_historico_usuarios_usuarios.insertColumn(0)
        self.tabela_historico_usuarios.setHorizontalHeaderItem(0, QTableWidgetItem("Selecionar"))
        self.checkboxes = []

        for row in range(self.tabela_historico_usuarios.rowCount()):
            checkbox = QCheckBox()
            checkbox.stateChanged.connect(self.atualizar_selecao_todos)
            checkbox_widget = QWidget()
            layout = QHBoxLayout(checkbox_widget)
            layout.addWidget(checkbox)
            layout.setAlignment(Qt.AlignCenter)
            layout.setContentsMargins(0, 0, 0, 0)
            checkbox_widget.setLayout(layout)
            self.tabela_historico_usuarios.setCellWidget(row, 0, checkbox)
            self.checkboxes.append(checkbox)

        self.tabela_historico_usuarios.setColumnWidth(0, 30)
        self.coluna_checkboxes_usuarios_adicionada = True
        return
    
    def atualizar_selecao_todos_usuarios(self):
        self.todos_selecionados.blockSignals(True)

        # Atualizar o estado do "Selecionar Todos"
        all_checked = all(checkbox.isChecked() for checkbox in self.checkboxes if checkbox)
        any_checked = any(checkbox.isChecked() for checkbox in self.checkboxes if checkbox)

        self.todos_selecionados.setChecked(all_checked)

        self.todos_selecionados.blockSignals(False)

    def ordenar_historico_usuario(self):
        # Obter a coluna pela qual o usuário deseja ordenar
        coluna = self.obter_coluna_usuario_para_ordenar()  # Função fictícia para capturar escolha
        if coluna is None:
            return  # Cancela o processo todo
        
        # Determinar a direção de ordenação (ascendente ou descendente)
        direcao = self.obter_direcao_ordenacao_usuario()  # Função fictícia para capturar escolha
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
        for row in range(self.tabela_historico_usuarios.rowCount()):
            linha = [
                self.tabela_historico_usuarios.item(row, col).text() if self.tabela_historico_usuarios.item(row, col) else ""
                for col in range(self.tabela_historico_usuarios.columnCount())
            ]
            dados.append(linha)
        
        # Ordenar os dados com base na coluna escolhida e direção
        dados.sort(key=lambda x: x[indice_coluna], reverse=(direcao == "Decrescente"))
        
        # Atualizar a tabela com os dados ordenados
        self.tabela_historico_usuarios.setRowCount(0)  # Limpar tabela
        for row_data in dados:
            row = self.tabela_historico_usuarios.rowCount()
            self.tabela_historico_usuarios.insertRow(row)
            for col, value in enumerate(row_data):
                self.tabela_historico_usuarios.setItem(row, col, QTableWidgetItem(value))

    def obter_coluna_usuario_para_ordenar(self):
        colunas = ["Data/Hora", "Usuário", "Ação", "Descrição"]
        coluna, ok = QInputDialog.getItem(self, "Ordenar por", "Escolha a coluna:", colunas, 0, False)
        return coluna if ok else None

    def obter_direcao_ordenacao_usuario(self):
        direcoes = ["Crescente", "Decrescente"]
        direcao, ok = QInputDialog.getItem(self, "Direção da Ordenação", "Escolha a direção:", direcoes, 0, False)
        return direcao if ok else None
    
    def filtrar_historico_usuarios(self):
        # Criar a janela de filtro
        janela_filtro = QDialog(self)
        janela_filtro.setWindowTitle("Filtrar Histórico")
        layout = QVBoxLayout(janela_filtro)

        # Campo para inserir a data
        campo_data = QLineEdit()
        campo_data.setPlaceholderText("Digite a data no formato DD/MM/AAAA")
        
        # Conectar ao método de formatação, passando o texto
        campo_data.textChanged.connect(lambda: self.formatar_data_usuarios(campo_data))


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
            lambda: self.aplicar_filtro_usuarios(
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

    def formatar_data_usuarios(self, campo_data):
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

    def aplicar_filtro_usuarios(self, data, filtrar_novo, filtrar_velho):
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
        self.tabela_historico_usuarios.clearContents()
        self.tabela_historico_usuarios.setRowCount(len(registros))

        for i, row in enumerate(registros):
            self.tabela_historico_usuarios.setItem(i, 0, QTableWidgetItem(row[0]))  # Data/Hora
            self.tabela_historico_usuarios.setItem(i, 1, QTableWidgetItem(row[1]))  # Usuário
            self.tabela_historico_usuarios.setItem(i, 2, QTableWidgetItem(row[2]))  # Ação
            self.tabela_historico_usuarios.setItem(i, 3, QTableWidgetItem(row[3]))  # Descrição

        QMessageBox.information(self, "Filtro Aplicado", f"{len(registros)} registro(s) encontrado(s)!")

    def exportar_csv_usuarios(self):
        num_linhas = self.tabela_historico_usuarios.rowCount()
        num_colunas = self.tabela_historico_usuarios.columnCount()

        # Verificar se a tabela está vazia
        if self.tabela_historico_usuarios.rowCount() == 0:
            QMessageBox.warning(self, "Aviso", "Nenhum histórico encontrado para gerar arquivo CSV.")
            return  # Se a tabela estiver vazia, encerra a função sem prosseguir

        nome_arquivo, _ = QFileDialog.getSaveFileName(
            self,
            "Salvar Arquivo CSV",
            "historico_usuarios.csv",
            "Arquivos CSV (*.csv)"

        )

        if not nome_arquivo:
            return
        
        #Criar o arquivo CSV
        try:
            with open(nome_arquivo, mode="w",newline="",encoding="utf-8-sig") as arquivo_csv:
                escritor = csv.writer(arquivo_csv, delimiter=";")

                 # Adicionar cabeçalhos ao CSV
                cabecalhos = [self.tabela_historico_usuarios.horizontalHeaderItem(col).text() for col in range (num_colunas)]
                escritor.writerow(cabecalhos)

                # Adicionar os dados da tabela ao CSV
                for linha in range(num_linhas):
                    dados_linhas = [
                        self.tabela_historico_usuarios.item(linha, col).text() if self.tabela_historico_usuarios.item(linha, col) else ""
                        for col in range(num_colunas)

                    ]
                    escritor.writerow(dados_linhas)

                    QMessageBox.information(self, "Sucesso", f"Arquivo CSV salvo com sucesso em:\n{nome_arquivo}")

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Falha ao salvar o arquivo CSV:\n{str(e)}")


    def exportar_excel_usuarios(self):
        num_linhas = self.tabela_historico_usuarios.rowCount()
        num_colunas = self.tabela_historico_usuarios.columnCount()

        # Verificar se a tabela está vazia
        if self.tabela_historico_usuarios.rowCount() == 0:
            QMessageBox.warning(self, "Aviso", "Nenhum histórico encontrado para gerar arquivo Excel.")
            return  # Se a tabela estiver vazia, encerra a função sem prosseguir
        
        nome_arquivo, _ = QFileDialog.getSaveFileName(
            self,
            "Salvar Arquivo Excel",
            "historico_usuarios.xlsx",
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
                item = self.tabela_historico_usuarios.item(linha, coluna)
                linha_dados.append(item.text() if item else "") # Adicionar o texto ou vazio se o item for None
            dados.append(linha_dados)

        # Obter os cabeçalhos da tabela        
        cabecalhos = [self.tabela_historico_usuarios.horizontalHeaderItem(coluna).text() for coluna in range (num_colunas)]
        
        try:
            # Criar um DataFrame do pandas com os dados e cabeçalhos
            df = pd.DataFrame(dados, columns=cabecalhos)

            # Exportar para Excel
            df.to_excel(nome_arquivo, index=False,engine="openpyxl")
            QMessageBox.information(self, "Sucesso",f"Arquivo Excel gerado com sucesso em: \n{nome_arquivo}")
        except Exception as e:
            QMessageBox.critical(self, "Erro",f"Erro ao salvar arquivo Excel: {str(e)}")

    def exportar_pdf_usuarios(self):
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

    def pausar_historico_usuario(self):
        # Criação da nova janela de histórico como QMainWindow
        self.janela_escolha = QMainWindow()
        self.janela_escolha.setWindowTitle("Pausar Histórico")
        self.janela_escolha.resize(255, 150)


        # Botão "Sim"
        botao_sim = QPushButton("Sim")
        botao_sim.clicked.connect(self.historico_ativo_usuario)

        # Botão "Não"
        botao_nao = QPushButton("Não")
        botao_nao.clicked.connect(self.historico_inativo_usuario)


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


    def historico_ativo_usuario(self):
        # Atualiza o estado do histórico para ativo
        self.main_window.historico_usuario_pausado = True  # Atualiza a variável no MainWindow
        QMessageBox.information(self, "Histórico", "O registro do histórico foi pausado.")
        self.janela_escolha.close()

    def historico_inativo_usuario(self):
        # Atualiza o estado do histórico para inativo (continua registrando)
        self.main_window.historico_usuario_pausado = False  # Atualiza a variável no MainWindow
        QMessageBox.information(self, "Histórico", "O registro do histórico continua ativo.")
        self.janela_escolha.close()


    def abrir_planilha_usuarios(self):
        # Abrir o diálogo para selecionar o arquivo Excel
        nome_arquivo, _ = QFileDialog.getOpenFileName(self, "Abrir Arquivo Excel", "", "Arquivos Excel (*.xlsx)")

        if not nome_arquivo:
            return  # Se o usuário cancelar a seleção do arquivo

        
        # Alterar o texto da line_excel para "Carregando arquivo Excel..."
        self.line_excel_usuarios.setText("Carregando arquivo Excel...")
        self.nome_arquivo_excel = nome_arquivo  # Salva para usar depois

        # Inicializar a barra de progresso
        self.progress_excel_usuarios.setValue(0)
        self.progresso = 0
        

        # Começar o timer para simular carregamento visual
        self.timer_excel = QTimer()
        self.timer_excel.timeout.connect(self.atualizar_progresso_excel_usuarios)
        self.timer_excel.start(20)


    def atualizar_progresso_excel_usuarios(self):
        if self.progresso < 100:
            self.progresso += 1
            self.progress_excel_usuarios.setValue(self.progresso)
        else:
            self.timer_excel.stop()

            try:
                df = pd.read_excel(self.nome_arquivo_excel, engine="openpyxl", header=0)
                df = df.fillna("Não informado")

                coluna_table_ativos = [
                    "Nome", "Usuário", "Senha", "Confirmar Senha", "Acesso",
                    "Endereço", "CEP", "CPF", "Número", "Estado", "E-mail", "RG", "Complemento", "Telefone",
                    "Data de Nascimento", "Última Troca de Senha", "Data da Senha Cadastrada",
                    "Data da Inclusão do Usuário", "Segredo", "Usuário Logado"
                ]

                if df.shape[1] != len(coluna_table_ativos):
                    QMessageBox.warning(self, "Erro", "O número de colunas no arquivo Excel não corresponde ao número esperado.")
                    self.line_excel_usuarios.clear()
                    self.resetar_progresso()
                    return

                if df.empty:
                    QMessageBox.warning(self, "Erro", "O arquivo Excel está vazio.")
                    self.line_excel_usuarios.clear()
                    self.resetar_progresso()
                    return

                self.table_ativos.setRowCount(0)

                for row in df.itertuples(index=False):
                    row_position = self.table_ativos.rowCount()
                    self.table_ativos.insertRow(row_position)
                    for column, value in enumerate(row):
                        item = self.formatar_texto(str(value))
                        self.table_ativos.setItem(row_position, column, item)

                QMessageBox.information(self, "Sucesso", "Arquivo Excel importado com sucesso!")

            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Erro ao importar o arquivo Excel: {e}")

            self.line_excel_usuarios.setText(self.nome_arquivo_excel)
            self.resetar_progresso()
            # Ajusta colunas e linhas automaticamente após preencher
            self.main_window.table_ativos.resizeColumnsToContents()
            self.main_window.table_ativos.resizeRowsToContents()

    def resetar_progresso(self):
        self.progress_excel_usuarios.setValue(0)
        self.progresso = 0
    
    def importar_usuario(self):
        if self.table_ativos.rowCount() == 0 and self.table_inativos.rowCount() == 0:
            QMessageBox.warning(self, "Aviso", "Nenhum dado encontrado para gerar arquivo Excel.")
            return

        nome_arquivo, _ = QFileDialog.getSaveFileName(
            self,
            "Salvar Arquivo Excel",
            "relatório de usuários.xlsx",
            "Arquivos Excel (*.xlsx)"
        )

        if not nome_arquivo:
            return

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
                
                if self.table_ativos.rowCount() > 0:
                    df_ativos = tabela_para_dataframe(self.table_ativos)
                    df_ativos.to_excel(writer, sheet_name="Ativos", index=False)

                if self.table_inativos.rowCount() > 0:
                    df_inativos = tabela_para_dataframe(self.table_inativos)
                    df_inativos.to_excel(writer, sheet_name="Inativos", index=False)

            # Abrir o arquivo com openpyxl para ajustar estilos
            from openpyxl import load_workbook
            wb = load_workbook(nome_arquivo)

            for sheet_name in wb.sheetnames:
                ws = wb[sheet_name]

                for col in ws.columns:
                    max_length = 0
                    column = col[0].column  # número da coluna (1, 2, ...)
                    column_letter = get_column_letter(column)

                    for cell in col:
                        if cell.value:
                            max_length = max(max_length, len(str(cell.value)))
                        cell.alignment = Alignment(horizontal="center", vertical="center")

                    ws.column_dimensions[column_letter].width = max_length + 2  # ajustar largura

                # Negrito no cabeçalho
                for cell in ws[1]:
                    cell.font = Font(bold=True)

            wb.save(nome_arquivo)

            QMessageBox.information(self, "Sucesso", f"Arquivo Excel gerado com sucesso em:\n{nome_arquivo}")

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao salvar arquivo Excel: {str(e)}")

    # Limpa a coluna selecionada clicando em qualquer lugar da tabela
    def eventFilter(self, source, event):
        if event.type() == QEvent.MouseButtonPress:
            if source == self.main_window.table_ativos.viewport():
                index = self.main_window.table_ativos.indexAt(event.pos())
                if not index.isValid():
                    self.main_window.table_ativos.clearSelection()

            elif source == self.main_window.table_inativos.viewport():
                index = self.main_window.table_inativos.indexAt(event.pos())
                if not index.isValid():
                    self.main_window.table_inativos.clearSelection()

        return super().eventFilter(source, event)
    
    def abrir_panilha_usuarios_em_massa(self):
        # Abrir o diálogo para selecionar o arquivo Excel
        nome_arquivo, _ = QFileDialog.getOpenFileName(self, "Abrir Arquivo Excel", "", "Arquivos Excel (*.xlsx)")

        # Se o usuário cancelar a seleção do arquivo
        if not nome_arquivo:
            return
        # Alterar o texto da line_excel para "Carregando arquivo Excel..."
        self.line_edit_massa_usuarios.setText("Carregando arquivo Excel...")
        self.nome_arquivo_excel_massa = nome_arquivo

        # Inicializar a barra de progresso
        self.progress_massa_usuarios.setValue(0)
        self.progresso_massa = 0

        # Começar o timer para simular carregamento visual
        self.timer_excel_massa_usuarios = QTimer()
        self.timer_excel_massa_usuarios.timeout.connect(self.atualizar_progress_line_usuarios_em_massa)
        self.timer_excel_massa_usuarios.start(20)

    def atualizar_progress_line_usuarios_em_massa(self):
        if self.progresso_massa < 100:
            self.progresso_massa += 1
            self.progress_massa_usuarios.setValue(self.progresso_massa)
        else:
            self.timer_excel_massa_usuarios.stop()

            try:
                df = pd.read_excel(self.nome_arquivo_excel_massa, engine="openpyxl", header=0)
                df = df.fillna("Não informado")

                colunas_table_massa_usuarios = ["Nome", "Usuário", "Senha", "Confirmar Senha", "Acesso",
                    "Endereço", "CEP", "CPF", "Número", "Estado", "E-mail", "RG", "Complemento", "Telefone",
                    "Data de Nascimento"]

                # Verificar se o DataFrame está vazio
                if df.shape[1] != len(colunas_table_massa_usuarios):
                    QMessageBox.warning(self, "Erro", "O número de colunas em massa no arquivo Excel não corresponde ao número esperado.")
                    self.line_edit_massa_usuarios.clear()
                    # Zerando a barra de progresso
                    self.progress_massa_usuarios.setValue(0)
                    self.progresso_massa = 0
                    
                    
                if df.shape[0] == 0:
                    QMessageBox.warning(self, "Erro", "O arquivo Excel está vazio.")
                    self.line_edit_massa_usuarios.clear()
                    # Zerando a barra de progresso
                    self.progress_massa_usuarios.setValue(0)
                    self.progresso_massa = 0
                    return  
                # Adicionar os dados à tabela
                self.table_massa_usuarios.setRowCount(0)
                
        
                for _, row in df.iterrows():
                    row_position = self.table_massa_usuarios.rowCount()
                    self.table_massa_usuarios.insertRow(row_position)
                    for column, value in enumerate(row):
                        item = self.formatar_texto_usuarios_em_massa(str(value))
                        self.table_massa_usuarios.setItem(row_position, column, item)
                QMessageBox.information(self, "Sucesso", "Arquivo Excel importado com sucesso!")

            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Erro ao importar o arquivo Excel: {e}")
             # Quando o arquivo for carregado, atualizar o texto da line_excel com o caminho do arquivo
            self.line_edit_massa_usuarios.setText(self.nome_arquivo_excel_massa)
            
            self.progress_massa_usuarios.setValue(0)
            self.progresso_massa = 0
            self.table_massa_usuarios.resizeColumnsToContents()
            self.table_massa_usuarios.resizeRowsToContents()
            
    def formatar_texto_usuarios_em_massa(self, texto):
        item = QTableWidgetItem(texto)
        item.setTextAlignment(Qt.AlignCenter)  # Centraliza o texto
        item.setForeground(QBrush(QColor("white"))) 
        return item

    def cadastrar_usuarios_em_massa(self):
        try:
            total_linhas = self.table_massa_usuarios.rowCount()
            if total_linhas == 0:
                QMessageBox.warning(self, "Erro", "Nenhum usuário encontrado para cadastrar.")
                return

            for linha in range(total_linhas):
                nome = self.table_massa_usuarios.item(linha, 0).text().strip() if self.table_massa_usuarios.item(linha, 0) else ""
                # Gerar código único para o usuário
                usuario = self.main_window.gerar_codigo_usuarios()
                senha = self.table_massa_usuarios.item(linha, 2).text().strip() if self.table_massa_usuarios.item(linha, 2) else ""
                confirmar_senha = self.table_massa_usuarios.item(linha, 3).text().strip() if self.table_massa_usuarios.item(linha, 3) else ""
                acesso = self.table_massa_usuarios.item(linha, 4).text().strip() if self.table_massa_usuarios.item(linha, 4) else ""
                endereco = self.table_massa_usuarios.item(linha, 5).text().strip() if self.table_massa_usuarios.item(linha, 5) else ""
                cep = self.table_massa_usuarios.item(linha, 6).text().strip() if self.table_massa_usuarios.item(linha, 6) else ""
                cpf = self.table_massa_usuarios.item(linha, 7).text().strip() if self.table_massa_usuarios.item(linha, 7) else ""
                numero = self.table_massa_usuarios.item(linha, 8).text().strip() if self.table_massa_usuarios.item(linha, 8) else ""
                estado = self.table_massa_usuarios.item(linha, 9).text().strip() if self.table_massa_usuarios.item(linha, 9) else ""
                email = self.table_massa_usuarios.item(linha, 10).text().strip() if self.table_massa_usuarios.item(linha, 10) else ""
                rg = self.table_massa_usuarios.item(linha, 11).text().strip() if self.table_massa_usuarios.item(linha, 11) else ""
                complemento = self.table_massa_usuarios.item(linha, 12).text().strip() if self.table_massa_usuarios.item(linha, 12) else ""
                telefone = self.table_massa_usuarios.item(linha, 13).text().strip() if self.table_massa_usuarios.item(linha, 13) else ""
                data_nascimento = self.table_massa_usuarios.item(linha, 14).text().strip() if self.table_massa_usuarios.item(linha, 14) else ""

                dados_usuarios_massa = {
                    "Nome": nome,
                    "Usuário": usuario,
                    "Senha": senha,
                    "Confirmar Senha": confirmar_senha,
                    "Acesso": acesso,
                    "Endereço": endereco,
                    "CEP": cep,
                    "CPF": cpf,
                    "Número": numero,
                    "Estado": estado,
                    "E-mail": email,
                    "RG": rg,
                    "Complemento": complemento,
                    "Telefone": telefone,
                    "Data de Nascimento": data_nascimento
                }

                self.main_window.subscribe_user(usuario_info=dados_usuarios_massa, registrar_historico=True)

                # Registrar no histórico
                descricao = f"Usuário {usuario} foi cadastrado no sistema!"
                self.main_window.registrar_historico_usuarios("Cadastro em Massa", descricao)


            QMessageBox.information(self, "Sucesso", "Usuários cadastrados em massa com sucesso!")
            self.line_edit_massa_usuarios.clear()

            # Limpar a tabela após a inserção
            self.table_massa_usuarios.setRowCount(0)

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao cadastrar usuários em massa:\n{e}")

                
                
        
