from config.db.db_config import pegar_conexao

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
        raise Exception("Erro ao buscar feedbacks: {str(e)}")
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
        raise Exception(f"Erro ao buscar feedback por ID: {str(e)}")
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
        raise Exception(f"Erro ao buscar feedback por ID: {str(e)}")
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
        return id_var.getvalue()[0]
    except Exception as e:
        raise Exception(f"Erro ao criar feedback: {str(e)}")
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
        return cursor.rowcount > 0
    except Exception as e:
        raise Exception(f"Erro ao atualizar feedback: {str(e)}")
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
        return cursor.rowcount > 0
    except Exception as e:
        raise Exception(f"Erro ao deletar feedback: {str(e)}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()