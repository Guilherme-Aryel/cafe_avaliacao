# Especificação de Requisitos

## 1. Visão geral

### 1.1 Objetivo
Descreva, em poucas frases, o problema que o sistema resolve e o propósito deste documento.

O seguinte sistema trata-se de um genrenciador de cafeteria (The Coffee) junto com serviço de uso para clientes e foi criado com o próposito de centralizar a organização de um estabelecimento da franquia em
um só lugar, facilitando e agilizando processos tanto para funcionários quanto para clientes.

O objetivo deste documento é definir quais são os requisitos básicos e necessários para resolver os problemas
definidos.

### 1.2 Escopo
Descreva o que faz parte do sistema e, se necessário, o que está fora do escopo.

### 1.3 Público-alvo
Indique quem utilizará o sistema e quem consultará esta especificação.

### 1.4 Termos e definições
| Termo | Definição |
|---|---|
| [Termo] | [Significado no contexto do sistema] |

## 2. Stakeholders e perfis de usuário
| Perfil | Descrição | Necessidades principais |
|---|---|---|
| [Perfil] | [Quem é] | [O que precisa realizar] |

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
- **Origem:** [Stakeholder, regra de negócio ou documento]
- **Critérios de aceite:**
  - Dado a entrada do usuário no sistema, quando fornecer os seus dados, então ele será registrado e persistido em um banco de dados.

### RF-002 — Login de usuários
- **Descrição:** O sistema deve permitir que usuários possam fazer login nas suas contas cadastradas.
- **Prioridade:** Essencial
- **Origem:** [Stakeholder, regra de negócio ou documento]
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

Use identificadores `RN-001`, `RN-002`, ... para regras que restringem ou orientam o funcionamento do sistema.

### RN-001 — [Nome da regra]
- **Regra:** [Condição que deve ser respeitada]
- **Exemplo ou consequência:** [Como a regra afeta o comportamento]

## 5. Requisitos não funcionais

Descreva qualidades ou restrições mensuráveis, como segurança, desempenho, usabilidade, disponibilidade e compatibilidade. Use identificadores `RNF-001`, `RNF-002`, ...

### RNF-001 — [Nome do requisito]
- **Categoria:** [Segurança / Desempenho / Usabilidade / ...]
- **Descrição:** O sistema deve [qualidade ou restrição].
- **Métrica ou critério de verificação:** [Como confirmar que foi atendido]

## 6. Interfaces e integrações
- **Interface com o usuário:** [Telas, comandos ou canais necessários]
- **Integrações externas:** [Serviço, dados trocados e finalidade, ou "Nenhuma"]

## 7. Restrições e dependências
- [Tecnologias, legislação, ambiente ou dependências que limitam a solução]
- Python mais recente instalado

## 8. Casos de uso

### UC-001 — [Nome do caso de uso]
- **Ator:** [Perfil que inicia a ação]
- **Pré-condições:** [O que precisa ser verdadeiro antes]
- **Fluxo principal:**
  1. [Ação do ator]
  2. [Resposta do sistema]
- **Alternativas e erros:** [Variações ou falhas esperadas]
- **Pós-condições:** [Estado do sistema ao final]

## 9. Critérios de aceite do sistema
- [Condição verificável para considerar o escopo entregue]

## 10. Pendências e decisões
| Item | Dúvida ou decisão necessária | Responsável | Estado |
|---|---|---|---|
| [ID] | [Descrição] | [Pessoa ou perfil] | [Aberto / Resolvido] |