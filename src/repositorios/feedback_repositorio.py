from config.db.db_config import pegar_conexao
from config.logs.log_config import registrar_log

"""
pegar:
    Recupera todos os feedbacks cadastrados no banco de dados.
Returns:
    list: Lista de tuplas contendo os dados de todos os feedbacks
            (id, cultura_id, message_feedback, tips, percent, cultura_nome)
Raises:
    Exception: Se houver erro na consulta ao banco de dados
"""
def pegar() -> list:
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

"""
pegar_por_id:
    Recupera um feedback específico pelo seu ID.
Args:
    id (int): ID do feedback a ser buscado
Returns:
    tuple: Tupla contendo os dados do feedback
            (id, cultura_id, message_feedback, tips, percent, cultura_nome)
            ou None se não encontrado
Raises:
    Exception: Se houver erro na consulta ao banco de dados
"""
def pegar_por_id(id: int) -> tuple:
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

"""
pegar_por_cultura_id_e_percentual:
    Recupera o feedback mais próximo ao percentual especificado para uma cultura.
Args:
    cultura_id (int): ID da cultura
    percentual (float): Percentual de referência para busca
Returns:
    tuple: Tupla contendo os dados do feedback mais próximo ao percentual
            (id, cultura_id, message_feedback, tips, percent)
            ou None se não encontrado
Raises:
    Exception: Se houver erro na consulta ao banco de dados
"""
def pegar_por_cultura_id_e_percentual(cultura_id: int, percentual: float) -> tuple:
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

"""
criar:
    Cria um novo feedback no banco de dados.
Args:
    cultura_id (int): ID da cultura relacionada
    message_feedback (str): Mensagem do feedback
    tips (str): Dicas ou sugestões
    percent (float): Percentual relacionado ao feedback
Returns:
    int: ID do feedback criado
Raises:
    Exception: Se houver erro na criação do feedback
"""
def criar(cultura_id: int, message_feedback: str, tips: str, percent: float) -> int:
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

"""
atualizar_por_id:
    Atualiza os dados de um feedback existente.
Args:
    id (int): ID do feedback a ser atualizado
    cultura_id (int): Novo ID da cultura relacionada
    message_feedback (str): Nova mensagem do feedback
    tips (str): Novas dicas ou sugestões
    percent (float): Novo percentual
Returns:
    bool: True se o feedback foi atualizado com sucesso, False caso contrário
Raises:
    Exception: Se houver erro na atualização do feedback
"""
def atualizar_por_id(id: int, cultura_id: int, message_feedback: str, tips: str, percent: float) -> bool:
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

"""
deletar_por_id:
    Remove um feedback do banco de dados.
Args:
    id (int): ID do feedback a ser removido
Returns:
    bool: True se o feedback foi removido com sucesso, False caso contrário
Raises:
    Exception: Se houver erro na remoção do feedback
"""
def deletar_por_id(id: int) -> bool:
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