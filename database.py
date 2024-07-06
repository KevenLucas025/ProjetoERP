import sqlite3
from datetime import datetime

class DataBase:
    def __init__(self, name="banco_de_dados.db"):
        self.name = name
        self.connection = None
#*********************************************************************************************************************   
    def connecta(self):
        try:
            self.connection = sqlite3.connect(self.name)
            return self.connection
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {str(e)}")
            return None

#*********************************************************************************************************************   
    def close_connection(self):
        try:
            if self.connection:  # Verificar se a conexão existe antes de fechar
                self.connection.close()
        except Exception as e:
            print("Erro ao fechar conexão:", e)

#*********************************************************************************************************************    
    def create_table_users(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
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
                    "Data da Inclusão do Usuário" TEXT         
                    
                )
            """)
            print("Tabela de usuários criada com sucesso!")
        except Exception as e:
            print("Erro ao criar tabela de usuários:", e)

#*********************************************************************************************************************
    def create_table_products(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS products(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    Produto TEXT NOT NULL,
                    Quantidade INTEGER NOT NULL,
                    Valor_Real REAL NOT NULL,
                    Valor_Unidade REAL NOT NULL,
                    Desconto REAL,
                    Data_Compra TEXT,
                    Código_Item TEXT,
                    Cliente TEXT,
                    Descrição_Produto TEXT,
                    Imagem BLOB           
                )
            """)
            print("Tabela de produtos criada com sucesso!")
        except Exception as e:
            print("Erro ao criar tabela de produtos:", e)
#*********************************************************************************************************************

    def insert_product(self, produto, quantidade, valor_real, valor_unidade, desconto, data_compra, 
                       codigo_item, cliente, descricao_produto, imagem=None):
        try:
            cursor = self.connection.cursor()

            if produto is None:
                produto = "Não Cadastrado"
            if quantidade is None:
                quantidade = "Não Cadastrado"
            if valor_real is None:
                valor_real = "Não Cadastrado"
            if valor_unidade is None:
                valor_unidade = "Não Cadastrado"
            if desconto is None:
                desconto = "Não Cadastrado"
            if data_compra is None:
                data_compra = "Não Cadastrado"
            if codigo_item is None:
                codigo_item = "Não Cadastrado"
            if cliente is None:
                cliente = "Não Cadastrado"
            if descricao_produto is None:
                descricao_produto = "Não Cadastrado"
            if imagem is None:
                imagem = "Não Cadastrado"


            cursor.execute("""
                INSERT INTO products(Produto, Quantidade, Valor_Real, Valor_Unidade, Desconto, Data_Compra, Código_Item, 
                           Cliente,Imagem) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?,?)
            """, (produto, quantidade, valor_real, valor_unidade, desconto, data_compra, codigo_item, 
                  cliente,descricao_produto, imagem))
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
            print("Verificando usuário e senha no banco de dados...")
            print("Usuário fornecido:", usuario)
            print("Senha fornecida:", senha)
            
            query = "SELECT Acesso FROM users WHERE Usuário = ? AND Senha = ? COLLATE NOCASE"  # Comparação insensível a maiúsculas e minúsculas
            cursor = self.connection.cursor()
            cursor.execute(query, (usuario, senha))
            result = cursor.fetchone()
            print("Resultado da consulta:", result)
            if result:
                print("Usuário autenticado com sucesso")
                return result[0]  # Retorna o tipo de usuário
            else:
                return ""  # Retorna uma string vazia se as credenciais não corresponderem
        except Exception as e:
            print("Erro ao verificar usuário:", e)
            return ""
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
                        valor_real=None, valor_unidade=None, desconto=None, 
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
            if valor_unidade is not None:
                columns_to_update.append("Valor_Unidade = ?")
                values_to_update.append(valor_unidade)
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
    def obter_caminho_imagem(self, produto_id):
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
    def user_exists(self, CPF, Usuário):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT 1 FROM users WHERE CPF = ?", (CPF,))
            cpf_result = cursor.fetchone()
            
            cursor.execute("SELECT 1 FROM users WHERE Usuário = ?", (Usuário,))
            user_result = cursor.fetchone()
            
            if cpf_result:
                return 'cpf'  # Retorna 'cpf' se o CPF já estiver cadastrado
            elif user_result:
                return 'Usuário'  # Retorna 'user' se o nome de usuário já estiver cadastrado
            else:
                return None  # Retorna None se o usuário não existir
        except Exception as e:
            print("Erro ao verificar se usuário existe:", e)
            return None
#*********************************************************************************************************************
    def insert_user(self, nome, usuario, senha, confirmar_senha, acesso, endereco, cep, cpf, numero, estado, email, 
                    telefone, rg, data_nascimento, complemento, imagem=None):
        try:
            cursor = self.connection.cursor()

            # Definindo a data atual como a data de última troca de senha
            data_atual = datetime.now().strftime("%d/%m/%Y")

            # Substituir None ou valores vazios por "Não Cadastrado"
            if nome is None:
                nome = "Não Cadastrado"
            if usuario is None:
                usuario = "Não Cadastrado"
            if senha is None:
                senha = "Não Cadastrado"
            if confirmar_senha is None:
                confirmar_senha = "Não Cadastrado"
            if acesso is None:
                acesso = "Não Cadastrado"
            if endereco is None:
                endereco = "Não Cadastrado"
            if cep is None:
                cep = "Não Cadastrado"
            if cpf is None:
                cpf = "Não Cadastrado"
            if numero is None:
                numero = "Não Cadastrado"
            if estado is None:
                estado = "Não Cadastrado"
            if email is None:
                email = "Não Cadastrado"
            if rg is None:
                rg = "Não Cadastrado"
            if complemento is None:
                complemento = "Não Cadastrado"
            if telefone is None:
                telefone = "Não Cadastrado"       
            if data_nascimento is None:
                data_nascimento = "Não Cadastrado"
            if imagem is None:
                imagem = "Não Cadastrado"
            
            

            # Insira o novo usuário com a data atual de última troca de senha
            cursor.execute("""
                INSERT INTO users(Nome, Usuário, Senha, "Confirmar Senha", Acesso, Endereço, CEP, CPF, Número, Estado, 
                                  Email, Telefone, RG, Data_nascimento, Complemento,Imagem,"Última Troca de Senha",
                           "Data da Senha Cadastrada","Data da Inclusão do Usuário") 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?,?)
            """, (nome, usuario, senha, confirmar_senha, acesso, endereco, cep, cpf, numero, estado, email, 
                  telefone, rg, data_nascimento, "Não Cadastrado",imagem,"Não Cadastrado",data_atual,data_atual))
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

if __name__ == "__main__":
    db = DataBase()
    db.connecta()
    db.create_table_users()
    db.close_connection()
    