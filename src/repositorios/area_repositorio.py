from config.db.db_config import pegar_conexao
from config.logs.log_config import registrar_log

"""
pegar:
    Recupera todas as áreas cadastradas no banco de dados.
Returns:
    list: Lista de tuplas contendo os dados de todas as áreas
            (id, nome, localizacao, hectar)
Raises:
    Exception: Se houver erro na consulta ao banco de dados
"""
def pegar() -> list:
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM area')
        areas = cursor.fetchall()
        return areas
    except Exception as e:
        message_error = f"Erro ao buscar áreas: {str(e)}"
        registrar_log("area_repositorio", "pegar", "Erro", message_error)
        raise Exception(message_error)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()

"""
pegar_por_id:
    Recupera uma área específica pelo seu ID.
Args:
    id (int): ID da área a ser buscada
Returns:
    tuple: Tupla contendo os dados da área (id, nome, localizacao, hectar)
            ou None se não encontrada
Raises:
    Exception: Se houver erro na consulta ao banco de dados
"""
def pegar_por_id(id: int) -> tuple:
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM area WHERE id = :1', [id])
        area = cursor.fetchone()
        return area
    except Exception as e:
        message_error = f"Erro ao buscar área por ID: {str(e)}"
        registrar_log("area_repositorio", "pegar_por_id", "Erro", message_error)
        raise Exception(message_error)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()

"""
criar:
    Cria uma nova área no banco de dados.
Args:
    nome (str): Nome da área
    localizacao (str): Localização da área
    hectar (float): Tamanho da área em hectares
Returns:
    int: ID da área criada
Raises:
    Exception: Se houver erro na criação da área
"""
def criar(nome: str, localizacao: str, hectar: float) -> int:
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        id_var = cursor.var(int)
        cursor.execute(
            'INSERT INTO area (nome, localizacao, hectar) VALUES (:1, :2, :3) RETURNING id INTO :4',
            [nome, localizacao, hectar, id_var]
        )
        conexao.commit()
        registrar_log("area_repositorio", "criar", "Sucesso", f"Área criada com sucesso - id: {str(id_var.getvalue()[0])}, nome: {str(nome)}, localização: {str(localizacao)}, hectares: {str(hectar)}")
        return id_var.getvalue()[0]
    except Exception as e:
        message_error = f"Erro ao criar área: {str(e)}"
        registrar_log("area_repositorio", "criar", "Erro", message_error)
        raise Exception(message_error)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()

"""
atualizar_por_id:
    Atualiza os dados de uma área existente.
Args:
    id (int): ID da área a ser atualizada
    nome (str): Novo nome da área
    localizacao (str): Nova localização da área
    hectar (float): Novo tamanho da área em hectares
Returns:
    bool: True se a área foi atualizada com sucesso, False caso contrário
Raises:
    Exception: Se houver erro na atualização da área
"""
def atualizar_por_id(id: int, nome: str, localizacao: str, hectar: float) -> bool:
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        cursor.execute(
            'UPDATE area SET nome = :1, localizacao = :2, hectar = :3 WHERE id = :4',
            [nome, localizacao, hectar, id]
        )
        conexao.commit()
        registrar_log("area_repositorio", "atualizar_por_id", "Sucesso", f"Área atualizada com sucesso - id: {str(id)}, nome: {str(nome)}, localização: {str(localizacao)}, hectares: {str(hectar)}")
        return cursor.rowcount > 0
    except Exception as e:
        message_error = f"Erro ao atualizar área: {str(e)}"
        registrar_log("area_repositorio", "atualizar_por_id", "Erro", message_error)
        raise Exception(message_error)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()

"""
deletar_por_id:
    Remove uma área do banco de dados.
Args:
    id (int): ID da área a ser removida
Returns:
    bool: True se a área foi removida com sucesso, False caso contrário
Raises:
    Exception: Se houver erro na remoção da área
"""
def deletar_por_id(id: int) -> bool:
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        cursor.execute('DELETE FROM area WHERE id = :1', [id])
        conexao.commit()
        registrar_log("area_repositorio", "deletar_por_id", "Sucesso", f"Área deletada com sucesso - id: {str(id)}")
        return cursor.rowcount > 0
    except Exception as e:
        message_error = f"Erro ao deletar área: {str(e)}"
        registrar_log("area_repositorio", "deletar_por_id", "Erro", message_error)
        raise Exception(message_error)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()