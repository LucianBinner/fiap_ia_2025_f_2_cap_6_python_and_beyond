import os
from datetime import datetime

"""
registrar_log:
    Registra uma entrada de log no arquivo de logs do sistema.
Args:
    repositorio (str): Nome do repositório onde a operação foi realizada
    operacao (str): Tipo de operação realizada (ex: criar, atualizar, deletar)
    status (str): Status da operação (ex: SUCESSO, ERRO)
    message (str): Mensagem detalhada sobre a operação
O log é salvo no formato:
    [YYYY-MM-DD HH:MM:SS] STATUS - REPOSITORIO - OPERACAO: MENSAGEM
Raises:
    Exception: Se houver erro ao escrever no arquivo de log
"""
def registrar_log(repositorio, operacao, status, message):
    try:
        log_dir = os.path.dirname(os.path.abspath(__file__))
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        log_file = os.path.join(log_dir, 'log.txt')
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = f"[{timestamp}] {status} - {repositorio} - {operacao}: {str(message)}\n"
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(log_message)
    except Exception as e:
        print(f"Erro ao registrar log: {str(e)}")