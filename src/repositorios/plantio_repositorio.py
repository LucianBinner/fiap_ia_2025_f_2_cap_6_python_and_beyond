from config.db.db_config import pegar_conexao
from config.logs.log_config import registrar_log

def pegar():
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

def pegar_por_id(id):
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

def criar(nome, observacao, area_id, cultura_id, data_plantio):
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

def atualizar_por_id(id, nome, observacao, area_id, cultura_id, data_plantio):
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

def deletar_por_id(id):
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