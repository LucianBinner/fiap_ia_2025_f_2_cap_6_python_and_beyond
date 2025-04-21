"""
avaliar_irrigacao:
    Avalia a eficiência da irrigação comparando o volume utilizado com o volume ideal.
Args:
    volume_utilizado (float): Volume de água utilizado na irrigação em litros
    area_ha (float): Área irrigada em hectares
    consumo_l_m2 (float): Consumo hídrico diário em L/m²
Returns:
    float: Percentual de diferença entre o volume utilizado e o ideal.
            Valores positivos indicam excesso, negativos indicam déficit.
Raises:
    Exception: Se houver erro nos cálculos da avaliação
"""
def avaliar_irrigacao(volume_utilizado: float, area_ha: float, consumo_l_m2: float) -> float:
    try:
        area_m2 = area_ha * 10000
        volume_ideal = area_m2 * consumo_l_m2
        diferenca = volume_utilizado - volume_ideal
        percentual = diferenca / volume_ideal * 100
        return percentual
    except Exception as e:
        raise Exception(f"Erro ao avaliar irrigação: {str(e)}")