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

6º: 

