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

Cada requisito deve descrever uma capacidade observável do sistema. Use identificadores estáveis (`RF-001`, `RF-002`, ...) e escreva um requisito por item.

### RF-001 — [Nome do requisito]
- **Descrição:** O sistema deve [comportamento esperado].
- **Prioridade:** [Essencial / Importante / Desejável]
- **Origem:** [Stakeholder, regra de negócio ou documento]
- **Critérios de aceite:**
  - Dado [contexto], quando [ação], então [resultado verificável].

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

## 11. Histórico de alterações
| Versão | Data | Autor | Alterações |
|---|---|---|---|
| 0.1 | [AAAA-MM-DD] | [Nome] | Criação inicial |