from Busca_largura.struct import SearchTree
import json

map = None
with open("Busca_largura\infos\map.json") as mapJson:
    stringContent = mapJson.read()
    map = json.loads(stringContent)

map = dict(map)

arvoreBusca = SearchTree(map)

arvoreBusca.Buscar("A", "E")

a = {"a" : "b"}

a["b"] = "a"