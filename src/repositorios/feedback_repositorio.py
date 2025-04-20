from config.db.db_config import pegar_conexao
from config.logs.log_config import registrar_log

def pegar():
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        cursor.execute('''
            SELECT f.*, c.nome as cultura_nome 
            FROM feedback f 
            JOIN cultura c ON f.cultura_id = c.id
        ''')
        feedbacks = cursor.fetchall()
        return feedbacks
    except Exception as e:
        message_error = f"Erro ao buscar feedbacks: {str(e)}"
        registrar_log("feedback_repositorio", "pegar", "Erro", message_error)
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
            SELECT f.*, c.nome as cultura_nome 
            FROM feedback f 
            JOIN cultura c ON f.cultura_id = c.id 
            WHERE f.id = :1
        ''', [id])
        feedback = cursor.fetchone()
        return feedback
    except Exception as e:
        message_error = f"Erro ao buscar feedback por ID: {str(e)}"
        registrar_log("feedback_repositorio", "pegar_por_id", "Erro", message_error)
        raise Exception(message_error)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()

def pegar_por_cultura_id_e_percentual(cultura_id, percentual):
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        cursor.execute('''
            SELECT *
            FROM feedback
            WHERE cultura_id = :1
            ORDER BY ABS(percent - :2)
            FETCH FIRST 1 ROWS ONLY
        ''', [cultura_id, percentual])
        feedback = cursor.fetchone()
        return feedback
    except Exception as e:
        message_error = f"Erro ao buscar feedback por cultura_id e percentual: {str(e)}"
        registrar_log("feedback_repositorio", "pegar_por_cultura_id_e_percentual", "Erro", message_error)
        raise Exception(message_error)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()

def criar(cultura_id, message_feedback, tips, percent):
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        id_var = cursor.var(int)
        cursor.execute(
            'INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (:1, :2, :3, :4) RETURNING id INTO :5',
            [cultura_id, message_feedback, tips, percent, id_var]
        )
        conexao.commit()
        registrar_log("feedback_repositorio", "criar", "Sucesso", f"Feedback criado com sucesso - id: {str(id_var.getvalue())}, cultura_id: {str(cultura_id)}, message_feedback: {str(message_feedback)}, tips: {str(tips)}, percent: {str(percent)}")
        return id_var.getvalue()[0]
    except Exception as e:
        message_error = f"Erro ao criar feedback: {str(e)}"
        registrar_log("feedback_repositorio", "criar", "Erro", message_error)
        raise Exception(message_error)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()

def atualizar_por_id(id, cultura_id, message_feedback, tips, percent):
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        cursor.execute(
            'UPDATE feedback SET cultura_id = :1, message_feedback = :2, tips = :3, percent = :4 WHERE id = :5',
            [cultura_id, message_feedback, tips, percent, id]
        )
        conexao.commit()
        registrar_log("feedback_repositorio", "atualizar_por_id", "Sucesso", f"Feedback atualizado com sucesso - id: {str(id)}, cultura_id: {str(cultura_id)}, message_feedback: {str(message_feedback)}, tips: {str(tips)}, percent: {str(percent)}")
        return cursor.rowcount > 0
    except Exception as e:
        message_error = f"Erro ao atualizar feedback: {str(e)}"
        registrar_log("feedback_repositorio", "atualizar_por_id", "Erro", message_error)
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
        cursor.execute('DELETE FROM feedback WHERE id = :1', [id])
        conexao.commit()
        registrar_log("feedback_repositorio", "deletar_por_id", "Sucesso", f"Feedback deletado com sucesso - id: {str(id)}")
        return cursor.rowcount > 0
    except Exception as e:
        message_error = f"Erro ao deletar feedback: {str(e)}"
        registrar_log("feedback_repositorio", "deletar_por_id", "Erro", message_error)
        raise Exception(message_error)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()