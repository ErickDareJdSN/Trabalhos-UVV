CREATE TABLE Participante (
    email VARCHAR PRIMARY KEY,
    nome VARCHAR NOT NULL,
    instituicao VARCHAR,
    endereco VARCHAR,
    telefone VARCHAR,
    categoria VARCHAR NOT NULL
);

CREATE TABLE Autor (
    nome VARCHAR PRIMARY KEY,
    instituicao VARCHAR
);

CREATE TABLE Autor_Participante (
    nome_autor VARCHAR,
    email_participante VARCHAR,
    PRIMARY KEY (nome_autor, email_participante),
    FOREIGN KEY (nome_autor) REFERENCES Autor(nome),
    FOREIGN KEY (email_participante) REFERENCES Participante(email)
);

CREATE TABLE Revisor (
    nome VARCHAR PRIMARY KEY,
    email VARCHAR UNIQUE NOT NULL,
    instituicao VARCHAR UNIQUE,
    endereco VARCHAR,
    telefone VARCHAR,
    fax VARCHAR
);

CREATE TABLE Artigo (
    codigo SERIAL PRIMARY KEY,
    titulo VARCHAR NOT NULL,
    email_primeiro_autor VARCHAR,
    status VARCHAR
);

CREATE TABLE Local (
    nome VARCHAR PRIMARY KEY,
    capacidade INT NOT NULL
);

CREATE TABLE Atividade (
    id_atividade SERIAL PRIMARY KEY,
    data_inicio TIMESTAMP NOT NULL,
    data_fim TIMESTAMP NOT NULL,
    nome_local VARCHAR,
    responsavel VARCHAR,
    FOREIGN KEY (nome_local) REFERENCES Local(nome),
    FOREIGN KEY (responsavel) REFERENCES Participante(email)
);

CREATE TABLE Sessao (
    id_atividade INT PRIMARY KEY,
    nome VARCHAR UNIQUE,
    FOREIGN KEY (id_atividade) REFERENCES Atividade(id_atividade)
);

CREATE TABLE Palestra (
    id_atividade INT PRIMARY KEY,
    titulo VARCHAR,
    nome_palestrante VARCHAR,
    instituicao VARCHAR,
    chegada TIMESTAMP,
    partida TIMESTAMP,
    FOREIGN KEY (id_atividade) REFERENCES Atividade(id_atividade)
);

CREATE TABLE Minicurso (
    id_atividade INT PRIMARY KEY,
    titulo VARCHAR,
    nome_palestrante VARCHAR,
    instituicao VARCHAR,
    taxa NUMERIC,
    vagas INT,
    FOREIGN KEY (id_atividade) REFERENCES Atividade(id_atividade)
);

CREATE TABLE Autor_Artigo (
    nome_autor VARCHAR,
    codigo_artigo INT,
    PRIMARY KEY (nome_autor, codigo_artigo),
    FOREIGN KEY (nome_autor) REFERENCES Autor(nome),
    FOREIGN KEY (codigo_artigo) REFERENCES Artigo(codigo)
);

CREATE TABLE Avaliacao (
    nome_revisor VARCHAR,
    codigo_artigo INT,
    nota NUMERIC,
    PRIMARY KEY (nome_revisor, codigo_artigo),
    FOREIGN KEY (nome_revisor) REFERENCES Revisor(nome),
    FOREIGN KEY (codigo_artigo) REFERENCES Artigo(codigo)
);

CREATE TABLE Apresentacao (
    id_sessao INT,
    codigo_artigo INT UNIQUE,
    ordem INT,
    PRIMARY KEY (id_sessao, codigo_artigo),
    FOREIGN KEY (id_sessao) REFERENCES Sessao(id_atividade),
    FOREIGN KEY (codigo_artigo) REFERENCES Artigo(codigo)
);

CREATE TABLE Inscricao (
    email_participante VARCHAR PRIMARY KEY,
    FOREIGN KEY (email_participante) REFERENCES Participante(email)
);

CREATE TABLE Inscricao_Minicurso (
    email_participante VARCHAR,
    id_minicurso INT,
    PRIMARY KEY (email_participante, id_minicurso),
    FOREIGN KEY (email_participante) REFERENCES Participante(email),
    FOREIGN KEY (id_minicurso) REFERENCES Minicurso(id_atividade)
);

CREATE TABLE Assunto (
    nome VARCHAR PRIMARY KEY
);

CREATE TABLE Artigo_Assunto (
    codigo_artigo INT,
    nome_assunto VARCHAR,
    PRIMARY KEY (codigo_artigo, nome_assunto),
    FOREIGN KEY (codigo_artigo) REFERENCES Artigo(codigo),
    FOREIGN KEY (nome_assunto) REFERENCES Assunto(nome)
);

CREATE TABLE Revisor_Assunto (
    nome_revisor VARCHAR,
    nome_assunto VARCHAR,
    PRIMARY KEY (nome_revisor, nome_assunto),
    FOREIGN KEY (nome_revisor) REFERENCES Revisor(nome),
    FOREIGN KEY (nome_assunto) REFERENCES Assunto(nome)
);

CREATE TABLE Submissao_Final (
    codigo_artigo INT PRIMARY KEY,
    nome_arquivo VARCHAR,
    enviado BOOLEAN,
    FOREIGN KEY (codigo_artigo) REFERENCES Artigo(codigo)
);