# Vibbra Project

Controle de NF Freelancer

## Summary

* [Apresentação](#apresentação)
* [Objetivos do projeto](#Objetivos-do-Projeto)
* [Público alvo](#Público-Alvo)
* [Requisitos](#Requisitos)
  * [Módulo de Usuário](#Módulo-de-Usuário)
  * [Módulo de Autenticação](#Módulo-de-Autenticação)
  * [Módulo de Empresas Parceiras](#Módulo-de-Empresas-Parceiras)
  * [Módulo de Receita](#Módulo-de-Receita)
  * [Módulo de Despesas](#Módulo-de-Despesas)
  * [Módulo de Relatórios](#Módulo-de-Relatórios)
* [Planejamento de Sprint](#Planejamento-de-Sprint)
  * [Sprint 1](#Sprint-1)
  * [Sprint 2](#Sprint-2)
  * [Sprint 3](#Sprint-3)
  * [Sprint 4](#Sprint-4)
* [Usage](#Usage)
  * [Using Docker](#using-docker)
  * [Authentication](#Authentication)
  * [Running tests](#running-tests)
  * [Documentation](#documentation)
  * [Video Demonstration](#video-demonstration)

## Apresentação

Emitir nota fiscal eletrônica é a melhor alternativa para garantir a legalidade do seu processo comercial, prevenir erros manuais, reduzir custos e, principalmente, garantir a segurança das informaçōes emitidas e um maior controle financeiro do seu negócio.

Emita as suas notas fiscais em poucos cliques, diretamente do pedido de venda e integradas com os dados do cliente, estoque e fluxo de caixa, para você não perder nenhum detalhe.

### Objetivos do Projeto

O projeto possui objetivo de desenvolver uma aplicação o qual resolva os problemas acima mencionados de forma com que o empreededor possa cadastrar suas receitas e emitir suas NF.

### Público Alvo

Empreendedores formalizados como Microempreendedores Individuais que buscam uma forma automática de organizar suas Receitas (geração de Notas Fiscais) para evitar surpresas com pagamento de impostos ao final do ano.

### Requisitos

#### Módulo de Usuário

- O sistema deve permitir a adição, removação, edição e recuperação de um usuário.

#### Módulo de Autenticação

- O sistema deve permitir com que o usuário efetue login para utilizar as rotas (endpoint) privadas da API.

#### Módulo de Empresas Parceiras

- O sistema deve permitir com que o usuário faça a adição, removação, recuperação e deleção de empresas parceiras.
- O sistema deve permitir com que o usuário consiga pesquisar a empresa parceira pelo nome e cnpj.

#### Módulo de Receita

- O sistema deve permitir com que o usuário faça a adição, removação, recuperação e deleção de receitas.
- O sistema deve permitir com que o usuário consiga vincular a receita a uma categoria de receita anteriormente cadastrada.

#### Módulo de Despesas

- O sistema deve permitir com que o usuário faça a adição, removação, recuperação e deleção de despesas.
- O sistema deve permitir com que o usuário consiga vincular a despesa a uma categoria de despesa anteriormente cadastrada. 

#### Módulo de Relatórios

- O sistema deve permitir com o que o usuário gere os seguintes relatórios:
  - Total de Receitas;
  - Total de Receitas agrupado por mês;
  - Total de Receitas agrupado por empresas parceiras.

### Planejamento de Sprint

#### Sprint 1
- Planned Effort: 15 working days
- Resumo:
  - Planejamento de escopo e cronograma 
  - Análise e levantamento de requisitos funcionais e não funcionais
  - Escolha arquitetural
  - Criação de diagrama de caso de uso
  - Criação de diagrama de entidade-relacionamento, modelagem e mapeamento
  - Configuração do ambiente de desenvolvimento

#### Sprint 2
- Planned Effort: 15 working days
- Resumo:
  - Módulo de Usuário e Autentifcação
  - Módulo de Empresas Parceiras

#### Sprint 3
- Planned Effort: 15 working days
- Resumo:
  - Módulo de Receitas e Despesas

#### Sprint 4
- Planned Effort: 15 working days
- Resumo:
  - Módulo de Relatórios
 
## Usage

### Using docker

Build images:

```bash
make build
```

Run container

```bash
make run
```

### Authentication

To access protected resources, you will need an access token. You can generate an access and a refresh token using `/auth/login` endpoint, example using curl

```bash
curl -X POST -H "Content-Type: application/json" -d '{"username": "admin", "password": "admin"}' http://localhost:5000/auth/login
```

This will return something like this

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzIiwiaWRlbnRpdHkiOjEsImlhdCI6MTUxMDAwMDQ0MSwiZnJlc2giOmZhbHNlLCJqdGkiOiI2OTg0MjZiYi00ZjJjLTQ5MWItYjE5YS0zZTEzYjU3MzFhMTYiLCJuYmYiOjE1MTAwMDA0NDEsImV4cCI6MTUxMDAwMTM0MX0.P-USaEIs35CSVKyEow5UeXWzTQTrrPS_YjVsltqi7N4", 
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGl0eSI6MSwiaWF0IjoxNTEwMDAwNDQxLCJ0eXBlIjoicmVmcmVzaCIsImp0aSI6IjRmMjgxOTQxLTlmMWYtNGNiNi05YmI1LWI1ZjZhMjRjMmU0ZSIsIm5iZiI6MTUxMDAwMDQ0MSwiZXhwIjoxNTEyNTkyNDQxfQ.SJPsFPgWpZqZpHTc4L5lG_4aEKXVVpLLSW1LO7g4iU0"
}
```
You can use access_token to access protected endpoints :

```bash
curl -X GET -H "Content-Type: application/json" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzIiwiaWRlbnRpdHkiOjEsImlhdCI6MTUxMDAwMDQ0MSwiZnJlc2giOmZhbHNlLCJqdGkiOiI2OTg0MjZiYi00ZjJjLTQ5MWItYjE5YS0zZTEzYjU3MzFhMTYiLCJuYmYiOjE1MTAwMDA0NDEsImV4cCI6MTUxMDAwMTM0MX0.P-USaEIs35CSVKyEow5UeXWzTQTrrPS_YjVsltqi7N4" http://127.0.0.1:5000/api/v1/users
```

You can use refresh token to retreive a new access_token using the endpoint `/auth/refresh`


```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGl0eSI6MSwiaWF0IjoxNTEwMDAwNDQxLCJ0eXBlIjoicmVmcmVzaCIsImp0aSI6IjRmMjgxOTQxLTlmMWYtNGNiNi05YmI1LWI1ZjZhMjRjMmU0ZSIsIm5iZiI6MTUxMDAwMDQ0MSwiZXhwIjoxNTEyNTkyNDQxfQ.SJPsFPgWpZqZpHTc4L5lG_4aEKXVVpLLSW1LO7g4iU0" http://127.0.0.1:5000/auth/refresh
```

This will only return a new access token

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzIiwiaWRlbnRpdHkiOjEsImlhdCI6MTUxMDAwMDYxOCwiZnJlc2giOmZhbHNlLCJqdGkiOiIzODcxMzg4Ni0zNGJjLTRhOWQtYmFlYS04MmZiNmQwZjEyNjAiLCJuYmYiOjE1MTAwMDA2MTgsImV4cCI6MTUxMDAwMTUxOH0.cHuNf-GxVFJnUZ_k9ycoMMb-zvZ10Y4qbrW8WkXdlpw"
}
```

### Running tests

#### Using tox

Simplest way to run tests is to use tox, it will create a virtualenv for tests, install all dependencies and run pytest

```bash
tox
```

### Documentation

* Swagger Documentation API (access this after run): http://0.0.0.0:5000/swagger-ui
* Postman Collection Helper: [Vibbra Postman Collection](postman/Vibbra.postman_collection.json)

### Video Demonstration

<a href="https://youtu.be/FizsRWTfjdk" target="_blank"><img src="https://www.nicepng.com/png/full/213-2131375_watch-now-button-png-food-waste-only-sign.png" width="180"></a>