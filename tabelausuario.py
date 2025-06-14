from PySide6.QtWidgets import (QDialog, QPushButton, QVBoxLayout, QTableWidget, 
                               QTableWidgetItem, QMessageBox, QCheckBox, QLabel, QLineEdit, 
                               QLabel, QFrame,QMainWindow,QWidget,QComboBox,QHeaderView,
                               QAbstractItemView,QHBoxLayout)
from PySide6 import QtWidgets
from PySide6.QtGui import QPixmap, Qt, QImage,QBrush, QColor
from PySide6.QtCore import  Qt,QEvent,QTimer
from PySide6 import QtCore
from database import DataBase, sqlite3
import base64
import re
import os
from configuracoes import Configuracoes_Login

class TabelaUsuario(QMainWindow):
    def __init__(self, main_window, parent=None):
        super().__init__(parent)
        self.main_window = main_window
        self.frame_imagem_cadastro = QFrame()
        self.db = DataBase()
        self.setWindowTitle("Tabela de Usuários")
        self.setMinimumWidth(800)
        self.setMinimumHeight(600)

        self.config = Configuracoes_Login(self)
        self.config.carregar()

        self.usuarios = self.db.get_users()
        self.usuario_selecionado = False
        
        self.checkboxes = []  # Lista para armazenar os checkboxes
        
        self.coluna_checkboxes_adicionada = False  # Variável para controlar se a coluna de checkbox foi adicionada

        # Widget central e layout principal vertical
        widget_central = QWidget()
        self.layout_tabela = QVBoxLayout(widget_central)

        self.limpar_campos_de_texto()

        # Criar tabela
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(24)
        self.table_widget.setFocusPolicy(Qt.StrongFocus)
        self.table_widget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.table_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        font = self.table_widget.horizontalHeader().font()
        font.setBold(True)
        self.table_widget.horizontalHeader().setFont(font)
        self.table_widget.verticalHeader().setFont(font)

        # Criar QLabel para imagem
        self.label_imagem_usuario = QLabel()
        self.label_imagem_usuario.setScaledContents(True)
        layout_usuario = QVBoxLayout()
        layout_usuario.addWidget(self.label_imagem_usuario)
        self.main_window.frame_imagem_cadastro.setLayout(layout_usuario)

        # Botões (verticais para ficar empilhados e largos)
        self.btn_apagar_usuario = QPushButton("Apagar Usuários")
        self.btn_editar_usuario = QPushButton("Atualizar Usuário")
        self.btn_filtrar_usuario = QPushButton("Filtrar Usuários")
        self.btn_selecionar_todos = QCheckBox("Selecionar")
        self.btn_ordenar_usuario = QPushButton("Ordenar Usuários")
        self.btn_visualizar_imagem = QPushButton("Visualizar Imagem")
        self.btn_atualizar_tabela = QPushButton("Atualizar Tabela")

        layout_botoes = QVBoxLayout()
        layout_botoes.addWidget(self.btn_apagar_usuario)
        layout_botoes.addWidget(self.btn_editar_usuario)
        layout_botoes.addWidget(self.btn_filtrar_usuario)
        layout_botoes.addWidget(self.btn_ordenar_usuario)
        layout_botoes.addWidget(self.btn_visualizar_imagem)
        layout_botoes.addWidget(self.btn_atualizar_tabela)
        layout_botoes.addWidget(self.btn_selecionar_todos)

        # Faz os botões ficarem do tamanho da largura da janela
        for btn in [self.btn_apagar_usuario, self.btn_editar_usuario, self.btn_filtrar_usuario,
                    self.btn_selecionar_todos, self.btn_ordenar_usuario, self.btn_visualizar_imagem,
                    self.btn_atualizar_tabela]:
            btn.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)

        # Adicionar layout dos botões em cima
        self.layout_tabela.addLayout(layout_botoes)

        # Depois adicionar a tabela (ocupando o restante)
        self.layout_tabela.addWidget(self.table_widget)

        # Adicionar o frame de imagem (se quiser que fique embaixo da tabela)
        self.layout_tabela.addWidget(self.frame_imagem_cadastro)

        # Definir widget central
        self.setCentralWidget(widget_central)

        # Inicializar a tabela e limpar campos
        self.limpar_campos_de_texto()
        self.preencher_tabela_usuario()


        # Conectar sinais dos botões
        self.btn_apagar_usuario.clicked.connect(self.confirmar_apagar_usuario)
        self.btn_editar_usuario.clicked.connect(self.editar_usuario)
        self.btn_filtrar_usuario.clicked.connect(self.filtrar_usuario)
        self.btn_ordenar_usuario.clicked.connect(self.ordenar_usuario)
        self.btn_visualizar_imagem.clicked.connect(self.visualizar_imagem_usuario)
        self.btn_selecionar_todos.clicked.connect(self.selecionar_todos_users)
        self.btn_atualizar_tabela.clicked.connect(self.atualizar_tabela_usuario)

    
    def preencher_tabela_usuario(self):
        self.table_widget.setRowCount(0)
        column_titles = [
            "ID","Nome", "Usuário", "Senha", "Confirmar Senha", "CEP", "Endereço",
            "Número", "Cidade", "Bairro", "Estado", "Complemento", "Telefone", "Email",
            "Data de Nascimento", "RG", "CPF", "CNPJ",
            "Última Troca de Senha", "Data da Senha Cadastrada",
            "Data da Inclusão do Usuário", "Segredo", "Usuário Logado", "Acesso"
        ]

        for col, title in enumerate(column_titles):
            self.table_widget.setHorizontalHeaderItem(col, QTableWidgetItem(title))

        try:
            self.db.connecta()
            usuarios = self.db.obter_usuarios_sem_imagem()

            for usuario in usuarios:
                row_position = self.table_widget.rowCount()
                self.table_widget.insertRow(row_position)


                for i, dado in enumerate(usuario):
                    item = QTableWidgetItem(str(dado))
                    self.table_widget.setItem(row_position, i, item)
         

            self.table_widget.resizeColumnsToContents()
            self.table_widget.resizeRowsToContents()

            if self.table_widget.rowCount() == 0:
                self.exibir_mensagem_sem_usuarios()
            else:
                self.ocultar_mensagem_sem_usuarios()

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao acessar o banco de dados: {str(e)}")
#*******************************************************************************************************
    def exibir_mensagem_sem_usuarios(self):
        # Verificar se a QLabel já existe
        if not hasattr(self, 'label_sem_usuario'):
            self.label_sem_usuario = QLabel("Usuários cadastrados serão exibidos aqui...")
            self.label_sem_usuario.setAlignment(Qt.AlignCenter)
            self.label_sem_usuario.setStyleSheet("font-size: 16px; color: black;")
            
            # Verificar se o widget tem um layout
            if not self.table_widget.layout():
                self.main_layout = QVBoxLayout(self.table_widget)
                self.table_widget.setLayout(self.main_layout)
            else:
                self.main_layout = self.table_widget.layout()

            self.main_layout.addWidget(self.label_sem_usuario)

        self.label_sem_usuario.show()

    def ocultar_mensagem_sem_usuarios(self):
        if hasattr(self,"label_sem_usuario"):
            self.label_sem_usuario.hide()
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
            
            #Obter o nome do usuário 
            nome_usuario = self.table_widget.item(index, 1).text()
            
            # Remover a linha da tabela
            self.table_widget.removeRow(index)
            
            # Remover o usuário do banco de dados
            db = DataBase()
            try:
                db.connecta()
                db.remover_usuario(id_usuario)
                QMessageBox.information(self, "Sucesso", "Usuário removido com sucesso!")
                
                usuario = f"O Usuário {nome_usuario} foi removido."
                self.main_window.registrar_historico_usuarios("Removação de Usuário", usuario)
            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Erro ao remover o usuário: {str(e)}")
            finally:
                pass
        else:
            QMessageBox.warning(self, "Aviso", "Nenhuma célula selecionada ou célula vazia.")
#*******************************************************************************************************
    def recuperar_imagem_do_banco(self, id_usuario):
        imagem_blob = None
        try:
            connection = self.db.connecta()
            print("Conexão está ativa:", connection is not None)

            if connection:
                cursor = connection.cursor()
                cursor.execute("SELECT Imagem FROM users WHERE id = ?", (id_usuario,))
                result = cursor.fetchone()

                if result:
                    imagem_blob = result[0]
                    if imagem_blob:
                        imagem_bytes = base64.b64decode(imagem_blob)
                        return imagem_bytes  # Agora está como binário de imagem mesmo
                else:
                    print(f"Nenhum resultado retornado para ID: {id_usuario}")
                    return None

        except ValueError or AttributeError:
            pass
#*******************************************************************************************************
    def editar_usuario(self):
        if self.table_widget.currentRow() >= 0:
            row_index = self.table_widget.currentRow()
            id_usuario = int(self.table_widget.item(row_index, 0).text())

            # Obter a imagem do banco de dados
            imagem_data = self.recuperar_imagem_do_banco(id_usuario)

            if not hasattr(self, 'label_imagem_usuario') or self.label_imagem_usuario is None:
                self.label_imagem_usuario = QLabel()
                self.label_imagem_usuario.setScaledContents(True)  # Redimensiona a imagem para o tamanho do QLabel

            self.main_window.usuario_tem_imagem_salva = bool(imagem_data)

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

            # Recuperar dados do usuário diretamente do banco
            dados_usuario = self.db.recuperar_usuario_por_id(id_usuario)
            if dados_usuario:
                (usuario_nome, usuario_usuario, usuario_senha, usuario_confirmar_senha, usuario_cep, usuario_endereco,
                usuario_numero, usuario_cidade, usuario_bairro, usuario_estado, usuario_complemento, usuario_telefone,
                usuario_email, usuario_data_nascimento, usuario_rg, usuario_cpf, usuario_cnpj, usuario_acesso) = dados_usuario

                # Preencher os campos da MainWindow com os dados do usuário selecionado
                self.main_window.txt_nome.setText(usuario_nome or "")
                self.main_window.txt_usuario.setText(usuario_usuario or "")
                self.main_window.txt_senha.setText(usuario_senha or "")
                self.main_window.txt_confirmar_senha.setText(usuario_confirmar_senha or "")
                self.main_window.txt_cep.setText(usuario_cep or "")
                self.main_window.txt_endereco.setText(usuario_endereco or "")
                self.main_window.txt_numero.setText(usuario_numero or "")
                self.main_window.txt_cidade.setText(usuario_cidade or "")
                self.main_window.txt_bairro.setText(usuario_bairro or "")
                self.main_window.perfil_estado.setCurrentText(usuario_estado or "")
                self.main_window.txt_complemento.setText(usuario_complemento or "")
                self.main_window.txt_telefone.setText(usuario_telefone or "")
                self.main_window.txt_email.setText(usuario_email or "")
                self.main_window.txt_data_nascimento.setText(usuario_data_nascimento or "")
                self.main_window.txt_rg.setText(usuario_rg or "")
                self.main_window.txt_cpf.setText(usuario_cpf or "")
                self.main_window.txt_cnpj.setText(usuario_cnpj or "")
                self.main_window.perfil_usuarios.setCurrentText(usuario_acesso or "")


                # Atualizar o layout do frame_imagem_cadastro com o QLabel
                self.main_window.frame_imagem_cadastro.setVisible(True)  # Garante que o frame esteja visível
                self.main_window.frame_imagem_cadastro.layout().addWidget(self.label_imagem_usuario)

                self.main_window.is_editing = True  # Indica que um usuário está em edição
                self.main_window.selected_user_id = id_usuario  # Guarda o ID do usuário selecionado
                self.main_window.imagem_removida_usuario = False  # Indica que a imagem não foi removida

                self.usuario_selecionado = True  # Indica que um usuário foi selecionado

                self.close()
            else:
                print("Usuário não encontrado no banco de dados.")

    def usuario_foi_selecionado(self):
        return self.usuario_selecionado     

#*******************************************************************************************************
    def atualizar_tabela_usuario_filtrada(self, usuarios):
        self.table_widget.setRowCount(0)

        # Cabeçalhos: sem a coluna "Imagem"
        column_titles = [
            "ID","Nome", "Usuário", "Senha", "Confirmar Senha", "CEP", "Endereço",
            "Número", "Cidade", "Bairro", "Estado", "Complemento", "Telefone", "Email",
            "Data de Nascimento", "RG", "CPF", "CNPJ",
            "Última Troca de Senha", "Data da Senha Cadastrada",
            "Data da Inclusão do Usuário", "Segredo", "Usuário Logado", "Acesso"
        ]

        self.table_widget.setColumnCount(len(column_titles))
        for col, title in enumerate(column_titles):
            self.table_widget.setHorizontalHeaderItem(col, QTableWidgetItem(title))

        usuario_logado = self.config.obter_usuario_logado()

        for usuario in usuarios:
            # Remover a coluna "Imagem" (índice 18) de uma cópia da tupla
            dados = list(usuario)
            if len(dados) >= 25:
                del dados[18]  # Remove "Imagem"
                dados[23] = usuario_logado


            row_position = self.table_widget.rowCount()
            self.table_widget.insertRow(row_position)

            for col, data in enumerate(dados):
                item = self.formatar_texto(str(data))
                self.table_widget.setItem(row_position, col, item)

        self.table_widget.resizeColumnsToContents()
        self.table_widget.resizeRowsToContents()
#*******************************************************************************************************
    def obter_usuarios_por_filtro(self, campo, valor):
        query = f"""
            SELECT "ID","Nome", "Usuário", "Senha", "Confirmar Senha", "CEP", "Endereço",
            "Número", "Cidade", "Bairro", "Estado", "Complemento", "Telefone", "Email",
            "Data de Nascimento", "RG", "CPF", "CNPJ",
            "Última Troca de Senha", "Data da Senha Cadastrada",
            "Data da Inclusão do Usuário", "Segredo", "Usuário Logado", "Acesso"
            FROM users
            WHERE "{campo}" LIKE ?
        """
        parameters = (f"%{valor}%",)
        
        try:
            db = DataBase()
            connection = db.connecta()
            cursor = connection.cursor()
            cursor.execute(query, parameters)
            return cursor.fetchall()
        except Exception as e:
            print(f"Erro ao filtrar usuários por {campo}:", e)
            return []
        finally:
            if cursor:
                cursor.close()
#*******************************************************************************************************
    def filtrar_usuario(self):
        if hasattr(self, "checkbox_header_users"):
            QMessageBox.warning(
                None,
                "Aviso",
                "Desmarque o checkbox antes de filtrar os usuários."
            )
            return
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Filtrar Usuários")
        msg_box.setText("Deseja filtrar os usuários?")
        
        btn_sim = QPushButton("Sim")
        btn_nao = QPushButton("Não")
        
        msg_box.addButton(btn_sim, QMessageBox.YesRole)
        msg_box.addButton(btn_nao, QMessageBox.NoRole)
        msg_box.setDefaultButton(btn_sim)
        
        resposta = msg_box.exec()

        if msg_box.clickedButton() == btn_sim:
            dialog = QDialog(self)
            dialog.setWindowTitle("Escolha o Filtro")
            layout = QVBoxLayout()

            combo = QComboBox()
            filtros = [
                "Filtrar por Nome", "Filtrar Por Usuário", "Filtrar Por Acesso",
                "Filtrar Por Telefone", "Filtrar Por Email", "Filtrar Por RG",
                "Filtrar Por CPF", "Filtrar Por CNPJ"
            ]
            combo.addItems(filtros)
            layout.addWidget(combo)

            # Criação da label e line edit genéricos
            lbl_criterio = QLabel("Nome do Usuário:")
            txt_entrada = QLineEdit()
            layout.addWidget(lbl_criterio)
            layout.addWidget(txt_entrada)

            # Atualização da label dinamicamente
            def atualizar_label():
                texto = combo.currentText()
                mapeamento = {
                    "Filtrar por Nome": "Nome do Usuário:",
                    "Filtrar Por Usuário": "Usuário:",
                    "Filtrar Por Acesso": "Acesso do Usuário:",
                    "Filtrar Por Telefone": "Telefone do Usuário:",
                    "Filtrar Por Email": "Email do Usuário:",
                    "Filtrar Por RG": "RG do Usuário:",
                    "Filtrar Por CPF": "CPF do Usuário:",
                    "Filtrar Por CNPJ": "CNPJ do Usuário:"
                }
                lbl_criterio.setText(mapeamento.get(texto, "Digite o valor:"))

            combo.currentIndexChanged.connect(atualizar_label)

            # Botão de filtrar
            btn_filtrar = QPushButton("Filtrar")
            layout.addWidget(btn_filtrar)

            def formatar_texto(text):
                cursor_pos = txt_entrada.cursorPosition()
                criterio = combo.currentText()
                formatado = text  # valor padrão
                numero = ''.join(filter(str.isdigit, text))  # agora sempre existe

                if criterio == "Filtrar Por CPF":
                    numero = numero[:11]
                    if len(numero) <= 3:
                        formatado = numero
                    elif len(numero) <= 6:
                        formatado = "{}.{}".format(numero[:3], numero[3:])
                    elif len(numero) <= 9:
                        formatado = "{}.{}.{}".format(numero[:3], numero[3:6], numero[6:])
                    else:
                        formatado = "{}.{}.{}-{}".format(numero[:3], numero[3:6], numero[6:9], numero[9:])

                elif criterio == "Filtrar Por CNPJ":
                    numero = numero[:14]
                    if len(numero) <= 2:
                        formatado = numero
                    elif len(numero) <= 5:
                        formatado = "{}.{}".format(numero[:2], numero[2:])
                    elif len(numero) <= 8:
                        formatado = "{}.{}.{}".format(numero[:2], numero[2:5], numero[5:])
                    elif len(numero) <= 12:
                        formatado = "{}.{}.{}/{}".format(numero[:2], numero[2:5], numero[5:8], numero[8:])
                    else:
                        formatado = "{}.{}.{}/{}-{}".format(numero[:2], numero[2:5], numero[5:8], numero[8:12], numero[12:14])

                elif criterio == "Filtrar Por RG":
                    numero = numero[:9]
                    if len(numero) <= 2:
                        formatado = numero
                    elif len(numero) <= 5:
                        formatado = "{}.{}".format(numero[:2], numero[2:])
                    elif len(numero) <= 8:
                        formatado = "{}.{}.{}".format(numero[:2], numero[2:5], numero[5:])
                    else:
                        formatado = "{}.{}.{}-{}".format(numero[:2], numero[2:5], numero[5:8], numero[8:])

                elif criterio == "Filtrar Por Telefone":
                    numero = numero[:11]
                    if len(numero) <= 2:
                        formatado = "({})".format(numero)
                    elif len(numero) <= 6:
                        formatado = "({}) {}".format(numero[:2], numero[2:])
                    elif len(numero) <= 10:
                        formatado = "({}) {}-{}".format(numero[:2], numero[2:6], numero[6:])
                    else:
                        formatado = "({}) {}-{}".format(numero[:2], numero[2:7], numero[7:])

                # Evita loop de evento
                if txt_entrada.text() != formatado:
                    txt_entrada.blockSignals(True)
                    txt_entrada.setText(formatado)
                    nova_pos = min(cursor_pos + 1, len(formatado))
                    txt_entrada.setCursorPosition(nova_pos)
                    txt_entrada.blockSignals(False)

            txt_entrada.textEdited.connect(formatar_texto)

            def aplicar_filtro():
                criterio = combo.currentText()
                valor = txt_entrada.text()

                mapeamento_campo = {
                    "Filtrar por Nome": "Nome",
                    "Filtrar Por Usuário": "Usuário",
                    "Filtrar Por Acesso": "Acesso",
                    "Filtrar Por Telefone": "Telefone",
                    "Filtrar Por Email": "Email",
                    "Filtrar Por RG": "RG",
                    "Filtrar Por CPF": "CPF",
                    "Filtrar Por CNPJ": "CNPJ"
                }

                campo_bd = mapeamento_campo.get(criterio)
                if campo_bd:
                    usuarios = self.obter_usuarios_por_filtro(campo_bd, valor)
                    dialog.close()

                    if not usuarios:
                        QMessageBox.warning(
                            dialog,
                            "Nenhum resultado encontrado",
                            f"Nenhum usuário com {campo_bd} '{valor}' foi encontrado no sistema"
                        )
                    else:
                        self.atualizar_tabela_usuario_filtrada(usuarios)

            btn_filtrar.clicked.connect(aplicar_filtro)
            dialog.setLayout(layout)
            dialog.exec()
#*******************************************************************************************************
    def selecionar_todos_users(self):
        if not self.coluna_checkboxes_adicionada:
            self.selecionar_users_individual()
            return

        estado = self.checkbox_header_users.checkState()
        estado_checked = estado == Qt.Checked

        # Verifica se todos estavam marcados antes
        todos_estavam_marcados = all(checkbox.isChecked() for checkbox in self.checkboxes)

        # Marca ou desmarca os checkboxes
        for checkbox in self.checkboxes:
            checkbox.blockSignals(True)
            checkbox.setChecked(estado_checked)
            checkbox.blockSignals(False)

        # Se desmarcou "Selecionar Todos" E todos estavam marcados antes
        # Isso significa que o usuário quer remover a coluna
        if not estado_checked and todos_estavam_marcados:
            self.selecionar_users_individual()




                    
    def selecionar_users_individual(self):
        if self.table_widget.rowCount() == 0:
            QMessageBox.warning(self, "Aviso", "Não há usuários na tabela para selecionar.")
            return

        if self.coluna_checkboxes_adicionada:
            self.table_widget.removeColumn(0)
            self.table_widget.verticalHeader().setVisible(True)
            self.coluna_checkboxes_adicionada = False

            if hasattr(self, "checkbox_header_users"):
                self.checkbox_header_users.blockSignals(True)
                self.checkbox_header_users.setChecked(False)  # Garante que não fique marcado
                self.checkbox_header_users.blockSignals(False)
                
                self.checkbox_header_users.deleteLater()
                del self.checkbox_header_users

            self.checkboxes.clear()
            return

        self.table_widget.insertColumn(0)
        self.table_widget.setHorizontalHeaderItem(0, QTableWidgetItem(""))
        self.table_widget.setColumnWidth(0, 30)
        self.table_widget.horizontalHeader().setMinimumSectionSize(30)
        self.table_widget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)

        # Checkbox do cabeçalho
        self.checkbox_header_users = QCheckBox(self.table_widget)
        self.checkbox_header_users.setToolTip("Selecionar todos")
        self.checkbox_header_users.setChecked(False)
        self.checkbox_header_users.setFixedSize(20, 20)
        self.checkbox_header_users.stateChanged.connect(self.selecionar_todos_users)
        self.checkbox_header_users.show()

        self.atualizar_posicao_checkbox_header_users()
        self.table_widget.horizontalHeader().sectionResized.connect(self.atualizar_posicao_checkbox_header_users)
        QTimer.singleShot(0, self.atualizar_posicao_checkbox_header_users)

        self.checkboxes.clear()

        for row in range(self.table_widget.rowCount()):
            checkbox = QCheckBox()
            checkbox.stateChanged.connect(self.atualizar_selecao_todos_usuarios)

            container = QWidget()
            layout = QHBoxLayout(container)
            layout.addWidget(checkbox)
            layout.setAlignment(Qt.AlignCenter)
            layout.setContentsMargins(0, 0, 0, 0)

            self.table_widget.setCellWidget(row, 0, container)
            self.checkboxes.append(checkbox)

        self.table_widget.verticalHeader().setVisible(False)
        self.coluna_checkboxes_adicionada = True

        
    def atualizar_selecao_todos_usuarios(self):
        self.checkbox_header_users.blockSignals(True)

        # Atualizar o estado do "Selecionar Todos"
        all_checked = all(checkbox.isChecked() for checkbox in self.checkboxes if checkbox)
        any_checked = any(checkbox.isChecked() for checkbox in self.checkboxes if checkbox)

        if all_checked:
            self.checkbox_header_users.setCheckState(Qt.Checked)
        elif any_checked:
            self.checkbox_header_users.setCheckState(Qt.PartiallyChecked)
        else:
            self.checkbox_header_users.setCheckState(Qt.Unchecked)

        self.checkbox_header_users.blockSignals(False)

    def atualizar_posicao_checkbox_header_users(self):
        if hasattr(self, "checkbox_header_users") and self.coluna_checkboxes_adicionada:
            header = self.table_widget.horizontalHeader()

            x = header.sectionViewportPosition(0) + (header.sectionSize(0) - self.checkbox_header_users.width()) // 2 + 4
            y = (header.height() - self.checkbox_header_users.height()) // 2
            self.checkbox_header_users.move(x, y)

#*******************************************************************************************************
    def ordenar_usuario(self):
        if hasattr(self, "checkbox_header_users"):
            QMessageBox.warning(
                None,
                "Aviso",
                "Desmarque o checkbox antes de ordenar o histórico."
            )
            return
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
            pass
#*******************************************************************************************************
    def fechar_janela_tabela(self):
        # Fechar a janela
        self.close()


    def limpar_campos_de_texto(self):
        self.main_window.txt_usuario.clear()

    def atualizar_tabela_usuario(self):
        try:
            # Limpar a tabela antes de atualizar
            self.table_widget.setRowCount(0)
            self.table_widget.setColumnCount(23)  # Definir o número de colunas
            self.table_widget.setHorizontalHeaderLabels([
                 "Nome", "Usuário", "Senha", "Confirmar Senha", "CEP", "Endereço",
                "Número", "Cidade", "Bairro", "Estado", "Complemento", "Telefone", "Email",
                "Data de Nascimento", "RG", "CPF", "CNPJ",
                "Última Troca de Senha", "Data da Senha Cadastrada",
                "Data da Inclusão do Usuário", "Segredo", "Usuário Logado", "Acesso"
            ])

            conexao = self.db.connecta()
            cursor = conexao.cursor()
            
            cursor.execute("""
                SELECT Nome, Usuário, Senha, "Confirmar Senha", CEP, Endereço,Número,Cidade,
                Bairro, Estado, Complemento, Telefone, Email, "Data de Nascimento", RG, CPF,
                CNPJ, "Última Troca de Senha", "Data da Senha Cadastrada",
                "Data da Inclusão do Usuário", Segredo, "Usuário Logado", Acesso
                FROM users
            """)
            usuarios = cursor.fetchall()


            # Preencher a tabela com os dados atualizados
            for usuario in usuarios:
                row_position = self.table_widget.rowCount()
                self.table_widget.insertRow(row_position)
                for col, dado in enumerate(usuario):
                    item = self.formatar_texto(str(dado))
                    self.table_widget.setItem(row_position, col, item)         

            # Ajustar o tamanho das colunas
            self.table_widget.resizeColumnsToContents()
            self.table_widget.resizeRowsToContents()

        except Exception as e:
            print(f"Erro ao atualizar a tabela de usuários: {e}")

     # Função auxiliar para criar um QTableWidgetItem com texto centralizado e branco
    def formatar_texto(self, text):
        item = QTableWidgetItem(text)
        item.setTextAlignment(Qt.AlignCenter)
        item.setForeground(QBrush(QColor("black")))
        return item            
    
