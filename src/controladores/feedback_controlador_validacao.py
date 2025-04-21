from validadores.tipo_validador import validar_string, validar_decimal

"""
validar_id:
    Valida se o ID fornecido é um número inteiro válido e tem comprimento adequado.
Args:
    id (str): O ID a ser validado
    msg (str, opcional): Mensagem de erro personalizada. Padrão: "ID inválido!"
Raises:
    Exception: Se o ID não for um número inteiro válido ou estiver fora do tamanho permitido
"""
def validar_id(id, msg="ID inválido!"):
    try:
        int(id)
        if not id.strip() or len(id.strip()) > 50:
            raise ValueError()
    except ValueError:
        raise Exception(msg)

"""
validar_pegar_feedback_por_id:
    Valida o ID para busca de feedback.
Args:
    id (str): O ID do feedback a ser buscado
Raises:
    Exception: Se o ID for inválido
"""
def validar_pegar_feedback_por_id(id):
    validar_id(id)

"""
validar_feedback:
    Valida os dados de um feedback antes de sua criação ou atualização.
Args:
    cultura_id (str): ID da cultura associada ao feedback
    message_feedback (str): Mensagem do feedback
    tips (str): Dicas de melhoria
    percent_input (str): Porcentagem em formato string
Raises:
    Exception: Se qualquer um dos campos for inválido ou estiver vazio
"""
def validar_feedback(cultura_id, message_feedback, tips, percent_input):
    validar_id(cultura_id, "ID da cultura inválido!")
    if not validar_string(message_feedback) or not message_feedback.strip():
        raise Exception("A mensagem do feedback não pode estar vazia")
    if not validar_string(tips) or not tips.strip():
        raise Exception("As dicas não podem estar vazias")
    if not percent_input.strip():
        raise Exception("A porcentagem não pode estar vazia")
    try:
        percent = float(percent_input)
        if not validar_decimal(percent) or percent < 0 or percent > 100:
            raise Exception("A porcentagem deve ser um número entre 0 e 100")
    except ValueError:
        raise Exception("A porcentagem deve ser um número válido")

"""
validar_atualizar_feedback:
    Valida os dados para atualização de um feedback existente.
Args:
    id (str): ID do feedback a ser atualizado
    cultura_id (str): ID da cultura associada
    message_feedback (str): Nova mensagem do feedback
    tips (str): Novas dicas
    percent_input (str): Nova porcentagem em formato string
Raises:
    Exception: Se qualquer um dos campos for inválido
"""
def validar_atualizar_feedback(id, cultura_id, message_feedback, tips, percent_input):
    validar_id(id)
    validar_feedback(cultura_id, message_feedback, tips, percent_input)

"""
validar_deletar_feedback:
    Valida o ID para exclusão de um feedback.
Args:
    id (str): ID do feedback a ser excluído
Raises:
    Exception: Se o ID for inválido
"""
def validar_deletar_feedback(id):
    return validar_id(id)