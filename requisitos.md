# Especificação de Requisitos

## 1. Visão geral

### 1.1 Objetivo
Descreva, em poucas frases, o problema que o sistema resolve e o propósito deste documento.

O seguinte sistema trata-se de um genrenciador de cafeteria (The Coffee) junto com serviço de uso para clientes e foi criado com o próposito de centralizar a organização de um estabelecimento da franquia em
um só lugar, facilitando e agilizando processos tanto para funcionários quanto para clientes.

O objetivo deste documento é definir quais são os requisitos básicos e necessários para resolver os problemas
definidos.

### 1.2 Escopo
O escopo do sistema engloba autenticação de usuários e administração de produtos no estoque.

### 1.3 Público-alvo
Os principais usuários do sistema serão os funcionários que o utilizarão para fazer a administração do estabelecimento e os clientes que poderam utilizá-lo para realizar comprar

### 1.4 Termos e definições
| Termo | Definição |
|---|---|
| [Termo] | [Significado no contexto do sistema] |

## 2. Stakeholders e perfis de usuário
| Perfil | Descrição | Necessidades principais |
|---|---|---|
| [Perfil] | [Quem é] | [O que precisa realizar] |
| Cliente | Quem irá comprar produtos | Usar o sistema para solicitar serviços oferecidos pela empresa |
| Funcionário | Principal responsável pela manutenção do sistema já funcionando e em uso | Usa o sistema para administrar e atender clientes |
| Usuário | Perfil genérico de quem usa o sistema | Usa o sistema para funções diversas |

## 3. Requisitos funcionais


### RF-000 — [Nome do requisito]
- **Descrição:** O sistema deve [comportamento esperado].
- **Prioridade:** [Essencial / Importante / Desejável]
- **Origem:** [Stakeholder, regra de negócio ou documento]
- **Critérios de aceite:**
  - Dado [contexto], quando [ação], então [resultado verificável].


### RF-001 — Cadastro de usuários
- **Descrição:** O sistema deve cadastrar os usuários com base nos dados fornecidos se válidos.
- **Prioridade:** Essencial
- **Origem:** Usuário
- **Critérios de aceite:**
  - Dado a entrada do usuário no sistema, quando fornecer os seus dados, então ele será registrado e persistido em um banco de dados.

### RF-002 — Login de usuários
- **Descrição:** O sistema deve permitir que usuários possam fazer login nas suas contas cadastradas.
- **Prioridade:** Essencial
- **Origem:** Usuário
- **Critérios de aceite:**
  - Dado a entrada do usuário no sistema, quando fornecer os seus dados, então ele será verificado e, se existir uma conta salva, irá entrar com aquela conta no sistema.

### RF-003 — Cadastro de produtos
- **Descrição:** O sistema deve possibilitar que funcionários possam cadastrar produtos no sistema.
- **Prioridade:** Essencial
- **Origem:** [Stakeholder, regra de negócio ou documento]
- **Critérios de aceite:**
  - Dado o fornecimento de novos produtos, quando um funcionário entrar e registrar um produto, então os produtos registrados ficaram salvos para compra no estoque.

### RF-003 — Compra de produtos
- **Descrição:** O sistema deve deixar que usuários comprem produtos existentes no estoque.
- **Prioridade:** Essencial
- **Origem:** [Stakeholder, regra de negócio ou documento]
- **Critérios de aceite:**
  - Dada a situação em que o usuário queira realizar a compra de um produto, quando ele entrar na sessão de comprar permitir que ele escolha um produto, então então o produto escolhido será descontado do estoque

## 4. Regras de negócio

### RN-000 — [Nome da regra]
- **Regra:** [Condição que deve ser respeitada]
- **Exemplo ou consequência:** [Como a regra afeta o comportamento]

### RN-001 — Persistência de estado de valores monetários
- **Regra:** A representação do dinheiro no sistema deve respeitar as propriedades de transação e estado que acontecem na vida real, no caso, uma abstração da realidade
- **Exemplo ou consequência:** Dinheiro não pode ter valor negativo. Comprar um produto de valor negativo vai gerar prejuízo para o estabelecimento.

## 5. Requisitos não funcionais

Descreva qualidades ou restrições mensuráveis, como segurança, desempenho, usabilidade, disponibilidade e compatibilidade. Use identificadores `RNF-001`, `RNF-002`, ...

### RNF-000 — [Nome do requisito]
- **Categoria:** [Segurança / Desempenho / Usabilidade / ...]
- **Descrição:** O sistema deve [qualidade ou restrição].
- **Métrica ou critério de verificação:** [Como confirmar que foi atendido]

### RNF-001 — Persistência de dados sensíveis
- **Categoria:** Segurança
- **Descrição:** Atualmente, o sistema restringe o acesso de usuários à opções de funcionários dentro do uso do próprio sistema, mas os dados ainda podem ser alterados diretamente pelo banco.
- **Métrica ou critério de verificação:** Usuários são barrados pelo sistema se o código não for alterado diretamente, mas os dados ainda são sucetíveis à alterações diretas fora do sistema.

## 6. Interfaces e integrações
- **Interface com o usuário:** Por se tratar de um CLI (Command-Line Interface) atualmente a interface de uso, tanto para clientes como funcionários é o próprio terminal.
- **Integrações externas:** Nenhuma

## 7. Restrições e dependências
- [Tecnologias, legislação, ambiente ou dependências que limitam a solução]
- Python mais recente instalado

## 8. Casos de uso

### UC-000 — [Nome do caso de uso]
- **Ator:** [Perfil que inicia a ação]
- **Pré-condições:** [O que precisa ser verdadeiro antes]
- **Fluxo principal:**
  1. [Ação do ator]
  2. [Resposta do sistema]
- **Alternativas e erros:** [Variações ou falhas esperadas]
- **Pós-condições:** [Estado do sistema ao final]

### UC-001 — Entrar no sistema
- **Ator:** Cliente / Funcionário
- **Pré-condições:** O sistema deve estar inicializado.
- **Fluxo principal:**
  1. O cliente (ou o funcionário) entra no sistema;
  2. O sistema solicita os dados para entrar no sistema;
  2. O usuário dá entrada nos seus dados no sistema;
  2. O sistema verifica quem é o usuário e permite que ele entre caso exista registro dele.
- **Alternativas e erros:** Falhas externas como ausência de python instalado pode gerar erros; o sistema incompleto etc.
- **Pós-condições:** O cliente/funcionário poderá ter acesso as suas respectivas sessões dentro do sistema.

### UC-001 — Entrar no sistema
- **Ator:** Cliente / Funcionário
- **Pré-condições:** O sistema deve estar inicializado.
- **Fluxo principal:**
  1. O cliente (ou o funcionário) entra no sistema;
  2. O sistema solicita os dados para entrar no sistema;
  2. O usuário dá entrada nos seus dados no sistema;
  2. O sistema verifica quem é o usuário e permite que ele entre caso exista registro dele.
- **Alternativas e erros:** Falhas externas como ausência de python instalado pode gerar erros; o sistema incompleto etc.
- **Pós-condições:** O cliente/funcionário poderá ter acesso as suas respectivas sessões dentro do sistema.

## 9. Critérios de aceite do sistema
- Clientes conseguem escolher produtos e comprá-los pelo sistema;
- Funcionários conseguem registrar, alterar e remover produtos do estoque;
- Usuários conseguem se cadastrar, entrar e sair de contas.

## 10. Pendências e decisões
| Item | Dúvida ou decisão necessária | Responsável | Estado |
|---|---|---|---|
| [ID] | [Descrição] | [Pessoa ou perfil] | [Aberto / Resolvido] |
| 001 | Registro de clientes na inicialização do sistema | Usuário | Aberto |