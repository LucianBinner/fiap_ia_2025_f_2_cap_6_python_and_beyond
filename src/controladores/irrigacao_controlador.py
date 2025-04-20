from repositorios import irrigacao_repositorio, feedback_repositorio
from controladores.irrigacao_controlador_validacao import *
from regras.avaliar_irrigacao_regra import avaliar_irrigacao
import pandas as pd
from datetime import datetime


def pegar_irrigacoes():
    irrigacoes = irrigacao_repositorio.pegar()
    irrigacoes_formatadas = [{
        'id': irrigacao[0],
        'plantio': irrigacao[2],
        'data_irrigacao': irrigacao[3].strftime('%Y-%m-%d'),
        'volume_agua_l': irrigacao[4]
    } for irrigacao in irrigacoes]
    df = pd.DataFrame(irrigacoes_formatadas)
    return df.to_string(index=False)

def pegar_irrigacao_por_id(id):
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

def criar_irrigacao(plantio_id, data_irrigacao_input, volume_agua_l_input):
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

def atualizar_irrigacao_por_id(id, plantio_id, data_irrigacao_input, volume_agua_l_input):
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

def deletar_irrigacao_por_id(id):
    validar_deletar_irrigacao(id)
    irrigacao = irrigacao_repositorio.pegar_por_id(id)
    if irrigacao is None:
        raise Exception("Irrigação não encontrada")
    if irrigacao_repositorio.deletar_por_id(id):
        return
    else:
        raise Exception("Erro ao deletar irrigação")