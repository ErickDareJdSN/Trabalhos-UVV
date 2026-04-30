'3. Remover coluna desnecessária
Tarefa: Remover coluna descricao de tipos_eventos
'

select * from tipos_eventos

alter table tipos_eventos
drop column descricao