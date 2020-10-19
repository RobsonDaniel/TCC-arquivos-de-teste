import paho.mqtt.client as mqtt
import json
import time
from datetime import datetime

def data_hora():
    return datetime.now().isoformat(timespec='microseconds')

dados = [
    ["ssc/201/acesso", {"permitido": True,
      "usuario": {
        "nome": "Leonardo",
        "vinculo": True,
        "registro": "1000001",
        "id": 1,
        "horario_cadastrado": "2020-05-29T01:11:04.916000",
        "horario_tag": "2019-06-28T16:26:35"
      },
      "tag": {
        "id": 5,
        "codigo": "0D00A0F859",
        "horario": "2020-05-29T01:11:04.957000"
      },
      "sala": {
        "numero": 201,
        "nome_completo": "Apartamento de Leonardo",
        "nome_curto": "APLEONARDO",
        "id": 10,
        "horario": "2020-07-22T02:19:06.517000"
      },
      "horario": data_hora()}
    ],
    ["ssc/201/acesso", {"permitido": False,
      "sala": {
        "numero": 201,
        "nome_completo": "Apartamento de Leonardo",
        "nome_curto": "APLEONARDO",
        "id": 10,
        "horario": "2020-07-22T02:19:06.517000"
      },
      "horario": data_hora()}
    ],
    ["ssc/202/acesso", {"permitido": True,
      "usuario": {
        "nome": "Marcelo",
        "vinculo": True,
        "registro": "1000002",
        "id": 2,
        "horario_cadastrado": "2020-05-29T01:11:04.916000",
        "horario_tag": "2019-06-28T16:26:35"
      },
      "tag": {
        "id": 5,
        "codigo": "0D00A0F859",
        "horario": "2020-05-29T01:11:04.957000"
      },
      "sala": {
        "numero": 202,
        "nome_completo": "Apartamento de Marcelo",
        "nome_curto": "APMARCELO",
        "id": 11,
        "horario": "2020-07-22T02:19:06.517000"
      },
      "horario": data_hora()}
    ],
    ["ssc/202/acesso", {"permitido": False,
      "sala": {
        "numero": 202,
        "nome_completo": "Apartamento de Marcelo",
        "nome_curto": "APMARCELO",
        "id": 11,
        "horario": "2020-07-22T02:19:06.517000"
      },
      "horario": data_hora()}
    ],
    ["ssc/203/acesso", {"permitido": True,
      "usuario": {
        "nome": "Alvinho",
        "vinculo": True,
        "registro": "1000004",
        "id": 4,
        "horario_cadastrado": "2020-05-29T01:11:04.916000",
        "horario_tag": "2019-06-28T16:26:35"
      },
      "tag": {
        "id": 5,
        "codigo": "0D00A0F859",
        "horario": "2020-05-29T01:11:04.957000"
      },
      "sala": {
        "numero": 203,
        "nome_completo": "Apartamento do Alvinho",
        "nome_curto": "APALVINHO",
        "id": 13,
        "horario": "2020-07-22T02:19:06.517000"
      },
      "horario": data_hora()}
    ],
    ["ssc/203/acesso", {"permitido": False,
      "sala": {
        "numero": 203,
        "nome_completo": "Apartamento do Alvinho",
        "nome_curto": "APALVINHO",
        "id": 13,
        "horario": "2020-07-22T02:19:06.517000"
      },
      "horario": data_hora()}
    ],
    ["ssc/222/acesso", {"permitido": True,
      "usuario": {
        "nome": "Lucas",
        "vinculo": True,
        "registro": "1000003",
        "id": 3,
        "horario_cadastrado": "2020-05-29T01:11:04.916000",
        "horario_tag": "2019-06-28T16:26:35"
      },
      "tag": {
        "id": 5,
        "codigo": "0D00A0F859",
        "horario": "2020-05-29T01:11:04.957000"
      },
      "sala": {
        "numero": 222,
        "nome_completo": "Apartamento de Lucas",
        "nome_curto": "APLUCAS",
        "id": 14,
        "horario": "2020-07-22T02:19:06.517000"
      },
      "horario": data_hora()}
    ],
    ["ssc/222/acesso", {"permitido": False,
      "sala": {
        "numero": 222,
        "nome_completo": "Apartamento de Lucas",
        "nome_curto": "APLUCAS",
        "id": 14,
        "horario": "2020-07-22T02:19:06.517000"
      },
      "horario": data_hora()}
    ]
]

def main(topico, mensagem):
    client = mqtt.Client()

    client.connect("broker.hivemq.com", 1883)

    client.publish(topico, mensagem)

    client.disconnect()

while True:
    for indice in range(len(dados)):
        topico, mensagem = dados[indice]
        main(topico, json.dumps(mensagem))

    #time.sleep(5)
