create database escola_db;

use escola_db;

  CREATE TABLE alunos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            matricula VARCHAR(50) UNIQUE NOT NULL,
            nome VARCHAR(100) NOT NULL
        );

        CREATE TABLE turmas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) UNIQUE NOT NULL,
            professor VARCHAR(100)
        );
        
	CREATE TABLE turma_aluno (
    id INT AUTO_INCREMENT PRIMARY KEY,
    turma_id INT,
    aluno_matricula VARCHAR(50),
    FOREIGN KEY (turma_id) REFERENCES turmas(id),
    FOREIGN KEY (aluno_matricula) REFERENCES alunos(matricula)
    );