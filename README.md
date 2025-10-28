👋 Fala, pessoal! Tudo bem?

Este é o meu terceiro projeto em Python, um projeto mais ambicioso e detalhado, reunindo tudo — e um pouco mais — dos dois projetos anteriores.
Espero que gostem! 👇
Abaixo explico um pouco mais sobre as tecnologias utilizadas e as melhorias implementadas.

💡 Observação: o projeto está em fase final de desenvolvimento.
Como ele é bastante extenso e estou trabalhando sozinho, ainda estou realizando os últimos ajustes e otimizações.
A previsão é que até o final de 2025 o sistema esteja 100% finalizado e disponível para download.

Além disso, podem ocorrer atualizações e ajustes ao longo do tempo, portanto esta versão ainda não representa o produto final.

1°: O Sistema de Gerenciamento foi desenvolvido com o objetivo de gerenciar pessoas e produtos, aprimorando o conceito central presente nos meus dois projetos anteriores.
Nesta versão, o sistema foi melhorado e expandido, reunindo as melhores ideias e funcionalidades já testadas anteriormente, com foco em organização, praticidade e eficiência.

2°: ⚙️ Funcionalidades do sistema

O projeto conta com uma ampla variedade de opções para o usuário manipular e gerenciar informações.
Como mencionado anteriormente, é possível cadastrar e administrar pessoas e produtos, de acordo com a necessidade de uso.

Entre as funcionalidades disponíveis, destaca-se o controle completo do histórico de ações.
Tudo o que for considerado importante dentro do sistema é registrado automaticamente em uma aba de Histórico, onde o usuário pode visualizar:

📅 Data e hora da ação
👤 Usuário responsável
📝 O que foi alterado
📍 Onde ocorreu a alteração

Por exemplo: caso um usuário exclua o produto X no dia XX/XX/XXXX, essa ação será registrada e poderá ser consultada a qualquer momento.

Além disso, dentro dessa aba o sistema oferece recursos adicionais, como:

📄 Geração de relatórios em PDF
📊 Exportação e importação de arquivos CSV
🔍 Pesquisa e filtros por data específica
➕ E muito mais!

3°: 🧾 Páginas e gerenciamento de dados

O sistema conta com páginas dedicadas exclusivamente aos usuários e aos produtos cadastrados, cada uma com suas próprias opções e funcionalidades.

Em alguns momentos, você pode notar semelhanças entre as páginas, como na seção Verificar Estoque, onde há uma tabela com todos os produtos cadastrados.
Nessa tela, é possível excluir produtos — lembrando que essa exclusão é relativamente permanente (explicado mais abaixo).

Caso o usuário exclua um produto por engano ou se arrependa, ele poderá estornar o produto, retornando-o ao estoque normalmente.

Ao realizar uma exclusão, o produto é movido para uma tabela inferior chamada “Saída”, onde permanece suspenso, como se não estivesse mais disponível no estoque.
No entanto, os dados do produto continuam armazenados no banco de dados, garantindo a segurança das informações.

Por fim, o sistema define uma data média de exclusão permanente desses produtos — um prazo mínimo de 12 meses (1 ano) — antes que sejam removidos definitivamente.

4°: 📦 Página de Verificar Estoque

A página Verificar Estoque já está completamente finalizada, contendo todas as suas principais funcionalidades:

➕ Novo Produto
🔄 Atualizar Saída
📥 Atualizar Estoque
🕓 Histórico de ações
🧹 Limpar tabelas
✅ Incluir produto no sistema

Essa página também permite estornar produtos excluídos, possibilitando que retornem ao estoque caso o usuário tenha removido algo por engano.

⚠️ Diferente da página Verificar Usuários, esta possui a opção de estorno, oferecendo mais flexibilidade no gerenciamento dos produtos.

5º: 👥 Página de Verificar Usuários

A página Verificar Usuários também está totalmente finalizada, com todas as suas funcionalidades prontas e operacionais.
Suas funções são semelhantes às da página Verificar Estoque, garantindo uma experiência de uso consistente em todo o sistema.

⚠️ Importante: nesta página não é possível realizar o “estorno” ou recuperar um usuário excluído.
Portanto, recomenda-se atenção ao remover registros, já que essa ação é definitiva e não pode ser desfeita.

6º: 🧾 Página de Cadastrar Produto

A página Cadastrar Produto foi desenvolvida para ser intuitiva e prática, permitindo cadastrar novos produtos e também editar informações já existentes.

Além disso, o usuário pode adicionar uma imagem para melhorar a identificação visual do produto.

Por exemplo, ao cadastrar um produto como “Pizza”, a página oferece os seguintes campos:

Campo	                                  Descrição
Produto	                                Nome do produto (ex: Pizza)
Quantidade	                            Quantidade em estoque (ex: 2)
Valor do Produto	                      O sistema formata automaticamente o valor para a moeda nacional (R$)
Desconto	                              Pode ser aplicado até 100%; se não houver desconto, deixe em branco ou insira 0
Data do Cadastro/Compra	                O usuário escolhe a data desejada
Código do Item	Gerado automaticamente; o botão ADICIONAR cria esse código
Cliente	                                Deve estar cadastrado previamente no sistema
Descrição do Produto	                  Campo livre para uma descrição breve e clara

Após preencher todos os campos, basta clicar no botão ADICIONAR — o sistema realizará todos os cálculos automaticamente, garantindo praticidade e consistência nos registros.


7º: 👤 Página de Cadastrar Usuários

A página Cadastrar Usuários foi desenvolvida para ser simples, organizada e eficiente, facilitando o gerenciamento de dados cadastrais dos usuários do sistema.

Ela permite cadastrar, editar e atualizar informações, além de carregar ou remover imagens de perfil para melhor visualização do usuário.

Os principais campos disponíveis incluem:

Campo	                        Descrição
Nome completo	                Nome completo do usuário
Nome de Usuário	              Utilizado para login no sistema
Senha / Confirmar Senha	      Garantem segurança e autenticação
CPF / RG / CEP	              Campos formatados automaticamente/ O sistema utiliza uma API de consulta de CEP para preencher automaticamente os campos de endereço, cidade, estado e bairro
Endereço	                    Endereço completo do usuário
E-mail	                      Contato e recuperação de acesso
Data de Nascimento	          Informações pessoais adicionais
Imagem do Usuário	            Opcional, pode ser carregada ou removida a qualquer momento

A interface foi pensada para oferecer agilidade e praticidade, mantendo a consistência com o restante do sistema e reduzindo o tempo de preenchimento manual.

8º: 🧑‍💼 Página de Clientes

A página Clientes permite o cadastro e gerenciamento completo de clientes físicos e jurídicos, reunindo todas as informações essenciais em uma única interface.

Ela conta com uma tabela detalhada, exibindo os principais dados de cada cliente de forma organizada e acessível.

Entre as funcionalidades disponíveis estão:

📝 Cadastro de clientes (pessoa física e jurídica)
✏️ Edição e atualização de informações existentes
🕓 Histórico completo de cada cliente, incluindo quem realizou o cadastro e quando foi feito
📄 Geração de relatórios para análise e controle de clientes
🔍 Pesquisa avançada, permitindo localizar rapidamente clientes ao digitar parte do nome, CNPJ ou CPF

Essa página foi projetada para oferecer agilidade, clareza e eficiência no gerenciamento dos registros, tornando a navegação mais intuitiva e profissional.

9: ⚡ Páginas Extras — Cadastro em Massa

As páginas Cadastrar Cliente (Físico e Jurídico), Cadastrar Produtos em Massa e Cadastrar Usuários em Massa foram desenvolvidas para otimizar o processo de cadastro de grandes volumes de informações.

Essas páginas permitem registrar vários clientes, produtos ou usuários de uma só vez, proporcionando mais agilidade e eficiência no gerenciamento dos dados.

🔒 Atenção: essas funcionalidades estarão disponíveis somente para usuários com assinatura mensal ou anual do sistema.

Para facilitar o uso, o sistema disponibiliza planilhas de exemplo, servindo como modelo para o preenchimento correto das informações antes da importação em massa.

10º ⚙️ Página de Configurações

A página Configurações foi criada para permitir que o usuário personalize o funcionamento e a aparência do sistema de acordo com suas preferências.

Entre as principais opções disponíveis estão:

🎨 Alteração de tema: escolha entre Modo Claro, Modo Escuro ou Modo Clássico
🔠 Ajuste do tamanho dos botões para melhor usabilidade
⌨️ Mapeamento de teclas personalizável, permitindo redefinir atalhos do sistema
🔔 Ativar ou desativar notificações e mensagens informativas
🔄 Ativar ou desativar atualizações automáticas (em desenvolvimento)

⚠️ Observação: a opção de ativar/desativar atualizações ainda está em fase de desenvolvimento, pois envolve uma integração mais complexa.
Estou trabalhando para aprimorar essa funcionalidade e garantir que seja implementada da melhor forma possível.







