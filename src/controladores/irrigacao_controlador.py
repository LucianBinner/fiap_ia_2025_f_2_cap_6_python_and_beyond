from repositorios import irrigacao_repositorio, feedback_repositorio
from controladores.irrigacao_controlador_validacao import *
from regras.avaliar_irrigacao_regra import avaliar_irrigacao
import pandas as pd
from datetime import datetime


"""
pegar_irrigacoes:
    Retorna todas as irrigações cadastradas no sistema em formato de string tabulada.
Returns:
    str: String formatada contendo todas as irrigações com suas informações (id, plantio, data, volume)
Raises:
    Exception: Se houver erro ao buscar as irrigações no repositório
"""
def pegar_irrigacoes() -> str:
    irrigacoes = irrigacao_repositorio.pegar()
    irrigacoes_formatadas = [{
        'id': irrigacao[0],
        'plantio': irrigacao[2],
        'data_irrigacao': irrigacao[3].strftime('%Y-%m-%d'),
        'volume_agua_l': irrigacao[4]
    } for irrigacao in irrigacoes]
    df = pd.DataFrame(irrigacoes_formatadas)
    return df.to_string(index=False)

"""
pegar_irrigacao_por_id:
    Busca uma irrigação específica pelo seu ID.
Args:
    id (int): ID da irrigação a ser buscada
Returns:
    dict: Dicionário contendo as informações da irrigação (id, data, volume, plantio, feedback, dica)
Raises:
    Exception: Se a irrigação não for encontrada ou houver erro ao buscar o feedback
"""
def pegar_irrigacao_por_id(id: int) -> dict:
    validar_pegar_irrigacao_por_id(id)
    irrigacao = irrigacao_repositorio.pegar_por_id(id)
    if irrigacao is None:
        raise Exception("Irrigação não encontrada")
    percentual = avaliar_irrigacao(irrigacao[1], irrigacao[10], irrigacao[12])
    feedback = feedback_repositorio.pegar_por_cultura_id_e_percentual(irrigacao[6], percentual)
    if feedback is None:
        raise Exception("Erro ao pegar feedback da irrigação")
    return {
        'id': irrigacao[0],
        'data_irrigacao': irrigacao[2].strftime('%Y-%m-%d'),
        'volume_agua_l': irrigacao[1],
        'plantio': irrigacao[3],
        'feedback': feedback[2],
        'dica': feedback[3],
    }

"""
criar_irrigacao:
    Cria uma nova irrigação no sistema.
Args:
    plantio_id (int): ID do plantio associado
    data_irrigacao_input (str): Data da irrigação no formato YYYY-MM-DD
    volume_agua_l_input (str): Volume de água em litros (será convertido para float)
Returns:
    dict: Dicionário contendo as informações da irrigação criada
Raises:
    Exception: Se houver erro na validação, criação ou ao buscar o feedback
"""
def criar_irrigacao(plantio_id: int, data_irrigacao_input: str, volume_agua_l_input: str) -> dict:
    validar_irrigacao(plantio_id, data_irrigacao_input, volume_agua_l_input)
    data_irrigacao = datetime.strptime(data_irrigacao_input, '%Y-%m-%d')
    volume_agua_l = float(volume_agua_l_input)
    id_irrigacao = irrigacao_repositorio.criar(plantio_id, data_irrigacao, volume_agua_l)
    if id_irrigacao:
        irrigacao = irrigacao_repositorio.pegar_por_id(id_irrigacao[0])
        percentual = avaliar_irrigacao(irrigacao[1], irrigacao[10], irrigacao[12])
        feedback = feedback_repositorio.pegar_por_cultura_id_e_percentual(irrigacao[6], percentual)
        if feedback is None:
            raise Exception("Erro ao pegar feedback da irrigação")
        return {
            'id': irrigacao[0],
            'data_irrigacao': irrigacao[2].strftime('%Y-%m-%d'),
            'volume_agua_l': irrigacao[1],
            'plantio': irrigacao[3],
            'feedback': feedback[2],
            'dica': feedback[3],
        }
    else:
        raise Exception("Erro ao criar irrigação")

"""
atualizar_irrigacao_por_id:
    Atualiza as informações de uma irrigação existente.
Args:
    id (int): ID da irrigação a ser atualizada
    plantio_id (int): Novo ID do plantio associado
    data_irrigacao_input (str): Nova data da irrigação no formato YYYY-MM-DD
    volume_agua_l_input (str): Novo volume de água em litros (será convertido para float)
Returns:
    dict: Dicionário contendo as informações atualizadas da irrigação
Raises:
    Exception: Se a irrigação não for encontrada ou houver erro na atualização
"""
def atualizar_irrigacao_por_id(id: int, plantio_id: int, data_irrigacao_input: str, volume_agua_l_input: str) -> dict:
    validar_atualizar_irrigacao(id, plantio_id, data_irrigacao_input, volume_agua_l_input)
    irrigacao = irrigacao_repositorio.pegar_por_id(id)
    if irrigacao is None:
        raise Exception("Irrigação não encontrada")
    data_irrigacao = datetime.strptime(data_irrigacao_input, '%Y-%m-%d')
    volume_agua_l = float(volume_agua_l_input)
    if irrigacao_repositorio.atualizar_por_id(id, plantio_id, data_irrigacao, volume_agua_l):
        irrigacao_atualizada = irrigacao_repositorio.pegar_por_id(id)
        percentual = avaliar_irrigacao(irrigacao_atualizada[1], irrigacao_atualizada[10], irrigacao_atualizada[12])
        feedback = feedback_repositorio.pegar_por_cultura_id_e_percentual(irrigacao_atualizada[6], percentual)
        if feedback is None:
            raise Exception("Erro ao pegar feedback da irrigação")
        return {
            'id': irrigacao_atualizada[0],
            'data_irrigacao': irrigacao_atualizada[2].strftime('%Y-%m-%d'),
            'volume_agua_l': irrigacao_atualizada[1],
            'plantio': irrigacao_atualizada[3],
            'feedback': feedback[2],
            'dica': feedback[3],
        }
    else:
        raise Exception("Erro ao atualizar irrigação")

"""
deletar_irrigacao_por_id:
    Remove uma irrigação do sistema.
Args:
    id (int): ID da irrigação a ser removida
Returns:
    None
Raises:
    Exception: Se a irrigação não for encontrada ou houver erro na remoção
"""
def deletar_irrigacao_por_id(id: int) -> None:
    validar_deletar_irrigacao(id)
    irrigacao = irrigacao_repositorio.pegar_por_id(id)
    if irrigacao is None:
        raise Exception("Irrigação não encontrada")
    if irrigacao_repositorio.deletar_por_id(id):
        return
    else:
        raise Exception("Erro ao deletar irrigação")