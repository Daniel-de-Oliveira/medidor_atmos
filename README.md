# medidor_atmos
<p>Para importar os dados do broker para o banco de dados executar o arquivo conectar_medidor.py</p>
<p>Os parâmetros do banco de dados postgres devem ser colocados no arquivo parametros_banco.py</p>
<p>Para criar a API de requisição dos dados executar o arquivo criar_api.py</p>
<p>O teste da API pode ser feito diretamente pela documentação da API no endereco http://127.0.0.1:8000/docs#/default/read_item_medidor__mac__get ,
ou executando o arquivo chamar_api.py , que retorna a consulta em um DataFrame do pandas</p>
<p>Para executar o teste pelo arquivo chamar_api.py , coloque os parametros de mac do medidor e datas da consulta no arquivo parametros_medidor.py</p>
