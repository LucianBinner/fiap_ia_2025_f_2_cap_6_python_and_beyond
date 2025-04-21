import oracledb
from config.variaiveis_ambiente.variaveis_ambiente_config import pegar_oracle_db_usuario, pegar_oracle_db_senha

"""
pegar_conexao:
    Estabelece uma conexão com o banco de dados Oracle.
    Esta função cria e retorna uma conexão com o banco de dados Oracle usando as credenciais obtidas através das funções de ambiente.
Returns:
    oracledb.Connection: Objeto de conexão com o banco de dados Oracle
Raises:
    oracledb.Error: Se houver erro na conexão com o banco
    Exception: Se houver erro ao obter as credenciais de acesso
"""
def pegar_conexao():
    return oracledb.connect(
        user=pegar_oracle_db_usuario(),
        password=pegar_oracle_db_senha(),
        dsn="oracle.fiap.com.br:1521/ORCL"
    )
