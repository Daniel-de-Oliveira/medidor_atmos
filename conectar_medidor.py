from aquisicao_dados import on_connect,on_message
import paho.mqtt.client as mqtt
from interacao_banco import criar_db,criar_tabela
from parametros_banco import config

criar_db(config['pguser'],
                    config['pgpw'],
                    config['pghost'],
                    config['pgport'],
                    config['pgdb'])
criar_tabela()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


client.connect("broker.hivemq.com", 1883, 60) 

client.loop_forever()



