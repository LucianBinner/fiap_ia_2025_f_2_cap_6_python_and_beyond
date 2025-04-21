from repositorios import cultura_repositorio
from controladores.cultura_controlador_validacao import *
import pandas as pd

"""
pegar_culturas:
    Retorna todas as culturas cadastradas no sistema em formato de string tabulada.
Returns:
    str: String formatada contendo todas as culturas com suas informações (id, nome, consumo hídrico)
Raises:
    Exception: Se houver erro ao buscar as culturas no repositório
"""
def pegar_culturas() -> str:
    culturas = cultura_repositorio.pegar()
    if culturas is None:
        raise Exception("Erro ao buscar culturas!")
    culturas_formatadas = [{
        'id': cultura[0],
        'nome': cultura[1],
        'consumo_hidrico_diario_l_m2': cultura[2]
    } for cultura in culturas]
    df = pd.DataFrame(culturas_formatadas)
    return df.to_string(index=False)

"""
pegar_cultura_por_id:
    Busca uma cultura específica pelo seu ID.
Args:
    id (int): ID da cultura a ser buscada
Returns:
    dict: Dicionário contendo as informações da cultura (id, nome, consumo hídrico)
Raises:
    Exception: Se a cultura não for encontrada ou houver erro na validação
"""
def pegar_cultura_por_id(id: int) -> dict:
    validar_pegar_cultura_por_id(id)
    cultura = cultura_repositorio.pegar_por_id(id)
    if cultura is None:
        raise Exception("Cultura não encontrada")
    return {
        'id': cultura[0],
        'nome': cultura[1],
        'consumo_hidrico_diario_l_m2': cultura[2]
    }

"""
criar_cultura:
    Cria uma nova cultura no sistema.
Args:
    nome (str): Nome da cultura
    consumo_hidrico_diario_l_m2_input (str): Consumo hídrico diário em L/m² (será convertido para float)
Returns:
    dict: Dicionário contendo as informações da cultura criada
Raises:
    Exception: Se houver erro na validação ou na criação da cultura
"""
def criar_cultura(nome: str, consumo_hidrico_diario_l_m2_input: str) -> dict:
    validar_criar_cultura(nome, consumo_hidrico_diario_l_m2_input)
    consumo_hidrico_diario_l_m2 = float(consumo_hidrico_diario_l_m2_input)
    id_cultura = cultura_repositorio.criar(nome, consumo_hidrico_diario_l_m2)
    if id_cultura:
        cultura = cultura_repositorio.pegar_por_id(id_cultura[0])
        return {
            'id': cultura[0],
            'nome': cultura[1],
            'consumo_hidrico_diario_l_m2': cultura[2]
        }

"""
atualizar_cultura_por_id:
    Atualiza as informações de uma cultura existente.
Args:
    id (int): ID da cultura a ser atualizada
    nome (str): Novo nome da cultura
    consumo_hidrico_diario_l_m2_input (str): Novo consumo hídrico diário em L/m² (será convertido para float)
Returns:
    dict: Dicionário contendo as informações atualizadas da cultura
Raises:
    Exception: Se a cultura não for encontrada ou houver erro na atualização
"""
def atualizar_cultura_por_id(id: int, nome: str, consumo_hidrico_diario_l_m2_input: str) -> dict:
    validar_atualizar_cultura(id, nome, consumo_hidrico_diario_l_m2_input)
    cultura = cultura_repositorio.pegar_por_id(id)
    if cultura is None:
        raise Exception("Cultura não encontrada")
    consumo_hidrico_diario_l_m2 = float(consumo_hidrico_diario_l_m2_input)
    if cultura_repositorio.atualizar_por_id(id, nome, consumo_hidrico_diario_l_m2):
        cultura_atualizada = cultura_repositorio.pegar_por_id(id)
        return {
            'id': cultura_atualizada[0],
            'nome': cultura_atualizada[1],
            'consumo_hidrico_diario_l_m2': cultura_atualizada[2]
        }
    else:
        raise Exception("Erro ao atualizar cultura!")

"""
deletar_cultura_por_id:
    Remove uma cultura do sistema.
Args:
    id (int): ID da cultura a ser removida
Returns:
    None
Raises:
    Exception: Se a cultura não for encontrada ou houver erro na remoção
"""
def deletar_cultura_por_id(id: int) -> None:
    validar_deletar_cultura(id)
    cultura = cultura_repositorio.pegar_por_id(id)
    if cultura is None:
        raise Exception("Cultura não encontrada")
    if cultura_repositorio.deletar_por_id(id):
        return
    else:
        raise Exception("Erro ao deletar cultura!")