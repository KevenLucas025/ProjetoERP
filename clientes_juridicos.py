from PySide6.QtWidgets import (QLineEdit, QToolButton,QTableWidgetItem,
                               QMessageBox,QMainWindow,QVBoxLayout,QWidget,QLabel,QCheckBox,QPushButton,QScrollArea,QComboBox)
from PySide6.QtGui import QPixmap, QIcon,QColor,QBrush,QGuiApplication
from PySide6.QtCore import Qt
from database import DataBase
import sqlite3
import pandas as pd
from configuracoes import Configuracoes_Login
from datetime import datetime
from PySide6.QtGui import QKeySequence, QShortcut

class Clientes:
    def __init__(self, line_clientes: QLineEdit,main_window,btn_adicionar_cliente_juridico,
                 btn_editar_clientes,btn_excluir_clientes,btn_visualizar_clientes,btn_enviaremail_clientes,
                 btn_gerar_relatorio_clientes,btn_marcar_como_clientes,btn_historico_clientes):
        self.line_clientes = line_clientes
        self.imagem_line()
        self.db = DataBase("banco_de_dados.db")
        self.config = Configuracoes_Login(self)
        self.main_window = main_window
        self.table_clientes_juridicos = self.main_window.table_clientes_juridicos  # Referência para a tabela no main window
        self.btn_adicionar_cliente_juridico = btn_adicionar_cliente_juridico
        self.btn_editar_clientes = btn_editar_clientes
        self.btn_excluir_clientes = btn_excluir_clientes
        self.btn_visualizar_clientes = btn_visualizar_clientes
        self.btn_enviaremail_clientes = btn_enviaremail_clientes
        self.btn_gerar_relatorio_clientes = btn_gerar_relatorio_clientes
        self.btn_marcar_como_clientes = btn_marcar_como_clientes
        self.btn_historico_clientes = btn_historico_clientes
        self.btn_adicionar_cliente_juridico.clicked.connect(self.exibir_janela_cadastro_cliente)
        
        # ✅ Atalho de teclado F5 para atualizar a tabela
        atalho_f5 = QShortcut(QKeySequence("F5"),self.main_window)
        atalho_f5.activated.connect(self.carregar_clientes_juridicos)

    # Função auxiliar para criar um QTableWidgetItem com texto centralizado
    def formatar_texto_juridico(self, text):
        item = QTableWidgetItem(text)
        item.setTextAlignment(Qt.AlignCenter)  # Centraliza o texto
        item.setForeground(QBrush(QColor("white")))
        return item
                
    def carregar_clientes_juridicos(self):
        try:
            with self.db.connecta() as conexao:
                cursor = conexao.cursor()

                cursor.execute("""
                    SELECT 
                        "Nome do Cliente",
                        "Razão Social",
                        "Data da Inclusão",
                        CNPJ, 
                        Telefone, 
                        CEP, 
                        Endereço, 
                        Número,
                        Complemento,
                        Cidade, 
                        Bairro,
                        Estado,
                        "Status do Cliente", 
                        "Categoria do Cliente",
                        "Última Atualização",
                        "Origem do Cliente",
                        "Valor Gasto Total",
                        "Última Compra"
                    FROM clientes_juridicos
                    ORDER BY "Data da Inclusão" DESC
                """)
                
                dados = cursor.fetchall()

                # Limpa a tabela antes de recarregar
                self.table_clientes_juridicos.setRowCount(0)
                

                for linha_idx, linha_dados in enumerate(dados):
                    self.table_clientes_juridicos.insertRow(linha_idx)
                    for coluna_idx, dado in enumerate(linha_dados):
                        item = self.formatar_texto_juridico(str(dado))
                        self.table_clientes_juridicos.setItem(linha_idx, coluna_idx, item)
                        
                # Redimensiona apenas uma vez após preencher
                self.table_clientes_juridicos.resizeColumnsToContents()
                self.table_clientes_juridicos.resizeRowsToContents()

        except Exception as e:
            QMessageBox.critical(None, "Erro", f"Erro ao carregar clientes: \n{e}")
            
    



    def imagem_line(self):
        # Criar botão da lupa
        self.botao_lupa = QToolButton(self.line_clientes)
        self.botao_lupa.setCursor(Qt.PointingHandCursor)  # Muda o cursor ao passar o mouse
        self.botao_lupa.setIcon(QIcon(QPixmap("imagens/pngegg.png")))  # Substitua pelo caminho correto
        self.botao_lupa.setStyleSheet("border: none; background: transparent;")  # Sem fundo e sem borda
        
        # Definir tamanho do botão
        altura = self.line_clientes.height() - 4  # Ajustar altura conforme a LineEdit
        self.botao_lupa.setFixedSize(altura, altura)

        # Posicionar o botão no canto direito da LineEdit
        self.botao_lupa.move(self.line_clientes.width() - altura + 45, 2)

        # Ajustar padding para o texto não sobrepor o botão
        self.line_clientes.setStyleSheet(
            "QLineEdit {"
            "    color: black;"
            "    background-color: rgb(240, 240, 240);"
            "    border: 2px solid rgb(50, 150, 250);"
            "    border-radius: 6px;"
            "    padding: 3px;"  # Padding normal
            f"    padding-right: {altura + 5}px;"  # Ajuste para o botão
            "}"
            "QLineEdit::placeholderText {"
            "    color: black;"
            "}"
        )

        # Conectar clique do botão a uma função
        self.botao_lupa.clicked.connect(self.buscar)

    def buscar(self):
        QMessageBox.information(
            None,
            "Aviso",
            "Essa função ainda não está disponível"
        )

    def exibir_janela_cadastro_cliente(self):
        self.campos_cliente_juridico = {}
        self.informacoes_obrigatorias_clientes()
        
        self.janela_cadastro = QMainWindow()
        self.janela_cadastro.resize(700, 550)
        self.janela_cadastro.setWindowTitle("Cadastro do Cliente")
        self.janela_cadastro.setStyleSheet("""
            background-color: rgb(0, 80, 121);
        """)

        # Centralizar a janela
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_geometry = self.janela_cadastro.frameGeometry()
        window_geometry.moveCenter(screen_geometry.center())
        self.janela_cadastro.move(window_geometry.topLeft())

        # Conteúdo do formulário
        conteudo = QWidget()
        layout = QVBoxLayout(conteudo)
        conteudo.setStyleSheet("""
            QLineEdit {
                color: black;
                background-color: rgb(240, 240, 240);
                border: 2px solid rgb(50, 150, 250);
                border-radius: 6px;
                padding: 3px;
            }
            QLineEdit::placeholderText {
                color: black;
            }
        """)

        def add_linha(titulo, widget=None):
            layout.addWidget(QLabel(titulo))
            if widget is None:
                widget = QLineEdit()
            layout.addWidget(widget)
            chave_sem_ponto = titulo.rstrip(":")  # remove ':' do final
            self.campos_cliente_juridico[chave_sem_ponto] = widget


        add_linha("Nome do Cliente")
        add_linha("Razão Social")
        add_linha("CNPJ")
        cnpj_widget = self.campos_cliente_juridico["CNPJ"]
        cnpj_widget.textChanged.connect(lambda text: self.main_window.formatar_cnpj(text, cnpj_widget))
        add_linha("Telefone")
        telefone_widget = self.campos_cliente_juridico["Telefone"]
        telefone_widget.textChanged.connect(lambda text: self.main_window.formatar_telefone(text, telefone_widget))        
        add_linha("CEP")
        cep_widget = self.campos_cliente_juridico["CEP"]
        # Formatação do CEP enquanto digita
        cep_widget.textChanged.connect(lambda text: self.main_window.formatar_cep(text,cep_widget))
        # Buscar dados do CEP ao terminar de digitar
        cep_widget.editingFinished.connect(lambda: self.on_cep_editing_finished_cadastro(cep_widget))
        add_linha("Endereço")
        add_linha("Número")
        add_linha("Complemento")
        add_linha("Cidade")
        add_linha("Bairro")

        # Aqui adiciona Estado logo após Bairro
        combobox_estado_cliente = QComboBox()
        combobox_estado_cliente.addItems([
            "Selecionar","AC","AL","AP","AM","BA","CE","DF","ES","GO","MA","MT",
            "MS","MG","PA","PB","PR","PE","PI","RJ","RN","RS","RO","RR","SC","SP","SE","TO"
        ])
        combobox_estado_cliente.setCurrentIndex(0) # Seleciona "Selecionar" por padrão
        combobox_estado_cliente.setStyleSheet("""
            QComboBox { 
                background-color: white; 
                border: 3px solid rgb(50,150,250); 
                border-radius: 5px; 
                color: black; 
                padding: 5px;
            }
            QComboBox QAbstractItemView {
                background-color: white; 
                color: black; 
                border: 1px solid #ccc; 
                selection-background-color: #e5e5e5; 
                selection-color: black;
            }
            QComboBox QAbstractItemView QScrollBar:vertical {
                background: #f5f5f5; 
                width: 12px; 
                border: none;
            }
            QComboBox QAbstractItemView QScrollBar::handle:vertical {
                background: #cccccc; 
                min-height: 20px; 
                border-radius: 5px;
            }
            QComboBox QAbstractItemView QScrollBar::add-line:vertical, 
            QComboBox QAbstractItemView QScrollBar::sub-line:vertical {
                background: none;
                height: 0px;  /* Remove os botões de linha (setas de cima e baixo) */
            }
            QComboBox QAbstractItemView QScrollBar::add-page:vertical, 
            QComboBox QAbstractItemView QScrollBar::sub-page:vertical {
                background: none;
            }
        """)
        add_linha("Estado", combobox_estado_cliente)
        add_linha("Nacionalidade")
        add_linha("Categoria do Cliente")

        combobox_status_cliente = QComboBox()
        combobox_status_cliente.addItems(["Selecionar","Ativo","Inativo"])
        combobox_status_cliente.setCurrentIndex(0) # Seleciona "Selecionar" por padrão
        combobox_status_cliente.setStyleSheet("""
            QComboBox { 
                background-color: white; 
                border: 3px solid rgb(50,150,250); 
                border-radius: 5px; 
                color: black; 
                padding: 5px;
            }
            QComboBox QAbstractItemView {
                background-color: white; 
                color: black; 
                border: 1px solid #ccc; 
                selection-background-color: #e5e5e5; 
                selection-color: black;
            }
            QComboBox QAbstractItemView QScrollBar:vertical {
                background: #f5f5f5; 
                width: 12px; 
                border: none;
            }
            QComboBox QAbstractItemView QScrollBar::handle:vertical {
                background: #cccccc; 
                min-height: 20px; 
                border-radius: 5px;
            }
            QComboBox QAbstractItemView QScrollBar::add-line:vertical, 
            QComboBox QAbstractItemView QScrollBar::sub-line:vertical {
                background: none;
                height: 0px;  /* Remove os botões de linha (setas de cima e baixo) */
            }
            QComboBox QAbstractItemView QScrollBar::add-page:vertical, 
            QComboBox QAbstractItemView QScrollBar::sub-page:vertical {
                background: none;
            }
        """)
        add_linha("Status do Cliente:", combobox_status_cliente)    

        btn_fazer_cadastro = QPushButton("Fazer o Cadastro")
        btn_fazer_cadastro.clicked.connect(self.cadastrar_clientes_juridicos)
        btn_fazer_cadastro.setStyleSheet("""
            QPushButton {
                color: rgb(255, 255, 255);
                border-radius: 8px;
                font-size: 16px;
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255));
                border: 4px solid transparent;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255));
                color: black;
            }
        """)
        layout.addWidget(btn_fazer_cadastro)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(conteudo)

        self.janela_cadastro.setCentralWidget(scroll_area)
        self.janela_cadastro.show()



    def cadastrar_clientes_juridicos(self):
        try:
            with self.db.connecta() as conexao:
                cursor = conexao.cursor()
                usuario_logado = self.config.obter_usuario_logado()

                # Coletar dados dos campos
                get = lambda campo: self.campos_cliente_juridico[campo].text().strip() \
                    if isinstance(self.campos_cliente_juridico[campo], QLineEdit) \
                    else self.campos_cliente_juridico[campo].currentText()

                nome = get("Nome do Cliente")
                razao_social = get("Razão Social")
                cnpj = get("CNPJ")
                telefone = get("Telefone")
                cep = get("CEP")
                endereco = get("Endereço")
                numero = get("Número")
                complemento = get("Complemento")
                cidade = get("Cidade")
                bairro = get("Bairro")
                estado = get("Estado")
                nacionalidade = get("Nacionalidade")
                categoria = get("Categoria do Cliente")
                status = get("Status do Cliente")

                # Verificar se o cliente já existe
                cursor.execute("""
                    SELECT 1 FROM clientes_juridicos 
                    WHERE CNPJ = ? OR "Razão Social" = ?
                """, (cnpj, razao_social))

                if cursor.fetchone():
                    QMessageBox.warning(None, "Cliente já existe", "Já existe um cliente com este CNPJ ou Razão Social.")
                    return

                # Validação de todos os campos obrigatórios
                for campo, mensagem in self.campos_obrigatorios_clientes.items():
                    widget = self.campos_cliente_juridico[campo]
                    valor = widget.text().strip() if isinstance(widget, QLineEdit) else widget.currentText()
                    
                    if not valor or (isinstance(widget, QComboBox) and valor == "Selecionar"):
                        QMessageBox.warning(None, "Atenção", mensagem)
                        return
                    

                data_inclusao = datetime.now().strftime("%d/%m/%Y %H:%M")
                # Inserir no banco
                cursor.execute("""
                    INSERT INTO clientes_juridicos(
                        "Nome do Cliente", "Razão Social", "Data da Inclusão", CNPJ, Telefone, CEP, Endereço, Número,
                        Complemento, Cidade, Bairro, Estado, "Status do Cliente", "Categoria do Cliente", "Origem do Cliente"
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    nome,razao_social, data_inclusao, cnpj, telefone, cep, endereco, numero,complemento, cidade,
                    bairro,estado, status, categoria, nacionalidade 
                ))

                conexao.commit()
                QMessageBox.information(None, "Sucesso", "Cliente cadastrado com sucesso!")
                # Redimensiona apenas uma vez após preencher
                self.table_clientes_juridicos.resizeColumnsToContents()
                self.table_clientes_juridicos.resizeRowsToContents()
                self.limpar_campos_clientes()
                self.carregar_clientes_juridicos()

        except Exception as e:
            QMessageBox.critical(None, "Erro", f"Erro ao cadastrar cliente: \n{e}")

    def informacoes_obrigatorias_clientes(self):
        self.campos_obrigatorios_clientes = {
            "Nome do Cliente": "O campo Nome do Cliente é obrigatório.",
            "Razão Social": "O campo de Razão Social é obrigatório",
            "CNPJ": "O campo CNPJ é obrigatório.",
            "Telefone": "O campo Telefone é obrigatório.",
            "CEP": "O campo CEP é obrigatório.",
            "Endereço": "O campo Endereço é obrigatório.",
            "Número": "O campo Número é obrigatório.",
            "Cidade": "O campo Cidade é obrigatório.",
            "Bairro": "O campo Bairro é obrigatório.",
            "Estado": "O campo de Estado é obrigatório",
            "Nacionalidade": "O campo Nacionalidade é obrigatório.",
            "Categoria do Cliente": "O campo Categoria do Cliente é obrigatório.",
            "Status do Cliente": "Você deve selecionar um status válido para o cliente.",
        }

        
    def limpar_campos_clientes(self):
        for campo, widget in self.campos_cliente_juridico.items():
            if isinstance(widget,QLineEdit):
                widget.clear()
            elif isinstance(widget, QComboBox):
                widget.setCurrentIndex(0) # Volta para "Selecionar"
                    
    def on_cep_editing_finished_cadastro(self, cep_widget):
        cep_digitado = cep_widget.text()
        dados_cep = self.main_window.buscar_cep(cep_digitado)
        if dados_cep:
            self.preencher_campos_cep_cadastro(dados_cep)

    def preencher_campos_cep_cadastro(self, dados):
        if dados is None:
            return

        # Preencher os campos do seu formulário usando self.campos_cliente_juridico
        self.campos_cliente_juridico["Endereço"].setText(dados.get("logradouro", ""))
        self.campos_cliente_juridico["Bairro"].setText(dados.get("bairro", ""))
        self.campos_cliente_juridico["Cidade"].setText(dados.get("localidade", ""))

        complemento = dados.get("complemento", "")
        if any(char.isdigit() for char in complemento):
            self.campos_cliente_juridico["Número"].setText(complemento)

        estado = dados.get("uf", "")
        # Se tiver um combobox para estado, aqui você ajusta o índice
        if "Estado" in self.campos_cliente_juridico:
            estado_combobox = self.campos_cliente_juridico["Estado"]
            index_estado = estado_combobox.findText(estado)
            if index_estado != -1:
                estado_combobox.setCurrentIndex(index_estado)
