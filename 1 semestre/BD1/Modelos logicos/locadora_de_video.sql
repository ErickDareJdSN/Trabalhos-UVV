CREATE TABLE "Cliente"(
    "num_associado" BIGINT NOT NULL,
    "RG" VARCHAR(15) NOT NULL,
    "nome" VARCHAR(255) NOT NULL,
    "tel"."" VARCHAR(20) NOT NULL,
    "endereco" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Cliente" ADD PRIMARY KEY("num_associado");
ALTER TABLE
    "Cliente" ADD CONSTRAINT "cliente_rg_unique" UNIQUE("RG");
CREATE TABLE "Filmes"(
    "cod"."filme" BIGINT NOT NULL,
    "titulo" VARCHAR(255) NOT NULL,
    "categoria" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Filmes" ADD PRIMARY KEY("cod"."filme");
CREATE TABLE "Atores"(
    "num_ator" BIGINT NOT NULL,
    "nome_real" VARCHAR(255) NOT NULL,
    "data_nascimento" DATE NOT NULL
);
ALTER TABLE
    "Atores" ADD PRIMARY KEY("num_ator");
CREATE TABLE "Fitas"(
    "num_fita" BIGINT NOT NULL,
    "cod"."filme" BIGINT NOT NULL,
    "prateleira" BIGINT NOT NULL
);
ALTER TABLE
    "Fitas" ADD PRIMARY KEY("num_fita");
ALTER TABLE
    "Fitas" ADD PRIMARY KEY("cod"."filme");
CREATE TABLE "Atuações"(
    "cod"."filme, num_ator" BIGINT NOT NULL
);
ALTER TABLE
    "Atuações" ADD PRIMARY KEY("cod"."filme, num_ator");
CREATE TABLE "Locação"(
    "num_associado, num_fita" BIGINT NOT NULL,
    "data_locacao" DATE NOT NULL
);
ALTER TABLE
    "Locação" ADD PRIMARY KEY("num_associado, num_fita");
ALTER TABLE
    "Locação" ADD CONSTRAINT "locação_data_locacao_foreign" FOREIGN KEY("data_locacao") REFERENCES "Cliente"("RG");
ALTER TABLE
    "Locação" ADD CONSTRAINT "locação_data_locacao_foreign" FOREIGN KEY("data_locacao") REFERENCES "Fitas"("num_fita");
ALTER TABLE
    "Fitas" ADD CONSTRAINT "fitas_cod_filme_foreign" FOREIGN KEY("cod"."filme") REFERENCES "Filmes"("cod"."filme");
ALTER TABLE
    "Atuações" ADD CONSTRAINT "atuações_cod_filme, num_ator_foreign" FOREIGN KEY("cod"."filme, num_ator") REFERENCES "Filmes"("titulo");
ALTER TABLE
    "Atuações" ADD CONSTRAINT "atuações_cod_filme, num_ator_foreign" FOREIGN KEY("cod"."filme, num_ator") REFERENCES "Atores"("num_ator");