from PySide6.QtWidgets import (QDialog, QPushButton, QVBoxLayout, QTableWidget, 
                               QTableWidgetItem, QMessageBox, QCheckBox, QLabel, QLineEdit, 
                               QLabel, QFrame,QDateEdit,QGridLayout,
                               QFileDialog,QMainWindow,QWidget,QSizePolicy,QApplication,QHBoxLayout,
                               QComboBox,QAbstractItemView,QDialogButtonBox,QHeaderView)
from PySide6 import QtWidgets
from PySide6.QtGui import QPixmap, Qt, QImage
from PySide6.QtCore import QDate, Qt,QSize,QTimer
from database import DataBase, sqlite3
import base64
import re
import locale
import random
import string
import subprocess
import pandas as pd
import openpyxl


class TabelaProdutos(QDialog):
    def __init__(self, main_window, date_edit, parent=None):
        super().__init__(parent)
        self.main_window = main_window
        self.date_edit = date_edit
        self.edit_mode = False  # Inicializando o modo de edição como falso
        self.codigo_item_original = None
        self.filtragem_aplicada = False  # Inicializa a variável
        self.db = DataBase()  # Inicializando o atributo db
        
        self.setWindowTitle("Tabela de Produtos")
        self.setMinimumWidth(800)
        self.setMinimumHeight(600)
    

        self.frame_valor_total_produtos = QtWidgets.QFrame()
        self.frame_valor_do_desconto = QtWidgets.QFrame()
        self.frame_valor_desconto = QtWidgets.QFrame()
        self.frame_quantidade = QtWidgets.QFrame()

        label_imagem_produto = None

        self.checkboxes = []  # Inicializa a lista de checkboxes

        # Inicialize a variável de estado
        self.todos_selecionados = False
        # Variável para rastrear se a coluna de checkboxes está visível
        self.coluna_checkboxes_produtos_adicionada = False


        cursor = None
        
        # Layout principal da janela
        layout = QVBoxLayout()

        self.grid_layout = QGridLayout()
        

        # Tabela para exibir os produtos
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(10)  # Definindo o número de colunas
        self.table_widget.setHorizontalHeaderLabels(["ID", "Produto", "Quantidade", "Valor do Produto", 
                                                     "Desconto", "Data da Compra", "Código do Produto", 
                                                     "Cliente", "Descrição","Usuário"])  # Definindo os rótulos das colunas
        
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

        
        self.btn_ordenar_produtos = QPushButton("Ordenar Produtos")
        layout.addWidget(self.btn_ordenar_produtos)

        self.btn_visualizar_imagem = QPushButton("Visualizar Imagem")
        layout.addWidget(self.btn_visualizar_imagem)

        self.btn_atualizar_tabela_produtos = QPushButton("Atualizar Tabela")
        layout.addWidget(self.btn_atualizar_tabela_produtos)

        self.btn_gerar_excel = QPushButton("Gerar arquivo Excel")
        layout.addWidget(self.btn_gerar_excel)

        self.btn_duplicar_produto = QPushButton("Duplicar Produto")
        layout.addWidget(self.btn_duplicar_produto)

        self.checkbox_selecionar_produtos = QCheckBox("Selecionar")
        layout.addWidget(self.checkbox_selecionar_produtos)

        # Adicionar a tabela ao layout
        layout.addWidget(self.table_widget)
        
        # Definir o layout da janela
        self.setLayout(layout)
 

        self.btn_apagar_produto.clicked.connect(self.apagar_produto_confirmado)
        self.btn_editar_produto.clicked.connect(self.editar_produto_tabela)
        self.btn_filtrar_produtos.clicked.connect(self.filtrar_produtos)
        self.btn_ordenar_produtos.clicked.connect(self.ordenar_produtos)
        self.btn_visualizar_imagem.clicked.connect(self.visualizar_imagem)
        self.btn_atualizar_tabela_produtos.clicked.connect(self.atualizar_tabela_products)
        self.btn_duplicar_produto.clicked.connect(self.duplicar_produto)
        self.btn_gerar_excel.clicked.connect(self.gerar_arquivo_excel)
        self.checkbox_selecionar_produtos.clicked.connect(self.selecionar_individual)
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
            self.table_widget.resizeColumnsToContents()  # Ajustar as colunas para o conteúdo
            self.table_widget.resizeRowsToContents()  # Ajustar as linhas para o conteúdo

            # Verificar se a tabela está vazia
            if self.table_widget.rowCount() == 0:
                self.exibir_mensagem_sem_produtos()
            else:
                self.ocultar_mensagem_sem_produtos()

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao acessar o banco de dados: {str(e)}")
        finally:
            pass

    def exibir_mensagem_sem_produtos(self):
        # Verificar se a QLabel já existe
        if not hasattr(self, 'label_sem_produto'):
            self.label_sem_produto = QLabel("Produtos cadastrados serão exibidos aqui...")
            self.label_sem_produto.setAlignment(Qt.AlignCenter)
            self.label_sem_produto.setStyleSheet("font-size: 16px; color: black;")
            
            # Verificar se o widget tem um layout
            if not self.table_widget.layout():
                self.main_layout = QVBoxLayout(self.table_widget)
                self.table_widget.setLayout(self.main_layout)
            else:
                self.main_layout = self.table_widget.layout()

            self.main_layout.addWidget(self.label_sem_produto)

        self.label_sem_produto.show()

    def ocultar_mensagem_sem_produtos(self):
        # Oculta a mensagem caso existam produtos na tabela
        if hasattr(self, 'label_sem_produto'):
            self.label_sem_produto.hide()

     
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
    def obter_produtos_por_id(self, id):
        query = "SELECT * FROM products WHERE ID = ?"
        parameters = (id,)

        cursor = None  # Inicialize o cursor como None
        
        try:
            db = DataBase()  # Cria uma instância da classe DataBase
            connection = db.connecta()  # Obtemos uma conexão
            cursor = connection.cursor()  # Criamos um cursor a partir da conexão
            cursor.execute(query, parameters)
            
            produtos = cursor.fetchall()
            
            return produtos
        except Exception as e:
            print("Erro ao consultar produtos por ID:", e)
            return []
        finally:
            if cursor:
                cursor.close()  # Fechamos o cursor apenas se ele não for None
#*******************************************************************************************************          
    def obter_produtos_por_codigo(self, codigo):
        query = "SELECT * FROM products WHERE Código_Item = ?"
        parameters = (codigo,)

        cursor = None  # Inicialize o cursor como None
        
        try:
            db = DataBase()  # Cria uma instância da classe DataBase
            connection = db.connecta()  # Obtemos uma conexão
            cursor = connection.cursor()  # Criamos um cursor a partir da conexão
            cursor.execute(query, parameters)
            
            produtos = cursor.fetchall()
            
            return produtos
        except Exception as e:
            print("Erro ao consultar produtos por código:", e)
            return []
        finally:
            if cursor:
                cursor.close()  # Fechamos o cursor apenas se ele não for None
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
#*******************************************************************************************************
    def filtrar_produtos(self): 

        # Verificar se a tabela está vazia
        if self.table_widget.rowCount() == 0:
            QMessageBox.warning(self, "Aviso", "Nenhum produto cadastrado para filtrar.")
            return  # Se a tabela estiver vazia, encerra a função sem prosseguir
           
        # Criar um QDialog para a caixa de confirmação
        mensagem_box = QDialog(self)
        mensagem_box.setWindowTitle("Filtrar Produtos")
        
        layout = QVBoxLayout(mensagem_box)
        
        # Adiciona a mensagem de confirmação
        lbl_mensagem = QLabel("Deseja filtrar os produtos?", mensagem_box)
        layout.addWidget(lbl_mensagem)
        
        # Botões de Sim e Não com QDialogButtonBox
        botoes = QDialogButtonBox(QDialogButtonBox.StandardButtons(0), Qt.Horizontal, mensagem_box)
        
        botao_sim = botoes.addButton("Sim", QDialogButtonBox.AcceptRole)
        botao_nao = botoes.addButton("Não", QDialogButtonBox.RejectRole)
        
        layout.addWidget(botoes)
        
        # Funções para lidar com os cliques dos botões
        def on_sim():
            mensagem_box.accept()  # Fechar a caixa de diálogo
            self.abrir_criterio_dialog()  # Abrir o diálogo de critérios
        
        def on_nao():
            mensagem_box.reject()  # Fechar a caixa de diálogo
        
        botao_sim.clicked.connect(on_sim)
        botao_nao.clicked.connect(on_nao)
        
        # Executa a caixa de diálogo e espera pela resposta
        mensagem_box.exec()

    def abrir_criterio_dialog(self):
        # Criar um QDialog para a seleção do critério de filtragem
        criterio_dialog = QDialog(self)
        criterio_dialog.setWindowTitle("Escolha o Critério de Filtragem")
        
        layout = QVBoxLayout(criterio_dialog)
        
        # Criar e adicionar os botões de seleção de critério
        btn_nome = QPushButton("Filtrar pelo Nome do Produto", criterio_dialog)
        btn_id = QPushButton("Filtrar pelo ID", criterio_dialog)
        btn_codigo = QPushButton("Filtrar pelo Código do Item", criterio_dialog)
        
        # Botão de Voltar
        btn_voltar = QPushButton("Voltar", criterio_dialog)
        
        def selecionar_criterio(criterio):
            criterio_dialog.close()
            self.abrir_dialogo_filtro(criterio)
        
        def voltar():
            criterio_dialog.close()
            self.filtrar_produtos()  # Volta para a janela anterior
        
        btn_nome.clicked.connect(lambda: selecionar_criterio('nome'))
        btn_id.clicked.connect(lambda: selecionar_criterio('id'))
        btn_codigo.clicked.connect(lambda: selecionar_criterio('codigo'))
        btn_voltar.clicked.connect(voltar)
        
        layout.addWidget(btn_nome)
        layout.addWidget(btn_id)
        layout.addWidget(btn_codigo)
        layout.addWidget(btn_voltar)
        
        criterio_dialog.setLayout(layout)
        criterio_dialog.exec_()

    def abrir_dialogo_filtro(self, criterio):
        # Abre um diálogo para inserir o valor de filtragem com base no critério selecionado
        dialog = QDialog(self)
        dialog.setWindowTitle(f"Filtrar por {criterio.capitalize()}")
        
        layout = QVBoxLayout(dialog)
        
        # Label e campo de entrada baseado no critério
        lbl_criterio = QLabel(dialog)
        txt_criterio = QLineEdit(dialog)
        
        if criterio == 'nome':
            lbl_criterio.setText("Nome do Produto:")
        elif criterio == 'id':
            lbl_criterio.setText("ID do Produto:")
        elif criterio == 'codigo':
            lbl_criterio.setText("Código do Item:")
        
        layout.addWidget(lbl_criterio)
        layout.addWidget(txt_criterio)
        
        # Botão para aplicar o filtro
        btn_filtrar = QPushButton("Filtrar", dialog)
        
        # Botão de Voltar
        btn_voltar = QPushButton("Voltar", dialog)
        
        def aplicar_filtro():
            valor = txt_criterio.text()
            print(f"Filtrando por {criterio.capitalize()}: {valor}")
            
            if criterio == 'nome':
                produtos = self.obter_produtos_por_nome(valor)
            elif criterio == 'id':
                produtos = self.obter_produtos_por_id(valor)
            elif criterio == 'codigo':
                produtos = self.obter_produtos_por_codigo(valor)
            
            self.atualizar_tabela_produtos_filtrada(produtos)
            dialog.close()  # Fechar o diálogo de filtragem após aplicar o filtro
            self.filtragem_aplicada = True  # Marca que a filtragem foi aplicada
        
        def voltar():
            dialog.close()
            self.abrir_criterio_dialog()  # Volta para a janela anterior
        
        btn_filtrar.clicked.connect(aplicar_filtro)
        btn_voltar.clicked.connect(voltar)
        
        layout.addWidget(btn_filtrar)
        layout.addWidget(btn_voltar)
        
        dialog.setLayout(layout)
        dialog.exec()
#*******************************************************************************************************
    def atualizar_valores_frames(self, valor_total, valor_com_desconto, valor_do_desconto, quantidade):
        # Verificar e formatar os valores corretamente
        valor_total_formatado = locale.currency(valor_total, grouping=True)
        
        # Se o valor do desconto for 0, significa que não há desconto, então "Sem desconto" é exibido
        valor_com_desconto_formatado = "Sem desconto" if valor_do_desconto == 0 else locale.currency(valor_com_desconto, grouping=True)

        # Evitar erro de tipo ao formatar "Sem desconto"
        if isinstance(valor_do_desconto, (int, float)):
            valor_do_desconto_formatado = locale.currency(valor_do_desconto, grouping=True)
        else:
            valor_do_desconto_formatado = "Sem desconto"

        # Definir os textos nos frames    
        self.main_window.frame_valor_do_desconto.setText(valor_do_desconto_formatado)
        self.main_window.frame_valor_desconto.setText(valor_com_desconto_formatado)
        self.main_window.frame_quantidade.setText("{:.0f}".format(quantidade))
        self.main_window.frame_valor_total_produtos.setText(valor_total_formatado)

        # Ajustar as geometrias, se necessário
        altura = 101
        largura_padrao = 335

        # Ajustar a posição e tamanho apenas quando o desconto for zero (Sem desconto)
        if valor_do_desconto == 0:  # Verificando se o valor do desconto é zero (sem desconto)
            largura = 300  # Ajuste a largura para acomodar "Sem desconto"
            self.main_window.frame_valor_do_desconto.setGeometry(100,50,largura,altura) # Posição da label quando não há desconto
        else:
            largura = largura_padrao  # Tamanho padrão do frame quando há desconto
            self.main_window.frame_valor_do_desconto.setGeometry(90, 45, largura, altura)

        # Posicionar o frame de valor total
        self.main_window.frame_valor_total_produtos.setGeometry(125, 45, largura, altura)

        # Posicionar o frame de valor com desconto
        self.main_window.frame_valor_desconto.setGeometry(115, 45, largura, altura)

        # Posicionar o frame de quantidade
        self.main_window.frame_quantidade.setGeometry(135, 50, largura, altura)

        # Atualizar os frames para exibir os novos valores
        self.main_window.frame_valor_total_produtos.adjustSize()
        self.main_window.frame_valor_do_desconto.adjustSize()
        self.main_window.frame_valor_desconto.adjustSize()
        self.main_window.frame_quantidade.adjustSize()
#*******************************************************************************************************
    def apagar_produto_confirmado(self):
        produtos_para_remover = []
        linhas_para_remover = []

        # Verificar se a tabela está vazia
        if self.table_widget.rowCount() == 0:
            QMessageBox.warning(self, "Aviso", "Nenhum produto cadastrado para apagar.")
            return  # Se a tabela estiver vazia, encerra a função sem prosseguir

        # 1. Verificar checkboxes marcadas
        if self.coluna_checkboxes_produtos_adicionada:
            total_rows = self.table_widget.rowCount()
            for row in range(total_rows):
                if row < len(self.checkboxes):
                    checkbox = self.checkboxes[row]
                    if checkbox and checkbox.isChecked():
                        item_id = self.table_widget.item(row, 1)  # ID do produto (coluna 1)
                        nome_item = self.table_widget.item(row, 2)  # Nome do produto (coluna 2)

                        if item_id and nome_item:
                            produto_id = item_id.text().strip()
                            nome_produto = nome_item.text().strip()

                            print(f"Produto (checkbox) na linha {row + 1}: Nome = '{nome_produto}', ID = '{produto_id}'")  # Depuração

                            # Verificando se o ID do produto é um número válido
                            if produto_id.isdigit():  # Verifica se o ID é numérico
                                # Evitar duplicados entre seleção direta e checkboxes
                                if (int(produto_id), nome_produto) not in produtos_para_remover:
                                    produtos_para_remover.append((int(produto_id), nome_produto))
                                    linhas_para_remover.append(row)
                            else:
                                QMessageBox.warning(self, "Erro", f"ID inválido para o produto na linha {row + 1}. Esperado um número.")

        # 2. Verificar linhas selecionadas utilizando selectedIndexes, se não houver seleção por checkbox
        if not produtos_para_remover:  # Só verificar `selectedIndexes()` se não houver produtos selecionados via checkbox
            selecionados = self.table_widget.selectedIndexes()

            if selecionados:
                # Usando um conjunto para garantir que cada linha seja processada apenas uma vez
                linhas_selecionadas = set(index.row() for index in selecionados)

                for row in linhas_selecionadas:
                    item_id = self.table_widget.item(row, 0)  # ID do produto (coluna 1)
                    nome_item = self.table_widget.item(row, 1)  # Nome do produto (coluna 2)

                    if item_id and nome_item:
                        produto_id = item_id.text().strip()  # Pega o ID e remove espaços extras
                        nome_produto = nome_item.text().strip()

                        # Verificando se o ID do produto é um número válido
                        if produto_id.isdigit():  # Verifica se o ID é numérico
                            produtos_para_remover.append((int(produto_id), nome_produto))
                            linhas_para_remover.append(row)
                        else:
                            QMessageBox.warning(self, "Erro", f"ID inválido para o produto na linha {row + 1}: '{produto_id}'. Esperado um número.")
                    else:
                        QMessageBox.warning(self, "Erro", f"Produto na linha {row + 1} não tem dados válidos.")

        # 3. Validar se há produtos para remover
        if produtos_para_remover:
            num_produtos = len(produtos_para_remover)
            mensagem = "Você tem certeza que deseja apagar o produto selecionado?" if num_produtos == 1 else "Você tem certeza que deseja apagar os produtos selecionados?"

            # Criar a caixa de confirmação
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

            # Se o usuário confirmar a ação
            if msgbox.clickedButton() == btn_sim:
                db = DataBase()
                try:
                    db.connecta()
                    for produto_id, nome_produto in produtos_para_remover:
                        db.remover_produto(produto_id)

                        # Registrar no histórico após a remoção do produto
                        descricao = f"Produto {nome_produto} (ID: {produto_id}) foi removido."
                        self.main_window.registrar_historico("Remoção de Produto", descricao)

                    # Remover as linhas da tabela
                    for row in sorted(linhas_para_remover, reverse=True):
                        self.table_widget.removeRow(row)

                    # Sucesso
                    QMessageBox.information(self, "Sucesso", "Produtos removidos com sucesso!")

                except Exception as e:
                    QMessageBox.critical(self, "Erro", f"Erro ao remover os produtos: {str(e)}")
        else:
            QMessageBox.warning(self, "Aviso", "Nenhum produto selecionado para apagar.")

#*******************************************************************************************************
    def editar_produto_tabela(self):
        produto_id = None

        # Verificar se a tabela está vazia
        if self.table_widget.rowCount() == 0:
            QMessageBox.warning(self, "Aviso", "Nenhum produto cadastrado para atualizar.")
            return  # Se a tabela estiver vazia, encerra a função sem prosseguir

        # Verifica se a coluna de checkboxes está ativa
        if self.coluna_checkboxes_produtos_adicionada:
            produtos_selecionados = []
            total_rows = self.table_widget.rowCount()

            for row in range(total_rows):
                if row < len(self.checkboxes):
                    checkbox = self.checkboxes[row]
                    if checkbox is not None:  # Verifica se o checkbox ainda existe
                        try:
                            if checkbox.isChecked():
                                item = self.table_widget.item(row, 1) # Quando checkbox ativo, ID está na coluna 1
                                if item:
                                    produto_id = int(item.text())
                                    produtos_selecionados.append(produto_id)
                        except RuntimeError:
                            # O checkbox foi deletado, então ignore essa linha
                            continue

            if len(produtos_selecionados) > 1:
                QMessageBox.warning(None, "Erro", "Somente um produto por vez poderá ser editado.")
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

        coluna_id = 1 if self.coluna_checkboxes_produtos_adicionada else 0
        coluna_nome = coluna_id + 1
        coluna_quantidade = coluna_nome + 1
        coluna_valor = coluna_quantidade + 1
        coluna_desconto = coluna_valor + 1
        coluna_dateEdit = coluna_desconto + 1
        coluna_codigo_item = coluna_dateEdit + 1
        coluna_cliente = coluna_codigo_item + 1
        coluna_descricao = coluna_cliente + 1

        # Econtrar a linha onde está o produto id
        linha_produto = None
        for row in range(self.table_widget.rowCount()):
            item = self.table_widget.item(row, coluna_id)
            if item and item.text() == str(produto_id):
                linha_produto = row
                break
        if linha_produto is None:
            QMessageBox.warning(self, "Erro", f"Produto com ID {produto_id} não encontrado na tabela.")
            return

        # Pegar os dados da linha selecionada
        produto_nome = self.table_widget.item(linha_produto, coluna_nome).text()
        produto_quantidade = self.table_widget.item(linha_produto, coluna_quantidade).text()
        produto_valor_real = self.table_widget.item(linha_produto, coluna_valor).text()
        produto_desconto = self.table_widget.item(linha_produto, coluna_desconto).text()
        produto_dateEdit = self.table_widget.item(linha_produto, coluna_dateEdit).text()
        produto_codigo_item = self.table_widget.item(linha_produto, coluna_codigo_item).text()
        produto_cliente = self.table_widget.item(linha_produto, coluna_cliente).text()
        produto_descricao = self.table_widget.item(linha_produto, coluna_descricao).text()

        
        # Tratar a conversão do desconto para evitar erro
        desconto_str = produto_desconto.replace('%', '').replace(',', '.').strip()
        # Se o desconto for "Sem desconto" ou vazio, define como 0.0 para cálculo
        if not desconto_str or not desconto_str.replace('.','').isdigit() or desconto_str.lower() == "sem desconto":
            desconto = 0.0
            desconto_exibicao = "Sem desconto"
        else:
            desconto = float(desconto_str)
            desconto_exibicao = f"{desconto}%"

        # Atualizar os campos visuais
        self.main_window.txt_desconto_3.setText(desconto_exibicao)

        # Armazenar o estado original do produto selecionado
        self.main_window.produto_selecionado = {
            "produto": produto_nome,
            "quantidade": int(produto_quantidade),
            "valor_produto": float(produto_valor_real.replace('R$', '').replace('.', '').replace(',', '.').strip()),
            "desconto": desconto,  # Tratado como número para cálculos
            "data_compra": produto_dateEdit,
            "codigo_item": produto_codigo_item,
            "cliente": produto_cliente,
            "descricao_produto": produto_descricao
            }

        self.main_window.txt_produto.setText(produto_nome)
        self.main_window.txt_quantidade.setText(produto_quantidade)
        self.main_window.txt_valor_produto_3.setText(produto_valor_real)
        self.date_edit.setDate(QDate.fromString(produto_dateEdit, "dd/MM/yyyy"))
        self.main_window.txt_codigo_item.setText(produto_codigo_item)
        self.main_window.txt_cliente_3.setText(produto_cliente)
        self.main_window.txt_descricao_produto_3.setText(produto_descricao)

        self.main_window.is_editing_produto = True
        self.codigo_item_original = produto_codigo_item
        self.main_window.produto_id = produto_id

        try:
            # Remover símbolo da moeda e converter para float
            valor_produto_str = produto_valor_real.replace('R$', '').replace('.', '').replace(',', '.').strip()
            produto_valor_real = float(valor_produto_str) if valor_produto_str else 0

            # Converter quantidade para inteiro
            quantidade_str = produto_quantidade.strip()
            produto_quantidade = int(quantidade_str) if quantidade_str else 0

            print(f"DEBUG - desconto_str antes da conversão: {desconto_str}")  # Adicionado para depuração

            # Garantir que não convertemos "Sem desconto" para float novamente
            if desconto_exibicao == "Sem desconto":
                produto_desconto = 0.0
            else:
                produto_desconto = float(desconto_str)

            # Calcular valores
            valor_total = (produto_valor_real * produto_quantidade) / 100
            valor_desconto = valor_total * desconto
            valor_com_desconto = valor_total - valor_desconto

            # Atualizar os frames com os valores corretos
            if desconto_exibicao == "Sem desconto":
                self.atualizar_valores_frames(valor_total, valor_com_desconto, "Sem desconto", produto_quantidade)
            else:
                self.atualizar_valores_frames(valor_total,valor_com_desconto,valor_desconto,produto_quantidade)

            # Registrar a edição no histórico
            descricao_edicao = f"Produto {produto_nome} foi editado. Novos valores: quantidade {produto_quantidade}, valor {produto_valor_real}, desconto {produto_desconto}%."
            self.main_window.registrar_historico("Edição de Produto", descricao_edicao)

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

                    self.label_imagem = QLabel(self.main_window.frame_imagem_produto_3)
                    frame_size = self.main_window.frame_imagem_produto_3.size()
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
                if self.main_window.frame_imagem_produto_3.layout():
                    old_layout = self.main_window.frame_imagem_produto_3.layout()
                    while old_layout.count():
                        item = old_layout.takeAt(0)
                        widget = item.widget()
                        if widget:
                            widget.deleteLater()
                self.main_window.frame_imagem_produto_3.setLayout(None)

            self.accept()

        except ValueError as e:
            print(f"Erro ao converter valores: {str(e)}")
#*******************************************************************************************************
    def selecionar_todos(self):
        if not self.coluna_checkboxes_produtos_adicionada:
            QMessageBox.warning(self, "Aviso", "Ative a opção 'Selecionar' antes.")
            if hasattr(self, "checkbox_header_produtos"):
                self.checkbox_header_produtos.setChecked(False)
            return

        estado = self.checkbox_header_produtos.checkState() == Qt.Checked
        self.checkboxes.clear()  # Reinicia a lista para manter consistência
        
        for row in range(self.table_widget.rowCount()):
            widget = self.table_widget.cellWidget(row, 0)
            if widget is not None:
                checkbox = widget.findChild(QCheckBox)
                if checkbox:
                    checkbox.blockSignals(True)
                    checkbox.setChecked(estado)
                    checkbox.blockSignals(False)

#*******************************************************************************************************
     # Função para adicionar checkboxes selecionar_individual na tabela de histórico
    def selecionar_individual(self):
        if self.table_widget.rowCount() == 0:
            QMessageBox.warning(self, "Aviso", "Nenhum histórico para selecionar.")
            self.coluna_checkboxes_produtos_adicionada.setChecked(False)
            return

        if self.coluna_checkboxes_produtos_adicionada:
            self.table_widget.removeColumn(0)
            self.table_widget.verticalHeader().setVisible(True)
            self.coluna_checkboxes_produtos_adicionada = False

            if hasattr(self, "checkbox_header_produtos"):
                self.checkbox_header_produtos.deleteLater()
                del self.checkbox_header_produtos

            self.checkboxes.clear()
            return

        self.table_widget.insertColumn(0)
        self.table_widget.setHorizontalHeaderItem(0, QTableWidgetItem(""))
        self.table_widget.setColumnWidth(0, 30)
        self.table_widget.horizontalHeader().setMinimumSectionSize(30)
        self.table_widget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)

        # Checkbox do cabeçalho
        self.checkbox_header_produtos = QCheckBox(self.table_widget)
        self.checkbox_header_produtos.setToolTip("Selecionar todos")
        self.checkbox_header_produtos.setChecked(False)
        self.checkbox_header_produtos.stateChanged.connect(self.selecionar_todos)
        self.checkbox_header_produtos.setFixedSize(20, 20)
        self.checkbox_header_produtos.show()

        header = self.table_widget.horizontalHeader()
        self.atualizar_posicao_checkbox_header_produtos()
        header.sectionResized.connect(self.atualizar_posicao_checkbox_header_produtos)

        self.checkboxes.clear()

        QTimer.singleShot(0,self.atualizar_posicao_checkbox_header_produtos)

        for row in range(self.table_widget.rowCount()):
            checkbox = QCheckBox()
            checkbox.stateChanged.connect(self.atualizar_selecao_todos)

            container = QWidget()
            layout = QHBoxLayout(container)
            layout.addWidget(checkbox)
            layout.setAlignment(Qt.AlignCenter)
            layout.setContentsMargins(0, 0, 0, 0)

            self.table_widget.setCellWidget(row, 0, container)
            self.checkboxes.append(checkbox)

        self.table_widget.verticalHeader().setVisible(False)
        self.coluna_checkboxes_produtos_adicionada  = True

    def atualizar_selecao_todos(self):
        self.checkbox_header_produtos.blockSignals(True)

        all_checked = all(checkbox.isChecked() for checkbox in self.checkboxes if checkbox)
        any_checked = any(checkbox.isChecked() for checkbox in self.checkboxes if checkbox)

        if all_checked:
            self.checkbox_header_produtos.setCheckState(Qt.Checked)
        elif any_checked:
            self.checkbox_header_produtos.setCheckState(Qt.PartiallyChecked)
        else:
            self.checkbox_header_produtos.setCheckState(Qt.Unchecked)

        self.checkbox_header_produtos.blockSignals(False)


    def atualizar_posicao_checkbox_header_produtos(self):
        if hasattr(self, "checkbox_header_produtos") and self.coluna_checkboxes_produtos_adicionada:
            header = self.table_widget.horizontalHeader()

            x = header.sectionViewportPosition(0) + (header.sectionSize(0) - self.checkbox_header_produtos.width()) // 2 + 4
            y = (header.height() - self.checkbox_header_produtos.height()) // 2

            self.checkbox_header_produtos.move(x, y)
  
#*******************************************************************************************************
    def ordenar_produtos(self):
        # Verificar se a tabela está vazia
        if self.table_widget.rowCount() == 0:
            QMessageBox.warning(self, "Aviso", "Nenhum produto cadastrado para ordenar.")
            return  # Se a tabela estiver vazia, encerra a função sem prosseguir
        
        # Cria e exibe um QDialog para confirmação
        confirmar_dialogo = QDialog(self)
        confirmar_dialogo.setWindowTitle("Confirmar Ordenação")
        
        layout = QVBoxLayout(confirmar_dialogo)
        mensagem = QLabel("Você deseja ordenar os produtos?", confirmar_dialogo)
        layout.addWidget(mensagem)
        
        botoes = QDialogButtonBox(QDialogButtonBox.StandardButtons(0), Qt.Horizontal, confirmar_dialogo)
        
        botao_sim = botoes.addButton("Sim", QDialogButtonBox.AcceptRole)
        botao_nao = botoes.addButton("Não", QDialogButtonBox.RejectRole)
        
        layout.addWidget(botoes)
        
        botao_sim.clicked.connect(lambda: self.abre_dialogo_ordenacao(confirmar_dialogo))
        botao_nao.clicked.connect(confirmar_dialogo.reject)
        
        confirmar_dialogo.exec()

    def abre_dialogo_ordenacao(self, confirmar_dialogo):
        confirmar_dialogo.accept()
        
        # Cria e exibe um QDialog para escolher a ordenação
        ordenar_dialogo = QDialog(self)
        ordenar_dialogo.setWindowTitle("Escolher Ordenação")
        
        layout = QVBoxLayout(ordenar_dialogo)
        
        # Opções de ordenação
        ordenar_por_label = QLabel("Ordenar por:", ordenar_dialogo)
        layout.addWidget(ordenar_por_label)
        
        ordenar_por_combo = QComboBox(ordenar_dialogo)
        ordenar_por_combo.addItems(["ID", "Nome", "Quantidade"])
        layout.addWidget(ordenar_por_combo)
        
        ordem_label = QLabel("Ordem:", ordenar_dialogo)
        layout.addWidget(ordem_label)
        
        ordem_combo = QComboBox(ordenar_dialogo)
        ordem_combo.addItems(["A a Z", "Z a A", "Menor para Maior", "Maior para Menor"])
        layout.addWidget(ordem_combo)
        
        botoes = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, ordenar_dialogo)
        layout.addWidget(botoes)
        
        botoes.button(QDialogButtonBox.Ok).clicked.connect(lambda: self.aplicar_ordenacao(ordenar_por_combo.currentText(), ordem_combo.currentText(), ordenar_dialogo))
        botoes.button(QDialogButtonBox.Cancel).clicked.connect(ordenar_dialogo.reject)
        
        ordenar_dialogo.exec()

    def aplicar_ordenacao(self, criterio, ordem, ordenar_dialogo):
        ordenar_dialogo.accept()
        
        colunas = {
            "ID": 0,
            "Nome": 1,
            "Quantidade": 2
        }
        
        ordem_map = {
            "A a Z": Qt.AscendingOrder,
            "Z a A": Qt.DescendingOrder,
            "Menor para o Maior": Qt.AscendingOrder,
            "Maior para o Menor": Qt.DescendingOrder
        }
        
        coluna = colunas.get(criterio, 0)
        ordem = ordem_map.get(ordem, Qt.AscendingOrder)
        
        self.table_widget.sortItems(coluna, ordem)
#*******************************************************************************************************
    def visualizar_imagem(self):
        # Verificar se a tabela está vazia
        if self.table_widget.rowCount() == 0:
            QMessageBox.warning(self, "Aviso", "Não é possível visualizar imagem de um produto não cadastrado.")
            return  # Se a tabela estiver vazia, encerra a função sem prosseguir
            
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

        # Verificar se a tabela está vazia
        if self.table_widget.rowCount() == 0:
            QMessageBox.warning(self, "Aviso", "Nenhum produto cadastrado para ordenar.")
            return  # Se a tabela estiver vazia, encerra a função sem prosseguir
        
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
        for widget in self.main_window.frame_imagem_produto_3.children():
            if isinstance(widget, QLabel):
                label_imagem = widget
                break

        # Se não houver QLabel, criar um novo
        if label_imagem is None:
            label_imagem = QLabel(self.main_window.frame_imagem_produto_3)
            label_imagem.setObjectName("label_imagem_produto")

            # Adicionar o QLabel ao layout do frame, se houver
            layout = self.main_window.frame_imagem_produto_3.layout()
            if layout is None:
                layout = QVBoxLayout(self.main_window.frame_imagem_produto_3)
                self.main_window.frame_imagem_produto_3.setLayout(layout)

            layout.addWidget(label_imagem)
     

            # Definir tamanho do QLabel para ser o mesmo que o QFrame
            frame_size = self.main_window.frame_imagem_produto_3.size()
            label_imagem.resize(frame_size.size())


            # Ajustar o alinhamento da imagem no QLabel
            label_imagem.setAlignment(Qt.AlignCenter)
            label_imagem.setStyleSheet("background-color: red;")  # Adicionar um fundo temporário para debug

        return label_imagem
    
    def carregar_tabela_produtos(self):
        with sqlite3.connect('banco_de_dados.db') as cn:
            cursor = cn.cursor()
            cursor.execute('SELECT id, Produto, Quantidade, Valor_Real, Desconto, Data_Compra, '
                        '"Código_Item", Cliente, "Descrição_Produto", "Usuário" '
                        'FROM products ORDER BY id ASC')  # <-- Ordem crescente

            registros = cursor.fetchall()

        self.table_widget.setSortingEnabled(False)  # Impede bagunça enquanto carrega
        self.table_widget.clearContents()
        self.table_widget.setRowCount(len(registros))

        deslocamento = 1 if self.coluna_checkboxes_produtos_adicionada else 0
        self.checkboxes = []  # Zera os checkboxes

        for i, (id, produto, quantidade, valor_real, desconto, data_compra,
                codigo_item, cliente, descricao_produto, usuario) in enumerate(registros):

            if self.coluna_checkboxes_produtos_adicionada:
                checkbox = QCheckBox()
                checkbox.setStyleSheet("margin-left:9px; margin-right:9px;")
                self.table_widget.setCellWidget(i, 0, checkbox)
                self.checkboxes.append(checkbox)

            self.table_widget.setItem(i, 0 + deslocamento, QTableWidgetItem(str(id)))
            self.table_widget.setItem(i, 1 + deslocamento, QTableWidgetItem(produto))
            self.table_widget.setItem(i, 2 + deslocamento, QTableWidgetItem(str(quantidade)))
            self.table_widget.setItem(i, 3 + deslocamento, QTableWidgetItem(str(valor_real)))
            self.table_widget.setItem(i, 4 + deslocamento, QTableWidgetItem(str(desconto)))
            self.table_widget.setItem(i, 5 + deslocamento, QTableWidgetItem(data_compra))
            self.table_widget.setItem(i, 6 + deslocamento, QTableWidgetItem(codigo_item))
            self.table_widget.setItem(i, 7 + deslocamento, QTableWidgetItem(cliente))
            self.table_widget.setItem(i, 8 + deslocamento, QTableWidgetItem(descricao_produto))
            self.table_widget.setItem(i, 9 + deslocamento, QTableWidgetItem(usuario))

        # Agora sim: organiza pela coluna de ID (em ordem crescente)
        self.table_widget.sortItems(0 + deslocamento, Qt.AscendingOrder)
        self.table_widget.setSortingEnabled(True)



            



    def atualizar_tabela_products(self):
        QMessageBox.information(None, "Sucesso", "Dados carregados com sucesso!")
        self.carregar_tabela_produtos()


    def gerar_arquivo_excel(self):
        # Obtém o número de linhas e colunas da tabela
        num_linhas = self.table_widget.rowCount()
        num_colunas = self.table_widget.columnCount()

        # Verificar se a tabela está vazia
        if self.table_widget.rowCount() == 0:
            QMessageBox.warning(self, "Aviso", "Nenhum produto cadastrado para gerar arquivo excel.")
            return  # Se a tabela estiver vazia, encerra a função sem prosseguir

        # Extrai os dados da tabela para uma lista de listas
        dados = []
        for linha in range(num_linhas):
            linha_dados = []
            for coluna in range(num_colunas):
                item = self.table_widget.item(linha, coluna)
                linha_dados.append(item.text() if item else "")
            dados.append(linha_dados)

        # Obtém os cabeçalhos da tabela
        cabecalhos = []
        for coluna in range(num_colunas):
            cabecalho_item = self.table_widget.horizontalHeaderItem(coluna)
            cabecalhos.append(cabecalho_item.text() if cabecalho_item else "")

        # Cria um DataFrame do pandas com os dados da tabela
        df = pd.DataFrame(dados, columns=cabecalhos)

        # Abre um diálogo para salvar o arquivo
        caminho_arquivo, _ = QFileDialog.getSaveFileName(self, "Salvar Arquivo Excel", "Tabela Produtos", "Arquivo Excel (*.xlsx)")
        
        if caminho_arquivo:
            # Salva o DataFrame como um arquivo Excel
            df.to_excel(caminho_arquivo, index=False)
            QMessageBox.information(self,"Aviso","Arquivo excel gerado com sucesso")

    def duplicar_produto(self):
        # Verificar se há uma linha selecionada
        linha_selecionada = self.table_widget.currentRow()

        # Verificar se a tabela está vazia
        if self.table_widget.rowCount() == 0:
            QMessageBox.warning(self, "Aviso", "Nenhum produto cadastrado para duplicar.")
            return  # Se a tabela estiver vazia, encerra a função sem prosseguir
        
        if linha_selecionada == -1:
            # Se nenhuma linha estiver selecionada, mostrar um aviso
            QMessageBox.warning(self, "Aviso", "Nenhum produto selecionado para duplicar.")
            return

        # Obter os dados da linha selecionada
        dados_produto = []
        for coluna in range(self.table_widget.columnCount()):
            item = self.table_widget.item(linha_selecionada, coluna)
            dados_produto.append(item.text() if item is not None else "")

        # Adicionar uma nova linha na tabela
        linha_nova = self.table_widget.rowCount()
        self.table_widget.insertRow(linha_nova)

        # Preencher a nova linha com os dados duplicados
        for coluna, dado in enumerate(dados_produto):
            self.table_widget.setItem(linha_nova, coluna, QTableWidgetItem(dado))

        # Inserir o produto duplicado no banco de dados
        try:
            # Preparar os dados para inserção, omitindo o ID
            produto = dados_produto[1]  # Assumindo que o primeiro dado é o nome do produto
            quantidade = dados_produto[2]
            valor_real = dados_produto[3]
            desconto = dados_produto[4]
            data_compra = dados_produto[5]
            codigo_item = dados_produto[6]
            cliente = dados_produto[7]
            descricao_produto = dados_produto[8]
            imagem = dados_produto[9] if len(dados_produto) > 8 else None

            # Inserir o produto no banco de dados usando a função do módulo database
            self.db.insert_product(produto, quantidade, valor_real, desconto, data_compra, 
                        codigo_item, cliente, descricao_produto, imagem)

            # Exibir uma mensagem de sucesso
            QMessageBox.information(self, "Sucesso", "Produto duplicado e cadastrado com sucesso.")
        
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Falha ao cadastrar o produto: {str(e)}")


    def atualizar_checkboxes(self):
        # Atualiza a lista de checkboxes para corresponder ao número de linhas na tabela
        total_rows = self.table_widget.rowCount()
        self.checkboxes = []
        for row in range(total_rows):
            checkbox = self.table_widget.cellWidget(row, 0)
            if checkbox is None:
                checkbox = QCheckBox()
                self.table_widget.setCellWidget(row, 0, checkbox)
            self.checkboxes.append(checkbox)



