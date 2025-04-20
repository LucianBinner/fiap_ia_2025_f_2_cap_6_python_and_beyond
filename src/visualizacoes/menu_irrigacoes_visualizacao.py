from controladores.irrigacao_controlador import pegar_irrigacoes, pegar_irrigacao_por_id, criar_irrigacao, atualizar_irrigacao_por_id, deletar_irrigacao_por_id
import os

def exibir_menu_principal():
    print('\n=== Menu Irrigação ===\n')
    print('1. Listar todas as irrigações')
    print('2. Buscar irrigação por ID')
    print('3. Criar nova irrigação')
    print('4. Atualizar irrigação')
    print('5. Deletar irrigação')
    print('0. Sair')
    print('\nEscolha uma opção: ', end='')

def menu_irrigacoes():
    while True:
        try:
            os.system("cls")
            exibir_menu_principal()
            opcao = input().strip()
            os.system("cls")
            match opcao:
                case '1':
                    print('\n=== Irrigações Cadastradas ===\n')
                    irrigacoes = pegar_irrigacoes()
                    print('\nIrrigações Encontradas\n')
                    print(irrigacoes)
                case '2':
                    print('\n=== Buscar Irrigação Por ID ===')
                    id = input('\nDigite o ID da irrigação: ')
                    irrigacao = pegar_irrigacao_por_id(id)
                    print('\nIrrigação Encontrada\n')
                    print("ID:", irrigacao['id'])
                    print("Plantio:", irrigacao['plantio'])
                    print("Data da irrigação:", irrigacao['data_irrigacao'])
                    print("Quantidade de água:", irrigacao['volume_agua_l'], "litros")
                    print("Feedback:", irrigacao['feedback'])
                    print("Dica:", irrigacao['dica'])
                case '3':
                    print('\n=== Registrar Irrigação ===')
                    plantio_id = input('\nDigite o ID do plantio: ')
                    data_irrigacao = input('\nDigite a data da irrigação (YYYY-MM-DD): ')
                    quantidade_agua = input('\nDigite a quantidade de água em litros: ')
                    irrigacao = criar_irrigacao(plantio_id, data_irrigacao, quantidade_agua)
                    print('\nIrrigação Criada com Sucesso!')
                    print('\nIrrigação criada:')
                    print("ID:", irrigacao['id'])
                    print("Plantio:", irrigacao['plantio'])
                    print("Data da irrigação:", irrigacao['data_irrigacao'])
                    print("Quantidade de água:", irrigacao['volume_agua_l'], "litros")
                    print("Feedback:", irrigacao['feedback'])
                    print("Dica:", irrigacao['dica'])

                case '4':
                    print('\n=== Alterar Irrigação ===')
                    id = input('\nDigite o ID da irrigação: ')
                    plantio_id = input('\nDigite o novo ID do plantio: ')
                    data_irrigacao = input('\nDigite a nova data da irrigação (YYYY-MM-DD): ')
                    quantidade_agua = input('\nDigite a nova quantidade de água em litros: ')
                    irrigacao = atualizar_irrigacao_por_id(id, plantio_id, data_irrigacao, quantidade_agua)
                    print('\nIrrigação atualizada com sucesso!')
                    print('\nIrrigação atualizada:')
                    print("ID:", irrigacao['id'])
                    print("Plantio:", irrigacao['plantio'])
                    print("Data da irrigação:", irrigacao['data_irrigacao'])
                    print("Quantidade de água:", irrigacao['volume_agua_l'], "litros")
                    print("Feedback:", irrigacao['feedback'])
                    print("Dica:", irrigacao['dica'])
                case '5':
                    print('\n=== Deletar Irrigação ===')
                    id = input('\nDigite o ID da irrigação: ')
                    deletar_irrigacao_por_id(id)
                    print('\nIrrigação deletada com sucesso!')
                case '0':
                    print('\nSaindo do menu de irrigações...')
                    break
                case _:
                    raise Exception("Opção inválida!")
        except Exception as e:
            os.system("cls")
            print(f'\nERRO')
            print(f'\n\033[31m{str(e)}\033[0m')
        finally:
            input("\nPressione ENTER")