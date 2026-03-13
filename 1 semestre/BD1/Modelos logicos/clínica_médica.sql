CREATE TABLE "Clínica"(
    "CNPJ_c" VARCHAR(14) NOT NULL,
    "nome" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Clínica" ADD PRIMARY KEY("CNPJ_c");
CREATE TABLE "Médicos"(
    "CRM" VARCHAR(6) NOT NULL,
    "CNPJ_c" VARCHAR(14) NOT NULL,
    "nome_med" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Médicos" ADD PRIMARY KEY("CRM");
ALTER TABLE
    "Médicos" ADD PRIMARY KEY("CNPJ_c");
CREATE TABLE "Pacientes"(
    "CPF" VARCHAR(11) NOT NULL,
    "RG" VARCHAR(15) NOT NULL,
    "nome_cliente" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Pacientes" ADD PRIMARY KEY("CPF");
ALTER TABLE
    "Pacientes" ADD CONSTRAINT "pacientes_rg_unique" UNIQUE("RG");
CREATE TABLE "Fabricante"(
    "CNPJ_f" VARCHAR(14) NOT NULL,
    "nome" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Fabricante" ADD PRIMARY KEY("CNPJ_f");
CREATE TABLE "Medicamentos"(
    "RF" VARCHAR(13) NOT NULL,
    "CNPJ_f" VARCHAR(14) NOT NULL,
    "nome" VARCHAR(255) NOT NULL,
    "tipo" VARCHAR(20) NOT NULL,
    "preco" FLOAT(53) NOT NULL
);
ALTER TABLE
    "Medicamentos" ADD PRIMARY KEY("RF");
ALTER TABLE
    "Medicamentos" ADD PRIMARY KEY("CNPJ_f");
CREATE TABLE "Consultas"(
    "cod"."consulta" bigserial NOT NULL,
    "CRM" VARCHAR(6) NOT NULL,
    "CPF" VARCHAR(11) NOT NULL,
    "data" DATE NOT NULL,
    "descricao" TEXT NOT NULL
);
ALTER TABLE
    "Consultas" ADD PRIMARY KEY("cod"."consulta");
ALTER TABLE
    "Consultas" ADD PRIMARY KEY("CRM");
ALTER TABLE
    "Consultas" ADD PRIMARY KEY("CPF");
CREATE TABLE "Receitas"(
    "num_receita" bigserial NOT NULL,
    "cod"."consulta" bigserial NOT NULL,
    "descricao" TEXT NOT NULL,
    "data" DATE NOT NULL
);
ALTER TABLE
    "Receitas" ADD PRIMARY KEY("num_receita");
ALTER TABLE
    "Receitas" ADD PRIMARY KEY("cod"."consulta");
CREATE TABLE "Prescrições"(
    "num_prescricao" bigserial NOT NULL,
    "num_receita" bigserial NOT NULL,
    "RF" VARCHAR(13) NOT NULL,
    "modo_usos" TEXT NOT NULL,
    "quantidade" INTEGER NOT NULL,
    "posologia" TEXT NOT NULL
);
ALTER TABLE
    "Prescrições" ADD PRIMARY KEY("num_prescricao");
ALTER TABLE
    "Prescrições" ADD PRIMARY KEY("num_receita");
ALTER TABLE
    "Prescrições" ADD PRIMARY KEY("RF");
ALTER TABLE
    "Consultas" ADD CONSTRAINT "consultas_cod_consulta_foreign" FOREIGN KEY("cod"."consulta") REFERENCES "Receitas"("num_receita");
ALTER TABLE
    "Medicamentos" ADD CONSTRAINT "medicamentos_cnpj_f_foreign" FOREIGN KEY("CNPJ_f") REFERENCES "Prescrições"("RF");
ALTER TABLE
    "Consultas" ADD CONSTRAINT "consultas_cpf_foreign" FOREIGN KEY("CPF") REFERENCES "Pacientes"("RG");
ALTER TABLE
    "Fabricante" ADD CONSTRAINT "fabricante_cnpj_f_foreign" FOREIGN KEY("CNPJ_f") REFERENCES "Medicamentos"("nome");
ALTER TABLE
    "Médicos" ADD CONSTRAINT "médicos_cnpj_c_foreign" FOREIGN KEY("CNPJ_c") REFERENCES "Clínica"("CNPJ_c");
ALTER TABLE
    "Receitas" ADD CONSTRAINT "receitas_cod_consulta_foreign" FOREIGN KEY("cod"."consulta") REFERENCES "Prescrições"("modo_usos");
ALTER TABLE
    "Consultas" ADD CONSTRAINT "consultas_crm_foreign" FOREIGN KEY("CRM") REFERENCES "Médicos"("CNPJ_c");