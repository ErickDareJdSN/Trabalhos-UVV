'Separar nome completo: nome está tudo junto
Tarefa: Em clientes, criar:
primeiro_nome
sobrenome
Preencher com base em nome
(Depois pode manter ou remover nome)
'

select * from clientes

ALTER TABLE clientes 
ADD COLUMN primeiro_nome TEXT,
ADD COLUMN sobrenome TEXT;

UPDATE clientes
SET primeiro_nome = split_part (nome, ' ', 1);
UPDATE clientes
SET sobrenome = split_part(nome, ' ', 2)

ALTER TABLE clientes
DROP COLUMN nome;

ALTER TABLE clientes
ALTER COLUMN primeiro_nome SET NOT NULL;

ALTER TABLE clientes
ALTER COLUMN sobrenome SET NOT NULL;