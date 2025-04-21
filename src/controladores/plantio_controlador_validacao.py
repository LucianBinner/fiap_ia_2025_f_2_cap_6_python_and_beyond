from validadores.tipo_validador import validar_string
from datetime import datetime
from repositorios import area_repositorio, cultura_repositorio

"""
validar_id:
    Valida o ID de um plantio.
Args:
    id (str): ID a ser validado
    msg (str, optional): Mensagem de erro personalizada. Defaults to "ID inválido!"
Raises:
    ValueError: Se o ID for inválido (vazio, muito longo ou não numérico)
"""
def validar_id(id: str, msg: str = "ID inválido!") -> None:
    try:
        int(id)
        if not id.strip() or len(id.strip()) > 50:
            raise ValueError()
    except ValueError:
        raise ValueError(msg)

"""
validar_pegar_plantio_por_id:
    Valida o ID para busca de um plantio.
Args:
    id (str): ID do plantio a ser validado
Raises:
    ValueError: Se o ID for inválido
"""
def validar_pegar_plantio_por_id(id: str) -> None:
    validar_id(id)

"""
validar_plantio:
    Valida os dados para criação/atualização de um plantio.
Args:
    nome (str): Nome do plantio
    observacao (str): Observação sobre o plantio
    area_id (str): ID da área associada
    cultura_id (str): ID da cultura associada
    data_plantio_input (str): Data do plantio no formato YYYY-MM-DD
Raises:
    Exception: Se algum dos campos for inválido ou se a área/cultura não existir
"""
def validar_plantio(nome: str, observacao: str, area_id: str, cultura_id: str, data_plantio_input: str) -> None:
    validar_id(area_id, "O ID da área é inválido!")
    validar_id(cultura_id, "O ID da cultura é inválido!")
    if not validar_string(nome) or not nome.strip():
        raise Exception("O nome do plantio não pode estar vazio")
    if not validar_string(observacao) or not observacao.strip():
        raise Exception("A observação do plantio não pode estar vazia")
    area = area_repositorio.pegar_por_id(area_id)
    if area is None:
        raise Exception("A área especificada não existe")
    cultura = cultura_repositorio.pegar_por_id(cultura_id)
    if cultura is None:
        raise Exception("A cultura especificada não existe")
    if not validar_string(data_plantio_input) or not data_plantio_input.strip():
        raise Exception("A data de plantio não pode estar vazia")
    try:
        datetime.strptime(data_plantio_input, '%Y-%m-%d')
    except ValueError:
        raise Exception("A data de plantio deve estar no formato YYYY-MM-DD")

"""
validar_atualizar_plantio:
    Valida os dados para atualização de um plantio existente.
Args:
    id (str): ID do plantio
    nome (str): Novo nome do plantio
    observacao (str): Nova observação sobre o plantio
    area_id (str): Novo ID da área associada
    cultura_id (str): Novo ID da cultura associada
    data_plantio_input (str): Nova data do plantio no formato YYYY-MM-DD
Raises:
    ValueError: Se o ID for inválido
    Exception: Se algum dos outros campos for inválido
"""
def validar_atualizar_plantio(id: str, nome: str, observacao: str, area_id: str, cultura_id: str, data_plantio_input: str) -> None:
    validar_id(id)
    validar_plantio(nome, observacao, area_id, cultura_id, data_plantio_input)

"""
validar_deletar_plantio:
    Valida o ID para remoção de um plantio.
Args:
    id (str): ID do plantio a ser removido
Raises:
    ValueError: Se o ID for inválido
"""
def validar_deletar_plantio(id: str) -> None:
    validar_id(id)