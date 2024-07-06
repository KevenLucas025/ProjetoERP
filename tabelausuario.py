from PySide6.QtWidgets import (QDialog, QPushButton, QVBoxLayout, QTableWidget, 
                               QTableWidgetItem, QMessageBox, QCheckBox, QLabel, QLineEdit, 
                               QLabel, QFrame,QGridLayout,QFileDialog)
from PySide6 import QtWidgets
from PySide6.QtGui import QPixmap, Qt, QImage
from PySide6.QtCore import  Qt,QRect
from PySide6 import QtCore
from database import DataBase, sqlite3
import base64
import re
import os


class TabelaUsuario(QDialog):
    def __init__(self, main_window, parent=None):
        super().__init__(parent)
        self.main_window = main_window
        self.frame_imagem_cadastro = QFrame()  # Adicionar o atributo frame_imagem_cadastro
        self.db = DataBase()  # Inicializando o atributo db
        self.setWindowTitle("Tabela de Usuários")
        self.setMinimumWidth(800)
        self.setMinimumHeight(600)

        self.usuario_selecionado = False  # Adiciona um atributo para verificar se um usuário foi selecionado

        cursor = None

        self.limpar_campos_de_texto() 

        # Inicializar a tabela
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(20)  # Definir o número de colunas
        
        # Definir os cabeçalhos das colunas
        headers = [
            "ID", "Nome", "Usuário", "Senha","Confirmar Senha", "Acesso", "Endereço", "CEP", "CPF", 
            "Número", "Estado", "Email", "Complemento", "Telefone", "Data de Nascimento", "RG", "Imagem"]
        self.table_widget.setHorizontalHeaderLabels(headers)
        
        # Layout para a janela da tabela
        layout_tabela = QVBoxLayout()
        layout_tabela.addWidget(self.table_widget)
        self.setLayout(layout_tabela)
        
        # Preencher a tabela com os dados dos usuários
        self.preencher_tabela_usuario()

        
        # Personalizar o estilo dos cabeçalhos de linha e coluna
        font = self.table_widget.horizontalHeader().font()
        font.setBold(True)
        self.table_widget.horizontalHeader().setFont(font)
        self.table_widget.verticalHeader().setFont(font)

        # Criar o QLabel para exibir a imagem do usuário
        self.label_imagem_usuario = QLabel()
        self.label_imagem_usuario.setScaledContents(True)  # Redimensiona a imagem para o tamanho do QLabel

        #self.configure_frame_imagem_cadastro() # Configurar o layout do frame_imagem_cadastro

        # Criar o layout para o frame_imagem_cadastro e adicionar o QLabel
        layout_usuario = QVBoxLayout()
        layout_usuario.addWidget(self.label_imagem_usuario)
        self.main_window.frame_imagem_cadastro.setLayout(layout_usuario)

        # Botão para apagar usuário, dentro da tabela usuário
        self.btn_apagar_usuario = QPushButton("Apagar Usuários")
        layout_tabela.addWidget(self.btn_apagar_usuario)  # Corrigido aqui

        self.btn_apagar_usuario.clicked.connect(self.fechar_janela_tabela)

        self.btn_editar_usuario = QPushButton("Atualizar Usuários")
        layout_tabela.addWidget(self.btn_editar_usuario)

        self.btn_editar_usuario.clicked.connect(self.fechar_janela_tabela)

        self.btn_filtrar_usuario = QPushButton("Filtrar Usuários")
        layout_tabela.addWidget(self.btn_filtrar_usuario)

        #self.btn_apagar_usuario.clicked.connect(self.fechar_janela_tabela) fechar janela ao clicar no botão filtrar

        self.btn_selecionar_todos = QPushButton("Selecionar Usuários")
        layout_tabela.addWidget(self.btn_selecionar_todos)

        #self.btn_apagar_usuario.clicked.connect(self.fechar_janela_tabela)
        
        self.btn_ordenar_usuario = QPushButton("Ordenar Usuários")
        layout_tabela.addWidget(self.btn_ordenar_usuario)


        self.btn_visualizar_imagem = QPushButton("Visualizar Imagem")
        layout_tabela.addWidget(self.btn_visualizar_imagem)

        # Adicionar a tabela ao layout
        layout_tabela.addWidget(self.table_widget)
        
        # Definir o layout da janela
        self.setLayout(layout_tabela)


        self.btn_apagar_usuario.clicked.connect(self.confirmar_apagar_usuario)
        self.btn_editar_usuario.clicked.connect(self.editar_usuario)
        self.btn_filtrar_usuario.clicked.connect(self.filtrar_usuario)
        self.btn_ordenar_usuario.clicked.connect(self.ordenar_usuario)
        self.btn_visualizar_imagem.clicked.connect(self.visualizar_imagem_usuario)
        self.btn_selecionar_todos.clicked.connect(self.selecionar_todos)
        self.btn_filtrar_usuario.clicked.connect(self.filtrar_usuario)
#*******************************************************************************************************
    
    def configure_frame_imagem_cadastro(self):
        # Criar o QLabel para exibir a imagem do usuário
        self.label_imagem_usuario = QLabel()
        self.label_imagem_usuario.setScaledContents(True)  # Redimensiona a imagem para o tamanho do QLabel

        # Criar o layout para o frame_imagem_cadastro e adicionar o QLabel
        layout_usuario = QVBoxLayout()
        layout_usuario.addWidget(self.label_imagem_usuario)
        self.frame_imagem_cadastro.setLayout(layout_usuario)
#*******************************************************************************************************
    def preencher_tabela_usuario(self):
        # Limpar a tabela antes de preencher
        self.table_widget.setRowCount(0)

        # Definir os títulos das colunas
        column_titles = [
            "ID",
            "Nome",
            "Usuário",
            "Senha",
            "Confirmar Senha",
            "Acesso",
            "Endereço",
            "CEP",
            "CPF",
            "Número",
            "Estado",
            "Email",
            "RG",
            "Complemento",
            "Telefone",
            "Data de Nascimento",
            "Imagem",
            "Última Troca de Senha",
            "Data da Senha Cadastrada",
            "Data da Inclusão do Usuário"
        ]

        for col, title in enumerate(column_titles):
            header = QTableWidgetItem(title)
            self.table_widget.setHorizontalHeaderItem(col, header)

        # Conectar ao banco de dados
        try:
            self.db.connecta()

            # Obter os usuários do banco de dados
            usuarios = self.db.get_users()

            # Preencher a tabela com os dados dos usuários
            for usuario in usuarios:
                row_position = self.table_widget.rowCount()
                self.table_widget.insertRow(row_position)

                # Preencher cada coluna com os dados do usuário
                for col, data in enumerate(usuario):
                    item = QTableWidgetItem(str(data))
                    self.table_widget.setItem(row_position, col, item)

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao acessar o banco de dados: {str(e)}")
        finally:
            # Fechar a conexão com o banco de dados
            self.db.close_connection()




#*******************************************************************************************************
    def confirmar_apagar_usuario(self):
        # Verificar se uma linha está selecionada
        if self.table_widget.currentRow() >= 0:
            # Exibir uma mensagem de confirmação
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Confirmar")
            msg_box.setText("Você tem certeza que deseja apagar este usuário?")
            
            sim_button = QPushButton("Sim")
            sim_button.clicked.connect(self.apagar_usuario_confirmado)
            msg_box.addButton(sim_button, QMessageBox.YesRole)
            
            nao_button = QPushButton("Não")
            nao_button.clicked.connect(msg_box.reject)
            msg_box.addButton(nao_button, QMessageBox.NoRole)

            # Exibir a caixa de mensagem
            msg_box.exec()
        else:
            QMessageBox.warning(self, "Aviso", "Nenhum usuário selecionado.")
#*******************************************************************************************************
    def apagar_usuario_confirmado(self):
        # Obter o índice da linha selecionada
        index = self.table_widget.currentRow()
        
        # Obter o item da célula
        item = self.table_widget.item(index, 0)
        
        # Verificar se o item não é None e se o texto não está vazio
        if item is not None and item.text():
            # Obter o ID do usuário da coluna 0 (ID)
            id_usuario = int(item.text())
            
            # Remover a linha da tabela
            self.table_widget.removeRow(index)
            
            # Remover o usuário do banco de dados
            db = DataBase()
            try:
                db.connecta()
                db.remover_usuario(id_usuario)
                QMessageBox.information(self, "Sucesso", "Usuário removido com sucesso!")
            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Erro ao remover o usuário: {str(e)}")
            finally:
                # Fechar a conexão com o banco de dados
                db.close_connection()
        else:
            QMessageBox.warning(self, "Aviso", "Nenhuma célula selecionada ou célula vazia.")


#*******************************************************************************************************
    def recuperar_imagem_do_banco(self, id_usuario):
        imagem_blob = None
        
        try:
            connection = self.db.connecta()
            if connection:
                cursor = connection.cursor()
                cursor.execute("SELECT Imagem FROM users WHERE id = ?", (id_usuario,))
                result = cursor.fetchone()

                if result:
                    imagem_blob = result[0]
                else:
                    print(f"Imagem não encontrada para o usuário: {id_usuario}")
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
            print("Imagem não encontrada para o usuário:", id_usuario)
            return None
#*******************************************************************************************************
    def editar_usuario(self):
        print("Função editar_usuario chamada")

        if self.table_widget.currentRow() >= 0:
            row_index = self.table_widget.currentRow()
            id_usuario = int(self.table_widget.item(row_index, 0).text())

            print("ID do usuário selecionado:", id_usuario)

            # Obter a imagem do banco de dados
            imagem_data = self.recuperar_imagem_do_banco(id_usuario)

            if not hasattr(self, 'label_imagem_usuario') or self.label_imagem_usuario is None:
                self.label_imagem_usuario = QLabel()
                self.label_imagem_usuario.setScaledContents(True)  # Redimensiona a imagem para o tamanho do QLabel

            if imagem_data:
                try:
                    image = QImage.fromData(imagem_data)
                    if not image.isNull():
                        pixmap = QPixmap.fromImage(image)

                        # Redimensionar a imagem para o tamanho do QLabel
                        pixmap = pixmap.scaled(self.label_imagem_usuario.size(), Qt.KeepAspectRatio)

                        # Definir a imagem no QLabel
                        self.label_imagem_usuario.setPixmap(pixmap)
                        self.label_imagem_usuario.repaint()
                        print("Imagem definida no QLabel")
                    else:
                        print("Erro: Imagem está vazia")
                except Exception as e:
                    print(f"Erro ao processar imagem: {str(e)}")
            else:
                print("Imagem não encontrada no banco de dados.")

            # Obter os dados do usuário selecionado
            usuario_nome = self.table_widget.item(row_index, 1).text()
            usuario_usuario = self.table_widget.item(row_index, 2).text()
            usuario_senha = self.table_widget.item(row_index, 3).text()
            usuario_confirmar_senha = self.table_widget.item(row_index, 4).text()
            usuario_acesso = self.table_widget.item(row_index, 5).text()
            usuario_endereco = self.table_widget.item(row_index, 6).text()
            usuario_cep = self.table_widget.item(row_index, 7).text()
            usuario_cpf = self.table_widget.item(row_index, 8).text()
            usuario_numero = self.table_widget.item(row_index, 9).text()
            usuario_estado = self.table_widget.item(row_index, 10).text()
            usuario_email = self.table_widget.item(row_index, 11).text()
            usuario_complemento = self.table_widget.item(row_index, 12).text()
            usuario_telefone = self.table_widget.item(row_index, 13).text()
            usuario_data_nascimento = self.table_widget.item(row_index, 14).text()
            usuario_rg = self.table_widget.item(row_index, 15).text()

            # Preencher os campos da MainWindow com os dados do usuário selecionado
            self.main_window.txt_nome.setText(usuario_nome)
            self.main_window.txt_usuario.setText(usuario_usuario)
            self.main_window.txt_senha.setText(usuario_senha)
            self.main_window.txt_confirmar_senha.setText(usuario_confirmar_senha)
            self.main_window.txt_telefone.setText(usuario_telefone)
            self.main_window.txt_endereco.setText(usuario_endereco)
            self.main_window.txt_numero.setText(usuario_numero)
            self.main_window.txt_complemento.setText(usuario_complemento)
            self.main_window.txt_email.setText(usuario_email)
            self.main_window.txt_data_nascimento.setText(usuario_data_nascimento)
            self.main_window.txt_rg.setText(usuario_rg)
            self.main_window.txt_cpf.setText(usuario_cpf)
            self.main_window.txt_cep.setText(usuario_cep)
            self.main_window.txt_estado.setText(usuario_estado)
            self.main_window.comboBox.setCurrentText(usuario_acesso)

            # Atualizar o layout do frame_imagem_cadastro com o QLabel
            self.main_window.frame_imagem_cadastro.setVisible(True)  # Garante que o frame esteja visível
            self.main_window.frame_imagem_cadastro.layout().addWidget(self.label_imagem_usuario)

            self.main_window.is_editing = True  # Indica que um usuário está em edição
            self.main_window.selected_user_id = id_usuario  # Guarda o ID do usuário selecionado

            self.usuario_selecionado = True  # Indica que um usuário foi selecionado

    def usuario_foi_selecionado(self):
        return self.usuario_selecionado

#*******************************************************************************************************
    def adicionar_widgets(self, frame, debug_text):
        layout = QVBoxLayout()  # Criar um layout vertical
        label_imagem_usuario = QLabel(debug_text)
        label_imagem_usuario.setAlignment(Qt.AlignCenter)
        layout.addWidget(label_imagem_usuario)  # Adicionar o label ao layout
        frame.setLayout(layout)  # Definir o layout ao frame
#*******************************************************************************************************     

#*******************************************************************************************************
    def atualizar_tabela_usuario_filtrada(self, usuario):
    # Limpar a tabela antes de preencher com os usuários filtrados
        self.table_widget.setRowCount(0)

        # Preencher a tabela com os produtos filtrados
        for produto in usuario:
            row_position = self.table_widget.rowCount()
            self.table_widget.insertRow(row_position)
            for col, data in enumerate(produto):
                item = QTableWidgetItem(str(data))
                self.table_widget.setItem(row_position, col, item)

#*******************************************************************************************************
    def obter_usuario_por_nome(self, nome):
        query = "SELECT * FROM users WHERE Nome LIKE ?"
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
    def filtrar_usuario(self):
    # Perguntar ao usuário se ele deseja filtrar os produtos
        filtro = QMessageBox.question(self, "Filtrar Usuários", "Deseja filtrar os usuários?", QMessageBox.Yes | QMessageBox.No)
        
        if filtro == QMessageBox.Yes:
            dialog = QDialog(self)
            dialog.setWindowTitle("Filtrar por Nome")
            
            layout = QVBoxLayout()
            
            # Label e campo de entrada para o nome do produto
            lbl_nome = QLabel("Nome do Usuário:")
            txt_nome = QLineEdit()
            layout.addWidget(lbl_nome)
            layout.addWidget(txt_nome)
            
            # Botão para aplicar o filtro
            btn_filtrar = QPushButton("Filtrar")
            
            def aplicar_filtro():
                nome = txt_nome.text()
                print(f"Filtrando por Nome: {nome}")
                
                usuarios = self.obter_usuario_por_nome(nome)
                self.atualizar_tabela_usuario_filtrada(usuarios)
                
                dialog.close()
            
            btn_filtrar.clicked.connect(aplicar_filtro)
            layout.addWidget(btn_filtrar)
            
            dialog.setLayout(layout)
            dialog.exec()
        else:
            return

#*******************************************************************************************************
    def selecionar_todos(self):
        # Verificar se os checkboxes já estão visíveis na primeira coluna antes da coluna ID
        if self.table_widget.cellWidget(0, 0) is None:
            # Criar e exibir os checkboxes em cada linha da primeira coluna antes da coluna ID
            total_rows = self.table_widget.rowCount()
            for row in range(total_rows):
                for col in range(self.table_widget.columnCount()):
                    item = self.table_widget.item(row, col)
                    if col == 0 and item:  # Se for a primeira coluna e houver um item
                        # Criar e posicionar o QCheckBox
                        checkbox = QCheckBox()
                        self.table_widget.setCellWidget(row, col, checkbox)
        else:
            # Remover os checkboxes da primeira coluna antes da coluna ID
            total_rows = self.table_widget.rowCount()
            for row in range(total_rows):
                for col in range(self.table_widget.columnCount()):
                    if col == 0:
                        self.table_widget.removeCellWidget(row, col)


#*******************************************************************************************************
    def ordenar_usuario(self):
        # Implementação básica para ordenar produtos
        self.table_widget.sortItems(1, Qt.AscendingOrder)  # Ordenar pela coluna 1 em ordem ascendente
#*******************************************************************************************************
    def visualizar_imagem_usuario(self):
        if self.table_widget.currentRow() >= 0:
            row_index = self.table_widget.currentRow()
            id_usuario = int(self.table_widget.item(row_index, 0).text())

            imagem_data = self.recuperar_imagem_do_banco(id_usuario)

            if imagem_data:
                try:
                    print("Dados da imagem recuperados com sucesso para visualização.")

                    pixmap = QPixmap()
                    pixmap.loadFromData(imagem_data)

                    if pixmap.isNull():
                        print("Aviso: pixmap é nulo")
                        QMessageBox.warning(self, "Aviso", "Não foi possível carregar a imagem.")
                        return

                    # Salvar a imagem temporária no disco
                    with open("imagem_temporaria.png", "wb") as file:
                        file.write(imagem_data)

                    # Tentar abrir o arquivo com um visualizador de imagens padrão
                    os.startfile("imagem_temporaria.png")

                except Exception as e:
                    print(f"Erro ao processar imagem: {str(e)}")
            else:
                QMessageBox.warning(self, "Aviso", "Imagem não encontrada.")

#*******************************************************************************************************
    def verificar_usuario(self, usuario, senha):
        # Consulta SQL para verificar o usuário e senha
        query = "SELECT Acesso FROM users WHERE Usuário = ? AND Senha = ? COLLATE NOCASE"
        parameters = (usuario, senha)

        cursor = None  # Inicialize o cursor como None
        
        try:
            # Obter o cursor usando o método da classe DataBase
            cursor = self.db.execute_query(query, parameters)
            
            resultado = cursor.fetchone()
            
            if resultado:
                tipo_usuario = resultado[0]
                print(f"Resultado da consulta: {resultado}")
                print("Usuário autenticado com sucesso")
                return tipo_usuario.lower()
            else:
                print("Usuário ou senha incorretos")
                return None
        except Exception as e:
            print(f"Erro ao verificar usuário: {str(e)}")
            return None
        finally:
            # Fechar o cursor se ele foi inicializado
            if cursor:
                cursor.close()
#*******************************************************************************************************
    def obter_usuario_por_nome(self, nome):
        query = "SELECT * FROM users WHERE Nome LIKE ?"
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
    def fechar_janela_tabela(self):
        # Fechar a janela
        self.close()


    def limpar_campos_de_texto(self):
        self.main_window.txt_usuario.clear()

        