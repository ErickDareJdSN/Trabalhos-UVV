'2. Adicionar coluna obrigatória com dados existentes
Tarefa: Adicionar coluna titulo em casos (NOT NULL)
Desafio:
Como a tabela já tem dados, você precisa:
Criar a coluna permitindo NULL
Preencher com base na descricao
Alterar para NOT NULL
'

select * from casos

alter table casos
add column titulo text;

update casos
set titulo = descricao
where titulo is null

alter table casos
alter column titulo set not null