CREATE TABLE "Curso"(
    "cod"."curso" BIGINT NOT NULL,
    "nome_curso" BIGINT NOT NULL,
    "preco" BIGINT NOT NULL,
    "cpf_prof" BIGINT NOT NULL,
    "cpf_alu" BIGINT NOT NULL
);
ALTER TABLE
    "Curso" ADD PRIMARY KEY("cod"."curso");
ALTER TABLE
    "Curso" ADD PRIMARY KEY("cpf_prof");
ALTER TABLE
    "Curso" ADD PRIMARY KEY("cpf_alu");
CREATE TABLE "Professor"(
    "cpf_prof" BIGINT NOT NULL,
    "telefone" BIGINT NOT NULL,
    "nome" BIGINT NOT NULL,
    "endereco" BIGINT NOT NULL,
    "sexo" BIGINT NOT NULL
);
ALTER TABLE
    "Professor" ADD PRIMARY KEY("cpf_prof");
ALTER TABLE
    "Professor" ADD CONSTRAINT "professor_telefone_unique" UNIQUE("telefone");
CREATE TABLE "Estudante"(
    "cpf_alu" BIGINT NOT NULL,
    "telefone" BIGINT NOT NULL,
    "nome" BIGINT NOT NULL,
    "endereco" BIGINT NOT NULL,
    "sexo" BIGINT NOT NULL
);
ALTER TABLE
    "Estudante" ADD PRIMARY KEY("cpf_alu");
ALTER TABLE
    "Estudante" ADD CONSTRAINT "estudante_telefone_unique" UNIQUE("telefone");
CREATE TABLE "Matricula"(
    "cod"."curso" BIGINT NOT NULL,
    "cpf_alu" BIGINT NOT NULL
);
ALTER TABLE
    "Matricula" ADD PRIMARY KEY("cod"."curso");
ALTER TABLE
    "Matricula" ADD PRIMARY KEY("cpf_alu");