import os
from controladores.logs_controlador import ler_logs

def exibir_menu():
    print('\n=== Menu de Logs ===\n')
    print('1. Visualizar todos os logs')
    print('0. Voltar')
    print('\nEscolha uma opção: ', end='')

def visualizar_logs():
    try:
        print('\n=== Logs do Sistema ===\n')
        logs = ler_logs()
        if logs is None:
            print('Nenhum log encontrado.')
            return
        for log in logs:
            print(log.strip())
    except Exception as e:
        print(f'\nErro ao ler logs: {str(e)}')

def menu_logs():
    while True:
        try:
            os.system('cls')
            exibir_menu()
            opcao = input().strip()
            match opcao:
                case '1':
                    os.system('cls')
                    visualizar_logs()
                case '0':
                    print('\nSaindo do menu de logs...')
                    break
                case _:
                    print('\nOpção inválida!')
        except Exception as e:
            os.system("cls")
            print(f'\nERRO')
            print(f'\n\033[31m{str(e)}\033[0m')
        finally:
            input("\nPressione ENTER")