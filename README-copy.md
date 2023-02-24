#

Instalado
Django
Django rest framework
psycopg2 - engine para utilizar o postgres
simple jwt - para autenticacao via jwt

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

## Endpoints

- `POST /api/users/` - Criar um novo usuario
- `GET /api/users/{id_user}/` - Informacoes de um usuario especifico
- `GET /api/users/me/` - Todas as informacoes de um usuario logado
- `PATCH /api/users/me/` - Atualiza informacoes do usuario logado
- `GET /api/account/me/` - Visualizar informacoes da conta do usuario logado
- `POST /api/deposit/` - Criar deposito para o usuario logado
- `GET /api/deposit/` - Lista todos os depositos do usuario logado
