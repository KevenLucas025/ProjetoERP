Fala pessoal, tudo bem?

Esse é meu terceiro projeto em Python, um projeto mais ambicioso e detalhado.
Contém tudo e mais um pouco dos 2 projetos anteriores, espero que gostem. Abaixo detalharei um pouco mais sobre o que o projeto utiliza e quais suas melhorias.

Antes de mais nada, é bom lembrar que o projeto ainda está em fase de desenvolvimento..
pois como o projeto é bem extenso e exige atenção e só eu estou trabalhando nele, então preciso de mais alguns meses para que o projeto possa ser finalizado.

Lembrando também que possa ser que tenha "atualizações" e que essa versão não represente o produto final.

1°: O projeto chama-se ERP em inglês Enterprise Resource Planning [Planejamento de Recursos Empresariais]. Pois quis fazer algo como um sistema de gerenciamento incremento tudo em um lugar só,
como a ideia de cadastrar pessoas (essa ideia foi o principal conceito dos meus 2 projetos anteriores, aqui foi melhorado), e também de cadastrar produtos, já que o sistema utiliza também,
a ideia dos projetos anteriores.

2°: O projeto conta com uma variedade vasta de opções para o usuário manipular, como disse acima é possível cadastrar e gerir pessoas e produtos. Dependendo da intenção do usuário.
Dentre as opções existe por exemplo a opção de poder controlar o histório de manipulação. Por exemplo tudo o que for feito no sistema considerado "importante" o sistema guarda isso, 
em uma aba de Histórico, nela podendo ver a data/hora o usuário que fez a alteração, o que foi alterado e aonde foi alterado. Por exemplo o usuário exclui o produto X na data do dia XX/XX/XXXX.
É interresante mencionar que dentro dessa aba há opções de criar PDF com todas as informações, criar arquivo CSV, importar arquivo CSV, pesquisar e filtrar por datas específicas e muito mais.

3°: O sistema conta com páginas dedicadas somente ao usuário e aos produtos cadastrados. Sendo que cada uma conta com suas próprias opções. Claro que em algum momento vocês iram notar algo parecido, como por exemplo na página de Verificar Estoque, dentro dela há uma tabela com produtos cadastrado e que podem ser ou não excluído (a opção de excluir é relativamente permanente, irei falar sobre isso logo abaixo),o usuário que "excluir" um produto e se arrepender ou caso exclua de forma equivocada poderá estornar esse produto para que o mesmo possa entrar em estoque novamente.Lembrando que ao fazer a exclusão, o produto irá para a tabela abaixo chamada de "Sáida". Os produtos que forem movidos para lá ficam suspensos como se não estivessem mais no estoque. Porém continuam salvos dentro do banco de dados. Estará definido uma data média para exclusão permanente desses produtos de no mínimo 12 meses (1 ano).

4°: A página de Verificar Estoque já está finalizada. Tendo todas  as suas funções de (Novo Produto, Atualizar Saída, Atualizar Estoque, Histórico, Gerar PDF, Limpar tabelas e Incluir produto no sistema). Lembrando que essa página permite o estorno dos produtos, ao contrário da página de Verificar Usuários que não possue essa opção.

5º: A página de Verificar Usuários está em desenvolvimento, com quase todas as suas funções prontas. Suas funções são semelhantes as funções da página de Verificar Estoque. 

