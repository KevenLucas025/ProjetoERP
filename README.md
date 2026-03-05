# 🧠 Sistema de Gerenciamento

👋 Olá! Seja bem-vindo ao meu projeto.

Este é o meu **terceiro projeto desenvolvido em Python** e também o mais ambicioso até agora.  
Ele reúne e aprimora diversas ideias e funcionalidades presentes nos meus dois projetos anteriores, trazendo um sistema mais completo, organizado e funcional para **gerenciamento de pessoas, produtos e clientes**.

O objetivo deste projeto foi criar uma aplicação **robusta, prática e escalável**, focada em organização de dados e facilidade de uso.

---

## 🚧 Status do Projeto

⚠️ **Projeto finalizado, porém em constante evolução.**

O sistema já possui todas as funcionalidades principais implementadas, mas melhorias, otimizações e novas funcionalidades poderão ser adicionadas ao longo do tempo.

Como todo projeto desenvolvido individualmente, alguns ajustes ainda podem acontecer conforme o sistema evolui.

---

# ⚙️ Tecnologias Utilizadas

Este projeto foi desenvolvido utilizando principalmente:

- 🐍 **Python**
- 🖥 **PySide6 (Interface Gráfica)**
- 🗄 **SQLite3 (Banco de Dados)**
- 📊 **Pandas (Manipulação de dados)**
- 📄 **ReportLab / FPDF (Geração de relatórios em PDF)**
- 🔎 **CSV para importação e exportação de dados**

O sistema também utiliza **APIs externas**, como por exemplo a consulta automática de **CEP** para preenchimento de endereço.

---

# 📋 Principais Funcionalidades

O sistema oferece diversas funcionalidades para gerenciamento de dados:

✔ Cadastro e gerenciamento de usuários  
✔ Cadastro e gerenciamento de produtos  
✔ Cadastro de clientes (Pessoa Física e Jurídica)  
✔ Controle completo de histórico de ações  
✔ Exportação e importação de dados (CSV)  
✔ Geração de relatórios em PDF  
✔ Sistema de busca e filtros avançados  
✔ Cadastro em massa de informações  
✔ Sistema de configurações personalizáveis  

---

# 📜 Sistema de Histórico

Uma das funcionalidades centrais do sistema é o **registro automático de ações**.

Sempre que uma ação importante acontece dentro do sistema, ela é registrada automaticamente.

Cada registro contém:

📅 Data e hora da ação  
👤 Usuário responsável  
📝 Descrição da ação realizada  
📍 Local onde a alteração ocorreu

Isso garante **rastreabilidade e controle total das alterações realizadas no sistema**.

Exemplo:

> Se um usuário excluir um produto, o sistema registrará quem realizou a ação, quando ela ocorreu e qual produto foi afetado.

---

# 📦 Gerenciamento de Produtos

A página **Verificar Estoque** permite visualizar todos os produtos cadastrados no sistema.

Entre as funcionalidades disponíveis:

- ➕ Adicionar novos produtos
- 🔄 Atualizar estoque
- 📥 Atualizar saída de produtos
- 🕓 Visualizar histórico
- 🧹 Limpar tabelas
- 🔍 Pesquisar produtos

Quando um produto é removido, ele **não é excluído imediatamente do banco de dados**.

Ele é movido para uma tabela chamada **Saída**, onde permanece armazenado por um período mínimo de **12 meses** antes da remoção definitiva.

Isso permite **recuperar produtos excluídos por engano**.

---

# 👥 Gerenciamento de Usuários

A página **Verificar Usuários** permite visualizar e gerenciar todos os usuários cadastrados no sistema.

Funcionalidades disponíveis:

- ➕ Cadastro de novos usuários
- ✏️ Edição de informações
- ❌ Exclusão de usuários
- 🔎 Busca rápida por dados

⚠️ Diferente do sistema de produtos, **usuários excluídos não podem ser restaurados**.

---

# 🧑‍💼 Gerenciamento de Clientes

A página **Clientes** permite cadastrar e gerenciar clientes **Pessoa Física e Pessoa Jurídica**.

Funcionalidades principais:

- 📝 Cadastro de clientes
- ✏️ Atualização de informações
- 📄 Geração de relatórios
- 🔎 Pesquisa por nome, CPF ou CNPJ
- 🕓 Histórico completo de alterações

---

# ⚡ Cadastro em Massa

O sistema também possui funcionalidades para **importação em massa de dados**.

É possível cadastrar:

- Clientes
- Produtos
- Usuários

Utilizando arquivos **CSV** previamente formatados.

📄 O sistema fornece **planilhas modelo** para facilitar o preenchimento correto das informações.

⚠️ Esta funcionalidade pode ser limitada a versões com assinatura do sistema.

---

# ⚙️ Página de Configurações

A página de configurações permite personalizar o comportamento do sistema.

Opções disponíveis:

🎨 Alteração de tema (Claro, Escuro ou Clássico)  
🔠 Ajuste do tamanho dos botões  
⌨️ Personalização de atalhos de teclado  
🔔 Ativar ou desativar notificações  
🔄 Controle de atualizações automáticas 

---

# 📌 Observações

Este projeto foi desenvolvido **de forma independente**, com o objetivo de aprimorar conhecimentos em:

- Desenvolvimento de aplicações desktop
- Gerenciamento de banco de dados
- Organização de projetos Python
- Interface gráfica com PySide6

---

# ⭐ Conclusão

Este projeto representa uma evolução significativa em relação aos meus projetos anteriores.

Ele foi desenvolvido com foco em:

- organização
- praticidade
- eficiência
- escalabilidade

Novas melhorias e funcionalidades poderão ser adicionadas no futuro conforme o projeto evolui.
