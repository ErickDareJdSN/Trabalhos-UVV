create table
     enderecos(
          id_endereco serial,
          rua varchar(100),
          avenida varchar (100),
          bairro varchar(50) not null,
          cidade varchar(100),
          estado varchar(100),
          constraint pk_enderecos primary key (id_endereco)
);

create table
     cinemas(
          id_cinema serial,
		  id_endereco int not null,
		  nome_fantasia varchar(100) not null,
		  capacidade smallint not null,
		  constraint pk_cinema primary key (id_cinema),
		  constraint fk_cinema foreign key (id_endereco)
		       references enderecos (id_endereco)
);

create table
     pessoas(
          id_pessoa serial,
		  nome varchar(100) not null,
		  nacionalidade varchar(50) not null,
		  idade smallint not null,
		  constraint pk_pessoa primary key (id_pessoa)
);

create table
     filmes(
          id_filme serial,
		  id_diretor int,
		  pais_origem varchar(50) not null,
		  titulo_original varchar(50) not null,
		  titulo_ptbr varchar(50),
		  genero varchar(20) not null,
		  duracao int not null,
		  impropriedades varchar(50) not null,
		  constraint pk_filme primary key (id_filme),
		  constraint fk_filme foreign key (id_diretor)
		       references pessoas (id_pessoa)
);

create table
     filmes_atores(
          id_pessoa int,
		  id_filme int,
		  constraint pk_filme_ator primary key (id_pessoa, id_filme),
		  constraint fk_filme_ator_ator foreign key (id_pessoa)
		       references pessoas (id_pessoa),
			   constraint fk_filme_ator_filme foreign key (id_filme)
			        references filmes (id_filme)
);

create table
     sessoes(
          id_sessao serial,
		  id_cinema int,
		  id_filme int,
		  intervalo int not null,
		  horario time not null,
		  constraint pk_sessoes primary key (id_sessao),
		  constraint fk_sessoes_cinema foreign key (id_cinema)
		       references cinemas (id_cinema),
			   constraint fk_sessoes_filme foreign key (id_filme)
			        references filmes (id_filme)
);

create table
     registros_publicos (
          id_registro serial,
		  id_sessao int,
		  data_registro date not null,
		  quantidade_assistentes smallint not null,
		  constraint pk_registros_publicos primary key (id_registro),
		  constraint fk_registros_publicos foreign key (id_sessao)
		       references sessoes (id_sessao)
);

alter table pessoas
     add column cpf varchar(11),
	 add column id_endereco int,
	 add constraint un_pessoas unique (cpf),
	 add constraint fk_pessoas foreign key (id_endereco)
	          references enderecos (id_endereco);

alter table sessoes
     drop column intervalo;

alter table registros_publicos
     add constraint un_registros_publicos unique (id_sessao, data_registro)