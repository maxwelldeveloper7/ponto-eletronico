create table colaborador(
	matricula character(6) primary key not null,
	cpf character(11) not null,
	pispasep character(11) not null,
	nome character varying not null,
	cargo character varying not null,
	admissao date not null
)