from config.db.db_config import pegar_conexao
from config.logs.log_config import registrar_log

"""
pegar:
    Recupera todas as culturas cadastradas no banco de dados.
Returns:
    list: Lista de tuplas contendo os dados de todas as culturas
            (id, nome, consumo_hidrico_diario_l_m2)
Raises:
    Exception: Se houver erro na consulta ao banco de dados
"""
def pegar() -> list:
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM cultura')
        culturas = cursor.fetchall()
        return culturas
    except Exception as e:
        message_error = f"Erro ao buscar culturas: {str(e)}"
        registrar_log("cultura_repositorio", "pegar", "Erro", message_error)
        raise Exception(message_error)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()

"""
pegar_por_id:
    Recupera uma cultura específica pelo seu ID.
Args:
    id (int): ID da cultura a ser buscada
Returns:
    tuple: Tupla contendo os dados da cultura (id, nome, consumo_hidrico_diario_l_m2)
            ou None se não encontrada
Raises:
    Exception: Se houver erro na consulta ao banco de dados
"""
def pegar_por_id(id: int) -> tuple:
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM cultura WHERE id = :1', [id])
        cultura = cursor.fetchone()
        return cultura
    except Exception as e:
        message_error = f"Erro ao buscar cultura por ID: {str(e)}"
        registrar_log("cultura_repositorio", "pegar_por_id", "Erro", message_error)
        raise Exception(message_error)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()

"""
criar: 
    Cria uma nova cultura no banco de dados.
Args:
    nome (str): Nome da cultura
    consumo_hidrico_diario_l_m2 (float): Consumo hídrico diário em L/m²
Returns:
    int: ID da cultura criada
Raises:
    Exception: Se houver erro na criação da cultura
"""
def criar(nome: str, consumo_hidrico_diario_l_m2: float) -> int:
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        id_var = cursor.var(int)
        cursor.execute(
            'INSERT INTO cultura (nome, consumo_hidrico_diario_l_m2) VALUES (:1, :2) RETURNING id INTO :3',
            (nome, consumo_hidrico_diario_l_m2, id_var)
        )
        id = id_var.getvalue()
        conexao.commit()
        registrar_log("cultura_repositorio", "criar", "Sucesso", f"Cultura criada com sucesso - id: {str(id)}, nome: {str(nome)}, consumo_hidrico_diario_l_m2: {str(consumo_hidrico_diario_l_m2)}")
        return id
    except Exception as e:
        message_error = f"Erro ao criar cultura: {str(e)}"
        registrar_log("cultura_repositorio", "criar", "Erro", message_error)
        raise Exception(message_error)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()

"""
atualizar_por_id:
    Atualiza os dados de uma cultura existente.
Args:
    id (int): ID da cultura a ser atualizada
    nome (str): Novo nome da cultura
    consumo_hidrico_diario_l_m2 (float): Novo consumo hídrico diário em L/m²
Returns:
    bool: True se a cultura foi atualizada com sucesso, False caso contrário
Raises:
    Exception: Se houver erro na atualização da cultura
"""
def atualizar_por_id(id: int, nome: str, consumo_hidrico_diario_l_m2: float) -> bool:
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        cursor.execute(
            'UPDATE cultura SET nome = :1, consumo_hidrico_diario_l_m2 = :2 WHERE id = :3',
            (nome, consumo_hidrico_diario_l_m2, id)
        )
        conexao.commit()
        registrar_log("cultura_repositorio", "atualizar_por_id", "Sucesso", f"Cultura atualizada com sucesso - id: {str(id)}, nome: {str(nome)}, consumo_hidrico_diario_l_m2: {str(consumo_hidrico_diario_l_m2)}")
        return cursor.rowcount > 0
    except Exception as e:
        message_error = f"Erro ao atualizar cultura: {str(e)}"
        registrar_log("cultura_repositorio", "atualizar_por_id", "Erro", message_error)
        raise Exception(message_error)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()

"""
deletar_por_id:
    Remove uma cultura do banco de dados.
Args:
    id (int): ID da cultura a ser removida
Returns:
    bool: True se a cultura foi removida com sucesso, False caso contrário
Raises:
    Exception: Se houver erro na remoção da cultura
"""
def deletar_por_id(id: int) -> bool:
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        cursor.execute('DELETE FROM cultura WHERE id = :1', (id,))
        conexao.commit()
        registrar_log("cultura_repositorio", "deletar_por_id", "Sucesso", f"Cultura deletada com sucesso - id: {str(id)}")
        return cursor.rowcount > 0
    except Exception as e:
        message_error = f"Erro ao deletar cultura: {str(e)}"
        registrar_log("cultura_repositorio", "deletar_por_id", "Erro", message_error)
        raise Exception(message_error)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()