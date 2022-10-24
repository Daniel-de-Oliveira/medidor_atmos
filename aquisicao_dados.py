
import paho.mqtt.client as mqtt
from interacao_banco import inserir_registo
import json


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("/atmos-message")


def on_message(client, userdata, msg):
    
    x=str(msg.payload).lstrip("b'").rstrip("'")       
    msg_json=json.loads(x)
    inserir_registo(msg_json)
