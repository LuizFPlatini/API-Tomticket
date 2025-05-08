# 🎫 TomTicket Viewer - Flask App
Aplicação web simples desenvolvida em Python + Flask que permite a consulta e filtragem de chamados do sistema TomTicket via API, com uma interface moderna usando Bootstrap.

# Foto da interface
![Foto Tomticket](https://github.com/user-attachments/assets/12863432-2db2-4208-909d-8412575ec7b5)


# 🚀 Funcionalidades

* Consulta automática de chamados da API do TomTicket.
* Filtros por categoria, atendente e prioridade.
* Exibição em tabela responsiva com Bootstrap.
* Interface com sidebar fixa e visual limpo.
* Rota /api/chamados para consumir os dados diretamente em JSON.

# ⚙️ Requisitos

## Python 3.10 ou superior, e bibliotecas necessárias:
* Flask
* requests

## Instale os requisitos com:
* pip install flask requests

# 🔧 Configuração

## Insira o seu token da API TomTicket no app.py, na linha:
* TOKEN = 'Seu Token do TomTicket aqui'

## A URL base da API é montada automaticamente:
* API_URL = f'https://api.tomticket.com/chamados/{TOKEN}/'

# ▶️ Como Executar

## No terminal, estando dentro da pasta Tomticket, execute:

* python app.py

## A aplicação estará acessível em:
* http://127.0.0.1:5000/

## 🌐 Rotas Disponíveis "/" – Página principal

* Interface web com filtro e visualização de chamados.
   
## Parâmetros de filtro aceitos na URL:

* categoria: texto parcial ou completo da categoria
* atendente: nome ou parte do nome do atendente
* prioridade: "Baixa", "Média", "Alta" ou "Urgente"

## Exemplo de URL com filtro:
* http://127.0.0.1:5000/?categoria=Suporte&prioridade=Alta

## "/api/chamados" – API JSON
* Retorna os chamados diretamente da API TomTicket em formato JSON.
