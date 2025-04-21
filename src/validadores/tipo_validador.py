"""
validar_string:
    Valida se o valor fornecido é uma string.
Args:
    valor: O valor a ser validado
Returns:
    bool: True se o valor for uma string, False caso contrário
"""
def validar_string(valor):
    try:
        return isinstance(valor, str)
    except Exception as e:
        print(f"Erro ao validar string: {str(e)}")
        return False

"""
validar_inteiro:
    Valida se o valor fornecido é um número inteiro.
Args:
    valor: O valor a ser validado
Returns:
    bool: True se o valor for um inteiro, False caso contrário
"""
def validar_inteiro(valor):
    try:
        return isinstance(valor, int)
    except Exception as e:
        print(f"Erro ao validar inteiro: {str(e)}")
        return False

"""
validar_decimal:
    Valida se o valor fornecido é um número decimal (float).
Args:
    valor: O valor a ser validado
Returns:
    bool: True se o valor for um decimal, False caso contrário
"""
def validar_decimal(valor):
    try:
        return isinstance(valor, float)
    except Exception as e:
        print(f"Erro ao validar decimal: {str(e)}")
        return False

"""
validar_booleano:
    Valida se o valor fornecido é um booleano.
Args:
    valor: O valor a ser validado
Returns:
    bool: True se o valor for um booleano, False caso contrário
"""
def validar_booleano(valor):
    try:
        return isinstance(valor, bool)
    except Exception as e:
        print(f"Erro ao validar booleano: {str(e)}")
        return False

"""
validar_lista:
    Valida se o valor fornecido é uma lista.
Args:
    valor: O valor a ser validado
Returns:
    bool: True se o valor for uma lista, False caso contrário
"""
def validar_lista(valor):
    try:
        return isinstance(valor, list)
    except Exception as e:
        print(f"Erro ao validar lista: {str(e)}")
        return False