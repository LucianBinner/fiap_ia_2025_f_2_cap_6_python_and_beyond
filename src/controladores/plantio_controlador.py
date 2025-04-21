from repositorios import plantio_repositorio
from controladores.plantio_controlador_validacao import *
import pandas as pd
from datetime import datetime

"""
pegar_plantios:
    Retorna todos os plantios cadastrados no sistema.
Returns:
    str: String formatada contendo todos os plantios em formato tabular.
Raises:
    Exception: Se houver erro ao buscar os plantios.
"""
def pegar_plantios():
    plantios = plantio_repositorio.pegar()
    if plantios is None:
        raise Exception("Erro ao buscar plantios")
    plantios_formatados = [{
        'id': plantio[0],
        'nome': plantio[1],
        'observacao': plantio[2],
        'area': plantio[4],
        'cultura': plantio[6],
        'data_plantio': plantio[7].strftime('%Y-%m-%d')
    } for plantio in plantios]
    df = pd.DataFrame(plantios_formatados)
    return df.to_string(index=False)

"""
pegar_plantio_por_id:
    Busca um plantio específico pelo seu ID.
Args:
    id (int): ID do plantio a ser buscado.
Returns:
    dict: Dicionário contendo os dados do plantio.
Raises:
    Exception: Se o plantio não for encontrado.
"""
def pegar_plantio_por_id(id):
    validar_pegar_plantio_por_id(id)
    plantio = plantio_repositorio.pegar_por_id(id)
    if plantio is None:
        raise Exception("Plantio não encontrado")
    return {
        'id': plantio[0],
        'nome': plantio[1],
        'observacao': plantio[2],
        'area': plantio[4],
        'cultura': plantio[6],
        'data_plantio': plantio[7].strftime('%Y-%m-%d')
    }

"""
criar_plantio:
    Cria um novo plantio no sistema.
Args:
    nome (str): Nome do plantio.
    observacao (str): Observações sobre o plantio.
    area_id (int): ID da área onde será feito o plantio.
    cultura_id (int): ID da cultura a ser plantada.
    data_plantio_input (str): Data do plantio no formato 'YYYY-MM-DD'.
Returns:
    dict: Dicionário contendo os dados do plantio criado.
Raises:
    Exception: Se houver erro na criação do plantio.
    ValueError: Se a data estiver em formato inválido.
"""
def criar_plantio(nome, observacao, area_id, cultura_id, data_plantio_input):
    validar_plantio(nome, observacao, area_id, cultura_id, data_plantio_input)
    data_plantio = datetime.strptime(data_plantio_input, '%Y-%m-%d')
    id_plantio = plantio_repositorio.criar(nome, observacao, area_id, cultura_id, data_plantio)
    if id_plantio:
        plantio = plantio_repositorio.pegar_por_id(id_plantio[0])
        return {
            'id': plantio[0],
            'nome': plantio[1],
            'observacao': plantio[2],
            'area': plantio[4],
            'cultura': plantio[6],
            'data_plantio': plantio[7].strftime('%Y-%m-%d')
        }
    else:
        raise Exception("Erro ao criar plantio")

"""
atualizar_plantio_por_id:
    Atualiza um plantio existente.
Args:
    id (int): ID do plantio a ser atualizado.
    nome (str): Novo nome do plantio.
    observacao (str): Novas observações.
    area_id (int): Novo ID da área.
    cultura_id (int): Novo ID da cultura.
    data_plantio_input (str): Nova data no formato 'YYYY-MM-DD'.
Returns:
    dict: Dicionário contendo os dados do plantio atualizado.
Raises:
    Exception: Se o plantio não for encontrado ou houver erro na atualização.
    ValueError: Se a data estiver em formato inválido.
"""
def atualizar_plantio_por_id(id, nome, observacao, area_id, cultura_id, data_plantio_input):
    validar_atualizar_plantio(id, nome, observacao, area_id, cultura_id, data_plantio_input)
    plantio = plantio_repositorio.pegar_por_id(id)
    if plantio is None:
        raise Exception("Plantio não encontrado")
    data_plantio = datetime.strptime(data_plantio_input, '%Y-%m-%d')
    if plantio_repositorio.atualizar_por_id(id, nome, observacao, area_id, cultura_id, data_plantio):
        plantio_atualizado = plantio_repositorio.pegar_por_id(id)
        return {
            'id': plantio_atualizado[0],
            'nome': plantio_atualizado[1],
            'observacao': plantio_atualizado[2],
            'area': plantio_atualizado[4],
            'cultura': plantio_atualizado[6],
            'data_plantio': plantio_atualizado[7].strftime('%Y-%m-%d')
        }
    else:
        raise Exception("Erro ao atualizar plantio")

"""
deletar_plantio_por_id:
    Remove um plantio do sistema.
Args:
    id (int): ID do plantio a ser removido.
Raises:
    Exception: Se o plantio não for encontrado ou houver erro na deleção.
"""
def deletar_plantio_por_id(id):
    validar_deletar_plantio(id)
    plantio = plantio_repositorio.pegar_por_id(id)
    if plantio is None:
        raise Exception("Plantio não encontrado")
    if plantio_repositorio.deletar_por_id(id):
        return
    else:
        raise Exception("Erro ao deletar plantio")