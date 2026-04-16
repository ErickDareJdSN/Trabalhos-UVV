CREATE TABLE
    enderecos (
        id_endereco SERIAL NOT NULL,
        rua VARCHAR(50) NOT NULL,
        bairro VARCHAR(50) NOT NULL,
        cidade VARCHAR(50) NOT NULL,
        estado VARCHAR(50) NOT NULL,
        cep VARCHAR(9) NOT NULL,
        numero SMALLINT NOT NULL,
        CONSTRAINT pk_enderecos PRIMARY KEY (id_endereco)
    );

CREATE TABLE
    telefones (
        id_telefone SERIAL NOT NULL,
        ddd VARCHAR(5) NOT NULL,
        numero_tel VARCHAR(10) NOT NULL,
        CONSTRAINT pk_telefones PRIMARY KEY (id_telefone)
    );

CREATE TABLE
    alunos (
        id_aluno SERIAL NOT NULL,
        cpf_aluno VARCHAR(15) NOT NULL,
        nome VARCHAR(100) NOT NULL,
        CONSTRAINT pk_alunos PRIMARY KEY (id_aluno),
        CONSTRAINT un_alunos UNIQUE (cpf_aluno)
    );

CREATE TABLE
    professores (
        id_professor SERIAL NOT NULL,
        cpf_professor VARCHAR(15) NOT NULL,
        nome VARCHAR(100) NOT NULL,
        CONSTRAINT pk_professores PRIMARY KEY (id_professor),
        CONSTRAINT un_professores UNIQUE (cpf_professor)
    );

CREATE TABLE
    cursos (
        id_curso SERIAL NOT NULL,
        id_professor INT NOT NULL,
        nome VARCHAR(100) NOT NULL,
        preco DECIMAL(6, 2) NOT NULL,
        duracao INT NOT NULL,
        CONSTRAINT pk_cursos PRIMARY KEY (id_curso),
        CONSTRAINT fk_cursos_professores FOREIGN KEY (id_professor) REFERENCES professores (id_professor)
    );

CREATE TABLE
    matriculas (
        id_matricula SERIAL NOT NULL,
        id_curso INT NOT NULL,
        id_aluno INT NOT NULL,
        data_inicio DATE NOT NULL,
        CONSTRAINT pk_matriculas PRIMARY KEY (id_matricula),
        CONSTRAINT fk_matriculas_cursos FOREIGN KEY (id_curso) REFERENCES cursos (id_curso),
        CONSTRAINT fk_matriculas_alunos FOREIGN KEY (id_aluno) REFERENCES alunos (id_aluno)
    );

CREATE TABLE
    alunos_enderecos (
        id_aluno INT NOT NULL,
        id_endereco INT NOT NULL,
        CONSTRAINT pk_alunos_enderecos PRIMARY KEY (id_aluno, id_endereco),
        CONSTRAINT fk_alunos_enderecos_alunos FOREIGN KEY (id_aluno) REFERENCES alunos (id_aluno),
        CONSTRAINT fk_alunos_enderecos_enderecos FOREIGN KEY (id_endereco) REFERENCES enderecos (id_endereco)
    );

CREATE TABLE
    professores_enderecos (
        id_professor INT NOT NULL,
        id_endereco INT NOT NULL,
        CONSTRAINT pk_professores_enderecos PRIMARY KEY (id_professor, id_endereco),
        CONSTRAINT fk_professores_enderecos_professores FOREIGN KEY (id_professor) REFERENCES professores (id_professor),
        CONSTRAINT fk_professores_enderecos_enderecos FOREIGN KEY (id_endereco) REFERENCES enderecos (id_endereco)
    );

CREATE TABLE
    alunos_telefones (
        id_aluno INT NOT NULL,
        id_telefone INT NOT NULL,
        CONSTRAINT pk_alunos_telefones PRIMARY KEY (id_aluno, id_telefone),
        CONSTRAINT fk_alunos_telefones_alunos FOREIGN KEY (id_aluno) REFERENCES alunos (id_aluno),
        CONSTRAINT fk_alunos_telefones_telefones FOREIGN KEY (id_telefone) REFERENCES telefones (id_telefone)
    );

CREATE TABLE
    professores_telefones (
        id_professor INT NOT NULL,
        id_telefone INT NOT NULL,
        CONSTRAINT pk_professores_telefones PRIMARY KEY (id_professor, id_telefone),
        CONSTRAINT fk_professores_telefones_professores FOREIGN KEY (id_professor) REFERENCES professores (id_professor),
        CONSTRAINT fk_professores_telefones_telefones FOREIGN KEY (id_telefone) REFERENCES telefones (id_telefone)
    );