--DESCOMENTE A LINHA ABAIXO PARA RECRIAR UMA TABELA EXISTENTE
--DROP TABLE IF EXISTS public.resposta_medidor;

CREATE TABLE public.resposta_medidor
(
    id bigserial NOT NULL,
    mac varchar(17) NOT NULL,
    date timestamp NOT NULL,
    rssi smallint,
    va numeric(6, 2),
    vb numeric(6, 2),
    vc numeric(6, 2),
    ia numeric(6, 2),
    ib numeric(6, 2),
    ic numeric(6, 2),
    wa numeric(10, 4),
    wb numeric(10, 4),
    wc numeric(10, 4),
    PRIMARY KEY (id)
);

