from elasticsearch import Elasticsearch

es = Elasticsearch("192.168.0.23:9200")

def indexar(nome_index, documento):
    if type(documento) == type(tuple()):
        doc, rot = documento
        indexacao = es.index(index=nome_index, body=doc, routing=rot)
        print(indexacao)
    else:
        indexacao = es.index(index=nome_index, body=documento)
        print(indexacao)
