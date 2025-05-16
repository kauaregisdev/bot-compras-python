# Bot de automação de compras

Bem-vindo! Este é o repositório de um projeto de bot de automação de compras no site da Growth Supplements.
Utilizei Selenium para interagir com o site, e estou trabalhando na interface com o uso de Django.

## Status:
Em desenvolvimento. Atualmente, o código está dando erro em partes específicas, como por exemplo na seleção dos sabores de whey e pré-treino, bem como na checagem de e-mails, e a interface está sendo criada.

## Pré-requisitos:
Python 3.13
Google Chrome 136 + Chromedriver
Ambiente virtual (recomendado)

## Arquivos necessários para usar o código:
Chromedriver: https://storage.googleapis.com/chrome-for-testing-public/136.0.7103.49/win64/chromedriver-win64.zip
Para baixar as dependências necessárias: pip install -r requirements.txt

## Como executar o código:
1. clone o repositório, executando no terminal os seguintes comandos:
git clone https://github.com/kauaregisdev/bot-compras-python.git
cd bot-compras-python

2. crie e ative o ambiente virtual, com os comandos:
python -m venv venv
venv\Scripts\activate
OBSERVAÇÃO: caso haja uma pasta venv/ nos arquivos do projeto, delete-a antes de criar um novo ambiente virtual!

3. instale as dependências pelo terminal, com o comando:
pip install -r requirements.txt

4. baixe e configure o chromedriver, cujo link está acima neste texto
você deve colocá-lo no mesmo diretório do script (bot/scripts)

5. execute o bot no terminal, com o comando:
python main.py

AVISO: A execução em Django não está funcionando ainda!

## Observações importantes:
1. O bot utiliza Selenium para interagir com o site
2. O projeto não está 100% ainda, pois falta configurar a escolha dos sabores quando for preciso, bem como a validação dos e-mails