import os
from datetime import datetime

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