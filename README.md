# API de Gerenciamento de Loja de Comidas

Esta é uma API desenvolvida para facilitar o gerenciamento de uma loja de comidas. Ela oferece uma série de funcionalidades para verificar a existência de produtos no menu, listar alimentos por categoria, calcular o gasto total de uma mesa e muito mais.

## Requisitos

A aplicação deve atender aos seguintes requisitos:

- Verificar a existência de um produto no menu.
- Listar alimentos de uma categoria específica.
- Calcular o gasto total de uma mesa.
- Adicionar um novo produto ao menu.
- Remover um produto do menu.
- Atualizar informações de um produto no menu.
- Registrar um pedido de um cliente.
- Listar todos os pedidos realizados.
- Calcular o total de vendas de um período específico.
- Gerar relatórios de vendas.

## Instalação

Siga as instruções abaixo para configurar e executar a API:

1. Certifique-se de ter o Python 3 instalado em seu ambiente.
2. Clone o repositório do projeto: `git clone https://github.com/seu-usuario/api-loja-de-comidas.git`
3. Navegue até o diretório do projeto: `cd api-loja-de-comidas`
4. Instale as dependências usando o gerenciador de pacotes do Python: `pip install -r requirements.txt`
5. Execute o arquivo `main.py` para iniciar a aplicação.

## Uso

A API é acessada através de endpoints HTTP e retorna respostas em formato JSON. Abaixo estão listados os endpoints disponíveis:

- **GET /menu/{produto}**: Verifica a existência de um produto no menu. Substitua `{produto}` pelo nome do produto desejado. Retorna um objeto JSON contendo informações sobre o produto, caso ele exista, ou uma mensagem de erro, caso contrário.

- **GET /menu/categoria/{categoria}**: Lista alimentos de uma categoria específica. Substitua `{categoria}` pela categoria desejada. Retorna um objeto JSON contendo uma lista de alimentos da categoria informada.

- **GET /mesa/{mesa}/gasto**: Calcula o gasto total de uma mesa. Substitua `{mesa}` pelo número da mesa desejada. Retorna um objeto JSON contendo o valor total gasto na mesa.

- **POST /menu**: Adiciona um novo produto ao menu. O corpo da requisição deve conter as informações do novo produto em formato JSON. Retorna um objeto JSON contendo as informações do produto adicionado.

- **DELETE /menu/{produto}**: Remove um produto do menu. Substitua `{produto}` pelo nome do produto a ser removido. Retorna uma mensagem de sucesso ou erro.

- **PUT /menu/{produto}**: Atualiza as informações de um produto no menu. Substitua `{produto}` pelo nome do produto a ser atualizado. O corpo da requisição deve conter as novas informações do produto em formato JSON. Retorna um objeto JSON contendo as informações do produto atualizado.

- **POST /pedido**: Registra um novo pedido de um cliente. O corpo da requisição deve conter as informações do pedido em formato JSON. Retorna um objeto JSON contendo as informações do pedido registrado.

- **GET /pedidos**: Lista todos os pedidos realizados. Retorna um objeto JSON contendo uma lista de todos os pedidos.

- **GET /vendas/{data_inicial}/{data_final}**: Calcula o total de vendas em um período específico. Substitua `{data_inicial}` e `{data_final}` pelas datas inicial e final do período desejado, respectivamente, no formato "AAAA-MM-DD". Retorna um objeto JSON contendo o valor total de vendas no período.

- **GET /relatorios/vendas**: Gera relatórios de vendas. Retorna um arquivo PDF contendo os relatórios de vendas.

## Contribuição

Se desejar contribuir para este projeto, siga as etapas abaixo:

1. Faça um fork do repositório.
2. Crie uma nova branch com sua contribuição: `git checkout -b minha-contribuicao`
3. Faça as alterações desejadas e faça commit das mesmas: `git commit -am 'Minha contribuição'`
4. Envie suas alterações para o seu fork: `git push origin minha-contribuicao`
5. Abra um pull request no repositório original, descrevendo suas alterações.


