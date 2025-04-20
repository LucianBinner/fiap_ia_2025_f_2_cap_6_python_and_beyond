# Sistema de Gestão Hídrica

## Como Executar o Sistema

### Requisitos
- Python 3.10 ou superior
- Bibliotecas necessárias:
  - os (biblioteca padrão)

### Instalação e Execução
1. Clone o repositório
   ```
   git clone URL_ADDRESS.com/yourusername/sistema-gestao-hidrica.git
   ```
2. Navegue até a pasta do raiz do projeto
3. Execute o sistema através do comando:
   ```
   python src/main.py
   ```

## Descrição do Sistema

O Sistema de Gestão Hídrica é uma solução completa para o gerenciamento eficiente de recursos hídricos na agricultura. Desenvolvido para enfrentar os desafios da irrigação agrícola moderna, o sistema resolve problemas críticos como:

- Desperdício de água na irrigação através do monitoramento preciso do consumo.
- Dificuldade no controle de múltiplas áreas de cultivo e diferentes espécies.
- Falta de dados para tomada de decisão sobre irrigação
- Ausência de histórico e acompanhamento do desenvolvimento das culturas.

Através de um conjunto integrado de funcionalidades, o sistema permite o cadastro e monitoramento de áreas de cultivo, gestão de diferentes culturas, controle de ciclos de plantio, programação de irrigações e acompanhamento do desenvolvimento das plantas através de feedbacks. Todas as operações são registradas em logs, possibilitando análises detalhadas e melhorias contínuas no processo de irrigação.

## Como Utilizar o Sistema

### Menu Principal
O sistema possui os seguintes menus:

1. **Áreas** - Gerenciamento de áreas de cultivo e suas características
   - Listar todas as áreas - Visualiza todas as áreas cadastradas
   - Buscar área por ID - Localiza uma área específica
   - Criar nova área - Cadastra uma nova área de cultivo
   - Atualizar área - Modifica informações de uma área existente
   - Deletar área - Remove uma área do sistema

2. **Culturas** - Cadastro e controle das espécies cultivadas
   - Listar todas as culturas - Exibe todas as culturas cadastradas
   - Buscar cultura por ID - Encontra uma cultura específica
   - Criar nova cultura - Adiciona uma nova espécie de cultura
   - Atualizar cultura - Altera dados de uma cultura existente
   - Deletar cultura - Remove uma cultura do sistema

3. **Plantios** - Gestão dos ciclos de plantio em cada área
   - Listar todos os plantios - Mostra todos os plantios ativos
   - Buscar plantio por ID - Localiza um plantio específico
   - Criar novo plantio - Inicia um novo ciclo de plantio
   - Atualizar plantio - Atualiza informações do plantio
   - Deletar plantio - Encerra um ciclo de plantio

4. **Irrigações** - Controle do sistema de irrigação
   - Listar todas as irrigações - Visualiza histórico de irrigações
   - Buscar irrigação por ID - Encontra uma irrigação específica
   - Criar nova irrigação - Registra nova operação de irrigação
   - Atualizar irrigação - Modifica dados de uma irrigação
   - Deletar irrigação - Remove um registro de irrigação

5. **Feedbacks** - Avaliação e acompanhamento das culturas
   - Listar todos os feedbacks - Exibe todas as avaliações
   - Buscar feedback por ID - Localiza uma avaliação específica
   - Criar novo feedback - Registra nova avaliação
   - Atualizar feedback - Modifica uma avaliação existente
   - Deletar feedback - Remove uma avaliação do sistema

6. **Logs do Sistema** - Registro de atividades do sistema
   - Visualizar logs do sistema - Acompanha todas as operações realizadas

7. **Sobre o Sistema** - Detalhes e documentação
   - Informações sobre o sistema de gestão hídrica - Consulta dados gerais do sistema

### Navegação
- Use os números correspondentes para navegar entre os menus
- Digite '0' para voltar ao menu anterior ou sair do sistema
- Siga as instruções na tela para inserir os dados solicitados
- Pressione ENTER após cada operação para continuar

### Observações
- O sistema limpa a tela automaticamente para melhor visualização
- Mensagens de erro são exibidas em vermelho
- Todas as operações são confirmadas com mensagens de sucesso