#Parâmetros da conexão
from postgres import conectar_db
from model import Pessoa, PessoaAtualizada


def adicionar_cadastro(pessoa: Pessoa):
        try:
            db = conectar_db()
            query = f"INSERT INTO cadastros (idpessoa, nome, cpf, celular, endereco) VALUES ({pessoa.id}, '{pessoa.nome}', '{pessoa.cpf}', '{pessoa.celular}','{pessoa.endereco}');"
            db.execute(query) #método para executar ação no banco de dados
            db.connection.commit() #método para comitar as informaçãos com cenexão com o banco de dados
        
        except Exception as error :
            db.connection.rollback() #método que retorna o banco de dados a algum estado anterior
            raise Exception(f"Não foi possível cadastrar, verifique o preenchimento.{error}")
        
        finally:
             db.close()


def buscar_cadastro():
        try:
            db = conectar_db()
            query = "SELECT * FROM cadastros" #query(consulta do banco SQL)      
            db.execute(query)
            resultado = db.fetchall() #método para realizar a consulta e recuperar os resultados do banco SQL
            return resultado
        
        except Exception as error:
            raise ConnectionError(f"Erro na tentativa de consulta ao banco. {error}")
        
        finally:
            db.close()
        
            
def atualizar_cadastro(pessoa: PessoaAtualizada, id: int):
        try:
            db = conectar_db()
            query = f"UPDATE cadastros SET nome='{pessoa.nome}', cpf='{pessoa.cpf}', celular='{pessoa.celular}', endereco='{pessoa.endereco}' WHERE idpessoa={id};"
            db.execute(query)
            db.connection.commit()
        
        except Exception as error:
            db.connection.rollback()
            raise ValueError(f'Não foi possível atualizar o dado.')
        
        finally:
            db.close()


def atualizar_parcial_cadastro(pessoa: PessoaAtualizada, id: int):
        try:
            db = conectar_db()
            db.execute(f"SELECT * FROM cadastros WHERE idpessoa={id};")
            dado_antigo = db.fetchall()

            nome = pessoa.nome if pessoa.nome else dado_antigo[0][1]
            cpf = pessoa.cpf if pessoa.cpf else dado_antigo[0][2]
            celular = pessoa.celular if pessoa.celular else dado_antigo[0][3]
            endereco = pessoa.endereco if pessoa.endereco else dado_antigo[0][4]

            db.execute(f"UPDATE cadastros SET nome='{nome}', cpf='{cpf}', celular='{celular}', endereco='{endereco}' WHERE idpessoa={id};")
            db.connection.commit()
        
        except Exception as error:
            db.connection.rollback()
            raise ValueError(f'Não foi possível atualizar o dado.')
        
        finally:
            db.close()

        
def deletar_cadastro(id: int):
        try:
            db = conectar_db()
            query = f'DELETE FROM cadastros WHERE idpessoa={id};'
            db.execute(query)
            db.connection.commit()
        
        except Exception as error:
            db.connection.rollback()
            raise ValueError(f'Erro na operação deletar.')
        
        finally:
            db.close()
