\COPY operadoras
FROM 'file_path'
DELIMITER ';'
CSV HEADER ENCODING 'UTF8';

\COPY demonstracoes_contabeis(data, registro_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'file_path'
DELIMITER ';'
CSV ENCODING 'UTF8';