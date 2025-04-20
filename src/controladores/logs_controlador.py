import os
from config.logs.log_config import registrar_log

def obter_caminho_arquivo_log():
    try:
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        return os.path.join(base_dir, 'src','config', 'logs', 'log.txt')
    except Exception as e:
        raise Exception(f'Erro ao obter caminho do arquivo de log: {str(e)}')

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