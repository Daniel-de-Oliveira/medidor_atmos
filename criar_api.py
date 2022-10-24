from typing import Union
import pandas as pd
from fastapi import FastAPI
from interacao_banco import obter_dados
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"Acesse: http://127.0.0.1:8000/docs para obter a documentação da API"}

@app.get("/medidor/{mac}")
def read_item(mac: str, time_init:Union[str, None] = None, time_final:Union[str, None] = None ):
    resposta = obter_dados(mac,time_init,time_final)  
    return resposta

uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")