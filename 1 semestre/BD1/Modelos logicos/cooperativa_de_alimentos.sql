CREATE TABLE "Fornecedores"("CNPJ_f" VARCHAR(14) NOT NULL);
ALTER TABLE
    "Fornecedores" ADD PRIMARY KEY("CNPJ_f");
CREATE TABLE "Itens"(
    "cod"."item" bigserial NOT NULL,
    "quantidade_item" BIGINT NOT NULL,
    "preco_item" FLOAT(53) NOT NULL
);
ALTER TABLE
    "Itens" ADD PRIMARY KEY("cod"."item");
CREATE TABLE "Cooperativa"("CNPJ_c" VARCHAR(14) NOT NULL);
ALTER TABLE
    "Cooperativa" ADD PRIMARY KEY("CNPJ_c");
CREATE TABLE "Associados"(
    "num_associado" bigserial NOT NULL,
    "CPF" VARCHAR(11) NOT NULL,
    "nome" VARCHAR(255) NOT NULL,
    "tel"."" BIGINT NOT NULL,
    "endereco" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Associados" ADD PRIMARY KEY("num_associado");
ALTER TABLE
    "Associados" ADD CONSTRAINT "associados_cpf_unique" UNIQUE("CPF");
CREATE TABLE "Cestas"(
    "num_pedido" bigserial NOT NULL,
    "num_associado" bigserial NOT NULL,
    "CNPJ_c" VARCHAR(14) NOT NULL,
    "nota_entrega" BIGINT NOT NULL
);
ALTER TABLE
    "Cestas" ADD PRIMARY KEY("num_pedido");
ALTER TABLE
    "Cestas" ADD PRIMARY KEY("num_associado");
ALTER TABLE
    "Cestas" ADD PRIMARY KEY("CNPJ_c");
ALTER TABLE
    "Cestas" ADD CONSTRAINT "cestas_nota_entrega_unique" UNIQUE("nota_entrega");
CREATE TABLE "Entregas"(
    "CNPJ_c" VARCHAR(14) NOT NULL,
    "num_nota" bigserial NOT NULL,
    "CNPJ_f" BIGINT NOT NULL,
    "cod"."item" BIGINT NOT NULL,
    "quantidade_item" BIGINT NOT NULL,
    "preco_item" FLOAT(53) NOT NULL,
    "valor_total" FLOAT(53) NOT NULL
);
ALTER TABLE
    "Entregas" ADD PRIMARY KEY("CNPJ_c");
ALTER TABLE
    "Entregas" ADD PRIMARY KEY("num_nota");
ALTER TABLE
    "Entregas" ADD PRIMARY KEY("CNPJ_f");
ALTER TABLE
    "Entregas" ADD PRIMARY KEY("cod"."item");
CREATE TABLE "Pedidos"(
    "CNPJ_c" VARCHAR(14) NOT NULL,
    "num_associado" bigserial NOT NULL,
    "num_pedido" bigserial NOT NULL,
    "nota_entrega" BIGINT NOT NULL,
    "CPF" VARCHAR(11) NOT NULL,
    "nome" VARCHAR(255) NOT NULL,
    "tel"."" BIGINT NOT NULL,
    "endereco" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Pedidos" ADD PRIMARY KEY("CNPJ_c");
ALTER TABLE
    "Pedidos" ADD PRIMARY KEY("num_associado");
ALTER TABLE
    "Pedidos" ADD PRIMARY KEY("num_pedido");
ALTER TABLE
    "Pedidos" ADD CONSTRAINT "pedidos_nota_entrega_unique" UNIQUE("nota_entrega");
ALTER TABLE
    "Pedidos" ADD CONSTRAINT "pedidos_cpf_unique" UNIQUE("CPF");
ALTER TABLE
    "Cooperativa" ADD CONSTRAINT "cooperativa_cnpj_c_foreign" FOREIGN KEY("CNPJ_c") REFERENCES "Entregas"("CNPJ_c");
ALTER TABLE
    "Cestas" ADD CONSTRAINT "cestas_num_associado_foreign" FOREIGN KEY("num_associado") REFERENCES "Pedidos"("endereco");
ALTER TABLE
    "Entregas" ADD CONSTRAINT "entregas_num_nota_foreign" FOREIGN KEY("num_nota") REFERENCES "Fornecedores"("CNPJ_f");
ALTER TABLE
    "Pedidos" ADD CONSTRAINT "pedidos_nome_foreign" FOREIGN KEY("nome") REFERENCES "Associados"("nome");
ALTER TABLE
    "Entregas" ADD CONSTRAINT "entregas_cod_item_foreign" FOREIGN KEY("cod"."item") REFERENCES "Itens"("preco_item");
ALTER TABLE
    "Pedidos" ADD CONSTRAINT "pedidos_nota_entrega_foreign" FOREIGN KEY("nota_entrega") REFERENCES "Cooperativa"("CNPJ_c");