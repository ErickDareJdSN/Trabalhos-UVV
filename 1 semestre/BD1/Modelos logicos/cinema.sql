CREATE TABLE "Cinema"(
    "id_cinema" SERIAL NOT NULL,
    "id_endereco(FK)" VARCHAR(9) NOT NULL,
    "nome_fantasia" VARCHAR(50) NOT NULL,
    "capacidade" INTEGER NOT NULL
);
ALTER TABLE
    "Cinema" ADD PRIMARY KEY("id_cinema");
ALTER TABLE
    "Cinema" ADD PRIMARY KEY("id_endereco(FK)");
CREATE TABLE "Endereços"(
    "id_endereco" VARCHAR(9) NOT NULL,
    "rua" VARCHAR(50) NOT NULL,
    "avenida" VARCHAR(50) NOT NULL,
    "bairro" VARCHAR(50) NOT NULL,
    "cidade" VARCHAR(50) NOT NULL,
    "estado" VARCHAR(50) NOT NULL
);
ALTER TABLE
    "Endereços" ADD PRIMARY KEY("id_endereco");
CREATE TABLE "Sessão"(
    "id_sessao" SERIAL NOT NULL,
    "id_cinema(FK)" SERIAL NOT NULL,
    "id_filme(FK)" SERIAL NOT NULL,
    "intervalo" INTEGER NOT NULL,
    "horario" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL
);
ALTER TABLE
    "Sessão" ADD PRIMARY KEY("id_sessao");
ALTER TABLE
    "Sessão" ADD PRIMARY KEY("id_cinema(FK)");
ALTER TABLE
    "Sessão" ADD PRIMARY KEY("id_filme(FK)");
CREATE TABLE "Filme"(
    "id_filme" SERIAL NOT NULL,
    "id_diretor(FK)" SERIAL NOT NULL,
    "pais_origem" VARCHAR(20) NOT NULL,
    "titulo_original" VARCHAR(50) NOT NULL,
    "titulo_ptbr" VARCHAR(50) NOT NULL,
    "genero" VARCHAR(20) NOT NULL,
    "duracao" INTEGER NOT NULL,
    "impropriedades" VARCHAR(20) NOT NULL
);
ALTER TABLE
    "Filme" ADD PRIMARY KEY("id_filme");
ALTER TABLE
    "Filme" ADD PRIMARY KEY("id_diretor(FK)");
CREATE TABLE "Pessoa_diretor"(
    "id_pessoa(PK, FK)" SERIAL NOT NULL,
    "id_diretor(PK, FK)" SERIAL NOT NULL
);
ALTER TABLE
    "Pessoa_diretor" ADD PRIMARY KEY("id_pessoa(PK, FK)");
ALTER TABLE
    "Pessoa_diretor" ADD PRIMARY KEY("id_diretor(PK, FK)");
CREATE TABLE "Pessoa"(
    "id_pessoa" BIGINT NOT NULL,
    "nome" VARCHAR(50) NOT NULL,
    "nacionalidade" VARCHAR(20) NOT NULL,
    "idade" SMALLINT NOT NULL
);
ALTER TABLE
    "Pessoa" ADD PRIMARY KEY("id_pessoa");
CREATE TABLE "Pessoa_ator"(
    "id_pessoa(PK, FK)" SERIAL NOT NULL,
    "id_ator(PK, FK)" SERIAL NOT NULL
);
ALTER TABLE
    "Pessoa_ator" ADD PRIMARY KEY("id_pessoa(PK, FK)");
ALTER TABLE
    "Pessoa_ator" ADD PRIMARY KEY("id_ator(PK, FK)");
CREATE TABLE "Registro_público"(
    "id_registro" SERIAL NOT NULL,
    "id_sessao(FK)" SERIAL NOT NULL,
    "data" DATE NOT NULL,
    "quantidade_assistentes" INTEGER NOT NULL
);
ALTER TABLE
    "Registro_público" ADD PRIMARY KEY("id_registro");
ALTER TABLE
    "Registro_público" ADD PRIMARY KEY("id_sessao(FK)");
CREATE TABLE "Filme_Ator"(
    "id_ator(PK, FK)" SERIAL NOT NULL,
    "id_filme(PK, FK)" SERIAL NOT NULL
);
ALTER TABLE
    "Filme_Ator" ADD PRIMARY KEY("id_ator(PK, FK)");
ALTER TABLE
    "Filme_Ator" ADD PRIMARY KEY("id_filme(PK, FK)");
ALTER TABLE
    "Cinema" ADD CONSTRAINT "cinema_id_endereco(fk)_foreign" FOREIGN KEY("id_endereco(FK)") REFERENCES "Endereços"("id_endereco");
ALTER TABLE
    "Sessão" ADD CONSTRAINT "sessão_id_filme(fk)_foreign" FOREIGN KEY("id_filme(FK)") REFERENCES "Filme"("id_filme");
ALTER TABLE
    "Filme" ADD CONSTRAINT "filme_id_diretor(fk)_foreign" FOREIGN KEY("id_diretor(FK)") REFERENCES "Pessoa_diretor"("id_diretor(PK, FK)");
ALTER TABLE
    "Registro_público" ADD CONSTRAINT "registro_público_id_sessao(fk)_foreign" FOREIGN KEY("id_sessao(FK)") REFERENCES "Sessão"("id_sessao");
ALTER TABLE
    "Pessoa_ator" ADD CONSTRAINT "pessoa_ator_id_pessoa(pk, fk)_foreign" FOREIGN KEY("id_pessoa(PK, FK)") REFERENCES "Pessoa"("id_pessoa");
ALTER TABLE
    "Pessoa_diretor" ADD CONSTRAINT "pessoa_diretor_id_pessoa(pk, fk)_foreign" FOREIGN KEY("id_pessoa(PK, FK)") REFERENCES "Pessoa"("id_pessoa");
ALTER TABLE
    "Filme_Ator" ADD CONSTRAINT "filme_ator_id_filme(pk, fk)_foreign" FOREIGN KEY("id_filme(PK, FK)") REFERENCES "Filme"("id_filme");
ALTER TABLE
    "Filme_Ator" ADD CONSTRAINT "filme_ator_id_ator(pk, fk)_foreign" FOREIGN KEY("id_ator(PK, FK)") REFERENCES "Pessoa_ator"("id_ator(PK, FK)");
ALTER TABLE
    "Sessão" ADD CONSTRAINT "sessão_id_cinema(fk)_foreign" FOREIGN KEY("id_cinema(FK)") REFERENCES "Cinema"("id_cinema");