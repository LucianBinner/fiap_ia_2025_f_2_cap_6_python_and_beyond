from config.db.db_config import pegar_conexao
from config.logs.log_config import registrar_log

def pegar():
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

def pegar_por_id(id):
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

def criar(plantio_id, data_irrigacao, volume_agua_l):
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

def atualizar_por_id(id, plantio_id, data_irrigacao, volume_agua_l):
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

def deletar_por_id(id):
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