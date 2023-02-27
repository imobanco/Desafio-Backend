# API BANCO - DDD

## Considerações sobre o projeto

- Todos ou sua grande maioria de requisitos do desafio foram atendidas
- O projeto foi dockerizado por completo.
- No campo dos padrões de projeto, foi adicionado o pre-commit, onde garantiremos uma melhor padronização do nosso código. Isso tudo antes de enviarmos para nosso repositório remoto.
  - Foi adicionado o Makefile, onde teremos uma maior agilidade em executarmos alguns comandos.

## Comandos pelo Makefile

| email do usuário | senha |
| ---------------- | ----- |
| admin@com.br     | 123   |

## Como utilizar o projeto

> ⚠ **Atenção**
>
> É necessário ter o docker e o docker compose instalados em seu computador.

```bash
# Clone o repositorio
$ git clone https://github.com/peidrao/Desafio-Backend.git
# entre no diretorio
$ cd Desafio-Backend
# Instalando projeto
$ make run
# Vendo se o projeto fez o start
$ make logs
# Criacao de migracoes no banco de dados
$ make migrate
```

## Criando usuário administrador

```bash
# Para criar super usuario
$ make admin
```

As credenciais do usuário administrador são:

| comando       | funcionalidade                                  |
| ------------- | ----------------------------------------------- |
| make run      | Iniciar projeto                                 |
| make bash     | Abrir terminal do projeto                       |
| make make     | Criar arquivos de migracao                      |
| make migrate  | Criar migracoes no banco de dados               |
| make admin    | Criar super usuario                             |
| make test     | Rodar os testes unitarios                       |
| make coverage | Rodar testes para gerar relatorios de cobertura |
| make html     | Gerar arquivos de cobertura de teste            |
| make logs     | Visualizar logs da aplicacao                    |

## Testes unitários

O projeto tem cobertura de 93%, ou seja, para quase todo código existem testes unitários

```bash
# Rodar os testes
$ make test
# Verificar cobertura
$ make coverage
# Gerar arquivos html
$ make html
```

> ⚠ **Atenção**
>
> O make html irá gerar um diretório dentro do nosso projeto chamado **htmlcov**. Dentro dele existem vários arquivos html, e entre eles o **index.html**, basta abrir o mesmo no navegador e teremos a porcentagem mais arquivos que estão cobertos.

## Requisitos

- [x] - RF1.1 Cadastro de usuário
- [ ] - RF1.2 Visualização de dados - Falta escrever a regra para ver somente o nome completo de outros usuarios
- [x] - RF1.3 Atualização de dados
- [x] - RF2.0 Dados da conta digital
- [x] - RF2.1 Cadastro de conta digital
- [x] - RF2.2 Visualização de dados
- [x] - RF2.3 Atualização de dados
- [x] - RF2.4 Deleção de dados
- [x] - RF3.0 Dados do depósito
- [x] - RF3.1 Cadastro de depósito
- [x] - RF3.2 Visualização de dados
- [x] - RF3.3 Atualização de dados
- [x] - RF3.4 Deleção de dados
- [x] - RF4.0 Dados da transferência
- [x] - RF4.1 Cadastro de Transferência
- [x] - RF4.2 Visualização de dados
- [x] - RF4.3 Atualização de dados
- [x] - RF4.4 Deleção de dados
- [x] - RF5.0 Dados do comentário
- [x] - RF5.1 Criação de comentário
- [x] - RF5.2 Visualização de dados
- [x] - RF5.3 Atualização de dados
- [x] - RF5.4 Deleção de dados

## Endpoints

- `POST /api/users/` - Criar um novo usuario
- `GET /api/users/{id_user}/` - Informacoes de um usuario especifico
- `GET /api/users/me/` - Todas as informacoes de um usuario logado
- `PATCH /api/users/me/` - Atualiza informacoes do usuario logado
- `GET /api/account/me/` - Visualizar informacoes da conta do usuario logado
- `POST /api/deposit/` - Criar deposito para o usuario logado
- `GET /api/deposit/` - Lista todos os depositos do usuario logado
- `POST /api/transfer/` - Cria uma tranferencia para outro usuario
- `GET /api/transfer/` - Lista todas as transfencias relacionadadas a um usuario logado, sejam enviadas ou recebidas
- `GET /api/transfer/public/` - Lista todas as transfencias que nao publicas
- `PATCH /api/transfer/{id_tranfer}/` - Atualiza informacoes de uma transferencia publica
- `DELETE /api/transfer/{id_tranfer}/` - Remove transferencia
- `POST /api/comment/` - Cria um comentario a partir de uma transferencia | Falta validacao para verificar se transferencia eh publica.
- `GET /api/comment/` - Listagem dos comentarios do usuario logado
- `GET /api/comment/{id_comment}` - Visualizar comentario pelo id
- `PATCH /api/comment/{id_comment}` - Atualiza informacoes de comentarios
