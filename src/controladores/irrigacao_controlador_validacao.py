from validadores.tipo_validador import validar_string, validar_decimal
from datetime import datetime
from repositorios import plantio_repositorio

"""
validar_id:
    Valida o ID de uma irrigação.
Args:
    id (str): ID a ser validado
    msg (str, optional): Mensagem de erro personalizada. Defaults to "ID inválido!"
Raises:
    Exception: Se o ID for inválido (vazio, muito longo ou não numérico)
"""
def validar_id(id: str, msg: str = "ID inválido!") -> None:
    try:
        int(id)
        if not id.strip() or len(id.strip()) > 50:
            raise ValueError()
    except ValueError:
        raise Exception(msg)

"""
validar_pegar_irrigacao_por_id:
    Valida o ID para busca de uma irrigação.
Args:
    id (str): ID da irrigação a ser validado
Raises:
    Exception: Se o ID for inválido
"""
def validar_pegar_irrigacao_por_id(id: str) -> None:
    validar_id(id)

"""
validar_irrigacao:
    Valida os dados para criação/atualização de uma irrigação.
Args:
    plantio_id (str): ID do plantio associado
    data_irrigacao_input (str): Data da irrigação no formato YYYY-MM-DD
    volume_agua_l_input (str): Volume de água em litros (será convertido para float)
Raises:
    Exception: Se algum dos campos for inválido ou se o plantio não existir
"""
def validar_irrigacao(plantio_id: str, data_irrigacao_input: str, volume_agua_l_input: str) -> None:
    validar_id(plantio_id, "O ID do plantio inválido!")
    plantio = plantio_repositorio.pegar_por_id(plantio_id)
    if plantio is None:
        raise Exception("O plantio especificado não existe")
    if not validar_string(data_irrigacao_input) or not data_irrigacao_input.strip():
        raise Exception("A data de irrigação não pode estar vazia")
    try:
        datetime.strptime(data_irrigacao_input, '%Y-%m-%d')
    except ValueError:
        raise Exception("A data de irrigação deve estar no formato YYYY-MM-DD")
    if not volume_agua_l_input.strip():
        raise Exception("O volume de água não pode estar vazio")
    try:
        volume_agua_l = float(volume_agua_l_input)
        if not validar_decimal(volume_agua_l) or volume_agua_l <= 0:
            raise Exception("O volume de água deve ser um número positivo")
    except ValueError:
        raise Exception("O volume de água deve ser um número válido")
    
"""
validar_atualizar_irrigacao:
    Valida os dados para atualização de uma irrigação existente.
Args:
    id (str): ID da irrigação
    plantio_id (str): Novo ID do plantio associado
    data_irrigacao_input (str): Nova data da irrigação no formato YYYY-MM-DD
    volume_agua_l_input (str): Novo volume de água em litros (será convertido para float)
Raises:
    Exception: Se algum dos campos for inválido
"""
def validar_atualizar_irrigacao(id: str, plantio_id: str, data_irrigacao_input: str, volume_agua_l_input: str) -> None:
    validar_id(id)
    validar_irrigacao(plantio_id, data_irrigacao_input, volume_agua_l_input)

"""
validar_deletar_irrigacao:
    Valida o ID para remoção de uma irrigação.
Args:
    id (str): ID da irrigação a ser removida
Raises:
    Exception: Se o ID for inválido
"""
def validar_deletar_irrigacao(id: str) -> None:
    validar_id(id)