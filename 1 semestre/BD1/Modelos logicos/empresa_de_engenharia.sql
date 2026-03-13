CREATE TABLE "Engenheiros"(
    "CREA" BIGINT NOT NULL,
    "nome" VARCHAR(255) NOT NULL,
    "endereco" VARCHAR(255) NOT NULL,
    "tel"."" BIGINT NOT NULL,
    "salario" BIGINT NOT NULL
);
ALTER TABLE
    "Engenheiros" ADD PRIMARY KEY("CREA");
CREATE TABLE "Projetos"(
    "num"."projeto" BIGINT NOT NULL,
    "duracao" TIME(0) WITHOUT TIME ZONE NOT NULL,
    "descricao" VARCHAR(255) NOT NULL,
    "local" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Projetos" ADD PRIMARY KEY("num"."projeto");
CREATE TABLE "Equipamentos"(
    "cod"."equipamento" BIGINT NOT NULL,
    "num"."projeto" BIGINT NOT NULL,
    "desc"."equipamento" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Equipamentos" ADD PRIMARY KEY("cod"."equipamento");
ALTER TABLE
    "Equipamentos" ADD PRIMARY KEY("num"."projeto");
CREATE TABLE "Ativos"(
    "CREA" BIGINT NOT NULL,
    "num"."projeto" BIGINT NOT NULL
);
ALTER TABLE
    "Ativos" ADD PRIMARY KEY("CREA");
ALTER TABLE
    "Ativos" ADD PRIMARY KEY("num"."projeto");
ALTER TABLE
    "Ativos" ADD CONSTRAINT "ativos_crea_foreign" FOREIGN KEY("CREA") REFERENCES "Engenheiros"("CREA");
ALTER TABLE
    "Equipamentos" ADD CONSTRAINT "equipamentos_cod_equipamento_foreign" FOREIGN KEY("cod"."equipamento") REFERENCES "Projetos"("duracao");
ALTER TABLE
    "Ativos" ADD CONSTRAINT "ativos_num_projeto_foreign" FOREIGN KEY("num"."projeto") REFERENCES "Projetos"("duracao");