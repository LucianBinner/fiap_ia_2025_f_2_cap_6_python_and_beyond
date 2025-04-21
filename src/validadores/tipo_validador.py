"""
validar_string:
    Valida se o valor fornecido é uma string.
Args:
    valor: O valor a ser validado
Returns:
    bool: True se o valor for uma string, False caso contrário
"""
def validar_string(valor):
    return isinstance(valor, str)

"""
validar_inteiro:
    Valida se o valor fornecido é um número inteiro.
Args:
    valor: O valor a ser validado
Returns:
    bool: True se o valor for um inteiro, False caso contrário
"""
def validar_inteiro(valor):
    return isinstance(valor, int)

"""
validar_decimal:
    Valida se o valor fornecido é um número decimal (float).
Args:
    valor: O valor a ser validado
Returns:
    bool: True se o valor for um decimal, False caso contrário
"""
def validar_decimal(valor):
    return isinstance(valor, float)

"""
validar_booleano:
    Valida se o valor fornecido é um booleano.
Args:
    valor: O valor a ser validado
Returns:
    bool: True se o valor for um booleano, False caso contrário
"""
def validar_booleano(valor):
    return isinstance(valor, bool)

"""
validar_lista:
    Valida se o valor fornecido é uma lista.
Args:
    valor: O valor a ser validado
Returns:
    bool: True se o valor for uma lista, False caso contrário
"""
def validar_lista(valor):
    return isinstance(valor, list)