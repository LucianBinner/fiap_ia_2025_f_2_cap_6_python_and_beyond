from validadores.tipo_validador import validar_string, validar_decimal

"""
validar_id_area: 
    Valida o ID de uma área.
Args:
    id (str): ID da área a ser validado
Returns:
    None
Raises:
    Exception: Se o ID for inválido (vazio, muito longo ou não numérico)
"""
def validar_id_area(id: str) -> None:
    try:
        int(id)
        if not id.strip() or len(id.strip()) > 50:
            raise ValueError()
    except ValueError:
        raise Exception("ID inválido!")

"""
validar_pegar_area_por_id:
    Valida o ID para busca de uma área.
Args:
    id (str): ID da área a ser validado
Returns:
    None
Raises:
    Exception: Se o ID for inválido
"""
def validar_pegar_area_por_id(id: str) -> None:
    validar_id_area(id)

"""
validar_criar_area:
    Valida os dados para criação de uma nova área.
Args:
    nome (str): Nome da área
    localizacao (str): Localização da área
    hectar_input (str): Tamanho da área em hectares (será convertido para float)
Returns:
    None
Raises:
    Exception: Se algum dos campos for inválido
"""
def validar_criar_area(nome: str, localizacao: str, hectar_input: str) -> None:
    if not validar_string(nome) or not nome.strip():
        raise Exception("O nome da área não pode estar vazio")
    if not validar_string(localizacao) or not localizacao.strip():
        raise Exception("A localização da área não pode estar vazia")
    if not hectar_input.strip():
        raise Exception("O tamanho em hectares não pode estar vazio")
    try:
        hectar = float(hectar_input)
        if not validar_decimal(hectar) or hectar <= 0:
            raise Exception("O tamanho em hectares deve ser um número positivo")
    except ValueError:
        raise Exception("O tamanho em hectares deve ser um número válido")

"""
validar_atualizar_area:
    Valida os dados para atualização de uma área existente.
Args:
    id (str): ID da área
    nome (str): Novo nome da área
    localizacao (str): Nova localização da área
    hectar_input (str): Novo tamanho da área em hectares (será convertido para float)
Returns:
    None
Raises:
    Exception: Se algum dos campos for inválido
"""
def validar_atualizar_area(id: str, nome: str, localizacao: str, hectar_input: str) -> None:
    validar_id_area(id)
    if not validar_string(nome) or not nome.strip():
        raise Exception("O nome da área não pode estar vazio")
    if not validar_string(localizacao) or not localizacao.strip():
        raise Exception("A localização da área não pode estar vazia")
    if not hectar_input.strip():
        raise Exception("O tamanho em hectares não pode estar vazio")
    try:
        hectar = float(hectar_input)
        if not validar_decimal(hectar) or hectar <= 0:
            raise Exception("O tamanho em hectares deve ser um número positivo")
    except ValueError:
        raise Exception("O tamanho em hectares deve ser um número válido")

"""
validar_deletar_area:
    Valida o ID para remoção de uma área.
Args:
    id (str): ID da área a ser removida
Returns:
    None
Raises:
    Exception: Se o ID for inválido
"""
def validar_deletar_area(id: str) -> None:
    validar_id_area(id)