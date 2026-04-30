'5. Criar tabela de estados (normalização leve)
Tarefa:
Criar tabela estados (id, sigla)
Popular com os estados existentes em pessoas.estado
Alterar pessoas:
substituir estado por estado_id
criar FK
'

CREATE TABLE estados (
id serial NOT NULL,
sigla char(2) NOT NULL,
CONSTRAINT pk_estados PRIMARY KEY (id),
CONSTRAINT un_estados UNIQUE (sigla)
)

INSERT INTO estados(sigla)
SELECT DISTINCT estado FROM pessoas;

ALTER TABLE pessoas
ADD COLUMN estado_id INT;

UPDATE pessoas p
SET estado_id = e.id
FROM estados e
WHERE p.estado = e.sigla;

ALTER TABLE pessoas
ADD CONSTRAINT fk_pessoas_estados
FOREIGN KEY (estado_id) REFERENCES estados (id);