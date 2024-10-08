create table tb_carro(
    id number generated as identity by default,
    modelo varchar2(50),
    montadora varchar2(50),
    placa varchar2(15),
    ano number,
    primary key(id)
);