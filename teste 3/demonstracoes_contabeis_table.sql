CREATE TABLE demonstracoes_contabeis (
	id SERIAL PRIMARY KEY,
	data DATE NOT NULL,
	registro_ans CHAR(6) NOT NULL,
	cd_conta_contabil VARCHAR(20) NOT NULL,
	descricao VARCHAR(150) NOT NULL,
	vl_saldo_inicial FLOAT(2) NOT NULL DEFAULT 0,
	vl_saldo_final FLOAT(2) NOT NULL DEFAULT 0
)