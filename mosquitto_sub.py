import paho.mqtt.client as mqtt
from elasticSearch import indexar_documento
import formatar_dados
import json

def on_connect(client, userdata, flags, rc):
    client.subscribe("ssc/#")

def on_message(client, userdata, msg):
    topico = msg.topic
    mensagem = msg.payload

    lista_topico = topico.split('/')
    index = f"{lista_topico[0]}_{lista_topico[2]}"

    if index == 'ssc_sensor' or index == 'ssc_informacao' or (index == 'ssc_acesso' and json.loads(mensagem)['permitido'] == True):
        indexar_documento.indexar(index, formatar_dados.formatar(index, lista_topico, mensagem))

def main():
    client = mqtt.Client()

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("broker.hivemq.com", 1883)

    print("Esperando mensagens...")
    client.loop_forever()

main()
