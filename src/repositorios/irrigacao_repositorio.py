from config.db.db_config import pegar_conexao
from config.logs.log_config import registrar_log

"""
pegar:
    Recupera todas as irrigações cadastradas no banco de dados.
Returns:
    list: Lista de tuplas contendo os dados de todas as irrigações
            (id, plantio_id, plantio_nome, data_irrigacao, volume_agua_l)
Raises:
    Exception: Se houver erro na consulta ao banco de dados
"""
def pegar() -> list:
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        cursor.execute('''
            SELECT i.id, i.plantio_id, p.nome as plantio_nome, i.data_irrigacao, i.volume_agua_l
            FROM irrigacao i
            JOIN plantio p ON i.plantio_id = p.id
        ''')
        irrigacoes = cursor.fetchall()
        return irrigacoes
    except Exception as e:
        message_error = f"Erro ao buscar irrigacoes: {str(e)}"
        registrar_log("irrigacao_repositorio", "pegar", "Erro", message_error)
        raise Exception(message_error)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()

"""
pegar_por_id:
    Recupera uma irrigação específica pelo seu ID, incluindo dados relacionados.
Args:
    id (int): ID da irrigação a ser buscada
Returns:
    tuple: Tupla contendo os dados da irrigação e informações relacionadas
            (id, volume_agua_l, data_irrigacao, nome_plantio, observacao,
            area_id, cultura_id, data_plantio, nome_area, localizacao,
            hectar, nome_cultura, consumo_hidrico_diario_l_m2)
            ou None se não encontrada
Raises:
    Exception: Se houver erro na consulta ao banco de dados
"""
def pegar_por_id(id: int) -> tuple:
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        cursor.execute('''
            SELECT
                irr.id,
                irr.volume_agua_l,
                irr.data_irrigacao,
                plan.nome AS nome_pnatio,
                plan.observacao,
                plan.area_id,
                plan.cultura_id,
                plan.data_plantio,
                area.nome AS nome_area,
                area.localizacao,
                area.hectar,
                cult.nome AS nome_cultura,
                cult.consumo_hidrico_diario_l_m2
            FROM
                irrigacao irr
                LEFT JOIN plantio plan ON irr.PLANTIO_ID = plan.id
                LEFT JOIN area ON plan.area_id = area.id
                LEFT JOIN cultura cult ON plan.cultura_id = cult.id
            WHERE
                irr.id = :1
        ''', [id])
        irrigacao = cursor.fetchone()
        return irrigacao
    except Exception as e:
        message_error = f"Erro ao buscar irrigacao por ID: {str(e)}"
        registrar_log("irrigacao_repositorio", "pegar_por_id", "Erro", message_error)
        raise Exception(message_error)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()

"""
criar:
    Cria uma nova irrigação no banco de dados.
Args:
    plantio_id (int): ID do plantio relacionado
    data_irrigacao (str): Data da irrigação no formato YYYY-MM-DD
    volume_agua_l (float): Volume de água utilizado em litros
Returns:
    int: ID da irrigação criada
Raises:
    Exception: Se houver erro na criação da irrigação
"""
def criar(plantio_id: int, data_irrigacao: str, volume_agua_l: float) -> int:
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        id_var = cursor.var(int)
        cursor.execute(
            'INSERT INTO irrigacao (plantio_id, data_irrigacao, volume_agua_l) VALUES (:1, :2, :3) RETURNING id INTO :4',
            [plantio_id, data_irrigacao, volume_agua_l, id_var]
        )
        id = id_var.getvalue()
        conexao.commit()
        registrar_log("irrigacao_repositorio", "criar", "Sucesso", f"Irrigacao criada com sucesso - id: {str(id)}, plantio_id: {str(plantio_id)}, data_irrigacao: {str(data_irrigacao)}, volume_agua_l: {str(volume_agua_l)}")
        return id
    except Exception as e:
        message_error = f"Erro ao criar irrigacao: {str(e)}"
        registrar_log("irrigacao_repositorio", "criar", "Erro", message_error)
        raise Exception(message_error)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()

"""
atualizar_por_id:
    Atualiza os dados de uma irrigação existente.
Args:
    id (int): ID da irrigação a ser atualizada
    plantio_id (int): Novo ID do plantio relacionado
    data_irrigacao (str): Nova data da irrigação no formato YYYY-MM-DD
    volume_agua_l (float): Novo volume de água em litros
Returns:
    bool: True se a irrigação foi atualizada com sucesso, False caso contrário
Raises:
    Exception: Se houver erro na atualização da irrigação
"""
def atualizar_por_id(id: int, plantio_id: int, data_irrigacao: str, volume_agua_l: float) -> bool:
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        cursor.execute(
            'UPDATE irrigacao SET plantio_id = :1, data_irrigacao = :2, volume_agua_l = :3 WHERE id = :4',
            [plantio_id, data_irrigacao, volume_agua_l, id]
        )
        conexao.commit()
        registrar_log("irrigacao_repositorio", "atualizar_por_id", "Sucesso", f"Irrigacao atualizada com sucesso - id: {str(id)}, plantio_id: {str(plantio_id)}, data_irrigacao: {str(data_irrigacao)}, volume_agua_l: {str(volume_agua_l)}")
        return cursor.rowcount > 0
    except Exception as e:
        message_error = f"Erro ao atualizar irrigacao: {str(e)}"
        registrar_log("irrigacao_repositorio", "atualizar_por_id", "Erro", message_error)
        raise Exception(message_error)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()

"""
deletar_por_id:
    Remove uma irrigação do banco de dados.
Args:
    id (int): ID da irrigação a ser removida
Returns:
    bool: True se a irrigação foi removida com sucesso, False caso contrário
Raises:
    Exception: Se houver erro na remoção da irrigação
"""
def deletar_por_id(id: int) -> bool:
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        cursor.execute('DELETE FROM irrigacao WHERE id = :1', [id])
        conexao.commit()
        registrar_log("irrigacao_repositorio", "deletar_por_id", "Sucesso", f"Irrigacao deletada com sucesso - id: {str(id)}")
        return cursor.rowcount > 0
    except Exception as e:
        message_error = f"Erro ao deletar irrigacao: {str(e)}"
        registrar_log("irrigacao_repositorio", "deletar_por_id", "Erro", message_error)
        raise Exception(message_error)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()