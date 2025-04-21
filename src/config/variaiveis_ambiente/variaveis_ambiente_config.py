import json
import os

"""
pegar_variaveis_ambiente:
    Carrega as variáveis de ambiente do arquivo JSON.
Returns:
    dict: Dicionário contendo as variáveis de ambiente carregadas do arquivo JSON.
Raises:
    FileNotFoundError: Se o arquivo variaveis_ambiente.json não for encontrado.
    json.JSONDecodeError: Se o arquivo JSON estiver mal formatado.
"""
def pegar_variaveis_ambiente():
    diretorio_atual = os.path.dirname(__file__)
    json_path = os.path.join(diretorio_atual, "variaveis_ambiente.json")
    with open(json_path, "r") as file:
        variaveis_ambiente = file.read()
        return json.loads(variaveis_ambiente)
    
"""
pegar_oracle_db_usuario:
    Obtém o nome de usuário do banco de dados Oracle.
Returns:
    str: Nome de usuário para conexão com o banco Oracle.
Raises:
    KeyError: Se a chave 'oracle_db_usuario' não existir no arquivo de configuração.
"""
def pegar_oracle_db_usuario():
    pegar_variaveis = pegar_variaveis_ambiente()
    return pegar_variaveis['oracle_db_usuario']

"""
pegar_oracle_db_senha:
    Obtém a senha do banco de dados Oracle.
Returns:
    str: Senha para conexão com o banco Oracle.
Raises:
    KeyError: Se a chave 'oracle_db_senha' não existir no arquivo de configuração.
"""
def pegar_oracle_db_senha():
    pegar_variaveis = pegar_variaveis_ambiente()
    return pegar_variaveis['oracle_db_senha']
