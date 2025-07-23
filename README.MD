# API de Filmes (Full-Stack Backend)

## Visão Geral do Projeto

Este projeto consiste na construção de uma **API RESTful completa para gerenciamento de filmes**, desenvolvida utilizando **Python** com o poderoso framework **Django REST Framework (DRF)**. A API simula uma plataforma de catálogo e interação com filmes, atores, gêneros e avaliações, oferecendo todas as funcionalidades essenciais para um sistema robusto de backend.

O objetivo principal foi criar uma solução escalável e bem estruturada, demonstrando proficiência em desenvolvimento de APIs, autenticação de usuários e manipulação de dados.

## Funcionalidades Principais

* **Gerenciamento Completo (CRUD):**
    * **Gêneros:** Criação, Leitura, Atualização e Exclusão de gêneros de filmes.
    * **Filmes:** Criação, Leitura, Atualização e Exclusão de informações de filmes (título, ano, gênero, etc.).
    * **Atores:** Criação, Leitura, Atualização e Exclusão de dados de atores.
    * **Avaliações (Reviews):** Criação, Leitura, Atualização e Exclusão de avaliações de filmes.
* **Autenticação de Usuários:** Sistema seguro de autenticação baseado em **Token (JWT)** para proteger os endpoints da API.
* **Serializers:** Utilização de serializers do DRF para serialização e desserialização de dados, facilitando a interação entre a API e as aplicações cliente.
* **Versionamento de API:** Implementação de versionamento na URL (`api/v1/`) para garantir a compatibilidade futura e a evolução da API.
* **Estrutura Modular:** Código organizado em módulos e aplicações Django para facilitar a manutenção e escalabilidade.

## Tecnologias Utilizadas

* **Backend:**
    * Python
    * Django
    * Django REST Framework (DRF)
    * Simple JWT (para autenticação via Token)
    * Banco de Dados Relacional (SQLite por padrão, configurável para PostgreSQL, MySQL, etc.)
* **Controle de Versão:**
    * Git
    * GitHub

## Endpoints da API

A API é versionada sob `/api/v1/` e oferece os seguintes endpoints principais:

* **`api/v1/genres/`**
    * `GET /api/v1/genres/`: Lista todos os gêneros. (requer autenticação).
    * `POST /api/v1/genres/`: Cria um novo gênero (requer autenticação).
    * `GET /api/v1/genres/id/`: Retorna detalhes de um gênero específico.
    * `PUT /api/v1/genres/id/`: Atualiza um gênero existente (requer autenticação).
    * `DELETE /api/v1/genres/id/`: Exclui um gênero (requer autenticação).

* **`api/v1/movies/`**
    * `GET /api/v1/movies/`: Lista todos os filmes. (requer autenticação).
    * `GET /api/v1/movies/stats/`: Entregua uma visão gerão dos filmes. (requer autenticação).
    * `POST /api/v1/movies/`: Cria um novo filme (requer autenticação).
    * `GET /api/v1/movies/id/`: Retorna detalhes de um filme específico.
    * `PUT /api/v1/movies/id/`: Atualiza um filme existente (requer autenticação).
    * `DELETE /api/v1/movies/id/`: Exclui um filme (requer autenticação).

* **`api/v1/actors/`**
    * `GET /api/v1/actors`: Lista todos os atores.(requer autenticação)
    * `POST /api/v1/actors`: Cria um novo ator (requer autenticação).
    * `GET /api/v1/actors/id`: Retorna detalhes de um ator específico.
    * `PUT /api/v1/actors/id`: Atualiza um ator existente (requer autenticação).
    * `DELETE /api/v1/actors/id`: Exclui um ator (requer autenticação).

* **`api/v1/reviews/`**
    * `GET /api/v1/reviews/`: Lista todas as avaliações. (requer autenticação).
    * `POST /api/v1/reviews/`: Cria uma nova avaliação. (requer autenticação).
    * `GET /api/v1/reviews/id/`: Retorna detalhes de uma avaliação específica. (requer autenticação).
    * `PUT /api/v1/reviews/id/`: Atualiza uma avaliação existente (requer autenticação).
    * `DELETE /api/v1/reviews/id/`: Exclui uma avaliação (requer autenticação).

* **Autenticação (Exemplo):**
    * `POST /api/v1/authentication/token/`: Obtém um token de acesso para um usuário.
    * `POST /api/v1/authentication/token/refresh/`: Atualiza um token de acesso.
    * `POST /api/v1/authentication/token/verify/`: Verifica o status de seu token.

## Comandos Personalizados

Além dos comandos padrão do Django, esta API inclui um comando personalizado para facilitar a importação de dados iniciais:

* **`import_actors`**: Importa nomes de atores a partir de um arquivo CSV.
    * **Uso:** `python manage.py import_actors <nome_do_arquivo.csv>`
    * **Exemplo:** `python manage.py import_actors actors.csv`
    * **Detalhes:** Espera um arquivo CSV (ex: `actors.csv` na pasta do projeto) contendo uma lista de 20 nomes de atores, um por linha. Este comando automatiza a criação de registros de atores no banco de dados.