from config.db.db_config import pegar_conexao
from config.logs.log_config import registrar_log

def pegar():
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

def pegar_por_id(id):
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

def criar(nome, consumo_hidrico_diario_l_m2):
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

def atualizar_por_id(id, nome, consumo_hidrico_diario_l_m2):
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

def deletar_por_id(id):
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