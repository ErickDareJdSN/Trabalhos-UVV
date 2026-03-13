CREATE TABLE "Carros"(
    "num_licensa_placa" bigserial NOT NULL,
    "id_veiculo" bigserial NOT NULL,
    "vel"."maxima" BIGINT NOT NULL,
    "quant"."passageiros" BIGINT NOT NULL
);
ALTER TABLE
    "Carros" ADD PRIMARY KEY("num_licensa_placa");
ALTER TABLE
    "Carros" ADD PRIMARY KEY("id_veiculo");
CREATE TABLE "Caminhões"(
    "num_licensa_placa" bigserial NOT NULL,
    "id_veiculo" bigserial NOT NULL,
    "n"."eixos" BIGINT NOT NULL,
    "capacidade" FLOAT(53) NOT NULL
);
ALTER TABLE
    "Caminhões" ADD PRIMARY KEY("num_licensa_placa");
ALTER TABLE
    "Caminhões" ADD PRIMARY KEY("id_veiculo");
CREATE TABLE "Veículos"(
    "num_licensa_placa" bigserial NOT NULL,
    "id_veiculo" bigserial NOT NULL,
    "preco" FLOAT(53) NOT NULL
);
ALTER TABLE
    "Veículos" ADD PRIMARY KEY("num_licensa_placa");
ALTER TABLE
    "Veículos" ADD PRIMARY KEY("id_veiculo");
ALTER TABLE
    "Carros" ADD CONSTRAINT "carros_num_licensa_placa_foreign" FOREIGN KEY("num_licensa_placa") REFERENCES "Veículos"("num_licensa_placa");
ALTER TABLE
    "Caminhões" ADD CONSTRAINT "caminhões_num_licensa_placa_foreign" FOREIGN KEY("num_licensa_placa") REFERENCES "Veículos"("id_veiculo");