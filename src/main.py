from visualizacoes.menu_areas_visualizacao import menu_areas
from visualizacoes.menu_culturas_visualizacao import menu_culturas
from visualizacoes.menu_plantios_visualizacao import menu_plantios
from visualizacoes.menu_irrigacoes_visualizacao import menu_irrigacoes
from visualizacoes.menu_feedback_visualizacao import menu_feedbacks
from visualizacoes.menu_logs_visualizacao import menu_logs
import os

def exibir_menu():
    print('\n=== Sistema Gestão Hídrica ===')
    print('\n=== Menu Principal ===\n')
    print('1. Áreas')
    print('2. Culturas')
    print('3. Plantios')
    print('4. Irrigações')
    print('5. Feedbacks')
    print('6. Logs dos Sistema')
    print('7. Sobre o Sistema')
    print('0. Sair')
    print('\nEscolha uma opção: ', end='')

def main():
    while True:
        try:
            os.system("cls")
            exibir_menu()
            opcao = input().strip()
            match opcao:
                case '1':
                    menu_areas()
                case '2':
                    menu_culturas()
                case '3':
                    menu_plantios()
                case '4':
                    menu_irrigacoes()
                case '5':
                    menu_feedbacks()
                case '6':
                    menu_logs()
                case '7':
                    os.system("cls")
                    print('\n=== Sobre o Sistema ===')
                    print('\nEste é um sistema de gestão hídrica desenvolvido para facilitar o controle e a monitorização das irrigações de culturas.')
                    print('O sistema permite cadastrar áreas, culturas, plantios, irrigações e feedbacks.')
                    print('O sistema foi desenvolvido com o intuito de ajudar os agricultores a controlarem suas irrigações e a melhorarem a qualidade da água.')
                    print('O sistema tem com principal objetivo ajudar na economia hídrica, pois este é um dos grandes vilões no mercado agricultor, assim preserva-se o meio ambiente e ajuda o setor economicamente.')
                    input("\nPressione ENTER")
                case '0':
                    print('\nSaindo do sistema...')
                    break
                case _:
                    os.system("cls")
                    print('\nOpção inválida!')
                    print('\nPor favor, escolha uma opção válida.')
                    input("\nPressione ENTER")
        except Exception as e:
            print(f'\nErro: {str(e)}')
            print('Por favor, tente novamente.')

main()