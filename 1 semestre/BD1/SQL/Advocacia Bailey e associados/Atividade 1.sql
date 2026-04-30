'Padronização de nomes de colunas: inconsistência de nomenclatura
Tarefa: Renomear casos.numero → id'

select * from casos

ALTER TABLE casos RENAME COLUMN numero to id
