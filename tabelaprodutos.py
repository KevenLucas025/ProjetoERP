from PySide6.QtWidgets import (QDialog, QPushButton, QVBoxLayout, QTableWidget, 
                               QTableWidgetItem, QMessageBox, QCheckBox, QLabel, QLineEdit, 
                               QLabel, QFrame,QDateEdit,QGridLayout,
                               QFileDialog,QMainWindow,QWidget,QSizePolicy,QApplication,QHBoxLayout,QAbstractItemView)
from PySide6 import QtWidgets
from PySide6.QtGui import QPixmap, Qt, QImage
from PySide6.QtCore import QDate, Qt,QSize
from database import DataBase, sqlite3
import base64
import re
import locale
import random
import string
import subprocess


class TabelaProdutos(QDialog):
    def __init__(self, main_window, date_edit, parent=None):
        super().__init__(parent)
        self.main_window = main_window
        self.date_edit = date_edit
        self.edit_mode = False  # Inicializando o modo de edição como falso
        self.codigo_item_original = None
        self.db = DataBase()  # Inicializando o atributo db
        
        self.setWindowTitle("Tabela de Produtos")
        self.setMinimumWidth(800)
        self.setMinimumHeight(600)
    

        self.frame_valor_total_produtos = QtWidgets.QFrame()
        self.frame_valor_do_desconto = QtWidgets.QFrame()
        self.frame_valor_desconto = QtWidgets.QFrame()
        self.frame_quantidade = QtWidgets.QFrame()

        label_imagem_produto = None

        # Inicialize a variável de estado
        self.todos_selecionados = False

        # Variável para rastrear se a coluna de checkboxes está visível
        self.coluna_checkboxes_adicionada = False


        cursor = None
        
        # Layout principal da janela
        layout = QVBoxLayout()

        self.grid_layout = QGridLayout()
        

        # Tabela para exibir os produtos
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(10)  # Definindo o número de colunas
        self.table_widget.setHorizontalHeaderLabels(["ID", "Produto", "Quantidade", "Valor do Produto", 
                                                     "Desconto", "Data da Compra", "Código do Produto", 
                                                     "Cliente", "Descrição", "Imagem"])  # Definindo os rótulos das colunas
        
        # Personalizar o estilo dos cabeçalhos de linha e coluna
        font = self.table_widget.horizontalHeader().font()
        font.setBold(True)
        self.table_widget.horizontalHeader().setFont(font)
        self.table_widget.verticalHeader().setFont(font)

        # Botão para apagar produto, dentro da tabela produtos
        self.btn_apagar_produto = QPushButton("Apagar Produto")
        layout.addWidget(self.btn_apagar_produto)

        self.btn_editar_produto = QPushButton("Atualizar Produto")
        layout.addWidget(self.btn_editar_produto)

        self.btn_filtrar_produtos = QPushButton("Filtrar Produtos")
        layout.addWidget(self.btn_filtrar_produtos)

        self.btn_selecionar_todos = QCheckBox("Selecionar todos os produtos")
        layout.addWidget(self.btn_selecionar_todos)

        self.btn_selecionar_individual = QCheckBox("Selecionar individualmente")
        layout.addWidget(self.btn_selecionar_individual)
        
        self.btn_ordenar_produtos = QPushButton("Ordenar Produtos")
        layout.addWidget(self.btn_ordenar_produtos)

        self.btn_visualizar_imagem = QPushButton("Visualizar Imagem")
        layout.addWidget(self.btn_visualizar_imagem)

        # Adicionar a tabela ao layout
        layout.addWidget(self.table_widget)
        
        # Definir o layout da janela
        self.setLayout(layout)
 

        self.btn_apagar_produto.clicked.connect(self.apagar_produto_confirmado)
        self.btn_editar_produto.clicked.connect(self.editar_produto_tabela)
        self.btn_filtrar_produtos.clicked.connect(self.filtrar_produtos)
        self.btn_ordenar_produtos.clicked.connect(self.ordenar_produtos)
        self.btn_visualizar_imagem.clicked.connect(self.visualizar_imagem)
        self.btn_selecionar_todos.clicked.connect(self.selecionar_todos)
        self.btn_selecionar_individual.clicked.connect(self.selecionar_um_por_vez)
        self.btn_filtrar_produtos.clicked.connect(self.filtrar_produtos)
        self.btn_ordenar_produtos.clicked.connect(self.ordenar_produtos)
#*******************************************************************************************************
    def preencher_tabela_produtos(self):
    # Limpar a tabela antes de preencher
        self.table_widget.setRowCount(0)
        
        # Conectar ao banco de dados
        db = DataBase()
        try:
            db.connecta()
            
            # Obter os produtos do banco de dados
            produtos = db.get_products()
            
            # Preencher a tabela com os dados dos produtos
            for produto in produtos:
                row_position = self.table_widget.rowCount()
                self.table_widget.insertRow(row_position)
                for col, data in enumerate(produto):
                    item = QTableWidgetItem(str(data))
                    self.table_widget.setItem(row_position, col, item)
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao acessar o banco de dados: {str(e)}")
        finally:
            # Fechar a conexão com o banco de dados
            db.close_connection()      
#*******************************************************************************************************
    def recuperar_imagem_do_banco(self, produto_id):
        imagem_blob = None
        
        try:
            connection = self.db.connecta()
            if connection:
                cursor = connection.cursor()
                cursor.execute("SELECT Imagem FROM products WHERE id = ?", (produto_id,))
                result = cursor.fetchone()

                if result:
                    imagem_blob = result[0]
                else:
                    print(f"Imagem não encontrada para o produto: {produto_id}")
                    return None

        except Exception as e:
            print(f"Erro ao recuperar imagem do banco de dados: {str(e)}")
            return None

        finally:
            self.db.close_connection()

        if imagem_blob:
            try:
                imagem_data = base64.b64decode(imagem_blob)
                return imagem_data  # Retorna bytes decodificados
                
            except Exception as e:
                print(f"Erro ao decodificar imagem: {str(e)}")
                return None
        else:
            print("Imagem não encontrada para o produto:", produto_id)
            return None

#*******************************************************************************************************
    def atualizar_tabela_produtos_filtrada(self, produtos):
    # Limpar a tabela antes de preencher com os produtos filtrados
        self.table_widget.setRowCount(0)

        # Preencher a tabela com os produtos filtrados
        for produto in produtos:
            row_position = self.table_widget.rowCount()
            self.table_widget.insertRow(row_position)
            for col, data in enumerate(produto):
                item = QTableWidgetItem(str(data))
                self.table_widget.setItem(row_position, col, item)

#*******************************************************************************************************
    def obter_produtos_por_nome(self, nome):
        query = "SELECT * FROM products WHERE Produto LIKE ?"
        parameters = (f"%{nome}%",)  # Usamos LIKE com % para fazer a consulta parcial

        cursor = None  # Inicialize o cursor como None
        
        try:
            db = DataBase()  # Cria uma instância da classe DataBase
            connection = db.connecta()  # Obtemos uma conexão
            cursor = connection.cursor()  # Criamos um cursor a partir da conexão
            cursor.execute(query, parameters)
            
            produtos = cursor.fetchall()
            
            return produtos
        except Exception as e:
            print("Erro ao consultar produtos:", e)
            return []
        finally:
            if cursor:
                cursor.close()  # Fechamos o cursor apenas se ele não for None
            db.close_connection()  # Fechamos a conexão usando a instância de DataBase

#*******************************************************************************************************
    def filtrar_produtos(self):
        # Perguntar ao usuário se ele deseja filtrar os produtos
        filtro = QMessageBox.question(self, "Filtrar Produtos", "Deseja filtrar os produtos?", QMessageBox.Yes | QMessageBox.No)
        
        if filtro == QMessageBox.Yes:
            dialog = QDialog(self)
            dialog.setWindowTitle("Filtrar por Nome")
            
            layout = QVBoxLayout()
            
            # Label e campo de entrada para o nome do produto
            lbl_nome = QLabel("Nome do Produto:")
            txt_nome = QLineEdit()
            layout.addWidget(lbl_nome)
            layout.addWidget(txt_nome)
            
            # Botão para aplicar o filtro
            btn_filtrar = QPushButton("Filtrar")
            
            def aplicar_filtro():
                nome = txt_nome.text()
                print(f"Filtrando por Nome: {nome}")
                
                produtos = self.obter_produtos_por_nome(nome)
                self.atualizar_tabela_produtos_filtrada(produtos)
                
                dialog.close()
            
            btn_filtrar.clicked.connect(aplicar_filtro)
            layout.addWidget(btn_filtrar)
            
            dialog.setLayout(layout)
            dialog.exec_()
        else:
            return
        

#*******************************************************************************************************
    def editar_produto_tabela(self):
        produto_id = None

        # Verifica se a coluna de checkboxes está ativa
        if self.coluna_checkboxes_adicionada:
            produtos_selecionados = []
            total_rows = self.table_widget.rowCount()

            for row in range(total_rows):
                if row < len(self.checkboxes):
                    checkbox = self.checkboxes[row]
                    if checkbox and checkbox.isChecked():
                        item = self.table_widget.item(row, 1)
                        if item:
                            produto_id = int(item.text())
                            produtos_selecionados.append(produto_id)

            if len(produtos_selecionados) > 1:
                QMessageBox.warning(self, "Erro", "Somente um produto por vez poderá ser editado.")
                return

            if len(produtos_selecionados) == 1:
                produto_id = produtos_selecionados[0]
            else:
                QMessageBox.warning(self, "Erro", "Nenhum produto selecionado para editar.")
                return
        else:
            if self.table_widget.currentRow() >= 0:
                row_index = self.table_widget.currentRow()
                produto_id = int(self.table_widget.item(row_index, 0).text())
            else:
                QMessageBox.warning(self, "Erro", "Nenhum produto selecionado para editar.")
                return

        imagem_data = self.recuperar_imagem_do_banco(produto_id)

        coluna_id = 1 if self.coluna_checkboxes_adicionada else 0
        coluna_nome = coluna_id + 1
        coluna_quantidade = coluna_nome + 1
        coluna_valor = coluna_quantidade + 1
        coluna_desconto = coluna_valor + 1
        coluna_dateEdit = coluna_desconto + 1
        coluna_codigo_item = coluna_dateEdit + 1
        coluna_cliente = coluna_codigo_item + 1
        coluna_descricao = coluna_cliente + 1

        produto_nome = self.table_widget.item(self.table_widget.currentRow(), coluna_nome).text()
        produto_quantidade = self.table_widget.item(self.table_widget.currentRow(), coluna_quantidade).text()
        produto_valor_real = self.table_widget.item(self.table_widget.currentRow(), coluna_valor).text()
        produto_desconto = self.table_widget.item(self.table_widget.currentRow(), coluna_desconto).text()
        produto_dateEdit = self.table_widget.item(self.table_widget.currentRow(), coluna_dateEdit).text()
        produto_codigo_item = self.table_widget.item(self.table_widget.currentRow(), coluna_codigo_item).text()
        produto_cliente = self.table_widget.item(self.table_widget.currentRow(), coluna_cliente).text()
        produto_descricao = self.table_widget.item(self.table_widget.currentRow(), coluna_descricao).text()

        # Armazenar o estado original do produto selecionado
        self.main_window.produto_selecionado = {
        "produto": produto_nome,
        "quantidade": int(produto_quantidade),
        "valor_produto": float(produto_valor_real.replace('R$', '').replace('.','').replace(',','.').strip()),
        "desconto": float(produto_desconto.replace('%', '').replace(',','.').strip()),
        "data_compra": produto_dateEdit,
        "codigo_item": produto_codigo_item,
        "cliente": produto_cliente,
        "descricao_produto": produto_descricao
        }

        self.main_window.txt_produto.setText(produto_nome)
        self.main_window.txt_quantidade.setText(produto_quantidade)
        self.main_window.txt_valor_produto.setText(produto_valor_real)
        self.main_window.txt_desconto.setText(produto_desconto)
        self.date_edit.setDate(QDate.fromString(produto_dateEdit, "dd/MM/yyyy"))
        self.main_window.txt_codigo_item.setText(produto_codigo_item)
        self.main_window.txt_cliente.setText(produto_cliente)
        self.main_window.txt_descricao_produto.setText(produto_descricao)

        self.main_window.is_editing = True
        self.codigo_item_original = produto_codigo_item
        self.main_window.produto_id = produto_id

        try:
            # Remover símbolo da moeda e converter para float
            valor_produto_str = produto_valor_real.replace('R$', '').replace('.','').replace(',','.').strip()
            produto_valor_real = float(valor_produto_str) if valor_produto_str else 0

            # Converter quantidade para inteiro
            quantidade_str = produto_quantidade.strip()
            produto_quantidade = int(quantidade_str) if quantidade_str else 0

            # Converter desconto para float e tratá-lo como porcentagem
            desconto_str = produto_desconto.replace('%', '').replace(',','.').strip()
            produto_desconto = float(desconto_str)  if desconto_str else 0

            # Calcular valores
            valor_total = produto_valor_real * produto_quantidade
            valor_desconto = valor_total * produto_desconto
            valor_com_desconto = valor_total - valor_desconto

            # Atualizar os frames com os valores corretos
            self.atualizar_valores_frames(valor_total, valor_com_desconto, valor_desconto, produto_quantidade)


            if imagem_data:
                try:
                    pixmap = QPixmap()
                    pixmap.loadFromData(imagem_data)

                    if pixmap.isNull():
                        QMessageBox.warning(self, "Aviso", "Não foi possível carregar a imagem.")
                        return
                    else:
                        print("Pixmap carregado com sucesso.")
                        print("Pixmap carregado pelo botão EDITAR: ", pixmap)

                    self.label_imagem = QLabel(self.main_window.frame_imagem_produto)
                    frame_size = self.main_window.frame_imagem_produto.size()
                    self.label_imagem.setFixedSize(frame_size.width(), frame_size.height())
                    pixmap = pixmap.scaled(self.label_imagem.width(), self.label_imagem.height(), Qt.KeepAspectRatio)
                    self.label_imagem.setPixmap(pixmap)
                    self.label_imagem.setAlignment(Qt.AlignCenter)
                    self.label_imagem.show()
                    self.label_imagem.repaint()

                except Exception as e:
                    print(f"Erro ao processar imagem: {str(e)}")
            else:
                print("Imagem não encontrada no banco de dados.")
                if self.main_window.frame_imagem_produto.layout():
                    old_layout = self.main_window.frame_imagem_produto.layout()
                    while old_layout.count():
                        item = old_layout.takeAt(0)
                        widget = item.widget()
                        if widget:
                            widget.deleteLater()
                self.main_window.frame_imagem_produto.setLayout(None)

            self.accept()

        except ValueError as e:
            QMessageBox.warning(self, "Erro", f"Erro ao converter valores: {str(e)}")

#*******************************************************************************************************
    def atualizar_valores_frames(self, valor_total, valor_com_desconto, valor_do_desconto, quantidade):
        # Verificar e formatar os valores corretamente
        valor_total_formatado = locale.currency(valor_total, grouping=True)
        valor_com_desconto_formatado = locale.currency(valor_com_desconto, grouping=True)
        valor_do_desconto_formatado = locale.currency(valor_do_desconto, grouping=True)

        # Definir os textos nos frames    
        self.main_window.frame_valor_do_desconto.setText(valor_do_desconto_formatado)
        self.main_window.frame_valor_desconto.setText(valor_com_desconto_formatado)
        self.main_window.frame_quantidade.setText("{:.0f}".format(quantidade))
        self.main_window.frame_valor_total_produtos.setText(valor_total_formatado)

        # Ajustar as geometrias, se necessário
        altura = 101
        largura = 335

        # Posicionar os frames
        self.main_window.frame_valor_total_produtos.setGeometry(125, 45, largura, altura)
        self.main_window.frame_valor_do_desconto.setGeometry(125, 45, largura, altura)
        self.main_window.frame_valor_desconto.setGeometry(115, 45, largura, altura)
        self.main_window.frame_quantidade.setGeometry(135, 50, largura, altura)

        # Atualizar os frames para exibir os novos valores
        self.main_window.frame_valor_total_produtos.adjustSize()
        self.main_window.frame_valor_do_desconto.adjustSize()
        self.main_window.frame_valor_desconto.adjustSize()
        self.main_window.frame_quantidade.adjustSize()
#*******************************************************************************************************    
    def apagar_produto_confirmado(self):
        if self.coluna_checkboxes_adicionada:
            produtos_para_remover = []
            linhas_para_remover = []
            total_rows = self.table_widget.rowCount()
            
            for row in range(total_rows):
                if row < len(self.checkboxes):
                    checkbox = self.checkboxes[row]
                    if checkbox:
                        if checkbox.isChecked():
                            # Recuperar o ID do produto da coluna 1 (ID)
                            item = self.table_widget.item(row, 1)  # Assumindo que o ID está na coluna 1 após a coluna de checkboxes
                            if item:
                                produto_id = int(item.text())
                                produtos_para_remover.append(produto_id)
                                linhas_para_remover.append(row)

            if produtos_para_remover:
                num_produtos = len(produtos_para_remover)
                if num_produtos > 1:
                    mensagem = "Você tem certeza que deseja apagar os produtos selecionados?"
                else:
                    mensagem = "Você tem certeza que deseja apagar o produto selecionado?"

                # Criar a caixa de mensagem
                msgbox = QMessageBox(self)
                msgbox.setWindowTitle("Confirmar")
                msgbox.setText(mensagem)

                # Adicionar botões personalizados
                btn_sim = QPushButton("Sim")
                btn_nao = QPushButton("Não")
                msgbox.addButton(btn_sim, QMessageBox.ButtonRole.YesRole)
                msgbox.addButton(btn_nao, QMessageBox.ButtonRole.NoRole)

                msgbox.setDefaultButton(btn_nao)
                resposta = msgbox.exec()
   
                if resposta == btn_sim:
                    db = DataBase()
                    try:
                        db.connecta()
                        for produto_id in produtos_para_remover:
                            db.remover_produto(produto_id)
                        

                        QMessageBox.information(self, "Sucesso", "Produtos removidos com sucesso!")
                    except Exception as e:
                        QMessageBox.critical(self, "Erro", f"Erro ao remover os produtos: {str(e)}")
                    finally:
                        # Fechar a conexão com o banco de dados
                        db.close_connection()
                    
            else:
                QMessageBox.warning(self, "Aviso", "Nenhum produto selecionado para apagar.")
        else:
            # Apagar o produto selecionado se apenas um produto estiver selecionado
            index = self.table_widget.currentRow()
            if index >= 0:
                item = self.table_widget.item(index, 0)  # Assumindo que o ID está na coluna 0 quando checkboxes não estão adicionados
                if item:
                    produto_id = int(item.text())
                    
                    # Criar a caixa de mensagem
                    msgbox = QMessageBox(self)
                    msgbox.setWindowTitle("Confirmar")
                    msgbox.setText("Você tem certeza que deseja apagar este produto")

                    # Adicionar botões personalizados
                    btn_sim = QPushButton("Sim")
                    btn_nao = QPushButton("Não")
                    msgbox.addButton(btn_sim, QMessageBox.ButtonRole.YesRole)
                    msgbox.addButton(btn_nao, QMessageBox.ButtonRole.NoRole)

                    msgbox.setDefaultButton(btn_nao)
                
                    resposta = msgbox.exec()
                    
                    if resposta == btn_sim:
                        db = DataBase()
                        try:
                            db.connecta()
                            db.remover_produto(produto_id)
                            self.table_widget.removeRow(index)  # Remover linha da tabela
                            QMessageBox.information(self, "Sucesso", "Produto removido com sucesso!")
                        except Exception as e:
                            QMessageBox.critical(self, "Erro", f"Erro ao remover o produto: {str(e)}")
                        finally:
                            # Fechar a conexão com o banco de dados
                            db.close_connection()
            else:
                QMessageBox.warning(self, "Aviso", "Nenhum produto selecionado.")
#*******************************************************************************************************
    def selecionar_todos(self):
        self.checkbox_todos = []

        if self.coluna_checkboxes_adicionada:
            # Exibir mensagem de erro se a coluna de checkboxes estiver visível
            QMessageBox.warning(self, "Aviso", "Por favor, desmarque a opção 'Selecionar Individualmente' para utilizar esta função.")
            # Desmarcar o botão de selecionar todos
            self.btn_selecionar_todos.setChecked(False)
            return

        # Verificar se há pelo menos um produto na tabela
        if self.table_widget.rowCount() == 0:
            QMessageBox.warning(self, "Aviso", "Não há produtos para selecionar.")
            # Desmarcar o botão de selecionar todos
            self.btn_selecionar_todos.setChecked(False)
            return
        
        # Alternar o estado de seleção
        self.todos_selecionados = not self.todos_selecionados

        # Implementação para selecionar ou deselecionar todos os produtos na tabela
        total_rows = self.table_widget.rowCount()
        for row in range(total_rows):
            item = self.table_widget.item(row, 0)  # Assumindo que o ID está na coluna 0
            if item is not None:
                item.setSelected(self.todos_selecionados)
            else:
                # Se o item não existe, você pode adicionar uma mensagem de log ou lidar com isso de outra forma
                print(f"Item na linha {row} é None")
                self.checkbox_todos.append()
        
        # Desmarcar todos os checkboxes se a tabela estiver vazia
        if self.table_widget.rowCount() == 0 and self.coluna_checkboxes_adicionada:
            self.remover_checkboxes()
#*******************************************************************************************************
    def selecionar_um_por_vez(self):
        self.checkboxes = []  # Lista para armazenar os checkboxes

        # Verificar se há pelo menos um produto na tabela
        if self.table_widget.rowCount() == 0:
            QMessageBox.warning(self, "Aviso", "Não há produtos para selecionar.")
            # Desmarcar o botão de selecionar individualmente
            self.btn_selecionar_individual.setChecked(False)
            return
        
        if self.coluna_checkboxes_adicionada:
            # Se a coluna de checkboxes já estiver visível, remova-a
            self.remover_checkboxes()
        else:
            # Adicionar uma coluna de checkboxes se ainda não foi adicionada
            self.table_widget.insertColumn(0)
            self.table_widget.setHorizontalHeaderItem(0, QTableWidgetItem())
            
            # Atualizar cada linha para adicionar um checkbox na primeira coluna
            total_rows = self.table_widget.rowCount()
            for row in range(total_rows):
                checkbox = QCheckBox()
                checkbox_widget = QWidget()
                layout = QHBoxLayout(checkbox_widget)
                layout.addWidget(checkbox)
                layout.setAlignment(Qt.AlignCenter)
                layout.setContentsMargins(0, 0, 0, 0)
                checkbox_widget.setLayout(layout)
                self.table_widget.setCellWidget(row, 0, checkbox)
                self.checkboxes.append(checkbox)  # Armazenar o checkbox na lista
            
            # Definir a largura da coluna para corresponder ao tamanho do checkbox
            checkbox_width = checkbox.sizeHint().width()
            self.table_widget.setColumnWidth(0, checkbox_width)
            self.coluna_checkboxes_adicionada = True
#*******************************************************************************************************
    def remover_checkboxes(self):
        # Remover a coluna de checkboxes e desmarcar todos os checkboxes se existirem
        total_rows = self.table_widget.rowCount()
        if self.coluna_checkboxes_adicionada:
            self.table_widget.removeColumn(0)
            self.coluna_checkboxes_adicionada = False
            # Desmarcar todos os checkboxes
            for row in range(total_rows):
                checkbox_widget = self.table_widget.cellWidget(row, 0)
                if checkbox_widget:
                    checkbox = checkbox_widget.findChild(QCheckBox)
                    if checkbox:
                        checkbox.setChecked(False)     
#*******************************************************************************************************
    def ordenar_produtos(self):
        # Implementação básica para ordenar produtos
        self.table_widget.sortItems(1, Qt.AscendingOrder)  # Ordenar pela coluna 1 em ordem ascendente
#*******************************************************************************************************
    def visualizar_imagem(self):
        if self.table_widget.currentRow() >= 0:
            row_index = self.table_widget.currentRow()
            produto_id = int(self.table_widget.item(row_index, 0).text())
            
            imagem_data = self.recuperar_imagem_do_banco(produto_id)
            
            if imagem_data:
                try:
                    print("Dados da imagem recuperados com sucesso para visualização.")
                    
                    pixmap = QPixmap()
                    pixmap.loadFromData(imagem_data)
                    
                    if pixmap.isNull():
                        print("Aviso: pixmap é nulo")
                        QMessageBox.warning(self, "Aviso", "Não foi possível carregar a imagem.")
                        return
                    else:
                        print("Pixmap carregado com sucesso para visualização.")
                    
                    # Função para abrir a janela de visualização da imagem
                    def abrir_pelo_sistema():
                        visualizar_janela = QMainWindow(self)
                        visualizar_janela.setWindowTitle("Visualizador de Imagem")

                        # Criar um botão para baixar a imagem
                        btn_baixar_imagem = QPushButton("Baixar Imagem",self)
                        btn_baixar_imagem.clicked.connect(lambda: salvar_imagem(imagem_data))

                        # Função para salvar a imagem
                        def salvar_imagem(imagem_data):
                            #Renomeia por padrão a imagem salva
                            nome_padrao = f"Imagem salva produto {produto_id}"

                            options = QFileDialog.Options()
                            file_path, _ = QFileDialog.getSaveFileName(self, "Salvar Imagem", nome_padrao, "Imagens (*.png *.jpg *.bmp)", options=options)
                            if file_path:
                                with open(file_path, 'wb') as file:
                                    file.write(imagem_data)
                                QMessageBox.information(self, "Sucesso", "Imagem salva com sucesso")

                        
                        # Criar um widget central e definir o layout
                        central_widget = QWidget()
                        visualizar_janela.setCentralWidget(central_widget)
                        
                        layout = QVBoxLayout(central_widget)
                        
                        label_imagem = QLabel(central_widget)
                        label_imagem.setAlignment(Qt.AlignCenter)  # Centralizar a imagem dentro do QLabel
                    
                        # Função para atualizar o pixmap com o tamanho atual da janela
                        def atualizar_imagem():
                            tamanho_janela = visualizar_janela.centralWidget().size()
                            pixmap_redimensionado = pixmap.scaled(tamanho_janela, Qt.KeepAspectRatio)
                            label_imagem.setPixmap(pixmap_redimensionado)
                        
                        # Conectar o redimensionamento da janela ao ajuste da imagem
                        visualizar_janela.resizeEvent = lambda event: atualizar_imagem()
                        
                        # Inicializar o tamanho da janela
                        tamanho_inicial = QSize(800, 600)
                        visualizar_janela.resize(tamanho_inicial)
                        
                        # Centralizar a janela na tela
                        frame_graficos = visualizar_janela.frameGeometry()
                        tela = QApplication.primaryScreen().availableGeometry()
                        frame_graficos.moveCenter(tela.center())
                        visualizar_janela.move(frame_graficos.topLeft())
                        
                        # Adicionar o QLabel ao layout
                        layout.addWidget(label_imagem)
                        layout.addWidget(btn_baixar_imagem)
                        
                        # Ajustar a política de redimensionamento para permitir a alteração do tamanho
                        central_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                        label_imagem.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                        
                        # Ajustar a imagem pela primeira vez
                        atualizar_imagem()
                        
                        # Definir a janela para ser redimensionável
                        visualizar_janela.setMinimumSize(200, 200)  # Definindo um tamanho mínimo para a janela
                        
                        visualizar_janela.show()
                    
                    # Chamar a função para abrir a janela de visualização da imagem
                    abrir_pelo_sistema()
                    
                    
                except Exception as e:
                    print(f"Erro ao processar imagem: {str(e)}")
            else:
                QMessageBox.warning(self, "Aviso", "Imagem não encontrada.")
#*******************************************************************************************************         
    def adicionar_widgets(self, frame, debug_text):
        layout = QVBoxLayout()  # Criar um layout vertical
        label = QLabel(debug_text)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)  # Adicionar o label ao layout
        frame.setLayout(layout)  # Definir o layout ao frame
#*******************************************************************************************************
    def obter_produtos_por_nome(self, nome):
        query = "SELECT * FROM products WHERE Produto LIKE ?"
        parameters = (f"%{nome}%",)  # Usamos LIKE com % para fazer a consulta parcial

        cursor = None  # Inicialize o cursor como None
        
        try:
            db = DataBase()  # Cria uma instância da classe DataBase
            connection = db.connecta()  # Obtemos uma conexão
            cursor = connection.cursor()  # Criamos um cursor a partir da conexão
            cursor.execute(query, parameters)
            
            produtos = cursor.fetchall()
            
            return produtos
        except Exception as e:
            print("Erro ao consultar produtos:", e)
            return []
        finally:
            if cursor:
                cursor.close()  # Fechamos o cursor apenas se ele não for None
            db.close_connection()  # Fechamos a conexão usando a instância de DataBase
#*******************************************************************************************************
    def get_label_imagem(self):
        label_imagem = None
        for widget in self.main_window.frame_imagem_produto.children():
            if isinstance(widget, QLabel):
                label_imagem = widget
                break

        # Se não houver QLabel, criar um novo
        if label_imagem is None:
            label_imagem = QLabel(self.main_window.frame_imagem_produto)
            label_imagem.setObjectName("label_imagem_produto")

            # Adicionar o QLabel ao layout do frame, se houver
            layout = self.main_window.frame_imagem_produto.layout()
            if layout is None:
                layout = QVBoxLayout(self.main_window.frame_imagem_produto)
                self.main_window.frame_imagem_produto.setLayout(layout)

            layout.addWidget(label_imagem)
     

            # Definir tamanho do QLabel para ser o mesmo que o QFrame
            frame_size = self.main_window.frame_imagem_produto.size()
            label_imagem.resize(frame_size.size())


            # Ajustar o alinhamento da imagem no QLabel
            label_imagem.setAlignment(Qt.AlignCenter)
            label_imagem.setStyleSheet("background-color: red;")  # Adicionar um fundo temporário para debug

        return label_imagem