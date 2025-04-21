import os
from config.logs.log_config import registrar_log

"""
obter_caminho_arquivo_log:
    Obtém o caminho absoluto do arquivo de log do sistema.
Returns:
    str: Caminho absoluto para o arquivo de log
Raises:
    Exception: Se houver erro ao construir o caminho do arquivo
"""
def obter_caminho_arquivo_log():
    try:
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        return os.path.join(base_dir, 'src','config', 'logs', 'log.txt')
    except Exception as e:
        raise Exception(f'Erro ao obter caminho do arquivo de log: {str(e)}')

"""
ler_logs:
    Lê o conteúdo do arquivo de log do sistema.
Returns:
    list: Lista de linhas do arquivo de log, ou None se o arquivo estiver vazio ou não existir
Raises:
    Exception: Se houver erro na leitura do arquivo de log
"""
def ler_logs():
    try:
        log_file = obter_caminho_arquivo_log()
        if not os.path.exists(log_file):
            return None
        with open(log_file, 'r', encoding='utf-8') as f:
            logs = f.readlines()
            return logs if logs else None
    except Exception as e:
        raise Exception(f'Erro ao ler logs: {str(e)}')