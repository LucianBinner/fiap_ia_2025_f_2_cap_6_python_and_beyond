from repositorios import area_repositorio
from controladores.area_controlador_validacao import *
import pandas as pd

"""
pegar_areas:
    Retorna todas as áreas cadastradas no sistema em formato de string tabulada.
Returns:
    str: String formatada contendo todas as áreas com suas informações (id, nome, localização e hectares)
Raises:
    Exception: Se houver erro ao buscar as áreas no repositório
"""
def pegar_areas() -> str:
    areas = area_repositorio.pegar()
    if areas is None:
        raise Exception('Erro ao buscar áreas')
    areas_formatadas = [{
        'id': area[0],
        'nome': area[1],
        'localizacao': area[2],
        'hectar': area[3]
    } for area in areas]
    df = pd.DataFrame(areas_formatadas)
    return df.to_string(index=False)

"""
pegar_area_por_id:
    Busca uma área específica pelo seu ID.
Args:
    id (int): ID da área a ser buscada
Returns:
    dict: Dicionário contendo as informações da área (id, nome, localização e hectares)
Raises:
    Exception: Se a área não for encontrada ou houver erro na validação
"""
def pegar_area_por_id(id: int) -> dict:
    validar_pegar_area_por_id(id)
    area = area_repositorio.pegar_por_id(id)
    if area is None:
        raise Exception("Área não encontrada")
    return {
        'id': area[0],
        'nome': area[1],
        'localizacao': area[2],
        'hectar': area[3]
    }

"""
criar_area:
    Cria uma nova área no sistema.
Args:
    nome (str): Nome da área
    localizacao (str): Localização da área
    hectar_input (str): Tamanho da área em hectares (será convertido para float)
Returns:
    dict: Dicionário contendo as informações da área criada
Raises:
    Exception: Se houver erro na validação ou na criação da área
"""
def criar_area(nome: str, localizacao: str, hectar_input: str) -> dict:
    validar_criar_area(nome, localizacao, hectar_input)
    hectar = float(hectar_input)
    id_area = area_repositorio.criar(nome, localizacao, hectar)
    if id_area:
        area = area_repositorio.pegar_por_id(id_area)
        return {
            'id': area[0],
            'nome': area[1],
            'localizacao': area[2],
            'hectar': area[3]
        }
    else:
        raise Exception("Erro ao criar área!")

"""
atualizar_area_por_id:
    Atualiza as informações de uma área existente.
Args:
    id (int): ID da área a ser atualizada
    nome (str): Novo nome da área
    localizacao (str): Nova localização da área
    hectar_input (str): Novo tamanho da área em hectares (será convertido para float)
Returns:
    dict: Dicionário contendo as informações atualizadas da área
Raises:
    Exception: Se a área não for encontrada ou houver erro na atualização
"""
def atualizar_area_por_id(id: int, nome: str, localizacao: str, hectar_input: str) -> dict:
    validar_atualizar_area(id, nome, localizacao, hectar_input)
    area = area_repositorio.pegar_por_id(id)
    if area is None:
        raise Exception("Área não encontrada")
    hectar = float(hectar_input)
    if area_repositorio.atualizar_por_id(id, nome, localizacao, hectar):
        area_atualizada = area_repositorio.pegar_por_id(id)
        return {
            'id': area_atualizada[0],
            'nome': area_atualizada[1],
            'localizacao': area_atualizada[2],
            'hectar': area_atualizada[3]
        }
    else:
        raise Exception("Erro ao atualizar área!")

"""
deletar_area_por_id:
    Remove uma área do sistema.
Args:
    id (int): ID da área a ser removida
Returns:
    None
Raises:
    Exception: Se a área não for encontrada ou houver erro na remoção
"""
def deletar_area_por_id(id: int) -> None:
    validar_deletar_area(id)
    area = area_repositorio.pegar_por_id(id)
    if area is None:
        raise Exception("Área não encontrada")
    if area_repositorio.deletar_por_id(id):
        return
    else:
        raise Exception("Erro ao deletar área!")