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
            if not self.connection:  # Verifica se já existe uma conexão
                self.connection = sqlite3.connect(self.name)
        except Exception as e:
            print(f"Erro ao conectar ao banco: {e}")

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
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Nome TEXT NOT NULL,
                    Usuário TEXT UNIQUE NOT NULL,
                    Senha TEXT NOT NULL,
                    "Confirmar Senha" TEXT NOT NULL,
                    Acesso TEXT NOT NULL,
                    Endereço TEXT,
                    CEP TEXT,
                    CPF TEXT,
                    Número TEXT,
                    Estado TEXT,
                    Email TEXT,
                    Complemento TEXT,
                    Telefone TEXT,
                    Data_nascimento TEXT,
                    RG TEXT,
                    Imagem BLOB,
                    "Última Troca de Senha" TEXT,
                    "Data da Senha Cadastrada" TEXT,
                    "Data da Inclusão do Usuário" TEXT,
                     Secret TEXT       
                    
                )
            """)
            print("Tabela de usuários criada com sucesso!")
        except Exception as e:
            print("Erro ao criar tabela de usuários:", e)

#*********************************************************************************************************************
    def create_table_products(self):
        try:
            if self.connection is None:
                raise Exception("Conexão com o banco de dados não estabelecida.")
            
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS products(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    Produto TEXT NOT NULL,
                    Quantidade INTEGER NOT NULL,
                    Valor_Real REAL NOT NULL,
                    Desconto REAL,
                    Data_Compra TEXT,
                    Código_Item TEXT,
                    Cliente TEXT,
                    Descrição_Produto TEXT,
                    Usuário,
                    Imagem BLOB
                )
            """)
            self.connection.commit()  # Confirmar a transação
            print("Tabela de produtos criada com sucesso!")
        except Exception as e:
            print("Erro ao criar tabela de produtos:", e)

    def create_table_products_saida(self):
        try:
            if self.connection is None:
                raise Exception("Conexão com o banco de dados não estabelecida.")
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS products_saida(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    Produto TEXT NOT NULL,
                    Quantidade INTEGER NOT NULL,
                    "Valor do Produto"  NOT NULL,
                    Desconto,
                    "Data de Saída" TEXT,
                    "Data da Criação" TEXT,
                    "Código do Produto" TEXT,
                    Cliente TEXT,
                    "Descrição do Produto",
                    Usuário TEXT,
                    Status TEXT,
                    'Status da Saída' TEXT,
                    Imagem BLOB
                )
            """)
            self.connection.commit()  # Confirmar a transação
            print("Tabela de produtos saída criada com sucesso!")
        except Exception as e:
            print("Erro ao criar tabela de produtos:", e)

    def create_table_historico(self):
        pass

#*********************************************************************************************************************
    def insert_product(self, produto, quantidade, valor_real, desconto, data_compra, 
                    codigo_item, cliente, descricao_produto, usuario, imagem=None):
        try:
            cursor = self.connection.cursor()

            # Substitua valores nulos por valores padrão
            produto = produto if produto is not None else "Não Cadastrado"
            quantidade = quantidade if quantidade is not None else 0
            valor_real = valor_real if valor_real is not None else 0.0
            desconto = desconto if desconto is not None else "Sem desconto"
            data_compra = data_compra if data_compra is not None else "Não Cadastrado"
            codigo_item = codigo_item if codigo_item is not None else "Não Cadastrado"
            cliente = cliente if cliente is not None else "Não Cadastrado"
            descricao_produto = descricao_produto if descricao_produto is not None else "Não Cadastrado"
            usuario = usuario if usuario is not None else "Não Cadastrado"
            imagem = imagem if imagem is not None else "Não Cadastrado"

            cursor.execute("""
                INSERT INTO products (Produto, Quantidade, Valor_Real, Desconto, Data_Compra, Código_Item, 
                        Cliente, Descrição_Produto, Imagem, Usuário) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (produto, quantidade, valor_real, desconto, data_compra, codigo_item, 
                cliente, descricao_produto, imagem, usuario))
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
            query = "SELECT Senha FROM users WHERE Usuário = ? AND Senha = ? COLLATE NOCASE"
            cursor = self.connection.cursor()  # Usar a conexão já existente
            cursor.execute(query, (usuario, senha))
            result = cursor.fetchone()
            return result[0] if result else None
        except Exception as e:
            print(f"Erro ao verificar usuário: {e}")
            return False
#*********************************************************************************************************************
    def user_exists_usuario(self, usuario):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT 1 FROM users WHERE Usuário = ?", (usuario,))
            result = cursor.fetchone()
            return bool(result)  # Retorna True se o usuário existir, False caso contrário
        except Exception as e:
            print("Erro ao verificar se usuário existe:", e)
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
                        valor_real=None,desconto=None, 
                        data_compra=None, codigo_item=None, cliente=None, descricao_produto=None, produto_imagem=None):
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
            if data_compra:
                columns_to_update.append("Data_Compra = ?")
                values_to_update.append(data_compra)
            else:
                data_compra = "Não Cadastrado"
                columns_to_update.append("Data_Compra = ?")
                values_to_update.append(data_compra)
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
    def user_exists(self, CPF, Usuario):
        try:
            if not self.connection:  # Verifica se a conexão está ativa
                self.connecta()
            cursor = self.connection.cursor()
            cursor.execute("SELECT 1 FROM users WHERE CPF = ?", (CPF,))
            cpf_result = cursor.fetchone()
            
            cursor.execute("SELECT 1 FROM users WHERE Usuário = ?", (Usuario,))
            user_result = cursor.fetchone()
            
            if cpf_result:
                return 'cpf'
            elif user_result:
                return 'Usuário'
            else:
                return None
        except Exception as e:
            print("Erro ao verificar se usuário existe:", e)
            return None

            
#*********************************************************************************************************************
    def insert_user(self, nome, usuario, senha, confirmar_senha, acesso, endereco, cep, cpf, numero, estado, email, 
                telefone, rg, data_nascimento, complemento, usuario_logado, imagem=None):
        try:
            cursor = self.connection.cursor()

            # Definindo a data atual como a data de última troca de senha
            data_atual = datetime.now().strftime("%d/%m/%Y")

            # Substituir None ou valores vazios por "Não Cadastrado"
            nome = nome or "Não Cadastrado"
            usuario = usuario or "Não Cadastrado"
            senha = senha or "Não Cadastrado"
            confirmar_senha = confirmar_senha or "Não Cadastrado"
            acesso = acesso or "Não Cadastrado"
            endereco = endereco or "Não Cadastrado"
            cep = cep or "Não Cadastrado"
            cpf = cpf or "Não Cadastrado"
            numero = numero or "Não Cadastrado"
            estado = estado or "Não Cadastrado"
            email = email or "Não Cadastrado"
            telefone = telefone or "Não Cadastrado"
            rg = rg or "Não Cadastrado"
            data_nascimento = data_nascimento or "Não Cadastrado"
            complemento = complemento or "Não Cadastrado"
            imagem = imagem or "Não Cadastrado"
            usuario_logado = usuario_logado or "Não Cadastrado"  # Certifique-se de que o valor está definido

            cursor.execute("""
                INSERT INTO users(Nome, Usuário, Senha, "Confirmar Senha", Acesso, Endereço, CEP, CPF, Número, Estado, 
                                Email, Telefone, RG, Data_nascimento, Complemento, Imagem, "Última Troca de Senha",
                                "Data da Senha Cadastrada", "Data da Inclusão do Usuário", "Usuário Logado") 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (nome, usuario, senha, confirmar_senha, acesso, endereco, cep, cpf, numero, estado, email, telefone, 
                rg, data_nascimento, complemento, imagem, "Não Cadastrado", data_atual, data_atual, usuario_logado))


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
    def atualizar_usuario(self, nome=None, usuario=None, senha=None, confirmar_senha=None, acesso=None, endereco=None, 
                      cep=None, cpf=None, numero=None, estado=None, email=None, 
                      telefone=None, rg=None, data_nascimento=None, complemento=None, imagem=None):
        try:
            # Monta a query SQL dinamicamente com base nos parâmetros fornecidos
            columns_to_update = []
            values_to_update = []

            if nome is not None:
                columns_to_update.append("Nome = ?")
                values_to_update.append(nome if nome else "Não cadastrado")
            if usuario is not None:
                columns_to_update.append("Usuário = ?")
                values_to_update.append(usuario if usuario else "Não cadastrado")
            if senha is not None:
                columns_to_update.append("Senha = ?")
                values_to_update.append(senha if senha else "Não cadastrado")
            if confirmar_senha is not None:
                columns_to_update.append("Confirmar Senha = ?")
                values_to_update.append(confirmar_senha if confirmar_senha else "Não cadastrado")
            if acesso is not None:
                columns_to_update.append("Acesso = ?")
                values_to_update.append(acesso if acesso else "Não cadastrado")
            if endereco is not None:
                columns_to_update.append("Endereço = ?")
                values_to_update.append(endereco if endereco else "Não cadastrado")
            if cep is not None:
                columns_to_update.append("CEP = ?")
                values_to_update.append(cep if cep else "Não cadastrado")
            if cpf is not None:
                columns_to_update.append("CPF = ?")
                values_to_update.append(cpf if cpf else "Não cadastrado")
            if numero is not None:
                columns_to_update.append("Número = ?")
                values_to_update.append(numero if numero else "Não cadastrado")
            if estado is not None:
                columns_to_update.append("Estado = ?")
                values_to_update.append(estado if estado else "Não cadastrado")
            if email is not None:
                columns_to_update.append("Email = ?")
                values_to_update.append(email if email else "Não cadastrado")
            if telefone is not None:
                columns_to_update.append("Telefone = ?")
                values_to_update.append(telefone if telefone else "Não cadastrado")
            if rg is not None:
                columns_to_update.append("RG = ?")
                values_to_update.append(rg if rg else "Não cadastrado")
            if data_nascimento is not None:
                columns_to_update.append("Data_nascimento = ?")
                values_to_update.append(data_nascimento if data_nascimento else "Não cadastrado")
            if complemento is not None:
                columns_to_update.append("Complemento = ?")
                values_to_update.append(complemento if complemento else "Não cadastrado")
            if imagem is not None:
                columns_to_update.append("Imagem = ?")
                values_to_update.append(imagem if imagem else "Não cadastrado")

            # Converte as listas em strings separadas por vírgula
            set_clause = ", ".join(columns_to_update)

            query = f"""
                UPDATE users
                SET {set_clause}
                WHERE id = ?
            """

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
            SELECT Produto, Quantidade, Valor_Real, Desconto, Data_Compra, Código_Item, Cliente, Descrição_Produto, Imagem, Status, 'Status da Saída' 
            FROM products
        """)
        produtos = cursor.fetchall()
        return produtos

    def obter_produtos_saida(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT Produto, Quantidade, "Valor do Produto", Desconto, "Data de Saída", "Data da Criação", "Código do Produto", Cliente, "Descrição do Produto", Usuário, Imagem 
            FROM products_saida
        """)
        produtos = cursor.fetchall()
        return produtos

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
        

if __name__ == "__main__":
    db = DataBase()
    db.connecta()
    db.close_connection()
    
    