
from sqlalchemy_utils import database_exists,create_database
from parametros_banco import config
import psycopg2 as pg
import json
import pandas as pd

#CRIAR BANCO DE DADOS POSTGRES
def criar_db(user,pw,host,port,db):
    url = f'postgresql://{user}:{pw}@{host}:{port}/{db}'
    if not database_exists(url):
        create_database(url)
#CRIAR TABELA PARA IMPORTACAO DOS DADOS
def criar_tabela():
    con = pg.connect(host=config['pghost'],
                     database=config['pgdb'],
                     user=config['pguser'],
                     password=config['pgpw'])
    cur = con.cursor()
    
    sql="SELECT EXISTS (SELECT FROM pg_tables WHERE schemaname = 'public' AND tablename  = 'resposta_medidor');"
    cur.execute(sql)
    r=cur.fetchall()
    if not r[0][0]:
        with open('criar_tabela.sql') as f:
            sql = f.read()+'ALTER TABLE IF EXISTS public.resposta_medidor OWNER to {owner};'.format(owner=config['pguser'])
            cur.execute(sql)
            con.commit()
   
    cur.close()
    con.close()
#INSERIR REGISTRO DE MEDICAO
def inserir_registo(msg_json):
    mac=msg_json['mac']
    date=msg_json['date']
    rssi=msg_json['rssi']
    va=msg_json['va']
    vb=msg_json['vb']
    vc=msg_json['vc']
    ia=msg_json['ia']
    ib=msg_json['ib']
    ic=msg_json['ic']
    wa=msg_json['wa']
    wb=msg_json['wb']
    wc=msg_json['wc']
    sql=f'INSERT INTO resposta_medidor(mac,date,rssi,va,vb,vc,ia,ib,ic,wa,wb,wc) VALUES(\'{mac}\',\'{date}\',{rssi},{va},{vb},{vc},{ia},{ib},{ic},{wa},{wb},{wc});'
    con = pg.connect(host=config['pghost'],
                     database=config['pgdb'],
                     user=config['pguser'],
                     password=config['pgpw'])
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    cur.close()
    con.close()
#OBTER DADOS DO BANCO
def obter_dados(mac,time_init,time_final):
    
    con = pg.connect(host=config['pghost'],
                     database=config['pgdb'],
                     user=config['pguser'],
                     password=config['pgpw'])
    cur = con.cursor()
    sql = '''SELECT * FROM public.resposta_medidor\
 WHERE mac = '%s' and date >= '%s' and date <= '%s\'
 ORDER BY id ASC;\
 ''' % (mac,time_init,time_final)
    print(sql)
    cur.execute(sql)
    resposta=pd.DataFrame(data=cur.fetchall(),columns=['id','mac','date','rssi','va','vb','vc','ia','ib','ic','wa','wb','wc']).set_index('id').to_json()
    print(resposta)
    cur.close()
    con.close()
    return resposta

