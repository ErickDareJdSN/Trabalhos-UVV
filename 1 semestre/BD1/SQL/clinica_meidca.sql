CREATE TABLE
    enderecos (
        id_endereco SERIAL NOT NULL,
        rua VARCHAR(100) NOT NULL,
        numero SMALLINT NOT NULL,
        bairro VARCHAR(50) NOT NULL,
        cep VARCHAR(10) NOT NULL,
        CONSTRAINT pk_enderecos PRIMARY KEY (id_endereco),
    );

CREATE TABLE
    telefones (
        id_telefone SERIAL NOT NULL,
        ddd VARCHAR NOT NULL,
        numero VARCHAR(10) NOT NULL,
        CONSTRAINT pk_telefones PRIMARY KEY (id_telefone)
    );

CREATE TABLE
    medicos (
        id_medico SERIAL NOT NULL,
        crm VARCHAR NOT NULL,
        nome_medico VARCHAR(100) NOT NULL,
        id_endereco INT NOT NULL,
        id_telefone INT NOT NULL,
        CONSTRAINT pk_medicos PRIMARY KEY (id_medico),
        CONSTRAINT un_medicos UNIQUE (crm),
        CONSTRAINT fk_medicos_endereco FOREIGN KEY (id_endereco) REFERENCES enderecos (id_endereco),
        CONSTRAINT fk_medicos_telefone FOREIGN KEY (id_telefone) REFERENCES telefones (id_telefone)
    );

CREATE TABLE
    pacientes (
        id_paciente SERIAL NOT NULL,
        cpf VARCHAR(11) NOT NULL,
        rg VARCHAR(20) NOT NULL,
        nome_paciente VARCHAR(100) NOT NULL,
        id_endereco INT NOT NULL,
        id_telefone INT NOT NULL,
        CONSTRAINT pk_pacientes PRIMARY KEY (id_paciente),
        CONSTRAINT un_pacientes_cpf UNIQUE (cpf),
        CONSTRAINT un_pacientes_rg UNIQUE (rg),
        CONSTRAINT fk_pacientes_endereco FOREIGN KEY (id_endereco) REFERENCES enderecos (id_endereco),
        CONSTRAINT fk_pacientes_telefone FOREIGN KEY (id_telefone) REFERENCES telefones (id_telefones)
    );

CREATE TABLE
    consultas (
        id_consulta SERIAL NOT NULL,
        data_consulta DATE NOT NULL,
        descricao TEXT NOT NULL,
        id_medico INT NOT NULL,
        id_paciente INT NOT NULL,
        CONSTRAINT pk_consultas PRIMARY KEY (id_consulta),
        CONSTRAINT fk_consultas_medico FOREIGN KEY (id_medico) REFERENCES medicos (id_medico),
        CONSTRAINT fk_consultas_paciente FOREIGN KEY (id_paciente) REFERENCES pacientes (id_paciente)
    );

CREATE TABLE
    receitas (
        id_receita SERIAL NOT NULL,
        id_consulta INT NOT NULL,
        descricao TEXT NOT NULL,
        data_receita DATE NOT NULL,
        custo_receita DECIMAL(8, 2) NOT NULL,
        CONSTRAINT pk_receitas PRIMARY KEY (id_receita),
        CONSTRAINT fk_receitas FOREIGN KEY (id_consulta) REFERENCES consultas (id_consulta)
    );

CREATE TABLE
    fabricantes (
        id_fabricante SERIAL NOT NULL,
        cnpj VARCHAR(14) NOT NULL,
        nome_fabricante VARCHAR(100) NOT NULL,
        CONSTRAINT pk_fabricantes PRIMARY KEY (id_fabricante)
    );

CREATE TABLE
    enderecos_fabricantes (
        id_endereco INT NOT NULL,
        id_fabricante INT NOT NULL,
        CONSTRAINT pk_enderecos_fabricantes PRIMARY KEY (id_endereco, id_fabricante),
        CONSTRAINT fk_enderecos_fabricantes_endereco FOREIGN KEY (id_endereco) REFERENCES enderecos (id_endereco),
        CONSTRAINT fk_enderecos_fabricantes_fabricante FOREIGN KEY (id_fabricante) REFERENCES fabricantes (id_fabricante)
    );

CREATE TABLE
    tipos_medicamentos (
        id_tipo SERIAL NOT NULL,
        nome_tipo VARCHAR(50) NOT NULL,
        CONSTRAINT pk_tipos_medicamentos PRIMARY KEY (id_tipo)
    );

CREATE TABLE
    medicamentos (
        id_medicamento SERIAL NOT NULL,
        rf VARCHAR(10) NOT NULL,
        preco_medicamento DECIMAL(8, 2) NOT NULL,
        nome_medicamento VARCHAR(50) NOT NULL,
        id_fabricante INT NOT NULL,
        id_tipo INT NOT NULL,
        CONSTRAINT pk_medicamentos PRIMARY KEY (id_medicamento),
        CONSTRAINT fk_medicamentos_fabricante FOREIGN KEY (id_fabricante) REFERENCES fabricantes (id_fabricante),
        CONSTRAINT fk_medicamentos_tipo FOREIGN KEY (id_tipo) REFERENCES tipos_medicamentos (id_tipo)
    );

CREATE TABLE
    receitas_medicamentos (
        id_receita INT NOT NULL,
        id_medicamento INT NOT NULL,
        posologia VARCHAR NOT NULL,
        modo_uso TEXT NOT NULL,
        quantidade SMALLINT NOT NULL,
        CONSTRAINT pk_receitas_medicamentos PRIMARY KEY 
    );