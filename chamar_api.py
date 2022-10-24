from dateutil import parser
import datetime
import requests
import pandas as pd
from parametros_medidor import params


mac=params['mac']
time_init=parser.parse(params['data_inicial'])
time_final=parser.parse(params['data_final'])

print(time_init,time_final)

parametros={'time_init':time_init,'time_final':time_final}

endereco = 'http://127.0.0.1:8000/medidor/'+mac
r = requests.get(url=endereco,params=parametros)
dados = r.json()
df=pd.read_json(dados)

print(df)