import json
from datetime import datetime

def json_to_dict(str):
    return json.loads(str)

def ssc_informacao(mensagem):
    return json_to_dict(mensagem)

def ssc_sensor(lista_topico, mensagem):
    id = lista_topico[1]
    sensor = lista_topico[3]
    valor_sensor = json_to_dict(mensagem)

    documento = {
        'id': id,
        'nome_sensor': sensor,
        'valor': valor_sensor,
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # documento = {
    #     "nome_sensor": sensor,
    #     "valor": valor_sensor,
    #     "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    #     "documento": {
    #     "name": "sensor",
    #     "parent": str(id)
    #     }
    # }

    # return documento, id
    return documento

def ssc_acesso(mensagem):
    dados = json_to_dict(mensagem)

    documento = {
        "permitido": dados['permitido'],
        "usuario.nome": dados['usuario']['nome'],
        "usuario.vinculo": dados['usuario']['vinculo'],
        "usuario.registro": dados['usuario']['registro'],
        "usuario.id": dados['usuario']['id'],
        "usuario.horario_cadastrado": dados['usuario']['horario_cadastrado'],
        "usuario.horario_tag": dados['usuario']['horario_tag'],
        "tag.id": dados['tag']['id'],
        "tag.codigo": dados['tag']['codigo'],
        "tag.horario": dados['tag']['horario'],
        "sala.numero": dados['sala']['numero'],
        "sala.nome_completo": dados['sala']['nome_completo'],
        "sala.nome_curto": dados['sala']['nome_curto'],
        "sala.id": dados['sala']['id'],
        "sala.horario": dados['sala']['horario'],
        "horario": dados['horario']
    }

    return json.dumps(documento)

def formatar(index, lista_topico, mensagem):
    if index == "ssc_sensor":
        return ssc_sensor(lista_topico, mensagem)
    elif index == "ssc_informacao":
        return ssc_informacao(mensagem)
    elif index == 'ssc_acesso':
        return ssc_acesso(mensagem)
