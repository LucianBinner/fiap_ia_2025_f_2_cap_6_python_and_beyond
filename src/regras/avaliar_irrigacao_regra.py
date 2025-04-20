def avaliar_irrigacao(volume_utilizado, area_ha, consumo_l_m2):
    try:
        area_m2 = area_ha * 10000
        volume_ideal = area_m2 * consumo_l_m2
        diferenca = volume_utilizado - volume_ideal
        percentual = diferenca / volume_ideal * 100
        return percentual
    except Exception as e:
        raise Exception(f"Erro ao avaliar irrigação: {str(e)}")