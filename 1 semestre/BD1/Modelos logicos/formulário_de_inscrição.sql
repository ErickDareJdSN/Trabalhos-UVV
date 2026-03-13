CREATE TABLE "Funcionário"(
    "R"."A"."" BIGINT NOT NULL,
    "nome" VARCHAR(255) NOT NULL,
    "Idade" INTEGER NOT NULL,
    "nacionalidade" VARCHAR(255) NOT NULL,
    "sexo" VARCHAR(255) NOT NULL,
    "tel"."" BIGINT NOT NULL,
    "endereco" BIGINT NOT NULL
);
ALTER TABLE
    "Funcionário" ADD PRIMARY KEY("R"."A"."");
CREATE TABLE "Cursos"(
    "cod"."curso" BIGINT NOT NULL,
    "nome" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Cursos" ADD PRIMARY KEY("cod"."curso");
CREATE TABLE "Inscrição"(
    "cod"."curso" BIGINT NOT NULL,
    "R"."A"."" BIGINT NOT NULL,
    "nome" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Inscrição" ADD PRIMARY KEY("cod"."curso");
ALTER TABLE
    "Inscrição" ADD PRIMARY KEY("R"."A"."");
ALTER TABLE
    "Inscrição" ADD CONSTRAINT "inscrição_r_a__foreign" FOREIGN KEY("R"."A"."") REFERENCES "Cursos"("cod"."curso");
ALTER TABLE
    "Inscrição" ADD CONSTRAINT "inscrição_cod_curso_foreign" FOREIGN KEY("cod"."curso") REFERENCES "Funcionário"("nome");