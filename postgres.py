#database da aplicação
import psycopg2 #biblioteca do database POstegreSQL
import os #módulo que busca a variável do sistema

host = os.getenv("POSTGRES_PORT")
port = os.getenv("POSTGRES_PORT")
database = os.getenv("POSTGRES_DATABASE")
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")


#Função para fazer a conexão da app com o banco de dados
def conectar_db():
    try:
        conexao = psycopg2.connect(port=port, database=database, user=user, password=password)
        cursor = conexao.cursor()
        print("Conexão com o banco com sucesso!")
        return cursor
    
    except Exception as error:
        raise ConnectionError("Conexão falhou, verifique os dados")
    

    
