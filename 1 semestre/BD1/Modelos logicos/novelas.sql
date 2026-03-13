CREATE TABLE "Novelas"(
    "cod"."novela" bigserial NOT NULL,
    "nome" VARCHAR(255) NOT NULL,
    "resumo" TEXT NOT NULL
);
ALTER TABLE
    "Novelas" ADD PRIMARY KEY("cod"."novela");
CREATE TABLE "Emissora"(
    "num_emissora" BIGINT NOT NULL,
    "nome" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Emissora" ADD PRIMARY KEY("num_emissora");
CREATE TABLE "Atores"(
    "CPF" bigserial NOT NULL,
    "cod"."novela" bigserial NOT NULL,
    "nome" VARCHAR(255) NOT NULL,
    "data_atuacao" DATE NOT NULL
);
ALTER TABLE
    "Atores" ADD PRIMARY KEY("CPF");
ALTER TABLE
    "Atores" ADD PRIMARY KEY("cod"."novela");
ALTER TABLE
    "Novelas" ADD CONSTRAINT "novelas_nome_foreign" FOREIGN KEY("nome") REFERENCES "Emissora"("num_emissora");
ALTER TABLE
    "Atores" ADD CONSTRAINT "atores_cpf_foreign" FOREIGN KEY("CPF") REFERENCES "Novelas"("cod"."novela");