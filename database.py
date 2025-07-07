import sqlite3
from datetime import datetime

class DataBase:
    def __init__(self, name="banco_de_dados.db"):
        self.name = name
        self.connection = None
        self.connecta()  # Tente conectar ao banco ao instanciar
#*********************************************************************************************************************
    def connecta(self):
        try:
            self.connection = sqlite3.connect("banco_de_dados.db")
            return self.connection
        except Exception as e:
            print(f"Erro ao conectar ao banco: {e}")
            return None
#*********************************************************************************************************************
    # Método para verificar se a conexão foi estabelecida com sucesso
    def verificar_conexao(self):
        if not self.connection:
            print("A conexão não foi estabelecida.")
            return False
        return True
 #*********************************************************************************************************************   
    def executar_comando(self, query, params=None):
        try:
            if not self.connection:
                self.connecta()

            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.connection.commit()
            return cursor
        except Exception as e:
            print(f"Erro ao executar comando: {e}")
            return None
#*********************************************************************************************************************
    def close_connection(self):
        try:
            if self.connection:  # Verifica se a conexão existe antes de fechar
                self.connection.close()
                self.connection = None
                print("O banco de dados foi fechado com sucesso.")
        except Exception as e:
            print("Erro ao fechar conexão:", e)
#*********************************************************************************************************************    
    def create_table_users(self):
        try:
            if self.tabela_existe("users"):
                print("A tabela 'users' já está criada.")
                return
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Nome TEXT NOT NULL,
                    Usuário TEXT UNIQUE NOT NULL,
                    Senha TEXT NOT NULL,
                    "Confirmar Senha" TEXT NOT NULL,
                    CEP TEXT,
                    Endereço TEXT,
                    Número TEXT,
                    Cidade TEXT,
                    Bairro TEXT, 
                    Estado TEXT, 
                    Complemento TEXT,
                    Telefone TEXT,
                    Email TEXT,
                    "Data de Nascimento" TEXT,          
                    RG TEXT,
                    CPF TEXT,
                    CNPJ TEXT,
                    Imagem BLOB,
                    "Última Troca de Senha" TEXT,
                    "Data da Senha Cadastrada" TEXT,
                    "Data da Inclusão do Usuário" TEXT,
                    Segredo TEXT,
                    "Usuário Logado" TEXT,
                    Acesso TEXT NOT NULL
                )
            """)
            print("Tabela de usuários criada com sucesso!")
        except Exception as e:
            print("Erro ao criar tabela de usuários:", e)
#*********************************************************************************************************************
    def create_table_users_inativos(self):
         try:
            if self.tabela_existe("users_inativos"):
                print("A tabela 'users_inativos' já está criada.")
                return
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users_inativos(
                    Nome TEXT NOT NULL,
                    Usuário TEXT UNIQUE NOT NULL,
                    Senha TEXT NOT NULL,
                    'Confirmar Senha' TEXT NOT NULL,
                    CEP TEXT NOT NULL,
                    Endereço TEXT NOT NULL,
                    Número TEXT NOT NULL,
                    Cidade TEXT NOT NULL,
                    Bairro TEXT NOT NULL,
                    Estado TEXT NOT NULL,  
                    Complemento TEXT,
                    Telefone TEXT NOT NULL,
                    Email TEXT NOT NULL,
                    "Data de Nascimento" TEXT NOT NULL,
                    RG TEXT NOT NULL,   
                    CPF TEXT NOT NULL,
                    CNPJ TEXT NOT NULL,
                    Imagem BLOB,
                    'Última Troca de Senha' TEXT,
                    'Data da Senha Cadastrada' TEXT,
                    'Data da Inclusão do Usuário' TEXT,
                    'Data da Inatividade do Usuário' TEXT,
                    Segredo TEXT,
                    'Usuário Logado' TEXT NOT NULL,
                    Acesso TEXT NOT NULL
                                    
                )
            """)
            print("Tabela de usuário inativos criada com sucesso! ")
         except Exception as e:
             print("Erro ao criar a tabela users_inativos", e)

#*********************************************************************************************************************
    def create_table_products(self):
        try:
            if self.connection is None:
                raise Exception("Conexão com o banco de dados não estabelecida.")
            if self.tabela_existe("products"):
                print("A tabela 'produtos' já está criada.")
                return
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS products(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    Produto TEXT NOT NULL,
                    Quantidade INTEGER NOT NULL,
                    Valor_Real REAL NOT NULL,
                    Desconto TEXT,
                    "Valor Total" TEXT,
                    "Data do Cadastro" TEXT,
                    Código_Item TEXT,
                    Cliente TEXT,
                    Descrição_Produto TEXT,
                    Usuário TEXT,
                    "Status da Saída" TEXT,
                    Imagem TEXT
                )
            """)
            self.connection.commit()  # Confirmar a transação
            print("Tabela de produtos criada com sucesso!")
        except Exception as e:
            print("Erro ao criar tabela de produtos:", e)
#*********************************************************************************************************************
    def create_table_products_saida(self):
        try:
            if self.connection is None:
                raise Exception("Conexão com o banco de dados não estabelecida.")
            if self.tabela_existe("products_saida"):
                print("A tabela 'produtos saída' já está criada.")
                return
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS products_saida(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    Produto TEXT NOT NULL,
                    Quantidade INTEGER NOT NULL,
                    "Valor do Produto"  NOT NULL,
                    Desconto,
                    "Valor Total" TEXT,
                    "Data de Saída" TEXT,
                    "Data da Criação" TEXT,
                    "Código do Produto" TEXT,
                    Cliente TEXT,
                    "Descrição do Produto",
                    Usuário TEXT,
                    'Status da Saída' TEXT,
                    Imagem BLOB
                )
            """)
            self.connection.commit()  # Confirmar a transação
            print("Tabela de produtos saída criada com sucesso!")
        except Exception as e:
            print("Erro ao criar tabela de produtos:", e)
#*********************************************************************************************************************
    def create_table_historico(self):
        try:
            if self.tabela_existe("historico"):
                print("A tabela 'histórico' já está criada.")
                return
            cursor = self.connection.cursor()
            cursor.execute("""
                 CREATE TABLE IF NOT EXISTS historico(
                    'Data e Hora' TEXT,
                    Usuário TEXT,
                    Ação TEXT,
                    Descrição TEXT      
                 )          
            """)
            self.connection.commit() # Confirmar a transação
            print("Tabela de histórico criada com sucesso! ")
        except Exception as e:
            print("Erro ao criar tabela de histórico: ", e)
#*********************************************************************************************************************            
    def create_table_historico_usuario(self):
        try:
            if self.tabela_existe("historico_usuarios"):
                print("A tabela 'historico_usuarios' já está criada")
                return
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS historico_usuarios(
                    'Data e Hora' TEXT,
                    Usuário TEXT,
                    Ação TEXT,
                    Descrição TEXT                                   
                )           
            """)
            self.connection.commit()
            print("Tabela de histórico usuários criada com sucesso! ")
        except Exception as e:
            print("Erro ao criar tabela de historico_usuarios: ", e)
#*********************************************************************************************************************
    def create_table_clientes_juridicos(self):
        try:
            if self.tabela_existe("clientes_juridicos"):
                print("A tabela 'clientes_juridicos' já está criada")
                return
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS clientes_juridicos(
                    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    "Nome do Cliente" TEXT,
                    "Razão Social" TEXT,
                    "Data da Inclusão" TEXT,
                    CNPJ TEXT,
                    Telefone TEXT,
                    CEP TEXT,
                    Endereço TEXT,
                    Número TEXT,
                    Complemento TEXT,
                    Cidade TEXT,
                    Bairro TEXT,
                    Estado TEXT,
                    "Status do Cliente" TEXT,
                    "Categoria do Cliente" TEXT,
                    "Última Atualização" TEXT,
                    "Origem do Cliente" TEXT,
                    "Valor Gasto Total" TEXT,
                    "Última Compra" TEXT  
                    )
                """)
            self.connection.commit()
            print("Tabela de clientes jurídicos criada com sucesso! ")
        except Exception as e:
            print("Erro ao criar tabela de clientes_juridicos: ", e)
#*********************************************************************************************************************
    def create_table_clientes_fisicos(self):
        try:
            if self.tabela_existe("clientes_fisicos"):
                print("A tabela 'clientes_fisicos' já está criada")
                return
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS clientes_fisicos(
                    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    "Nome do Cliente" TEXT,
                    "Data da Inclusão" TEXT,
                    CPF TEXT,
                    Telefone TEXT,
                    Endereço TEXT,
                    Número TEXT,
                    Complemento TEXT,
                    Cidade TEXT,
                    Bairro TEXT,
                    Estado TEXT,
                    "Status do Cliente" TEXT,
                    "Categoria do Cliente" TEXT,
                    "Última Atualização" TEXT,
                    "Origem do Cliente" TEXT,
                    "Valor Gasto Total" TEXT,
                    "Última Compra" TEXT  
                    )
                """)
            self.connection.commit()
            print("Tabela de clientes fisícos criada com sucesso! ")
        except Exception as e:
            print("Erro ao criar tabela de clientes_fisicos: ", e)
#*********************************************************************************************************************
    def insert_product(self, produto, quantidade, valor_real, desconto,valor_total, data_cadastro, 
                    codigo_item, cliente, descricao_produto, usuario, imagem=None):
        try:
            cursor = self.connection.cursor()

            # Substitua valores nulos por valores padrão
            produto = produto if produto is not None else "Não Cadastrado"
            quantidade = quantidade if quantidade is not None else 0
            valor_real = valor_real if valor_real is not None else 0.0
            desconto = desconto if desconto is not None else "Sem desconto"
            valor_total = valor_total if valor_total is not None else "Não Cadastrado"
            data_cadastro = data_cadastro if data_cadastro is not None else "Não Cadastrado"
            codigo_item = codigo_item if codigo_item is not None else "Não Cadastrado"
            cliente = cliente if cliente is not None else "Não Cadastrado"
            descricao_produto = descricao_produto if descricao_produto is not None else "Não Cadastrado"
            usuario = usuario if usuario is not None else "Não Cadastrado"
            imagem = imagem if imagem is not None else "Não Cadastrado"

            cursor.execute("""
                INSERT INTO products (Produto, Quantidade, Valor_Real, Desconto,"Valor Total", "Data do Cadastro", Código_Item, 
                        Cliente, Descrição_Produto,"Status da Saída", Imagem, Usuário) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?,?)
            """, (produto, quantidade, valor_real, desconto,valor_total, data_cadastro, codigo_item, 
                cliente, descricao_produto, 0,imagem, usuario))
            self.connection.commit()
            print("Produto inserido com sucesso!")
        except Exception as e:
            print("Erro ao inserir produto:", e)
#*********************************************************************************************************************
    def insert_imagem_produto(self, produto_id, imagem):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                UPDATE products
                SET Imagem = ?
                WHERE id = ?
            """, (imagem, produto_id))
            self.connection.commit()
            print("Imagem inserida com sucesso!")
        except Exception as e:
            print("Erro ao inserir imagem:", e)
#*********************************************************************************************************************
    def insert_imagem_usuario(self, id_usuario, imagem):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                UPDATE users
                SET Imagem = ?
                WHERE id = ?
            """, (imagem, id_usuario))
            self.connection.commit()
            print("Imagem inserida com sucesso!")
        except Exception as e:
            print("Erro ao inserir imagem:", e)
#*********************************************************************************************************************
    def retrieve_imagem(self, produto_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT Imagem FROM products WHERE id = ?", (produto_id,))
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                return None
        except Exception as e:
            print("Erro ao recuperar imagem:", e)
            return None
#*********************************************************************************************************************        
    def retrieve_imagem_usuario(self, id_usuario):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT Imagem FROM users WHERE id = ?", (id_usuario,))
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                return None
        except Exception as e:
            print("Erro ao recuperar imagem:", e)
            return None
#*********************************************************************************************************************
    def check_user(self, usuario, senha):
        try:
            query = "SELECT Usuário FROM users WHERE Usuário = ? AND Senha = ? COLLATE NOCASE"
            cursor = self.connection.cursor()  # Usar a conexão já existente
            cursor.execute(query, (usuario, senha))
            result = cursor.fetchone()
            return result[0] if result else None
        except Exception as e:
            print(f"Erro ao verificar usuário: {e}")
            return False  
#*********************************************************************************************************************
    def get_products(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM products")
            produtos = cursor.fetchall()
            return produtos
        except Exception as e:
            print("Erro ao obter produtos:", e)
            return []
#*********************************************************************************************************************        
    def get_users(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM users")
            usuarios = cursor.fetchall()

            # Substituir None por "Não Cadastrado"
            usuarios_modificados = []
            for usuario in usuarios:
                usuario_modificado = ["Não Cadastrado" if campo is None else campo for campo in usuario]
                usuarios_modificados.append(usuario_modificado)

            return usuarios_modificados
        except Exception as e:
            print("Erro ao obter os usuários:", e)
            return []

 #*********************************************************************************************************************       
    def remover_produto(self, produto_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM products WHERE id = ?", (produto_id,))
            self.connection.commit()
            print("Produto removido com sucesso!")
        except Exception as e:
            print("Erro ao apagar produto do banco de dados:", e)
#*********************************************************************************************************************
    def remover_usuario(self, id_usuario):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM users WHERE id = ?", (id_usuario,))
            self.connection.commit()
            print("Usuário removido com sucesso!")
        except Exception as e:
            print("Erro ao apagar usuário do banco de dados:", e)
#*********************************************************************************************************************
    def atualizar_produto(self, produto_id, produto=None, quantidade=None, 
                        valor_real=None,desconto=None, valor_total=None,
                        data_cadastro=None, codigo_item=None, cliente=None, descricao_produto=None, produto_imagem=None):
        try:
            # Monta a query SQL dinamicamente com base nos parâmetros fornecidos
            columns_to_update = []
            values_to_update = []

            if produto:
                columns_to_update.append("Produto = ?")
                values_to_update.append(produto)
            if quantidade is not None:
                columns_to_update.append("Quantidade = ?")
                values_to_update.append(quantidade)
            if valor_real is not None:
                columns_to_update.append("Valor_Real = ?")
                values_to_update.append(valor_real)
            if desconto is not None:
                columns_to_update.append("Desconto = ?")
                values_to_update.append(desconto)
            else:
                desconto = "Não Cadastrado"
                columns_to_update.append("Desconto = ?")
                values_to_update.append(desconto)
            if valor_total is not None:
                columns_to_update.append("Valor Total = ?")
                values_to_update.append(valor_total)
            else:
                valor_total = "Não Cadastrado"
                columns_to_update.append("Valor Total = ?")
                values_to_update.append(valor_total)
            if data_cadastro:
                columns_to_update.append("Data do Cadastro = ?")
                values_to_update.append(data_cadastro)
            else:
                data_cadastro = "Não Cadastrado"
                columns_to_update.append("Data do Cadastro = ?")
                values_to_update.append(data_cadastro)
            if codigo_item:
                columns_to_update.append("Código_Item = ?")
                values_to_update.append(codigo_item)
            else:
                codigo_item = "Não Cadastrado"
                columns_to_update.append("Código_Item = ?")
                values_to_update.append(codigo_item)
            if cliente:
                columns_to_update.append("Cliente = ?")
                values_to_update.append(cliente)
            else:
                cliente = "Não Cadastrado"
                columns_to_update.append("Cliente = ?")
                values_to_update.append(cliente)
            if descricao_produto:
                columns_to_update.append("Descrição_Produto = ?")
                values_to_update.append(descricao_produto)
            else:
                descricao_produto = "Não Cadastrado"
                columns_to_update.append("Descrição_Produto = ?")
                values_to_update.append(descricao_produto)
            if produto_imagem:
                columns_to_update.append("Imagem = ?")
                values_to_update.append(produto_imagem)
            else:
                produto_imagem = "Não Cadastrado"
                columns_to_update.append("Não Cadastrado")
                values_to_update.append(produto_imagem)


            # Converte as listas em strings separadas por vírgula
            set_clause = ", ".join(columns_to_update)

            query = f"""
                UPDATE products
                SET {set_clause}
                WHERE id = ?
            """

            # Adiciona o produto_id ao final da lista de valores
            values_to_update.append(produto_id)

            cursor = self.connection.cursor()
            cursor.execute(query, tuple(values_to_update))
            self.connection.commit()

            print("Produto atualizado com sucesso!")
        except Exception as e:
            print("Erro ao atualizar produto:", e)

#*********************************************************************************************************************
    def obter_caminho_imagem_produto(self, produto_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT Imagem FROM products WHERE id = ?", (produto_id,))
            resultado = cursor.fetchone()
            
            if resultado:
                # Retorna o caminho da imagem se o produto for encontrado
                return resultado[0]
            else:
                # Retorna None se o produto não for encontrado
                return None
        except Exception as e:
            print("Erro ao obter caminho da imagem:", e)
            return None
#*********************************************************************************************************************        
    def user_exists(self, Usuario, Telefone, Email, RG, CPF,CNPJ):
        try:
            if not self.connection:
                self.connecta()
            cursor = self.connection.cursor()

            cursor.execute("SELECT 1 FROM users WHERE Usuário = ?", (Usuario,))
            user_result = cursor.fetchone()

            cursor.execute("SELECT 1 FROM users WHERE Telefone = ?", (Telefone,))
            telefone_result = cursor.fetchone()

            cursor.execute("SELECT 1 FROM users WHERE Email = ?", (Email,))
            email_result = cursor.fetchone()

            cursor.execute("SELECT 1 FROM users WHERE RG = ?", (RG,))
            rg_result = cursor.fetchone()

            cursor.execute("SELECT 1 FROM users WHERE CPF = ?", (CPF,))
            cpf_result = cursor.fetchone()
            
            cursor.execute("SELECT 1 FROM users WHERE CNPJ = ?", (CNPJ,))
            cnpj_result = cursor.fetchone()

            if user_result:
                return 'usuario'
            elif telefone_result:
                return 'telefone'
            elif email_result:
                return 'email'
            elif rg_result:
                return 'rg'
            elif cpf_result:
                return 'cpf'
            elif cnpj_result:
                return 'cnpj'
            else:
                return None
        except Exception as e:
            print("Erro ao verificar se usuário existe:", e)
            return None
#*********************************************************************************************************************
    def insert_user(self, nome, usuario, senha, confirmar_senha, cep, endereco, numero, cidade, bairro, estado,
                complemento, telefone, email, data_nascimento, rg, cpf, cnpj, segredo, usuario_logado, acesso, imagem=None):
        try:
            cursor = self.connection.cursor()
            data_atual = datetime.now().strftime("%d/%m/%Y")

            # Função auxiliar para padronizar valores
            def padrao(valor):
                return valor.strip() if isinstance(valor, str) else valor
            def tratar(valor):
                return padrao(valor) if padrao(valor) else "Não Cadastrado"

            # Aplicar tratamento
            nome = tratar(nome)
            usuario = tratar(usuario)
            senha = tratar(senha)
            confirmar_senha = tratar(confirmar_senha)
            cep = tratar(cep)
            endereco = tratar(endereco)
            numero = tratar(numero)
            cidade = tratar(cidade)
            bairro = tratar(bairro)
            estado = tratar(estado)
            complemento = tratar(complemento)
            telefone = tratar(telefone)
            email = tratar(email)
            data_nascimento = tratar(data_nascimento)
            rg = tratar(rg)
            cpf = tratar(cpf)
            cnpj = tratar(cnpj)
            imagem = tratar(imagem)
            segredo = tratar(segredo)
            usuario_logado = tratar(usuario_logado)
            acesso = tratar(acesso)

            cursor.execute("""
                INSERT INTO users(Nome, Usuário, Senha, "Confirmar Senha", CEP, Endereço, Número, Cidade, Bairro, Estado, Complemento,
                                Telefone, Email, "Data de Nascimento", RG, CPF, CNPJ, Imagem, "Última Troca de Senha",
                                "Data da Senha Cadastrada", "Data da Inclusão do Usuário", Segredo, "Usuário Logado", Acesso)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                nome, usuario, senha, confirmar_senha, cep, endereco, numero, cidade, bairro, estado, complemento,
                telefone, email, data_nascimento, rg, cpf, cnpj, imagem,
                "Não Cadastrado", data_atual, data_atual, segredo, usuario_logado, acesso
            ))

            self.connection.commit()
            print("Usuário inserido com sucesso!")

        except Exception as e:
            print("Erro ao inserir usuário:", e)

#*********************************************************************************************************************
    def obter_caminho_imagem_usuario(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT Imagem FROM users WHERE id = ?", )
            resultado = cursor.fetchone()
            
            if resultado:
                # Retorna o caminho da imagem se o produto for encontrado
                return resultado[0]
            else:
                # Retorna None se o produto não for encontrado
                return None
        except Exception as e:
            print("Erro ao obter caminho da imagem:", e)
            return None
#*********************************************************************************************************************        
    def atualizar_usuario(self,id,nome=None, usuario=None, senha=None, confirmar_senha=None,
                      cep=None, endereco=None, numero=None, cidade=None, bairro=None, estado=None,
                      complemento=None, telefone=None, email=None, data_nascimento=None, rg=None,
                    cpf=None, cnpj=None, imagem=None, segredo=None, usuario_logado=None, acesso=None):
        try:
            campos = {
                "Nome": nome,
                "Usuário": usuario,
                "Senha": senha,
                "Confirmar Senha": confirmar_senha,
                "CEP": cep,
                "Endereço": endereco,
                "Número": numero,
                "Cidade": cidade,
                "Bairro": bairro,
                "Estado": estado,
                "Complemento": complemento,
                "Telefone": telefone,
                "Email": email,
                "Data_nascimento": data_nascimento,
                "RG": rg,
                "CPF": cpf,
                "CNPJ": cnpj,
                "Imagem": imagem,
                "Segredo": segredo,
                "Usuário Logado": usuario_logado,
                "Acesso": acesso
            }

            columns_to_update = []
            values_to_update = []

            for coluna, valor in campos.items():
                if valor is not None:
                    columns_to_update.append(f'"{coluna}" = ?')
                    values_to_update.append(valor if valor else "Não Cadastrado")

            if not columns_to_update:
                print("Nenhum campo para atualizar.")
                return

            set_clause = ", ".join(columns_to_update)
            query = f"UPDATE users SET {set_clause} WHERE id = ?"
            values_to_update.append(id)

            cursor = self.connection.cursor()
            cursor.execute(query, tuple(values_to_update))
            self.connection.commit()

            print("Usuário atualizado com sucesso!")

        except Exception as e:
            print("Erro ao atualizar usuário:", e)
#*********************************************************************************************************************
    def update_password(self, id_usuario, nova_senha):
        dias_desde_ultima_troca = self.verificar_tempo_ultima_troca(id_usuario)
        if dias_desde_ultima_troca is None or dias_desde_ultima_troca >= 15:  # Permitir atualização se for None
            cursor = self.connection.cursor()
            cursor.execute("UPDATE users SET Senha = ?, \"Última Troca de Senha\" = ? WHERE id = ?", 
                        (nova_senha, datetime.now().strftime("%d/%m/%Y"), id_usuario))
            self.connection.commit()
            return True
        return False
#*********************************************************************************************************************
    def atualizar_data_ultima_troca(self, id_usuario):
        data_atual = datetime.now().strftime("%d/%m/%Y ")
        cursor = self.connection.cursor()
        cursor.execute("UPDATE users SET \"Última Troca de Senha\" = ? WHERE id = ?", (data_atual, id_usuario))
        self.connection.commit()
#*********************************************************************************************************************
        
    def ultima_troca(self, usuario):
        try:
            cursor = self.connection.cursor()
            query = "SELECT strftime('%d/%m/%Y', [Última Troca de Senha']) FROM users WHERE Usuário = ?"
            cursor.execute(query, (usuario,))
            result = cursor.fetchone()
            
            if result:
                data_ultima_troca = result[0]
                if data_ultima_troca is not None:
                    return data_ultima_troca  # Retorna a data
                else:
                    return ""  # Se a data estiver vazia, retorna uma string vazia
            else:
                return None  # Se não houver resultado, retorna None
            
        except Exception as e:
            print("Erro ao obter a data da última troca de senha:", e)
            return None
#*********************************************************************************************************************

    def verificar_tempo_ultima_troca(self, id_usuario):
        cursor = self.connection.cursor()
        cursor.execute("SELECT \"Última Troca de Senha\" FROM users WHERE id = ?", (id_usuario,))
        result = cursor.fetchone()
        if result and result[0]:
            ultima_troca = datetime.strptime(result[0], "%d/%m/%Y ")
            dias_passados = (datetime.now() - ultima_troca).days
            return dias_passados
        return None

#*********************************************************************************************************************
    def executar_query(self, query, params=None):
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor.fetchall()  # Retorna todos os resultados da consulta
        except Exception as e:
            print(f"Erro ao executar a consulta: {str(e)}")
            return None

    def obter_produtos_base(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT Produto, Quantidade, Valor_Real, Desconto,"Valor Total", "Data do Cadastro", Código_Item, Cliente, 
                       Descrição_Produto, Imagem, 'Status da Saída' 
            FROM products
        """)
        produtos = cursor.fetchall()
        return produtos

    def obter_produtos_saida(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT Produto, Quantidade, "Valor do Produto", Desconto, "Valor Total","Data de Saída", "Data da Criação", "Código do Produto", 
                       Cliente, "Descrição do Produto", Usuário, "Status da Saída",Imagem 
            FROM products_saida
        """)
        produtos = cursor.fetchall()
        return produtos
    
    def obter_usuarios_ativos(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT Nome,Usuário,Senha,"Confirmar Senha",CEP,Endereço,Número,Cidade,Bairro,Estado,Complemento,Telefone,Email,
                       "Data de Nascimento",RG,CPF,CNPJ,"Última Troca de Senha","Data da Senha Cadastrada",
                       "Data da Inclusão do Usuário",Segredo,"Usuário Logado",Acesso
            FROM users
        """)
        usuarios = cursor.fetchall()
        return usuarios
    
    def obter_usuarios_inativos(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT Nome,Usuário,Senha,"Confirmar Senha",CEP,Endereço,Número,Cidade,Bairro,Estado,Complemento,Telefone,Email,
                       "Data de Nascimento",RG,CPF,CNPJ,"Última Troca de Senha","Data da Senha Cadastrada",
                       "Data da Inclusão do Usuário","Data da Inatividade do Usuário",Segredo,"Usuário Logado",Acesso
            FROM users_inativos
        """)
        usuarios = cursor.fetchall()
        return usuarios

    def remover_historico(self, valor_identificador, coluna_identificador="id"):
        try:
            cursor = self.connection.cursor()
            query = f"DELETE FROM historico WHERE \"{coluna_identificador}\" = ?"
            cursor.execute(query, (valor_identificador,))
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Erro ao remover registro do histórico: {str(e)}")
            return False
        
    def ensure_connection(self):
        if not self.connection:
            self.connecta()  # Método para estabelecer a conexão


    def get_user_secret(self, usuario_ou_email):
        try:
            self.ensure_connection()  # Garante que a conexão está ativa
            cursor = self.connection.cursor()
            query = "SELECT Secret FROM users WHERE (Usuário = ? OR Email = ?)"
            cursor.execute(query, (usuario_ou_email, usuario_ou_email))
            result = cursor.fetchone()
            if result:
                return result[0]  # Retorna o segredo
            else:
                print("Segredo não encontrado para o usuário.")
                return None
        except Exception as e:
            print("Erro ao buscar chave secreta:", e)
            return None

    def salvar_usuario_logado(self, usuario_logado):
        try:
            if not self.connection:
                self.connecta()
            query = "UPDATE users SET 'Usuário Logado' = ? WHERE id = 1"
            cursor = self.connection.cursor()
            cursor.execute(query, (usuario_logado,))
            self.connection.commit()
        except Exception as e:
            print(f"Erro ao salvar usuário logado: {e}")
        finally:
            pass  # Não feche a conexão automaticamente aqui

    def get_user_email(self, usuario):
        self.connecta()
        query = "SELECT Email FROM users WHERE Usuário = ?"
        cursor = self.connection.cursor()
        cursor.execute(query, (usuario,))
        result = cursor.fetchone()
        self.close_connection()
        return result[0] if result else None
    
    def tabela_existe(self, nome_tabela):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT name FROM sqlite_master WHERE type='table' AND name=?
        """, (nome_tabela,))
        return cursor.fetchone() is not None

    def salvar_saida_produto(self, produto_info):
        try:
            codigo_produto = produto_info[6]
            quantidade_nova = int(produto_info[1])

            query_verificar = """
            SELECT Quantidade FROM products_saida
            WHERE "Código do Produto" = ? AND "Status da Saída" = 1
            """
            resultado = self.executar_query(query_verificar, (codigo_produto,))

            if resultado:
                quantidade_atual = int(resultado[0][0])
                nova_quantidade = quantidade_atual + quantidade_nova

                query_update = """
                UPDATE products_saida
                SET Quantidade = ?
                WHERE "Código do Produto" = ? AND "Status da Saída" = 1
                """
                self.executar_comando(query_update, (nova_quantidade, codigo_produto))
            else:
                query_insert = """
                INSERT INTO products_saida 
                (Produto, Quantidade, "Valor do Produto", Desconto,"Valor Total", "Data de Saída", 
                "Data da Criação", "Código do Produto", Cliente, "Descrição do Produto", Usuário, Imagem,"Status da Saída")
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """
                self.executar_comando(query_insert, produto_info)

        except Exception as e:
            print(f"Erro ao salvar saída: {e}")   

    def obter_usuarios_sem_imagem(self):
        query = """
            SELECT "ID","Nome", "Usuário", "Senha", "Confirmar Senha", "CEP", "Endereço",
                "Número", "Cidade", "Bairro", "Estado", "Complemento", "Telefone", "Email",
                "Data de Nascimento", "RG", "CPF", "CNPJ",
                "Última Troca de Senha", "Data da Senha Cadastrada",
                "Data da Inclusão do Usuário", "Segredo", "Usuário Logado", "Acesso"
            FROM users
        """
        try:
            conn = self.connecta()
            cursor = conn.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print("Erro ao obter usuários:", e)
            return []
        finally:
            if cursor:
                cursor.close()

    def recuperar_usuario_por_id(self, id_usuario):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT Nome, Usuário, Senha, "Confirmar Senha", CEP, Endereço, Número, Cidade, Bairro,
                Estado, Complemento, Telefone, Email, "Data de Nascimento", RG, CPF, CNPJ, Acesso
            FROM users
            WHERE id = ?
        """, (id_usuario,))
        return cursor.fetchone()
    
    def upsert_cliente_juridico(self, nome_cliente, data_inclusao, status, categoria, ultima_atualizacao, 
                                origem, valor_gasto, ultima_compra):
        cursor = self.connection.cursor()

        cursor.execute("SELECT * FROM clientes_juridicos WHERE \"Nome do Cliente\" = ?", (nome_cliente,))
        existente = cursor.fetchone()

        if existente:
            cursor.execute("""
                UPDATE clientes_juridicos
                SET "Última Atualização" = ?, "Categoria do Cliente" = ?, 
                    "Origem do Cliente" = ?, "Valor Gasto Total" = "Valor Gasto Total" + ?, 
                    "Última Compra" = ?, "Status do Cliente" = ?
                WHERE "Nome do Cliente" = ?
            """, (
                ultima_atualizacao, categoria, origem, valor_gasto, ultima_compra, status, nome_cliente
            ))
        else:
            cursor.execute("""
                INSERT INTO clientes_juridicos (
                    "Nome do Cliente","Razão Social", "Data da Inclusão", "Status do Cliente", 
                    "Categoria do Cliente", "Última Atualização", 
                    "Origem do Cliente", "Valor Gasto Total", "Última Compra"
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?,?)
            """, (
                nome_cliente, data_inclusao, status, categoria, ultima_atualizacao,
                origem, valor_gasto, ultima_compra
            ))

        self.connection.commit()


    def update_dados_cliente_juridico_endereco(self, nome_cliente, cnpj, telefone, cep, endereco, numero, cidade, bairro):
        cursor = self.connection.cursor()

        cursor.execute("SELECT * FROM clientes_juridicos WHERE \"Nome do Cliente\" = ?", (nome_cliente,))
        existente = cursor.fetchone()

        if existente:
            # Atualiza os dados
            cursor.execute("""
                UPDATE clientes_juridicos
                SET CNPJ = ?, Telefone = ?, CEP = ?, Endereço = ?, Número = ?,Complemento = ?, Cidade = ?, Bairro = ?
                WHERE "Nome do Cliente" = ?
            """, (cnpj, telefone, cep, endereco, numero, cidade, bairro, nome_cliente))
        else:
            # Cria um novo cliente com os dados básicos
            cursor.execute("""
                INSERT INTO clientes_juridicos (
                    "Nome do Cliente", "Data da Inclusão", CNPJ, Telefone, CEP, Endereço, Número,Complemento,
                    Cidade, Bairro, "Status do Cliente", "Categoria do Cliente", "Última Atualização",
                    "Origem do Cliente", "Valor Gasto Total", "Última Compra"
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?,?)
            """, (
                nome_cliente, datetime.now().strftime("%d/%m/%Y"), cnpj, telefone, cep, endereco, numero,
                cidade, bairro, "Ativo", "Não informado", datetime.now().strftime("%d/%m/%Y"),
                "Nacional", 0.0, "Não informado"
            ))

        self.connection.commit()



    def get_dados_cliente_por_nome(self, nome_cliente):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT CNPJ, Telefone, CEP, Endereço, Número,CEP, Cidade, Bairro
            FROM users WHERE Nome = ?
        """, (nome_cliente,))
        return cursor.fetchone()
    
    def obter_clientes_juridicos(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT "Nome do Cliente", "Razão Social","Data da Inclusão", CNPJ, Telefone, CEP, Endereço, Número,
                Complemento,Cidade, Bairro,Estado, "Status do Cliente", "Categoria do Cliente", "Última Atualização",
                "Origem do Cliente", "Valor Gasto Total", "Última Compra"
            FROM clientes_juridicos
        """)
        return cursor.fetchall()



if __name__ == "__main__":
    db = DataBase()
    db.connecta()
    db.close_connection()
    
    