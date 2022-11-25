![Imobanco](https://avatars.githubusercontent.com/u/49695163?s=200&v=4)

# Desafio para Backend Imobanco

Esse é um repositório contendo um projeto de desafio para o onboarding na equipe de backend do Imobanco!

Agradecemos seu interesse em trabalhar conosco 😁

# Instruções iniciais
## O que esperamos de seu código/projeto
- boa organização
- boa legibilidade
- boa qualidade
- reprodutibilidade e assertividade na implementação
- commits organizados são bem vistos
- boa documentação (readme's, docstrings, comentários em código quando for necessário)

## Como fazer o desafio
Fazer um fork desse repositório e seguir sua implementação. Ao final, abrir um PR do seu fork para esse repositório solicitando revisão. Isso facilitará a análise do código, nos permitindo fazer um feedback e questionamento técnico sobre implementações específicas.

Lembre-se, o processo de desenvolvimento é tão importante quanto a entrega do projeto em si!

# Domínio do Projeto/Aplicação

O projeto consistirá em uma API REST HTTP a ser utilizada por um frontend (web/mobile).

A aplicação está inserida no domínio de Contas Digitais do mundo financeiro. Nela cada usuário/pessoa possui sua própria conta digital e será possível realizar pagamentos para outros usuários/pessoas do sistema.

Além disso, existe um aspecto de rede social na aplicação. Permitindo que usuários comentem em pagamentos feitos por outras pessoas.

> Prometemos que não estamos plagiando o PicPay e que esse repositório é apenas para propósitos educacionais e avaliativos 😆 


## Requisitos Técnicos (RT)

### RT1 Linguagem e framework
O projeto deverá ser feito em Python utilizando os frameworks Django e Django Rest Framework!

> recomendamos utilizar versões atualizadas. Por exemplo python 3.8^, Django 3.2^

### RT2 Banco de dados e persistência
O projeto deverá utilizar o banco de dados PostgreSQL para realizar sua persistências.

> recomendamos utilizar versões atualizadas. Por exemplo psql 13^

### RT3 Bibliotecas
A utilização de bibliotecas python é incentivada!

> Por que reinventar a roda se temos open source e bibliotecas maravilhosas em python?

Para gerenciar as dependências do projeto o poetry deverá ser utilizado, juntamente ao arquivo `pyproject.toml`.

### RT4 Containers
A reprodutibilidade e portabilidade do projeto é essencial. Então deverá ser utilizado alguma tecnologia de containers.

Algumas das alternativas são:
- Docker + docker-compose
- Podman

> existem outras tecnologias, porém complexidade desnecessária é um ponto negativo. Então não recomendamos utilizar kubernets e orquestradores de containers mais complexos.

### RT5 Instruções de instalação e execução
Como já foi citado no RT4, a reprodutibilidade do projeto é essencial.

Então no projeto, deverá existir as instruções de instalação de TODAS as tecnologias utilizadas. 

> Para esse critério, deverá ser levado em consideração que o sistema operacional padrão suportado pela empresa é o Ubuntu, de preferência o LTS mais recente.

Da mesma forma, deverá existir a documentação utilização do projeto.

### RT6 Arquitetura do projeto
Para que o projeto da conta digital possa crescer corretamente, é necessário que seja utilizado uma arquitetura MVC ou hexagonal. Possibilitando centralizar e facilitar a manutenção das regras de negócio ao longo prazo da evolução do projeto.

As seguintes abordagens não são recomendadas:
- fat models
- regras de negócio nas views/serializers DRF

Um bom guia de implementação é o https://phalt.github.io/django-api-domains/

### RT7 Programas e dependências {BÔNUS}
Como já foi citado no RT4, a reprodutibilidade do projeto é essencial.

Então o ideal é que o desenvolvedor **NÃO** precise instalar diversas dependências na sua máquina para poder executar o projeto. Na verdade, o ideal é que o desenvolvedor não precise instalar **NENHUMA** dependência técnica em sua máquina via `APT` (considerando o RT5).

Isso pode ser alcançado utilizado NIX.

Esse critério bônus consiste em utilizar o [gerenciador de pacotes NIX](https://nixos.org/download.html) para criar um ambiente de desenvolvimento com as dependências necessárias. Por exemplo, podman, python, poetry, postgresql dentre outros programas necessários.

### RT8 Boa qualidade de código {BÔNUS}
O código deverá adotar boas práticas de programação. Por exemplo, nomenclatura semântica para variáveis e entidades, formatação de código, testes e outros fatores.

Para a formatação de código recomendamos a utilização das libs:
- black
- flake8
- isort

Para os testes, recomendamos eles sejam feitos considerando uma abordagem BDD. Testes unitários e técnicos são legais. Mas lembre-se de testar COMPORTAMENTOS e não DETALHES DE IMPLEMENTAÇÃO. 

E a melhor forma de garantir que essas diretrizes estejam sendo obedecidas de fato é utilizar um CI que rode automaticamente a formatação e os testes do projeto.

## Requisitos Funcionais (RF)

### RF1 Usuário/Pessoa

Temos usuários/pessoas utilizando o sistema.

#### RF1.0 Dados
- nome completo
- data de nascimento {SENSÍVEL}
- email {SENSÍVEL}
- telefone {SENSÍVEL}
- CPF {SENSÍVEL}
- senha {SENSÍVEL}

#### RF1.1 Cadastro de usuário
A aplicação deve permitir que usuários se cadastrem na plataforma, inserindo os seus dados.

> a senha deverá ser criptograda no banco de dados!

### RF1.2 Visualização de dados
A aplicação deve permitir que o próprio usuários visualize os seus PRÓPRIOS dados. Uma vez que eles estão AUTENTICADOS.

A aplicação deverá permitir que os usuários visualizem os dados NÃO SENSÍVEIS de outros usuários.

#### RF1.3 Atualização de dados
O próprio usuário poderá atualizar os seus dados.

Porém, ele NÃO poderá alterar os dados de OUTROS usuários.

#### RF1.4 Deleção de dados
Os dados não podem ser deletados!

### RF2 Conta Digital
Cada usuário/pessoa possui sua conta digital. 

#### RF2.0 Dados da conta digital
- saldo
- dono

#### RF2.1 Cadastro de conta digital
A conta digital é cadastrada AUTOMATICAMENTE no registro do usuário.

O usuário não é capaz de criar uma OUTRA conta digital.

#### RF2.2 Visualização de dados
O próprio usuário poderá ver seu saldo. Porém ele não pode visualizar o saldo da conta digital de outras pessoas!

#### RF2.3 Atualização de dados
Os dados da conta digital NÃO PODEM ser alterados por nenhum usuário!

#### RF2.4 Deleção de dados
Os dados da conta digital NÃO PODEM ser deletados!

### RF3 Depósito
O usuário precisa ser capaz de realizado uma carga/depósito em sua conta digital.

#### RF3.0 Dados do depósito
- conta digital de destino
- descrição
- valor
- horário de efetivação

#### RF3.1 Cadastro de depósito
A qualquer momento o usuário poderá cadastrar um depósito para si mesmo. E em qualquer valor!

> Deu a louca no gerente 🤪

Isso poderia ser interpretado como se o usuário tivesse feito um PIX no mundo real para a sua conta digital!

#### RF3.2 Visualização de dados
O próprio usuário poderá ver os seus próprios depósitos. Porém não poderá visualizar os depósitos das outras pessoas.

#### RF3.3 Atualização de dados
Os dados dos depósitos NÃO PODEM ser alterados por nenhum usuário!

#### RF3.4 Deleção de dados
Os dados da conta digital NÃO PODEM ser deletados!

### RF4 Transferência
O usuário poderá utilizar o seu saldo da conta digital para realizar uma transferência para QUALQUER outro usuário no sistema.

#### RF4.0 Dados da transferência
- origem
- destino
- descrição
- valor
- horário de efetivação
- público

#### RF4.1 Cadastro de Transferência
A transferência será cadsatrada pelo próprio usuário.

Não é possível cadastrar transferência em que a ORIGEM não seja você mesmo!

Na hora de registro da transferência, o usuário poderá escolher se quer fazer ela como pública ou como privada.

#### RF4.2 Visualização de dados
O próprio usuário pode ver todas as transferências feitas POR ele ou PARA ele. Independente de serem públicas ou privadas.

Porém o usuário só poderá ver transações que NÃO envolvem ele se elas estiverem marcadas como pública.

#### RF4.3 Atualização de dados
A maior parte dos dados das transferências NÃO PODEM ser alterados por nenhum usuário!

Exceto a flag de `público`, que pode ser alterada pelo usuário de ORIGEM da transferência a qualquer momento.

#### RF4.4 Deleção de dados
Os dados da transferência NÃO PODEM ser deletados!

### RF5 Comentários
Os usuários podem comentar em transferências que eles podem VISUALIZAR (vide RF4.2).

#### RF5.0 Dados do comentário
- dono
- transferência
- texto
- horário de publicação

#### RF5.1 Criação de comentário
Qualquer usuário pode criar um comentário a qualquer momento em qualquer transferência que ele POSSA VISUALIZAR (vide RF4.2).

#### RF5.2 Visualização de dados
Qualquer usuário poderá visualizar qualquer comentário em qualquer transferência que ele POSSA VISUALIZAR (vide RF4.2).

O usuário dono do comentário SEMPRE poderá visualizar seus próprios comentários.

#### RF5.3 Atualização de dados
O comentário só pode ser alterado pelo próprio usuário dono do comentário.

#### RF5.4 Deleção de dados
O comentário só pode ser deletado pelo próprio usuário dono do comentário ou dono da transação.
