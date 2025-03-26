O SGBD utilizado para realizar o teste foi o PostgreSQL.

Como alguns dos dados dos arquivos de demonstrações contábeis possuíam "registros ans" que não estavam presentes na tabela de registro de operadoras, decidi remover a restrição de chave estrangeira da tabela de demonstrações contábeis. Com a restrição a tabela ficaria da seguinte forma:

CREATE TABLE demonstracoes_contabeis (
	id SERIAL PRIMARY KEY,
	data DATE NOT NULL,
	registro_ans CHAR(6) NOT NULL,
	cd_conta_contabil VARCHAR(20) NOT NULL,
	descricao VARCHAR(150) NOT NULL,
	vl_saldo_inicial FLOAT(2) NOT NULL DEFAULT 0,
	vl_saldo_final FLOAT(2) NOT NULL DEFAULT 0,
	FOREIGN KEY(registro_ans) REFERENCES operadoras (registro_ans)
)

É importante destacar que para importar os dados para as tabelas foi usado o psql no terminal Windows, para acessá-lo digite o seguinte comando no terminal 'psql postgres://<username>:<password>@<host>:<port>/<database>' e substitua por seus dados. Antes de realizar a importação das demonstrações contábeis foi necessário fazer alguns tratamentos que estão descritos a seguir.

Primeiramente, substitui as vírgulas presentes nas colunas de saldo em cada arquivo por pontos, pois o Postgres separa a parte flutuante de um número utilizando um ponto. Para isso executei o seguinte comando no diretório onde todos os arquivos csv das demonstrações contábeis estavam armazenados:
for i in ./*.csv; do     awk -F';' 'BEGIN {OFS=";"} { $5 = gensub(/,/, ".", "g", $5); $6 = gensub(/,/, ".", "g", $6); print }' "$i" > "$i.tmp" && mv "$i.tmp" "$i"; done


Segundamente, gerei um único arquivo com todos os dados dos arquivos csv, para dessa forma executar só um comando no momento em que fosse importar os dados para a tabela. No mesmo diretório dos arquivos csv executei o seguinte comando:
for i in ./*.csv; do     tail -n +2 "$i" >> all.csv; done


Por fim, executei os comandos para importar os dados para as tabelas, descritos no arquivo "import_data".