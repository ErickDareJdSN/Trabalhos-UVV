CREATE TABLE
    emissoras (
        id_emissora SERIAL NOT NULL,
        nome VARCHAR(50) NOT NULL,
        CONSTRAINT pk_emissora PRIMARY KEY (id_emissora)
    );

CREATE TABLE
    novelas (
        id_novela SERIAL NOT NULL,
        id_emissora INT NOT NULL,
        nome VARCHAR(50) NOT NULL,
        resumo TEXT NOT NULL,
        CONSTRAINT pk_novelas PRIMARY KEY (id_novela),
        CONSTRAINT fk_emissoras FOREIGN KEY (id_emissora) REFERENCES emissoras (id_emissora)
    );

CREATE TABLE
    atores (
        id_ator SERIAL NOT NULL,
        id_novela INT NOT NULL,
        cpf_ator VARCHAR(15) NULL,
        nome_ator VARCHAR(100) NOT NULL,
        periodo_atuacao DATE NOT NULL,
        CONSTRAINT pk_atores PRIMARY KEY (id_ator),
        CONSTRAINT fk_novelas FOREIGN KEY (id_novela) REFERENCES novelas (id_novela),
        CONSTRAINT un_atores UNIQUE (cpf_ator)
    );