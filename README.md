# Projeto: Sistema de Envio de Currículos com IA

## 📋 Descrição do Projeto

Este projeto tem como objetivo ajudar pessoas na busca por emprego através de um sistema inteligente que utiliza Inteligência Artificial para analisar currículos e realizar envios personalizados para vagas adequadas ao perfil do candidato.

## 🎯 Objetivo

Desenvolver um sistema que recebe o currículo do usuário e, utilizando IA, identifica as áreas onde o candidato tem maior destaque, permitindo o envio personalizado de currículos para vagas específicas.

## ⚙️ Funcionalidades Principais

### 1. Análise Inteligente de Currículos
- **Análise de Perfil**: A IA analisa o currículo e identifica as áreas de destaque do candidato
- **Recomendações**: Sugere melhorias, cursos complementares e correções no currículo
- **Geração de Currículos**: Cria versões personalizadas do currículo para diferentes áreas

### 2. Sistema de Envio Personalizado
- **Seleção de Vagas**: O usuário escolhe para quais áreas deseja enviar o currículo
- **Personalização**: A IA adapta o conteúdo do currículo e a mensagem de envio para cada vaga
- **Base de Dados**: Acesso a um banco de vagas atualizado diariamente

## 🖥️ Interface do Usuário

### Tela Inicial
- Apresentação do sistema e seu funcionamento
- Botão de call-to-action: "Vamos começar a testar?"
- Explicação simplificada da ideia do projeto

### Fluxo Principal
1. **Upload do Currículo**: Usuário envia currículo em PDF ou DOCX
2. **Análise da IA**: Sistema identifica áreas de destaque
3. **Seleção de Vagas**: Usuário escolhe as áreas para envio
4. **Personalização**: IA adapta currículos para cada área selecionada
5. **Envio**: Disparo para a base de dados de vagas

## 🗃️ Estrutura do Banco de Dados

A base de dados contém uma tabela principal com as seguintes colunas:

| Campo | Tipo | Descrição |
|-------|------|-----------|
| **id** | Inteiro | Identificador único da vaga |
| **Nome da Vaga** | Texto | Nome/título da vaga |
| **Email** | Texto | E-mail para contato/envio |
| **Data Inserida** | Data | Data de cadastro da vaga |
| **Data Limite** | Data | Prazo final para inscrição |
| **Requisitos** | Texto | Requisitos necessários para a vaga |
| **Atividades** | Texto | Descrição das atividades |
| **Benefícios** | Texto | Benefícios oferecidos |
| **Observações** | Texto | Informações adicionais |

## 🤖 Tecnologia de IA

### DeepSeek-V3
- **Framework**: Utilizaremos o DeepSeek-V3 como modelo principal
- **Implementação**: Execução local para análise de currículos
- **Treinamento**: Modelo será treinado para realizar análises precisas e sem erros

## 📊 Processo de Geração de Currículos

A IA gera currículos personalizados preenchendo automaticamente um template em Excel que é convertido para PDF, contendo:

- Informações pessoais
- Experiência profissional
- Formação acadêmica
- Cursos e certificações
- Habilidades técnicas
- Outras informações relevantes

## 🚀 Próximos Passos

1. Desenvolvimento da interface do usuário
2. Implementação do banco de dados
3. Integração com o modelo DeepSeek-V3
4. Criação dos templates de currículo
5. Testes e validação do sistema

---

*Este projeto visa revolucionar o processo de busca por emprego através da aplicação de Inteligência Artificial para personalização e otimização do envio de currículos.*
