import sqlite3
from datetime import datetime,timedelta
import os
import sys

class DataBase:
    def __init__(self, name="banco_de_dados.db"):
        self.name = name
        self.connection = None
        self.db_path = self.obter_caminho_banco()
        self.connecta()  # Tente conectar ao banco ao instanciar
        self.criar_tabelas()
        
        
    def criar_tabelas(self):
        self.garantir_conexao()
        self.create_table_users()
        self.create_table_users_inativos()
        self.create_table_products()
        self.create_table_products_saida()
        self.create_table_historico()
        self.create_table_historico_usuario()
        self.create_table_clientes_juridicos()
        self.create_table_clientes_fisicos()
        self.create_table_historico_fisico()
        self.create_table_historico_juridico()
        self.criar_tabela_master_nonces()
        self.connection.commit()

#*********************************************************************************************************************       
    def obter_caminho_banco(self):
        # Detecta se está rodando como um executável criado pelo PyInstaller
        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            # Caminho persistente e oculto no Windows
            appdata = os.getenv("APPDATA")
            pasta_dados = os.path.join(appdata, "SistemaGerenciamento")
        else:
            # Rodando no VSCode / Python normal → usa o caminho original
            pasta_dados = os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                "SistemaGerenciamento"
            )

        os.makedirs(pasta_dados, exist_ok=True)

        return os.path.join(pasta_dados, self.name)
#*********************************************************************************************************************
    def connecta(self):
        try:
            self.connection = sqlite3.connect(self.db_path)
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
            
    def garantir_conexao(self):
        try:
            if self.connection is None:
                self.connection = sqlite3.connect(self.db_path)
            else:
                self.connection.execute("SELECT 1")
        except:
            self.connection = sqlite3.connect(self.db_path)

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
                    "Imagem Original" TEXT,
                    "Imagem Usuário" TEXT,
                    "Última Troca de Senha" TEXT,
                    "Data da Senha Cadastrada" TEXT,
                    "Data da Inclusão do Usuário" TEXT,
                    Segredo TEXT,
                    "Usuário Logado" TEXT,
                    Acesso TEXT NOT NULL
                )
            """)
            self.connection.commit()
        except Exception as e:
            print("Erro ao criar tabela de usuários:", e)
#*********************************************************************************************************************
    def create_table_users_inativos(self):
         try:
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
                    "Imagem Original" TEXT,
                    'Última Troca de Senha' TEXT,
                    'Data da Senha Cadastrada' TEXT,
                    'Data da Inclusão do Usuário' TEXT,
                    'Data da Inatividade do Usuário' TEXT,
                    Segredo TEXT,
                    'Usuário Logado' TEXT NOT NULL,
                    Acesso TEXT NOT NULL
                                    
                )
            """)
            self.connection.commit()
         except Exception as e:
             print("Erro ao criar a tabela users_inativos", e)

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
                    "Valor Unitário" REAL NOT NULL,
                    Desconto TEXT,
                    "Total Sem Desconto",
                    "Total Com Desconto" TEXT,
                    "Data do Cadastro" TEXT,
                    Código_Item TEXT,
                    Cliente TEXT,
                    Descrição_Produto TEXT,
                    Usuário TEXT,
                    "Status da Saída" TEXT,
                    Imagem TEXT,
                    CNPJ TEXT,
                    CPF TEXT
                )
            """)
            self.connection.commit()  # Confirmar a transação
        except Exception as e:
            print("Erro ao criar tabela de produtos:", e)
#*********************************************************************************************************************
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
                    "Valor Unitário"  NOT NULL,
                    Desconto,
                    "Total Sem Desconto", 
                    "Total Com Desconto" TEXT,
                    "Data de Saída" TEXT,
                    "Data da Criação" TEXT,
                    "Código do Produto" TEXT,
                    Cliente TEXT,
                    "Descrição do Produto",
                    Usuário TEXT,
                    'Status da Saída' TEXT,
                    Imagem TEXT
                )
            """)
            self.connection.commit()  # Confirmar a transação
        except Exception as e:
            print("Erro ao criar tabela de produtos:", e)
#*********************************************************************************************************************
    def create_table_historico(self):
        try:
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
        except Exception as e:
            print("Erro ao criar tabela de histórico: ", e)
#*********************************************************************************************************************            
    def create_table_historico_usuario(self):
        try:
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
        except Exception as e:
            print("Erro ao criar tabela de historico_usuarios: ", e)
#*********************************************************************************************************************
    def create_table_clientes_juridicos(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS clientes_juridicos(
                    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    "Nome do Cliente" TEXT,
                    "Razão Social" TEXT,
                    "Data da Inclusão" TEXT,
                    CNPJ TEXT,
                    RG TEXT,
                    CPF TEXT,
                    Email TEXT,
                    CNH TEXT,
                    "Categoria da CNH" TEXT,
                    "Data de Emissão da CNH" TEXT,
                    "Data de Vencimento da CNH" TEXT,
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
                    "Valor Gasto Total" TEXT,
                    "Modo Valor Gasto" TEXT,
                    "Última Compra" TEXT  
                    )
                """)
            self.connection.commit()
        except Exception as e:
            print("Erro ao criar tabela de clientes_juridicos: ", e)
#*********************************************************************************************************************
    def create_table_clientes_fisicos(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS clientes_fisicos(
                    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    "Nome do Cliente" TEXT,
                    "Data da Inclusão" TEXT,
                    RG TEXT,
                    CPF TEXT,
                    Email TEXT,
                    CNH TEXT,
                    "Categoria da CNH" TEXT,
                    "Data de Emissão da CNH" TEXT,
                    "Data de Vencimento da CNH" TEXT,
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
                    "Valor Gasto Total" TEXT,
                    "Modo Valor Gasto" TEXT,
                    "Última Compra" TEXT  
                    )
                """)
            self.connection.commit()
        except Exception as e:
            print("Erro ao criar tabela de clientes_fisicos: ", e)
            
    def create_table_historico_juridico(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS historico_clientes_juridicos(
                    'Data e Hora' TEXT,
                    Usuário TEXT,
                    Ação TEXT,
                    Descrição TEXT                                   
                )           
            """)
            self.connection.commit()
        except Exception as e:
            print("Erro ao criar tabela de historico_clientes_juridicos: ", e)

    def create_table_historico_fisico(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS historico_clientes_fisicos(
                    'Data e Hora' TEXT,
                    Usuário TEXT,
                    Ação TEXT,
                    Descrição TEXT                                   
                )           
            """)
            self.connection.commit()
        except Exception as e:
            print("Erro ao criar tabela de historico_clientes_fisicos: ", e)
#*********************************************************************************************************************
    def insert_product(self, produto, quantidade, valor_unitario, desconto,total_sem_desconto,total_com_desconto, data_cadastro, 
                    codigo_item, cliente, descricao_produto, usuario,cnpj,cpf, imagem=None):
        try:
            cursor = self.connection.cursor()

            # Substitua valores nulos por valores padrão
            produto = produto if produto is not None else "Não Cadastrado"
            quantidade = quantidade if quantidade is not None else 0
            valor_unitario = valor_unitario if valor_unitario is not None else 0.0
            desconto = desconto if desconto is not None else "Sem desconto"
            total_sem_desconto = total_sem_desconto if total_sem_desconto is not None else "Não Cadastrado"
            total_com_desconto = total_com_desconto if total_com_desconto is not None else "Não Cadastrado"
            data_cadastro = data_cadastro if data_cadastro is not None else "Não Cadastrado"
            codigo_item = codigo_item if codigo_item is not None else "Não Cadastrado"
            cliente = cliente if cliente is not None else "Não Cadastrado"
            descricao_produto = descricao_produto if descricao_produto is not None else "Não Cadastrado"
            usuario = usuario if usuario is not None else "Não Cadastrado"
            imagem = imagem if imagem is not None else "Não Cadastrado"
            cnpj = cnpj if cnpj is not None else "Não Cadastrado"
            cpf = cpf if cpf is not None else "Não Cadastrado"

            cursor.execute("""
                INSERT INTO products (
                    Produto, Quantidade, "Valor Unitário", Desconto, "Total Sem Desconto","Total Com Desconto",
                    "Data do Cadastro", Código_Item, Cliente, Descrição_Produto,
                    "Status da Saída", Imagem, Usuário, CNPJ, CPF
                ) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)
            """, (
                produto, quantidade, valor_unitario, desconto,total_sem_desconto, total_com_desconto,
                data_cadastro, codigo_item, cliente, descricao_produto,
                0, imagem, usuario, cnpj, cpf
            ))
            self.connection.commit()
            print("Produto inserido com sucesso!")
        except Exception as e:
            print("Erro ao inserir produto:", e)
#*********************************************************************************************************************
    def check_user(self, usuario_email_cpf, senha):
        try:
            query = """
                SELECT "Usuário"
                FROM users
                WHERE (Usuário = ? OR Email = ? OR CPF = ? ) 
                AND Senha = ? COLLATE NOCASE
            """
            cursor = self.connection.cursor()  # Usar a conexão já existente
            cursor.execute(query, (usuario_email_cpf,usuario_email_cpf,usuario_email_cpf, senha))
            result = cursor.fetchone()
            return result[0] if result else None
        except Exception as e:
            print(f"Erro ao verificar usuário: {e}")
            return False  
#*********************************************************************************************************************
    def get_products(self):
        try:
            self.garantir_conexao()
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM products")
            return cursor.fetchall()
        except Exception as e:
            print("Erro ao obter produtos:", e)
            return []

#*********************************************************************************************************************        
    def get_users(self):
        try:
            self.garantir_conexao()
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
            self.garantir_conexao()
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM products WHERE id = ?", (produto_id,))
            self.connection.commit()
            print("Produto removido com sucesso!")
        except Exception as e:
            print("Erro ao apagar produto do banco de dados:", e)
#*********************************************************************************************************************
    def remover_usuario(self, id_usuario):
        try:
            self.garantir_conexao()
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM users WHERE id = ?", (id_usuario,))
            self.connection.commit()
            print("Usuário removido com sucesso!")
        except Exception as e:
            print("Erro ao apagar usuário do banco de dados:", e)
#*********************************************************************************************************************            
    def atualizar_valor_gasto_cliente(self, nome_cliente):
        cursor = self.connection.cursor()

        # Soma todos os valores finais dos produtos do cliente
        cursor.execute("""
            SELECT SUM(
                REPLACE(
                    REPLACE(
                        REPLACE("Total Sem Desconto", 'R$', ''),
                    '.', ''),
                ',', '.')
            )
            FROM products
            WHERE Cliente = ?
        """, (nome_cliente,))

        total = cursor.fetchone()[0] or 0

        cursor.execute("""
            UPDATE clientes_juridicos
            SET 
                "Valor Gasto Total" = ?,
                "Modo Valor Gasto" = 'automatico',
                "Última Compra" = ?
            WHERE "Nome do Cliente" = ?
        """, (
            f"R$ {total:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
            datetime.now().strftime("%d/%m/%Y %H:%M"),
            nome_cliente
        ))

        self.connection.commit()
#*********************************************************************************************************************       
    def atualizar_valor_gasto_cliente_fisico(self, nome_cliente):
            cursor = self.connection.cursor()

            # Soma todos os valores finais dos produtos do cliente
            cursor.execute("""
                SELECT SUM(
                    REPLACE(
                        REPLACE(
                            REPLACE("Total Com Desconto", 'R$', ''),
                        '.', ''),
                    ',', '.')
                )
                FROM products
                WHERE Cliente = ?
            """, (nome_cliente,))

            total = cursor.fetchone()[0] or 0

            cursor.execute("""
                UPDATE clientes_fisicos
                SET 
                    "Valor Gasto Total" = ?,
                    "Modo Valor Gasto" = 'automatico',
                    "Última Compra" = ?
                WHERE "Nome do Cliente" = ?
            """, (
                f"R$ {total:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
                datetime.now().strftime("%d/%m/%Y %H:%M"),
                nome_cliente
            ))

            self.connection.commit()
#*********************************************************************************************************************
    def atualizar_produto(
        self, produto_id, produto=None, quantidade=None, 
        valor_unitario=None, desconto=None,total_sem_desconto=None, total_com_desconto=None,
        data_cadastro=None, codigo_item=None, cliente=None,
        descricao_produto=None, produto_imagem=None
    ):
        try:
            columns_to_update = []
            values_to_update = []

            if produto:
                columns_to_update.append("Produto = ?")
                values_to_update.append(produto)

            if quantidade is not None:
                columns_to_update.append("Quantidade = ?")
                values_to_update.append(quantidade)

            if valor_unitario is not None:
                columns_to_update.append('"Valor Unitário" = ?')
                values_to_update.append(valor_unitario)

            # Desconto
            columns_to_update.append("Desconto = ?")
            values_to_update.append(desconto if desconto else "Não Cadastrado")
            
            columns_to_update.append('"Total Sem Desconto" = ?')
            values_to_update.append(total_sem_desconto if total_sem_desconto else "Não Cadastrado")

            # Total Com Desconto (COLUNA COM ESPAÇO)
            columns_to_update.append('"Total Com Desconto" = ?')
            values_to_update.append(total_com_desconto if total_com_desconto else "Não Cadastrado")

            # Data do Cadastro (COLUNA COM ESPAÇO)
            columns_to_update.append('"Data do Cadastro" = ?')
            values_to_update.append(data_cadastro if data_cadastro else "Não Cadastrado")

            # Código do Item
            columns_to_update.append("Código_Item = ?")
            values_to_update.append(codigo_item if codigo_item else "Não Cadastrado")

            # Cliente
            columns_to_update.append("Cliente = ?")
            values_to_update.append(cliente if cliente else "Não Cadastrado")

            # Descrição do Produto
            columns_to_update.append("Descrição_Produto = ?")
            values_to_update.append(descricao_produto if descricao_produto else "Não Cadastrado")

            # Imagem (CORRIGIDO)
            columns_to_update.append("Imagem = ?")
            values_to_update.append(produto_imagem if produto_imagem else "Não Cadastrado")

            set_clause = ", ".join(columns_to_update)

            query = f"""
                UPDATE products
                SET {set_clause}
                WHERE id = ?
            """

            values_to_update.append(produto_id)

            cursor = self.connection.cursor()
            cursor.execute(query, tuple(values_to_update))
            self.connection.commit()

            print("Produto atualizado com sucesso!")

        except Exception as e:
            print("Erro ao atualizar produto:", e)
#*********************************************************************************************************************        
    def user_exists(self, Usuario, Telefone, Email, RG, CPF,CNPJ):
        try:
            self.garantir_conexao()
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
        
    def resolver_campo_alvo(self, alvo: str) -> str | None:
        a = (alvo or "").strip()
        if not a:
            return None

        # Reaproveita seu método, passando o alvo no parâmetro certo
        tipo = self.user_exists(
            Usuario=a,
            Telefone=a,
            Email=a,
            RG=a,
            CPF=a,
            CNPJ=a
        )
        return tipo
#*********************************************************************************************************************
    def insert_user(self, nome, usuario, senha, confirmar_senha, cep, endereco, numero, cidade, bairro, estado,
                complemento, telefone, email, data_nascimento, rg, cpf, cnpj, segredo, usuario_logado, acesso, imagem=None):
        try:
            self.garantir_conexao()
            cursor = self.connection.cursor()
            data_atual = datetime.now().strftime("%d/%m/%Y %H:%M")

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
            imagem = imagem.strip() if isinstance(imagem, str) else "Não Cadastrado"
            segredo = tratar(segredo)
            usuario_logado = tratar(usuario_logado)
            acesso = tratar(acesso)

            cursor.execute("""
                INSERT INTO users(Nome, Usuário, Senha, "Confirmar Senha", CEP, Endereço, Número, Cidade, Bairro, Estado, Complemento,
                                Telefone, Email, "Data de Nascimento", RG, CPF, CNPJ, "Imagem Original", "Última Troca de Senha",
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
            
    def obter_email_usuario(self, usuario_email_cpf):
        cursor = self.connection.cursor()
        cursor.execute(
            'SELECT Email FROM users WHERE "Usuário" = ? OR Email = ? OR CPF = ?',
            (usuario_email_cpf, usuario_email_cpf,usuario_email_cpf)
        )
        row = cursor.fetchone()
        return row[0] if row else None


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
            self.garantir_conexao()
            cursor.execute("UPDATE users SET Senha = ?, \"Última Troca de Senha\" = ? WHERE id = ?", 
                        (nova_senha, datetime.now().strftime("%d/%m/%Y"), id_usuario))
            self.connection.commit()
            return True
        return False
#*********************************************************************************************************************
    def atualizar_data_ultima_troca(self, id_usuario):
        data_atual = datetime.now().strftime("%d/%m/%Y ")
        cursor = self.connection.cursor()
        self.garantir_conexao()
        cursor.execute("UPDATE users SET \"Última Troca de Senha\" = ? WHERE id = ?", (data_atual, id_usuario))
        self.connection.commit()
#*********************************************************************************************************************
        
    def ultima_troca(self, usuario):
        try:
            self.garantir_conexao()
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
        self.garantir_conexao()
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
            self.garantir_conexao()
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Erro ao executar a consulta: {str(e)}")
            return None
#*********************************************************************************************************************        
    def salvar_imagem_usuario(self, usuario, caminho_imagem):
        cursor = self.connection.cursor()
        cursor.execute("""
            UPDATE users
            SET "Imagem Usuário" = ?
            WHERE "Usuário" = ?
        """, (caminho_imagem, usuario))
        self.connection.commit()
#*********************************************************************************************************************        
    def obter_imagem_usuario(self, usuario):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT "Imagem Usuário" FROM users WHERE "Usuário" = ?
        """, (usuario,))
        row = cursor.fetchone()
        return row[0] if row and row[0] else None
#*********************************************************************************************************************
    def obter_produtos_base(self):
        self.garantir_conexao()
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT Produto, Quantidade, "Valor Unitário", Desconto,"Total Sem Desconto","Total Com Desconto", "Data do Cadastro", Código_Item, Cliente, 
                       Descrição_Produto, Imagem, 'Status da Saída' 
            FROM products
        """)
        produtos = cursor.fetchall()
        return produtos
#*********************************************************************************************************************
    def obter_produtos_saida(self):
        self.garantir_conexao()
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT Produto, Quantidade, "Valor Unitário", Desconto,"Total Sem Desconto", "Total Com Desconto","Data de Saída", "Data da Criação", "Código do Produto", 
                       Cliente, "Descrição do Produto", Usuário, "Status da Saída",Imagem 
            FROM products_saida
        """)
        produtos = cursor.fetchall()
        return produtos
#********************************************************************************************************************* 
    def obter_usuarios_ativos(self):
        self.garantir_conexao()
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
        self.garantir_conexao()
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT Nome,Usuário,Senha,"Confirmar Senha",CEP,Endereço,Número,Cidade,Bairro,Estado,Complemento,Telefone,Email,
                       "Data de Nascimento",RG,CPF,CNPJ,"Última Troca de Senha","Data da Senha Cadastrada",
                       "Data da Inclusão do Usuário","Data da Inatividade do Usuário",Segredo,"Usuário Logado",Acesso
            FROM users_inativos
        """)
        usuarios = cursor.fetchall()
        return usuarios

    def salvar_usuario_logado(self, usuario_logado):
        try:
            self.garantir_conexao()
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
                (Produto, Quantidade, "Valor Unitário", Desconto,"Total Sem Desconto","Total Com Desconto", "Data de Saída", 
                "Data da Criação", "Código do Produto", Cliente, "Descrição do Produto", Usuário, Imagem,"Status da Saída")
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)
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
            self.garantir_conexao()
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print("Erro ao obter usuários:", e)
            return []
        finally:
            if cursor:
                cursor.close()
                
    def obter_nome_completo_usuario(self, usuario_login):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT Nome FROM users WHERE Usuário = ?
        """, (usuario_login,))
        resultado = cursor.fetchone()
        return resultado[0] if resultado else None


    def recuperar_usuario_por_id(self, id_usuario):
        self.garantir_conexao()
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT Nome, Usuário, Senha, "Confirmar Senha", CEP, Endereço, Número, Cidade, Bairro,
                Estado, Complemento, Telefone, Email, "Data de Nascimento", RG, CPF, CNPJ, Acesso
            FROM users
            WHERE id = ?
        """, (id_usuario,))
        return cursor.fetchone()
    
    def buscar_produto_por_id(self, produto_id):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT
                Produto, Quantidade, "Valor Unitário", Desconto,
                "Total Sem Desconto", "Total Com Desconto",
                "Data do Cadastro", Código_Item, Cliente,
                Descrição_Produto, Usuário, CNPJ, CPF, Imagem
            FROM products
            WHERE id = ?
        """, (produto_id,))

        row = cursor.fetchone()
        if not row:
            return None

        return {
            "produto": row[0],
            "quantidade": row[1],
            "valor_unitario": row[2],
            "desconto": row[3],
            "total_sem_desconto": row[4],
            "total_com_desconto": row[5],
            "data_cadastro": row[6],
            "codigo_item": row[7],
            "cliente": row[8],
            "descricao_produto": row[9],
            "usuario": row[10],
            "cnpj": row[11],
            "cpf": row[12],
            "imagem": row[13]
        }


    
    def obter_clientes_juridicos(self):
        self.garantir_conexao()
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT "Nome do Cliente", "Razão Social","Data da Inclusão", CNPJ,RG,CPF,Email,CNH,"Categoria da CNH","Data de Emissão da CNH",
                "Data de Vencimento da CNH",Telefone, CEP, Endereço, Número,Complemento,Cidade, Bairro,Estado, "Status do Cliente",
                "Categoria do Cliente", "Última Atualização","Valor Gasto Total", "Última Compra"
            FROM clientes_juridicos
        """)
        return cursor.fetchall()
    
    def obter_clientes_fisicos(self):
        self.garantir_conexao()
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT "Nome do Cliente","Data da Inclusão",RG,CPF,Email,CNH,"Categoria da CNH","Data de Emissão da CNH","Data de Vencimento da CNH",
                Telefone, CEP, Endereço, Número,Complemento,Cidade, Bairro,Estado, "Status do Cliente", "Categoria do Cliente", "Última Atualização", 
                "Valor Gasto Total", "Última Compra"
            FROM clientes_fisicos 
        """)
        return cursor.fetchall()
    

    def atualizar_primeiro_acesso(self, intervalo: timedelta = timedelta(days=1)) -> int:
        """
        Se "Usuário Logado" == 'Primeiro Acesso' e já passou `intervalo` desde
        "Data da Inclusão do Usuário", troca para 'Não Logado'.
        Retorna quantos foram atualizados.
        """
        try:
            self.garantir_conexao()
            cursor = self.connection.cursor()

            cursor.execute("""
                SELECT id, "Data da Inclusão do Usuário"
                FROM users
                WHERE "Usuário Logado" = 'Primeiro Acesso'
            """)
            rows = cursor.fetchall()

            if not rows:
                return 0

            agora = datetime.now()
            ids_para_atualizar = []

            for user_id, data_inclusao in rows:
                try:
                    dt = datetime.strptime(data_inclusao, "%d/%m/%Y %H:%M")
                except:
                    continue

                if agora - dt >= intervalo:
                    ids_para_atualizar.append(user_id)

            if not ids_para_atualizar:
                return 0

            placeholders = ",".join(["?"] * len(ids_para_atualizar))
            cursor.execute(f"""
                UPDATE users
                SET "Usuário Logado" = 'Não Logado'
                WHERE id IN ({placeholders})
                AND "Usuário Logado" = 'Primeiro Acesso'
            """, ids_para_atualizar)

            self.connection.commit()
            return cursor.rowcount

        except Exception as e:
            print(f"Erro ao atualizar Primeiro Acesso para Não Logado: {e}")
            return 0
        
    def obter_tipo_usuario(self, usuario_email_cpf: str) -> str | None:
        try:
            self.garantir_conexao()
            cursor = self.connection.cursor()

            cursor.execute("""
                SELECT TRIM(Acesso)
                FROM users
                WHERE TRIM("Usuário") = TRIM(?) COLLATE NOCASE
                OR TRIM(Email) = TRIM(?) COLLATE NOCASE
                OR TRIM(CPF) = TRIM(?) COLLATE NOCASE
                LIMIT 1
            """, (usuario_email_cpf, usuario_email_cpf, usuario_email_cpf))

            row = cursor.fetchone()


            return row[0] if row and row[0] else None

        except Exception as e:
            print("Erro ao obter tipo de usuário (Acesso):", e)
            return None

    def obter_acesso_usuario(self,usuario_alvo: str):
        self.garantir_conexao()
        
        tipo = self.resolver_campo_alvo(usuario_alvo)
        if not tipo:
            return None

        coluna_map = {
            "usuario": '"Usuário"',
            "telefone": "Telefone",
            "email": "Email",
            "rg": "RG",
            "cpf": "CPF",
            "cnpj": "CNPJ",
        }

        coluna = coluna_map.get(tipo)

        cursor = self.connection.cursor()
        cursor.execute(
            f'SELECT Acesso FROM users WHERE {coluna} = ?',
            (usuario_alvo,)
        )

        resultado = cursor.fetchone()

        if resultado:
            return resultado[0]

        return None

    def contar_primeiro_acesso_pendente(self, intervalo: timedelta = timedelta(days=1)) -> int:
        """
        Conta usuários que ainda estão com "Usuário Logado"='Primeiro Acesso' e:
        - já venceu o prazo (intervalo), OU
        - a data de inclusão está inválida/vazia (não dá pra calcular)
        Isso serve para avisar o usuário que precisa corrigir manualmente.
        """
        try:
            self.garantir_conexao()
            cursor = self.connection.cursor()

            cursor.execute("""
                SELECT "Data da Inclusão do Usuário"
                FROM users
                WHERE "Usuário Logado" = 'Primeiro Acesso'
            """)
            datas = cursor.fetchall()

            if not datas:
                return 0

            agora = datetime.now()
            pendentes = 0

            for (data_inclusao,) in datas:
                # data vazia/None => pendente (precisa intervenção)
                if not data_inclusao or not str(data_inclusao).strip():
                    pendentes += 1
                    continue

                try:
                    dt = datetime.strptime(data_inclusao, "%d/%m/%Y %H:%M")
                except:
                    # data inválida => pendente
                    pendentes += 1
                    continue

                if agora - dt >= intervalo:
                    pendentes += 1

            return pendentes

        except Exception as e:
            print(f"Erro ao contar Primeiro Acesso pendente: {e}")
            return 0
        
    def criar_tabela_master_nonces(self):
        cur = self.connection.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS master_nonces(
                nonce TEXT PRIMARY KEY,
                usado_em TEXT
            )
        """)
        self.connection.commit()

    def nonce_ja_usado(self, nonce: str) -> bool:
        cur = self.connection.cursor()
        cur.execute("SELECT 1 FROM master_nonces WHERE nonce = ? LIMIT 1", (nonce,))
        return cur.fetchone() is not None

    def registrar_nonce(self, nonce: str):
        cur = self.connection.cursor()
        cur.execute("INSERT OR IGNORE INTO master_nonces(nonce, usado_em) VALUES(?, datetime('now'))", (nonce,))
        self.connection.commit()

    def atualizar_acesso_usuario(self, usuario_alvo: str, novo_acesso: str):
        self.garantir_conexao()

        tipo = self.resolver_campo_alvo(usuario_alvo)

        if not tipo:
            return False

        coluna_map = {
            "usuario": '"Usuário"',
            "telefone": "Telefone",
            "email": "Email",
            "rg": "RG",
            "cpf": "CPF",
            "cnpj": "CNPJ"
        }

        coluna = coluna_map.get(tipo)

        cursor = self.connection.cursor()
        cursor.execute(
            f'UPDATE users SET Acesso = ? WHERE {coluna} = ?',
            (novo_acesso, usuario_alvo)
        )

        self.connection.commit()

        return cursor.rowcount > 0

if __name__ == "__main__":
    db = DataBase()
    db.close_connection()
    
    
    