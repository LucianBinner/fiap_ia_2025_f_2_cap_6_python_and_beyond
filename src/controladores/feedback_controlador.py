from repositorios import feedback_repositorio
from controladores.feedback_controlador_validacao import *
import pandas as pd

"""
pegar_feedbacks:
    Retorna todos os feedbacks cadastrados no sistema.
Returns:
    str: String formatada contendo todos os feedbacks em formato tabular.
"""
def pegar_feedbacks():
    feedbacks = feedback_repositorio.pegar()
    feedbacks_formatados = [{
        'id': feedback[0],
        'cultura_id': feedback[1],
        'message_feedback': feedback[2],
        'tips': feedback[3],
        'percent': feedback[4],
        'cultura_nome': feedback[5]
    } for feedback in feedbacks]
    df = pd.DataFrame(feedbacks_formatados)
    return df.to_string(index=False)

"""
pegar_feedback_por_id:
    Busca um feedback específico pelo seu ID.
Args:
    id (int): ID do feedback a ser buscado.
Returns:
    dict: Dicionário contendo os dados do feedback.
Raises:
    Exception: Se o feedback não for encontrado.
"""
def pegar_feedback_por_id(id):
    validar_pegar_feedback_por_id(id)
    feedback = feedback_repositorio.pegar_por_id(id)
    if feedback is None:
        raise Exception("Feedback não encontrado")
    return {
        'id': feedback[0],
        'cultura_id': feedback[1],
        'message_feedback': feedback[2],
        'tips': feedback[3],
        'percent': feedback[4],
        'cultura_nome': feedback[5]
    }

"""
criar_feedback:
    Cria um novo feedback no sistema.
Args:
    cultura_id (int): ID da cultura relacionada ao feedback.
    message_feedback (str): Mensagem principal do feedback.
    tips (str): Dicas ou sugestões relacionadas ao feedback.
    percent_input (str): Percentual em formato string (será convertido para float).
Returns:
    dict: Dicionário contendo os dados do feedback criado.
Raises:
    Exception: Se houver erro na criação do feedback.
"""
def criar_feedback(cultura_id, message_feedback, tips, percent_input):
    validar_feedback(cultura_id, message_feedback, tips, percent_input)
    percent = float(percent_input)
    id_feedback = feedback_repositorio.criar(cultura_id, message_feedback, tips, percent)
    if id_feedback:
        feedback = feedback_repositorio.pegar_por_id(id_feedback)
        return {
            'id': feedback[0],
            'cultura_id': feedback[1],
            'message_feedback': feedback[2],
            'tips': feedback[3],
            'percent': feedback[4],
            'cultura_nome': feedback[5]
        }
    else:
        raise Exception("Erro ao criar feedback!")

"""
atualizar_feedback_por_id:
    Atualiza um feedback existente.
Args:
    id (int): ID do feedback a ser atualizado.
    cultura_id (int): Novo ID da cultura.
    message_feedback (str): Nova mensagem do feedback.
    tips (str): Novas dicas.
    percent_input (str): Novo percentual em formato string.
Returns:
    dict: Dicionário contendo os dados do feedback atualizado.
Raises:
    Exception: Se o feedback não for encontrado ou houver erro na atualização.
"""
def atualizar_feedback_por_id(id, cultura_id, message_feedback, tips, percent_input):
    validar_atualizar_feedback(id, cultura_id, message_feedback, tips, percent_input)
    feedback = feedback_repositorio.pegar_por_id(id)
    if feedback is None:
        raise Exception("Feedback não encontrado")
    percent = float(percent_input)
    if feedback_repositorio.atualizar_por_id(id, cultura_id, message_feedback, tips, percent):
        feedback_atualizado = feedback_repositorio.pegar_por_id(id)
        return {
            'id': feedback_atualizado[0],
            'cultura_id': feedback_atualizado[1],
            'message_feedback': feedback_atualizado[2],
            'tips': feedback_atualizado[3],
            'percent': feedback_atualizado[4],
            'cultura_nome': feedback_atualizado[5]
        }
    else:
        raise Exception("Erro ao atualizar feedback!")

"""
deletar_feedback_por_id:
    Remove um feedback do sistema.
Args:
    id (int): ID do feedback a ser removido.
Raises:
    Exception: Se o feedback não for encontrado ou houver erro na deleção.
"""
def deletar_feedback_por_id(id):
    validar_deletar_feedback(id)
    feedback = feedback_repositorio.pegar_por_id(id)
    if feedback is None:
        raise Exception("Feedback não encontrado")
    if feedback_repositorio.deletar_por_id(id):
        return
    else:
        raise Exception("Erro ao deletar feedback")