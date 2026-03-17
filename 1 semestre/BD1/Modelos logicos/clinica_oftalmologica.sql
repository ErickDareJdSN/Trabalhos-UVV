CREATE TABLE "Médico"(
    "CRM" VARCHAR(255) NOT NULL,
    "nome_m" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Médico" ADD PRIMARY KEY("CRM");
CREATE TABLE "Paciente"(
    "CPF" VARCHAR(255) NOT NULL,
    "nome_p" VARCHAR(255) NOT NULL,
    "sigla_plano(FK)" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Paciente" ADD PRIMARY KEY("CPF");
CREATE TABLE "Consulta"(
    "id_consulta" SERIAL NOT NULL,
    "CRM(FK)" VARCHAR(255) NOT NULL,
    "CPF(FK)" VARCHAR(255) NOT NULL,
    "data" DATE NOT NULL
);
ALTER TABLE
    "Consulta" ADD PRIMARY KEY("id_consulta");
CREATE TABLE "Exame"(
    "codigo" SERIAL NOT NULL,
    "nome" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Exame" ADD PRIMARY KEY("codigo");
CREATE TABLE "Exame_clínico"(
    "codigo(PK, FK)" INTEGER NOT NULL,
    "CRM(FK)" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Exame_clínico" ADD PRIMARY KEY("codigo(PK, FK)");
CREATE TABLE "Exame_laboratorial"(
    "codigo(PK, FK)" INTEGER NOT NULL
);
ALTER TABLE
    "Exame_laboratorial" ADD PRIMARY KEY("codigo(PK, FK)");
CREATE TABLE "Plano"(
    "sigla" VARCHAR(255) NOT NULL,
    "nome" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Plano" ADD PRIMARY KEY("sigla");
CREATE TABLE "Exame_paciente"(
    "codigo(PK, FK)" INTEGER NOT NULL,
    "CPF(PK, FK)" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Exame_paciente" ADD PRIMARY KEY("codigo(PK, FK)");
ALTER TABLE
    "Exame_paciente" ADD PRIMARY KEY("CPF(PK, FK)");
ALTER TABLE
    "Exame_clínico" ADD CONSTRAINT "exame_clínico_codigo(pk, fk)_foreign" FOREIGN KEY("codigo(PK, FK)") REFERENCES "Médico"("nome_m");
ALTER TABLE
    "Exame_paciente" ADD CONSTRAINT "exame_paciente_cpf(pk, fk)_foreign" FOREIGN KEY("CPF(PK, FK)") REFERENCES "Paciente"("nome_p");
ALTER TABLE
    "Exame_clínico" ADD CONSTRAINT "exame_clínico_codigo(pk, fk)_foreign" FOREIGN KEY("codigo(PK, FK)") REFERENCES "Exame"("codigo");
ALTER TABLE
    "Consulta" ADD CONSTRAINT "consulta_cpf(fk)_foreign" FOREIGN KEY("CPF(FK)") REFERENCES "Paciente"("CPF");
ALTER TABLE
    "Paciente" ADD CONSTRAINT "paciente_sigla_plano(fk)_foreign" FOREIGN KEY("sigla_plano(FK)") REFERENCES "Plano"("nome");
ALTER TABLE
    "Plano" ADD CONSTRAINT "plano_sigla_foreign" FOREIGN KEY("sigla") REFERENCES "Paciente"("CPF");
ALTER TABLE
    "Exame_paciente" ADD CONSTRAINT "exame_paciente_codigo(pk, fk)_foreign" FOREIGN KEY("codigo(PK, FK)") REFERENCES "Exame"("codigo");
ALTER TABLE
    "Exame_laboratorial" ADD CONSTRAINT "exame_laboratorial_codigo(pk, fk)_foreign" FOREIGN KEY("codigo(PK, FK)") REFERENCES "Exame"("nome");
ALTER TABLE
    "Consulta" ADD CONSTRAINT "consulta_crm(fk)_foreign" FOREIGN KEY("CRM(FK)") REFERENCES "Médico"("CRM");