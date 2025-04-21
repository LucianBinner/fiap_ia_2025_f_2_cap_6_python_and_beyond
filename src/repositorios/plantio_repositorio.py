from config.db.db_config import pegar_conexao
from config.logs.log_config import registrar_log

"""
pegar:
    Recupera todos os plantios cadastrados no banco de dados.
Returns:
    list: Lista de tuplas contendo os dados de todos os plantios
            (id, nome, observacao, area_id, area_nome, cultura_id, cultura_nome, data_plantio)
Raises:
    Exception: Se houver erro na consulta ao banco de dados
"""
def pegar() -> list:
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        cursor.execute('''
            SELECT p.id, p.nome, p.observacao, p.area_id, a.nome as area_nome, p.cultura_id, c.nome as cultura_nome, p.data_plantio
            FROM plantio p
            JOIN area a ON p.area_id = a.id
            JOIN cultura c ON p.cultura_id = c.id
        ''')
        plantios = cursor.fetchall()
        return plantios
    except Exception as e:
        message_erro = f"Erro ao buscar plantios: {str(e)}"
        registrar_log("plantio_repositorio", "pegar", "Erro", message_erro)
        raise Exception(message_erro)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()

"""
pegar_por_id:
    Recupera um plantio específico pelo seu ID.
Args:
    id (int): ID do plantio a ser buscado
Returns:
    tuple: Tupla contendo os dados do plantio
            (id, nome, observacao, area_id, area_nome, cultura_id, cultura_nome, data_plantio)
            ou None se não encontrado
Raises:
    Exception: Se houver erro na consulta ao banco de dados
"""
def pegar_por_id(id: int) -> tuple:
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        cursor.execute('''
            SELECT p.id, p.nome, p.observacao, p.area_id, a.nome as area_nome, p.cultura_id, c.nome as cultura_nome, p.data_plantio
            FROM plantio p
            JOIN area a ON p.area_id = a.id
            JOIN cultura c ON p.cultura_id = c.id
            WHERE p.id = :1
        ''', [id])
        plantio = cursor.fetchone()
        return plantio
    except Exception as e:
        message_erro = f"Erro ao buscar plantio por ID: {str(e)}"
        registrar_log("plantio_repositorio", "pegar_por_id", "Erro", message_erro)
        raise Exception(message_erro)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()

"""
criar:
    Cria um novo plantio no banco de dados.
Args:
    nome (str): Nome do plantio
    observacao (str): Observações sobre o plantio
    area_id (int): ID da área onde será feito o plantio
    cultura_id (int): ID da cultura a ser plantada
    data_plantio (str): Data do plantio no formato YYYY-MM-DD
Returns:
    int: ID do plantio criado
Raises:
    Exception: Se houver erro na criação do plantio
"""
def criar(nome: str, observacao: str, area_id: int, cultura_id: int, data_plantio: str) -> int:
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        id_var = cursor.var(int)
        cursor.execute(
            'INSERT INTO plantio (nome, observacao, area_id, cultura_id, data_plantio) VALUES (:1, :2, :3, :4, :5) RETURNING id INTO :6',
            [nome, observacao, area_id, cultura_id, data_plantio, id_var]
        )
        id = id_var.getvalue()
        conexao.commit()
        registrar_log("plantio_repositorio", "criar", "Sucesso", f"Plantio criada com sucesso - id: {str(id)}, nome: {str(nome)}, observacao: {str(observacao)}, area_id: {str(area_id)}, cultura_id: {str(cultura_id)}, data_plantio: {str(data_plantio)}")
        return id
    except Exception as e:
        message_error = f"Erro ao criar plantio: {str(e)}"
        registrar_log("plantio_repositorio", "criar", "Erro", message_error)
        raise Exception(message_error)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()

"""
atualizar_por_id:
    Atualiza os dados de um plantio existente.
Args:
    id (int): ID do plantio a ser atualizado
    nome (str): Novo nome do plantio
    observacao (str): Novas observações sobre o plantio
    area_id (int): Novo ID da área do plantio
    cultura_id (int): Novo ID da cultura do plantio
    data_plantio (str): Nova data do plantio no formato YYYY-MM-DD
Returns:
    bool: True se o plantio foi atualizado com sucesso, False caso contrário
Raises:
    Exception: Se houver erro na atualização do plantio
"""
def atualizar_por_id(id: int, nome: str, observacao: str, area_id: int, cultura_id: int, data_plantio: str) -> bool:
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        cursor.execute(
            'UPDATE plantio SET nome = :1, observacao = :2, area_id = :3, cultura_id = :4, data_plantio = :5 WHERE id = :6',
            [nome, observacao, area_id, cultura_id, data_plantio, id]
        )
        conexao.commit()
        registrar_log("plantio_repositorio", "atualizar_por_id", "Sucesso", f"Plantio atualizada com sucesso - id: {str(id)}, nome: {str(nome)}, observacao: {str(observacao)}, area_id: {str(area_id)}, cultura_id: {str(cultura_id)}, data_plantio: {str(data_plantio)}")
        return cursor.rowcount > 0
    except Exception as e:
        message_error = f"Erro ao atualizar plantio: {str(e)}"
        registrar_log("plantio_repositorio", "atualizar_por_id", "Erro", message_error)
        raise Exception(message_error)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()

"""
deletar_por_id:
    Remove um plantio do banco de dados.
Args:
    id (int): ID do plantio a ser removido
Returns:
    bool: True se o plantio foi removido com sucesso, False caso contrário
Raises:
    Exception: Se houver erro na remoção do plantio
"""
def deletar_por_id(id: int) -> bool:
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        cursor.execute('DELETE FROM plantio WHERE id = :1', [id])
        conexao.commit()
        registrar_log("plantio_repositorio", "deletar_por_id", "Sucesso", f"Plantio deletada com sucesso - id: {str(id)}")
        return cursor.rowcount > 0
    except Exception as e:
        message_error = f"Erro ao deletar plantio: {str(e)}"
        registrar_log("plantio_repositorio", "deletar_por_id", "Erro", message_error)
        raise Exception(message_error)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()