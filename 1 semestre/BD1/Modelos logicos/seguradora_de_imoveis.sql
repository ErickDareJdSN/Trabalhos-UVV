CREATE TABLE "Cliente"(
    "cod"."cliente" BIGINT NOT NULL,
    "nome" BIGINT NOT NULL,
    "endereco" BIGINT NOT NULL
);
ALTER TABLE
    "Cliente" ADD PRIMARY KEY("cod"."cliente");
CREATE TABLE "Carro"(
    "registro" BIGINT NOT NULL,
    "marca" BIGINT NOT NULL,
    "modelo" BIGINT NOT NULL
);
ALTER TABLE
    "Carro" ADD PRIMARY KEY("registro");
CREATE TABLE "Apólice"(
    "num"."apolice" BIGINT NOT NULL,
    "cod"."cliente" BIGINT NOT NULL,
    "registro" BIGINT NOT NULL,
    "valor" BIGINT NOT NULL
);
ALTER TABLE
    "Apólice" ADD PRIMARY KEY("num"."apolice");
ALTER TABLE
    "Apólice" ADD PRIMARY KEY("cod"."cliente");
ALTER TABLE
    "Apólice" ADD PRIMARY KEY("registro");
CREATE TABLE "Acidente"(
    "num"."acidente" BIGINT NOT NULL,
    "registro" BIGINT NOT NULL,
    "data" BIGINT NOT NULL,
    "hora" BIGINT NOT NULL,
    "local" BIGINT NOT NULL
);
ALTER TABLE
    "Acidente" ADD PRIMARY KEY("num"."acidente");
ALTER TABLE
    "Acidente" ADD PRIMARY KEY("registro");