CREATE TABLE
    engenheiros (
        crea_engen SERIAL NOT NULL,
        nome VARCHAR(50) NOT NULL,
        salario DECIMAL(10, 2) NOT NULL,
        CONSTRAINT pk_engenheiro PRIMARY KEY (crea_engen)
    );

CREATE TABLE
    telefones (
        id_telefone SERIAL NOT NULL,
        ddd VARCHAR NOT NULL,
        numero VARCHAR NOT NULL,
        crea_engen INT NOT NULL,
        CONSTRAINT pk_telefones PRIMARY KEY (id_telefone),
        CONSTRAINT fk_telefones FOREIGN KEY (crea_engen) REFERENCES engenheiros (crea_engen)
    );

CREATE TABLE
    enderecos (
        id_endereco SERIAL NOT NULL,
        rua VARCHAR(100) NOT NULL,
        bairro VARCHAR(50) NOT NULL,
        numero SMALLINT NOT NULL,
        CONSTRAINT pk_enderecos PRIMARY KEY (id_endereco)
    );

CREATE TABLE
    engenheiros_enderecos (
        crea_engen INT NOT NULL,
        id_endereco INT NOT NULL,
        CONSTRAINT pk_engenheiros_enderecos PRIMARY KEY (crea_engen, id_endereco),
        CONSTRAINT fk_engenheiros_enderecos_engenheiro FOREIGN KEY (crea_engen) REFERENCES engenheiros (crea_engen),
        CONSTRAINT fk_engenheiros_enderecos_endereco FOREIGN KEY (id_endereco) REFERENCES enderecos (id_endereco)
    );

CREATE TABLE
    projetos (
        id_projeto SERIAL NOT NULL,
        duracao INT NOT NULL,
        descricao TEXT NOT NULL,
        CONSTRAINT pk_projetos PRIMARY KEY (id_projeto)
    );

CREATE TABLE
    atuacao (
        crea_engen INT NOT NULL,
        id_projeto INT NOT NULL,
        funcao VARCHAR(50) NOT NULL,
        qtd_horas INT NOT NULL,
        CONSTRAINT pk_atuacao PRIMARY KEY (crea_engen, id_projeto),
        CONSTRAINT fk_atuacao_engenheiro FOREIGN KEY (crea_engen) REFERENCES engenheiros (crea_engen),
        CONSTRAINT fk_atuacao_projeto FOREIGN KEY (id_projeto) REFERENCES projetos (id_projeto)
    );

CREATE TABLE
    enderecos_projetos (
        id_endereco INT NOT NULL,
        id_projeto INT NOT NULL,
        CONSTRAINT pk_enderecos_projetos PRIMARY KEY (id_endereco, id_projeto),
        CONSTRAINT fk_enderecos_projetos_endereco FOREIGN KEY (id_endereco) REFERENCES enderecos (id_endereco),
        CONSTRAINT fk_enderecos_projetos_projeto FOREIGN KEY (id_projeto) REFERENCES projetos (id_projeto)
    );

CREATE TABLE
    equipamentos (
        id_equipamento SERIAL NOT NULL,
        descricao TEXT NOT NULL,
        id_projeto INT NOT NULL,
        CONSTRAINT pk_equipamentos PRIMARY KEY (id_equipamento),
        CONSTRAINT fk_equipamentos FOREIGN KEY (id_projeto) REFERENCES projetos (id_projeto)
    );