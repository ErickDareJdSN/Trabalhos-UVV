CREATE TABLE
    funcionarios (
        ra SERIAL NOT NULL,
        cpf VARCHAR(15) NOT NULL,
        nome VARCHAR(100) NOT NULL,
        sexo CHAR(1) NOT NULL,
        nacionalidade VARCHAR(50) NOT NULL,
        data_nascimento DATE NOT NULL,
        CONSTRAINT pk_funcionarios PRIMARY KEY (ra),
        CONSTRAINT un_funcionarios_cpf UNIQUE (cpf)
    );

CREATE TABLE
    cursos (
        id SERIAL NOT NULL,
        nome VARCHAR(100) NOT NULL,
        CONSTRAINT pk_cursos PRIMARY KEY (id)
    );

CREATE TABLE
    enderecos (
        id SERIAL NOT NULL,
        rua VARCHAR(100) NOT NULL,
        numero SMALLINT NOT NULL,
        bairro VARCHAR(50) NOT NULL,
        cidade VARCHAR(100) NOT NULL,
        cep VARCHAR(9) NOT NULL,
        CONSTRAINT pk_enderecos PRIMARY KEY (id)
    );

CREATE TABLE
    telefones (
        id SERIAL NOT NULL,
        ra INT NOT NULL,
        ddi CHAR(5) NOT NULL,
        ddd CHAR(3) NOT NULL,
        numero VARCHAR(9) NOT NULL,
        CONSTRAINT pk_telefones PRIMARY KEY (id),
        CONSTRAINT fk_telefones_funcionarios FOREIGN KEY (ra) REFERENCES funcionarios (ra)
    );

CREATE TABLE
    funcionarios_enderecos (
        ra INT NOT NULL,
        endereco_id INT NOT NULL,
        CONSTRAINT pk_funcionarios_enderecos PRIMARY KEY (ra, endereco_id),
        CONSTRAINT fk_funcionarios_enderecos_funcionario FOREIGN KEY (ra) REFERENCES funcionarios (ra),
        CONSTRAINT fk_funcionarios_enderecos_endereco FOREIGN KEY (endereco_id) REFERENCES enderecos (id)
    );

CREATE TABLE
    matricula (
        ra INT NOT NULL,
        curso_id INT NOT NULL,
        inscricao TIMESTAMP NOT NULL,
        termino TIMESTAMP NOT NULL,
        CONSTRAINT pk_matricula PRIMARY KEY (ra, curso_id),
        CONSTRAINT fk_matricula_funcionario FOREIGN KEY (ra) REFERENCES funcionarios (ra),
        CONSTRAINT fk_matricula_curso FOREIGN KEY (curso_id) REFERENCES cursos (id)
    );