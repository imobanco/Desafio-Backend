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
- [x] - RF4.0 Dados da transferência
- [x] - RF4.1 Cadastro de Transferência
- [x] - RF4.2 Visualização de dados
- [x] - RF4.3 Atualização de dados
- [x] - RF4.4 Deleção de dados
- [x] - RF5.0 Dados do comentário
- [x] - RF5.1 Criação de comentário

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
- `POST /api/comment/` - Cria um comentario a partir de uma transferencia
