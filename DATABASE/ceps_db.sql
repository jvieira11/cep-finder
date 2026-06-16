-- Cria tabela
CREATE TABLE consultas_cep (
	id SERIAL PRIMARY KEY,
	cep VARCHAR(9) NOT NULL,
	logradouro VARCHAR(200),
	bairro VARCHAR(100),
	cidade VARCHAR(100),
	estado VARCHAR(2),
	consultado_em TIMESTAMP DEFAULT NOW()
);