from controladores.plantio_controlador import pegar_plantios, pegar_plantio_por_id, criar_plantio, atualizar_plantio_por_id, deletar_plantio_por_id
import os

def exibir_menu_principal():
    print('\n=== Menu Plantio ===\n')
    print('1. Listar todos os plantios')
    print('2. Buscar plantio por ID')
    print('3. Criar novo plantio')
    print('4. Atualizar plantio')
    print('5. Deletar plantio')
    print('0. Sair')
    print('\nEscolha uma opção: ', end='')

def menu_plantios():
    while True:
        try:
            os.system("cls")
            exibir_menu_principal()
            opcao = input().strip()
            os.system("cls")
            match opcao:
                case '1':
                    print('\n=== Plantios Cadastradas ===\n')
                    plantios = pegar_plantios()
                    print('\nPlantios Encontradas\n')
                    print(plantios)
                case '2':
                    print('\n=== Buscar Plantio ===')
                    id = input('\nDigite o ID do plantio: ')
                    plantio = pegar_plantio_por_id(id)
                    print('\nPlantio Encontrado\n')
                    print("ID:", plantio['id'])
                    print("Nome:", plantio['nome'])
                    print("Observação:", plantio['observacao'])
                    print("Área:", plantio['area'])
                    print("Cultura:", plantio['cultura'])
                case '3':
                    print('\n=== Cadastrar Novo Plantio ===')
                    nome = input('\nDigite o nome do plantio: ')
                    observacao = input('\nDigite a observação do plantio: ')
                    area_id = input('\nDigite o ID da área: ')
                    cultura_id = input('\nDigite o ID da cultura: ')
                    data_plantio = input('\nDigite a data do plantio (YYYY-MM-DD): ')
                    plantio = criar_plantio(nome, observacao, area_id, cultura_id, data_plantio)
                    print('\nPlantio Criado com Sucesso!')
                    print('\nPlantio criado:')
                    print("ID:", plantio['id'])
                    print("Nome:", plantio['nome'])
                    print("Observação:", plantio['observacao'])
                    print("Área:", plantio['area'])
                case '4':
                    print('\n=== Alterar Plantio ===')
                    id = input('\nDigite o ID do plantio: ')
                    nome = input('\nDigite o novo nome do plantio: ')
                    observacao = input('\nDigite a nova observação do plantio: ')
                    area_id = input('\nDigite o novo ID da área: ')
                    cultura_id = input('\nDigite o novo ID da cultura: ')
                    data_plantio = input('\nDigite a nova data do plantio (YYYY-MM-DD): ')
                    plantio = atualizar_plantio_por_id(id, nome, observacao, area_id, cultura_id, data_plantio)
                    print('\nPlantio atualizado com sucesso!')
                    print('\nPlantio atualizado:')
                    print("ID:", plantio['id'])
                    print("Nome:", plantio['nome'])
                    print("Observação:", plantio['observacao'])
                    print("Área:", plantio['area'])
                case '5':
                    print('\n=== Deletar Plantio ===')
                    id = input('\nDigite o ID do plantio: ')
                    deletar_plantio_por_id(id)
                    print('\nPlantio Deletado com sucesso!')
                case '0':
                    print('\nSaindo do menu de plantios...')
                    break
                case _:
                    raise Exception("Opção inválida!")
        except Exception as e:
            os.system("cls")
            print(f'\nERRO')
            print(f'\n\033[31m{str(e)}\033[0m')
        finally:
            input("\nPressione ENTER")