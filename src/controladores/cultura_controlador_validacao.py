from validadores.tipo_validador import validar_string, validar_decimal

"""
validar_id_cultura:
    Valida o ID de uma cultura.
Args:
    id (str): ID da cultura a ser validado
Returns:
    None
Raises:
    Exception: Se o ID for inválido (vazio, muito longo ou não numérico)
"""
def validar_id_cultura(id: str) -> None:
    try:
        int(id)
        if not id.strip() or len(id.strip()) > 50:
            raise ValueError()
    except ValueError:
        raise Exception("ID inválido!")

"""
validar_pegar_cultura_por_id:
    Valida o ID para busca de uma cultura.
Args:
    id (str): ID da cultura a ser validado
Returns:
    None
Raises:
    Exception: Se o ID for inválido
"""
def validar_pegar_cultura_por_id(id: str) -> None:
    validar_id_cultura(id)

"""
validar_criar_cultura:
    Valida os dados para criação de uma nova cultura.
Args:
    nome (str): Nome da cultura
    consumo_hidrico_diario_l_m2_input (str): Consumo hídrico diário em L/m² (será convertido para float)
Returns:
    None
Raises:
    Exception: Se algum dos campos for inválido
"""
def validar_criar_cultura(nome: str, consumo_hidrico_diario_l_m2_input: str) -> None:
    if not validar_string(nome) or not nome.strip():
        raise Exception("O nome da cultura não pode estar vazio")
    if not consumo_hidrico_diario_l_m2_input.strip():
        raise Exception("O consumo hídrico diário não pode estar vazio")
    try:
        consumo_hidrico_diario_l_m2 = float(consumo_hidrico_diario_l_m2_input)
        if not validar_decimal(consumo_hidrico_diario_l_m2) or consumo_hidrico_diario_l_m2 <= 0:
            raise Exception("O consumo hídrico diário deve ser um número positivo")
    except ValueError:
        raise Exception("O consumo hídrico diário deve ser um número válido")

"""
validar_atualizar_cultura:
    Valida os dados para atualização de uma cultura existente.
Args:
    id (str): ID da cultura
    nome (str): Novo nome da cultura
    consumo_hidrico_diario_l_m2_input (str): Novo consumo hídrico diário em L/m² (será convertido para float)
Returns:
    None
Raises:
    Exception: Se algum dos campos for inválido
"""
def validar_atualizar_cultura(id: str, nome: str, consumo_hidrico_diario_l_m2_input: str) -> None:
    validar_id_cultura(id)
    validar_criar_cultura(nome, consumo_hidrico_diario_l_m2_input)

"""
validar_deletar_cultura:
    Valida o ID para remoção de uma cultura.
Args:
    id (str): ID da cultura a ser removida
Returns:
    None
Raises:
    Exception: Se o ID for inválido
"""
def validar_deletar_cultura(id: str) -> None:
    validar_id_cultura(id)