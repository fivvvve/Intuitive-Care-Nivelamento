SELECT op.registro_ans, razao_social, cnpj, nome_fantasia, despesa FROM (
	SELECT registro_ans, -SUM(vl_saldo_final - vl_saldo_inicial) AS despesa FROM demonstracoes_contabeis AS dc WHERE
	descricao = 'EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA À SAÚDE' AND
	data >= DATE_TRUNC('quarter', CURRENT_DATE) - INTERVAL '3 months' AND
	data < DATE_TRUNC('quarter', CURRENT_DATE)
	GROUP BY registro_ans
) AS desp JOIN operadoras AS op ON desp.registro_ans = op.registro_ans
ORDER BY despesa DESC
LIMIT 10;